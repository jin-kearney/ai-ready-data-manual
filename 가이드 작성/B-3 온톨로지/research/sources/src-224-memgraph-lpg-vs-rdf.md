# src-224 — LPG vs. RDF | Memgraph Documentation

**URL:** https://memgraph.com/docs/data-modeling/graph-data-model/lpg-vs-rdf  
**Title:** LPG vs. RDF — Memgraph Data Modeling  
**AccessDate:** 2026-06-19  
**Related section:** §Architecture — Format Decision

---

## Relevant Excerpt

**LPG (Labeled Property Graph):**
- Nodes: entities with labels and key-value properties (`(:Person {name: "Alice", age: 30})`)
- Relationships: directed, typed edges also with key-value properties (`-[:KNOWS {since: 2020}]->`)
- Schema-optional — flexible for evolving requirements
- Query language: Cypher / openCypher / ISO GQL
- Optimized for "real-time graph traversal and analytics"
- "LPGs outperform RDF, especially for highly interconnected datasets"
- "RDF suffers from an explosion of triplets due to its global uniqueness requirement"
- More efficient multi-hop traversals without expensive triple computations

**RDF (Resource Description Framework):**
- Triples: subject-predicate-object (`:Alice :KNOWS :Bob . :Alice :name "Alice" .`)
- Schema-focused, ontology-driven — requires predefined vocabularies
- Query language: SPARQL (W3C standard)
- Better for linked data integration, semantic reasoning

**Performance insight for manufacturing (multi-hop):**
LPG's architecture avoids the triple explosion problem in RDF when traversing 6+ hop paths (e.g., defect → cause → subprocess → equipment → supplier → material). Each hop in RDF requires multiple triple joins; LPG traverses edges directly.

**When to Choose LPG:**
- Real-time applications requiring low-latency traversal
- Schema flexibility and frequent updates
- Developer accessibility (Cypher syntax is SQL-like)
- Advanced graph analytics and algorithms
- Manufacturing root-cause reasoning with deep paths

**When to Choose RDF:**
- Linked data integration across diverse, external sources
- Semantic reasoning requirements (OWL inference)
- SPARQL as mandatory query language
- Ontology-driven applications requiring formal axioms
- External standard interoperability (IOF, FIBO, etc.)
