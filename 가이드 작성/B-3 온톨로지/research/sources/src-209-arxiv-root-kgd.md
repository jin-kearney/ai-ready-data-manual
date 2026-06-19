# src-209 — Root-KGD: Knowledge Graph-Based Root Cause Diagnosis

**URL:** https://arxiv.org/html/2406.13664v1  
**Title:** Root-KGD: A Novel Framework for Root Cause Diagnosis Based on Knowledge Graph and Industrial Data  
**AccessDate:** 2026-06-19  
**Related section:** §5b (Multi-hop causal path reasoning in manufacturing)

---

## Relevant Excerpt

**Abstract:**
Root-KGD combines domain knowledge and industrial data for fault root cause diagnosis. The framework uses knowledge graphs to represent process relationships and data-driven modeling to extract fault features, enabling accurate and interpretable online fault diagnosis for industrial systems.

**Core Methodology — Three Steps:**
1. **Fault Feature Extraction**: Reconstruction-Based Contribution (RBC) algorithm generates variable contribution scores reflecting system impact.
2. **Prior Industrial Knowledge Graph (PIKG) Construction**: Encodes domain knowledge via structured triples connecting devices, streams, and variables.
3. **Root Cause Reasoning**: Applies the Ripple Fault Propagation Algorithm (RFPA) to identify root cause entities.

**Triple-Based Knowledge Representation:**
PIKG uses "head entity, relation, tail entity" triples. The framework distinguishes:
- Physical entities: Devices, streams, materials
- Data entities: Variables representing operational status
- Relations: State, output, contain, and other functional connections

**Multi-Hop Reasoning via RFPA:**
The algorithm simulates fault propagation from candidate source nodes outward:
- Initial fault quantity propagates through knowledge graph pathways
- Attenuation factors account for relation types and propagation frequency
- Termination occurs when propagation quantity drops below thresholds
- "The root cause node rank is used to analyze the possibility of nodes as root causes" — cosine similarity between simulated fault patterns and observed variable contributions

**Industrial Validation:**
Tennessee Eastman Process (TEP) and Multiphase Flow Facility (MFF) — correctly identifies fault sources while providing interpretable device/stream-level localization.

**Key Insight for B-3:**
This is a concrete example of how a manufacturing ontology with Defect→Cause→Action path structure enables 3+ hop causal reasoning to diagnose root causes. The triple model (head, relation, tail) directly maps to the B-3 canonical triple (subject–predicate–object).
