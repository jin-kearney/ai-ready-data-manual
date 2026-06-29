#!/usr/bin/env python3
# Markdown -> Word(.docx) with rendered Mermaid diagrams, bordered/readable tables,
# fitted images, resolved internal anchors. Reusable engine.
import re, os, sys, json, subprocess, zipfile, shutil, tempfile

HOME=os.path.expanduser("~")
MMDC="/tmp/node_modules/.bin/mmdc"
PCFG="/tmp/puppeteer-config.json"

# ---- style knobs (tuned to match the Kearney reference .docx) ----
FONT="Noto Sans KR"          # one font for body, headings, tables AND code (reference unifies all)
TOTAL=9180; MINW=1100        # table width in dxa (~content width on Letter w/ 1in margins)
BORDER_COLOR="808080"; BORDER_SZ="4"
HEADER_FILL="DCE8F5"
BOX_BORDER="6B9AD1"; BOX_FILL="EEF4FB"   # blockquote callout box (matches diagrams)
MAXH=7680960; MAXW=5715000   # EMU caps (8.4in x 6.25in) — image fit unchanged from original
CENTER_TABLES=True           # center tables on the page (reference look)
TABLE_PCT=4800               # table width as fiftieths of a percent (4800 = 96%, slightly inset)
JUSTIFY=True                 # justify body paragraphs (both edges), like the reference
# body / heading point sizes (the reference renders these exact sizes)
BODY_PT=10                   # base body font size
H2_PT=12; H3_PT=10; H4_PT=10 # 12 / 10 / 10 pt for section / sub / sub-sub headings

strip=lambda s:re.sub(r"<[^>]+>","",s)
cells=lambda row:re.findall(r"<w:tc>.*?</w:tc>",row,re.DOTALL)

def render_mermaid(md, diagdir):
    os.makedirs(diagdir,exist_ok=True)
    env=dict(os.environ); env["LD_LIBRARY_PATH"]=HOME+"/extralibs"
    env["PUPPETEER_DISABLE_HEADLESS_WARNING"]="1"
    pat=re.compile(r"```mermaid\n(.*?)\n```",re.DOTALL)
    n=[0]
    def repl(m):
        n[0]+=1; i=n[0]
        mmd=f"{diagdir}/d{i:02d}.mmd"; png=f"{diagdir}/d{i:02d}.png"
        open(mmd,"w",encoding="utf-8").write(m.group(1))
        subprocess.run([MMDC,"-i",mmd,"-o",png,"-p",PCFG,"-b","white","-s","2"],
                       env=env,capture_output=True)
        return f"\n![]({png})\n" if os.path.exists(png) else m.group(0)
    return pat.sub(repl,md), n[0]

def gh_slug(text):
    # GitHub(gfm) heading-id algorithm: lowercase; drop chars that aren't
    # letters/numbers/space/hyphen/underscore (Unicode-aware, keeps CJK);
    # spaces -> hyphens. Used so #1-제목 TOC links keep working under the
    # pandoc `markdown` reader (which would otherwise strip leading numbers).
    t=text.lower()
    t=re.sub(r'`[^`]*`',lambda m:m.group(0).strip('`'),t)   # inline code -> text
    t=re.sub(r'[*_]','',t)                                   # emphasis markers
    t="".join(ch for ch in t if ch.isalnum() or ch in " -_")
    return t.strip().replace(" ","-")

def heading_text(raw):
    h=re.sub(r'<a id="[^"]+"></a>','',raw)
    h=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',h)   # [t](u)->t
    h=re.sub(r'[*_`]','',h)
    return h.strip()

def parse_anchors(md):
    # Return (anchor_id, heading_text) for BOTH custom <a id> anchors and the
    # gfm-style id of every heading, so all internal links resolve.
    lines=md.split("\n"); out=[]
    for i,l in enumerate(lines):
        hm=re.match(r'^#{1,6}\s+(.*)',l)
        if hm:
            ht=heading_text(hm.group(1))
            if ht: out.append((gh_slug(hm.group(1)),ht))
        for aid in re.findall(r'<a id="([^"]+)"></a>',l):
            for j in range(i,min(i+6,len(lines))):
                hm2=re.match(r'^#{1,6}\s+(.*)',lines[j])
                if hm2:
                    out.append((aid,heading_text(hm2.group(1)))); break
    return out

def cap(cx,cy):
    s=1.0
    if cy>MAXH: s=min(s,MAXH/cy)
    if cx*s>MAXW: s=min(s,MAXW/cx)
    return int(cx*s),int(cy*s)

def col_widths(rows):
    n=len(cells(rows[0]))
    if n==0: return []
    w=[0]*n
    for r in rows:
        for j,c in enumerate(cells(r)[:n]):
            w[j]=max(w[j],min(len(strip(c)),46))
    if sum(w)==0: w=[1]*n
    raw=[max(MINW,int(TOTAL*x/sum(w))) for x in w]
    s=sum(raw); wid=[int(x*TOTAL/s) for x in raw]; wid[-1]+=TOTAL-sum(wid)
    return wid

def bold_runs(cell):
    # ensure every run in header cell is bold
    def fixrun(rm):
        r=rm.group(0)
        if "<w:rPr>" in r:
            if "<w:b " not in r and "<w:b/>" not in r:
                r=r.replace("<w:rPr>","<w:rPr><w:b />",1)
        else:
            r=re.sub(r"(<w:r(?:\s[^>]*)?>)",r"\1<w:rPr><w:b /></w:rPr>",r,1)
        return r
    return re.sub(r"<w:r(?:\s[^>]*)?>.*?</w:r>",fixrun,cell,flags=re.DOTALL)

def build_tcpr(width,header):
    p='<w:tcPr><w:tcW w:type="dxa" w:w="%d" />'%width
    if header: p+='<w:shd w:val="clear" w:color="auto" w:fill="%s" />'%HEADER_FILL
    p+='<w:vAlign w:val="center" /></w:tcPr>'
    return p

def tighten_cell(body):
    # compress row height like the reference: every cell paragraph gets
    # spacing before/after = 0 (kept inside the table only, not body text).
    def fixp(pm):
        p=pm.group(0)
        if "<w:spacing " in p: return p
        if "<w:pPr>" in p:
            return p.replace("<w:pPr>","<w:pPr><w:spacing w:before=\"0\" w:after=\"0\" />",1)
        # paragraph with no pPr -> add one right after the <w:p ...> open tag
        return re.sub(r"(<w:p(?:\s[^>]*)?>)",
                      r'\1<w:pPr><w:spacing w:before="0" w:after="0" /></w:pPr>',p,1)
    return re.sub(r"<w:p(?:\s[^>]*)?>.*?</w:p>",fixp,body,flags=re.DOTALL)

def _grid_widths(tbl):
    # reuse pandoc's proportional column widths when present; else compute our own
    g=re.search(r"<w:tblGrid>(.*?)</w:tblGrid>",tbl,re.DOTALL)
    if g:
        cols=re.findall(r'<w:gridCol w:w="(\d+)"',g.group(1))
        if cols: return [int(c) for c in cols], True
    return None, False

def fix_table(tbl):
    rows=re.findall(r"<w:tr>.*?</w:tr>",tbl,re.DOTALL)
    if not rows: return tbl
    pandoc_w, have_grid = _grid_widths(tbl)
    wid = pandoc_w if have_grid else col_widths(rows)
    n=len(wid)
    if n==0: return tbl
    # tblPr: borders + cell margins (inserted before tblLook)
    borders=('<w:tblBorders>'
        +''.join('<w:%s w:val="single" w:sz="%s" w:space="0" w:color="%s" />'%(s,BORDER_SZ,BORDER_COLOR)
                 for s in ["top","left","bottom","right","insideH","insideV"])
        +'</w:tblBorders>')
    cellmar=('<w:tblCellMar><w:top w:w="40" w:type="dxa" /><w:left w:w="108" w:type="dxa" />'
             '<w:bottom w:w="40" w:type="dxa" /><w:right w:w="108" w:type="dxa" /></w:tblCellMar>')
    if "<w:tblBorders>" not in tbl:
        tbl=tbl.replace("<w:tblLook",borders+cellmar+"<w:tblLook",1)
    # width: inset to ~content width and (optionally) center, like the reference
    tbl=re.sub(r'<w:tblW w:type="(?:pct|dxa)" w:w="[0-9.]+" />',
               '<w:tblW w:type="pct" w:w="%d" />'%TABLE_PCT,tbl,1)
    if CENTER_TABLES:
        if '<w:jc ' in tbl.split("</w:tblPr>")[0]:
            tbl=tbl.replace('<w:jc w:val="start" />','<w:jc w:val="center" />',1)
        else:
            tbl=tbl.replace("</w:tblPr>",'<w:jc w:val="center" /></w:tblPr>',1)
    # empty grid (older pandoc) -> inject computed widths
    if not have_grid:
        tbl=tbl.replace("<w:tblGrid />","<w:tblGrid>"+"".join('<w:gridCol w:w="%d" />'%x for x in wid)+"</w:tblGrid>",1)
    # rebuild each row's cells: tcPr (width + header style), bold header text,
    # tight paragraph spacing; center each row so a centered table lines up.
    first=[True]
    def fr(rm):
        row=rm.group(0); cs=cells(row); newrow=row; hdr=first[0]
        if CENTER_TABLES and "<w:trPr>" not in row:
            newrow=newrow.replace("<w:tr>",'<w:tr><w:trPr><w:jc w:val="center" /></w:trPr>',1)
        for j,c in enumerate(cs):
            ww=wid[j] if j<n else wid[-1]
            body=c
            body=re.sub(r"<w:tcPr>.*?</w:tcPr>","",body,1,flags=re.DOTALL)
            body=body.replace("<w:tc>","<w:tc>"+build_tcpr(ww,hdr),1)
            body=tighten_cell(body)
            if hdr: body=bold_runs(body)
            newrow=newrow.replace(c,body,1)
        first[0]=False
        return newrow
    tbl=re.sub(r"<w:tr>.*?</w:tr>",fr,tbl,flags=re.DOTALL)
    return tbl

def pandoc_bookmark_name(ident):
    # Mirror pandoc's docx writer: Word bookmark names must start with a letter,
    # contain only [A-Za-z0-9._-], and be <=40 chars; otherwise pandoc emits
    # 'X' + sha1(ident) hex with the first hex char replaced by 'X'. We must
    # name injected bookmarks identically so the link anchors resolve.
    import hashlib
    ok = bool(ident) and ident[0].isalpha() and len(ident)<=40 and \
         all(c.isalnum() or c in ".-_" for c in ident)
    if ok: return ident
    return "X"+hashlib.sha1(ident.encode("utf-8")).hexdigest()[1:]

def inject_bookmarks(xml, anchors):
    from collections import defaultdict
    def norm(s):
        s=re.sub(r"\s+","",strip(s))
        s=re.sub(r"[‘’“”'\"`]","",s)   # quotes (pandoc smart-quotes)
        s=re.sub(r"[‐-―\-]","",s)                 # hyphens / dashes
        return s
    h2=defaultdict(list)
    for aid,ht in anchors: h2[norm(ht)].append(pandoc_bookmark_name(aid))
    existing=set(re.findall(r'w:name="([^"]+)"',xml)); bid=[7000]
    def inj(pm):
        p=pm.group(0)
        if 'w:pStyle w:val="Heading' not in p: return p
        t=norm(p)
        # exact match first (avoids a short anchor landing on the wrong heading),
        # then a contains-fallback for headings carrying extra trailing text
        ids=h2.get(t) or next((v for k,v in h2.items() if k and (t.startswith(k) or k in t)),None)
        if ids:
            adds=""
            for aid in ids:
                if aid in existing: continue
                existing.add(aid); bid[0]+=1
                adds+='<w:bookmarkStart w:id="%d" w:name="%s" /><w:bookmarkEnd w:id="%d" />'%(bid[0],aid,bid[0])
            if adds and "</w:pPr>" in p:
                return p.replace("</w:pPr>","</w:pPr>"+adds,1)
        return p
    return re.sub(r"<w:p>.*?</w:p>",inj,xml,flags=re.DOTALL)

LB_TOKEN="X0LINEBREAKX0"   # no markdown-special chars (avoid @ -> citation, etc.)

# --- sections excluded from the Word output (boilerplate, per user request) ---
# 1) the "이 가이드가 답하는 N가지 질문" callout box, 2) change-log(변경 이력 / 피드백 반영).
# (References 참고자료 is KEPT, with clickable [N] cross-links.)
# Also drops their table-of-contents links.
QUESTION_MARKERS=["이 가이드가 답하는"]

def _drop_heading(text):
    t=re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    t=re.sub(r'[*_`#]', '', t).strip()
    return ("변경 이력" in t or "변경이력" in t or "피드백" in t)

def drop_sections(md):
    lines=md.split("\n"); out=[]; i=0; n=len(lines)
    while i<n:
        line=lines[i]
        # (1) remove a contiguous blockquote block that is the question box
        if line.lstrip().startswith(">"):
            j=i; block=[]
            while j<n and lines[j].lstrip().startswith(">"):
                block.append(lines[j]); j+=1
            if any(mk in "\n".join(block) for mk in QUESTION_MARKERS):
                i=j
                if i<n and lines[i].strip()=="" : i+=1
                continue
            out.extend(block); i=j; continue
        # (2)(3) remove heading section until next heading of same/higher level
        hm=re.match(r'^(#{1,6})\s+(.*)', line)
        if hm and _drop_heading(hm.group(2)):
            lvl=len(hm.group(1)); j=i+1
            while j<n:
                hm2=re.match(r'^(#{1,6})\s+', lines[j])
                if hm2 and len(hm2.group(1))<=lvl: break
                j+=1
            # also swallow a preceding '---' rule that introduced the section
            while out and out[-1].strip() in ("","---"): out.pop()
            out.append("")  # keep one blank separator
            i=j; continue
        # drop TOC list-item links pointing to the removed sections
        if re.match(r'^\s*[-*]\s+\[', line):
            lbl=re.match(r'^\s*[-*]\s+\[([^\]]*)\]', line)
            if lbl and _drop_heading(lbl.group(1)):
                i+=1; continue
        out.append(line); i+=1
    return "\n".join(out)

def ensure_list_blanklines(md):
    # pandoc `markdown` only starts a list when a blank line precedes it; otherwise
    # "**Label**\n- item" merges into one paragraph. Insert a blank line before any
    # list that directly follows a non-blank, non-list line. Skips fenced code.
    LIST=re.compile(r'^\s*([-*+]|\d+[.)])\s+')
    out=[]; fence=False
    for line in md.split("\n"):
        if re.match(r'^\s*```', line): fence=not fence
        if (not fence and LIST.match(line) and out and out[-1].strip()!=""
                and not LIST.match(out[-1]) and not out[-1].lstrip().startswith((">","|"))):
            out.append("")
        out.append(line)
    return "\n".join(out)

def convert_inline_anchors(md):
    # Inline HTML anchors that sit *within* text (e.g. list items in References:
    # "- <a id="ref1"></a>**[1]** ...") become pandoc empty spans -> real bookmarks,
    # so body cross-links like [\[1\]](#ref1) jump to them. Standalone-on-their-own-line
    # anchors (those preceding a heading) are left for the heading-text injector.
    out=[]
    for line in md.split("\n"):
        if re.search(r'<a id="[^"]+"></a>', line) and re.sub(r'<a id="[^"]+"></a>','',line).strip():
            line=re.sub(r'<a id="([^"]+)"></a>', r'[]{#\1}', line)
        out.append(line)
    return "\n".join(out)

def clean_markdown(md):
    md=drop_sections(md)
    md=ensure_list_blanklines(md)
    md=convert_inline_anchors(md)
    # Strip Obsidian-style callout tokens like "> [!question] title" -> "> title"
    md=re.sub(r'(?m)^(>\s*)\[!\w+\]\s*', r'\1', md)
    # <br> (incl. inside pipe-table cells) -> token; restored as a real Word line
    # break after pandoc. pandoc drops raw inline HTML, so cells otherwise merge.
    md=re.sub(r'<br\s*/?>', LB_TOKEN, md)
    return md

def boxify_blockquotes(styles):
    # Render blockquotes (pandoc style "BlockText") as a bordered + shaded callout
    # box instead of an indented quote. Consecutive blockquote lines merge into one
    # box in Word (identical paragraph borders are collapsed).
    box=('<w:pPr>'
         '<w:pBdr>'
         +''.join('<w:%s w:val="single" w:sz="8" w:space="6" w:color="%s" />'%(s,BOX_BORDER)
                  for s in ["top","left","bottom","right"])
         +'</w:pBdr>'
         '<w:shd w:val="clear" w:color="auto" w:fill="%s" />'%BOX_FILL
         +'<w:spacing w:before="120" w:after="120" />'
         '<w:ind w:left="120" w:right="120" w:firstLine="0" /></w:pPr>')
    return re.sub(r'(<w:style w:type="paragraph" w:styleId="BlockText".*?)<w:pPr>.*?</w:pPr>(.*?</w:style>)',
                  lambda m:m.group(1)+box+m.group(2), styles, flags=re.DOTALL)

def set_fonts(styles):
    # Unify every font to FONT (Noto Sans KR), like the reference: body, headings,
    # tables AND code blocks. (a) docDefaults rFonts -> FONT so everything inherits;
    # (b) force FONT on the monospace code styles so JSON/code samples match too.
    def setdefault(m):
        block=m.group(0)
        if "<w:rFonts" in block:
            block=re.sub(r"<w:rFonts[^/]*/>",
                '<w:rFonts w:ascii="%s" w:eastAsia="%s" w:hAnsi="%s" w:cs="%s" />'%(FONT,FONT,FONT,FONT),
                block,1)
        else:
            block=block.replace("<w:rPr>",
                '<w:rPr><w:rFonts w:ascii="%s" w:eastAsia="%s" w:hAnsi="%s" w:cs="%s" />'%(FONT,FONT,FONT,FONT),1)
        return block
    styles=re.sub(r'<w:rPrDefault>.*?</w:rPrDefault>',setdefault,styles,1,flags=re.DOTALL)
    # code styles: replace their monospace rFonts with FONT
    for sid in ["VerbatimChar","SourceCode"]:
        def fixcode(m,_f=FONT):
            b=m.group(0)
            if "<w:rFonts" in b:
                b=re.sub(r"<w:rFonts[^/]*/>",
                    '<w:rFonts w:ascii="%s" w:eastAsia="%s" w:hAnsi="%s" w:cs="%s" />'%(_f,_f,_f,_f),b)
            return b
        styles=re.sub(r'<w:style [^>]*w:styleId="%s".*?</w:style>'%sid,fixcode,styles,flags=re.DOTALL)
    return styles

def set_heading_sizes(styles):
    # match the reference's rendered heading sizes: H2=12pt, H3=10pt, H4=10pt.
    # also make H4 bold + non-italic (reference style).
    plan={"Heading2":H2_PT*2,"Heading3":H3_PT*2,"Heading4":H4_PT*2}
    for sid,hp in plan.items():
        def fix(m,_hp=hp,_h4=(sid=="Heading4")):
            b=m.group(0)
            if "<w:sz " in b: b=re.sub(r'<w:sz w:val="\d+" />','<w:sz w:val="%d" />'%_hp,b)
            else: b=b.replace("<w:rPr>",'<w:rPr><w:sz w:val="%d" />'%_hp,1)
            if "<w:szCs " in b: b=re.sub(r'<w:szCs w:val="\d+" />','<w:szCs w:val="%d" />'%_hp,b)
            if _h4:
                b=re.sub(r'<w:i />','',b); b=re.sub(r'<w:i/>','',b)   # drop italic
                if "<w:b " not in b and "<w:b/>" not in b and "<w:b />" not in b:
                    b=b.replace("<w:rPr>","<w:rPr><w:b />",1)
            return b
        styles=re.sub(r'<w:style [^>]*w:styleId="%s".*?</w:style>'%sid,fix,styles,flags=re.DOTALL)
    return styles

def justify_body(styles):
    # justify body paragraphs (both edges) like the reference; leave table cells
    # (Compact) left-aligned and headings untouched.
    if not JUSTIFY: return styles
    for sid in ["BodyText","FirstParagraph"]:
        def fix(m):
            b=m.group(0)
            if "<w:jc " in b: b=re.sub(r'<w:jc w:val="\w+" />','<w:jc w:val="both" />',b,1)
            elif "<w:pPr>" in b: b=b.replace("<w:pPr>",'<w:pPr><w:jc w:val="both" />',1)
            return b
        styles=re.sub(r'<w:style [^>]*w:styleId="%s".*?</w:style>'%sid,fix,styles,flags=re.DOTALL)
    return styles

def set_font_size(styles):
    # set base size (docDefaults) to BODY_PT; headings keep their own (set above)
    hp=str(BODY_PT*2)  # half-points
    def fix(m):
        block=m.group(0)
        block=re.sub(r'<w:sz w:val="\d+" />',   '<w:sz w:val="%s" />'%hp,   block)
        block=re.sub(r'<w:szCs w:val="\d+" />', '<w:szCs w:val="%s" />'%hp, block)
        return block
    return re.sub(r'<w:rPrDefault>.*?</w:rPrDefault>', fix, styles, flags=re.DOTALL)

def main(src, out):
    work=tempfile.mkdtemp(prefix="md2docx_")
    diag=work+"/diagrams"
    md=clean_markdown(open(src,encoding="utf-8").read())
    md2,ndia=render_mermaid(md,diag)
    anchors=parse_anchors(md)
    wm=work+"/in.md"; open(wm,"w",encoding="utf-8").write(md2)
    tmp_docx=work+"/out.docx"
    # `markdown` reader (not gfm): renders **bold** correctly even when followed
    # by a Korean particle (gfm/CommonMark flanking leaves the ** literal there).
    # -implicit_figures: render images inline without a figure caption
    subprocess.run(["pandoc",wm,"-f","markdown-tex_math_dollars-raw_tex-citations-implicit_figures",
                    "-t","docx","-o",tmp_docx],check=True)
    up=work+"/unp"; os.makedirs(up)
    with zipfile.ZipFile(tmp_docx) as z: z.extractall(up)
    docp=up+"/word/document.xml"; xml=open(docp,encoding="utf-8").read()
    # restore <br> line breaks (token -> real Word break, splitting the text run)
    xml=xml.replace(LB_TOKEN,'</w:t><w:br /><w:t xml:space="preserve">')
    # image fit
    xml=re.sub(r'<wp:extent cx="(\d+)" cy="(\d+)"',lambda m:'<wp:extent cx="%d" cy="%d"'%cap(int(m.group(1)),int(m.group(2))),xml)
    xml=re.sub(r'<a:ext cx="(\d+)" cy="(\d+)"',lambda m:'<a:ext cx="%d" cy="%d"'%cap(int(m.group(1)),int(m.group(2))),xml)
    # tables
    xml=re.sub(r"<w:tbl>.*?</w:tbl>",lambda m:fix_table(m.group(0)),xml,flags=re.DOTALL)
    # bookmarks
    if anchors: xml=inject_bookmarks(xml,anchors)
    open(docp,"w",encoding="utf-8").write(xml)
    # fonts, sizes, justification, callout boxes
    sp=up+"/word/styles.xml"
    if os.path.exists(sp):
        st=open(sp,encoding="utf-8").read()
        st=set_fonts(st); st=set_font_size(st); st=set_heading_sizes(st)
        st=justify_body(st); st=boxify_blockquotes(st)
        open(sp,"w",encoding="utf-8").write(st)
    # png default content type
    ctp=up+"/[Content_Types].xml"; ct=open(ctp,encoding="utf-8").read()
    if 'Default Extension="png"' not in ct:
        ct=ct.replace('<Default Extension="rels"','<Default Extension="png" ContentType="image/png" /><Default Extension="rels"',1)
        open(ctp,"w",encoding="utf-8").write(ct)
    # repack
    if os.path.exists(out): os.remove(out)
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        z.write(ctp,"[Content_Types].xml")
        for dp,_,fs in os.walk(up):
            for f in fs:
                full=os.path.join(dp,f); rel=os.path.relpath(full,up)
                if rel=="[Content_Types].xml": continue
                z.write(full,rel)
    print(f"OK: {out} (diagrams={ndia}, anchors={len(anchors)})")
    shutil.rmtree(work,ignore_errors=True)

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])
