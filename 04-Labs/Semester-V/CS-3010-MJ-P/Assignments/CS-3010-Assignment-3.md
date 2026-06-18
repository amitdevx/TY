# Assignment 3: MongoDB CRUD Operations

## Problem Statement / Aim
To perform Create, Read, Update, and Delete (CRUD) operations on documents within a MongoDB collection.

## Theory & Concept
CRUD operations are the fundamental actions performed on databases:
- **Create:** Inserting new documents into a collection (`insertOne`, `insertMany`).
- **Read:** Querying documents from a collection (`find`, `findOne`).
- **Update:** Modifying existing documents (`updateOne`, `updateMany`, `replaceOne`).
- **Delete:** Removing documents from a collection (`deleteOne`, `deleteMany`).

## Fully Solved Code / Implementation

```javascript
// 1. Select the database
use universityDB

// 2. CREATE Operations
db.students.insertOne({
    roll_no: 101,
    name: "Alice Smith",
    department: "Computer Science",
    age: 20
});

db.students.insertMany([
    { roll_no: 102, name: "Bob Jones", department: "Electronics", age: 21 },
    { roll_no: 103, name: "Charlie Brown", department: "Computer Science", age: 22 }
]);

// 3. READ Operations
// Fetch all students
db.students.find().pretty();

// Fetch students in Computer Science department
db.students.find({ department: "Computer Science" }).pretty();

// 4. UPDATE Operations
// Update the age of Bob Jones
db.students.updateOne(
    { roll_no: 102 },
    { $set: { age: 22 } }
);

// Add a new field 'status' to all Computer Science students
db.students.updateMany(
    { department: "Computer Science" },
    { $set: { status: "Active" } }
);

// 5. DELETE Operations
// Delete the student with roll_no 103
db.students.deleteOne({ roll_no: 103 });

// Delete all students from Electronics department
db.students.deleteMany({ department: "Electronics" });
```

## Expected Output
Each command returns an acknowledgment or a cursor containing the result set. For example, `insertOne` returns `{ acknowledged: true, insertedId: ObjectId(...) }`. Read operations will output the JSON documents matching the query conditions.

[[CS-3010-Viva-3|View Viva Questions]]
