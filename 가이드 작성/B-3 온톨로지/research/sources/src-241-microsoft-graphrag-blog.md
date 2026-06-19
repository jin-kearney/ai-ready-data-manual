# src-241 — Microsoft GraphRAG: Unlocking LLM Discovery on Narrative Private Data

**URL:** https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/
**Title:** GraphRAG: Unlocking LLM discovery on narrative private data — Microsoft Research Blog
**AccessDate:** 2026-06-19
**Related section:** WHY (GraphRAG vs RAG); relational reasoning benefit

---

## Key Excerpts

**Problem baseline RAG cannot solve:**
"Baseline RAG struggles to connect the dots. This happens when answering a question requires traversing disparate pieces of information through their shared attributes."

**Second failure mode of baseline RAG:**
It performs poorly when asked to "holistically understand summarized semantic concepts over large data collections or even singular large documents."

**How GraphRAG builds the knowledge graph:**
The LLM-generated knowledge graph represents entities (people, places, organizations) as nodes and their relationships as connections. This graph structure allows the system to traverse relationships between disparate entities, answering questions that require understanding how different pieces of information relate to one another — something vector similarity alone cannot accomplish.

**Grounding and source provenance:**
"The LLM can ground itself in the graph and results in a superior answer that contains provenance through links to the original supporting text."

**Whole-dataset reasoning:**
GraphRAG enables whole-dataset reasoning by organizing content into semantic clusters with pre-summarized themes, allowing the system to answer questions like "What are the top 5 themes?" where vector search alone fails.

**Comparative evaluation:**
Research uses "an LLM grader to determine a pairwise winner between GraphRAG and baseline RAG" on qualitative metrics. Results show GraphRAG "consistently outperforms" on comprehensiveness, source provision, and viewpoint diversity, while maintaining comparable faithfulness scores.

---

*Note: Microsoft Research does not publish a single precise % uplift on this page. Claims of "50–70% comprehensiveness improvement" circulating elsewhere require confirmation against the original paper (arxiv.org/abs/2404.16130).*
