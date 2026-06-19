# src-267 — Ontology Learning and KG Construction: Impact on RAG Performance

**URL:** https://arxiv.org/html/2511.05991v1  
**Title:** Ontology Learning and Knowledge Graph Construction: A Comparison of Approaches and Their Impact on RAG Performance  
**AccessDate:** 2026-06-19  
**Related sections:** KPI — AI-usage value; RAG accuracy improvement; ontology vs. keyword baseline

## Excerpt / Key Points

### Evaluation Setup
- **Corpus:** Single grant application document (Portuguese→English)
- **Evaluation set:** 20 manually created domain-specific questions (5 categories)
- **Evaluation method:** Manual categorical classification — Correct / Incomplete / False / "I don't know"

### Results (20-question evaluation)
| Approach | Correct | Accuracy |
|----------|---------|----------|
| Vector RAG (keyword baseline) | 12/20 | **60%** |
| Text Ontology KG (no chunks) | 3/20 | 15% |
| RDB Ontology KG (no chunks) | 4/20 | 20% |
| Text Ontology KG + chunks | 18/20 | **90%** |
| RDB Ontology KG + chunks | 18/20 | **90%** |
| GraphRAG (state-of-art) | 18/20 | 90% |

**Ontology KG + chunks vs. Vector RAG: +30 pp improvement**  
**Ontology KG without chunks: −40 to −45 pp vs. Vector RAG** (structural ontology alone not sufficient)

### Key Finding
> "Combining symbolic structure and contextual text segments proved critical for accurate reasoning."

Ontology structure alone (without linked textual evidence) performs *worse* than naive vector RAG. The value emerges from the combination: ontology provides relationship structure; text chunks provide evidence.

### Limitations / Caution for Guide
- Very small evaluation set (20 questions, 1 document) — results are directional, not statistically conclusive
- Manual evaluation prone to subjectivity
- Single domain (grant applications) — manufacturing/industrial transfer not validated

### Implication for KPI
Report RAG accuracy improvement as a **PoC measurement** not a guaranteed target. Measure: % of root-cause/analytical questions answered correctly by ontology-augmented retrieval vs. keyword-only baseline on domain-specific test set.

**Source type:** arXiv preprint 2511.05991 (2024)
