---
type: research
lang: en
date: 2026-06-19
tags: [kpi, roadmap, ontology-evaluation, quality-metrics, maturity-model, knowledge-graph, shacl, oops, ontoqa, ekgf, iof, rag, root-cause-analysis, change-management]
cluster: D — KPI + Roadmap
topic: B-3 Ontology
perspective: Preparing data FOR AI (not building AI)
---

# B-3 Ontology — Research Cluster D: KPI + Roadmap

> **Perspective lock**: All KPIs measure the quality, coverage, and usage of the ontology as a *data asset*. The roadmap describes how ontology *preparation* scales over time. Neither section addresses building AI models.

---

## 1. KPI Framework — Measuring Ontology Quality and Value

### 1.1 Theoretical Grounding: Quality Dimensions (Consensus)

Multiple independent surveys [[src-263]] [[src-264]] converge on six core quality dimensions for knowledge graphs and ontologies:

| Dimension | Plain meaning | Primary measurement method |
|-----------|--------------|---------------------------|
| **Completeness** | Does the ontology cover all intended concepts and relations? | CQ answerability rate; coverage % vs. scope inventory |
| **Accuracy** | Are facts correct? Are class/relation definitions sound? | Expert sampling; gold-standard comparison; OWL reasoner |
| **Consistency** | No internal contradictions or logical conflicts | OWL reasoner satisfiability; SHACL constraint pass rate |
| **Conciseness** | No redundancy; no duplicate/obsolete concepts | Orphan concept count; synonym consolidation audit |
| **Timeliness** | Is the ontology current with the domain? | Staleness flag rate; time since last review |
| **Availability / Usability** | Can downstream consumers find and use the ontology? | Query response SLA; reuse count across systems |

**Source authority**: Wang et al. KG quality model (6 dimensions), cited in [[src-264]]; extended 11-dimension model in [[src-263]].

---

### 1.2 Structural Metrics: OntoQA Framework

The **OntoQA** framework (Tartir & Arpinar) [[src-261]] defines three classes of schema metrics widely used in the literature:

#### Schema Metrics
| Metric | Formula | What it measures |
|--------|---------|-----------------|
| **Relationship Richness (RR)** | `RR = |P| / (|SC| + |P|)` where P = non-is-a relations, SC = subclasses | Proportion of relations beyond taxonomy; richer ontologies have higher RR |
| **Attribute Richness (AR)** | `AR = |AT| / |C|` where AT = total attributes across all classes, C = class count | Average knowledge density per concept |
| **Inheritance Richness (IR)** | `IR = |S| / |C|` where S = subclasses | Average depth of classification |

A higher RR is generally desirable for ontologies intended to support causal reasoning (manufacturing fault diagnosis, PFMEA). An ontology that is only a taxonomy (RR ≈ 0) cannot support relational queries.

#### Instance / Connectivity Metrics [[src-261]]
- **Class Instantiation (CI)**: % of defined classes that have at least one A-Box instance — measures whether the schema is actually used
- **Subclass Property Instantiation (SPI)**: % of subclasses that use inherited properties — measures inheritance effectiveness
- **Average Relations per Concept** (graph density): mean number of edges per node in the ontology graph

#### Orphan Concept Count [[src-261]] [[src-262]]
An *orphan* (isolated node) is a defined concept not connected to any other concept by any relation (neither subject nor object in any triple). OOPS! Pitfall P4 ("creating unconnected ontology elements") classifies this as a structural quality failure. Zero orphan concepts is a reasonable target.

---

### 1.3 OOPS! Pitfall Evaluation Framework

**OOPS! (OntOlogy Pitfall Scanner!)** [[src-262]] provides a catalogue of **41 pitfalls** across three categories:

| Level | Example pitfalls | Impact on KPI |
|-------|-----------------|---------------|
| **Critical** | Missing domain/range declarations; wrong inverse relations; untyped classes | Ontology reasoning fails; T-Box unusable by AI reasoner |
| **Important** | Missing disjointness; unconnected elements (orphan concepts); creating cycles | Suboptimal reasoning; incomplete query results |
| **Minor** | Inconsistent naming conventions; missing annotations | Usability degradation; poor maintainability |

A **OOPS!/SHACL constraint validation pass rate** = % of critical + important pitfall categories with zero violations in the current ontology version — directly operationalizable as a KPI. The SHACLEval study [[src-262 indirect]] found 145,910 violations across 416 non-conformant ontologies in a corpus of 868 vocabularies, confirming widespread real-world quality gaps.

---

### 1.4 Coverage Metric Design

Coverage is domain-specific and requires a scope inventory. Two complementary measurements:

#### A. Concept Coverage
```
Concept Coverage (%) = (Concepts modeled in ontology / Target concepts in domain scope) × 100
```
- Requires: pre-defined scope inventory (e.g., 50 core manufacturing fault types for quality root-cause domain)
- Target in PoC: organizations typically set 70–80% as initial milestone; 90%+ as mature target
- ⚠ Caution: No universal benchmark exists — set targets in PoC based on domain inventory

#### B. Document Mapping Coverage
```
Document Mapping Coverage (%) = (SOP / PFMEA / C-S documents with ≥1 concept mapped to ontology / Total target documents) × 100
```
- Source of concept scope: SOP / PFMEA / Control-Standard documents (manufacturing)
- Identifies which documents are "ontology-covered" vs. "dark data" not yet integrated

**Academic reference for coverage concept**: Scope coverage defined as "the percentage of broad semantic topics covered by the ontology" in ontology evaluation literature; relational coverage measured by "evaluation methods that compare semantic relations of established knowledge resources" [[src-261]].

---

### 1.5 AI-Usage Value: Retrieval and Reasoning Improvement

#### Finding 1: Ontology-Guided RAG vs. Vector Baseline [[src-267]]
A 2024 comparative study (20-question evaluation, grant application domain):
- Vector RAG (keyword baseline): **60% correct**
- Ontology KG + text chunks: **90% correct** → **+30 percentage-point improvement**
- Ontology KG without text chunks: **15–20% correct** — *worse* than baseline

**Critical insight**: The improvement requires ontology + textual evidence. Structural ontology alone degrades performance. This is a design requirement for how the ontology data asset is prepared, not just modeled.

**⚠ Caution**: Small evaluation set (n=20); single domain; results are directional. Organizations should run domain-specific PoC measurements. Do not assert the +30 pp figure as a guaranteed outcome.

#### Finding 2: KG-Enhanced Root Cause Analysis in Manufacturing [[src-266]]
KGroot study (production microservice fault diagnosis):
- KGroot with KG: **93.5% A@3 accuracy** (top-3 root cause identification)
- KGroot without KG component: **90.15% A@3** → KG adds +3.35 pp
- Outperforms non-KG baselines by 39–96% on Mean Average Rank

**⚠ Caution**: Specific microservice fault dataset (Dataset B). Industrial machinery datasets may differ. Present as "PoC measurement approach" not a universal target.

#### Measurement Approach for AI-Usage KPI
Rather than committing to specific numbers, define the measurement method:
1. Define a set of domain-specific test questions (root-cause / analytical / relational)
2. Run against: (a) keyword search, (b) vector RAG, (c) ontology-augmented retrieval
3. Score: % of questions answered correctly (manual evaluation) or precision@K
4. Track improvement over time as ontology coverage grows

---

### 1.6 Operational Metrics: Change Management

#### Survey Evidence for Operations Pain Point [[src-268]]
From the KGCL (Knowledge Graph Change Language) community survey:
- **82%** rated staying informed about ontology changes as "extremely or very important"
- Only **8%** were satisfied with existing change visualization methods
- Only **17%** were satisfied with change request turnaround times

The 17% satisfaction figure is strong evidence that **change request turnaround SLA** is a genuine operational pain point and meaningful KPI.

#### Change Tier Framework [[src-270]]
| Change type | Examples | Suggested SLA (PoC target) |
|-------------|----------|---------------------------|
| Editorial | Label correction, definition wording | 1–3 business days |
| Additive | New class, new property | 1–2 weeks; steward sign-off |
| Breaking | Redefine existing concept, rename | Governance board review; 3–4 weeks |

**Note**: These SLA tiers are suggested PoC targets, not industry-standard benchmarks. Organizations should set their own based on operational context.

#### Additional Operations Metrics [[src-268]] [[src-270]]
- **Version adoption rate**: % of downstream systems on current ontology version
- **Deprecation window compliance**: % of teams completing migration within stated timeline
- **Metric drift incidents**: cases where two reports show different numbers due to ontology divergence (measured by user-reported data inconsistency tickets)

---

### 1.7 Five Recommended KPIs (Guide Writer Selection)

The following five KPIs are grounded in the literature and operationalizable for a manufacturing enterprise context:

| # | KPI Name | One-line meaning | Direction | How measured | Primary source |
|---|----------|-----------------|-----------|-------------|----------------|
| **KPI-1** | Concept Coverage Rate | % of in-scope domain concepts modeled in the ontology | ↑ (target: 80%+ in PoC) | Scope inventory count ÷ modeled concept count | [[src-261]] [[src-263]] |
| **KPI-2** | Constraint Validation Pass Rate | % of critical + important OOPS!/SHACL pitfall checks passing (zero violations) | ↑ (target: 100% critical; 90%+ important) | OOPS! scan + SHACL shapes run on ontology | [[src-262]] [[src-264]] |
| **KPI-3** | Orphan Concept Count | Number of concepts with no relations (isolated nodes) | ↓ (target: 0) | Graph query: nodes with degree = 0 | [[src-261]] [[src-262]] |
| **KPI-4** | AI Retrieval Improvement | % improvement in domain-specific Q&A accuracy vs. keyword baseline | ↑ (measure in PoC; direction goal: positive) | Domain test-set evaluation; manual scoring | [[src-266]] [[src-267]] |
| **KPI-5** | Change Request Turnaround | Average business days from change request submission to approved update by tier | ↓ (target: SLA compliance ≥ 90%) | Governance ticket system timestamps | [[src-268]] [[src-270]] |

**Additional candidates** (gather in PoC, promote as maturity grows):
- Relationship Richness (RR) — monitor directional improvement as ontology deepens
- Document Mapping Coverage — % of SOPs/PFMEAs/C-S docs with mapped concepts
- Reuse Rate — number of affiliates/systems consuming the ontology
- Version adoption rate — % of consumers on current version

---

## 2. Roadmap — Ontology Preparation Maturity Stages

### 2.1 Reference Framework: Three-Stage Progression [[src-269]]

The LLM-empowered KG construction survey (arXiv 2510.20345) identifies a clear three-stage progression in the field:

| Stage | Ontology engineering mode | Knowledge extraction | Current availability |
|-------|--------------------------|---------------------|---------------------|
| **Manual** | Strong human supervision; specialist-only | Handcrafted rules, pattern matching | Widely deployed |
| **Semi-automated (LLM-assisted)** | Human at critical checkpoints; LLM drafts concepts | Schema-driven LLM extraction; LLM CQ formulation | Emerging in production |
| **Autonomous** | LLMs as adaptive reasoning agents; continuous maintenance | Schema-free autonomous inference + schema generation | Research stage |

This three-stage progression is the backbone of the roadmap narrative.

---

### 2.2 EKG Maturity Model Alignment [[src-265]]

The EKGF EKG Maturity Model (v1.0) provides a 4-pillar × 5-level structure. Mapping ontology preparation to EKG/MM levels:

| EKG/MM Level | Name | Ontology preparation state |
|-------------|------|---------------------------|
| **Level 1** | EKG Initiation | First pilot T-Box for one domain (e.g., quality root-cause); manual construction; no governance |
| **Level 2** | Extensible Platform | Reusable ontology modules; multi-domain expansion; integration with catalog; semi-automated extraction |
| **Level 3** | Enterprise Ready | Cross-affiliate shared ontology + local extensions; formal governance; SHACL validation automated in CI/CD |
| **Level 4** | Strategic Asset | Ontology drives KPI definitions, AI agent tool contracts, product-process traceability; IOF alignment progressing |
| **Level 5** | Operational Ecosystem | Continuous, largely automated ontology maintenance; agent reasoning over live ontology |

---

### 2.3 Detailed Roadmap: Four Stages for Manufacturing Context

#### Stage 1 — Pilot: Single-Domain Manual T-Box (Months 0–6)

**Goal**: Establish ontology data asset for one high-value use case.

**Activities**:
- Define scope via competency questions (CQs) for one domain (e.g., "quality defect root-cause for casting line")
- Identify 30–80 core concepts from SOP/PFMEA/C-S documents for that domain
- Model T-Box manually (Protégé or equivalent); define ~3–5 key relation types beyond is-a
- Load into triple store; run OOPS! scan; achieve zero critical pitfalls
- Connect ontology to data catalog (A-Box population: tag existing data assets to ontology concepts)

**KPIs to establish baseline**:
- Concept Coverage Rate (measured against scope inventory)
- Constraint Validation Pass Rate (zero critical pitfalls)
- Orphan Concept Count (target: 0 before Stage 1 exit)
- CQ Answerability Rate: % of pilot CQs answerable via SPARQL

**Output**: Working pilot ontology; validated against domain CQs; initial KPI baseline.

---

#### Stage 2 — Expansion: Multi-Domain + Semi-Automated (Months 6–18)

**Goal**: Grow ontology coverage and reduce manual effort through LLM assistance.

**Activities**:
- Expand to 2–4 additional domains (product-process-defect, equipment-maintenance, material-specification)
- Introduce LLM-assisted concept extraction from SOP/PFMEA documents (schema-driven: LLM proposes, expert validates)
- Build governance workflow: concept change request → steward review → SHACL validation → merge
- Begin connecting ontology to data catalog metadata, master data, and lineage records
- Start tracking Document Mapping Coverage: which SOP/PFMEA files have mapped concepts

**KPIs to track**:
- Concept Coverage Rate (growing, target 60–70% of expanded scope)
- Constraint Validation pass rate (maintain 100% critical, raise important to 90%+)
- Document Mapping Coverage (new KPI: target 50%+ of priority documents mapped)
- Change Request Turnaround (establish SLA tiers; baseline measurement begins)

**Evidence base**: The semi-automated stage matches the "LLM-assisted" level of the three-stage progression [[src-269]]; LLM-driven ontology construction achieves "quality comparable to junior human modelers" [[src-235]] at this stage.

---

#### Stage 3 — Enterprise Scale: Cross-Affiliate Governance + IOF Alignment (Months 18–36)

**Goal**: Shared ontology backbone across affiliates; formal governance; AI applications enabled.

**Activities**:
- Establish common core T-Box shared across affiliates (product, process, defect, equipment domains)
- Each affiliate maintains local extension T-Box (affiliate-specific processes/components)
- Adopt IOF (Industrial Ontologies Foundry) Core Ontology alignment for interoperability with standards [[src-204 from prior research]]
- Automate SHACL validation in CI/CD pipeline; every ontology change triggers validation gate
- Enable AI applications: ontology-augmented RAG for root-cause Q&A; FMEA knowledge retrieval

**KPIs to track**:
- Concept Coverage Rate (target: 80%+ for priority domains)
- Relationship Richness (RR): monitor to ensure ontology deepens beyond taxonomy
- AI Retrieval Improvement: first PoC measurement (ontology-augmented vs. keyword baseline)
- Reuse Rate: # of affiliates / systems consuming shared ontology (new)
- Change Request Turnaround SLA compliance (target: 90%+ on-time by tier)

---

#### Stage 4 — Continuous / Autonomous (Months 36+)

**Goal**: Ontology maintenance largely automated; ontology data asset drives agent reasoning.

**Activities**:
- Continuous ontology update pipeline: new documents → LLM extraction → human review only for breaking changes
- Agent tool contracts and D-2 API tool definitions reference ontology concepts directly
- Ontology serves as the semantic layer for enterprise KPI definitions (KPI governance via ontology)
- Progressive movement toward schema-free autonomous schema extension (research horizon)

**KPIs to track**:
- All Stage 3 KPIs at sustained target levels
- Change request turnaround for editorial/additive changes trending toward zero manual effort
- Ontology-powered AI application accuracy maintained as ontology evolves (regression testing)

---

### 2.4 Key Procedure Steps Within Each Stage [[src-264]]

The KG-PM seven-step procedure model applies iteratively within each roadmap stage:

```
Business Understanding (CQs) 
  → Data Understanding (source quality)
    → Data Preparation 
      → Ontology Modeling (T-Box)
        → Graph Setup (A-Box population)
          → Evaluation (SPARQL on CQs; SHACL; OOPS!)
            → Deployment (CI/CD; governance)
              → [Next iteration: expand CQ set]
```

Quality gate at Evaluation step: all pilot CQs must be answerable (SPARQL returns meaningful results) before proceeding to Deployment.

---

## 3. Consensus & Divergence

### Consensus
There is strong agreement across the literature on the **core quality dimensions** for ontology/KG evaluation: completeness, accuracy, consistency, and conciseness are cited in virtually every framework surveyed [[src-261]] [[src-262]] [[src-263]] [[src-264]]. The OntoQA metrics (RR, AR, IR) are cited across multiple independent papers as the standard structural metrics. The OOPS! pitfall taxonomy is the most widely referenced automated evaluation tool for ontology design quality.

For the **roadmap**, there is consensus on the three-stage progression (manual → semi-automated → autonomous) [[src-269]], and the EKGF five-level model [[src-265]] aligns well as an enterprise adoption framework. The KG-PM seven-step procedure [[src-264]] is a concrete instantiation of how each roadmap stage unfolds.

### Divergence
**On specific KPI target values**: The literature does not provide universal benchmarks. Every paper that presents numbers (93.5% RCA accuracy [[src-266]]; +30 pp RAG improvement [[src-267]]) reports domain-specific results with caveats. There is no cross-domain consensus on "good" concept coverage percentage or acceptable orphan count. This is appropriate to this type of data asset: targets must be set in PoC.

**On AI-usage value measurement**: Some sources emphasize automated precision/recall metrics; others (including [[src-267]]) use manual categorical evaluation. There is no agreed standard evaluation protocol for ontology-augmented RAG quality.

**On LLM assistance maturity**: The LLM-empowered KG construction survey [[src-269]] characterizes current LLM output as "comparable to junior human modelers" — not expert-level. However, enterprise vendor claims (OntoEKG, src-235) are more optimistic. The conservative academic position should be followed in the guide.

**On change management SLAs**: No industry-standard SLA tiers exist. The three-tier (editorial / additive / breaking) change classification [[src-270]] is a practitioner framework, not a formal standard.

---

## 4. Sources

| ID | Title | URL |
|----|-------|-----|
| [[src-261]] | Structural Quality Metrics to Evaluate Knowledge Graphs (arXiv 2211.10011) | https://arxiv.org/abs/2211.10011 |
| [[src-262]] | OOPS! OntOlogy Pitfall Scanner (IJSWIS 2014) | https://www.semanticscholar.org/paper/OOPS!-(OntOlogy-Pitfall-Scanner!):-An-On-line-Tool-Poveda-Villal%C3%B3n-G%C3%B3mez-P%C3%A9rez/28f692a5b6e61ab48bece1221f4e17e05a9a8139 |
| [[src-263]] | KG Quality Management: A Comprehensive Survey | https://www.researchgate.net/publication/358524938_Knowledge_Graph_Quality_Management_a_Comprehensive_Survey |
| [[src-264]] | Procedure Model for Building KGs for Industry (arXiv 2409.13425) | https://arxiv.org/html/2409.13425v1 |
| [[src-265]] | EKG Maturity Model (EKGF) | https://maturity.ekgf.org/intro/structure/ |
| [[src-266]] | KGroot: KG-Enhanced Root Cause Analysis (arXiv 2402.13264) | https://arxiv.org/html/2402.13264v1 |
| [[src-267]] | Ontology vs KG Construction: RAG Performance (arXiv 2511.05991) | https://arxiv.org/html/2511.05991v1 |
| [[src-268]] | KGCL: A Change Language for Ontologies (PMC 11753292) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11753292/ |
| [[src-269]] | LLM-Empowered KG Construction: Survey (arXiv 2510.20345) | https://arxiv.org/pdf/2510.20345 |
| [[src-270]] | Ontology Management Operating Model (Galaxy) | https://www.getgalaxy.io/articles/ontology-management-semantic-modeling-operating-model-enterprise-context |

---

## 5. Related

- [[research-A-what.en.md]] — What the ontology data asset IS (T-Box/A-Box, components, standards)
- [[research-B-how.en.md]] — How to build the ontology (methodology, tooling, LLM assistance)
- [[research-C-why-when.md]] — Why and when to invest in ontology preparation
- [[research-E-architecture.md]] — Architecture and deployment choices affecting KPI measurement
- [[B-3 온톨로지.md]] — Main guide document (consumer of this research)

---

*Research completed: 2026-06-19. Sources archived in `/research/sources/src-261` through `src-270`.*
