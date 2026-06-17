---
title: "CS-353 Web Technology-II - Expected PYQ"
subject: CS-353
paper: Web Technology-II
semester: VI
tags:
  - pyq
  - web-tech-2
  - postgresql
  - rest-api
  - react
  - jwt
  - semester-vi
  - exam
aliases:
  - Web Tech II PYQ
  - CS353 Questions
created: 2026-06-16
type: pyq
---

[[00-Dashboard/Home|Home]] | [[07-Exams/Exams-Dashboard|Exams Dashboard]]


# CS-353 Web Technology-II - Expected PYQ

> [!important] Exam Strategy
> Web Tech-II covers full-stack MERN-like development with PostgreSQL. Focus on PostgreSQL queries, REST API design with Express, React Hooks (useState/useEffect), and JWT authentication.

---

## Unit-wise Distribution

| Unit | Topic | Weightage |
|------|-------|-----------|
| I | PostgreSQL | 25% |
| II | REST API with Express/Node | 25% |
| III | React Fundamentals | 25% |
| IV | Authentication (JWT) | 15% |
| V | Deployment & DevOps | 10% |

---

## Section A - Short Answer (2 Marks)

1. **What is PostgreSQL? How does it differ from MySQL?**
2. **What is a foreign key? How is it defined in PostgreSQL?**
3. **What is a JOIN? Name its types.**
4. **What is a REST API? What are the HTTP methods used?**
5. **What is the difference between PUT and PATCH?**
6. **What are HTTP status codes? Give codes for 200, 201, 400, 401, 404, 500.**
7. **What is CORS? Why is it needed?**
8. **What is React? How is it different from Angular?**
9. **What is JSX in React?**
10. **What are React Hooks? Name the most common ones.**
11. **What is the difference between `useState` and `useEffect`?**
12. **What is the Virtual DOM in React?**
13. **What is `props` in React?**
14. **What is JWT? What are its three parts?**
15. **What is the difference between authentication and authorization?**
16. **What is bcrypt used for?**
17. **What is middleware in Express?**
18. **What is async/await in the context of Express routes?**
19. **What is React Router? What is `<Route>` and `<Link>`?**
20. **What is Redux? When would you use it over useState?**

---

## Section B - Long Answer (5–7 Marks)

---

### Q1. PostgreSQL - DDL, DML, and Joins ()

```sql
-- Create tables
CREATE TABLE departments (
  dept_id SERIAL PRIMARY KEY,
  dept_name VARCHAR(100) NOT NULL,
  location VARCHAR(100)
);

CREATE TABLE employees (
  emp_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  salary DECIMAL(10, 2),
  dept_id INT REFERENCES departments(dept_id) ON DELETE SET NULL,
  hire_date DATE DEFAULT CURRENT_DATE
);

-- Insert data
INSERT INTO departments (dept_name, location) VALUES
  ('Engineering', 'Pune'), ('Marketing', 'Mumbai');

INSERT INTO employees (name, email, salary, dept_id) VALUES
  ('Amit', 'amit@co.com', 75000, 1),
  ('Priya', 'priya@co.com', 65000, 2),
  ('Raj', 'raj@co.com', 80000, 1);

-- SELECT with conditions
SELECT * FROM employees WHERE salary > 70000 ORDER BY salary DESC;

-- Aggregate functions
SELECT dept_id, COUNT(*) as count, AVG(salary) as avg_salary
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 60000;

-- INNER JOIN
SELECT e.name, e.salary, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- LEFT JOIN (all employees, even without dept)
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- Subquery
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Update & Delete
UPDATE employees SET salary = salary * 1.10 WHERE dept_id = 1;
DELETE FROM employees WHERE emp_id = 3;
```

---

### Q2. REST API with Express.js + PostgreSQL ()

```javascript
// server.js
const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(cors());

const pool = new Pool({
  host: 'localhost', database: 'college',
  user: 'postgres', password: 'password', port: 5432
});

// GET all students
app.get('/api/students', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM students ORDER BY id');
    res.status(200).json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// GET single student
app.get('/api/students/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query('SELECT * FROM students WHERE id = $1', [id]);
    if (result.rows.length === 0) return res.status(404).json({ error: 'Not found' });
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// POST create student
app.post('/api/students', async (req, res) => {
  try {
    const { name, email, cgpa } = req.body;
    const result = await pool.query(
      'INSERT INTO students (name, email, cgpa) VALUES ($1, $2, $3) RETURNING *',
      [name, email, cgpa]
    );
    res.status(201).json(result.rows[0]);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// PUT update student
app.put('/api/students/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { name, email, cgpa } = req.body;
    const result = await pool.query(
      'UPDATE students SET name=$1, email=$2, cgpa=$3 WHERE id=$4 RETURNING *',
      [name, email, cgpa, id]
    );
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// DELETE student
app.delete('/api/students/:id', async (req, res) => {
  try {
    const { id } = req.params;
    await pool.query('DELETE FROM students WHERE id = $1', [id]);
    res.json({ message: 'Student deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(5000, () => console.log('API running on port 5000'));
```

---

### Q3. React Hooks - useState and useEffect ()

```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function StudentList() {
  // useState: manage local state
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [newName, setNewName] = useState('');
  const [count, setCount] = useState(0);

  // useEffect: side effects (API calls, subscriptions)
  useEffect(() => {
    // Runs after render, when [] dependency is empty = runs once
    fetchStudents();

    return () => {
      // Cleanup function (runs on unmount)
      console.log('Component unmounted');
    };
  }, []); // empty array = run only on mount

  const fetchStudents = async () => {
    try {
      const response = await axios.get('/api/students');
      setStudents(response.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const addStudent = async () => {
    const res = await axios.post('/api/students', { name: newName });
    setStudents([...students, res.data]);  // immutable state update
    setNewName('');
  };

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      <h2>Students ({count})</h2>
      <input value={newName} onChange={e => setNewName(e.target.value)} />
      <button onClick={addStudent}>Add</button>
      <ul>
        {students.map(s => (
          <li key={s.id}>{s.name} - {s.cgpa}</li>
        ))}
      </ul>
    </div>
  );
}

export default StudentList;
```

---

### Q4. React - Props, State, and Component Communication ()

```jsx
// Parent Component
function App() {
  const [message, setMessage] = useState('Hello from Parent');

  const handleChildMessage = (msg) => {
    setMessage(msg);
  };

  return (
    <div>
      <h1>{message}</h1>
      <Child
        title="Student Info"
        onSendMessage={handleChildMessage}
      />
    </div>
  );
}

// Child Component (receives props)
function Child({ title, onSendMessage }) {
  return (
    <div>
      <h2>{title}</h2>
      <button onClick={() => onSendMessage('Hello from Child!')}>
        Send to Parent
      </button>
    </div>
  );
}
```

---

### Q5. JWT Authentication ()

```javascript
// server.js - Auth routes
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const SECRET = process.env.JWT_SECRET || 'mysecretkey';

// Register
app.post('/api/register', async (req, res) => {
  const { username, password } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);
  await pool.query(
    'INSERT INTO users (username, password) VALUES ($1, $2)',
    [username, hashedPassword]
  );
  res.status(201).json({ message: 'User registered' });
});

// Login
app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;
  const result = await pool.query('SELECT * FROM users WHERE username = $1', [username]);

  if (result.rows.length === 0)
    return res.status(401).json({ error: 'User not found' });

  const valid = await bcrypt.compare(password, result.rows[0].password);
  if (!valid) return res.status(401).json({ error: 'Invalid password' });

  const token = jwt.sign({ id: result.rows[0].id, username }, SECRET, { expiresIn: '1h' });
  res.json({ token });
});

// Protected Middleware
function authenticate(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1]; // Bearer <token>
  if (!token) return res.status(401).json({ error: 'No token provided' });

  try {
    const decoded = jwt.verify(token, SECRET);
    req.user = decoded;
    next();
  } catch {
    res.status(403).json({ error: 'Invalid token' });
  }
}

// Protected route
app.get('/api/profile', authenticate, (req, res) => {
  res.json({ message: `Welcome, ${req.user.username}` });
});
```

**JWT Structure:**
```
Header.Payload.Signature
eyJ...  .eyJ...  .SflK...

Header:  { "alg": "HS256", "typ": "JWT" }
Payload: { "id": 1, "username": "amit", "exp": 1234567890 }
Signature: HMACSHA256(base64(header) + "." + base64(payload), secret)
```

---

### Q6. React Router ()

```jsx
import { BrowserRouter, Route, Routes, Link, useNavigate, useParams } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/students">Students</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/students" element={<StudentList />} />
        <Route path="/students/:id" element={<StudentDetail />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

// Access URL params
function StudentDetail() {
  const { id } = useParams();
  const navigate = useNavigate();

  return (
    <div>
      <h2>Student ID: {id}</h2>
      <button onClick={() => navigate('/students')}>Back</button>
    </div>
  );
}
```

---

## Most Expected Questions

> [!tip] High Probability
> 1.  PostgreSQL JOIN queries - INNER, LEFT, RIGHT
> 2.  REST API CRUD with Express + PostgreSQL
> 3.  React useState + useEffect with API call
> 4.  JWT Authentication - register, login, protected routes
> 5.  React props and parent-child communication
> 6.  PostgreSQL aggregate functions - GROUP BY, HAVING
> 7.  React Router - Routes, Link, useParams

---

*Tags: CS-353 Web Technology-II | Semester VI | [[07-Exams/Exams-Dashboard|Exams]]*
