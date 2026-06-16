---
title: CS-306-MJ-P Java and Web Lab
tags: [lab, java-lab, web-lab, semester-v, cs-306, java, html, css, javascript, nodejs]
aliases: [Java Web Lab, CS-306 Lab]
lab_code: CS-306-MJ-P
based_on: CS-301-MJ-T Core Java and CS-303-MJ-T Web Technology
language: Java, HTML, CSS, JavaScript, Node.js
semester: V
created: 2026-06-16
updated: 2026-06-16
---

#  CS-306-MJ-P - Java and Web Lab

> [!important] Lab Info
> **Code:** CS-306-MJ-P | **Based On:** CS-301 Core Java & CS-303 Web Technology
> **Languages:** Java, HTML/CSS/JS, Node.js
> **IDE:** VS Code / IntelliJ IDEA / Eclipse

---

## ️ Lab Navigation

| Part | Topic | Status |
|------|-------|--------|
| A - Java OOP | Classes, Interfaces, Exceptions | ⬜ |
| B - Java Collections | ArrayList, HashMap, Iterator | ⬜ |
| C - File Handling | I/O Streams, Serialization | ⬜ |
| D - JavaFX | GUI, Event Handling, FXML | ⬜ |
| E - HTML/CSS | Responsive Design, Flexbox, Grid | ⬜ |
| F - JavaScript | DOM, Events, AJAX, Fetch API | ⬜ |
| G - Node.js | Express, REST API, MongoDB | ⬜ |

---

##  Syllabus - Java Section

### Part A: Object-Oriented Programming

**Programs:**
1. Class and objects - Student class with constructors, getters/setters
2. Inheritance (single, multilevel, hierarchical)
3. Method overriding and `super` keyword
4. Interface implementation - `Drawable`, `Resizable`
5. Abstract class vs Interface comparison
6. Exception handling - try-catch-finally, custom exceptions
7. Multithreading - Thread class, Runnable, synchronization

### Part B: Java Collections Framework

**Programs:**
1. `ArrayList` - add, remove, sort, iterate
2. `LinkedList` - queue/stack operations
3. `HashMap` - word frequency counter
4. `TreeMap` - sorted map operations
5. `HashSet` vs `TreeSet`
6. `Iterator` and `ListIterator`
7. `Collections.sort()` with `Comparator`

### Part C: File Handling & I/O

**Programs:**
1. `FileReader`/`FileWriter` - read/write text files
2. `BufferedReader`/`BufferedWriter` - efficient I/O
3. `FileInputStream`/`FileOutputStream` - binary files
4. Object Serialization/Deserialization
5. `Scanner` for file parsing

### Part D: JavaFX (GUI Programming)

**Programs:**
1. Basic JavaFX window with Scene, Stage
2. Button, TextField, Label with event handlers
3. GridPane, VBox, HBox layouts
4. TableView with ObservableList
5. FXML with SceneBuilder
6. Simple calculator application

---

##  Syllabus - Web Section

### Part E: HTML & CSS

**Programs:**
1. Semantic HTML5 - header, nav, main, footer
2. CSS Box Model - margin, padding, border
3. Flexbox layout - responsive navigation
4. CSS Grid - complex page layouts
5. CSS animations and transitions
6. Media queries - responsive design
7. Bootstrap 5 integration

### Part F: JavaScript

**Programs:**
1. DOM manipulation - getElementById, querySelector
2. Event listeners - click, submit, keypress
3. Form validation with regex
4. Arrays - map, filter, reduce
5. ES6+ features - arrow functions, destructuring, spread
6. Fetch API - consuming REST APIs
7. Local Storage - CRUD operations
8. Promises and Async/Await

### Part G: Node.js & Backend

**Programs:**
1. Basic Node.js server - `http` module
2. Express.js - routing, middleware
3. RESTful API - GET, POST, PUT, DELETE
4. Express with MongoDB/Mongoose
5. JWT authentication basics
6. File upload with Multer

---

##  Completion Tracker

### Java Programs

- [ ] OOP - Class & Inheritance
- [ ] Interface & Abstract class
- [ ] Exception Handling
- [ ] Multithreading
- [ ] Collections - ArrayList/HashMap
- [ ] File I/O & Serialization
- [ ] JavaFX Calculator

### Web Programs

- [ ] HTML5 Semantic Page
- [ ] CSS Flexbox Layout
- [ ] CSS Grid Page
- [ ] Responsive Design
- [ ] DOM Manipulation
- [ ] Form Validation (JS)
- [ ] Fetch API + Display
- [ ] Node.js REST API

---

## ️ Setup Guide

### Java Setup

```bash
# Check Java version
java --version

# Compile Java program
javac Program.java

# Run compiled class
java Program

# Run JavaFX (with module path)
java --module-path $PATH_TO_FX --add-modules javafx.controls ProgramName
```

### Node.js Setup

```bash
# Check Node version
node --version
npm --version

# Initialize Node project
npm init -y

# Install Express
npm install express

# Install nodemon for development
npm install -g nodemon

# Run project
node app.js
# or with nodemon
nodemon app.js
```

### Project Structure (Node.js REST API)

```
my-api/
├── app.js          # Main entry point
├── routes/
│   ├── users.js    # User routes
│   └── products.js
├── models/
│   └── User.js     # Mongoose model
├── middleware/
│   └── auth.js     # Authentication
├── package.json
└── .env            # Environment variables
```

---

##  Quick Reference

### Java Collections Cheat Sheet

| Collection | Order | Duplicates | Null | Use When |
|-----------|-------|-----------|------|----------|
| ArrayList | Insertion | Yes | Yes | Random access |
| LinkedList | Insertion | Yes | Yes | Frequent insert/delete |
| HashSet | No | No | One | Unique elements |
| TreeSet | Sorted | No | No | Sorted unique |
| HashMap | No | (keys)No | Yes | Key-value |
| TreeMap | Key sorted | No | No | Sorted K-V |

### HTTP Methods Reference

| Method | Purpose | Body | Idempotent |
|--------|---------|------|-----------|
| GET | Retrieve | No | Yes |
| POST | Create | Yes | No |
| PUT | Update (replace) | Yes | Yes |
| PATCH | Update (partial) | Yes | No |
| DELETE | Remove | No | Yes |

---

##  Related

- [[../../../01-Core-Subjects/Semester-V/CS-301-Core-Java/Dashboard|CS-301 Core Java Dashboard]]
- [[../../../11-Tracking/Lab-Tracker|Lab Tracker]]

---

*Lab Overview | CS-306-MJ-P | Semester V | Last Updated: 2026-06-16*
