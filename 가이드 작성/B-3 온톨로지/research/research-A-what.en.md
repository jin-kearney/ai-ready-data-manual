---
title: "B-3 Ontology — WHAT Cluster Research Notes (English Pass)"
topic: Ontology
topic-code: B-3
type: research
lang: en
date: 2026-06-19
tags: [ai-ready-data, B-3, research, what]
---

# B-3 Ontology — WHAT Cluster Research Notes

> **Cluster scope:** Definition + boundary | 6-component structure | Triples + T-Box/A-Box | How reasoning works (manufacturing causal paths) | Standards landscape | Glossary

---

## 1. Plain Definition + Boundary

### 1.1 What an Ontology Is

An ontology is **a formal, explicit specification of a shared conceptualization of a domain** — a structured knowledge model that defines what concepts exist, what properties they have, and how they relate to each other, in a machine-readable and machine-reasoned form.

> W3C OWL2 Primer [[src-201]]: "A set of precise descriptive statements about some part of the world." It combines terminological knowledge (vocabulary, hierarchy, relationships) with assertional knowledge (concrete facts about specific objects).

> Ontotext [[src-202]]: "A formal description of knowledge as a set of concepts within a domain and the relationships that hold between them."

**In plain terms:** Think of an ontology as a "concept map with rules" — it not only lists terms but explicitly says how they connect, what constraints apply, and from those rules, what can be inferred automatically.

**Manufacturing framing (B-3):** A manufacturing ontology defines that a `Defect` *occurs-in* a `Process`, *is detected-by* an `Inspection-item`, and *has-cause* an `Equipment` state — and from those declared relations, an AI can automatically traverse the path: Defect → Cause → Action to suggest remediation without being individually programmed for each defect type.

### 1.2 What an Ontology Is NOT — Boundary Table

| Structure | What it does | What it does NOT do | B-3 boundary |
|-----------|-------------|---------------------|--------------|
| **Glossary** (→ A-3) | Defines meaning of individual terms/words | Does not model relationships between concepts | Single-term definitions live in A-3, not B-3 |
| **Taxonomy** | Organizes concepts in is-a hierarchy (parent → child) | Only hierarchy; no lateral relations, no rules, no inference | A taxonomy is a subset of an ontology (hierarchy component only) |
| **SKOS vocabulary** (→ A-3 adjacent) | Controlled vocabulary with broader/narrower/related labels | No formal class logic, no axioms, no OWL inference | SKOS = labeling layer; OWL = reasoning layer |
| **Schema / Data model** | Defines field structure for data storage | No semantics or inference rules | Database schema defines fields; ontology defines meaning + inferences |
| **Knowledge Graph** | Stores and queries instance-level facts (A-Box) | By itself, no formal concept schema; optional reasoning | KG = ontology (T-Box) + instance data (A-Box) realized together |
| **Metadata** (→ A-2) | Describes properties of a data asset | Does not define relations between domain concepts | Asset description ≠ domain concept network |

> Neo4j [[src-203]]: "A knowledge graph is the instantiation of an ontology, and an ontology is the knowledge model." The ontology is the blueprint; the knowledge graph is the structure built from it plus populated with data.

> PuppyGraph [[src-212]]: Ontology = conceptual level (stable, prescriptive). Knowledge Graph = instance level (dynamic, operational).

---

## 2. The 6-Component Structure

The locked canonical model for B-3 uses **6 components**. Research confirms these map cleanly to W3C OWL + LPG terminology.

### 2.1 Component Overview

| # | Component | One-line definition | OWL mapping | Manufacturing example |
|---|-----------|-------------------|-------------|----------------------|
| 1 | **Class (개념/클래스)** | A named category grouping entities that share common characteristics | `owl:Class` | Defect, Equipment, Process, Product |
| 2 | **Instance (인스턴스)** | A specific individual object that belongs to one or more classes | `owl:NamedIndividual` | "Scratch-defect-20240305" is an instance of Defect |
| 3 | **Property (속성)** | An attribute of a class or instance — either a data value or a link to another individual | `owl:DatatypeProperty` / `owl:ObjectProperty` | severity (data value), defectCode (data value) |
| 4 | **Relationship (관계)** | A directional link between two classes or instances expressing how they connect | `owl:ObjectProperty` (directed) | causes, detected-by, occurs-in, remediated-by |
| 5 | **Hierarchy (계층)** | A is-a (subclass) or part-of tree organizing classes from general to specific | `rdfs:subClassOf`, `rdfs:subPropertyOf` | ScratchDefect rdfs:subClassOf SurfaceDefect rdfs:subClassOf Defect |
| 6 | **Axiom/Rule (규칙/공리)** | A formal logical constraint or inference rule that restricts or derives new knowledge | `owl:Axiom`, SWRL rules, OWL restrictions | "If Defect has-cause Equipment AND Equipment belongs-to Line-A, then Defect affects Line-A" |

**Sources:** W3C OWL2 Primer [[src-201]], Ontotext [[src-202]], Factor Firm Ontology 101 [[src-211]], ScienceDirect ontology-concept overview (search result confirmation).

### 2.2 Note on Component Counts Across Sources

Different authors list 3–7 components. This is explained in §7 (Consensus & Divergence). The 6-component canonical model above is the most stable, aligning with W3C OWL's core constructs:
- OWL official documentation names: Classes, Properties, Individuals (= instances), Axioms — 4 top-level types.
- Hierarchy and Relationship are both ObjectProperty subtypes in OWL, but for *communication purposes* they are best treated separately (hierarchy = is-a; relationship = any domain-specific directed connection). This split is standard in ontology engineering pedagogy.

### 2.3 Formal Representation

Formally, an ontology can be expressed as: **O = ⟨C, R, ι, ξ⟩** where:
- C = set of classes/concepts
- R = set of relations
- ι = set of instances
- ξ = set of axioms

Source: arXiv 1509.05434 (ontology building guidelines), confirmed by multiple sources in search results.

### 2.4 The Manufacturing Entity Set — 7 Core Classes + 7 Core Relations

**T-Box (schema layer) — 7 core classes:**
`Product` | `Process` | `Defect` | `Equipment` | `Cause` | `Action` | `Inspection-item`

**7 core directed relationships:**
| Relation | Domain → Range | Direction |
|----------|---------------|-----------|
| `causes` | Cause → Defect | Cause leads to defect |
| `detected-by` | Defect → Inspection-item | Defect found via inspection |
| `occurs-in` | Defect → Process | Defect happens in a process step |
| `remediated-by` | Defect → Action | Defect corrected by action |
| `has-part` | Equipment → Equipment (or Process) | Part-of decomposition |
| `measured-by` | Product/Process → Inspection-item | Quality measured by |
| `affects` | Cause/Defect → Product | Impact path |

These 7 classes × 7 relations form the T-Box skeleton. Instances populate the A-Box.

---

## 3. Triples and T-Box / A-Box

### 3.1 The Triple Model

The fundamental unit of all RDF-based ontologies is the **Triple**: `(Subject, Predicate, Object)`

- Subject = the thing being described (an IRI or blank node)
- Predicate = the property or relation (always an IRI)
- Object = the value or related thing (IRI, blank node, or literal)

**W3C RDF 1.2** [[src-206]]: "Asserting an RDF triple says that some relationship, indicated by the predicate, holds between the resources denoted by the subject and object."

**Example triples from the B-3 manufacturing ontology:**

```
(ScratchDefect-001, rdf:type, Defect)                   ← A-Box: instance classification
(ScratchDefect-001, occurs-in, StampingProcess-Line3)    ← A-Box: instance relation
(ScratchDefect-001, has-cause, DieWear-Equipment-07)     ← A-Box: causal link
(DieWear-Equipment-07, remediated-by, DieReplacement-Action-12) ← A-Box: remediation
(Defect, rdfs:subClassOf, owl:Thing)                    ← T-Box: hierarchy
(ScratchDefect, rdfs:subClassOf, SurfaceDefect)         ← T-Box: subclass
```

An RDF graph is simply "a set of RDF triples" — connecting these triples produces the knowledge graph.

### 3.2 T-Box vs. A-Box

| Layer | Full Name | Contents | Database analogy | Manufacturing example |
|-------|-----------|----------|-----------------|----------------------|
| **T-Box** | Terminological Box | Class definitions, subclass hierarchies, property definitions, axioms — the **schema** | Database schema (DDL) | "Defect is a class; ScratchDefect subClassOf Defect; every Defect must have occurs-in some Process" |
| **A-Box** | Assertional Box | Specific individuals, their class memberships, property values — the **data** | Database rows (DML) | "ScratchDefect-001 is a Defect; it occurs-in StampingProcess-Line3; severity=High" |

**Source:** Telecom Paris DL slides (search result), confirmed by W3C OWL2 Primer [[src-201]] and W3C RDF [[src-206]].

**Key insight for AI data preparation:** 
- T-Box = the ontology asset you design and curate (the B-3 deliverable)
- A-Box = the operational data populated from plant systems (MES, SCADA, QMS) — each new production record becomes new triples in the A-Box
- A well-designed T-Box makes the A-Box queryable via SPARQL and reasoned over by OWL inference engines

### 3.3 Open-World Assumption (OWA)

OWL operates under the **Open-World Assumption**: if a fact is not stated, it is *unknown* (not necessarily false). This contrasts with relational databases' Closed-World Assumption. For AI applications this matters: an OWA system will not incorrectly deny a relationship just because it hasn't been entered yet.

**Source:** W3C OWL2 Primer [[src-201]].

---

## 4. How Ontologies Enable Reasoning (Inference)

### 4.1 Three Inference Mechanisms

**1. Subclass Inheritance (rdfs:subClassOf)**
If `ScratchDefect rdfs:subClassOf SurfaceDefect rdfs:subClassOf Defect`, then:
- Any instance of ScratchDefect is *automatically* inferred to also be an instance of SurfaceDefect and Defect.
- AI system can apply all Defect-level actions to ScratchDefect instances without explicit per-class programming.
- RushDB [[src-208]]: "A reasoner will automatically classify Alice as an :Employee — a behavior impossible in LPG without custom logic."

**2. Transitive Relations**
Some relations are declared transitive in OWL (`owl:TransitiveProperty`). If:
- `CauseA causes DefectB` AND `DefectB affects ProductC`
- With transitivity declared on an appropriate chain, an AI can follow the full path A → B → C.

For manufacturing: if `part-of` is transitive, then "bearing is part-of gearbox, gearbox is part-of press" → "bearing is part-of press." An AI diagnosing press defects can then automatically include bearing failure as a candidate cause.

**3. Axiom-Based Inference**
OWL axioms act as if-then rules over the ontology. Example:
```
IF  Defect occurs-in Process  
AND Process uses Equipment  
AND Equipment has-state Degraded  
THEN Defect has-cause Equipment  (inferred, not explicitly asserted)
```
This lets the AI traverse: `Defect → Process → Equipment` to infer causation without each individual defect-equipment pair being hand-coded. Source: OWL Guide [[src-201]], Jay Wang Medium (search result).

### 4.2 Manufacturing Causal-Path Traversal — Multi-Hop Example

Root-KGD framework [[src-209]] demonstrates the pattern concretely:

**Scenario:** Surface scratch defect detected at final inspection.

```
Hop 1: ScratchDefect-001 –[occurs-in]→ StampingProcess-Line3
Hop 2: StampingProcess-Line3 –[uses]→ DieEquipment-07
Hop 3: DieEquipment-07 –[has-state]→ WornDie  (state instance)
Hop 4: WornDie –[causes]→ ScratchDefect  (T-Box axiom — class level)
Hop 5: ScratchDefect-001 –[remediated-by]→ DieReplacement-Action
Hop 6: DieReplacement-Action –[scheduled-by]→ MaintenancePlan-Q2
```

An AI traversing this 6-hop path can:
- Automatically name the root cause (worn die)
- Suggest the correct remediation (die replacement)
- Link to the maintenance plan
- **Without** needing any free-text search or manual root-cause analysis

**This is only possible because the ontology pre-defined the T-Box relations: occurs-in, uses, has-state, causes, remediated-by, scheduled-by.** Without the ontology schema, the same facts in a flat database would require bespoke SQL joins written by a human analyst.

**Root-KGD key mechanism:** Ripple Fault Propagation Algorithm (RFPA) — simulates fault quantity propagating from candidate source nodes outward through the knowledge graph, with attenuation factors per relation type. Root cause ranked by cosine similarity between simulated and observed fault patterns. [[src-209]]

**FBS model supplement [[src-213]]:** Function-Behavior-Structure ontology for maintenance records — traces failures backward: structural degradation → behavioral anomaly → functional failure. Enables predictive maintenance from accumulated maintenance records.

**FMEA graph supplement [[src-214]]:** Ontology-guided FMEA constructs cross-line fault cause graphs. LLMs guided by the ontology extract causal relationships from free-text FMEA descriptions and structure them as triples. Key: the ontology is the "guide schema" that makes LLM extraction structured and reusable.

### 4.3 LPG vs. RDF for Reasoning

| Feature | RDF + OWL | LPG (Neo4j/property graph) |
|---------|-----------|---------------------------|
| Reasoning | Built-in via OWL reasoners | Custom logic required |
| Ontology support | Robust (RDFS, OWL, SHACL) | Limited |
| Subclass inference | Automatic | Must code explicitly |
| Standards | W3C-standardized | Non-standardized |
| Query language | SPARQL | Cypher, Gremlin |
| Edge properties | Via reification or RDF-star | Native (edges have key-value props) |
| Open-world | Yes | No (closed-world default) |
| Interoperability | High (IRI-based URIs) | Lower |
| Performance | Distributed, slower for traversal | Fast traversal |

Sources: Fluree [[src-207]], RushDB [[src-208]].

**Practical note:** Many enterprise systems (Neo4j, AWS Neptune hybrid, TigerGraph) support *both* models. The ontology T-Box is typically authored in OWL/RDF for semantic rigor, then sometimes projected to LPG for operational query performance.

---

## 5. Standards and Frameworks Landscape

### 5.1 W3C Stack (Bottom to Top)

| Standard | Layer | One-line description | Primary use |
|----------|-------|---------------------|-------------|
| **RDF** (Resource Description Framework) | Data model | Graph data model — subject–predicate–object triples | Foundation for all semantic web data |
| **RDFS** (RDF Schema) | Vocabulary | Adds class/property hierarchy to RDF | Basic taxonomies, domain/range declarations |
| **OWL 2** (Web Ontology Language) | Ontology | Full logical language with classes, properties, axioms; enables machine inference | Full ontologies with reasoning |
| **SKOS** | Vocabulary | Lightweight RDF vocabulary for thesauri/taxonomies (broader/narrower/related) | Controlled vocabularies, A-3 Glossary territory |
| **SHACL** | Validation | Constraint language for validating RDF graphs; defines "shapes" data must conform to | Data quality, ontology constraint enforcement |
| **SPARQL** | Query | Query language for RDF graphs | Querying knowledge graphs |

Sources: W3C OWL2 Primer [[src-201]], W3C RDF [[src-206]], W3C SKOS Primer [[src-210]], Ontotext SHACL [[src-205]], Jay Wang Medium (search result).

### 5.2 SHACL — Key Distinction from OWL

OWL enables **inference** (derives new facts from axioms).  
SHACL enables **validation** (checks that existing data meets constraints).

Example gap that SHACL fills: OWL can declare `familyName` has domain `Person`, but **cannot** require that every Person instance *must have* a `familyName`. SHACL fills this: you write a shape saying "every Person node must have exactly one `familyName` property with a string value." [[src-205]]

For AI data preparation: SHACL = the data quality gate for your ontology-backed knowledge graph. Before loading new manufacturing records into the A-Box, run SHACL validation to catch missing required relations (e.g., a Defect instance missing its `occurs-in` triple).

### 5.3 IOF (Industrial Ontologies Foundry) + BFO

**BFO (Basic Formal Ontology):** An upper-level ontology providing the most abstract foundational concepts (Continuant, Occurrent, Material Entity, Process, etc.). Used as the upper layer in IOF. BFO was selected as the top-level ontology for IOF.

**IOF (Industrial Ontologies Foundry):** An international initiative (NIST, Autodesk, and industry partners) to create a suite of interoperable ontologies for all areas of manufacturing. Structure:
- **BFO** (upper layer) → most abstract
- **IOF Core** (mid-level) → manufacturing-common concepts: processes, materials, equipment, measurements, roles
- **IOF domain ontologies** (domain layer) → supply chain, maintenance, production, lifecycle management

**IOF Core** [[src-204]]: Released in beta v1 (2022). Contains intermediate-level terms deriving from BFO from which domain-specific terms derive. Supports temporal relationships (Allen Interval Algebra), measurement processes, identifiers, role mechanics, integration with OWL Time and QUDT standards.

**Active development** [[src-204]]: Releases through 2025 show active additions — supply chain migration, consumable hierarchies, recipe process classification, structural modularization.

**Why IOF matters for B-3:** Any enterprise manufacturing ontology benefits from aligning with IOF Core — it provides a shared vocabulary that enables interoperability across plant systems, suppliers, and analytics tools. IOF's `Process`, `Equipment`, `MaterialArtifact` classes map directly to the B-3 canonical 7-entity set.

### 5.4 SKOS vs. OWL for Manufacturing Ontologies

| Dimension | SKOS | OWL |
|-----------|------|-----|
| Expressiveness | Low — labels and hierarchy only | High — classes, properties, axioms, inference |
| Reasoning | None | Full OWL reasoning |
| Ease of authoring | Easy (spreadsheet → SKOS) | Moderate (Protégé, ontology tool needed) |
| Use case | Controlled vocabularies, A-3 Glossary | B-3 Ontology (full semantic layer) |
| SKOS concepts are... | OWL individuals (not classes) | — |

A manufacturing glossary of defect codes → SKOS / A-3.  
A manufacturing ontology modeling causal relationships → OWL / B-3.

---

## 6. Glossary — Must-Know Terms for Manufacturing Reader

| Term | Easy one-line gloss |
|------|-------------------|
| **Ontology** | A formal "concept map with rules" — defines what exists in a domain, how concepts relate, and what can be inferred from those relations |
| **Class (클래스)** | A named category grouping similar things (e.g., all defect types grouped under "Defect") |
| **Instance (인스턴스)** | A specific individual object — one particular defect event, one specific piece of equipment |
| **Property (속성)** | A characteristic attached to a class or instance — either a data value (severity = High) or a link to another object |
| **Relationship (관계)** | A directed named link between two concepts: "Defect → occurs-in → Process" |
| **Hierarchy / Taxonomy (계층/분류체계)** | The is-a tree: ScratchDefect is-a SurfaceDefect is-a Defect |
| **Axiom (공리)** | A formal rule the ontology enforces: "If X causes Y and Y occurs-in Z, then X affects Z" |
| **Triple (트리플)** | The atom of knowledge: Subject–Predicate–Object (e.g., Defect001–occurs-in–StampingProcess) |
| **T-Box** | The concept schema layer — defines all the classes, relations, and rules (the "dictionary") |
| **A-Box** | The instance data layer — all the specific facts loaded from real records (the "data") |
| **RDF** | W3C standard — stores facts as triples in a graph; the foundation format for semantic web data |
| **OWL** | W3C standard — extends RDF with formal logic to define ontologies and enable automated reasoning |
| **SKOS** | W3C standard — lightweight vocabulary for thesauri/taxonomies; no reasoning; closer to A-3 glossary |
| **SHACL** | W3C standard — validates that RDF data meets constraints (the quality-gate companion to OWL) |
| **LPG** | Labeled Property Graph — graph model used by Neo4j/TigerGraph; nodes+edges both carry key-value properties; less formal than RDF but faster for traversal |
| **Knowledge Graph** | An ontology (T-Box) populated with instance data (A-Box) and queryable as a graph |
| **Inference / Reasoning** | Automated derivation of new facts from declared rules — e.g., inferring root cause from causal path without explicit programming |
| **IOF** | Industrial Ontologies Foundry — international standard manufacturing ontology suite built on BFO; aligning with it ensures interoperability |
| **BFO** | Basic Formal Ontology — the upper-level abstract foundation that IOF (and many domain ontologies) build upon |

---

## 7. Consensus & Divergence

### 7.1 Consensus — Safe Canonical Core

All authoritative sources agree on these points:

1. **Triple as the atomic unit.** RDF subject–predicate–object triples are universally accepted as the representation unit for semantic ontologies. W3C, all academic, and vendor sources concur. [[src-201, src-206]]

2. **T-Box / A-Box distinction.** Universally used in description-logics and OWL literature. T-Box = schema (concept definitions, rules); A-Box = instance data. All academic sources confirm. [[src-201]]

3. **Classes, Properties, Individuals, Axioms** as the four top-level OWL ontology constructs. This is the W3C OWL 2 official model. [[src-201]]

4. **Ontology enables inference that taxonomy does not.** All sources distinguish: taxonomy = hierarchy only; ontology = hierarchy + lateral relations + axioms + inference. [[src-202, src-203, src-211]]

5. **Knowledge Graph = Ontology (T-Box) + Instance Data (A-Box).** Confirmed across Neo4j [[src-203]], PuppyGraph [[src-212]], Ontotext [[src-202]] — all use the same framing.

6. **RDF + OWL = reasoning; LPG = no built-in reasoning.** Confirmed by Fluree [[src-207]] and RushDB [[src-208]]. LPG (Neo4j, etc.) requires custom logic to achieve what OWL inference does automatically.

7. **SHACL ≠ OWL reasoning; SHACL = validation.** Ontotext [[src-205]] and W3C literature consistently frame them as complementary, not competing.

8. **IOF Core is built on BFO as upper ontology.** NIST publication [[src-204]] and multiple academic sources confirm this architecture.

9. **Manufacturing ontology enables multi-hop causal path traversal.** Demonstrated by Root-KGD [[src-209]], FBS [[src-213]], FMEA [[src-214]] — pattern: Defect → Cause → Action as a traversable graph path is validated by independent research.

### 7.2 Divergence — Where Sources Differ

1. **Component count (3 to 7):**
   - W3C OWL official: 3 types (Classes, Properties, Individuals) + Axioms implicit
   - Many textbooks / introductions: 5 components (adding Hierarchy and Rules explicitly)
   - B-3 canonical model: 6 components (Class, Instance, Property, Relationship, Hierarchy, Axiom/Rule)
   - Some sources (Factor Firm [[src-211]]): list "Subclasses" as a 5th separate item from "Classes"
   - **Resolution:** The 6-component split is pedagogically sound and widely used in ontology engineering training. It separates the *logical operators* that OWL bundles (Property covers both datatype and object; Hierarchy = rdfs:subClassOf; Axiom = formal constraints). Safe to use. The count difference is presentational, not substantive.

2. **"Relationship" vs. "Property" terminology:**
   - OWL calls directed object links "Object Properties" (not "Relationships")
   - Many knowledge graph / industry sources call them "Relationships" or "Relations"
   - LPG (Neo4j) calls them "Relationships" by default
   - **Resolution:** For B-3's manufacturing audience, "Relationship" (관계) is clearer than "Object Property." The canonical 6-component model correctly uses Relationship for directed domain-concept links and Property for data-value attributes.

3. **Causal relation handling:**
   - Some sources treat "causal" as a special relation type requiring temporal logic
   - B-3 canonical model folds causal into Relationship as a directional link
   - **Resolution:** For manufacturing data preparation (not causal AI model building), treating `causes` as a standard directed ObjectProperty is correct and sufficient. Full causal AI modeling (interventional causality) is out of B-3 scope.

4. **"Ontology" vs. "Knowledge Graph" boundary:**
   - Some practitioners (especially in enterprise data) use "knowledge graph" to mean the combination of ontology + data; others use it loosely to mean any graph database
   - **Resolution:** The rigorous definition (PuppyGraph [[src-212]], Neo4j [[src-203]]) — ontology is the schema (T-Box), knowledge graph includes the instantiated data (A-Box) — is the safe framing for B-3.

5. **LPG vs. RDF as implementation choice:**
   - Academic/semantic web community: prefers RDF + OWL for formal reasoning
   - Enterprise / Neo4j community: often defaults to LPG for performance
   - Many real systems mix both (e.g., author T-Box in OWL, serve A-Box via Neo4j LPG)
   - **Resolution:** B-3 should present both models as valid implementation choices, noting that OWL/RDF is required if automated inference is needed; LPG can be used if only graph traversal queries are needed.

---

## 8. Backup Material (Detail-Level)

### 8.1 OWL 2 Sublanguages (detail — for backup slides)

| Sublanguage | Tradeoff | Typical use |
|-------------|----------|-------------|
| **OWL Lite** | Simplest; cardinality 0 or 1 only | Basic classification systems |
| **OWL DL** | Maximum expressiveness with decidable reasoning; type disjointness required | Full manufacturing ontologies (recommended) |
| **OWL Full** | Maximum freedom (classes can be individuals); reasoning not guaranteed | Rare; mainly research use |

Source: W3C OWL Guide [[src-201]].

### 8.2 SKOS Mapping Properties (detail)

For cross-system interoperability between manufacturing sites or supply chain partners:
- `skos:exactMatch` — concepts are equivalent (transitive)
- `skos:closeMatch` — concepts are close enough to use interchangeably (non-transitive)
- `skos:broadMatch`, `skos:narrowMatch` — hierarchical cross-scheme links
- `skos:relatedMatch` — associative cross-scheme links

Source: W3C SKOS Primer [[src-210]].

### 8.3 Root-KGD Triple Types (detail — manufacturing knowledge graph structure)

Three entity categories used in the Prior Industrial Knowledge Graph:
1. Physical entities: Devices, streams, materials
2. Data entities: Variables (operational status, sensor readings)
3. Relation types: State, output, contain, and domain-specific functional connections

Source: Root-KGD [[src-209]].

### 8.4 IOF Core Supporting Standards

IOF Core integrates with:
- **OWL Time** — temporal intervals and durations for process timing
- **QUDT** — Quantities, Units, Dimensions, Types ontology for measurement standardization
- **Allen Interval Algebra** — 13 possible temporal relationships between intervals

Source: IOF GitHub releases [[src-204]].

---

## Sources

| src-id | Wikilink | Notes |
|--------|----------|-------|
| src-201 | [[src-201-w3c-owl2-primer]] | W3C OWL2 Primer — primary authority on OWL components and T-Box/A-Box |
| src-202 | [[src-202-ontotext-what-are-ontologies]] | Ontotext — vendor authority, practical framing |
| src-203 | [[src-203-neo4j-taxonomy-ontology-knowledge-graph]] | Neo4j — industry authority on KG vs ontology vs taxonomy |
| src-204 | [[src-204-nist-iof-core-ontology]] | NIST + IOF GitHub — manufacturing standards authority |
| src-205 | [[src-205-ontotext-shacl]] | Ontotext SHACL — data validation complement to OWL |
| src-206 | [[src-206-w3c-rdf12-concepts]] | W3C RDF 1.2 — primary authority on triple model |
| src-207 | [[src-207-fluree-rdf-vs-lpg]] | Fluree — RDF vs LPG comparison |
| src-208 | [[src-208-rushdb-semantic-reasoning]] | RushDB — semantic reasoning mechanisms |
| src-209 | [[src-209-arxiv-root-kgd]] | arXiv Root-KGD — manufacturing multi-hop causal path |
| src-210 | [[src-210-w3c-skos-primer]] | W3C SKOS Primer — SKOS standard |
| src-211 | [[src-211-factorfirm-ontology-101]] | Factor Firm — beginner-friendly component explanation |
| src-212 | [[src-212-puppygraph-kg-vs-ontology]] | PuppyGraph — KG vs ontology boundary |
| src-213 | [[src-213-arxiv-fbs-maintenance-inference]] | arXiv FBS — FBS model for manufacturing causal inference |
| src-214 | [[src-214-arxiv-ontology-fmea-manufacturing]] | arXiv FMEA — ontology-guided FMEA fault identification |

---

## Related

- **research-B-how.en.md** (to be created) — WHAT cluster feeds into HOW section: how to model the 7 entities + 7 relations, how to choose between OWL/RDF vs. LPG, how SHACL is applied for data quality gates
- **research-C-why-when.en.md** — WHY (manufacturing pain points) and WHEN (which data/processes to ontologize first) cluster
- **B-3 온톨로지.md** — Final guide file that this research feeds
- **Adjacent topics:**
  - A-3 Glossary — single-term definitions (SKOS vocabulary territory)
  - A-2 Metadata — field-level descriptions (not concept relations)
  - A-1 Data Catalog — asset location and registration (not concept network)
  - B-2 Training labels — labeling instances (not concept schema)
  - D-series — usage and execution by AI agents (not data preparation)
