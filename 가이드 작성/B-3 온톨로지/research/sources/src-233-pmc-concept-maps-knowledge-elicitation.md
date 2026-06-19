# src-233 — Concept Maps During Knowledge Elicitation in Ontology Development | PMC

**URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC1524992/  
**Title:** The use of concept maps during knowledge elicitation in ontology development processes  
**AccessDate:** 2026-06-19  
**Related section:** §HOW — Concept Elicitation from Domain Experts

---

## Relevant Excerpt

**Core Approach: Concept Maps as Bridge Tool**
Concept maps (CMs) serve as a translation tool between domain experts and knowledge engineers. CMs are "graphs consisting of nodes representing concepts, connected by arcs representing the relationships" that enable informal knowledge capture before formal encoding.

**Six-Stage Development Process with Elicitation:**
1. Define ontology purpose, scope; identify reusable existing ontologies
2. Domain analysis through terminology definition (word type, definition, context, notes)
3. Iterative CM building and validation with domain experts
4. Formalization using ontology editors (Protégé with OWL)
5. Evaluation based on fitness for purpose
6. [Maintenance]

**Knowledge Elicitation Techniques:**
- Structured sessions: teleconferences with preset specific questions
- Focus on relationships: "How does A relate to B?" and "Why need A instead of B?"
- Domain experts narrate understanding using CM structure

**Instance-to-Class Abstraction:**
Experts initially provide specific use cases; knowledge engineers identify higher-level abstractions and group instances into classes through iterative discussion.

**Key Criteria During Capture:**
- Accuracy: term definitions with contextual information
- Coherence: conceptual narratives
- Extensibility: participatory scaling and re-factoring

**Practical Guidance:**
- Combine informal CMs with semi-automatic terminology extraction
- Use narrative approaches where experts build stories alongside vocabulary organization
- Maintain separate tools (CMAP for elicitation, Protégé for formalization) until better integration emerges
- Document methodology alongside ontology results

**Application to Manufacturing:**
For PFMEA/SOP-based ontology building: ask domain experts to narrate a defect scenario (what happened, why, what was done) using concept maps, then knowledge engineers formalize into class hierarchies and relation triples.
