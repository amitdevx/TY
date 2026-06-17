---
title: "CS-303 Web Technology-I - Revision Notes"
aliases: ["CS303 Revision", "Web Tech Quick Revision", "CS303 Cheat Sheet"]
tags:
  - subject/web-technology
  - semester/V
  - revision
  - cheat-sheet
subject_code: CS-303-MJ-T
type: revision
last_reviewed: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-303 Web Technology-I - Revision Notes

> [!note] Navigation
> [[Overview|CS-303 Overview]] | [[Important-Questions|CS-303 Important-Questions]] | [[Interview-Prep|CS-303 Interview-Prep]]

---

> [!tip] How to Use
> This file is your **last-minute revision guide**. Use it the night before your exam. For detailed notes, refer to the individual unit files.

---

## Chapter 1 - HTML5 & CSS3

### HTML5 Semantic Elements (Must Memorize)
```
<header>  - page/section header
<nav>     - navigation links
<main>    - primary content (1 per page)
<section> - thematic group (needs heading)
<article> - self-contained (blog post, news)
<aside>   - sidebar / related content
<footer>  - footer content
<figure>  - media with caption
<figcaption> - caption for figure
<time>    - machine-readable date/time
```

### CSS Box Model
```
Total width (content-box) = width + padding-left + padding-right + border-left + border-right
Total width (border-box)  = width (padding + border are INSIDE)

ALWAYS USE: box-sizing: border-box in your CSS reset
```

### Selector Specificity (Quick Ref)
```
!important  → Overrides all
Inline style → 1000
#id          → 100
.class, [attr], :pseudo-class → 10
element, ::pseudo-element     → 1
* → 0
```

### Flexbox Quick Reference
```css
/* Container */
display: flex;
flex-direction: row | column;
justify-content: flex-start | center | space-between | space-around | space-evenly;
align-items: stretch | center | flex-start | flex-end;
flex-wrap: wrap | nowrap;
gap: 10px;

/* Item */
flex: 1;         /* grow=1, shrink=1, basis=0% */
flex-grow: 1;
align-self: center;
order: 2;
```

### CSS Grid Quick Reference
```css
/* Container */
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: auto;
grid-template-areas: "h h h" "s c a" "f f f";
gap: 20px;

/* Item */
grid-area: header;
grid-column: 1 / 3;    /* from col line 1 to 3 */
grid-row: span 2;
```

### Media Queries - Common Breakpoints
```css
@media (min-width: 768px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (prefers-color-scheme: dark) { /* Dark mode */ }
@media print { /* Print */ }
```

### Animations
```css
@keyframes name { from {} to {} }
/* or */
@keyframes name { 0% {} 50% {} 100% {} }

animation: name duration timing iteration direction fill-mode;
/* e.g.: animation: bounce 1s ease infinite alternate; */

transition: property duration timing delay;
/* e.g.: transition: all 0.3s ease; */
```

---

## Chapter 2 - JavaScript ES6+

### Variable Scoping
```javascript
var  → function-scoped, hoisted (undefined), can re-declare
let  → block-scoped, TDZ, no re-declare, can re-assign
const → block-scoped, TDZ, no re-declare, no re-assign (binding)
```

### ES6 Feature Cheat Sheet
```javascript
// Arrow function
const fn = (a, b) => a + b;
const fn2 = x => x * 2;           // one param: no parens
const fn3 = () => ({ key: val }); // object: wrap in ()

// Destructuring
const { name, age = 0 } = user;
const [first, , third, ...rest] = arr;
const { a: { b } } = nested;  // nested

// Spread / Rest
const merged = [...arr1, ...arr2];
const clone = { ...obj, extra: true };
function sum(...args) { return args.reduce((a,b)=>a+b,0); }

// Template literals
`Hello ${name}, ${2+2} items`;

// Class
class Dog extends Animal {
  constructor(name) { super(name, 'Woof'); }
  speak() { return super.speak() + '!'; }
}

// Modules
export const x = 1;          // named export
export default function() {} // default export
import { x } from './file';
import name from './file';
import * as all from './file';
```

### Async JavaScript - The Three Styles
```javascript
// Callbacks
asyncOp(data, (err, result) => { ... });

// Promises
asyncOp(data)
  .then(result => ...)
  .catch(err => ...)
  .finally(() => ...);

// async/await
async function main() {
  try {
    const result = await asyncOp(data);
  } catch(err) { ... }
}

// Parallel:
const [a, b] = await Promise.all([op1(), op2()]);
```

---

## Chapter 3 - Node.js Fundamentals

### Key Facts
```
Node.js = V8 engine + libuv (async I/O library)
Single-threaded JavaScript execution
Event-driven, non-blocking I/O
npm = Node Package Manager
CommonJS: require() / module.exports
ESM: import / export
```

### npm Commands (Must Know)
```bash
npm init -y              # create package.json
npm install express      # install + add to dependencies
npm install -D jest      # add to devDependencies
npm install -g nodemon   # global install
npm start / npm test     # run scripts
npm run scriptname       # run custom script
```

### Event Loop Order (Priority High → Low)
```
1. Synchronous code (call stack)
2. process.nextTick() callbacks
3. Promise microtasks (.then/.catch)
4. setTimeout/setInterval callbacks (timers phase)
5. setImmediate callbacks (check phase)
6. I/O callbacks
```

### Core Modules
```javascript
// path
path.join(__dirname, 'folder', 'file.txt')
path.basename('/home/user/file.js')  // 'file.js'
path.extname('file.js')              // '.js'
path.dirname('/home/user/file.js')   // '/home/user'

// http server
const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'application/json'});
  res.end(JSON.stringify({ok: true}));
});
server.listen(3000);
```

---

## Chapter 4 - File Handling

### File Operations - Quick Reference
```javascript
// READ
fs.readFile(path, 'utf8', (err, data) => {});    // async
const data = fs.readFileSync(path, 'utf8');        // sync

// WRITE (overwrite)
fs.writeFile(path, content, 'utf8', (err) => {}); // async
fs.writeFileSync(path, content, 'utf8');           // sync

// APPEND
fs.appendFile(path, content, (err) => {});         // async
fs.appendFileSync(path, content);                  // sync

// DELETE
fs.unlink(path, (err) => {});    // async
fs.unlinkSync(path);             // sync

// DIRECTORY
fs.mkdir(path, {recursive: true}, cb);
fs.readdir(path, {withFileTypes: true}, cb);
fs.rm(path, {recursive: true, force: true}, cb);

// CHECK
fs.existsSync(path); // true/false (sync only)

// PROMISE style (modern)
const fs = require('fs/promises');
await fs.readFile(path, 'utf8');
await fs.writeFile(path, content);
```

### JSON File Operations
```javascript
// Read JSON
const raw = fs.readFileSync('data.json', 'utf8');
const obj = JSON.parse(raw);
// OR (shortcut, only for static files):
const obj = require('./data.json');

// Write JSON
fs.writeFileSync('data.json', JSON.stringify(obj, null, 2));

// Pretty print (null=no replacer, 2=indent)
JSON.stringify(obj, null, 2)
```

### Multer (File Upload) - Key Points
```javascript
const upload = multer({
  storage: multer.diskStorage({
    destination: (req, file, cb) => cb(null, 'uploads/'),
    filename: (req, file, cb) => cb(null, Date.now() + path.extname(file.originalname))
  }),
  limits: { fileSize: 5 * 1024 * 1024 }, // 5MB
  fileFilter: (req, file, cb) => {
    file.mimetype.startsWith('image/') ? cb(null, true) : cb(new Error('Images only!'));
  }
});

app.post('/upload', upload.single('photo'), (req, res) => {
  res.json({ url: '/uploads/' + req.file.filename });
});
```

---

## Exam Tips

> [!tip] Last-Minute Exam Tips
>
> 1. **Always add viewport meta tag** for any HTML you write: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
> 2. **For async code questions**: write all three styles (callback, Promise, async/await) if asked to compare
> 3. **For Node.js server**: always include error handling and 404 route
> 4. **For file operations**: mention sync vs async tradeoffs even if not asked explicitly
> 5. **For Flexbox**: remember `justify-content` = main axis, `align-items` = cross axis
> 6. **For CSS Grid**: `fr` unit means "fraction of remaining space"
> 7. **Promise states**: pending → fulfilled OR rejected (one-way, no going back)
> 8. **Arrow functions**: cannot use as constructors, no own `arguments`, no own `this`

---

## Key Comparisons Table

| Topic | Option A | Option B |
|-------|----------|----------|
| Layout | Flexbox (1D) | Grid (2D) |
| Animation trigger | `transition` (state change) | `animation` (@keyframes, auto) |
| Variable scope | `var` (function) | `let`/`const` (block) |
| Async style | Promises | async/await (syntactic sugar) |
| File ops | Sync (blocks) | Async (non-blocking) |
| Module system | CommonJS (require) | ES Modules (import/export) |
| File storage | diskStorage | memoryStorage (multer) |

---

*[[Overview|CS-303 Overview]] | [[Important-Questions|CS-303 Important-Questions]] | [[Interview-Prep|CS-303 Interview-Prep]]*
