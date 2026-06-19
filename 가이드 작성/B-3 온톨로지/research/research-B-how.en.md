---
type: research
lang: en
date: 2026-06-19
tags: [how, architecture, methodology, build, operations, governance, LPG, RDF, graph-db, IOF, T-box, A-box, materialization, versioning, llm-assistance, knowledge-elicitation, PFMEA, SOP, manufacturing]
cluster: HOW + ARCHITECTURE
topic: B-3 Ontology
perspective: "Preparing data FOR AI — modeling/building/storing/operating the ontology as a knowledge data asset"
---

# B-3 Ontology: HOW + Architecture Research (English)

> **Cluster focus:** Build methodology, data-prep workstream, architecture decision methodology (LPG vs RDF, store, query language, reasoning), holding company + affiliate structure, operations/change management, LLM/AI assistance.
> **Perspective fixed:** "Preparing data FOR AI" — not building AI. Tools, stages, and decisions that prepare the ontology as a reusable knowledge data asset.

---

## Table of Contents

1. [Ontology Build Methodology](#1-ontology-build-methodology)
   - 1.1 [Recognized Methodologies — One-Line Each](#11-recognized-methodologies-one-line-each)
   - 1.2 [Clean Stage Model (Synthesized)](#12-clean-stage-model-synthesized)
   - 1.3 [Start-Small Principle](#13-start-small-principle)
2. [Data-Prep Workstream: Extracting Concepts from Manufacturing Documents](#2-data-prep-workstream)
   - 2.1 [Source Documents and What to Extract](#21-source-documents-and-what-to-extract)
   - 2.2 [Knowledge Elicitation from Domain Experts](#22-knowledge-elicitation-from-domain-experts)
   - 2.3 [Relation Definition Document Template](#23-relation-definition-document-template)
   - 2.4 [Concept–Data–Document Mapping](#24-conceptdatadocument-mapping)
3. [Architecture Decision Methodology](#3-architecture-decision-methodology)
   - 3.1 [Decision Order (High-Level)](#31-decision-order)
   - 3.2 [Format Decision: LPG vs RDF](#32-format-decision-lpg-vs-rdf)
   - 3.3 [Store Decision: RDB + Graph DB Polyglot](#33-store-decision-rdb--graph-db-polyglot)
   - 3.4 [Query Language Decision](#34-query-language-decision)
   - 3.5 [Reasoning / Materialization Tradeoff](#35-reasoning--materialization-tradeoff)
   - 3.6 [Standard Adoption: IOF + BFO](#36-standard-adoption-iof--bfo)
   - 3.7 [Graph DB Landscape (Comparison Table)](#37-graph-db-landscape-comparison-table)
4. [Holding Company–Affiliate Ontology Structure](#4-holding-companyaffiliate-ontology-structure)
   - 4.1 [Structural Split Pattern](#41-structural-split-pattern)
   - 4.2 [Namespace and Import Mechanics](#42-namespace-and-import-mechanics)
   - 4.3 [NeOn Scenario Mapping](#43-neon-scenario-mapping)
5. [Operations: Change Management, Versioning, Governance](#5-operations)
   - 5.1 [Change Classification and Approval](#51-change-classification-and-approval)
   - 5.2 [Semantic Versioning for Ontologies](#52-semantic-versioning-for-ontologies)
   - 5.3 [Governance Roles](#53-governance-roles)
   - 5.4 [Impact on AI Retrieval/Reasoning — Checklist](#54-impact-on-ai-retrievalreasoning--checklist)
6. [LLM / Automation Assistance in Ontology Preparation](#6-llm--automation-assistance)
   - 6.1 [What LLMs Help With (and What They Don't)](#61-what-llms-help-with-and-what-they-dont)
   - 6.2 [Hybrid Automated Extraction Pipeline](#62-hybrid-automated-extraction-pipeline)
   - 6.3 [Accuracy Benchmark](#63-accuracy-benchmark)
7. [Consensus & Divergence](#7-consensus--divergence)
8. [Sources](#8-sources)
9. [Related](#9-related)

---

## 1. Ontology Build Methodology

### 1.1 Recognized Methodologies — One-Line Each

| Methodology | Year | Origin | One-Line Summary |
|-------------|------|--------|-----------------|
| **Uschold & King (ENTERPRISE)** | 1995 | AIAI Edinburgh | Four phases: identify purpose/scope → build (capture + code + integrate) → document → evaluate; first structured approach, emphasizes term ambiguity resolution [[src-223]] |
| **METHONTOLOGY** | 1997+ | Madrid Polytechnic (UPM) | Waterfall lifecycle: Specification → Conceptualisation → Formalisation → Integration → Implementation → Maintenance; parallel management activities (QA, documentation, knowledge acquisition) [[src-221]] |
| **Ontology Development 101** | 2001 | Stanford / Noy & McGuinness | Seven iterative steps from scope to instances; pragmatic, beginner-friendly; introduces competency questions and three hierarchy strategies (top-down / bottom-up / combination) [[src-237]] |
| **NeOn Methodology** | 2006+ | OEG, UPM / Suárez-Figueroa | Nine scenarios for building ontology networks; emphasizes reuse of ontological and non-ontological resources; designed for distributed, collaborative development — ideal for multi-affiliate structures [[src-222]] |
| **Ontology Summit 2013 Lifecycle** | 2013 | Community | Five phases with checkpoints; full lifecycle including deployment; adds evaluation criteria per stage [[src-221]] |

**Synthesis for manufacturing practice:** METHONTOLOGY provides the disciplined lifecycle skeleton; NeOn adds the reuse and network extension needed for holding-company + affiliate structures; OD101 provides the practitioner-level step-by-step guidance for knowledge engineers. Use all three in combination rather than picking one.

---

### 1.2 Clean Stage Model (Synthesized)

The following seven-stage model synthesizes METHONTOLOGY's lifecycle discipline, NeOn's reuse strategy, and OD101's practical authoring guidance into a single sequence applicable to manufacturing ontology data preparation:

```
Stage 1: SCOPE DEFINITION
  → "What questions must this ontology answer?"
  → Identify domain (e.g., welding defects on one product line), users, and key competency questions
  → Output: Scope definition document, competency question list

Stage 2: KNOWLEDGE SOURCE COLLECTION
  → Gather: PFMEA, SOP, C/S Reports, Inspection Records, existing Glossary (A-3)
  → Identify which source contains which type of knowledge (causes, actions, standards)
  → Output: Source document inventory, candidate term list

Stage 3: CONCEPT ELICITATION & NORMALIZATION
  → Domain experts + knowledge engineers: concept maps, structured interviews
  → Resolve synonyms, abbreviations, cross-department term conflicts (link to Glossary A-3)
  → Remove duplicates; define candidate class hierarchy
  → Output: Normalized concept list with definitions, conflict resolution log

Stage 4: CLASS HIERARCHY + RELATION DEFINITION
  → Define classes (entities), relations (object properties: causes, triggers, hasAction),
    data properties (attributes: severity, frequency), and constraints (cardinality, domain/range)
  → Map relations to a Relation Definition Document (name, domain, range, inverse, description)
  → Output: Class hierarchy diagram, Relation Definition Document

Stage 5: HOLDING COMPANY / AFFILIATE LAYER DESIGN
  → Common upper layer: upper concept classes + standard relation types (holding-owned)
  → Affiliate extension: domain-specific subclasses, local relations (affiliate-owned)
  → Define namespace policy and import/extension mechanism
  → Output: Two-layer schema (common + affiliate-specific)

Stage 6: INSTANCE POPULATION & DATA MAPPING
  → Map ontology classes → actual data fields in RDB/ERP/MES/PFMEA tables
  → Populate instance data (triples/property-graph records) from C/S Reports, inspection data
  → Load into graph DB
  → Output: Concept–Data–Document Mapping Table, populated graph DB

Stage 7: VALIDATION → PUBLISH → MAINTAIN (Loop)
  → SHACL constraint checks, reasoner consistency validation, domain expert sample review
  → AI retrieval test (does the ontology improve search/reasoning quality?)
  → Publish with version label; enter change management cycle
  → Output: Validation report, published ontology, version changelog
```

**Key principle (from all three methodologies):** Iterate. No ontology is correct on the first pass — expect 2–3 validation/correction cycles before production deployment.

---

### 1.3 Start-Small Principle

All recognized methodologies warn against attempting a comprehensive enterprise ontology from the beginning. Reasons:

- **Scope explosion:** Concepts grow multiplicatively; relations grow polynomially
- **Expert fatigue:** Domain experts lose engagement when asked to validate a 500-concept model
- **No early value:** Large ontologies take months to build before any AI benefit is visible

**Recommended entry point for manufacturing:** One product line + one defect domain (e.g., "welding defects on Product X"). Key competency questions should be answerable within 50–100 concepts and 10–15 relation types. Expand iteratively once AI retrieval value is demonstrated.

---

## 2. Data-Prep Workstream

### 2.1 Source Documents and What to Extract

The data-prep workstream is how you translate manufacturing documents into ontology concepts, relations, and instances. Three primary document types:

| Document | What to Extract | Ontology Element |
|----------|----------------|-----------------|
| **PFMEA (Process Failure Mode and Effects Analysis)** | Failure modes, potential effects, potential causes, current controls, severity/occurrence/detection ratings, recommended actions | Classes: Defect, Effect, Cause, Control, Action; Data properties: severity (1–10), occurrence (1–10) |
| **SOP (Standard Operating Procedure)** | Process steps, required inputs, acceptable parameter ranges, responsible roles, quality checkpoints | Classes: Process, ProcessStep, Resource, Role; Relations: hasStep, requiresInput, performedBy |
| **C/S Report (Customer/Service Report, field failure report)** | Actual defect instances, confirmed causes, remediation actions, recurrence flag, product/line context | A-Box instances: individual Case records connected to Cause, Defect, Action class instances |

**Practical extraction workflow from PFMEA [[src-239]]:**
- PFMEA Item "Failure Mode" → Defect subclass (e.g., `SurfaceCrack`)
- PFMEA Item "Potential Cause" → Cause subclass (e.g., `HeatTreatmentDefect`)
- PFMEA Item "Recommended Action" → Action subclass (e.g., `HeatTreatmentReset`)
- PFMEA ratings (S/O/D) → integer data properties on the Defect class
- PFMEA "Current Controls" → Control class with `mitigates` relation to Defect

---

### 2.2 Knowledge Elicitation from Domain Experts

Ontology building requires two roles working in tandem [[src-233]]:
- **Domain Expert (SME):** Knows the business meaning, edge cases, and ambiguities
- **Knowledge Engineer:** Knows how to represent knowledge formally; asks structured questions

**Concept map technique (most effective bridge between the two):**
1. Ask the SME to narrate a defect scenario: "Walk me through what happens from when you first see this defect to when it's resolved"
2. Knowledge engineer captures the narrative as a concept map: nodes = things, arcs = relationships
3. Review the map with the SME: "Does this capture how it actually works?"
4. Identify abstractions: multiple specific examples → candidate class

**Structured interview questions for manufacturing:**
- "What are the different types of [defect] you see on this line?"  → class hierarchy candidates
- "When you say 'heat treatment failure,' is that the same as 'temperature deviation' or different?" → synonym resolution
- "Can a single defect have multiple causes at the same time?" → cardinality constraint
- "Is this cause always followed by this action, or are there cases where a different action is used?" → relation constraint

**From PFMEA documents specifically [[src-239]]:**
- Use existing PFMEA structure as a pre-built concept map — it already organizes failure modes, causes, effects, and controls in tabular form
- Knowledge engineer's job: convert the table into a formal class hierarchy + relation definition document
- Challenge: PFMEA terminology is plant-specific — different plants use different names for the same phenomenon → normalization against Glossary A-3 is critical

---

### 2.3 Relation Definition Document Template

Every relation in the ontology should be documented in a Relation Definition Document before implementation. Template:

| Field | Description | Example |
|-------|-------------|---------|
| **Relation Name** | Preferred label (camelCase) | `hasCause` |
| **Display Label** | Human-readable label (Korean + English) | 원인을 갖는다 (hasCause) |
| **Domain** | Class this relation starts from | `Defect` |
| **Range** | Class this relation points to | `Cause` |
| **Inverse Relation** | Name of reverse relation (if defined) | `causeOf` |
| **Cardinality** | How many values allowed | One-to-many (one Defect, multiple Causes) |
| **Transitivity** | Is this transitive? | No |
| **Definition** | Plain-language description | "Links a defect occurrence to its contributing root cause(s)" |
| **Example** | Concrete manufacturing instance | `SurfaceCrack hasCause HeatTreatmentDefect` |
| **Source** | Where this relation was confirmed | PFMEA #W-023, Domain Expert review 2024-11 |

Standard manufacturing relation types to define:
- `hasCause` / `causeOf` — Defect → Cause
- `hasEffect` / `effectOf` — Defect → Effect (what happens downstream)
- `hasAction` / `actionFor` — Cause or Defect → remediation Action
- `isSubtypeOf` / `isSupertypeOf` — class hierarchy
- `occursIn` — Defect → ProcessStep or Equipment
- `mitigatedBy` — Defect or Cause → Control measure
- `relatedTo` — weak, symmetric association (use sparingly)

---

### 2.4 Concept–Data–Document Mapping

After defining concepts and relations in the ontology, each concept must be traceable back to actual data sources. This mapping table serves as the integration specification:

| Ontology Class | Glossary Term (A-3) | Metadata Field (A-2) | Catalog Asset (A-1) | Source Document | Instance Count |
|----------------|--------------------|--------------------|-------------------|----------------|---------------|
| `Defect` | 결함 (Defect) | defect_type | Inspection Records | C/S Report, PFMEA | ~2,400 |
| `SurfaceCrack` | 표면균열 (Surface Crack) | crack_location: surface | Welding QC Records | C/S Report 2022–2024 | ~480 |
| `Cause` | 원인 (Cause) | cause_code | PFMEA Table | PFMEA, 8D Reports | ~180 distinct |
| `HeatTreatmentDefect` | 열처리불량 | heat_anomaly_flag | HT Process Log | PFMEA #W-023, SOP #HT-007 | ~120 |
| `Action` | 조치 (Corrective Action) | action_code | Action Registry | 8D Reports, C/S Reports | ~95 distinct |
| `ProcessStep` | 공정 단계 | process_step_id | Process Catalog | SOP, MES logs | ~340 |

**Purpose of this mapping:** Enables automated population of the ontology A-Box from existing structured data. When a new C/S Report is filed, an ETL pipeline reads `defect_type` and `cause_code` from the structured report, maps them to the corresponding ontology classes, and creates instance triples in the graph DB — no manual ontology editing required for new data.

---

## 3. Architecture Decision Methodology

### 3.1 Decision Order

Architecture decisions must be made in this order because each decision constrains the next. Changing format (LPG vs RDF) later has the highest switching cost of all decisions:

```
① FORMAT: LPG vs RDF
     ↓ (determines available stores and query languages)
② STORE: RDB (T-Box schema / transactional) + Graph DB (A-Box instances / paths)
     ↓ (determines query language options)
③ QUERY LANGUAGE: openCypher/GQL (LPG) or SPARQL (RDF)
     ↓ (determines reasoning strategy)
④ REASONING: materialization (T-Box stable, queries frequent) vs query-time (T-Box evolving)
     ↓ (now ready to consider standards alignment)
⑤ STANDARD ADOPTION: IOF/BFO — reference vocabulary, align progressively
     ↓
⑥ DIAGNOSTICS: security, performance, cost tuning
```

---

### 3.2 Format Decision: LPG vs RDF

#### Core Tradeoff Summary

| Dimension | LPG (Labeled Property Graph) | RDF (Resource Description Framework) |
|-----------|------------------------------|--------------------------------------|
| **Data model** | Nodes + typed directed edges; both carry key-value properties | Subject–predicate–object triples; statements are atomic |
| **Edge properties** | Native (timestamp, confidence, frequency on a relation) | Requires RDF-Star (still emerging) or reification (verbose) |
| **Multi-hop performance** | Traverses edges directly; no join explosion | Triple joins multiply with each hop — 6+ hops = O(n^k) triple joins |
| **Schema** | Schema-optional; flexible for iterative development | Schema-focused, ontology-driven; predefined vocabularies |
| **Formal semantics** | No native axioms; hierarchy represented as graph patterns | OWL axioms, Open World Assumption, DL reasoning |
| **Query language** | Cypher / openCypher / ISO GQL (April 2024) | SPARQL 1.1 (W3C standard) |
| **Vendor portability** | Proprietary historically; ISO GQL (2024) standardizes this | RDF is W3C-standard; SPARQL portable across triple stores |
| **External interoperability** | Limited unless NeoSemantics bridge used | Strong — linked data, IOF, FIBO, schema.org all RDF |
| **Learning curve** | Low; Cypher is SQL-like | Higher; requires RDF/OWL conceptual model understanding |
| **Manufacturing path depth** | Excellent — 6+ hop defect→cause→subprocess→equipment→supplier | Explodes at 6+ hops without performance tuning |

[[src-224]] [[src-240]] [[src-207]] [[src-237]]

#### Decision Rule for This Project

**Choose LPG when:**
- Root-cause reasoning paths are long (6+ hops) — manufacturing diagnosis chains
- Schema evolves frequently in early development phases
- Real-time or near-real-time query latency required (sub-second)
- Team has strong SQL/Cypher skills; RDF/SPARQL expertise not available
- Closed enterprise environment (no cross-organization linked-data sharing required yet)

**Choose RDF when:**
- External standard interoperability is the primary requirement (IOF alignment, supplier data sharing, regulatory compliance)
- OWL-based logical reasoning is core (not just hierarchy traversal)
- Cross-domain semantic integration is the dominant use case
- Long-term archiving with open-standard portability is a governance requirement

**Locked recommendation for manufacturing root-cause ontology:** LPG (as established in §Architecture methodology). The triple explosion problem at 6+ hop paths is the decisive factor. LPG traverses the defect→cause→subprocess→equipment→supplier path efficiently; RDF requires expensive join computation at each step [[src-224]].

**Note on the LPG "lock-in" concern:** ISO/IEC 39075 GQL (published April 12, 2024) directly addresses this. openCypher implementations are on a migration path to GQL compliance. Cypher written today has a clear standardization trajectory [[src-225]].

---

### 3.3 Store Decision: RDB + Graph DB Polyglot

The polyglot persistence pattern [[src-207]] splits data by its access pattern:

| Layer | Store Type | What Goes Here | Why |
|-------|-----------|---------------|-----|
| **T-Box (schema)** | RDB (PostgreSQL or equivalent) | Class definitions, relation definitions, property constraints, namespace registry, version metadata | T-Box is small, stable, tabular — RDB is ideal; ACID transactions for governance-controlled schema changes |
| **A-Box (instances)** | Graph DB (Neo4j / Neptune) | Individual case instances, triple records, path traversal data | A-Box grows continuously; graph traversal queries are the dominant access pattern |
| **Structured transactional data** | RDB (ERP, MES, QMS) | C/S Report records, PFMEA tables, inspection results (raw source data) | ACID guarantees; existing system integration |
| **Unstructured documents** | Vector DB + Object Storage | SOP chunks, embedded for semantic search | Separate from graph; fed into RAG pipeline |

**Integration mechanism:** When a new C/S Report lands in the RDB, an ETL pipeline reads it, maps values to ontology class instances (using the Concept–Data–Document Mapping Table from §2.4), and writes property-graph records to the graph DB. The T-Box schema stored in the RDB constrains what classes and relations are valid.

---

### 3.4 Query Language Decision

| Scenario | Query Language | Standard |
|---------|---------------|---------|
| LPG store (Neo4j, Neptune openCypher mode, Memgraph) | openCypher → migrating to ISO GQL | ISO/IEC 39075:2024 [[src-225]] |
| RDF store (Stardog, Ontotext GraphDB, Neptune SPARQL mode) | SPARQL 1.1 | W3C Recommendation |
| Analytics / graph algorithms (Neo4j) | GDS (Graph Data Science) library / Python API | Neo4j proprietary |
| TigerGraph | GSQL | Proprietary (not GQL-aligned) |

**openCypher → GQL path:** openCypher is the open-source Cypher specification; as of April 2024, the openCypher project mission is to help implementors evolve toward GQL compliance. Writing openCypher today is not obsolescence risk — it is GQL preparation [[src-225]].

**Example — multi-hop defect path query (openCypher):**
```cypher
MATCH path = (c:Case)-[:HAS_DEFECT]->(d:Defect)
             -[:OFTEN_CAUSED_BY*1..3]->(root:Cause)
WHERE c.product = 'BobcatArm' AND c.date > '2024-01-01'
RETURN d.name, root.name, length(path) AS hops
ORDER BY count(*) DESC
LIMIT 10
```

**Example — same query in SPARQL (RDF):**
```sparql
PREFIX mfg: <http://doosan.com/ontology/manufacturing#>
SELECT ?defect ?rootCause (COUNT(?cause) AS ?hops) WHERE {
  ?case mfg:hasDefect ?defect ;
        mfg:onProduct "BobcatArm" .
  ?defect mfg:causeChain+ ?rootCause .
  OPTIONAL { ?defect mfg:hasCause ?cause }
}
GROUP BY ?defect ?rootCause
ORDER BY DESC(COUNT(*))
LIMIT 10
```
The SPARQL version requires property path syntax and performs multi-join traversal under the hood — performant for short paths, degrades with depth.

---

### 3.5 Reasoning / Materialization Tradeoff

#### T-Box vs A-Box [[src-238]]

- **T-Box** = terminological box = the ontology schema (class definitions, relation axioms, subclass hierarchy). Small (hundreds of concepts), comparatively stable, owned by governance.
- **A-Box** = assertional box = instance data (individual cases, triples). Large (millions of records), grows continuously, owned by data pipelines.

**Critical rule:** T-Box changes are expensive — they can invalidate all inferences across the entire A-Box. A-Box changes are routine data operations.

#### Materialization vs Query-Time Inference

| Approach | Mechanism | Storage Cost | Query Speed | Update Flexibility |
|---------|-----------|-------------|------------|-------------------|
| **Materialization (pre-compute)** | Run reasoner on T-Box + A-Box; write all inferred triples to the store | High (pre-computed triples stored) | Fast (direct lookup) | Low (must re-run reasoner after T-Box change) |
| **Query-time inference** | Apply T-Box axioms during query execution | Low | Slower (inference computed per query) | High (T-Box changes take effect immediately) |
| **Incremental materialization** | Re-materialize only affected A-Box subsets after T-Box change | Medium | Fast | Medium |

**Recommendation for manufacturing ontology:**
- T-Box (class hierarchy) is stable once designed → **materialize** inferences; faster queries, acceptable storage cost
- A-Box (case instances) arrives continuously → **insert new instances without re-materializing** the full A-Box; the materialized T-Box inferences already apply to new instances through class membership
- When T-Box changes (new defect subclass added) → **incremental re-materialization** of affected subgraph only

**Stardog vs GraphDB reasoning approaches [[src-230]]:**
- Stardog: query-time (just-in-time) reasoning — always current data; no migration cost for T-Box changes
- Ontotext GraphDB: forward-chaining materialization — faster queries; requires re-materialization when T-Box changes
- For manufacturing where T-Box is stable: GraphDB's materialization is preferable for query performance

---

### 3.6 Standard Adoption: IOF + BFO

#### What IOF Provides [[src-226]]

The Industrial Ontologies Foundry (IOF) provides a suite of interoperable ontologies for manufacturing built on BFO (Basic Formal Ontology) as the upper-level framework:

- **Core ontology** (normative): Foundational manufacturing concepts — processes, roles, identifiers, measurements, temporal relations
- **Domain ontologies** (some normative, some provisional): Supply Chain, Manufacturing, Maintenance, Material Procurement, Certification, Production Planning
- **Extension pattern:** Domain ontologies import Core concepts; organization-specific ontologies extend domain ontologies

#### Why IOF Matters for a Holding-Company Architecture

IOF provides battle-tested, community-validated concept definitions that can serve as the shared vocabulary for a holding company's upper ontology layer. Instead of inventing `mfg:ManufacturingProcess` from scratch, align to `iof-core:ManufacturingProcess` — external suppliers, auditors, and partner systems can then share semantic understanding.

#### Adoption Recommendation (Progressive)

**Do NOT adopt IOF wholesale at the start.** The cognitive overhead of learning BFO and aligning all local terms is too high for early-stage ontology work. Instead:

| Phase | IOF Adoption Action |
|-------|-------------------|
| **Phase 1 (Initial build)** | Build custom ontology from scratch based on internal PFMEA/SOP knowledge. Use IOF only as a reference vocabulary — check if your concepts have IOF equivalents; don't force-fit |
| **Phase 2 (Stabilization)** | After internal ontology is validated, progressively align high-frequency terms to IOF Core (Manufacturing, Maintenance modules) |
| **Phase 3 (External integration)** | When sharing data with external suppliers, regulators, or partners becomes necessary, formalize the IOF alignment and expose the ontology via IOF-compatible IRIs |

**BFO background:** BFO (Basic Formal Ontology) was adopted as IOF's top-level ontology in spring 2019. It provides the most abstract categories (continuant vs occurrent, independent vs dependent, etc.) — useful conceptual scaffolding but not required for initial ontology work.

---

### 3.7 Graph DB Landscape (Comparison Table)

| Database | Model | Query Language | Reasoning/Ontology | Deployment | Best For |
|---------|-------|---------------|-------------------|-----------|---------|
| **Neo4j** [[src-237]] [[src-229]] | LPG | Cypher / ISO GQL (migrating) | NeoSemantics plugin for RDF bridge; no native OWL | Self-managed (Community/Enterprise) + AuraDB (managed) | Transactional consistency, mature ecosystem, Cypher expertise, analytics (GDS library) |
| **Amazon Neptune** [[src-229]] [[src-231]] | LPG + RDF | Gremlin + openCypher + SPARQL 1.1 | RDF+SPARQL mode supports ontology-driven queries | Fully managed AWS; serverless | AWS-native orgs needing both RDF and property graph; SageMaker ML integration |
| **TigerGraph** [[src-231]] | LPG (native parallel) | GSQL (proprietary) | No native ontology/RDF | Self-managed + cloud | Deep analytics, fraud detection, telecom; high-performance compute-intensive traversal |
| **Ontotext GraphDB** [[src-230]] | RDF | SPARQL 1.1 | OWL QL/RL profiles; forward-chaining materialization; strong SHACL | Self-managed + cloud (GraphDB Cloud) | Semantic/ontology-driven apps, SPARQL workloads, linked data |
| **Stardog** [[src-230]] | RDF | SPARQL 1.1 | All OWL profiles; query-time reasoning; data virtualization | Self-managed + cloud | Cross-silo enterprise KG, data virtualization, complex reasoning without ETL |
| **Memgraph** | LPG | openCypher | No native OWL; graph algorithms | Self-managed (in-memory) | Real-time IoT streaming, sub-millisecond latency, Kafka integration |
| **Apache Jena + TDB** | RDF | SPARQL 1.1 | OWL reasoning (Pellet, HermiT integrations); SHACL via Jena-SHACL | Self-managed (open source, free) | Budget-conscious RDF deployments; research; PoC |

**For LPG-based manufacturing ontology (recommended path):**
- **PoC:** Neo4j Community (free, full Cypher support)
- **Production (cloud-first):** Amazon Neptune (if AWS org) or Neo4j AuraDB (multi-cloud)
- **High-volume real-time streaming:** Memgraph (Kafka-native, in-memory)
- **If RDF/OWL reasoning becomes required:** Ontotext GraphDB Free (PoC) → Stardog (enterprise, data virtualization)

---

## 4. Holding Company–Affiliate Ontology Structure

### 4.1 Structural Split Pattern

The holding company + affiliate structure maps directly to the NeOn Methodology's ontology network concept [[src-222]]. Two layers:

```
HOLDING COMPANY ONTOLOGY (mfg-common:)
├── Upper concept classes
│   ├── mfg-common:Product
│   ├── mfg-common:Defect
│   ├── mfg-common:Cause
│   ├── mfg-common:Action
│   ├── mfg-common:Process
│   └── mfg-common:Equipment
├── Standard relation types
│   ├── mfg-common:hasCause
│   ├── mfg-common:hasAction
│   ├── mfg-common:occursIn
│   └── mfg-common:mitigatedBy
└── Governance-controlled (Governance Board owns changes)

    ↓  (import / extend)

AFFILIATE ONTOLOGY — Bobcat (mfg-bc:)
├── Subclasses specific to Bobcat domain
│   ├── mfg-bc:WeldingDefect  subClassOf mfg-common:Defect
│   ├── mfg-bc:HeatTreatmentDefect  subClassOf mfg-common:Cause
│   └── mfg-bc:HydraulicSystem  subClassOf mfg-common:Equipment
├── Affiliate-specific relations
│   └── mfg-bc:requiresWeldCertification
└── Affiliate-owned (Bobcat domain steward approves changes)

AFFILIATE ONTOLOGY — Doosan Enerbility (mfg-de:)
├── mfg-de:TurbineComponent  subClassOf mfg-common:Product
├── mfg-de:CorrosionDefect  subClassOf mfg-common:Defect
└── ... (separate namespace, separate steward)
```

**Rule for what belongs in common vs affiliate:**
- Common: Any concept or relation that appears in ≥2 affiliates with the same meaning
- Affiliate: Any concept that is specific to one business unit's domain, product type, or process
- Contested (appears in multiple affiliates with slightly different meanings): Held in common with a superclass, with affiliate-specific subclasses handling differences

---

### 4.2 Namespace and Import Mechanics

**LPG approach (Neo4j / openCypher):**
```cypher
// Common schema: node labels prefixed to indicate layer
CREATE (:DefectType:Common {name: 'Defect', namespace: 'mfg-common'})
CREATE (:DefectType:Bobcat {name: 'WeldingDefect', namespace: 'mfg-bc'})
CREATE (weld:DefectType {name: 'WeldingDefect'})-[:IS_SUBTYPE_OF]->
       (d:DefectType {name: 'Defect', namespace: 'mfg-common'})

// Query: get all defect types for Bobcat including common supertypes
MATCH (t:DefectType)-[:IS_SUBTYPE_OF*0..]->(root:DefectType {namespace: 'mfg-common'})
WHERE t.namespace IN ['mfg-bc', 'mfg-common']
RETURN t.name, root.name
```

**RDF approach:**
```turtle
# Holding company common ontology
@prefix mfg-common: <http://doosan.com/ontology/common#> .
mfg-common:Defect a owl:Class .
mfg-common:hasCause a owl:ObjectProperty ;
    rdfs:domain mfg-common:Defect ; rdfs:range mfg-common:Cause .

# Bobcat affiliate extension (separate file, imports common)
@prefix mfg-bc: <http://doosan.com/ontology/bobcat#> .
@prefix mfg-common: <http://doosan.com/ontology/common#> .

<http://doosan.com/ontology/bobcat#> owl:imports 
    <http://doosan.com/ontology/common#> .

mfg-bc:WeldingDefect a owl:Class ;
    rdfs:subClassOf mfg-common:Defect .
```

---

### 4.3 NeOn Scenario Mapping

NeOn's nine scenarios [[src-222]] map to holding-company use cases:

| NeOn Scenario | When Applied in Holding Co. Context |
|--------------|-------------------------------------|
| Scenario 1 (From scratch) | Building the holding-company common ontology for the first time |
| Scenario 3 (Reusing ontological resources) | Affiliate B adopts concepts from Affiliate A's existing ontology |
| Scenario 5 (Reusing + Merging) | Two affiliates' ontologies merged into holding-company common layer |
| Scenario 7 (Reusing ODPs) | Using established Ontology Design Patterns (e.g., Fault–Cause–Effect ODP) for new affiliate |
| Scenario 8 (Restructuring) | Modularizing a monolithic ontology into common + affiliate layers retroactively |
| Scenario 9 (Localizing) | Adapting Korean-language labels and definitions for Korean-speaking manufacturing lines |

---

## 5. Operations

### 5.1 Change Classification and Approval

[[src-228]] [[src-232]]

| Change Type | Examples | Risk to AI Retrieval | Approval Level |
|------------|---------|---------------------|----------------|
| **Editorial** | Label correction, synonym addition, description update | None — AI behavior unchanged | Domain Steward (SME) alone |
| **Additive** | New subclass added, new relation type added | Low — new concepts available; existing queries unaffected | Standard cross-domain review (Steward + Semantic Architect) |
| **Breaking** | Class renamed/deleted, relation semantic redefined, hierarchy restructured | High — existing queries return different results; materialized inferences invalidated | Governance Board approval + impact analysis + migration plan |

**Key principle (from Galaxy operating model [[src-228]]):**
"Additive change before breaking change" — when possible, add a new concept instead of modifying an existing one, and deprecate the old concept with a pointer to the new one.

---

### 5.2 Semantic Versioning for Ontologies

[[src-227]]

```
VERSION FORMAT:  X.Y.Z
  X (Major):  Breaking changes — class deletions, hierarchy restructure, relation semantic change
  Y (Minor):  Additive changes — new classes, new relations, new properties
  Z (Patch):  Editorial changes — label corrections, descriptions, synonyms

DUAL IRI POLICY:
  Ontology IRI (latest):   http://doosan.com/ontology/manufacturing
  Version IRI (specific):  http://doosan.com/ontology/manufacturing/1.2.0

OWL VERSION METADATA:
  owl:versionIRI <http://doosan.com/ontology/manufacturing/1.2.0>
  owl:versionInfo "1.2.0"
  rdfs:comment "v1.2.0: Added 3 SurfaceCrack subtypes (2026-03-15). See changelog."
```

**Deprecation protocol [[src-227]]:**
1. Do not delete; mark as `owl:deprecated true` + add "(Deprecated)" label suffix
2. Add `rdfs:seeAlso` pointer to replacement concept
3. Keep deprecated entities until next Major version (X+1) release
4. Document deprecation in changelog with rationale

---

### 5.3 Governance Roles

[[src-228]] [[src-232]]

| Role | Responsibility | Who Holds It |
|------|---------------|-------------|
| **Domain Steward** | Proposes new concepts; provides business definitions; validates concepts for their domain; approves Editorial changes; identifies downstream data consumers | Business unit SME (quality engineer, process engineer) |
| **Semantic Architect / Ontology Engineer** | Models concepts formally; ensures cross-domain naming consistency; reviews Additive changes; maintains relation definition documents; resolves concept conflicts between affiliates | Data/IT function with ontology expertise |
| **Governance Board** | Owns holding-company common ontology; approves Breaking changes; sets naming conventions, namespace policy, identifier standards; arbitrates conflicts | Cross-affiliate committee (1–2 representatives per affiliate + Semantic Architect) |
| **Platform / Data Team** | Publishes approved versions; runs SHACL validation pipelines; manages graph DB deployment; implements rollback when needed | Data engineering / IT operations |

**Minimum viable governance (early stage):**
Even without a formal Governance Board, establish: one Domain Steward per affiliate + one Semantic Architect (can be a consultant initially) + a simple Git-based review process (pull request = change proposal, reviewed by Semantic Architect before merge).

---

### 5.4 Impact on AI Retrieval/Reasoning — Checklist

Run before publishing any ontology change:

```
PRE-PUBLISH IMPACT CHECKLIST

□ Run SHACL validation suite — zero violations?
□ Run reasoner consistency check — no unsatisfiable classes?
□ Execute regression query set (top 20 AI queries) — results unchanged for non-breaking changes?
□ For Breaking changes: identify all datasets, dashboards, API endpoints, AI retrieval pipelines 
  that reference changed concepts (dependency analysis)
□ For Breaking changes: test with production data sample — AI retrieval quality maintained?
□ Affiliated ontologies (child namespaces) — no conflicts introduced?
□ Downstream AI team notified of change (especially if Breaking)?
□ Changelog updated with: concept changed, version before/after, reason, date, author?
□ Deprecated concepts marked (not deleted)?
□ Version IRI published alongside Ontology IRI?
```

---

## 6. LLM / Automation Assistance in Ontology Preparation

### 6.1 What LLMs Help With (and What They Don't)

LLMs are tools that **prepare ontology data faster** — they are not autonomous ontology builders. Frame their role precisely:

| Task | LLM Role | Human Role Required |
|------|---------|-------------------|
| **Concept extraction from text** | First-pass extraction of candidate concepts from PFMEA/SOP documents | SME validation of every extracted concept before formalization |
| **Synonym identification** | Suggest candidate synonyms across different PFMEA documents | Knowledge engineer confirms which are truly equivalent |
| **Relation extraction** | Extract candidate subject–predicate–object triples from sentences | Expert review; many LLM-extracted relations are incorrect or too specific |
| **Ontology code generation** | Generate OWL/Turtle or Cypher CREATE statements from validated concept list | Engineer reviews and corrects generated code; do not auto-deploy |
| **Consistency checking** | Identify potential logical conflicts in draft ontology | Knowledge engineer interprets findings; LLM false-positives common |
| **Documentation drafting** | Draft concept definitions from existing text | SME reviews and approves all definitions |

**What LLMs cannot reliably do:**
- Determine correct class hierarchy (requires domain judgment)
- Decide what is a class vs. a property vs. an instance (requires modeling expertise)
- Resolve cross-document terminology conflicts (requires SME authority)
- Guarantee logical consistency across a large ontology

---

### 6.2 Hybrid Automated Extraction Pipeline

[[src-234]] [[src-235]] [[src-236]]

```
PHASE 1 — STRUCTURED SOURCE EXTRACTION
Input: ERP/MES database schemas, PFMEA tables (structured)
Tool: RIGOR-style LLM-guided schema-to-ontology extraction
Output: Draft class hierarchy derived from structured data fields
Accuracy: ~90% with chunk integration [[src-236]]

PHASE 2 — UNSTRUCTURED DOCUMENT ENRICHMENT
Input: SOP text, C/S Reports (unstructured)
Tool: LLM with manufacturing-specific prompts + CoT (Chain-of-Thought)
Output: Candidate concepts + relations not present in structured data
Accuracy: ~90% with chunk integration, ~15% without [[src-236]]

PHASE 3 — SEMANTIC MAPPING (LLM-Assisted)
Input: Candidate terms from Phase 1 + 2
Tool: LLM lookup against Glossary (A-3), IOF vocabulary, QUDT units
Output: Canonical term forms, synonym groupings, IOF alignment candidates
Human step: Expert validates each proposed mapping

PHASE 4 — EXPERT VALIDATION (Human-in-the-Loop)
Input: Phase 3 output in structured review format (CSV/table)
Tool: Structured review sessions (SME + Knowledge Engineer)
Output: Validated, corrected, finalized concept/relation list
[[src-233]] [[src-234]]

PHASE 5 — FORMAL ONTOLOGY GENERATION
Input: Validated concept/relation list
Tool: Protégé (manual) or code generation (LLM + human review)
Output: OWL file or Neo4j schema definition
```

**Critical finding from comparative research [[src-236]]:** Graphs built from either structured (RDB) or text-based (LLM extraction) sources without integrating document chunks achieve only 15–20% accuracy on domain-specific queries. Adding text chunks as node attributes boosts accuracy to 90% — matching full GraphRAG baselines. This confirms the hybrid approach (ontology structure + document chunks) is necessary.

---

### 6.3 Accuracy Benchmark

[[src-236]]

| Approach | Accuracy on Domain Queries (20-question eval) |
|---------|----------------------------------------------|
| RDB-derived ontology + document chunks | 90% |
| Text-derived ontology + document chunks | 90% |
| GraphRAG (standard) | 90% |
| Vector RAG (no ontology) | 60% |
| RDB-derived ontology only (no chunks) | 20% |
| Text-derived ontology only (no chunks) | 15% |

**Interpretation:** The ontology structure alone is insufficient for factual grounding — document chunks must accompany the graph. However, the ontology structure improves vector RAG baseline from 60% to 90% when combined with chunks. This is the measurable value of ontology for AI retrieval.

---

## 7. Consensus & Divergence

### Where There Is Strong Consensus

1. **Methodology choice does not matter as much as using one.** All recognized sources (METHONTOLOGY, NeOn, OD101, Uschold & King) agree that iterative, staged development with domain expert involvement produces better ontologies than ad hoc concept lists. The specific methodology is secondary to the discipline of following any structured process.

2. **Start small.** Every practitioner source warns against monolithic enterprise ontology attempts. Small scope → AI value demonstration → organic expansion is the universally recommended path.

3. **Human validation is non-negotiable in LLM-assisted workflows.** All LLM-ontology papers (src-234, src-235, src-236) agree LLMs are accelerators, not replacements for expert judgment. LLMs cannot reliably determine class hierarchy or resolve cross-document terminology conflicts.

4. **Deprecate before delete.** All versioning sources (src-227, src-228) align on keeping deprecated concepts with clear markers rather than deleting, to protect downstream consumers.

### Where Divergence Exists

**On LPG vs RDF — this is the primary architectural debate:**

- **RDF-advocate position (Enterprise Knowledge [src-240], Fluree [src-207], Stardog [src-230]):** RDF's formal semantics, W3C standardization, and OWL reasoning capabilities make it the only sustainable foundation for true enterprise knowledge graphs. "For pure analytics, LPG may feel faster. For building sustainable, interoperable graphs — RDF delivers the bigger payoff." LPG's vendor lock-in, lack of formal axioms, and absence of Open World Assumption are structural limitations.

- **LPG-advocate position (Memgraph [src-224], Enterprise Knowledge analytics use case [src-240], Neo4j [src-237]):** LPG's direct edge traversal, edge-property support, schema flexibility, and developer accessibility make it the practical choice for performance-critical enterprise applications. The ISO GQL 2024 standard addresses the vendor lock-in concern. For 6+ hop manufacturing reasoning chains, LPG's avoidance of triple join explosion is decisive.

- **Resolution:** The debate is genuinely conditional on use case. External interoperability and OWL reasoning → RDF. Closed-enterprise deep-path analytics and developer accessibility → LPG. For the manufacturing root-cause reasoning use case (long paths, closed enterprise environment, performance-critical), **LPG is the better-supported choice** — but this is a considered tradeoff, not a universal truth. RDF would be the right choice if the same ontology needed to be shared with external suppliers or regulatory bodies using IOF-aligned schemas.

**On reasoning approach (materialization vs query-time):**
- Stardog advocates query-time as more flexible and always-current [[src-230]]
- GraphDB advocates materialization as faster for stable T-Box scenarios [[src-230]]
- Practical consensus: the right choice depends on T-Box stability. Stable schema → materialize for query speed. Rapidly evolving schema → query-time to avoid frequent re-materialization.

**On IOF adoption timing:**
- Some sources imply IOF alignment should be built in from the start for proper semantic interoperability
- The IOF releases themselves [[src-226]] suggest a pragmatic progression from normative to provisional modules
- Most practitioner guidance recommends deferring full IOF alignment until after initial ontology validation — the cognitive overhead of BFO is too high for early-stage work

---

## 8. Sources

| Source | Key Contribution |
|--------|-----------------|
| [[src-221]] — LibreTexts/Keet, Ontology Methodologies | Comparative table: METHONTOLOGY vs NeOn vs OD101 vs Summit 2013 |
| [[src-222]] — NeOn Methodology, OEG UPM | Nine scenarios; ontology network lifecycle; affiliate extension pattern |
| [[src-223]] — Uschold & King 1995, AIAI Edinburgh | Original four-phase methodology; ontology capture; term ambiguity handling |
| [[src-224]] — Memgraph LPG vs RDF | LPG performance advantage for multi-hop; triple explosion problem; schema flexibility |
| [[src-225]] — TigerGraph GQL ISO 2024 | ISO/IEC 39075:2024 publication date (April 12, 2024); openCypher → GQL migration path |
| [[src-226]] — IOF Releases, GitHub | Domain coverage; BFO adoption (2019); normative/provisional distinction; YYYYMM versioning |
| [[src-227]] — Enterprise Knowledge, Versioning | SEMVER for ontologies; deprecation protocol; dual IRI policy; governance components |
| [[src-228]] — Galaxy, Operating Model | Three-layer governance; risk-based change classification; impact assessment framework |
| [[src-229]] — PuppyGraph, Neptune vs Neo4j | Query language comparison; RDF/SPARQL support in Neptune; deployment models |
| [[src-230]] — Stardog vs GraphDB | Reasoning approaches (query-time vs materialization); OWL profile support; virtualization |
| [[src-231]] — PuppyGraph, TigerGraph vs Neptune | GSQL vs SPARQL; ontology support gap in TigerGraph; Neptune RDF capabilities |
| [[src-232]] — metaphacts governance guide | Role-based governance lifecycle; 5-state lifecycle (Development → Archive) |
| [[src-233]] — PMC, concept maps elicitation | Six-stage elicitation process; concept map technique; structured interview questions |
| [[src-234]] — Frontiers, LLM collaborative design | HyWay six-stage methodology; LLM as constrained accelerator; human-in-the-loop validation |
| [[src-235]] — arXiv 2602.01276, LLM-driven EKG | Entity extraction → relationship discovery → property specification → expert validation |
| [[src-236]] — arXiv 2511.05991, onto learning vs RAG | Accuracy benchmark: hybrid 90% vs structure-only 15–20%; chunk integration critical |
| [[src-237]] — Neo4j, Ontologies in Neo4j | Class hierarchy as LPG graph pattern; NeoSemantics bridge to RDF; hierarchy traversal queries |
| [[src-238]] — The Ontologist, T-Box/A-Box | T-Box vs A-Box distinction; materialization tradeoff; governance implications |
| [[src-239]] — ResearchGate, PFMEA Ontology | PFMEA concept extraction; Defect/Cause/Action mapping; cross-line fault transfer |
| [[src-240]] — Enterprise Knowledge, RDF & LPG | RDF-advocate perspective; model-driven vs data-first distinction; vendor lock-in concern |

---

## 9. Related

- `research-A-what.en.md` — What is an ontology: components, T-Box/A-Box, OWL/SHACL, IOF background
- `research-C-why-when.en.md` — Why ontology, when to apply (decision criteria), pain points vs benefits
- `research-D-kpi-roadmap.en.md` — KPIs for ontology quality, adoption roadmap, maturity model
- `research-E-architecture.en.md` — Architecture decision detail from earlier Korean research pass
- `B-3 온톨로지.md` — Main guide document (Korean) — this research informs §4 (How) and §5 (Architecture)
- `_작업 메모.md` — Local work notes, feedback log, decisions
