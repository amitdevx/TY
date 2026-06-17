---
title: "CS-303 Web Technology-I - Interview Preparation"
aliases: ["CS303 Interview", "Web Tech Interview Prep", "CS303 Interview Questions"]
tags:
  - subject/web-technology
  - semester/V
  - interview-prep
  - career
subject_code: CS-303-MJ-T
type: interview-prep
last_reviewed: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-303 Web Technology-I - Interview Preparation

> [!note] Navigation
> [[Overview|CS-303 Overview]] | [[Revision|CS-303 Revision]] | [[Important-Questions|CS-303 Important-Questions]]

---

> [!important] This file prepares you for technical interviews and viva exams.
> Answers are concise. For detailed explanations, see the unit notes.

---

## HTML5 & CSS Interview Questions

### Q1: What are semantic HTML elements? Why should you use them?
**Answer:**
Semantic elements communicate the meaning/purpose of their content to browsers, developers, and screen readers. Examples: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`.

**Benefits:**
- **SEO**: Search engines better understand page structure
- **Accessibility**: Screen readers navigate by semantic roles
- **Maintainability**: Code is self-documenting
- **Team collaboration**: Clear structure for all developers

---

### Q2: Explain the CSS Box Model. What is `box-sizing`?
**Answer:**
Every element is a rectangular box with four layers (inside → outside):
1. **Content** - actual text/images
2. **Padding** - space inside the border
3. **Border** - surrounds padding
4. **Margin** - space outside the border

`box-sizing: content-box` (default): `width` applies only to content.
`box-sizing: border-box` (recommended): `width` includes padding and border.

```css
*, *::before, *::after { box-sizing: border-box; } /* Best practice reset */
```

---

### Q3: What is CSS Specificity? How do you resolve conflicts?
**Answer:**
Specificity determines which CSS rule applies when multiple rules target the same element:

| Selector | Specificity Value |
|----------|------------------|
| `!important` | Overrides everything |
| Inline style | 1000 |
| ID `#id` | 100 |
| Class `.c`, attribute `[a]`, pseudo-class `:hover` | 10 |
| Element `div`, pseudo-element `::before` | 1 |

**Resolution strategies:** Use more specific selectors; use `!important` sparingly; prefer class selectors over IDs.

---

### Q4: Flexbox vs CSS Grid - when to use which?
**Answer:**
- **Flexbox**: 1-dimensional (row OR column). Use for: navbars, button groups, centering, component-level layouts.
- **Grid**: 2-dimensional (rows AND columns). Use for: full-page layouts, complex multi-area designs.

```css
/* Flexbox: center items */
.container { display: flex; justify-content: center; align-items: center; }

/* Grid: full page layout */
.page { display: grid; grid-template-areas: "header" "main" "footer"; }
```

They can also be combined: Grid for outer layout, Flexbox for inner components.

---

### Q5: What is Responsive Design? Explain mobile-first approach.
**Answer:**
Responsive Design ensures a website adapts to all screen sizes using:
1. **Fluid layouts** (%, `fr`, not fixed `px`)
2. **Flexible images** (`max-width: 100%`)
3. **Media queries** (`@media`)

**Mobile-first**: Write CSS for mobile first, then use `min-width` media queries to scale up:
```css
/* Mobile: default */
.grid { grid-template-columns: 1fr; }

/* Tablet and above */
@media (min-width: 768px) { .grid { grid-template-columns: 1fr 1fr; } }

/* Desktop */
@media (min-width: 1024px) { .grid { grid-template-columns: repeat(3, 1fr); } }
```

---

### Q6: What is the difference between `transition` and `animation`?
**Answer:**

| Feature | `transition` | `animation` |
|---------|-------------|-------------|
| Trigger | Requires state change (hover, focus, JS) | Runs automatically |
| Definition | Property change from A → B | `@keyframes` with multiple steps |
| Control | Less control | Full control (iterations, direction, delay) |
| Use case | Button hover, menu slide | Loading spinners, complex animations |

---

## JavaScript ES6+ Interview Questions

### Q7: `var` vs `let` vs `const` - which should you use and why?
**Answer:**

| | `var` | `let` | `const` |
|-|-------|-------|---------|
| Scope | Function | Block | Block |
| Hoisting | Yes (undefined) | TDZ (error) | TDZ (error) |
| Re-assign | Yes | Yes | No |
| Re-declare | Yes | No | No |

**Best practice:** Use `const` by default; `let` for mutable variables; avoid `var` in modern code.

The classic `var` bug:
```javascript
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i)); // 3, 3, 3
for (let i = 0; i < 3; i++) setTimeout(() => console.log(i)); // 0, 1, 2
```

---

### Q8: What is the difference between arrow functions and regular functions?
**Answer:**

| Feature | Regular Function | Arrow Function |
|---------|----------------|---------------|
| `this` | Dynamic (call-site) | Lexical (enclosing scope) |
| `arguments` | Yes | No (use rest `...args`) |
| Constructor | Yes (`new`) | No (throws TypeError) |
| `prototype` | Yes | No |
| Syntax | `function fn() {}` | `const fn = () => {}` |

**Key use case:** Arrow functions in callbacks preserve `this` from the enclosing scope:
```javascript
class Timer {
  start() {
    setInterval(() => this.tick(), 1000); // 'this' = Timer instance 
  }
}
```

---

### Q9: Explain Promises. What problem do they solve?
**Answer:**
Promises solve **callback hell** - deeply nested, hard-to-read async code.

A Promise represents an eventual value with 3 states:
- `pending` → `fulfilled` (resolve called) or `rejected` (reject called)

```javascript
// Callback hell:
getUser(id, (u) => getPosts(u, (p) => getComments(p[0], (c) => console.log(c))));

// Promise chain (flat!):
getUser(id).then(u => getPosts(u)).then(p => getComments(p[0])).then(console.log).catch(handleError);
```

**Promise combinators:**
- `Promise.all([p1,p2])` - all must fulfill; fails fast
- `Promise.race([p1,p2])` - first to settle
- `Promise.allSettled([p1,p2])` - wait for all; never rejects
- `Promise.any([p1,p2])` - first to fulfill

---

### Q10: What is async/await? How does it differ from Promises?
**Answer:**
`async/await` is syntactic sugar over Promises that makes async code look synchronous.

```javascript
// Promises:
fetch('/api').then(r => r.json()).then(data => console.log(data)).catch(console.error);

// async/await (same logic, cleaner):
async function getData() {
  try {
    const r = await fetch('/api');
    const data = await r.json();
    console.log(data);
  } catch(err) {
    console.error(err);
  }
}
```

`async` function always returns a Promise. `await` pauses execution until Promise resolves. Error handling with `try/catch` instead of `.catch()`.

**Parallel with async/await:**
```javascript
const [user, posts] = await Promise.all([fetchUser(), fetchPosts()]);
```

---

### Q11: What are JavaScript Modules? Named vs Default exports?
**Answer:**

```javascript
// Named exports (multiple per file)
export const PI = 3.14;
export function add(a, b) { return a + b; }

// Default export (one per file)
export default class Calculator { ... }

// Importing
import { PI, add } from './math.js';        // named
import Calculator from './math.js';          // default
import * as MathUtils from './math.js';      // namespace
import Calculator, { PI } from './math.js';  // both
```

---

## Node.js Interview Questions

### Q12: What is Node.js? Why is it used for web servers?
**Answer:**
Node.js is an open-source, cross-platform JavaScript runtime built on V8. It uses an event-driven, non-blocking I/O model that makes it ideal for **I/O-intensive applications** (web APIs, real-time apps).

**Why Node.js:**
- Single language (JS) for front-end and back-end
- Huge npm ecosystem
- Excellent for real-time: chat apps, streaming
- Not ideal for CPU-intensive tasks (machine learning, video processing)

---

### Q13: Explain the Node.js Event Loop.
**Answer:**
The Event Loop allows Node.js to handle async operations despite being single-threaded:

```
Call Stack (JS)
    ↓ delegates async work
libuv (OS thread pool / OS async APIs)
    ↓ when done, pushes callback to queue
Event Loop (picks from queue when call stack is empty)
    ↓
Callback Queue → Call Stack
```

**Phase order:**
1. Synchronous code (call stack)
2. `process.nextTick()` + Promise callbacks
3. `setTimeout` / `setInterval` callbacks (timers)
4. I/O callbacks
5. `setImmediate` callbacks

---

### Q14: What is the difference between `require` and `import`?
**Answer:**

| | `require()` (CommonJS) | `import` (ESM) |
|-|----------------------|----------------|
| Synchronous | Yes (loads immediately) | No (static, analyzed at parse) |
| Where used | Anywhere in code | Top of file only |
| Dynamic | Yes (in expressions) | Only with `import()` |
| Default in Node | Yes | Needs `.mjs` or `"type":"module"` |

---

### Q15: What are the core Node.js modules you use most?
**Answer:**
- `fs` - file system operations
- `path` - file path utilities (cross-OS)
- `http` / `https` - create web servers
- `events` - EventEmitter
- `os` - operating system info
- `url` - URL parsing
- `crypto` - hashing, encryption
- `stream` - streaming data
- `child_process` - spawn OS commands
- `cluster` - multi-core process management

---

## File Handling Interview Questions

### Q16: Sync vs Async file operations - when to use each?
**Answer:**

| | Sync | Async |
|-|------|-------|
| API | `readFileSync()` | `readFile()` / `promises.readFile()` |
| Blocking | Yes (blocks event loop) | No |
| Use when | App startup, CLI scripts | Server request handlers, any concurrent code |
| Error handling | try/catch | callback error param / try/catch with await |

**Rule:** In a web server, always use async. Sync blocks all incoming requests!

---

### Q17: How do you implement a simple JSON database in Node.js?
**Answer:**
```javascript
const fs = require('fs/promises');
const DB = 'db.json';

async function readDB() {
  const data = await fs.readFile(DB, 'utf8');
  return JSON.parse(data);
}

async function writeDB(data) {
  await fs.writeFile(DB, JSON.stringify(data, null, 2));
}

async function getAll() { return (await readDB()).records; }
async function add(item) {
  const db = await readDB();
  item.id = Date.now();
  db.records.push(item);
  await writeDB(db);
  return item;
}
```

**Limitation:** Not suitable for production (no concurrency control, no ACID). Use MongoDB/PostgreSQL for production.

---

### Q18: Explain Multer. How do you validate file uploads?
**Answer:**
Multer is Express middleware for `multipart/form-data` (file upload). It processes uploaded files and provides them in `req.file`/`req.files`.

```javascript
const upload = multer({
  storage: multer.diskStorage({
    destination: (req, f, cb) => cb(null, 'uploads/'),
    filename: (req, f, cb) => cb(null, `${Date.now()}-${f.originalname}`)
  }),
  fileFilter: (req, f, cb) => {
    const allowed = ['image/jpeg', 'image/png', 'image/gif'];
    allowed.includes(f.mimetype) ? cb(null, true) : cb(new Error('Images only!'));
  },
  limits: { fileSize: 5 * 1024 * 1024 }  // 5MB
});
```

---

## Behavioral / Conceptual Questions

### Q19: Explain the difference between CFL and JavaScript at runtime.
**Answer:** "CFL" (Context-Free Language) is a theory concept. JavaScript itself is not a CFL - it requires more powerful parsers. The question likely means: JavaScript is parsed using LR/LALR parsers (more powerful than PDA) because of complex grammar rules.

### Q20: What happens when you type a URL and press Enter?
**Answer:**
1. **DNS Resolution** - domain → IP address
2. **TCP Connection** - 3-way handshake
3. **TLS Handshake** (for HTTPS)
4. **HTTP Request** - browser sends GET request
5. **Server processes** - Node.js receives, routes, responds
6. **HTTP Response** - HTML, CSS, JS sent
7. **Browser rendering** - parse HTML → DOM → CSSOM → render tree → paint
8. **JavaScript execution** - scripts run, async fetches made

---

## Quick Answer Reference (Viva)

| Question | One-Line Answer |
|----------|----------------|
| What is semantic HTML? | Elements that convey meaning, not just presentation |
| What is `box-sizing: border-box`? | Width includes padding and border |
| What is `flex: 1`? | grow=1, shrink=1, basis=0% |
| What is the event loop? | Mechanism that handles async callbacks in Node.js |
| What does `async` function return? | Always a Promise |
| What is TDZ? | Period before `let`/`const` declaration where access throws ReferenceError |
| What is `Promise.all` vs `allSettled`? | `all` fails fast; `allSettled` waits for all regardless |
| What is `__dirname`? | Absolute path of current file's directory in Node.js |
| What is Multer? | Express middleware for file uploads (multipart/form-data) |
| `readFile` vs `readFileSync`? | Async vs sync; sync blocks the event loop |

---

*[[Overview|CS-303 Overview]] | [[Revision|CS-303 Revision]] | [[Important-Questions|CS-303 Important-Questions]]*
