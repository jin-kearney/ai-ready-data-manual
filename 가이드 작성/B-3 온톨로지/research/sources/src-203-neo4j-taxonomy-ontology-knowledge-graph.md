# src-203 — Taxonomy vs. Ontology vs. Knowledge Graph | Neo4j Blog

**URL:** https://neo4j.com/blog/knowledge-graph/taxonomy-vs-ontology-vs-knowledge-graph/  
**Title:** Taxonomy vs. Ontology vs. Knowledge Graph: What's the Difference?  
**AccessDate:** 2026-06-19  
**Related section:** §1 (Definition + Boundary); §6 (Glossary)

---

## Relevant Excerpt

**Taxonomy:**
A taxonomy arranges entities into hierarchical parent-child categories. "A taxonomy organizes categories as a hierarchy." Provides classification and labeling through broader-to-narrower relationships, like navigating from "Foodstuffs" to "Fruit" to "Apple" in an online grocery store.

**Ontology:**
An ontology defines semantic meanings and logical connections between domain entities. It specifies how things relate using formal rules—for instance, "Person placed Order" and "Order contains Product." "An ontology defines the semantic meanings and logical connections between entities."

**Knowledge Graph:**
A knowledge graph is the implementation layer combining instance data with organizing principles. Comprises nodes (entities), relationships (connections), properties (descriptive attributes), and taxonomies or ontologies as structural guides.

**Key Differences Table:**

| Aspect | Taxonomy | Ontology | Knowledge Graph |
|--------|----------|----------|-----------------|
| Function | Hierarchical classification | Semantic meaning and logic | Integrated data system |
| Structure | Parent-child tree | Logical rules and connections | Nodes, relationships, properties |
| Use Case | Tagging and navigation | Interoperability and inference | Multi-hop reasoning for AI |

**Critical Distinction:**
Taxonomies handle hierarchy alone; ontologies add meaning and rules. A knowledge graph synthesizes both as "blueprints that provide it with structure and meaning," enabling AI agents to traverse connected context and perform intelligent reasoning.

**Key Relationship (from PuppyGraph, confirmed):**
"A knowledge graph is the instantiation of an ontology, and an ontology is the knowledge model."
