# src-201 — OWL 2 Web Ontology Language Primer (Second Edition)

**URL:** https://www.w3.org/TR/owl2-primer/  
**Title:** OWL 2 Web Ontology Language Primer (Second Edition)  
**AccessDate:** 2026-06-19  
**Related section:** §2 (Components — Class, Property, Individual, Axiom); §3 (T-Box/A-Box); §5 (Reasoning)

---

## Relevant Excerpt

An ontology is "a set of precise descriptive statements about some part of the world" presented as a computational document. It combines terminological knowledge (vocabulary and relationships) with assertional knowledge (concrete objects and facts).

**Core Components:**

- **Classes**: Named categories representing sets of individuals. Classes can be organized hierarchically through subclass relationships.
- **Properties (Object Properties)**: Link individuals to other individuals (e.g., "hasWife").
- **Properties (Datatype Properties)**: Connect individuals to data values (e.g., age as an integer).
- **Individuals (Instances)**: Named objects that belong to classes. Mary as an instance of "Woman" exemplifies this.
- **Axioms**: Fundamental statements expressing knowledge. These form the foundation of an ontology and can be evaluated as true or false.

**T-Box vs. A-Box:**

- **T-Box (Terminological)**: Defines vocabulary through class hierarchies, property relationships, and logical rules. Corresponds to "schema" in database terms.
- **A-Box (Assertional)**: Contains facts about specific individuals and their properties. Corresponds to "data" in database terms.

**OWL 2 Language Characteristics:**

OWL 2 is declarative, not procedural—it describes states of affairs logically rather than prescribing computational steps. The language operates under an "open-world assumption," meaning unstated facts are unknown rather than false, unlike databases using "closed-world" semantics.

**Three OWL Sublanguages (from OWL Guide, same W3C spec family):**

- **OWL Lite**: Basic classification hierarchies, cardinality 0 or 1.
- **OWL DL**: Maximum expressiveness with computational guarantees (complete, decidable reasoning). Type separation: classes cannot simultaneously be individuals or properties.
- **OWL Full**: Maximum syntactic freedom; classes can function as both collections and individuals; reasoning support less reliable.
