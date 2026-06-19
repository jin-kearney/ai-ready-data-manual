# src-263 — Knowledge Graph Quality Management: A Comprehensive Survey

**URL:** https://www.researchgate.net/publication/358524938_Knowledge_Graph_Quality_Management_a_Comprehensive_Survey  
**Title:** Knowledge Graph Quality Management: a Comprehensive Survey  
**AccessDate:** 2026-06-19  
**Related sections:** KPI — Quality dimensions taxonomy; measurement methods

## Excerpt / Key Points

### Core Quality Dimensions (widely cited consensus)
1. **Accuracy** — correctness of facts in the KG; measured via sampling + expert validation or gold-standard comparison
2. **Completeness** — coverage of knowledge for the intended domain; measured by comparing to reference inventory or scope definition
3. **Consistency** — absence of contradictions; measured by running OWL reasoner or SHACL constraints
4. **Timeliness** — currency of information; measured by last-update timestamps and staleness rate
5. **Trustworthiness** — provenance and source credibility
6. **Availability** — accessibility of the KG for query

### Extended 11-Dimension Model
When broader representational quality is included: accuracy, trustworthiness, consistency, relevancy, completeness, timeliness, ease of understanding, interoperability, accessibility, license, interlinking.

### Intrinsic / Contextual / Representational Split
- **Intrinsic**: accuracy, trustworthiness, consistency of entities
- **Contextual**: completeness, timeliness of resources  
- **Representational**: ease of understanding, interoperability

### Measurement Methods
- Automated: SPARQL queries, OWL reasoning, SHACL validation
- Semi-automated: OOPS! pitfall scanner (structural + functional)
- Manual: expert review, gold standard comparison, competency question testing

### Completeness Subtypes
- **Schema completeness**: are all relevant classes and properties defined?
- **Property completeness**: for each instance, do all required attributes have values?
- **Population completeness**: does the A-Box cover all entities in the target domain?

**Source type:** ResearchGate survey paper (peer-reviewed)
