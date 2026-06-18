# Assignment 5: MongoDB Indexing

## Problem Statement / Aim
To create and utilize indexes in MongoDB to optimize query performance.

## Theory & Concept
Indexes support the efficient execution of queries in MongoDB. Without indexes, MongoDB must perform a *collection scan*, scanning every document in a collection to select those that match the query statement. If an appropriate index exists, MongoDB uses the index to limit the number of documents it must inspect.
Types of indexes include Single Field, Compound, Multikey, Text, and Geospatial.

## Fully Solved Code / Implementation

```javascript
// Setup data
use libraryDB
for(let i=0; i<10000; i++) {
    db.books.insertOne({ title: "Book " + i, author: "Author " + (i%100), year: 2000 + (i%20) });
}

// Check query execution stats without an index
db.books.find({ author: "Author 50" }).explain("executionStats");
// Notice "totalDocsExamined" will be 10000.

// 1. Create a Single Field Index on the 'author' field
db.books.createIndex({ author: 1 });

// Check query execution stats with the index
db.books.find({ author: "Author 50" }).explain("executionStats");
// Notice "totalDocsExamined" will be 100, which is much faster.

// 2. Create a Compound Index on 'author' and 'year'
db.books.createIndex({ author: 1, year: -1 });

// 3. Create a Unique Index on 'title'
// (Ensures no two books have the exact same title)
db.books.createIndex({ title: 1 }, { unique: true });

// 4. List all indexes in the collection
db.books.getIndexes();

// 5. Drop an index
db.books.dropIndex("author_1");
```

## Expected Output
Using `.explain("executionStats")` before and after index creation demonstrates a massive reduction in the number of documents examined (from 10,000 to 100). The `getIndexes` command will list the default `_id_` index alongside the newly created indexes.

[[CS-3010-Viva-5|View Viva Questions]]
