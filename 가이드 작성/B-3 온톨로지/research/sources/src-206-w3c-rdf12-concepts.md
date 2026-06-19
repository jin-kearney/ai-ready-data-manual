# src-206 — RDF 1.2 Concepts and Abstract Data Model | W3C

**URL:** https://www.w3.org/TR/rdf12-concepts/  
**Title:** RDF 1.2 Concepts and Abstract Data Model  
**AccessDate:** 2026-06-19  
**Related section:** §3 (Triples and T-Box/A-Box); §6 (Glossary — RDF, Triple)

---

## Relevant Excerpt

**What is RDF:**
"The Resource Description Framework (RDF) is a framework for representing information on the Web."

**The Triple Structure:**
RDF's fundamental building block is the triple—a three-part statement:
- **Subject**: An IRI or blank node
- **Predicate**: An IRI identifying a property
- **Object**: An IRI, blank node, literal value, or triple term

"Asserting an RDF triple says that some relationship, indicated by the predicate, holds between the resources denoted by the subject and object."

**RDF Graphs:**
"An RDF graph is a set of RDF triples." Collections of triples forming a semantic network.

**RDF Datasets:**
Organize multiple graphs, comprising one default graph and zero or more named graphs with unique identifiers.

**RDF 1.2 Innovations:**
1. **Triple Terms**: Allows RDF triples themselves to serve as objects within other triples, enabling statements about statements.
2. **Directional Language-Tagged Strings**: Incorporates text directionality for multilingual support.
3. **Version Announcement**: Mechanisms for explicitly identifying RDF version compliance.

**Key concept:**
A triple "Alice age 24" → subject=Alice, predicate=age, object=24. This is the atomic unit of all RDF-based ontologies.
