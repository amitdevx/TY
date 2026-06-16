---
title: "CS-303 Unit-2 - Advanced JavaScript ES6+"
aliases: ["Web Tech Unit 2", "ES6 JavaScript Notes", "CS303 Ch2", "Modern JS Notes"]
tags:
  - subject/web-technology
  - semester/V
  - unit/2
  - javascript
  - es6
  - async-js
  - promises
  - arrow-functions
subject_code: CS-303-MJ-T
unit: 2
chapter: "Chapter 2 - Advanced JavaScript ES6+"
type: unit-notes
last_reviewed: 2026-06-16
---

#  Unit 2 - Advanced JavaScript ES6+

> [!note] Navigation
> [[Overview|CS-303 Overview]] | ← [[Unit-1]] | **Unit 2** → [[Unit-3]] → [[Unit-4]]

---

##  Learning Objectives

- Understand `var`, `let`, `const` and their scope differences
- Write arrow functions and understand lexical `this`
- Use destructuring for arrays and objects
- Apply spread and rest operators
- Use template literals for string formatting
- Create classes with inheritance using ES6 class syntax
- Work with modules (import/export)
- Master asynchronous JavaScript: callbacks, Promises, async/await
- Solve practical logic-building problems using ES6+ features

---

## 2.1 Variables - `var`, `let`, `const`

> [!important] The Variable Trinity
> ES6 introduced `let` and `const` to fix the problems with `var`.

### Comparison Table

| Feature | `var` | `let` | `const` |
|---------|-------|-------|---------|
| Scope | Function-scoped | Block-scoped | Block-scoped |
| Hoisting | Yes (undefined) | Yes (TDZ - error) | Yes (TDZ - error) |
| Re-declaration | Yes | No | No |
| Re-assignment | Yes | Yes | No |
| Global object property | Yes | No | No |
| When to use | Legacy code | Loop counters, mutable | Constants, references |

### Scope Examples

```javascript
// var: function-scoped (leaks out of blocks)
function varExample() {
  if (true) {
    var x = 10;      // accessible outside the if block!
    let y = 20;      // block-scoped
    const z = 30;    // block-scoped
  }
  console.log(x);    // 10  (var leaks)
  console.log(y);    // ReferenceError 
  console.log(z);    // ReferenceError 
}

// var hoisting
console.log(a);      // undefined (hoisted but not initialized)
var a = 5;

// let Temporal Dead Zone (TDZ)
console.log(b);      // ReferenceError! (TDZ)
let b = 5;

// const: immutable binding, not immutable value
const PI = 3.14;
PI = 3.15;           // TypeError: Assignment to constant variable

const obj = { name: "Alice" };
obj.name = "Bob";    //  Works! (object itself not frozen)
obj = {};            // TypeError! (binding cannot change)
```

### The Classic Loop Bug

```javascript
// Bug with var in loops
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3 (all closures share same 'i')

// Fixed with let
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 0, 1, 2  (each iteration has its own 'i')
```

^var-let-const

---

## 2.2 Arrow Functions

> [!important] Arrow Functions
> ==Arrow functions== provide a shorter syntax for writing functions and **lexically bind `this`** (no own `this` context).

### Syntax Variations

```javascript
// Traditional function
function add(a, b) {
  return a + b;
}

// Arrow function - full form
const add = (a, b) => {
  return a + b;
};

// Arrow function - implicit return (single expression, no braces)
const add = (a, b) => a + b;

// Single parameter - no parentheses needed
const square = x => x * x;

// No parameters - parentheses required
const greet = () => "Hello!";

// Returning an object literal - wrap in parentheses
const makeObj = (name, age) => ({ name, age });

// With function body
const process = (arr) => {
  const filtered = arr.filter(x => x > 0);
  return filtered.map(x => x * 2);
};
```

### `this` Binding - The Key Difference

```javascript
// Problem with traditional functions
const timer = {
  count: 0,
  start: function() {
    // 'this' in setInterval is 'window'/'undefined', not 'timer'
    setInterval(function() {
      this.count++;           // BUG: 'this' is window
      console.log(this.count); // NaN
    }, 1000);
  }
};

// Fix 1: var self = this
start: function() {
  var self = this;
  setInterval(function() {
    self.count++;
    console.log(self.count); // 
  }, 1000);
}

// Fix 2: Arrow function (lexical 'this')
const timer = {
  count: 0,
  start: function() {
    setInterval(() => {
      this.count++;           // 'this' = timer 
      console.log(this.count);
    }, 1000);
  }
};
```

> [!warning] Arrow Functions Cannot Be Used As
> - **Constructors**: `new ArrowFunc()` → TypeError
> - **Object methods** (when you need `this` to refer to the object)
> - **Generator functions**
> - They have no `arguments` object

^arrow-functions

---

## 2.3 Destructuring

> [!important] Destructuring
> ==Destructuring== allows extracting values from arrays or properties from objects into distinct variables.

### Array Destructuring

```javascript
const colors = ['red', 'green', 'blue', 'yellow'];

// Basic
const [first, second] = colors;
console.log(first, second);    // 'red' 'green'

// Skip elements
const [, , third] = colors;
console.log(third);            // 'blue'

// Rest element
const [head, ...tail] = colors;
console.log(head);  // 'red'
console.log(tail);  // ['green', 'blue', 'yellow']

// Default values
const [a = 'pink', b = 'orange'] = ['red'];
console.log(a, b);  // 'red' 'orange'

// Swap variables
let x = 1, y = 2;
[x, y] = [y, x];
console.log(x, y);  // 2 1

// From function return
function getCoords() { return [10, 20]; }
const [lat, lng] = getCoords();
```

### Object Destructuring

```javascript
const user = {
  name: 'Alice',
  age: 25,
  email: 'alice@example.com',
  address: {
    city: 'Mumbai',
    zip: '400001'
  }
};

// Basic
const { name, age } = user;
console.log(name, age);   // 'Alice' 25

// Rename variables
const { name: userName, age: userAge } = user;
console.log(userName);    // 'Alice'

// Default values
const { role = 'user' } = user;
console.log(role);        // 'user' (default, since role not in object)

// Nested destructuring
const { address: { city, zip } } = user;
console.log(city, zip);  // 'Mumbai' '400001'

// Rest in objects
const { name: n, ...rest } = user;
console.log(rest);  // { age: 25, email: '...', address: {...} }

// In function parameters
function greet({ name, age = 0 }) {
  console.log(`Hi ${name}, you are ${age}`);
}
greet(user);  // Hi Alice, you are 25
```

^destructuring

---

## 2.4 Spread and Rest Operators

```javascript
// === SPREAD OPERATOR (...) ===
// "Spread out" an iterable into individual elements

// 1. Combining arrays
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];    // [1,2,3,4,5,6]
const withExtra = [0, ...arr1, 3.5, ...arr2, 7]; // flexible

// 2. Copying arrays (shallow)
const original = [1, 2, 3];
const copy = [...original];   // independent copy

// 3. Spreading into function arguments
function sum(a, b, c) { return a + b + c; }
const nums = [1, 2, 3];
console.log(sum(...nums));    // 6

// 4. Spreading objects
const defaults = { color: 'blue', size: 'md' };
const custom = { ...defaults, color: 'red', weight: 'bold' };
// { color: 'red', size: 'md', weight: 'bold' }

// 5. String spread
const chars = [..."hello"];  // ['h','e','l','l','o']


// === REST OPERATOR (...) ===
// "Collect" remaining arguments into an array

// 1. Function rest parameters
function sumAll(first, ...rest) {
  return first + rest.reduce((acc, n) => acc + n, 0);
}
console.log(sumAll(1, 2, 3, 4));  // 10

// 2. Rest in destructuring (see §2.3)
const [a, b, ...remaining] = [1, 2, 3, 4, 5];
console.log(remaining);  // [3, 4, 5]

// 3. Replacing arguments object
function oldStyle() {
  console.log(arguments);       // array-like, not real array
}
function newStyle(...args) {
  console.log(args);            // real array, has .map() etc.
}
```

^spread-rest

---

## 2.5 Template Literals

```javascript
const name = "Alice";
const age = 25;

// Old way
const msg1 = "Hello, " + name + "! You are " + age + " years old.";

// Template literal - backticks, ${expression}
const msg2 = `Hello, ${name}! You are ${age} years old.`;

// Multi-line strings
const html = `
  <div class="card">
    <h2>${name}</h2>
    <p>Age: ${age}</p>
  </div>
`;

// Expressions inside ${}
const a = 10, b = 20;
console.log(`Sum: ${a + b}`);            // Sum: 30
console.log(`Is adult: ${age >= 18}`);   // Is adult: true
console.log(`Square: ${Math.pow(a, 2)}`);// Square: 100

// Nested template literals
const items = ['apple', 'banana'];
const list = `Items: ${items.map(i => `<li>${i}</li>`).join('')}`;

// Tagged templates (advanced)
function highlight(strings, ...values) {
  return strings.reduce((result, str, i) =>
    `${result}${str}${values[i] ? `<mark>${values[i]}</mark>` : ''}`, '');
}
const output = highlight`Hello ${name}, you are ${age} years old!`;
// Hello <mark>Alice</mark>, you are <mark>25</mark> years old!
```

^template-literals

---

## 2.6 ES6 Classes

> [!important] Classes in ES6
> ==Classes== in ES6 are **syntactic sugar** over JavaScript's prototype-based inheritance. They provide a cleaner syntax for creating objects.

```javascript
// === CLASS DEFINITION ===
class Animal {
  // Constructor
  constructor(name, sound) {
    this.name = name;      // instance property
    this.sound = sound;
    Animal.count++;        // static property update
  }
  
  // Static property
  static count = 0;
  
  // Instance method
  speak() {
    return `${this.name} says ${this.sound}`;
  }
  
  // Getter
  get info() {
    return `${this.name} (${this.sound})`;
  }
  
  // Setter
  set nickname(val) {
    this._nickname = val.trim();
  }
  
  get nickname() {
    return this._nickname || this.name;
  }
  
  // Static method
  static create(name, sound) {
    return new Animal(name, sound);
  }
  
  // toString
  toString() {
    return this.speak();
  }
}

const cat = new Animal('Cat', 'Meow');
console.log(cat.speak());   // Cat says Meow
console.log(cat.info);      // Cat (Meow)
cat.nickname = '  Kitty  ';
console.log(cat.nickname);  // Kitty
console.log(Animal.count);  // 1

// === INHERITANCE ===
class Dog extends Animal {
  constructor(name, breed) {
    super(name, 'Woof');    // must call super() first
    this.breed = breed;
  }
  
  // Override parent method
  speak() {
    return `${super.speak()}! (${this.breed})`;
  }
  
  fetch(item) {
    return `${this.name} fetches the ${item}!`;
  }
}

const dog = new Dog('Rex', 'Labrador');
console.log(dog.speak());   // Rex says Woof! (Labrador)
console.log(dog.fetch('ball'));  // Rex fetches the ball!
console.log(dog instanceof Animal);  // true
console.log(dog instanceof Dog);     // true

// Private fields (ES2022)
class BankAccount {
  #balance = 0;             // private field
  
  constructor(initialBalance) {
    this.#balance = initialBalance;
  }
  
  deposit(amount) { this.#balance += amount; }
  
  get balance() { return this.#balance; }
}

const acc = new BankAccount(1000);
acc.deposit(500);
console.log(acc.balance);  // 1500
// console.log(acc.#balance); // SyntaxError - private!
```

^es6-classes

---

## 2.7 Modules (import / export)

```javascript
// === math.js (module file) ===

// Named exports
export const PI = 3.14159;

export function add(a, b) { return a + b; }

export function multiply(a, b) { return a * b; }

export class Calculator {
  add(a, b) { return a + b; }
  sub(a, b) { return a - b; }
}

// Default export (one per module)
export default function subtract(a, b) { return a - b; }


// === app.js (importing) ===

// Import named exports
import { PI, add, multiply } from './math.js';

// Import with alias
import { add as sum, multiply as product } from './math.js';

// Import default export
import subtract from './math.js';        // any name works

// Import everything as namespace
import * as Math from './math.js';
console.log(Math.PI);
console.log(Math.add(2, 3));

// Import both default and named
import subtract, { PI, add } from './math.js';

// Dynamic import (lazy loading)
async function loadModule() {
  const module = await import('./math.js');
  console.log(module.add(1, 2));
}

// Re-export
export { add, multiply } from './math.js';
export { default as subtract } from './math.js';
```

---

## 2.8 Asynchronous JavaScript

> [!important] Why Asynchronous?
> JavaScript is ==single-threaded== - it can do only one thing at a time. Async allows long operations (network, file I/O) to run without **blocking** the main thread.

### The Async Evolution

```
Callbacks → Promises → async/await
  (ES5)       (ES6)     (ES2017)
```

### 2.8.1 Callbacks

```javascript
// Simple callback
function fetchData(callback) {
  setTimeout(() => {
    const data = { id: 1, name: "Alice" };
    callback(null, data);      // convention: (error, data)
  }, 1000);
}

fetchData((err, data) => {
  if (err) {
    console.error("Error:", err);
    return;
  }
  console.log("Data:", data);
});

// === CALLBACK HELL (Pyramid of Doom) ===
getUser(1, (err, user) => {
  if (err) return handleError(err);
  getPosts(user.id, (err, posts) => {
    if (err) return handleError(err);
    getComments(posts[0].id, (err, comments) => {
      if (err) return handleError(err);
      getAuthor(comments[0].authorId, (err, author) => {
        if (err) return handleError(err);
        console.log(author);  // deeply nested!
      });
    });
  });
});
```

> [!warning] Callback Hell Problems
> - Deeply nested, hard to read
> - Error handling must be repeated at every level
> - Difficult to reason about execution order
> - No easy way to run things in parallel

### 2.8.2 Promises

> [!important] Promise
> A ==Promise== is an object representing the eventual **completion or failure** of an asynchronous operation.
> 
> **States:** `pending` → `fulfilled` or `rejected`

```javascript
// Creating a Promise
const myPromise = new Promise((resolve, reject) => {
  // async operation
  setTimeout(() => {
    const success = true;
    if (success) {
      resolve({ id: 1, name: "Alice" }); // fulfilled
    } else {
      reject(new Error("Something went wrong")); // rejected
    }
  }, 1000);
});

// Consuming a Promise
myPromise
  .then(data => {
    console.log("Success:", data);
    return data.name;          // chaining
  })
  .then(name => {
    console.log("Name:", name);
  })
  .catch(err => {
    console.error("Error:", err.message);
  })
  .finally(() => {
    console.log("Always runs (cleanup)");
  });

// Solving Callback Hell with Promises
getUser(1)
  .then(user => getPosts(user.id))
  .then(posts => getComments(posts[0].id))
  .then(comments => getAuthor(comments[0].authorId))
  .then(author => console.log(author))
  .catch(err => handleError(err));   // ONE catch for all errors!

// === Promise Combinators ===

// All must succeed
Promise.all([fetchUser(), fetchPosts(), fetchSettings()])
  .then(([user, posts, settings]) => {
    // all 3 resolved
  })
  .catch(err => {
    // if ANY rejects, catch fires
  });

// Race: first to settle wins
Promise.race([fetch('/api/fast'), fetch('/api/slow')])
  .then(result => console.log("First:", result));

// All settle (ES2020)
Promise.allSettled([p1, p2, p3])
  .then(results => {
    results.forEach(r => {
      if (r.status === 'fulfilled') console.log(r.value);
      else console.error(r.reason);
    });
  });

// First to SUCCEED
Promise.any([p1, p2, p3])
  .then(firstSuccess => console.log(firstSuccess));
```

^promises

### 2.8.3 Async / Await

> [!important] Async/Await
> ==async/await== is syntactic sugar over Promises - makes async code look and behave like synchronous code.

```javascript
// async function always returns a Promise
async function fetchUserData(userId) {
  // await pauses execution until Promise resolves
  const user = await getUser(userId);
  const posts = await getPosts(user.id);
  const comments = await getComments(posts[0].id);
  const author = await getAuthor(comments[0].authorId);
  
  return author;  // becomes resolved Promise value
}

// Error handling with try/catch
async function loadData() {
  try {
    const user = await fetchUser(1);
    const posts = await fetchPosts(user.id);
    console.log(posts);
  } catch (err) {
    console.error("Failed:", err.message);
  } finally {
    console.log("Loading complete");
  }
}

// Parallel execution with async/await
async function loadAll() {
  // SEQUENTIAL (slow): waits for each
  const user = await fetchUser(1);
  const posts = await fetchPosts(user.id);
  
  // PARALLEL (fast): start all at once
  const [user2, settings] = await Promise.all([
    fetchUser(2),
    fetchSettings()
  ]);
}

// Async IIFE (Immediately Invoked Function Expression)
(async () => {
  const data = await fetchData();
  console.log(data);
})();

// Async arrow function
const getData = async () => {
  const result = await fetch('/api/data');
  return result.json();
};

// for...of with await (sequential async iteration)
async function processItems(items) {
  for (const item of items) {
    await processItem(item);  // sequential
  }
}
```

^async-await

### Async Comparison

```javascript
// Same logic: 3 ways

// Callbacks
getUser(1, (err, user) => {
  if (err) return console.error(err);
  getScore(user.id, (err, score) => {
    if (err) return console.error(err);
    console.log(`${user.name}: ${score}`);
  });
});

// Promises
getUser(1)
  .then(user => getScore(user.id).then(score => ({ user, score })))
  .then(({ user, score }) => console.log(`${user.name}: ${score}`))
  .catch(console.error);

// Async/Await (cleanest!)
async function showScore() {
  try {
    const user = await getUser(1);
    const score = await getScore(user.id);
    console.log(`${user.name}: ${score}`);
  } catch(err) {
    console.error(err);
  }
}
```

---

## 2.9 Logic-Building Programs (ES6+)

```javascript
// 1. Fibonacci with generator
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}
const fib = fibonacci();
console.log([...Array(8)].map(() => fib.next().value));
// [0, 1, 1, 2, 3, 5, 8, 13]

// 2. Array operations with ES6+
const students = [
  { name: 'Alice', grade: 85 },
  { name: 'Bob',   grade: 72 },
  { name: 'Carol', grade: 91 },
  { name: 'Dave',  grade: 68 },
];

// Filter passing (>=75), sort by grade desc, get names
const topStudents = students
  .filter(({ grade }) => grade >= 75)
  .sort((a, b) => b.grade - a.grade)
  .map(({ name, grade }) => `${name}: ${grade}`);
console.log(topStudents); // ['Carol: 91', 'Alice: 85']

// 3. Grouping with reduce
const grouped = students.reduce((acc, student) => {
  const key = student.grade >= 75 ? 'pass' : 'fail';
  acc[key] = acc[key] || [];
  acc[key].push(student.name);
  return acc;
}, {});

// 4. Async fetch with retry
async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.json();
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 1000 * (i + 1))); // exponential backoff
    }
  }
}

// 5. Debounce function
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
const debouncedSearch = debounce(searchAPI, 300);

// 6. Curry function
const curry = fn => {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn(...args);
    }
    return (...moreArgs) => curried(...args, ...moreArgs);
  };
};
const add = curry((a, b, c) => a + b + c);
console.log(add(1)(2)(3));  // 6
console.log(add(1, 2)(3));  // 6
```

---

##  Interview Questions - Unit 2

> [!question] Key Interview/Exam Questions

1. **`var` vs `let` vs `const` - key differences?**
   - `var`: function-scoped, hoisted (undefined), can re-declare
   - `let`: block-scoped, TDZ, no re-declaration
   - `const`: block-scoped, TDZ, no re-assignment of binding (object properties can change)

2. **What is the Temporal Dead Zone (TDZ)?**
   - The period between entering a scope and the variable's declaration being reached. Accessing `let`/`const` in TDZ throws ReferenceError.

3. **Arrow functions vs regular functions - key differences?**
   - No own `this` (lexical), no `arguments`, cannot be constructors, no `prototype`

4. **What is destructuring? Give an example.**
   - Syntax to unpack array elements or object properties into variables.
   ```js
   const { name, age } = user;
   const [first, ...rest] = arr;
   ```

5. **Difference between spread and rest?**
   - Both use `...`. Spread: expands iterable; Rest: collects remaining elements

6. **What are Promises? What are their states?**
   - Object for async ops; states: `pending`, `fulfilled`, `rejected`

7. **`Promise.all` vs `Promise.race` vs `Promise.allSettled`?**
   - `all`: all must fulfill (rejects on first rejection)
   - `race`: first to settle (fulfill or reject) wins
   - `allSettled`: waits for all, never rejects, returns all results

8. **What does `async` function always return?**
   - A Promise (even if you return a plain value, it's wrapped in Promise.resolve())

9. **Can you use `await` outside an async function?**
   - In modern JS (ES2022+), top-level await is allowed in ES modules; otherwise, must be inside an async function.

---

##  Revision Summary

> [!summary] Unit 2 Key Takeaways
>
> **Variables:**
> - Use `const` by default; `let` for mutable; avoid `var`
> - TDZ applies to `let` and `const`
>
> **Arrow Functions:**
> - Shorter syntax; lexical `this`; no `arguments`
>
> **Destructuring:**
> - Array: positional; Object: by name; supports defaults, rename, rest, nesting
>
> **Spread/Rest:**
> - Spread `...x`: expands; Rest `...x`: collects
>
> **Template Literals:**
> - Backticks, multi-line, `${expr}`, tagged templates
>
> **Classes:**
> - `class`, `constructor`, `extends`, `super`, static, getters/setters, private `#`
>
> **Modules:**
> - Named: `export { x }` / `import { x }`; Default: one per file
>
> **Async JS:**
> - Callbacks → callback hell
> - Promises → `.then().catch()` chaining; `Promise.all/race/allSettled`
> - async/await → cleaner, try/catch error handling; use `Promise.all` for parallel

^unit2-revision

---

*← [[Unit-1]] | [[Overview|CS-303 Overview]] | Next: [[Unit-3]] →*
