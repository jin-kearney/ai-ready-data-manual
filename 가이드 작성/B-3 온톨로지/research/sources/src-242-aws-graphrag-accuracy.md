# src-242 — Improving RAG Accuracy with GraphRAG — AWS Machine Learning Blog

**URL:** https://aws.amazon.com/blogs/machine-learning/improving-retrieval-augmented-generation-accuracy-with-graphrag/
**Title:** Improving Retrieval Augmented Generation accuracy with GraphRAG — AWS Machine Learning Blog
**AccessDate:** 2026-06-19
**Related section:** WHY (quantitative accuracy comparison); when to prefer GraphRAG

---

## Key Excerpts

**Core problem:**
"Translating natural language into vectors reduces the richness of the information, potentially leading to less accurate answers." Additionally, user queries may not align semantically with useful document information, causing vector search to exclude critical data points.

**Benchmark results (Lettria hybrid GraphRAG vs vector-only baseline — confirm primary source):**
- GraphRAG: 80% correct answers vs. 50.83% with traditional RAG
- Including "acceptable" answers: GraphRAG ~90% vs. 67.5% for vector
- In technical specifications sector: GraphRAG 90.63% correct vs. 46.88% for vector RAG
- Overall headline: "up to 35% more accurate answers"

**⚠️ Attribution note:** These numbers are from Lettria's benchmark published via AWS blog. They should be cited as "Lettria benchmark via AWS blog" — not as a Stanford or Microsoft study. Confirm original Lettria publication before asserting in final guide.

**Qualitative benefits:**
- "Capturing complexity": Graphs "mirror the way humans naturally think and ask questions"
- Maintains natural data structure for precise question-answer mapping
- Better on multi-hop queries: questions requiring connections across multiple data points

**When to prefer GraphRAG:**
- Questions demand connecting multiple information pieces
- Precision and contextual accuracy are business-critical
- Datasets contain complex technical specifications or regulatory requirements
- Explainability alongside accuracy is required
