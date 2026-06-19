# src-261 — Structural Quality Metrics to Evaluate Knowledge Graphs

**URL:** https://arxiv.org/abs/2211.10011  
**Title:** Structural Quality Metrics to Evaluate Knowledge Graphs  
**AccessDate:** 2026-06-19  
**Related sections:** KPI — Structural quality; OntoQA schema metrics; relationship richness

## Excerpt / Key Points

Six structural quality metrics determine whether a knowledge graph can express knowledge abundantly through a detailed ontology:

1. **Class Instantiation (CI)**: ratio of classes that have at least one instance; measures actual usage vs. defined schema
2. **Subclass Property Instantiation (SPI)**: ratio of subclasses that use inherited properties; measures inheritance utilization
3. **Relationship Richness (RR)** (from OntoQA): `RR = |P| / (|SC| + |P|)` where P = non-is-a relations, SC = subclasses; measures diversity beyond taxonomy
4. **Attribute Richness (AR)**: `AR = |AT| / |C|` where AT = total attributes, C = number of classes; measures knowledge density per concept
5. **Inheritance Richness (IR)**: `IR = |S| / |C|` where S = subclasses; measures how deeply knowledge is classified
6. **Graph Density**: edge count relative to node count; standard graph metric adapted for KG evaluation

### Key finding
> "High-quality KGs exhibit extensive class/property use, well-segmented but not overly complex hierarchies, and active utilization in instance data."

**Orphan/isolated concepts**: nodes with no edges (neither subject nor object in any triple) are a direct quality failure — each orphan represents a defined concept not integrated into the knowledge structure.

### From the OntoQA framework (Tartir & Arpinar)
- Schema metrics: richness, inheritance depth/breadth
- KB (instance) metrics: distribution of instances across classes, average attributes per instance
- Class metrics: connectivity of individual classes

**Source type:** Academic paper (arxiv preprint → published in Semantic Web Journal)
