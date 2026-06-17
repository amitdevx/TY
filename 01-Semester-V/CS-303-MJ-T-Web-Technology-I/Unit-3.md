---
title: "CS-303 Unit-3 - Node.js Fundamentals"
aliases: ["Web Tech Unit 3", "Node.js Notes", "CS303 Ch3", "Node Runtime Notes"]
tags:
  - subject/web-technology
  - semester/V
  - unit/3
  - nodejs
  - npm
  - event-loop
  - http-server
  - core-modules
subject_code: CS-303-MJ-T
unit: 3
chapter: "Chapter 3 - Node.js Fundamentals"
hours: 10
type: unit-notes
last_reviewed: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# Unit 3 - Node.js Fundamentals

> [!note] Navigation
> [[Overview|CS-303 Overview]] | ← [[Unit-2]] | **Unit 3** → [[Unit-4]]

---

## Learning Objectives

- Understand the Node.js runtime and how it differs from browser JavaScript
- Set up npm and manage packages with `package.json`
- Explain the event loop and non-blocking I/O model
- Use core modules: `fs`, `path`, `http`
- Create a basic HTTP server with routing

---

## 3.1 What is Node.js?

> [!important] Node.js
> ==Node.js== is an **open-source, cross-platform JavaScript runtime** built on Google's **V8 JavaScript engine**. It allows JavaScript to run **on the server** (outside the browser).

### Key Characteristics

| Feature | Description |
|---------|-------------|
| **Runtime** | V8 engine compiles JS to machine code |
| **Single-threaded** | One thread for JS execution |
| **Event-driven** | Responds to events asynchronously |
| **Non-blocking I/O** | Delegates I/O to OS; doesn't wait |
| **npm ecosystem** | Largest package registry in the world |
| **Use cases** | APIs, web servers, CLI tools, streaming, real-time apps |

### Browser JS vs Node.js

| Feature | Browser JS | Node.js |
|---------|-----------|---------|
| Runs in | Browser engine | V8 + libuv on OS |
| Global object | `window` | `global` |
| DOM access | Yes | No |
| File system | No (sandboxed) | Yes (`fs` module) |
| HTTP server | No | Yes (`http` module) |
| Modules | ES Modules (ESM) | CommonJS + ESM |
| `__dirname` | No | Yes |
| `require()` | No | Yes (CommonJS) |

### Node.js Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Node.js Application               │
│              (JavaScript - your code)               │
├─────────────────────────────────────────────────────┤
│                   Node.js APIs                      │
│        (fs, http, path, events, stream, ...)        │
├─────────────────────────────────────────────────────┤
│          Node.js Bindings (C++ wrappers)            │
├──────────────────────┬──────────────────────────────┤
│     V8 Engine        │        libuv                 │
│  (JS compilation)    │  (async I/O + event loop)    │
└──────────────────────┴──────────────────────────────┘
│              Operating System                       │
│      (Threads, File System, Networking, ...)        │
└─────────────────────────────────────────────────────┘
```

^nodejs-overview

---

## 3.2 Node.js Setup & First Program

### Installation Check

```bash
node --version    # e.g., v20.10.0
npm --version     # e.g., 10.2.3

# Run a file
node app.js

# Run REPL (Read-Eval-Print Loop)
node
> 2 + 2    // 4
> .exit
```

### Hello World

```javascript
// hello.js
console.log("Hello, Node.js!");
console.log("Process ID:", process.pid);
console.log("Node Version:", process.version);
console.log("Platform:", process.platform);

// Run: node hello.js
```

### Global Objects in Node.js

```javascript
// Available globally (no import needed)
console.log(__filename);  // Full path of current file
console.log(__dirname);   // Directory of current file
console.log(process.env.NODE_ENV); // Environment variable
process.exit(0);          // Exit program

// setTimeout, setInterval, clearTimeout (same as browser)
setTimeout(() => console.log("After 1 second"), 1000);

// Buffer - for binary data
const buf = Buffer.from("Hello", "utf8");
console.log(buf);         // <Buffer 48 65 6c 6c 6f>
console.log(buf.toString("hex"));  // 48656c6c6f
```

---

## 3.3 npm - Node Package Manager

> [!important] npm
> ==npm== (Node Package Manager) is the default package manager for Node.js. It provides:
> - A **CLI** to install/manage packages
> - A **registry** (npmjs.com) with millions of packages

### Essential npm Commands

```bash
# Initialize a new project
npm init              # interactive
npm init -y           # with defaults (creates package.json)

# Install packages
npm install express           # production dependency
npm install lodash            # shorthand: npm i lodash
npm install --save-dev jest   # dev dependency only
npm install -g nodemon        # global install

# Remove packages
npm uninstall express
npm uninstall --save-dev jest

# Run scripts (defined in package.json)
npm start
npm test
npm run dev
npm run build

# List installed packages
npm list              # local
npm list -g           # global

# Check for outdated
npm outdated

# Update packages
npm update

# View package info
npm info express

# Audit for security
npm audit
npm audit fix
```

### package.json - Complete Reference

```json
{
  "name": "my-node-app",
  "version": "1.0.0",
  "description": "A sample Node.js application",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest",
    "build": "webpack --mode production",
    "lint": "eslint src/"
  },
  "keywords": ["node", "web", "api"],
  "author": "Your Name <email@example.com>",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "dotenv": "^16.0.3",
    "mongoose": "^7.0.0"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "nodemon": "^3.0.0",
    "eslint": "^8.0.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

### Version Syntax

| Syntax | Meaning | Example |
|--------|---------|---------|
| `1.2.3` | Exact version | Only 1.2.3 |
| `^1.2.3` | Compatible (major stays) | 1.x.x where x ≥ 2.3 |
| `~1.2.3` | Approximately (minor stays) | 1.2.x where x ≥ 3 |
| `*` | Any version | Latest |
| `>=1.2.0` | Greater or equal | |
| `1.2.x` | x wildcard | |

```bash
# package-lock.json - exact versions (auto-generated)
# node_modules/ - installed packages (add to .gitignore!)
```

^npm-package-json

---

## 3.4 Event Loop & Non-Blocking I/O

> [!important] The Event Loop
> The ==event loop== is what allows Node.js to perform non-blocking I/O operations. Despite JavaScript being single-threaded, Node.js offloads operations to the OS/thread pool and uses callbacks to process results.

### Event Loop Phases

```
┌──────────────────────────────────────────────────────┐
│                   EVENT LOOP                         │
│                                                      │
│   ┌──────────┐                                       │
│   │  timers  │ ← setTimeout, setInterval callbacks  │
│   └────┬─────┘                                       │
│        ↓                                             │
│   ┌────────────────┐                                 │
│   │  pending I/O   │ ← OS-level callbacks            │
│   └────┬───────────┘                                 │
│        ↓                                             │
│   ┌──────────┐                                       │
│   │  idle,   │ ← Internal use                        │
│   │ prepare  │                                       │
│   └────┬─────┘                                       │
│        ↓                                             │
│   ┌──────────┐                                       │
│   │   poll   │ ← Fetch new I/O events; block here   │
│   └────┬─────┘                                       │
│        ↓                                             │
│   ┌──────────┐                                       │
│   │  check   │ ← setImmediate callbacks             │
│   └────┬─────┘                                       │
│        ↓                                             │
│   ┌──────────────┐                                   │
│   │close callbacks│ ← close events (socket.on)      │
│   └──────────────┘                                   │
│                                                      │
│   Between phases: process.nextTick(), Promises       │
└──────────────────────────────────────────────────────┘
```

### Execution Order Example

```javascript
console.log("1 - Start");            // synchronous

setTimeout(() => {
  console.log("4 - setTimeout 0");   // timers phase
}, 0);

setImmediate(() => {
  console.log("5 - setImmediate");   // check phase
});

process.nextTick(() => {
  console.log("3 - nextTick");       // before next phase
});

Promise.resolve().then(() => {
  console.log("3b - Promise");       // microtask
});

console.log("2 - End");              // synchronous

// Output order:
// 1 - Start
// 2 - End
// 3 - nextTick
// 3b - Promise
// 4 - setTimeout 0
// 5 - setImmediate
```

### Blocking vs Non-Blocking

```javascript
// BLOCKING (synchronous) - blocks the entire thread
const fs = require('fs');
const data = fs.readFileSync('file.txt', 'utf8');
console.log(data);         // waits for file
console.log("After file"); // runs after

// NON-BLOCKING (asynchronous) - registers callback, continues
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);       // runs when file is ready
});
console.log("After file"); // runs IMMEDIATELY (before file is read!)

// Why non-blocking is better for servers:
// Server can handle other requests while waiting for file/DB
```

^event-loop

---

## 3.5 CommonJS Modules

```javascript
// === math.js ===
// Export individual items
exports.add = (a, b) => a + b;
exports.PI = 3.14159;

// Or export object
module.exports = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  PI: 3.14159
};

// Export a function/class directly
module.exports = function Calculator() {
  this.add = (a, b) => a + b;
};

// === app.js ===
const math = require('./math');   // ./ for local files
console.log(math.add(2, 3));      // 5

// Destructuring import
const { add, PI } = require('./math');

// Built-in modules (no path needed)
const fs = require('fs');
const path = require('path');
const http = require('http');
const os = require('os');
const events = require('events');
```

---

## 3.6 Core Module: `path`

```javascript
const path = require('path');

// Join path segments (OS-independent)
const filePath = path.join(__dirname, 'public', 'index.html');
// On Linux: /home/user/project/public/index.html
// On Windows: C:\Users\user\project\public\index.html

// Resolve to absolute path
const absPath = path.resolve('public', 'css', 'style.css');

// Get components
const fullPath = '/home/user/project/app.js';
console.log(path.dirname(fullPath));   // /home/user/project
console.log(path.basename(fullPath));  // app.js
console.log(path.extname(fullPath));   // .js
console.log(path.basename(fullPath, '.js')); // app

// Parse
const parsed = path.parse(fullPath);
// { root: '/', dir: '/home/user/project', base: 'app.js', ext: '.js', name: 'app' }

// Format (reverse of parse)
const formatted = path.format({ dir: '/home/user', base: 'file.txt' });
// /home/user/file.txt

// Check if absolute
path.isAbsolute('/home/user');  // true
path.isAbsolute('./file');      // false

// Path separator
console.log(path.sep);     // '/' on Linux, '\' on Windows
console.log(path.delimiter); // ':' on Linux, ';' on Windows
```

^path-module

---

## 3.7 Core Module: `fs` (File System)

```javascript
const fs = require('fs');
const path = require('path');

// ========================================
// READING FILES
// ========================================

// Async (non-blocking) - preferred
fs.readFile('data.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log(data);
});

// Sync (blocking) - for scripts/startup only
try {
  const data = fs.readFileSync('data.txt', 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}

// Promise-based (Node 10+)
const fsPromises = require('fs').promises;
// or: const { promises: fs } = require('fs');
// or: const fs = require('fs/promises'); (Node 14+)

async function readFile() {
  const data = await fsPromises.readFile('data.txt', 'utf8');
  console.log(data);
}

// ========================================
// WRITING FILES
// ========================================

// Overwrites if exists, creates if not
fs.writeFile('output.txt', 'Hello, Node!', 'utf8', (err) => {
  if (err) throw err;
  console.log('File written!');
});

// Sync write
fs.writeFileSync('output.txt', 'Hello, Node!', 'utf8');

// ========================================
// APPENDING FILES
// ========================================

fs.appendFile('log.txt', 'New log entry\n', (err) => {
  if (err) throw err;
});

// ========================================
// DELETING FILES
// ========================================

fs.unlink('temp.txt', (err) => {
  if (err) {
    if (err.code === 'ENOENT') console.log('File not found');
    else throw err;
  }
  console.log('File deleted');
});

// ========================================
// FILE INFO
// ========================================

fs.stat('data.txt', (err, stats) => {
  if (err) throw err;
  console.log('Size:', stats.size, 'bytes');
  console.log('Is file:', stats.isFile());
  console.log('Is directory:', stats.isDirectory());
  console.log('Created:', stats.birthtime);
  console.log('Modified:', stats.mtime);
});

// Check if exists (sync)
const exists = fs.existsSync('data.txt');  // true or false
```

---

## 3.8 Core Module: `http` - Basic HTTP Server

> [!important] Building a Web Server
> Node.js can create an HTTP server without any third-party framework using the built-in `http` module.

```javascript
const http = require('http');
const url = require('url');

// Create server
const server = http.createServer((req, res) => {
  // req = IncomingMessage (request)
  // res = ServerResponse (response)
  
  // Parse URL
  const parsedUrl = url.parse(req.url, true);
  const pathname = parsedUrl.pathname;
  const query = parsedUrl.query;
  
  console.log(`${req.method} ${req.url}`);
  
  // Route handling
  if (pathname === '/' && req.method === 'GET') {
    res.writeHead(200, {
      'Content-Type': 'text/html',
      'X-Powered-By': 'Node.js'
    });
    res.end('<h1>Welcome Home!</h1>');
    
  } else if (pathname === '/about' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('About page');
    
  } else if (pathname === '/api/users' && req.method === 'GET') {
    const users = [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' }
    ];
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(users));
    
  } else if (pathname === '/api/users' && req.method === 'POST') {
    // Handle POST body
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      const userData = JSON.parse(body);
      res.writeHead(201, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ message: 'User created', user: userData }));
    });
    
  } else {
    res.writeHead(404, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Route not found' }));
  }
});

// Start server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});

// Handle server errors
server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`Port ${PORT} is already in use!`);
  } else {
    console.error('Server error:', err);
  }
});
```

### Serving Static HTML

```javascript
const http = require('http');
const fs = require('fs');
const path = require('path');

const mimeTypes = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.ico': 'image/x-icon',
};

const server = http.createServer((req, res) => {
  let filePath = path.join(__dirname, 'public', req.url === '/' ? 'index.html' : req.url);
  const ext = path.extname(filePath);
  const contentType = mimeTypes[ext] || 'application/octet-stream';
  
  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === 'ENOENT') {
        res.writeHead(404);
        res.end('404 Not Found');
      } else {
        res.writeHead(500);
        res.end('500 Server Error');
      }
    } else {
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content);
    }
  });
});

server.listen(3000, () => console.log('Server on port 3000'));
```

^http-server

---

## 3.9 EventEmitter

```javascript
const EventEmitter = require('events');

// Create custom event emitter
class MyEmitter extends EventEmitter {}

const emitter = new MyEmitter();

// Register listener
emitter.on('greet', (name) => {
  console.log(`Hello, ${name}!`);
});

// One-time listener
emitter.once('startup', () => {
  console.log('Server started!');
});

// Emit events
emitter.emit('greet', 'Alice');   // Hello, Alice!
emitter.emit('startup');          // Server started!
emitter.emit('startup');          // (no output - once() fired already)

// Remove listener
const handler = () => console.log('done');
emitter.on('done', handler);
emitter.removeListener('done', handler);

// List event names
console.log(emitter.eventNames());
```

---

## Interview Questions - Unit 3

> [!question] Key Interview/Exam Questions

1. **What is Node.js? How is it different from browser JavaScript?**
   - Node.js = V8 + libuv; runs on server; no DOM; has file system, http modules; uses CommonJS modules

2. **What is the event loop in Node.js?**
   - Mechanism that handles async operations: call stack → delegates I/O to OS → when complete, callback enters queue → event loop moves callback to call stack when empty

3. **What is non-blocking I/O? Why is it important for Node.js?**
   - I/O operations don't block the thread; Node can serve other requests while waiting for DB/file; makes it efficient for I/O-intensive apps

4. **What is `package.json`? What is the difference between `dependencies` and `devDependencies`?**
   - Project metadata + scripts + dependencies; `dependencies`: needed in production; `devDependencies`: only needed during development (testing, linting)

5. **What is the difference between `npm install` and `npm install --save-dev`?**
   - `npm install`: adds to `dependencies`; `--save-dev`: adds to `devDependencies`

6. **What is `process.nextTick()`? How does it differ from `setTimeout(fn, 0)`?**
   - `nextTick`: fires before any I/O, before next event loop iteration; `setTimeout(0)`: fires in timers phase, after I/O

7. **What does `require()` do? How is it different from ES6 `import`?**
   - `require()`: CommonJS, synchronous, loads at runtime; `import`: ESM, static, hoisted, tree-shakeable

8. **What is `__dirname` and `__filename` in Node.js?**
   - `__dirname`: absolute path of current file's directory; `__filename`: absolute path including filename

---

## Revision Summary

> [!summary] Unit 3 Key Takeaways
>
> **Node.js:**
> - V8 engine + libuv; server-side JS; no browser APIs
> - Single-threaded but non-blocking via event loop
>
> **npm:**
> - `npm init -y` → package.json
> - `npm install` (production) vs `--save-dev` (dev only)
> - `^` = compatible (major fixed); `~` = approximate (minor fixed)
>
> **Event Loop:**
> - Phases: timers → I/O → poll → check → close
> - nextTick + Promises: before each phase
> - Never block the event loop!
>
> **Core Modules:**
> - `path`: join, resolve, dirname, basename, extname
> - `fs`: readFile/writeFile (async) vs readFileSync/writeFileSync (sync)
> - `http`: createServer(), listen(), req.method, req.url, res.writeHead(), res.end()
>
> **Server:**
> - `http.createServer(callback).listen(port)`
> - Handle routes by checking `req.url` and `req.method`
> - Set Content-Type header appropriately

^unit3-revision

---

*← [[Unit-2]] | [[Overview|CS-303 Overview]] | Next: [[Unit-4]] →*
