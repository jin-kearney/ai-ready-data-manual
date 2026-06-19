# src-226 — IOF Ontology Releases | Industrial Ontologies Foundry GitHub

**URL:** https://github.com/iofoundry/ontology/releases/  
**Title:** IOF Ontology Releases — iofoundry/ontology  
**AccessDate:** 2026-06-19  
**Related section:** §Architecture — Standard Adoption (IOF/BFO)

---

## Relevant Excerpt

**IOF Domain Coverage:**
- Core: Foundational concepts applicable across domains
- Supply Chain: Transportation, procurement, trade identifiers
- Manufacturing: Production planning, scheduling, execution, recipes
- Maintenance: Equipment maintenance and lifecycle
- Material Procurement & Storage: Sublots, containers, trade items
- Biopharma: Pharmaceutical domain-specific applications
- Certification: Attesting processes and certificates

**BFO as Upper Ontology:**
IOF explicitly uses BFO (Basic Formal Ontology) as its foundational framework. Where BFO had gaps (e.g., "BFO does not provide a way to express when the bearer has started or stopped bearing a role"), the IOF team added specialized process classes like `gain of role` and `loss of role`.

**Domain Ontology Extension Pattern:**
Domain ontologies import and extend Core concepts. Supply Chain terms applicable beyond their domain migrate to Core and become deprecated in domain versions. Pattern: Core imports BFO → Domain ontologies import Core → Organization-specific extensions import Domain ontologies.

**Adoption Approach (pragmatic progression):**
- Start with normative modules (Core, Supply Chain) — stable and vetted
- Experiment with provisional modules (Certification, Production Planning) — non-normative, subject to change
- Use mapping files for interoperability with external ontologies (OWL Time, QUDT)

**Versioning:** YYYYMM format (e.g., 202602, 202601, 202502). Each release documents structural changes, IRI updates, normative/provisional status.

**Key defined concepts:** Temporal relations (Allen Interval Algebra), measurement processes, identifiers, designed functions, consumables with composition properties (`isMadeOfAtSomeTime` vs. structural part-whole).

**BFO adoption history:** BFO was adopted as IOF's top-level ontology in spring 2019.
