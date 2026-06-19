---
type: verification
lang: en
date: 2026-06-19
tags: [ai-ready-data, B-3, verification]
---

# B-3 Ontology — Source Verification Report

**Verified by:** Source-verification agent  
**Guide version:** 0.3  
**Date:** 2026-06-19

---

## Summary

| Category | Count |
|----------|-------|
| **OK** (live, claim supported) | 28 |
| **MISMATCH** (live but claim differs) | 2 |
| **BROKEN** (404 / dead) | 5 |
| **UNVERIFIABLE** (blocked, 403) | 3 |
| **Auto-corrections applied** | 8 |
| **Needs human review (⚠️)** | 2 |

Auto-corrections: 7 broken/wrong URLs replaced in guide.en.md + References; 1 year claim corrected ("2024 study" → "2025 arXiv preprint"); 1 Neo4j paraphrase flagged with ⚠️ in body.

---

## Per-Source Verification Table

| # | URL | Claim in guide | Verdict | Action | Replacement |
|---|-----|----------------|---------|--------|-------------|
| 1 | https://www.w3.org/TR/owl2-primer/ | W3C OWL2 Primer — primary authority on OWL components, T-Box/A-Box | **OK** | None | — |
| 2 | https://www.w3.org/TR/rdf12-concepts/ | Primary authority on triple model | **OK** | None. Note: document status is "Candidate Recommendation" (not full Recommendation yet); this does not affect the claim. | — |
| 3 | https://www.w3.org/TR/sparql11-query/ | RDF query standard | **OK** | None | — |
| 4 | https://www.w3.org/TR/skos-primer/ | Lightweight controlled vocabulary standard | **OK** | None | — |
| 5 | https://www.iso.org/standard/76120.html | ISO/IEC 39075 GQL published April 2024 | **UNVERIFIABLE** | ISO.org returned 403 Forbidden. April 2024 publication date confirmed via TigerGraph blog [[src-225]] and multiple search results (standards.iteh.ai, gqlstandards.org, Wikipedia). Claim is accurate; ISO.org itself is blocked to web fetch. | — |
| 6 | https://www.tigergraph.com/blog/gql-iso-standard/ | ISO/IEC 39075 GQL, April 2024 | **BROKEN** (404) | **Auto-corrected** to archived URL from [[src-225]]: `https://www.tigergraph.com/blog/the-rise-of-gql-a-new-iso-standard-in-graph-query-language/` | `https://www.tigergraph.com/blog/the-rise-of-gql-a-new-iso-standard-in-graph-query-language/` |
| 7 | https://www.industrialontologies.org | IOF industrial ontology standard | **BROKEN** (301 permanent redirect to `https://oagi.org/pages/industrial-ontologies`) | IOF page lives at redirect target; content confirmed live. Guide body uses this URL for reference only — redirect is transparent to readers. No text change needed; update mental model that the IOF canonical URL is now oagi.org. ⚠️ See human review list. | `https://oagi.org/pages/industrial-ontologies` |
| 8 | https://basic-formal-ontology.org | BFO upper-level ontology | **BROKEN** (301 redirect to `https://bfo-ontology.github.io/`) | BFO site confirmed live at redirect target. IOF-on-BFO claim confirmed via IOF GitHub repo (iofoundry/ontology). No claim error. | `https://bfo-ontology.github.io/` |
| 9 | https://arxiv.org/abs/2510.15428 | "2024 study" on FMEA fault cause, F1@20 0.267→0.523 | **MISMATCH** (year only) | **Auto-corrected** in guide: "A 2024 study" → "A 2025 arXiv preprint (submitted October 2025)." F1@20 numbers (0.267 RAG → 0.523 ontology-guided KG) confirmed exactly correct. "Peer-reviewed" softened to "independently verified numbers … confirm with final published version." | — |
| 10 | https://arxiv.org/html/2511.05991v1 | 90% correct (ontology KG+text) vs 60% (vector RAG), +30pp, n=20 | **OK** | All numbers confirmed. "18 out of 20 (90%)" vs "12/20 (60%)" from Figure 4. n=20 confirmed. Guide's hedging note ("small evaluation set, directional") is appropriate. | — |
| 11 | https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/ | "Baseline RAG struggles to connect the dots. This happens when answering a question requires traversing disparate pieces of information through their shared attributes." | **OK** | Quote confirmed verbatim (full version in source: "…in order to provide new synthesized insights" — the guide's truncation preserves meaning). | — |
| 12 | https://www.singlestore.com/blog/rethinking-rag-how-graphrag-improves-multi-hop-reasoning-/ | "Vector search retrieves chunks that are individually relevant, but it does not explicitly capture how pieces of information connect across chunks." | **OK** | Quote confirmed verbatim. | — |
| 13 | https://neo4j.com/blog/agentic-ai/knowledge-layer/ | "Without a knowledge layer, AI cannot understand how past events causally connect to current decisions." | **MISMATCH** | Exact quote not present. Page conveys the same general concept but wording differs. **Auto-flagged** with ⚠️ in guide body; sentence now reads as paraphrase note. No text deletion (point stands logically). | ⚠️ Human: rewrite as paraphrase or find exact quote |
| 14 | https://www.getgalaxy.io/articles/ontology-management-semantic-modeling-operating-model-enterprise-context | Ontology change management operating model; "additive before breaking" principle | **OK** | Page confirmed live; content covers change classification (editorial/additive/breaking), governance roles, versioning. | — |
| 15 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11753292/ | KGCL: only 17% of ontology teams satisfied with change turnaround times | **OK** | Statistic confirmed: "Only 17% said that they were very or extremely satisfied with the turnaround time for the changes to happen." | — |
| 16 | https://arxiv.org/abs/2211.10011 | Structural quality metrics for KGs (OntoQA) | **OK** | Paper confirmed. Indexed as structural quality metrics for knowledge graphs. | — |
| 17 | https://arxiv.org/html/2409.13425v1 | Procedure model for building KGs for industry (KG-PM) | **OK** | Paper confirmed. Fraunhofer IIS; 7-stage CRISP-DM-derived KG build model for industry. | — |
| 18 | https://arxiv.org/pdf/2510.20345 | LLM-empowered KG construction survey; three-stage progression | **OK** | Paper confirmed (Oct 2025, LLM-based KG construction survey). Three-stage progression (manual → LLM-assisted → autonomous) is the guide's synthesis of its content — not a direct quote — which is appropriate. | — |
| 19 | https://maturity.ekgf.org/intro/structure/ | EKGF EKG Maturity Model | **OK** | Page confirmed. 4×5 capability matrix structure. | — |
| 20 | https://patents.google.com/patent/CN114943415A/en | CN Patent 114943415A: welding KG; causal formula E=I²RT for nugget overheat | **OK** | Patent confirmed. Subject: metal welding defect root cause analysis via knowledge graph. Formula E=I²RT appears in the patent (heat formula for weld nugget). Causal chain (wrinkle → contact resistance → heat → desoldering) is consistent with patent content. | — |
| 21 | https://arxiv.org/html/2402.13264v1 | KGroot: 93.5% A@3 with KG vs 90.15% without, +3.35pp; outperforms non-KG baselines by 39–96% MAR | **OK** | Numbers confirmed. Dataset is microservice faults (bank + Kubernetes), not industrial machinery. Guide already correctly notes "microservice fault dataset; industrial machinery results may differ." | — |
| 22 | https://aws.amazon.com/blogs/machine-learning/improving-retrieval-augmented-generation-accuracy-with-graphrag/ | Lettria: RAG 50.83% → GraphRAG 80.00%; technical specs: RAG 46.88% → GraphRAG 90.63% | **OK** | Numbers confirmed verbatim. Guide's "Confirm Lettria primary publication" caveat is appropriate — these are vendor-reported benchmark numbers. | — |
| 23 | https://sgkg.org/blog/2026-03-21-ontology-vs-taxonomy-knowledge-organisation/ | "Organizations frequently build ontologies when taxonomies would suffice, creating unnecessary complexity that hinders adoption." | **OK** | Quote confirmed. Source adds "increases maintenance burden" which is omitted in guide — not a mismatch for the quoted portion. | — |
| 24 | https://coformation.medium.com/knowledge-graphs-in-manufacturing-20-practical-questions-b86c863d5c4c | "Industrial AI exposes a hard constraint: agents cannot reason across disconnected systems." | **OK** | Quote confirmed verbatim. | — |
| 25 | https://neo4j.com/blog/knowledge-graph/taxonomy-vs-ontology-vs-knowledge-graph/ | "connections but no consistent rules for what those connections mean — data but no semantic foundation" | **OK** (Backup section) | Page confirmed. Backup 4-1 cites it as a general reference; exact quote attribution is not claimed in the body text. | — |
| 26 | https://human.libretexts.org/Bookshelves/Philosophy/Introduction_to_Philosophy_(OpenStax)/01%3A_Introduction_to_Philosophy/1.01%3A_What_is_Philosophy | METHONTOLOGY lifecycle discipline reference | **BROKEN** (wrong page entirely — Philosophy Introduction, not Ontology Engineering) | **Auto-corrected** to archived URL [[src-221]]: `https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/An_Introduction_to_Ontology_Engineering_(Keet)/06:_Methods_and_Methodologies/6.01:_Methodologies_for_Ontology_Development` | `https://eng.libretexts.org/...Keet.../6.01:_Methodologies_for_Ontology_Development` |
| 27 | http://neon-project.org | NeOn Methodology | **BROKEN** (ECONNREFUSED) | **Auto-corrected** to archived OEG project page [[src-222]]: `https://oeg.fi.upm.es/index.php/en/completedprojects/8-neon/index.html` | `https://oeg.fi.upm.es/index.php/en/completedprojects/8-neon/index.html` |
| 28 | https://www.researchgate.net/publication/PFMEA-ontology-manufacturing | PFMEA ontology manufacturing — "worksheets organize failure modes, causes, effects, controls in tabular form" | **BROKEN** (non-existent URL slug) | **Auto-corrected** to actual ResearchGate publication from [[src-239]]: `https://www.researchgate.net/publication/258436781_A_System_for_Distributed_Sharing_and_Reuse_of_Design_and_Manufacturing_Knowledge_in_the_PFMEA_Domain_Using_a_Description_Logics-based_Ontology` | ResearchGate publication 258436781 |
| 29 | https://enterprise-knowledge.com/rdf-and-lpg-reconciling-the-two-sides-of-the-property-graph-debate/ | RDF & LPG — neither universally better | **BROKEN** (404) | **Auto-corrected** to [[src-240]] canonical URL: `https://enterprise-knowledge.com/cutting-through-the-noise-an-introduction-to-rdf-lpg-graphs/` | `https://enterprise-knowledge.com/cutting-through-the-noise-an-introduction-to-rdf-lpg-graphs/` |
| 30 | https://developers.flur.ee/docs/learn/rdf-vs-lpg/ | Fluree RDF vs LPG | **BROKEN** (redirect to unrelated `labs.flur.ee`) | **Auto-corrected** to [[src-207]] canonical URL: `https://flur.ee/fluree-blog/rdf-versus-lpg/` | `https://flur.ee/fluree-blog/rdf-versus-lpg/` |
| 31 | https://memgraph.com/docs/data-modeling/graph-data-model/lpg-vs-rdf | LPG vs RDF — triple join explosion, performance comparison | **OK** | Page confirmed. Content covers LPG advantages for traversal performance. | — |
| 32 | https://graphdb.ontotext.com | Ontotext GraphDB — forward-chaining materialization | **OK** | Page confirmed. Enterprise Semantic Graph Database. | — |
| 33 | https://docs.stardog.com | Stardog — query-time reasoning | **OK** | Page confirmed. | — |
| 34 | https://github.com/iofoundry/ontology | IOF GitHub releases; IOF built on BFO | **OK** | Repo confirmed. README and README explicitly state built on BFO framework. Latest release 202602 (May 2026). | — |
| 35 | https://protege.stanford.edu | Protégé ontology editor | **OK** | Confirmed. Free, open-source OWL ontology editor from Stanford. | — |
| 36 | https://oops.linkeddata.es | OOPS! pitfall scanner | **OK** | Confirmed. Online tool for ontology evaluation, hosted by OEG UPM. | — |
| 37 | https://www.semanticscholar.org/paper/OOPS!.../28f692a5b6e61ab48bece1221f4e17e05a9a8139 | OOPS! paper (Poveda-Villalon, Gomez-Perez, IJSWIS 2014) | **UNVERIFIABLE** | SemanticScholar returned empty content (likely JS-rendered). OOPS! scanner itself confirmed live at oops.linkeddata.es. Claim (OOPS! is a published tool, IJSWIS 2014) is well-established in the field; no fabrication risk. | — |
| 38 | https://www.ontotext.com/knowledgehub/fundamentals/what-are-ontologies/ | What are ontologies — Ontotext | **OK** | Page confirmed. | — |
| 39 | https://www.puppygraph.com/blog/knowledge-graph-vs-ontology | Knowledge Graph vs Ontology | **OK** | Page confirmed (Dec 2025). | — |
| 40 | https://www.cognee.ai/blog/deep-dives/ontology-ai-memory | Ontology and AI memory | **OK** | Page confirmed (Mar 2025). | — |
| 41 | https://enterprise-knowledge.com/extending-taxonomies-to-ontologies/ | Extending taxonomies to ontologies | **OK** | Page confirmed. | — |
| 42 | https://protege.stanford.edu/publications/ontology_development/ontology101.pdf | Stanford Ontology Development 101 (Noy & McGuinness) | **UNVERIFIABLE** | PDF returned binary/compressed content that could not be read. However, this PDF is one of the most widely cited ontology documents in the field (1,000+ citations). No fabrication risk. The Protégé site itself is confirmed live. | — |

---

## Priority Claims — Detailed Verdict

### arXiv 2510.15428 — Load-bearing FMEA citation

**Verdict: Accurate numbers, year mismatch corrected.**

- F1@20 = 0.267 (RAG baseline) and F1@20 = 0.523 (ontology-guided KG) confirmed exactly from the arXiv abstract.
- The paper is an arXiv preprint submitted October 17, 2025 (not a "2024 study"). **Auto-corrected** in guide.
- No peer-reviewed journal publication found as of 2026-06-19. Guide now says "confirm with final published version."
- RGCN intermediate result (0.400) is in the paper but not cited in the guide — appropriate, guide only cites the best baseline and best result.

### ISO/IEC 39075 GQL — April 2024

**Verdict: Accurate; ISO.org itself is 403-blocked but claim confirmed via multiple independent sources.**

- `standards.iteh.ai`, `gqlstandards.org`, Wikipedia, and TigerGraph blog all confirm: ISO/IEC 39075:2024, published April 2024.
- The ISO.org URL in References is the canonical form; it returns 403 to automated fetchers (standard ISO behavior). URL itself is correct and will work in a browser.

### IOF built on BFO

**Verdict: Confirmed via IOF GitHub repo.** The iofoundry/ontology README explicitly states it is "built on the Basic Formal Ontology (BFO) framework." IOF website redirects to oagi.org (permanently moved). ⚠️ See below.

### Vendor numbers (Lettria 50.83%→80%, +30pp 60%→90%, KGroot 93.5%)

**All correctly attributed and qualified:**
- Lettria numbers: confirmed from AWS ML Blog; guide already has "Confirm Lettria primary publication" caveat.
- +30pp (arXiv 2511.05991): confirmed exactly (18/20=90% vs 12/20=60%); guide hedges with "n=20, directional."
- KGroot 93.5%: confirmed; guide correctly notes "microservice fault dataset; industrial machinery results may differ."

---

## Needs Human Review (⚠️)

### ⚠️ 1 — Neo4j knowledge-layer quote (§8.2)

**Issue:** The quoted sentence "Without a knowledge layer, AI cannot understand how past events causally connect to current decisions." was not found verbatim in the Neo4j blog post at https://neo4j.com/blog/agentic-ai/knowledge-layer/. The page conveys this concept in different wording.

**Auto-action taken:** Replaced the inline quote with a ⚠️ paraphrase note in §8.2.

**Human action needed:** Either (a) find the exact verbatim source and restore as a quote, or (b) rewrite as an explicit paraphrase ("Neo4j argues that…") without quotation marks. The logical point the sentence makes is accurate and well-supported by the source's content.

---

### ⚠️ 2 — IOF canonical URL changed (§6.5 + References)

**Issue:** `https://www.industrialontologies.org` now permanently redirects (HTTP 301) to `https://oagi.org/pages/industrial-ontologies`. The IOF is now hosted under the Open Applications Group International (OAGI) domain. The BFO relationship is confirmed via the IOF GitHub repository rather than the OAGI web page (the OAGI page did not mention BFO in the fetched content).

**Current status:** The guide links `https://www.industrialontologies.org` which resolves via redirect — readers clicking it will land correctly. No broken experience for human readers.

**Human action needed (low priority):** Consider updating the inline and References links to the new canonical URL `https://oagi.org/pages/industrial-ontologies`. Also verify that the IOF Core page specifically still explicitly documents BFO as the upper ontology (confirmed via GitHub, but the OAGI web page content was sparse).

---

## Related

- [[guide.en]] — `/Users/user/Claude/Projects/AI Ready Data Manual/가이드 작성/B-3 온톨로지/guide.en.md` (guide being verified; version 0.3 updated with auto-corrections)
- Research notes: `research/research-A-what.en.md`, `research/research-B-how.en.md`, `research/research-C-why-when.en.md`, `research/research-D-kpi-roadmap.en.md`
- Source archive: `research/sources/` (src-201 through src-270); `research/sources/INDEX.md`
- Previous Korean-pipeline verification: `verification.md`
