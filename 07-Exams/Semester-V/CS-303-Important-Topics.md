---
title: "CS-303 Web Technology-I - Important Topics"
subject: CS-303
semester: V
tags:
  - important-topics
  - web-tech
  - html5
  - css3
  - javascript
  - nodejs
  - semester-v
  - exam
aliases:
  - Web Tech Important
  - CS303 Must-Know
created: 2026-06-16
type: important-topics
---

#  CS-303 Web Technology-I - Important Topics

> [!important] Exam Focus
> This subject is highly practical. Prioritize writing code. Theory questions are short - definitions and comparisons.

---

##  Top 10 Most Important Topics

| # | Topic | Description | Probability |
|---|-------|-------------|-------------|
| 1 | **CSS Flexbox & Grid** | Layout models - justify-content, align-items, grid-template-columns |  |
| 2 | **HTML5 Forms & Validation** | Input types, required, pattern, fieldset/legend |  |
| 3 | **ES6 Promises & async/await** | Asynchronous JS - .then(), .catch(), try/catch |  |
| 4 | **Node.js File Handling (fs)** | readFile, writeFile, appendFile, unlink |  |
| 5 | **Node.js HTTP Server** | http.createServer(), routing, status codes |  |
| 6 | **ES6 Features** | Arrow functions, template literals, destructuring, spread/rest |  |
| 7 | **Responsive Design / Media Queries** | @media, breakpoints, mobile-first |  |
| 8 | **ES6 Classes & Inheritance** | class, constructor, extends, super, override |  |
| 9 | **HTML5 Multimedia** | `<video>`, `<audio>`, attributes (controls, autoplay, loop) |  |
| 10 | **localStorage / sessionStorage** | setItem, getItem, removeItem, clear |  |

---

##  "Definitely Going to Come" Section

> [!warning] Exam Guaranteed Topics
> These have near 100% probability based on syllabus pattern:

### Must-Prepare Questions:
1. **Write a responsive webpage using CSS Flexbox OR Grid**
   - Create 3-column layout that collapses on mobile
   
2. **HTML5 Registration Form with all input types + validation**
   - text, email, password, date, radio, checkbox, submit
   - required, placeholder, pattern attributes

3. **Node.js program to read/write files using `fs` module**
   - Both synchronous and asynchronous versions

4. **ES6 Promises - create a Promise and handle with .then()/.catch() AND async/await**

5. **Create a simple HTTP server in Node.js that handles multiple routes**

6. **Explain ES6 features with code examples** (any 3-4 from the list)

---

##  Must-Know Definitions

| Term | Definition |
|------|-----------|
| **Semantic HTML** | HTML tags that describe their meaning (e.g., `<nav>`, `<article>`, `<main>`) |
| **CSS Specificity** | Rules determining which CSS applies: Inline > ID > Class > Element |
| **Flexbox** | CSS 1D layout - arranges items in row or column with alignment control |
| **CSS Grid** | CSS 2D layout - arranges items in rows AND columns simultaneously |
| **Promise** | JS object representing eventual completion or failure of async operation |
| **Arrow Function** | Concise function syntax; does NOT have its own `this` binding |
| **Closure** | Function that retains access to its outer scope even after outer function executes |
| **Event Loop** | Node.js mechanism for handling async callbacks without blocking |
| **Middleware** | Function(s) in Express that execute between request and response |
| **npm** | Node Package Manager - tool for installing/managing JS packages |

---

##  Quick Code Patterns to Remember

### CSS Flexbox Template
```css
.container {
  display: flex;
  justify-content: space-between; /* Main axis */
  align-items: center;            /* Cross axis */
  flex-wrap: wrap;
}
```

### CSS Grid Template
```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
@media (max-width: 768px) {
  .grid { grid-template-columns: 1fr; }
}
```

### Promise Pattern
```javascript
const promise = new Promise((resolve, reject) => {
  // async work
  if (success) resolve(data);
  else reject(error);
});

// Consume
promise.then(data => ...).catch(err => ...);

// async/await
async function run() {
  try { const data = await promise; }
  catch (e) { console.error(e); }
}
```

### Node.js fs Module
```javascript
const fs = require('fs');
fs.readFile('file.txt', 'utf8', (err, data) => { /* async read */ });
fs.writeFile('file.txt', 'content', err => { /* async write */ });
fs.appendFile('file.txt', 'more', err => { /* append */ });
fs.unlink('file.txt', err => { /* delete */ });
```

### Express Middleware Pattern
```javascript
const express = require('express');
const app = express();

app.use(express.json()); // built-in middleware

app.get('/', (req, res) => res.send('Hello World'));

app.listen(3000);
```

---

##  Common Mistakes to Avoid

> [!warning] Mistakes Students Commonly Make
> - **Flexbox vs Grid confusion:** Flexbox = 1D (row OR column), Grid = 2D (rows AND columns)
> - **`var` vs `let` vs `const`:** `var` is function-scoped, `let`/`const` are block-scoped. `const` doesn't mean immutable for objects!
> - **Promise `.then()` chaining:** Each `.then()` should return a value for proper chaining
> - **Arrow functions and `this`:** Arrow functions inherit `this` from enclosing scope - don't use them as object methods
> - **`fs.readFile` is async** - don't try to use the data outside the callback
> - **HTML form `method="POST"`** - forgetting method/action attributes
> - **CSS `position: absolute` is relative to nearest positioned ancestor**, not just the parent

---

##  Key HTML5 Attributes Cheatsheet

```html
<!-- Input types -->
<input type="email|tel|number|date|color|range|url|search">

<!-- Form attributes -->
<input required pattern="[A-Z]{3}" min="0" max="100" placeholder="hint">

<!-- Media attributes -->
<video controls autoplay muted loop poster="img.jpg" preload="auto">
<audio controls loop>
```

---

##  CSS Properties Quick Reference

| Property | Use |
|----------|-----|
| `flex-direction` | row \| column \| row-reverse \| column-reverse |
| `justify-content` | flex-start \| center \| flex-end \| space-between \| space-around |
| `align-items` | stretch \| center \| flex-start \| flex-end \| baseline |
| `grid-template-columns` | repeat(3, 1fr) \| 200px auto 200px |
| `grid-gap` / `gap` | Spacing between grid items |
| `@media` | `@media (max-width: 768px) { }` |
| `position` | static \| relative \| absolute \| fixed \| sticky |
| `z-index` | Stacking order (higher = on top) |

---

*Tags: CS-303 Web Technology-I | Semester V | [[07-Exams]]*
