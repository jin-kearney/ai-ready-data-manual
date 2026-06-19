# src-232 — A Guide to Ontology Governance in metaphactory | metaphacts

**URL:** https://blog.metaphacts.com/a-guide-to-ontology-governance-in-metaphactory  
**Title:** A Guide to Ontology Governance in metaphactory  
**AccessDate:** 2026-06-19  
**Related section:** §Operations — Governance Roles & Lifecycle

---

## Relevant Excerpt

**Governance Roles:**
- **Owners:** Permission to delete, publish, or initiate a new version of an ontology
- **Authors:** Permission to edit an ontology or vocabulary that is in development
- Role assignment is per-user and per-asset, enabling accountability and notifications

**Ontology Lifecycle (5 states):**
1. In Development — active editing phase
2. In Review — peer review; ontology enters locked state
3. Ready to Be Published — optional intermediate after review completion
4. Published — finalized and saved to Git
5. Archived — superseded by newer version but retained for reference

**Versioning:**
- Published ontologies cannot be directly modified; changes require creating a new version
- All versions saved to Git with hashed versioning for integrity and recovery
- Preserves original published version when a new version is created

**Review and Approval Process:**
- Contributors initiate review requests and assign specific reviewers
- Reviewers provide feedback via in-platform comments
- Once stakeholders approve, status changes to publication-ready or published

**Governance Tooling:**
- Ontology provenance tracking (creation/modification dates, responsible users)
- Editorial workflow status labels
- Role-based notifications
- Git integration for version storage
- In-platform communication features
