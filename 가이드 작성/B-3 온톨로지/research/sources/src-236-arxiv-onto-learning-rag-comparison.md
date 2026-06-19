# src-236 — Ontology Learning and KG Construction: Comparison and RAG Performance | arXiv

**URL:** https://arxiv.org/html/2511.05991v1  
**Title:** Ontology Learning and Knowledge Graph Construction: A Comparison of Approaches and Their Impact on RAG Performance  
**AccessDate:** 2026-06-19  
**Related section:** §HOW — LLM/AI Assistance; §Architecture — DB Integration

---

## Relevant Excerpt

**Three Primary Automated Extraction Approaches:**
1. **RDB Ontology Learning (RIGOR framework):** Extracts ontologies directly from database schemas and DDL statements with LLM-guided refinement
2. **Text-Based Ontology Learning:** Prompt-based approaches to extract domain concepts from unstructured corpora, with iterative syntax verification
3. **Hybrid Graph Construction:** Combines ontology constraints with textual chunks embedded as node attributes

**Comparative Accuracy Results (20 domain-specific questions):**
| Configuration | Accuracy |
|--------------|---------|
| RDB + chunks | 90% (18/20) |
| Text-derived + chunks | 90% (18/20) |
| GraphRAG baseline | 90% |
| Vector RAG baseline | 60% |
| RDB without chunks | 20% |
| Text-derived without chunks | 15% |

**Critical Finding:** Chunk integration proved essential — graphs without textual context performed substantially worse. "Symbolic structure alone insufficient for factual grounding in specialized domains."

**Limitations for Domain-Specific Applications:**
- Text-based: "Ontology alignment and schema evolution" — complex merging when documents introduce conflicting entities
- Database-derived: "Relational schemas tend to remain stable over time" → lower maintenance cost; advantage for manufacturing legacy systems

**Implication for Manufacturing Ontology:**
Hybrid approach (structured data from ERP/MES/PFMEA + unstructured from SOP/C-S Reports) outperforms either approach alone. Structure the ontology from existing database schemas first (RIGOR-style), then enrich with text-extracted concepts from documents.
