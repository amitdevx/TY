---
title: "CS-303 Web Technology-I - Expected PYQ"
subject: CS-303
paper: Web Technology-I
semester: V
tags:
  - pyq
  - web-tech
  - html5
  - css3
  - javascript
  - nodejs
  - semester-v
  - exam
aliases:
  - Web Tech PYQ
  - CS303 Questions
created: 2026-06-16
type: pyq
---

#  CS-303 Web Technology-I - Expected PYQ

> [!important] Exam Strategy
> Web Tech-I is a practical-heavy paper. Expect at least 2 coding/programming questions. Focus on HTML5 semantic elements, CSS Flexbox/Grid, ES6 features, and Node.js file handling. Short answers on definitions fetch easy marks.

---

## ️ Unit-wise Question Distribution

| Unit | Topic | Weightage |
|------|-------|-----------|
| I | HTML5 & CSS3 | 25% |
| II | JavaScript ES6 | 25% |
| III | Node.js Basics | 20% |
| IV | File Handling & npm | 15% |
| V | Responsive Design & APIs | 15% |

---

## ️ Section A - Short Answer Questions (2 Marks Each)

### Unit I: HTML5 & CSS3

1. **What are semantic elements in HTML5? List any four.**
2. **Differentiate between `<div>` and `<section>` in HTML5.**
3. **What is the purpose of the `<canvas>` element in HTML5?**
4. **List any four new input types introduced in HTML5.**
5. **What is the difference between `localStorage` and `sessionStorage`?**
6. **Define the CSS Box Model and name its four components.**
7. **What is the difference between `em` and `rem` units in CSS?**
8. **Define CSS Specificity. What is the priority order?**
9. **What is a CSS pseudo-class? Give two examples.**
10. **Differentiate between `position: absolute` and `position: relative` in CSS.**
11. **What is the `viewport` meta tag used for in responsive design?**
12. **What does `display: flex` do? Name any two flex properties.**

### Unit II: JavaScript ES6

13. **What is the difference between `let`, `const`, and `var`?**
14. **What is a Promise in JavaScript? What are its states?**
15. **What is destructuring assignment in ES6? Give an example.**
16. **Differentiate between `==` and `===` in JavaScript.**
17. **What is an arrow function? How does it differ from a regular function?**
18. **What is the purpose of the `spread` operator (`...`)?**
19. **What is a template literal? Give syntax and example.**
20. **Define `async/await` in JavaScript.**

### Unit III: Node.js

21. **What is Node.js? What makes it non-blocking?**
22. **What is the role of `package.json` in a Node.js project?**
23. **Differentiate between `require()` and `import` in Node.js.**
24. **What is an Event Emitter in Node.js?**
25. **What is the purpose of `process.argv` in Node.js?**
26. **What is middleware in Express.js?**

---

##  Section B - Long Answer Questions (5–7 Marks Each)

### Q1. Registration Form with HTML5 Validation ( HIGH PROBABILITY)

Write HTML5 code to create a registration form with Name, Email, Password, DOB (date), Gender (radio), Skills (checkbox), and Submit. Use fieldset and legend.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Registration Form</title>
</head>
<body>
  <form action="#" method="POST">
    <fieldset>
      <legend>Personal Information</legend>
      <label>Name: <input type="text" name="name" required></label><br>
      <label>Email: <input type="email" name="email" required></label><br>
      <label>Password: <input type="password" name="pass" required></label><br>
      <label>DOB: <input type="date" name="dob" required></label><br>
      <label>Gender:
        <input type="radio" name="gender" value="male"> Male
        <input type="radio" name="gender" value="female"> Female
      </label><br>
      <label>Skills:
        <input type="checkbox" name="skill" value="html"> HTML
        <input type="checkbox" name="skill" value="css"> CSS
        <input type="checkbox" name="skill" value="js"> JavaScript
      </label><br>
      <input type="submit" value="Register">
    </fieldset>
  </form>
</body>
</html>
```

---

### Q2. HTML5 Multimedia - Audio & Video

```html
<!-- Video -->
<video width="640" height="360" controls autoplay muted loop>
  <source src="movie.mp4" type="video/mp4">
  Your browser does not support video.
</video>

<!-- Audio -->
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  Your browser does not support audio.
</audio>
```

**Key Attributes:** `controls`, `autoplay`, `muted`, `loop`, `poster` (video), `preload`

---

### Q3. CSS Flexbox - Responsive Navbar ( HIGH PROBABILITY)

```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  background-color: #333;
  padding: 10px 20px;
}
.navbar a { color: white; text-decoration: none; padding: 8px 15px; }
.navbar a:hover { background-color: #555; border-radius: 4px; }
```

| Property | Values | Purpose |
|----------|--------|---------|
| `justify-content` | flex-start, center, space-between | Main axis |
| `align-items` | stretch, center, flex-start | Cross axis |
| `flex-direction` | row, column | Direction |
| `flex-wrap` | wrap, nowrap | Wrapping |

---

### Q4. CSS Grid Layout

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding: 20px;
}
@media (max-width: 768px) {
  .container { grid-template-columns: 1fr; }
}
```

---

### Q5. ES6 Promises and async/await ( HIGH PROBABILITY)

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Data fetched successfully!");
    }, 2000);
  });
}

// .then()/.catch()
fetchData().then(data => console.log(data)).catch(err => console.error(err));

// async/await
async function getData() {
  try {
    let result = await fetchData();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}
getData();
```

---

### Q6. ES6 Features - Arrow, Template Literals, Destructuring, Spread/Rest

```javascript
// Arrow Functions
const add = (a, b) => a + b;

// Template Literals
let name = "Amit";
console.log(`Hello, ${name}!`);

// Destructuring
const [x, y] = [1, 2];
const { brand } = { brand: "Toyota" };

// Spread
let arr2 = [...[1,2,3], 4, 5];

// Rest
function sum(...nums) { return nums.reduce((a,b) => a+b, 0); }
```

---

### Q7. ES6 Classes with Inheritance

```javascript
class Animal {
  constructor(name) { this.name = name; }
  speak() { console.log(`${this.name} makes a sound.`); }
}
class Dog extends Animal {
  speak() { console.log(`${this.name} barks!`); }
}
const d = new Dog("Rex");
d.speak(); // Rex barks!
```

---

### Q8. Node.js File Handling using `fs` module ( HIGH PROBABILITY)

```javascript
const fs = require('fs');

// Write
fs.writeFile('demo.txt', 'Hello Node.js!', err => { if(err) throw err; });

// Read
fs.readFile('demo.txt', 'utf8', (err, data) => { console.log(data); });

// Append
fs.appendFile('demo.txt', '\nNew Line', err => { if(err) throw err; });

// Delete
fs.unlink('demo.txt', err => { if(err) throw err; });
```

---

### Q9. Simple HTTP Server with Routing ( HIGH PROBABILITY)

```javascript
const http = require('http');
const url  = require('url');

const server = http.createServer((req, res) => {
  const path = url.parse(req.url).pathname;
  res.setHeader('Content-Type', 'text/html');

  if (path === '/') {
    res.writeHead(200); res.end('<h1>Home Page</h1>');
  } else if (path === '/about') {
    res.writeHead(200); res.end('<h1>About Us</h1>');
  } else {
    res.writeHead(404); res.end('<h1>404 Not Found</h1>');
  }
});

server.listen(3000, () => console.log('Server on http://localhost:3000'));
```

---

### Q10. npm and package.json

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "scripts": { "start": "node index.js" },
  "dependencies": { "express": "^4.18.2" },
  "devDependencies": { "nodemon": "^3.0.1" }
}
```

```bash
npm install express       # Install
npm install -D nodemon    # Dev dependency
npm update express        # Update
npm uninstall express     # Remove
```

---

##  Most Expected Questions (High Probability)

> [!tip] These topics have very high chance of appearing
> 1.  Responsive webpage with Flexbox/Grid
> 2.  Registration form with HTML5 validation
> 3.  Promises / async-await with example
> 4.  Node.js file read/write using `fs`
> 5.  Simple HTTP server with routing
> 6.  ES6 Classes with inheritance
> 7.  Media Queries for responsive design
> 8.  localStorage vs sessionStorage with code

---

##  Quick Revision Definitions

| Term | One-line Definition |
|------|---------------------|
| Semantic HTML | Tags that convey meaning (`<nav>`, `<article>`) |
| Flexbox | 1D CSS layout for row/column arrangement |
| CSS Grid | 2D CSS layout for rows AND columns |
| Promise | Object for eventual async completion/failure |
| Event Loop | Node.js mechanism for non-blocking I/O |
| Middleware | Function between req and res in Express |
| npm | Node Package Manager |

---

*Tags: CS-303 Web Technology-I | Semester V | [[07-Exams]]*
