# Assignment 7: Neo4j Cypher Queries

## Problem Statement / Aim
To perform advanced graph traversals and pattern matching using Neo4j's Cypher Query Language.

## Theory & Concept
Cypher is a declarative graph query language that allows for expressive and efficient querying, updating, and administering of the graph. It uses ASCII-art style syntax to represent patterns:
- `(node)`
- `-[relationship]->`
- `(node)-[relationship]->(node)`

Key clauses include `MATCH`, `WHERE`, `RETURN`, `SET`, `REMOVE`, and `DELETE`.

## Fully Solved Code / Implementation

```cypher
// Clear existing database (Caution: only for lab environments)
MATCH (n) DETACH DELETE n;

// Populate Data
CREATE (alice:User {name: 'Alice', age: 28})
CREATE (bob:User {name: 'Bob', age: 30})
CREATE (charlie:User {name: 'Charlie', age: 25})
CREATE (java:Skill {name: 'Java'})
CREATE (cypher:Skill {name: 'Cypher'})

CREATE (alice)-[:KNOWS]->(bob)
CREATE (bob)-[:KNOWS]->(charlie)
CREATE (alice)-[:KNOWS]->(charlie)

CREATE (alice)-[:HAS_SKILL]->(java)
CREATE (bob)-[:HAS_SKILL]->(cypher)
CREATE (charlie)-[:HAS_SKILL]->(java)
CREATE (charlie)-[:HAS_SKILL]->(cypher)

// 1. MATCH and RETURN: Find all Users who know Java
MATCH (u:User)-[:HAS_SKILL]->(s:Skill {name: 'Java'})
RETURN u.name, u.age;

// 2. Traversal / Friends of Friends: Find skills of people Alice knows
MATCH (a:User {name: 'Alice'})-[:KNOWS]->(friend)-[:HAS_SKILL]->(skill)
RETURN friend.name, collect(skill.name) AS skills;

// 3. Update Properties
MATCH (u:User {name: 'Bob'})
SET u.age = 31
RETURN u;

// 4. Delete a Relationship
MATCH (a:User {name: 'Alice'})-[r:KNOWS]->(c:User {name: 'Charlie'})
DELETE r;
```

## Expected Output
1. The first query returns Alice and Charlie.
2. The second query returns Bob with `['Cypher']` and Charlie with `['Java', 'Cypher']`.
3. The update query returns the Bob node with the updated age.
4. The deletion query confirms the removal of 1 relationship.

[[CS-3010-Viva-7|View Viva Questions]]
