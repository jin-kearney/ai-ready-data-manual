# src-270 — Ontology Management Operating Model: Governance & Change Control

**URL:** https://www.getgalaxy.io/articles/ontology-management-semantic-modeling-operating-model-enterprise-context  
**Title:** Ontology Management Operating Model: Governance, Versioning & Change Control  
**Organization:** Galaxy (enterprise semantic modeling platform)  
**AccessDate:** 2026-06-19  
**Related sections:** KPI — Operations; Roadmap — governance maturity; change management SLAs

## Excerpt / Key Points

### Change Classification (Three Tiers)
1. **Editorial changes** — label corrections, definition wording; lightweight asynchronous review; domain steward sign-off sufficient
2. **Additive changes** — new classes/properties; ship frequently with lightweight review
3. **Breaking changes** — redefining existing concepts; governance board sign-off required; must include impact analysis and migration plan

### Operational Metrics (framework-implied, not numerically specified)
- **Classification velocity**: time from intake to change classification
- **Approval cycle time** by change type
- **Version adoption rate**: % of downstream consumers on current version
- **Impact analysis turnaround time**: how quickly dependency impact is assessed
- **Deprecation window compliance**: % of teams completing migration within stated timelines
- **Metric drift incidents**: cases where two dashboards/reports show different numbers due to ontology divergence

### Core Principle (Key quote)
> "A change to shared concept will propagate correctly to every consumer" — this is the core success metric; specific numerical targets are left to the implementing organization.

### Governance Role: Semantic Steward
Manages meaning — concept definitions, metric intent, policy boundaries, and breaking semantic changes. This role is the operational owner of KPI metrics for the ontology.

### Downstream Impact Tracking
When an ontology is centralized:
> "The change propagates once and reaches every dashboard and report."
> "Dependency graphs can be queried rather than guessed."

### Relevance to B-3 KPI
Provides framework justification for **change request turnaround SLA** as a KPI:
- Publishing explicit SLAs by change tier creates accountability
- Low satisfaction (17% from KGCL survey, src-268) validates this gap

**Source type:** Enterprise vendor blog / framework documentation (Galaxy)
