# Assignment 6: Introduction to Graph Databases & Neo4j

## Problem Statement / Aim
To understand the fundamentals of Graph Databases and set up Neo4j for node and relationship data modeling.

## Theory & Concept
A **Graph Database** uses graph structures for semantic queries with nodes, edges (relationships), and properties to represent and store data. It is highly optimized for highly connected data and relationship traversals.
**Neo4j** is a native graph database, meaning it implements a true graph model natively down to the storage level. 
- **Nodes:** Represent entities (e.g., Person, Movie).
- **Relationships:** Connect nodes and provide context (e.g., ACTED_IN, DIRECTED). Relationships always have a direction and a type.
- **Properties:** Key-value pairs stored in nodes or relationships.

## Fully Solved Code / Implementation
*Cypher code to create basic graph structures:*

```cypher
// 1. Create Nodes
CREATE (p1:Person {name: "Keanu Reeves", born: 1964})
CREATE (p2:Person {name: "Carrie-Anne Moss", born: 1967})
CREATE (m1:Movie {title: "The Matrix", released: 1999})

// 2. Create Relationships between Nodes
MATCH (k:Person {name: "Keanu Reeves"}), (m:Movie {title: "The Matrix"})
CREATE (k)-[:ACTED_IN {roles: ["Neo"]}]->(m)

MATCH (c:Person {name: "Carrie-Anne Moss"}), (m:Movie {title: "The Matrix"})
CREATE (c)-[:ACTED_IN {roles: ["Trinity"]}]->(m)

// 3. Return the Graph
MATCH (n) RETURN n
```

## Expected Output
The Neo4j browser will visualize the graph showing two `Person` nodes connected to one `Movie` node via `ACTED_IN` relationships. The console will acknowledge the creation of 3 nodes, 2 relationships, and associated properties.

[[CS-3010-Viva-6|View Viva Questions]]
