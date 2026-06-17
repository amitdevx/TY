---
title: "CS-353 Web Technology-II - Important Topics"
subject: CS-353
semester: VI
tags:
  - important-topics
  - web-tech-2
  - postgresql
  - react
  - rest-api
  - jwt
  - semester-vi
  - exam
aliases:
  - Web Tech II Important
  - CS353 Must-Know
created: 2026-06-16
type: important-topics
---

[[00-Dashboard/Home|Home]] | [[07-Exams/Exams-Dashboard|Exams Dashboard]]


# CS-353 Web Technology-II - Important Topics

> [!important] Exam Focus
> Web Tech-II is full-stack. PostgreSQL queries and REST API design are guaranteed. React Hooks (useState/useEffect) + JWT auth are the most scoring practical topics.

---

## Top 10 Most Important Topics

| # | Topic | Description | Probability |
|---|-------|-------------|-------------|
| 1 | **PostgreSQL - JOINs** | INNER, LEFT, RIGHT, FULL OUTER JOIN with examples |  |
| 2 | **REST API Design** | Express CRUD endpoints with proper HTTP methods/codes |  |
| 3 | **React useState & useEffect** | State management + side effects with API calls |  |
| 4 | **JWT Authentication** | Register, login, token generation, protected routes |  |
| 5 | **PostgreSQL Aggregates** | COUNT, SUM, AVG, GROUP BY, HAVING |  |
| 6 | **React Props & Components** | Functional components, props passing, lifting state |  |
| 7 | **Express Middleware** | Custom middleware, error handling, CORS |  |
| 8 | **React Router** | BrowserRouter, Routes, Link, useParams, useNavigate |  |
| 9 | **Async/Await in Express** | try-catch pattern with PostgreSQL queries |  |
| 10 | **React Context API** | Global state without Redux |  |

---

## "Definitely Going to Come" Section

> [!warning] Near-Certain Questions
> 1. **PostgreSQL JOINs** - write INNER JOIN and LEFT JOIN queries
> 2. **REST API CRUD** - build /api/resource endpoints (GET, POST, PUT, DELETE)
> 3. **React - useState + useEffect** - fetch and display API data, handle loading/error
> 4. **JWT Auth** - bcrypt hash password, jwt.sign on login, middleware verify token
> 5. **PostgreSQL aggregate queries** - GROUP BY with HAVING
> 6. **React parent-child** - pass props, handle events, lift state up

---

## Must-Know Definitions

| Term | Definition |
|------|-----------|
| **PostgreSQL** | Open-source RDBMS - ACID compliant, supports JSON, arrays, etc. |
| **SERIAL** | PostgreSQL auto-increment integer type |
| **REST API** | Architectural style - stateless HTTP-based client-server communication |
| **CRUD** | Create(POST), Read(GET), Update(PUT/PATCH), Delete(DELETE) |
| **CORS** | Cross-Origin Resource Sharing - allows/restricts cross-domain requests |
| **React** | JS library for building component-based UIs (Meta) |
| **JSX** | JavaScript XML - HTML-like syntax in JavaScript files |
| **useState** | Hook for local component state management |
| **useEffect** | Hook for side effects (API calls, subscriptions, timers) |
| **Virtual DOM** | React's in-memory representation of DOM for efficient updates |
| **JWT** | JSON Web Token - stateless auth token (Header.Payload.Signature) |
| **bcrypt** | Password hashing library - computationally expensive hash |
| **Middleware** | Function with (req, res, next) that runs between request and response |

---

## Quick Code Patterns

### PostgreSQL Common Queries
```sql
-- JOIN
SELECT e.name, d.name FROM employees e
JOIN departments d ON e.dept_id = d.id;

-- Aggregate
SELECT dept_id, COUNT(*), AVG(salary) FROM employees
GROUP BY dept_id HAVING AVG(salary) > 50000;

-- Subquery
SELECT * FROM emp WHERE salary > (SELECT AVG(salary) FROM emp);
```

### Express REST Route Template
```javascript
app.get('/api/items', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM items');
    res.json(result.rows);
  } catch (err) { res.status(500).json({ error: err.message }); }
});
```

### React useState + useEffect + API
```jsx
const [data, setData] = useState([]);
const [loading, setLoading] = useState(true);

useEffect(() => {
  axios.get('/api/data')
    .then(res => setData(res.data))
    .catch(err => console.error(err))
    .finally(() => setLoading(false));
}, []); // [] = run once on mount
```

### JWT Auth Middleware
```javascript
const authenticate = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch { res.status(403).json({ error: 'Invalid token' }); }
};
```

---

## HTTP Status Codes Reference

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Missing token |
| 403 | Forbidden | Invalid token |
| 404 | Not Found | Resource doesn't exist |
| 500 | Internal Server Error | Server crash |

---

## Common Mistakes to Avoid

> [!warning] Avoid These Errors
> - **`useEffect` dependency array:** Missing dependencies cause stale closures; extra dependencies cause infinite loops.
> - **State mutation:** NEVER mutate state directly - use `setData([...data, newItem])` not `data.push(newItem)`.
> - **JWT secret in code:** Always use `process.env.JWT_SECRET` - never hardcode in production.
> - **PostgreSQL parameterized queries:** Use `$1, $2` placeholders, never string concatenation (SQL injection!).
> - **CORS:** Add `cors()` middleware BEFORE route handlers.
> - **bcrypt async:** Use `await bcrypt.hash()` and `await bcrypt.compare()` - don't forget await!
> - **React key prop:** Always add `key={unique_id}` when using `map()` to render lists.

---

## PostgreSQL Data Types Quick Reference

| Type | Example |
|------|---------|
| `SERIAL` | Auto-increment integer |
| `VARCHAR(n)` | Variable-length string |
| `TEXT` | Unlimited text |
| `INTEGER` | Whole number |
| `DECIMAL(p,s)` | Fixed precision decimal |
| `BOOLEAN` | true/false |
| `DATE` | Date only |
| `TIMESTAMP` | Date + time |
| `JSON/JSONB` | JSON data |
| `ARRAY` | Array type |

---

*Tags: CS-353 Web Technology-II | Semester VI | [[07-Exams/Exams-Dashboard|Exams]]*
