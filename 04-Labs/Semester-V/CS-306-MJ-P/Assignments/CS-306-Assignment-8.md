# Assignment 8: Modern JavaScript ES6+

## Problem Statement / Aim
To implement modern JavaScript (ES6+) features such as arrow functions, destructuring, and let/const.

## Theory & Concept
ECMAScript 6 (ES6) introduced significant updates to JavaScript:
- **`let` and `const`**: Block-scoped variable declarations.
- **Arrow Functions**: Shorter syntax for writing functions.
- **Template Literals**: Multi-line strings and string interpolation using backticks (``).
- **Destructuring**: Unpacking values from arrays or properties from objects into distinct variables.

## Fully Solved Code
```javascript
// Using const and let
const greeting = "Hello";
let count = 5;

// Arrow function
const multiply = (a, b) => a * b;

// Object destructuring
const student = { name: "John", age: 20, grade: "A" };
const { name, grade } = student;

// Template literals
const message = `${greeting}, ${name}! You scored grade ${grade} and the result is ${multiply(count, 2)}.`;

console.log(message);

// Spread Operator
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log("Spread array:", arr2);
```

## Expected Output
```
Hello, John! You scored grade A and the result is 10.
Spread array: [ 1, 2, 3, 4, 5 ]
```

---
[[CS-306-Viva-8|View Viva Questions]]
