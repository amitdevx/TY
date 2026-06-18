# Assignment 4: MongoDB Aggregation Framework

## Problem Statement / Aim
To process data records and return computed results using the MongoDB Aggregation Framework.

## Theory & Concept
The aggregation framework in MongoDB is a pipeline-based framework for data aggregation, modeled on the concept of data processing pipelines. Documents enter a multi-stage pipeline that transforms the documents into aggregated results. Common stages include:
- `$match`: Filters the documents.
- `$group`: Groups documents by a specified identifier and applies accumulator expressions.
- `$sort`: Sorts the documents.
- `$project`: Reshapes each document in the stream (adds/removes fields).

## Fully Solved Code / Implementation

```javascript
// Setup data
use salesDB
db.orders.insertMany([
    { _id: 1, item: "apple", price: 10, quantity: 2, date: new Date("2023-01-01") },
    { _id: 2, item: "banana", price: 5, quantity: 10, date: new Date("2023-01-02") },
    { _id: 3, item: "apple", price: 10, quantity: 5, date: new Date("2023-01-03") },
    { _id: 4, item: "orange", price: 8, quantity: 3, date: new Date("2023-01-04") },
    { _id: 5, item: "banana", price: 5, quantity: 2, date: new Date("2023-01-05") }
]);

// Aggregation Pipeline: Calculate total sales per item, sorted by total sales descending
db.orders.aggregate([
    {
        // Stage 1: Group by item and calculate total amount
        $group: {
            _id: "$item",
            totalSales: { $sum: { $multiply: ["$price", "$quantity"] } },
            totalQuantity: { $sum: "$quantity" }
        }
    },
    {
        // Stage 2: Sort by totalSales descending
        $sort: { totalSales: -1 }
    },
    {
        // Stage 3: Project to format the output
        $project: {
            _id: 0,
            itemName: "$_id",
            totalSales: 1,
            totalQuantity: 1
        }
    }
]);
```

## Expected Output
The aggregation query will output the computed metrics:
```json
[
  { "totalSales": 70, "totalQuantity": 7, "itemName": "apple" },
  { "totalSales": 60, "totalQuantity": 12, "itemName": "banana" },
  { "totalSales": 24, "totalQuantity": 3, "itemName": "orange" }
]
```

[[CS-3010-Viva-4|View Viva Questions]]
