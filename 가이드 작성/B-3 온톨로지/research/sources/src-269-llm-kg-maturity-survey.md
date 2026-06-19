# src-269 — LLM-Empowered Knowledge Graph Construction: A Survey

**URL:** https://arxiv.org/pdf/2510.20345  
**Title:** LLM-empowered knowledge graph construction: A survey  
**AccessDate:** 2026-06-19  
**Related sections:** Roadmap — LLM-assisted stage; automated ontology construction maturity

## Excerpt / Key Points

### Three-Stage Progression in KG Construction

**Stage 1: Manual / Rule-Based**
- "Handcrafted linguistic rules and pattern matching"
- "Strong human supervision and limited scalability"
- Ontology engineering = specialist-only task

**Stage 2: Semi-Automated / LLM-Assisted**
- "Semi-automated ontology construction pipelines encompassing the entire lifecycle—from CQ formulation and validation to ontology instantiation"
- "Human experts intervening only at critical checkpoints"
- LLMs autonomously identify classes, object properties, data properties

**Stage 3: Intelligent / Autonomous**
- LLMs as "adaptive reasoning agents that integrate contextual, structural, and retrieved signals"
- Continuous ontology maintenance; not yet achieved at scale

### Two Complementary Paradigms at Stage 2–3
- **Schema-Based**: LLMs instantiate or expand predefined ontologies; extraction guided by explicit schemas
- **Schema-Free**: LLMs autonomously infer entities/relations; new schema components generated

### Current Capability Ceiling (as of 2024–2025)
LLM outputs described as achieving "quality comparable to that of junior human modelers" — not expert-level. Limitations include:
- Difficulty determining optimal model scope
- Confusion between individuals and classes
- Hallucination of hierarchy directionality

### Maturity Metric Proxies (qualitative, from survey)
- "High semantic consistency" — measured by ontology reasoner satisfiability checks
- "Improved alignment precision" — measured by F1-score on extraction benchmarks
- "Factual coverage, scalability, maintainability" — directional progress indicators

### Implication for Roadmap
The survey validates a 3-stage roadmap: Manual → Semi-automated (LLM-assisted) → Autonomous. Current production state is transitioning from Stage 1 to Stage 2. Stage 3 is emerging research, not yet enterprise-deployable.

**Source type:** arXiv survey paper 2510.20345 (2024)
