# src-213 — FBS Model-based Maintenance Record Accumulation for Failure-Cause Inference

**URL:** https://arxiv.org/pdf/2510.11003  
**Title:** FBS Model-based Maintenance Record Accumulation for Failure-Cause Inference in Manufacturing Systems  
**AccessDate:** 2026-06-19  
**Related section:** §5b (Manufacturing causal inference via ontology)

---

## Relevant Excerpt

**Abstract:**
This research proposes a method for systematically accumulating maintenance records using the Function-Behavior-Structure (FBS) model to enable causal inference in manufacturing systems. Addresses the challenge of extracting actionable failure-cause relationships from disparate maintenance documentation through structured knowledge representation.

**FBS Model Application:**
Decomposes systems into:
- **Functional intent** (what the component should do)
- **Behavioral characteristics** (how it operates)
- **Structural components** (physical instantiation)

This tripartite representation captures not just what failed, but how the failure relates to design intent and physical instantiation.

**Methodology for Causal Inference:**
Ontology-based knowledge graph maps maintenance events to causal pathways:
- Traces failures backward through behavioral dependencies to functional deficiencies
- Links structural degradation to behavioral anomalies
- Identifies recurring failure patterns across similar system architectures
- Enables "explicit reasoning over maintenance relationships"

**Key Innovation:**
Rather than treating maintenance records as isolated documents, the FBS-ontology integration transforms them into interconnected causal networks, enabling predictive maintenance and improved design iteration.

**Relevance to B-3:**
Demonstrates that manufacturing ontology (with structured class/property/relationship design) enables automated root cause traversal — a concrete "how ontology enables AI to follow causal paths" example aligned with B-3's defect→cause→action model.
