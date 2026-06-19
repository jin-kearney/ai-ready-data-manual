# src-225 — ISO GQL: New Standard for Graph Query Language | TigerGraph

**URL:** https://www.tigergraph.com/blog/the-rise-of-gql-a-new-iso-standard-in-graph-query-language/  
**Title:** The Rise of GQL: A New ISO Standard in Graph Query Language  
**AccessDate:** 2026-06-19  
**Related section:** §Architecture — Query Language

---

## Relevant Excerpt

**Official designation:** ISO/IEC 39075:2024 — "Graph Query Language (GQL)"  
**Publication date:** April 12, 2024  
**Significance:** "The first sibling database language emerging from the ISO standard committee for databases since the initial publication of the SQL standard in 1986."

**Relationship to Cypher/openCypher:**
- GQL incorporates two syntax flavors: one based on Cypher (the Neo4j query language and its open-source variant openCypher), and one using SQL syntax
- Both flavors share the same underlying pattern-matching foundation
- TigerGraph championed the SQL dialect for easier SQL user adoption
- openCypher mission is now to "help implementors to evolve their implementation towards GQL"

**Key features:**
- Pattern matching syntax for querying property graph databases using vertex/edge patterns
- Linear composition of multiple pattern-match statements
- Filesystem-style directory hierarchy for hosting graph schemas
- Declaration of graph patterns to filter, group, aggregate, and project results

**Practical implication for LPG architecture decisions:**
ISO GQL standardization (April 2024) directly addresses the LPG "vendor lock-in" critique. openCypher → GQL migration path means Cypher-based implementations (Neo4j, Memgraph, Neptune) will converge on a portable standard. Teams writing openCypher today are positioned to adopt GQL with minimal rework.

**Database support as of 2024:** TigerGraph (GSQL), Neo4j (Cypher, migrating toward GQL), Amazon Neptune (openCypher), Memgraph (openCypher), Microsoft Fabric (GQL preview).
