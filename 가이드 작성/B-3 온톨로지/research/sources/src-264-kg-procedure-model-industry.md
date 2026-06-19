# src-264 — Procedure Model for Building Knowledge Graphs for Industry Applications

**URL:** https://arxiv.org/html/2409.13425v1  
**Title:** Procedure Model for Building Knowledge Graphs for Industry Applications (KG-PM)  
**AccessDate:** 2026-06-19  
**Related sections:** Roadmap — Build stages; KPI — Competency question answerability; SHACL validation

## Excerpt / Key Points

### Seven-Step KG-PM (adapted from CRISP-DM)
1. **Business Understanding** — define CQs, use cases, business goals
2. **Data Understanding** — evaluate data sources against quality criteria
3. **Data Preparation** — clean, integrate, normalize
4. **Modeling** — design domain ontology (RDFS/OWL); consider reusing Dublin Core, SKOS, schema.org
5. **Graph Setup** — RDF mapping, triple store loading
6. **Evaluation** — multi-level validation (syntax → logical → structural → CQ answerability)
7. **Deployment** — CI/CD automation, governance, versioning

### KPI-Relevant Evaluation (Step 6)
Three validation levels at Step 6:
1. **Syntax validation**: parse Turtle/N-Quads output files
2. **Logical consistency**: OWL reasoner with OWL-LD rule set
3. **Structural validation**: SHACL or ShEx shape constraints

**Competency Question Answerability Rate**: CQs are translated to SPARQL sub-queries; results documented in an evaluation table; % of CQs successfully answered = primary quality gate.

### Data Quality Dimensions at Step 2
Five source quality criteria: unambiguous interpretability, uniform representation, credibility, faultlessness, completeness.

### KG Quality Dimensions at Step 6 (Wang et al.)
Accuracy, completeness, consistency, timeliness, trustworthiness, availability.

### Lean/Agile Integration
- Product backlog = CQ collection
- Sprint goal = selected CQs to model and validate
- Feedback triggers iteration back to Step 1 with updated CQs

### Maturity Progression (implicit)
- **POC phase**: manual testing, single-machine deployment, limited CQ set
- **Production phase**: automated pipelines, distributed triple store, versioning governance, extended CQ coverage

**Source type:** arXiv preprint 2409.13425 — industry-focused academic paper
