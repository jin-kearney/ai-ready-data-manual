---
type: research
lang: en
date: 2026-06-19
cluster: C — WHY + WHEN
topic: B-3 Ontology
tags: [why, when, graphrag, multi-hop, manufacturing, defect-root-cause, decision-criteria, vector-rag, causal-reasoning]
sources: [src-241, src-242, src-243, src-244, src-245, src-246, src-247, src-248, src-249, src-250, src-251]
---

# B-3 Ontology — Research Cluster C: WHY + WHEN

**Purpose of this file:** Supply concept/structure-first material for the WHY (what breaks without an ontology) and WHEN (adoption judgement) sections of the B-3 guide. Not a market survey — focused on cause-effect understanding and decision criteria.

---

## 1. WHY — What Fails When AI Has Data but No Ontology

### 1.1 The core structural gap: data without explicit relations

AI systems without a relational knowledge layer face a hard architectural limit: they can retrieve text that *mentions* concepts, but they cannot *traverse the connections between* concepts.

**The failure chain:**

```
Data exists in many documents/systems
        ↓
No explicit relation layer
        ↓
AI can only do keyword/vector similarity search
        ↓
"Why did this defect occur?" → no traversable causal chain
        ↓
AI returns the most similar chunk, not the actual cause
```

Vector embeddings compress text into mathematical proximity scores. When a query arrives, the system finds the chunks most *semantically similar* to the query words — but semantic similarity is not the same as causal or hierarchical relationship. A chunk about "surface contamination" and a chunk about "weld desoldering" may be semantically distant even though one is the physical cause of the other.

**Source:** [[src-245]] (SingleStore): "Vector search retrieves chunks that are individually relevant, but it does not explicitly capture how pieces of information connect across chunks. The system performs blind similarity matching without understanding relationships between entities."

**Source:** [[src-241]] (Microsoft Research): "Baseline RAG struggles to connect the dots. This happens when answering a question requires traversing disparate pieces of information through their shared attributes."

### 1.2 What becomes impossible without an ontology

| Capability | Without ontology | With ontology + knowledge graph |
|---|---|---|
| Term unification across systems | Requires manual synonym lookup per query | Ontology maps synonyms to canonical concepts; query once, find across all systems |
| Hierarchical reasoning | "Is desoldering a bonding failure?" cannot be answered automatically | Class hierarchy: Desoldering → BondingFailure → WeldDefect — inferred automatically |
| Causal traversal | "Plate wrinkles → desoldering" is not discoverable from text similarity | Explicit `causes` relation traversed in one graph hop |
| Multi-hop root cause | "Why did defect X occur across three different lines?" impossible without a unified model | Knowledge graph bridges FMEA, MES, and SOP through shared ontology concepts |
| Cross-system question | Agent confined to one system at a time | Agent traverses ERP → MES → SCADA via relation edges |

**Source:** [[src-246]] (Neo4j): "Data stored in columns and rows makes it difficult for AI to access the relationships and context they need to produce useful, reliable answers." Without a knowledge layer, AI cannot understand how past events causally connect to current decisions.

**Source:** [[src-249]] (Cognee): Standard knowledge graphs are "limited to explicit information" — finding only what is written, never what can be logically deduced. An ontology-enhanced graph can infer a complete manufacturer hierarchy from formal class rules, whereas a plain graph shows only what is literally stated.

### 1.3 The specific failure: knowledge scattered across documents and systems

Manufacturing knowledge is not in one place. Root cause analysis for a weld defect requires:

- **PFMEA worksheet:** known failure modes and their causes
- **SOP / work instructions:** required process parameters and tolerances
- **MES records:** actual parameter values at the time of the defect
- **Equipment logs:** welding gun state, electrode cap wear, alarm history
- **C/S (Corrective/Submission) reports:** past resolutions for the same defect code

These five sources use different terminology (a "nugget diameter" in PFMEA may be called "weld diameter" in MES), different schemas, and different identifiers. Vector RAG retrieves from each in isolation — it cannot trace the path from MES parameter deviation back to PFMEA root cause to SOP corrective action, because that path only exists if the concepts are formally related.

**Source:** [[src-244]] (arXiv 2510.15428): "FMEA worksheets' reuse across heterogeneous lines is hindered by natural language variability, inconsistent terminology, and process differences." The ontology-guided approach transforms FMEA worksheets into "a unified knowledge graph … capturing domain concepts such as actions, states, components, and parameters."

**Source:** [[src-251]] (Industrial AI Ordo): "Without ontology and standardized relationships, manufacturing knowledge remains trapped in local systems, preventing enterprise-wide reasoning about anomalies and patterns."

### 1.4 Concrete manufacturing causal chain: welding defect

This example shows exactly what an ontology enables that vector RAG cannot:

**Defect:** Desoldering (welding gun fails to create a proper bond)

**Causal chain (from CN Patent 114943415A):**
```
Plate surface has wrinkles
    → increased contact resistance at the weld point
    → formula E = I²RT: same current I produces more heat
    → nugget overheats
    → desoldering
```

**Why vector RAG cannot answer "why did desoldering occur?":**
- The physics formula E=I²RT lives in an engineering manual
- The plate wrinkle measurement lives in incoming QC records
- The contact resistance value lives in equipment logs
- The nugget temperature lives in MES sensor data
- The defect type "desoldering" lives in the inspection report

No single chunk contains the full chain. Semantic similarity between "desoldering" and "plate wrinkle measurement" is near zero — they use different vocabulary. Only explicit `causes` and `relatedParameter` relations in a knowledge graph can traverse this chain in one query.

**Source:** [[src-250]] (CN Patent 114943415A): Quality portrait map documents "plate surface wrinkles → increased contact resistance → excessive nugget heat → overburning" as explicit factor transmission paths.

---

## 2. WHY — How an Ontology-Backed Knowledge Graph Specifically Helps AI

### 2.1 GraphRAG: graph traversal replaces pure semantic search

GraphRAG (Graph-augmented Retrieval Augmented Generation) combines two retrieval mechanisms:
1. Vector similarity: finds semantically related text chunks (broad)
2. Graph traversal: follows explicit entity-relation paths (deep and precise)

The graph traversal step is only possible if nodes (concepts) and edges (relations) have been formally defined — i.e., if an ontology exists.

**How it works:**
```
Query: "Why did this weld defect occur?"
  ↓
Entity extraction → "weld defect X"
  ↓
Graph lookup: WeldDefect X --hasCause--> ContactResistanceAnomaly
  ↓
Graph lookup: ContactResistanceAnomaly --causedBy--> SurfaceContamination
  ↓
Graph lookup: SurfaceContamination --detectedIn--> IncomingQCRecord #2024-0311
  ↓
LLM generates answer grounded in traversed evidence chain
```

Without the ontology defining `hasCause`, `causedBy`, `detectedIn` as typed relations, there is no graph to traverse.

**Source:** [[src-241]] (Microsoft Research): "The LLM can ground itself in the graph and results in a superior answer that contains provenance through links to the original supporting text."

**Source:** [[src-245]] (SingleStore): Multi-hop example: De Niro → Goodfellas → directed_by → Scorsese. Manufacturing equivalent: Defect X → hasCause → ParameterDeviation → observedIn → MES Record #Y.

### 2.2 Accuracy benchmarks (use conservatively — confirm primary sources)

The following numbers are from vendor/researcher benchmarks and should be treated as directional evidence, not as authoritative figures. The presenter should confirm with the primary publications before citing in a deck.

| Benchmark | Metric | Traditional RAG | GraphRAG | Source |
|---|---|---|---|---|
| Lettria hybrid (diverse technical domains) | Correct answers | 50.83% | 80% | [[src-242]] (AWS blog citing Lettria) — **confirm Lettria primary publication** |
| Lettria hybrid (technical specifications) | Correct answers | 46.88% | 90.63% | [[src-242]] — **confirm** |
| FMEA fault cause identification (automotive) | F1@20 | 0.267 (RAG baseline) | 0.523 (ontology-guided KG) | [[src-244]] arXiv 2510.15428 — peer-reviewed |
| Cornell LLM Q&A (cited by Neo4j) | Accuracy | lower (SQL baseline) | 3× improvement over SQL | [[src-246]] — **confirm Cornell paper** |

**Conservative framing for the guide:** Do not assert specific percentages unless the presenter confirms the primary source. Instead: "Studies and vendor benchmarks consistently show that knowledge-graph-augmented retrieval outperforms plain vector RAG on relational, multi-hop questions — with some benchmarks showing correct-answer rates rising from the 50% range to the 80–90% range on technical specifications [cite source + note to confirm]."

### 2.3 Why grounding matters beyond accuracy: explainability

An agent that answers "this defect was caused by surface contamination on line 3" must also be able to trace the exact evidence path — which MES record, which PFMEA entry, which expert rule — or the answer is not auditable.

**Source:** [[src-241]] (Microsoft Research): GraphRAG "contains provenance through links to the original supporting text."

**Source:** [[src-245]] (SingleStore): "Each answer can be traced back to specific nodes, edges, and text chunks — enabling verifiable, multi-step reasoning."

For manufacturing quality management, this provenance matters: an AI recommendation without an auditable evidence chain cannot be used in a regulated corrective action process.

---

## 3. WHEN — Adoption Judgement: Build vs. Simpler Alternative

### 3.1 The decision spectrum: glossary → taxonomy → ontology → knowledge graph

These are not competing alternatives but a spectrum of increasing richness and cost. Choose the simplest level that meets the requirement.

```
Glossary
  → Defines terms; no structure between terms
  → Use when: need consistent vocabulary; single-level term unification
  → Cost: lowest; maintained in a spreadsheet or wiki

Taxonomy
  → Adds hierarchy (IS-A): Product Type > Welding Defect > Surface Defect
  → Use when: need to classify and navigate; users think categorically
  → Cannot do: represent non-hierarchical relations; inference; cross-domain queries
  → Cost: weeks to build with subject-matter experts

Ontology
  → Adds formal semantics: typed relations, constraints, inference rules
  → Use when: relations between concepts are as important as the concepts themselves
  → Enables: logical inference, cross-system interoperability, reasoning
  → Cost: months + domain expert + ontology engineer

Knowledge Graph
  → Ontology + instance data (actual entities, actual events)
  → Use when: AI agents must traverse relations at query time over real data
  → Enables: GraphRAG, multi-hop question answering, root cause traversal
  → Cost: highest; requires graph database + ontology governance
```

**Sources:** [[src-243]], [[src-247]], [[src-248]]

### 3.2 Build an ontology when — concrete criteria

**Criterion A: Knowledge is scattered across multiple documents/systems AND must be connected**

If the answer to a question requires pulling together information from more than one system or document type, and those systems use different terminology for the same concept, a glossary cannot help — it unifies terms but does not connect the knowledge. An ontology provides the shared structure that makes the connection possible.

Example triggers:
- PFMEA, SOP, MES, and equipment logs each describe the same production process in their own vocabulary
- Customer complaint data and internal inspection records use different defect codes
- Multiple plant sites have local naming conventions for the same equipment

**Source:** [[src-248]] (Enterprise Knowledge): "A combination of taxonomies and ontologies can connect users to both content and data" (not just content alone). Cross-silo example: separate classifications for Reports, Employees, Media → unified via semantic relation "Employee _created_ File Type."

**Criterion B: Cause-effect relations matter (root cause analysis, recommendations, predictions)**

If the question is not "what is X?" but "why did X happen?" or "what should we do about X?", the answer requires traversing causal relations. Causal relations must be explicitly defined — they cannot be inferred from semantic similarity.

Example triggers:
- Need to trace a production defect back to its root process cause
- Need to generate AI-driven corrective action recommendations
- Need to explain why a maintenance event occurred

**Source:** [[src-250]] (CN Patent): The welding knowledge graph explicitly encodes `causes` paths — without them, "analysis is more dependent on expert experience" with "low flexibility."

**Criterion C: An AI Agent must judge, recommend, or analyze across multiple data sources**

AI agents that must navigate across ERP, MES, SCADA, and documents without a relational layer are "confined to single platforms" — they cannot reason across disconnected systems.

**Source:** [[src-251]] (Industrial AI Ordo): "Industrial AI exposes a hard constraint: agents cannot reason across disconnected systems."

**Criterion D: The same concept has different names across systems (AND relations matter, not just synonyms)**

If the only problem is naming inconsistency — "weld defect" vs. "welding fault" — a glossary or thesaurus may suffice. But if the question is "how does this defect relate to the process parameter that caused it?" then relations are needed, and an ontology is required.

**Source:** [[src-247]] (SGKG): "The taxonomy-to-ontology transition occurs when relationships between entities are as important as the entities themselves."

### 3.3 Do NOT build an ontology when — cheaper alternatives suffice

**When a glossary is enough:**
- Need is purely term unification: "field A in System 1 = field B in System 2"
- No relational queries planned
- Users only need to look up what a term means
- Maintenance must be done by non-specialists

**When a taxonomy is enough:**
- Need is to classify and navigate hierarchically: "What defect types exist under surface defects?"
- Data fits naturally into a tree (IS-A only)
- No cross-category relationships needed
- Quick build timeline required (weeks vs. months)

**When a relational database is enough:**
- Relationships are fixed, tabular, and well-understood in advance
- Schema does not evolve dynamically
- No need to infer unstated relationships
- Performance on bulk data operations is critical

**Source:** [[src-247]] (SGKG): "Organizations frequently build ontologies when taxonomies would suffice, creating unnecessary complexity that hinders adoption." Use the simplest structure that meets the requirement.

**Source:** [[src-243]] (Neo4j): "Knowledge graphs can start simple with just taxonomy and add ontological rigor later as needs evolve."

### 3.4 The boundary between glossary and ontology (crisp)

| Situation | Correct tool | Why |
|---|---|---|
| Align MES field "welding fault code" with PFMEA "failure mode code" | Glossary / data dictionary (A-3) | Term-level mapping; no relation traversal needed |
| Answer "What defect types exist?" with consistent names across plants | Taxonomy | IS-A hierarchy; classification only |
| Answer "What process parameters are associated with desoldering?" | Ontology relation: `associatedParameter` | Typed relation between defect and process parameter concepts |
| Answer "Why did desoldering occur in this batch, trace to root cause?" | Knowledge graph + ontology | Multi-hop causal traversal across MES, PFMEA, equipment logs |
| Agent recommends corrective action based on defect + context | Knowledge graph + ontology + agent | Agent must traverse relations AND access instance data |

### 3.5 When ontology preparation is a prerequisite for GraphRAG

GraphRAG requires a knowledge graph. A knowledge graph requires:
1. Nodes (entities) formally defined with consistent types → needs at minimum a taxonomy
2. Edges (relations) typed with formal semantics → needs an ontology
3. Instance data (actual events, actual measurements) loaded → needs data preparation

A GraphRAG deployment without an underlying ontology will have "connections but no consistent rules for what those connections mean — data but no semantic foundation to interpret it." [[src-243]]

**Practical prerequisite checklist:**
- [ ] Core domain concepts defined and agreed (ontology T-Box)
- [ ] Key relations typed: `hasCause`, `relatedParameter`, `occursAt`, `hasCorrectiveAction`
- [ ] Synonym mapping across source systems resolved
- [ ] Instance data quality sufficient (garbage in = garbage graph)

**Source:** [[src-251]]: "Knowledge graphs expose but don't fix bad data — foundational architecture must come first."

---

## 4. Manufacturing Scenario: Welding Defect Root Cause (Worked Example)

**Context:** Heavy equipment manufacturer. Welding defects appear on assembly line 3. Quality engineer asks AI agent: "Why is the desoldering rate on Line 3 higher than Lines 1 and 2 this month? What should we check?"

**Without ontology:**
- Vector RAG finds text chunks mentioning "desoldering" and "Line 3" — returns PFMEA entries for desoldering defects generically
- Cannot cross-reference MES parameter values for Line 3 vs. Lines 1 and 2 (different systems, different schemas)
- Cannot trace to equipment log showing elevated electrode cap wear on Line 3
- Agent output: generic advice ("check contact resistance" — from PFMEA text) with no specificity to Line 3's situation

**With ontology + knowledge graph:**
- Agent traverses: `Line3 --hasEquipment--> WeldingGun_G07 --currentState--> ElectrodeCapWear=HIGH`
- Agent traverses: `ElectrodeCapWear=HIGH --causes--> IncreasedContactResistance --causes--> ExcessiveNuggetHeat --causes--> Desoldering`
- Agent checks: Line 1 and Line 2 have `ElectrodeCapWear=NORMAL`
- Agent output: "Line 3's elevated desoldering rate is associated with high electrode cap wear on Gun G07 (last replaced 38 days ago; replacement threshold is 30 days). Recommended action: cap replacement — see SOP-WELD-047 §3.2."

**What the ontology enabled:**
1. Class hierarchy: `Desoldering` is a `BondingFailure` is a `WeldDefect`
2. Causal relation: `ElectrodeCapWear --causes--> ContactResistanceAnomaly`
3. Process parameter relation: `WeldingGun --hasMaintenanceCycle--> CapReplacementInterval`
4. Cross-system join: equipment entity in MES linked to maintenance record in EAM via shared ontology concept `WeldingGun`

None of these hops are possible from semantic similarity alone.

**Source basis:** [[src-250]] (welding knowledge graph patent), [[src-244]] (FMEA ontology paper), [[src-251]] (manufacturing KG scenario).

---

## 5. Consensus & Divergence

**Strong consensus across all sources:**

1. Vector/keyword RAG cannot traverse explicit causal or hierarchical relations — this is a structural limitation, not a tuning problem. All sources (Microsoft, AWS, SingleStore, cognee, Neo4j) agree on this.

2. An ontology is NOT needed when only term unification is required — a glossary or taxonomy suffices. Multiple independent sources (Neo4j, SGKG, Enterprise Knowledge) warn against over-engineering.

3. The adoption decision is a spectrum: glossary → taxonomy → ontology → knowledge graph. The trigger for moving up the spectrum is when "relationships between entities are as important as the entities themselves."

4. Manufacturing use cases (FMEA, root cause, cross-system traceability) are legitimately complex enough to justify ontology investment — confirmed by peer-reviewed papers (arXiv 2510.15428), patent literature, and practitioner sources.

**Divergences and cautions:**

1. **Performance numbers vary significantly.** Lettria benchmark (via AWS, [[src-242]]) shows 50.83% → 80% correct answers for GraphRAG vs. vector RAG. The arXiv FMEA paper ([[src-244]]) shows F1@20 of 0.267 (RAG) vs. 0.523 (ontology-guided KG). Neither is from a neutral third party — the Lettria figure comes from a vendor blog. Numbers circulating as "Stanford study: 35–45% reduction in factual errors" were not traceable to a primary source in this research pass. **Use numbers conservatively; flag as requiring primary-source confirmation.**

2. **Ontology scope and cost.** Vendor sources (Neo4j, AWS) tend to understate the cost and maintenance burden of ontology development. Academic sources are more candid about the need for domain expert involvement, formal methodology, and ongoing governance. The guide should balance enthusiasm with realistic scope guidance.

3. **"Ontology-first" vs. "graph-first" camps.** Neo4j and RDF/OWL communities disagree on whether formal ontologies (OWL, SHACL) are required or whether a property graph with informal labeling is sufficient. For the purpose of the B-3 guide, the position is: for *reasoning and inference*, formal semantics are needed; for *basic graph traversal*, informal property graphs can work but accumulate ambiguity over time.

4. **LLM can partially compensate.** A sufficiently capable LLM can sometimes infer causal chains from context even without a formal knowledge graph — but only if all the relevant information fits in the context window and the LLM has appropriate domain knowledge. For enterprise manufacturing data scattered across multiple systems over years of history, context-window-based reasoning cannot scale. Ontology + graph is the structural solution.

---

## 6. Sources

| Wikilink | Title | URL |
|---|---|---|
| [[src-241]] | GraphRAG: Unlocking LLM Discovery — Microsoft Research Blog | https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/ |
| [[src-242]] | Improving RAG Accuracy with GraphRAG — AWS ML Blog | https://aws.amazon.com/blogs/machine-learning/improving-retrieval-augmented-generation-accuracy-with-graphrag/ |
| [[src-243]] | Taxonomy vs. Ontology vs. Knowledge Graph — Neo4j | https://neo4j.com/blog/knowledge-graph/taxonomy-vs-ontology-vs-knowledge-graph/ |
| [[src-244]] | Fault Cause ID via Ontology-Guided FMEA — arXiv 2510.15428 | https://arxiv.org/abs/2510.15428 |
| [[src-245]] | GraphRAG Improves Multi-Hop Reasoning — SingleStore | https://www.singlestore.com/blog/rethinking-rag-how-graphrag-improves-multi-hop-reasoning-/ |
| [[src-246]] | Enterprise AI Knowledge Layer — Neo4j Blog | https://neo4j.com/blog/agentic-ai/knowledge-layer/ |
| [[src-247]] | Ontology vs Taxonomy Decision Framework — SGKG | https://sgkg.org/blog/2026-03-21-ontology-vs-taxonomy-knowledge-organisation/ |
| [[src-248]] | Extending Taxonomies to Ontologies — Enterprise Knowledge | https://enterprise-knowledge.com/extending-taxonomies-to-ontologies/ |
| [[src-249]] | Enhancing KG with Ontology Integration — Cognee | https://www.cognee.ai/blog/deep-dives/ontology-ai-memory |
| [[src-250]] | Metal Welding Defect Root Cause via KG — CN Patent 114943415A | https://patents.google.com/patent/CN114943415A/en |
| [[src-251]] | Knowledge Graphs in Manufacturing: 20 Questions — Industrial AI Ordo | https://coformation.medium.com/knowledge-graphs-in-manufacturing-20-practical-questions-b86c863d5c4c |

---

## 7. Related

- **research-A-what-components.en.md** (or equivalent) — ontology components (T-Box, A-Box, relations) explained
- **B-3 온톨로지.md** — guide main document (reads this file for WHY/WHEN sections)
- **A-3 Glossary** — the simpler alternative when only term unification is needed
- **D-2 Tool/API Specification Data** — AI agent's operational data layer that the ontology helps contextualize
- **Microsoft GraphRAG paper:** https://arxiv.org/abs/2404.16130 — confirm "comprehensiveness" improvement claim against this paper
- **Lettria primary publication:** locate via AWS blog for precise benchmark figures
