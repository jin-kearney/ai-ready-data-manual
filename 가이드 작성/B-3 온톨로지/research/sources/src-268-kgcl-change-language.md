# src-268 — Knowledge Graph Change Language (KGCL)

**URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11753292/  
**Title:** A change language for ontologies and knowledge graphs  
**AccessDate:** 2026-06-19  
**Related sections:** KPI — Operations (change request turnaround); Roadmap — governance evolution

## Excerpt / Key Points

### KGCL Overview
KGCL is a standard data model for describing changes to knowledge graphs and ontologies, enabling curators to request desired changes or describe changes that have already happened.

### Change Types Tracked
**Node Changes:**
- NodeRename, NodeObsoletion, NodeDeletion, ClassCreation
- Synonym operations (creation, removal, replacement)
- Definition operations (creation, removal, modification)

**Edge Changes:**
- EdgeCreation, EdgeDeletion, NodeMove, PredicateChange

### Quantitative Change Activity (GO Ontology as Reference)
- Change tracking across major releases (late 2018 – early 2024) shows "rates that remain high and even increase"
- Categories: terms created, merged, or obsoleted per release

### Survey Findings on Operations Pain Points
- **82%** of surveyed ontology users rated staying informed about changes as "extremely or very important"
- Only **8%** expressed satisfaction with existing change visualization methods
- Only **17%** were satisfied with change request turnaround times

> The 17% satisfaction rate with turnaround times = strong evidence that **change request SLA** is a meaningful operational KPI.

### Automation Tools
- **Ontobot**: GitHub-integrated automated agent processing curator requests → auto-generates pull requests
- Enables human-readable commands by non-technical stakeholders: `add synonym 'arm' to 'forelimb'`

### Governance Workflow
1. User submits change request (GitHub issue or BioPortal widget)
2. Automated agent generates pull request
3. Curator reviews + approves
4. Merge triggers downstream validation

### Implication for Operational KPI
**Change request turnaround time**: time from submission to approved merge. Target in PoC: define SLA tier (editorial = 3 days; structural = 2 weeks; breaking = governance board review ~4 weeks).

**Source type:** PMC peer-reviewed article (2024/2025)
