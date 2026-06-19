# src-266 — KGroot: Enhancing Root Cause Analysis via Knowledge Graphs

**URL:** https://arxiv.org/html/2402.13264v1  
**Title:** KGroot: Enhancing Root Cause Analysis through Knowledge Graphs and Graph Convolutional Neural Networks  
**AccessDate:** 2026-06-19  
**Related sections:** KPI — AI-usage value; retrieval improvement; root cause accuracy

## Excerpt / Key Points

### Methodology
KGroot constructs **Fault Propagation Graphs (FPGs)** from real-time events and compares them against pre-built **Fault Event Knowledge Graphs (FEKGs)** using Relational Graph Convolutional Networks (R-GCN) to identify the most similar historical fault scenario.

### Performance Metrics (Dataset B — production environment)
| Metric | KGroot | KGroot w/o KG | Next-best baseline (DéjàVu) |
|--------|--------|----------------|------------------------------|
| A@3 (top-3 accuracy) | **93.5%** | 90.15% | 90.62% |
| A@1 | 75.18% | — | — |
| Precision | 76.31% | — | — |
| F1 Score | 74.39% | 72.15% | — |

**KG contribution (ablation):** +3.35 pp on A@3, +2.24 pp on F1 vs. same model without KG component.

**Mean Average Rank improvement:** KGroot outperforms non-KG baselines by 39–96%.

### Speed
578 milliseconds for root cause localization — production-viable for real-time fault diagnosis.

### Key Limitation / Caution for Guide
The 93.5% A@3 figure reflects a **specific microservice fault dataset** (Dataset B). Industrial machinery fault datasets (Dataset A) may show different results. Do NOT present these numbers as universal benchmarks.

### Implication for KPI
Ontology-grounded KG for root cause analysis can be evaluated by comparing A@3 accuracy of ontology-guided retrieval vs. keyword/non-KG baseline — but organizations should run their own PoC measurement rather than assuming the 93.5% figure.

**Source type:** arXiv preprint 2402.13264 → published in Expert Systems with Applications (2024)
