# src-228 — Ontology Management Operating Model | Galaxy

**URL:** https://www.getgalaxy.io/articles/ontology-management-semantic-modeling-operating-model-enterprise-context  
**Title:** Ontology Management Operating Model: Governance, Versioning & Change Control  
**AccessDate:** 2026-06-19  
**Related section:** §Operations — Governance Roles & Change Control

---

## Relevant Excerpt

**Three-Layer Governance Structure:**

1. **Domain Stewards** — Own concept proposals and business context for their area; draft definitions; identify affected consumers within their domain
2. **Semantic Architecture / Governance Board** — Manages cross-domain standards, naming conventions, identifier policy, compatibility rules; "Central governance protects cross-domain coherence" by reconciling conflicts before definitions enter the shared model
3. **Platform Teams** — Operationalize decisions through testing pipelines, publication tooling, rollout sequencing, and rollback procedures

**Versioning Strategy:**
- Stable identifiers over changing labels: concept URIs/property IDs function as long-lived contracts; labels and descriptions can evolve freely
- "Additive change before breaking change" — new classes and properties are the default evolution pattern
- Breaking changes require higher approval bars and migration paths

**Risk-Based Change Classification:**
- **Editorial** (label corrections, synonym additions) — lightweight domain steward review
- **Additive** (new concepts, properties) — standard cross-domain review
- **Breaking** (renames, removals, semantic redefinition) — governance board approval with impact analysis and migration planning

**Impact Assessment Framework:**
Review process must answer: "what datasets, APIs, dashboards, metrics, agents, and validation rules depend on the concepts being changed?" Centralizing definitions enables dependency graph analysis rather than manual guessing.

**Enterprise Best Practices:**
- Deprecate before removing; maintain explicit compatibility windows
- Publish versioned releases with changelogs, rationale, migration guidance
- Implement automated validation suites before publishing changes
- Treat semantic changes as contract changes affecting downstream analytics, APIs, and AI agents
- Document rationale and examples as part of the governance contract

**Key insight:** "Most semantic initiatives collapse — not from technical failure, but from organizational paralysis." The operating model is more important than the tooling.
