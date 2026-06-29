#!/usr/bin/env bash
# Bootstrap headless Chromium + mermaid-cli (mmdc) in the sandbox so Mermaid
# diagrams can be rendered to PNG. Idempotent: re-running is safe and fast once set up.
# Resumable Chromium download (the sandbox proxy drops large single downloads).
set -u
EXTRA="$HOME/extralibs"
PW="$HOME/.cache/ms-playwright/chromium-1223"
CHROME="$PW/chrome-linux/chrome"
CFG="/tmp/puppeteer-config.json"

arch=$(uname -m)
if [ "$arch" = "aarch64" ] || [ "$arch" = "arm64" ]; then
  ZIPNAME="chromium-linux-arm64.zip"
else
  ZIPNAME="chromium-linux.zip"
fi
URL="https://cdn.playwright.dev/dbazure/download/playwright/builds/chromium/1223/$ZIPNAME"

ok() { LD_LIBRARY_PATH="$EXTRA" "$CHROME" --headless --no-sandbox --disable-gpu --dump-dom about:blank >/dev/null 2>&1; }

if [ -x "$CHROME" ] && ok; then echo "chromium OK"; else
  echo "Downloading Chromium (resumable)..."
  python3 - "$URL" <<'PY'
import urllib.request,os,sys,time
url=sys.argv[1]; out="/tmp/chromium.zip"
req=urllib.request.Request(url,method="HEAD")
total=int(urllib.request.urlopen(req,timeout=30).headers["content-length"])
# align existing partial to 8MB boundary
have=os.path.getsize(out) if os.path.exists(out) else 0
have=(have//(8*1024*1024))*(8*1024*1024)
if os.path.exists(out): os.truncate(out,have)
f=open(out,"ab")
while have<total:
    end=min(have+8*1024*1024-1,total-1)
    r=urllib.request.Request(url,headers={"Range":f"bytes={have}-{end}"})
    try:
        d=urllib.request.urlopen(r,timeout=25).read(); f.write(d); f.flush(); have+=len(d)
    except Exception as e:
        print("retry",e,file=sys.stderr); time.sleep(1)
f.close(); print("downloaded",have,"/",total)
PY
  mkdir -p "$PW" && unzip -q -o /tmp/chromium.zip -d "$PW"
fi

# Stub libXdamage.so.1 (only undefined lib for headless chrome here)
if [ ! -f "$EXTRA/libXdamage.so.1" ] || ! ok; then
  mkdir -p "$EXTRA"
  cat > /tmp/xdamage_stub.c <<'C'
unsigned long XDamageCreate(void*d,unsigned long w,int l){return 0;}
void XDamageDestroy(void*d,unsigned long x){}
int XDamageQueryExtension(void*d,int*e,int*r){if(e)*e=0;if(r)*r=0;return 0;}
void XDamageSubtract(void*d,unsigned long a,unsigned long b,unsigned long c){}
C
  gcc -shared -fPIC -Wl,-soname,libXdamage.so.1 -o "$EXTRA/libXdamage.so.1" /tmp/xdamage_stub.c
fi

# mermaid-cli (skip its chromium download; we provide our own)
if [ ! -x /tmp/node_modules/.bin/mmdc ]; then
  echo "Installing mermaid-cli..."
  ( cd /tmp && PUPPETEER_SKIP_DOWNLOAD=1 npm install @mermaid-js/mermaid-cli puppeteer >/dev/null 2>&1 )
fi

cat > "$CFG" <<JSON
{ "executablePath": "$CHROME",
  "args": ["--no-sandbox","--disable-gpu","--disable-dev-shm-usage"] }
JSON

if ok; then echo "SETUP OK"; else echo "SETUP INCOMPLETE — re-run (download may have been interrupted)"; exit 1; fi
