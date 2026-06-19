# src-244 — Fault Cause Identification via Ontology-Guided FMEA Graph Learning — arXiv 2510.15428

**URL:** https://arxiv.org/abs/2510.15428
**Title:** Fault Cause Identification across Manufacturing Lines through Ontology-Guided and Process-Aware FMEA Graph Learning with LLMs
**AccessDate:** 2026-06-19
**Related section:** WHY (manufacturing causal reasoning); WHEN (complex multi-system knowledge)

---

## Key Excerpts

**Problem addressed:**
FMEA worksheets' "reuse across heterogeneous lines is hindered by natural language variability, inconsistent terminology, and process differences." Without a unifying ontology, fault knowledge trapped in local FMEA documents cannot transfer across production lines.

**How ontology + knowledge graph solves this:**
FMEA worksheets from multiple manufacturing lines are "transformed into a unified knowledge graph through ontology-guided large language model (LLM) extraction, capturing domain concepts such as actions, states, components, and parameters."

**Manufacturing ontology entities:**
Action, State, Component, Parameter — applied to automotive pressure sensor assembly lines.

**Reasoning approach:**
A Relational Graph Convolutional Network (RGCN) with process-aware scoring learns embeddings capturing both semantic relationships and sequential manufacturing process flows, enabling link prediction for candidate fault cause inference.

**Key results (automotive pressure sensor assembly):**
- Proposed approach F1@20: 0.523
- RAG baseline: 0.267
- Standard RGCN: 0.400
- The ontology-guided approach outperforms both plain RAG and graph-only approaches

**Why this matters for the WHY/WHEN cluster:**
Demonstrates that when fault knowledge is scattered across heterogeneous FMEA worksheets (documents + systems), a plain vector RAG cannot traverse "defect → cause → action" chains. Only an ontology-grounded knowledge graph enables cross-line knowledge transfer and causal inference.
