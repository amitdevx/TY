---
title: "CS-303 Web Technology-I - Important Questions"
aliases: ["CS303 Important Questions", "Web Tech IQ", "CS303 Exam Questions"]
tags:
  - subject/web-technology
  - semester/V
  - exam-prep
  - important-questions
subject_code: CS-303-MJ-T
type: important-questions
last_reviewed: 2026-06-16
---

#  CS-303 Web Technology-I - Important Questions

> [!note] Navigation
> [[Overview|CS-303 Overview]] | [[Revision|CS-303 Revision]] | [[Interview-Prep|CS-303 Interview-Prep]]

---

> [!important] How to Use This File
> -  = Most likely to appear in exam
> -  = Descriptive / long answer
> -  = Code-based question
> -  = Practical/numerical

---

##  Chapter 1 - Web Basics (HTML5 & CSS3)

### Short Answer Questions

1.  What are HTML5 semantic elements? Name and explain any five. ^q1-1
2. What is the difference between `<section>`, `<article>`, and `<div>`?
3.  Explain the CSS Box Model with a diagram.
4. What is `box-sizing: border-box`? Why is it preferred?
5. What is CSS specificity? Explain with examples.
6. List 5 CSS pseudo-classes and 3 pseudo-elements with examples.
7. What is the difference between `nth-child` and `nth-of-type`?

### Long Answer Questions

8.  Explain CSS Flexbox in detail. Write a CSS code to create a responsive card layout using Flexbox.
9.  Explain CSS Grid layout. How does it differ from Flexbox? Write code to create a 3-column webpage layout.
10.  What is Responsive Web Design? Explain media queries with examples for mobile, tablet, and desktop breakpoints.
11.  Explain CSS animations. What are `@keyframes`? Write CSS to create a bouncing ball animation.
12.  Write a complete semantic HTML5 page structure for a blog post page.

### Code Questions

13.  Write CSS to center a div both horizontally and vertically using Flexbox.
14.  Write CSS media query to hide navigation links on mobile (< 768px).
15.  Create a responsive grid of cards (3 per row on desktop, 2 on tablet, 1 on mobile) using CSS Grid.
16.  Write CSS for a button that changes color and scales up on hover using transitions.
17.  Write CSS animation for a loading spinner (rotating element).

---

##  Chapter 2 - Advanced JavaScript ES6+

### Short Answer Questions

18.  What is the difference between `var`, `let`, and `const`? Explain with scope examples.
19. What is the Temporal Dead Zone (TDZ)?
20.  What are arrow functions? How is `this` different in arrow functions vs regular functions?
21. Explain destructuring with examples for both arrays and objects.
22.  What is the difference between spread and rest operators?
23. What are template literals? How do tagged templates work?
24. What is the difference between ES6 classes and constructor functions?
25. Explain `import` and `export` in JavaScript modules.

### Long Answer Questions

26.  Explain callback functions. What is callback hell? How do Promises solve this problem?
27.  Explain JavaScript Promises in detail. What are the states of a Promise? Explain `Promise.all`, `Promise.race`, `Promise.allSettled`.
28.  What is `async/await`? How does it make asynchronous code easier to write? Explain error handling with `try/catch`.
29.  Explain the difference between callbacks, Promises, and async/await with the same code example written three ways.
30.  Write an ES6 class `Animal` with constructor, methods, static method, and getter/setter. Then extend it with `Dog`.

### Code Questions

31.  Write a function using async/await that fetches user data and posts from two API endpoints in parallel using `Promise.all`.
32.  Write a `debounce` function using ES6+ features.
33.  Rewrite the following with arrow functions, destructuring, and template literals:
    ```javascript
    var person = { name: "Alice", age: 25 };
    function greet(person) { return "Hello, " + person.name + "!"; }
    ```
34.  Use array destructuring to swap two variables without a temp variable.
35.  Write a function that takes any number of numbers (using rest), filters out negatives, and returns their sum.

---

##  Chapter 3 - Node.js Fundamentals

### Short Answer Questions

36.  What is Node.js? How is it different from browser JavaScript?
37. What is the event loop in Node.js?
38.  What is non-blocking I/O? Why is it important in Node.js?
39. What is npm? What is `package.json`?
40. What is the difference between `dependencies` and `devDependencies`?
41. What is `process.nextTick()`? How is it different from `setTimeout(fn, 0)`?
42. What is `__dirname` and `__filename`?
43. What are the phases of the Node.js event loop?

### Long Answer Questions

44.  Explain the Node.js event loop in detail with a diagram. What is the execution order of callbacks?
45.  Explain the `path` module in Node.js. Describe `join`, `resolve`, `dirname`, `basename`, `extname` with examples.
46.  Create a basic HTTP server in Node.js that handles routes `/`, `/about`, `/api/users`, and returns a 404 for unknown routes.

### Code Questions

47.  Write a Node.js HTTP server that:
    - Responds with HTML on GET /
    - Responds with JSON array on GET /api/data
    - Returns 404 for unknown routes
48.  Write a Node.js program to demonstrate the execution order of `console.log`, `setTimeout`, `Promise.resolve().then()`, and `process.nextTick()`.
49.  Write code to serve static files (HTML, CSS, JS) from a `public/` folder using Node.js `http` and `fs` modules.

---

##  Chapter 4 - File Handling with Node.js

### Short Answer Questions

50.  What is the difference between `fs.readFile()` and `fs.readFileSync()`?
51. What is the difference between `fs.writeFile()` and `fs.appendFile()`?
52. How do you delete a file in Node.js?
53. How do you create a directory recursively in Node.js?
54.  What is Multer? Why is it used for file uploads?
55. What error codes should you handle in file operations (`ENOENT`, `EACCES`, `EEXIST`)?

### Long Answer Questions

56.  Explain synchronous vs asynchronous file operations in Node.js. When should each be used?
57.  Explain how to read, write, update, and delete JSON files in Node.js. Give code examples for each.
58.  Write a Node.js program that implements a simple JSON-based file database with CRUD operations.

### Code Questions

59.  Write a Node.js program to:
    - Read contents of `input.txt`
    - Reverse the content
    - Write reversed content to `output.txt`
60.  Write an async function that reads all `.json` files from a directory and parses them.
61.  Write Express + Multer code to:
    - Accept single file upload on `/upload`
    - Validate file type (images only)
    - Limit file size to 2MB
    - Return file info as JSON response
62.  Write a Node.js program to create a logger that appends timestamped log entries to a file.
63.  Write code to recursively list all files in a directory with their sizes.

---

##  Previous Year-Style Questions (Most Important)

> [!warning] These types of questions appear most frequently

### 5-Mark Questions
1.  Write HTML5 page structure with all semantic elements. [Unit 1]
2.  Explain flexbox with `justify-content` and `align-items` values. [Unit 1]
3.  What is callback hell? How are Promises better? [Unit 2]
4.  Explain the Node.js event loop with diagram. [Unit 3]
5.  Write a Node.js HTTP server with basic routing. [Unit 3]

### 10-Mark Questions
1.  Explain CSS Grid and Flexbox with examples. Compare the two. [Unit 1]
2.  Explain async JS evolution: callbacks → Promises → async/await. Write same code in all three styles. [Unit 2]
3.  Explain Node.js file handling. Write code for read/write/append/delete with both sync and async methods. [Unit 4]
4.  Implement a file upload system using Express + Multer with validation. [Unit 4]
5.  Explain ES6 features: let/const, arrow functions, destructuring, spread, template literals, classes. [Unit 2]

---

*[[Overview|CS-303 Overview]] | [[Revision|CS-303 Revision]] | [[Interview-Prep|CS-303 Interview-Prep]]*
