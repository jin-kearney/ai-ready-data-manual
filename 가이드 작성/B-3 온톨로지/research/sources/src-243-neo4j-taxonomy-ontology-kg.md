# src-243 — Taxonomy vs. Ontology vs. Knowledge Graph — Neo4j Blog

**URL:** https://neo4j.com/blog/knowledge-graph/taxonomy-vs-ontology-vs-knowledge-graph/
**Title:** Taxonomy vs. Ontology vs. Knowledge Graph: What's the Difference? — Neo4j Blog
**AccessDate:** 2026-06-19
**Related section:** WHEN — decision criteria; boundary between glossary/taxonomy/ontology/KG

---

## Key Excerpts

**Taxonomy:**
"A taxonomy organizes categories into a parent-child hierarchy." Useful for classification and navigation. Examples: e-commerce product catalogs.

**Ontology:**
"Provides semantic meanings and logical connections" between entities. Enables AI systems to understand not just *what* something is, but *how* different things relate to one another. Unlike taxonomies/thesauri, ontologies define the *nature* of relationships (e.g., "has part," "manufactured in").

**Knowledge Graph:**
The implementation layer. Combines "nodes, relationships, properties, and organizing principles (taxonomy and/or ontology)" into a queryable structure.

**When to use each:**
- Taxonomy: data has natural hierarchies; classification and tagging are primary goals
- Ontology: formal semantic meanings matter; logical inference needed; integrating across multiple systems with shared vocabularies
- Knowledge graph: multi-hop reasoning; AI agents must traverse relationships; combine taxonomies and ontologies as organizing structures

**Key insight on evolution:**
"There's no required order — knowledge graphs can start simple with just taxonomy and add ontological rigor later as needs evolve."

**Without ontology, knowledge graphs accumulate problems:**
"Teams that start with a graph database without an ontology discover semantic differences between the same concept in different systems, and without an ontology to enforce a shared definition, the knowledge graph silently accumulates entity duplication and relationship ambiguity that corrupts downstream AI outputs."
