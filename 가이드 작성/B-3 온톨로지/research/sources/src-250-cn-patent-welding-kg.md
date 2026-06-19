# src-250 — Metal Welding Defect Root Cause Analysis via Knowledge Graph — CN Patent 114943415A

**URL:** https://patents.google.com/patent/CN114943415A/en
**Title:** Metal welding defect root cause analysis method based on knowledge graph — CN Patent 114943415A
**AccessDate:** 2026-06-19
**Related section:** WHY + WHEN — manufacturing welding defect; concrete knowledge graph structure

---

## Key Excerpts

**Defects addressed:**
Burn-through, overburning, small nugget, desoldering, crack, askew beating, and cold welding.

**Problem before knowledge graph:**
"Analysis is more dependent on an expert experience system" with "low flexibility." Causation chains are not explicit; tracing requires isolated expert judgment rather than systematic relationship traversal.

**Knowledge graph structure (four interconnected maps):**

1. **Process Knowledge Graph:** Maps metal welding operations chronologically — equipment, parameters (reference, set, actual values), and plate information across production stages.

2. **Statistical Equipment Map:** Tracks relationships between welding guns, electrode caps, and welding points to identify error rates and equipment reliability patterns.

3. **Expert Rule Map:** Encodes mechanistic knowledge. Example: nugget heat follows E=I²RT, so insufficient current, insufficient time, or elevated resistance causes desoldering.

4. **Quality Portrait Map:** Documents factor transmission paths. Example: "plate surface wrinkles → increased contact resistance → excessive nugget heat → overburning."

**Root cause path example:**
`plate surface condition → contact resistance → heat generated → nugget quality → defect type`

This is exactly the "defect → cause → action" causal chain that vector RAG cannot traverse, because the chain crosses physical mechanisms, equipment parameters, and process history — no single document chunk contains the full path.

**Why this requires an ontology:**
Each hop in the chain uses domain concepts that must be formally defined: what "contact resistance" is, how it relates to "heat," what the threshold is for "overburning." Without formal definitions (ontology), the graph's nodes are labels with no computable meaning.
