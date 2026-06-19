# src-234 — LLM-Supported Collaborative Ontology Design | Frontiers in Big Data

**URL:** https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1676477/full  
**Title:** LLM-supported collaborative ontology design for data and knowledge management platforms  
**AccessDate:** 2026-06-19  
**Related section:** §HOW — LLM/AI Assistance in Ontology Preparation

---

## Relevant Excerpt

**Six-Stage HyWay Methodology (NeOn-extended with LLM integration):**
1. Initial Information Gathering: Domain experts complete structured Excel surveys documenting workflows, parameters, inputs, outputs, units
2. Automated Ingestion: Python scripts convert Excel → CSV/JSON (ontology-agnostic representation)
3. LLM-Assisted Semantic Mapping: Python workflow performs deterministic lookups against curated dictionaries (QUDT, EMMO), then invokes GPT-3.5 to propose canonical unit forms and select appropriate ontology codes
4. Iterative Expert Validation: Enriched CSV circulates to domain specialists for review, correction, and refinement
5. Formal Ontology Generation: Finalized data transforms into formal OWL ontologies (class hierarchies, properties, logical constraints)
6. Publication: Final ontology publishes through persistent URLs

**How LLMs Assist (constrained scope):**
Rather than generating full ontologies, LLMs "propose a canonical form of the reported unit" and "select the most appropriate QUDT code from a shortlist." This two-phase approach "ensures robust handling of noisy or heterogeneous input while constraining the output to valid ontology codes."

**Human Validation Requirements:**
Expert validation is essential because LLMs "exhibited limitations when interpreting the specific modeling techniques used in domain-specialized tools." Experts identify mismatches, resolve ambiguities, refine definitions through structured CSV reviews.

**Key Finding:**
Human-in-the-loop validation proved "highly effective in accelerating ontology development without compromising semantic accuracy."

**Implication for Manufacturing:**
This approach directly applies to manufacturing ontology building: use LLMs to extract candidate concepts/relations from PFMEA/SOP text → domain experts validate and correct → knowledge engineers formalize. LLMs as first-pass accelerators, not autonomous builders.
