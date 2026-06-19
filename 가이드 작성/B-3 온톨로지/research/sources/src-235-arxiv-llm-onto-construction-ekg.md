# src-235 — LLM-Driven Ontology Construction for Enterprise Knowledge Graphs | arXiv

**URL:** https://arxiv.org/pdf/2602.01276  
**Title:** LLM-Driven Ontology Construction for Enterprise Knowledge Graphs  
**AccessDate:** 2026-06-19  
**Related section:** §HOW — LLM/AI Assistance in Ontology Preparation

---

## Relevant Excerpt

**Methodology Stages:**
1. Entity and Concept Extraction: LLMs identify domain concepts from enterprise data/text → recognize relevant classes
2. Relationship Discovery: LLMs extract semantic relationships between identified entities
3. Property Specification: Models help define attributes, data types, constraints
4. Human Validation: Domain experts review extracted classes, proposed relationships, property assignments, overall coherence
5. Quality Metrics: Benchmark comparison, domain expert assessment, consistency checks, coverage analysis

**Human-in-the-Loop Framework:**
Emphasizes human validation at each stage — automated extraction aligns with enterprise requirements and domain knowledge only after expert oversight.

**Quality Evaluation:**
- Comparison against benchmark datasets
- Domain expert assessment
- Consistency checks for logical soundness
- Coverage analysis of domain concepts

**Key Innovation:**
Integration of LLMs with structured human validation creates a scalable approach that reduces manual effort while maintaining quality assurance.

**Limitation for manufacturing:**
The paper references enterprise knowledge graphs generally; detailed manufacturing case studies are not extensively elaborated. The methodology is domain-agnostic and must be calibrated to manufacturing-specific terminology (PFMEA failure modes, SOP process steps, C/S report defect types).
