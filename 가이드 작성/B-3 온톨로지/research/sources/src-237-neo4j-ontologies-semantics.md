# src-237 — Ontologies in Neo4j: Semantics and Knowledge Graphs | Neo4j Blog

**URL:** https://neo4j.com/blog/knowledge-graph/ontologies-in-neo4j-semantics-and-knowledge-graphs/  
**Title:** Ontologies in Neo4j: Semantics and Knowledge Graphs  
**AccessDate:** 2026-06-19  
**Related section:** §Architecture — LPG Ontology Modeling

---

## Relevant Excerpt

**How Ontologies Are Modeled in Neo4j LPG:**
- Class hierarchies translate to nodes with labels connected through relationship types like `sublabel_of` or `subClassOf`
- Example using FIBO ontology: "a privately held company is classified as a subclass of stock corporation" → node connected via `:IS_SUBCLASS_OF` relationship
- Properties/attributes become node properties

**NeoSemantics Plugin:**
Enables two primary functions:
1. Interoperability: Exposing Neo4j data as RDF using standard vocabularies (Schema.org, FIBO)
2. Inferencing: Deriving new knowledge from existing data through hierarchy traversal

**Practical Implementation Pattern:**
- Import OWL/RDF ontology into Neo4j using NeoSemantics
- Map loan data to Schema.org vocabulary
- Query for "financial products" → retrieves loans even if that term never explicitly appears in the database (reasoning through `:IS_SUBCLASS_OF` hierarchy)
- Real-time mapping between graph properties and ontology concepts

**Implication for LPG Architecture:**
Neo4j LPG can represent ontology class hierarchies natively. For manufacturing: `(:DefectType)-[:IS_SUBCLASS_OF]->(:Defect)` works as a hierarchy representation. The NeoSemantics bridge allows consuming RDF/OWL standards while operating in LPG.
