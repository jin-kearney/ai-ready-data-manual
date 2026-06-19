# src-262 — OOPS! (OntOlogy Pitfall Scanner!) — Evaluation Framework

**URL:** https://www.semanticscholar.org/paper/OOPS!-(OntOlogy-Pitfall-Scanner!):-An-On-line-Tool-Poveda-Villal%C3%B3n-G%C3%B3mez-P%C3%A9rez/28f692a5b6e61ab48bece1221f4e17e05a9a8139  
**Title:** OOPS! (OntOlogy Pitfall Scanner!): An On-line Tool for Ontology Evaluation  
**Authors:** Poveda-Villalón, M. and Gómez-Pérez, A.  
**Published:** International Journal on Semantic Web and Information Systems, Vol. 10, No. 2, 2014  
**AccessDate:** 2026-06-19  
**Related sections:** KPI — Constraint validation; quality pitfall categories

## Excerpt / Key Points

OOPS! scans ontologies for pitfalls from a catalogue of **41 common pitfalls** derived from analysis of 693+ real-world ontologies, classified by:

### Pitfall Dimensions
1. **Structural** — schema structure problems (e.g., creating unconnected elements = orphan concepts, missing domain/range, missing inverse relations)
2. **Functional** — modeling problems causing incorrect inferences
3. **Usability-Profiling** — documentation and metadata problems

### Importance Levels (three-tier)
- **Critical** — cause ontology to behave incorrectly with reasoners; must fix
- **Important** — likely cause suboptimal reasoning or incomplete querying
- **Minor** — style/documentation issues; fix when possible

### Semi-Automatic Detection
33 out of 41 pitfalls can be detected semi-automatically. The remaining 8 require human judgment.

### Pitfall Examples Relevant to KPI Design
- P4: Creating unconnected ontology elements (= orphan/isolated concepts)
- P10: Missing disjointness (consistency issue)
- P19: Defining wrong inverse relationships (logic error = constraint validation failure)
- P22: Using different naming conventions (usability/consistency)
- P34: Untyped class (structural gap)

### System Evaluation
- Usage statistics show widespread adoption across the semantic web community
- Survey of user satisfaction provides external validation evidence

### Implication for KPI
A **SHACL/OOPS! pass rate** metric can operationalize constraint validation: percentage of critical + important pitfalls with zero violations in the current ontology version.

**Source type:** Peer-reviewed journal article; tool available at http://oops.linkeddata.es/
