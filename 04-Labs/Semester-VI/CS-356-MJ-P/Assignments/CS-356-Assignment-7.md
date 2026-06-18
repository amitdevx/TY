# CS-356 Assignment 7: CRUD API Development using Express.js, Postman and Swagger

## Problem Statement / Aim
To build a CRUD API using Express.js, test it via Postman, and document it using Swagger.

## Theory & Concept
Express.js is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. It facilitates the rapid development of RESTful APIs. Postman is a tool for API testing. Swagger (OpenAPI) provides a standardized way to describe RESTful APIs, allowing for interactive documentation.

## Fully Solved Code
```javascript
// Install dependencies: npm install express body-parser swagger-ui-express

const express = require('express');
const bodyParser = require('body-parser');
const swaggerUi = require('swagger-ui-express');
const app = express();

app.use(bodyParser.json());

// In-memory data store
let items = [{ id: 1, name: "Item One" }];

// Simple Swagger Document definition
const swaggerDocument = {
  openapi: '3.0.0',
  info: { title: 'Simple CRUD API', version: '1.0.0' },
  paths: {
    '/items': {
      get: {
        summary: 'Get all items',
        responses: { '200': { description: 'Successful response' } }
      }
    }
  }
};

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// Create
app.post('/items', (req, res) => {
    const newItem = { id: items.length + 1, name: req.body.name };
    items.push(newItem);
    res.status(201).json(newItem);
});

// Read
app.get('/items', (req, res) => {
    res.json(items);
});

// Update
app.put('/items/:id', (req, res) => {
    const item = items.find(i => i.id === parseInt(req.params.id));
    if (!item) return res.status(404).send('Item not found');
    item.name = req.body.name;
    res.json(item);
});

// Delete
app.delete('/items/:id', (req, res) => {
    items = items.filter(i => i.id !== parseInt(req.params.id));
    res.status(204).send();
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

## Expected Output
```
Server running on port 3000

# GET /items
[{"id": 1, "name": "Item One"}]

# Swagger UI available at: http://localhost:3000/api-docs
```

---
[[CS-356-Viva-7|View Viva Questions]]
