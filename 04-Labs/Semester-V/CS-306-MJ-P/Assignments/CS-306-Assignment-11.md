# Assignment 11: File System and API Fundamentals

## Problem Statement / Aim
To interact with the File System and understand fundamental API concepts in Node.js.

## Theory & Concept
The **`fs` (File System)** module in Node.js provides an API for interacting with the file system. It supports both synchronous and asynchronous methods.

An **API (Application Programming Interface)** in the context of web servers is a set of endpoints (URLs) that respond with data (usually JSON), forming the basis of RESTful services.

## Fully Solved Code
```javascript
// file-api.js
const fs = require('fs');
const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/api/data' && req.method === 'GET') {
        // Read data asynchronously from a file
        fs.readFile('data.txt', 'utf8', (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Internal Server Error' }));
            } else {
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ message: 'Success', content: data.trim() }));
            }
        });
    } else {
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Endpoint not found' }));
    }
});

// Create a dummy data.txt file for testing
fs.writeFileSync('data.txt', 'This is some sample text data from the file system.');

server.listen(3000, () => {
    console.log('API Server running on port 3000');
});
```

## Expected Output
```
API Server running on port 3000
// Request to /api/data returns:
// {"message":"Success","content":"This is some sample text data from the file system."}
```

---
[[CS-306-Viva-11|View Viva Questions]]
