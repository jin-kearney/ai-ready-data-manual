# src-239 — PFMEA Ontology for Manufacturing Knowledge Sharing | ResearchGate/ScienceDirect

**URL:** https://www.researchgate.net/publication/258436781_A_System_for_Distributed_Sharing_and_Reuse_of_Design_and_Manufacturing_Knowledge_in_the_PFMEA_Domain_Using_a_Description_Logics-based_Ontology  
**Title:** A System for Distributed Sharing and Reuse of Design and Manufacturing Knowledge in the PFMEA Domain Using a Description Logics-based Ontology  
**AccessDate:** 2026-06-19  
**Related section:** §HOW — Knowledge Extraction from Manufacturing Documents

---

## Relevant Excerpt

**Problem addressed:**
PFMEA activities generate valuable knowledge about manufacturing processes, but "sharing and reuse of this knowledge is a challenge because the knowledge is usually not semantically organized, and its meaning depends on the understanding of the specialists involved." High fragmentation and distribution of knowledge along the production chain.

**Ontology structure for PFMEA domain:**
- Integrates: Problem-solving method 8D, PFMEA, Case-Based Reasoning (CBR), PLM
- Core concepts: Manufacturing problems linked to production lines, PFMEA analysis results (failure modes, effects, causes, controls)
- Allows representing any type of manufacturing problem with PFMEA reuse

**Knowledge Elicitation Approach:**
- Domain experts provide relevant knowledge sources or use structured knowledge elicitation techniques
- Methodology supported "structured knowledge elicitation and reduced manual effort"
- Hybrid approaches address "labor-intensive nature of manual modeling and complexity of eliciting structured knowledge from domain experts"

**Concept Extraction from PFMEA:**
Key concepts extracted from natural language FMEA descriptions using LLMs guided by a manufacturing-specific ontology. Semi-automatic tools assist in creating surveys about FMEA and Risk Analysis.

**Practical Outcome:**
System enables cross-line fault cause identification — analogous failure patterns across different production lines connected through shared ontology concepts.

**Application to Doosan/Manufacturing context:**
PFMEA items directly map to ontology concepts: Failure Mode → Defect class, Potential Effect → Effect class, Potential Cause → Cause class, Current Controls → Control class, Recommended Actions → Action class. PFMEA severity/occurrence/detection ratings become properties.
