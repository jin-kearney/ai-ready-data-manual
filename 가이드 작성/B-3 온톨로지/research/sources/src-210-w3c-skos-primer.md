# src-210 — SKOS Simple Knowledge Organization System Primer | W3C

**URL:** https://www.w3.org/TR/skos-primer/  
**Title:** SKOS Simple Knowledge Organization System Primer  
**AccessDate:** 2026-06-19  
**Related section:** §4 (Standards Landscape — SKOS); §6 (Glossary)

---

## Relevant Excerpt

**Definition and Purpose:**
SKOS is an RDF vocabulary for representing "semi-formal knowledge organization systems like thesauri, taxonomies, and classification schemes." It "provides a model for expressing the basic structure and content of concept schemes such as thesauri, classification schemes, subject heading lists, taxonomies, folksonomies, and other similar types of controlled vocabulary."

**Core Components:**

**Concepts:** The fundamental unit in SKOS—"ideas, meanings, or (categories of) objects and events" that exist independently from their labels. Each concept has a unique URI.

**Labels (3 types):**
- `skos:prefLabel`: The primary term for a concept
- `skos:altLabel`: Synonyms, near-synonyms, acronyms
- `skos:hiddenLabel`: Terms accessible to search but not displayed to users
- Labels support multilingual representation through language tags (e.g., "@en", "@ko")

**Semantic Relationships (3 types):**
- **Hierarchical**: `skos:broader` and `skos:narrower` — generic-to-specific
- **Associative**: `skos:related` — non-hierarchical connections
- **Transitive**: `skos:broaderTransitive` and `skos:narrowerTransitive` — ancestor-descendant inference
- Note: `skos:broader` and `skos:narrower` are NOT inherently transitive (allows "dirty hierarchies")

**Concept Schemes:** `skos:ConceptScheme` aggregates related concepts.

**SKOS vs. OWL — Critical Distinction:**
"SKOS concepts are OWL individuals, not classes." SKOS avoids using `owl:sameAs` for mappings; instead uses `skos:exactMatch` (equivalence without merging concept properties).

**Cross-scheme Mapping:**
- `skos:exactMatch`: Equivalent meaning (transitive)
- `skos:closeMatch`: Sufficient similarity for interchangeable use (non-transitive)
- `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`: Hierarchical and associative mappings

**Use Cases:**
Publishing controlled vocabularies in machine-readable formats; indexing documents; integrating heterogeneous knowledge organization systems; faceted navigation and search interfaces.

**Key takeaway for B-3:**
SKOS = vocabulary/taxonomy layer. OWL = ontology layer with reasoning. They operate at different expressiveness levels. SKOS is closer to A-3 Glossary territory; OWL is the full B-3 ontology territory.
