# Assignment 10: Server-Side Basics with Node.js

## Problem Statement / Aim
To create a basic server using Node.js and its core modules.

## Theory & Concept
**Node.js** is an open-source, cross-platform JavaScript runtime environment built on Chrome's V8 engine. It allows executing JavaScript code outside a web browser.

The core `http` module allows Node.js to transfer data over the Hyper Text Transfer Protocol (HTTP), making it possible to create a web server.

## Fully Solved Code
```javascript
// server.js
const http = require('http');

const server = http.createServer((req, res) => {
    // Set response header
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    
    if (req.url === '/') {
        res.end('Welcome to Node.js Server Basics!\n');
    } else if (req.url === '/about') {
        res.end('About Us Page\n');
    } else {
        res.writeHead(404);
        res.end('404 Not Found\n');
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
```

## Expected Output
```
Server running at http://localhost:3000/
(When visited in browser, displays "Welcome to Node.js Server Basics!")
```

---
[[CS-306-Viva-10|View Viva Questions]]
