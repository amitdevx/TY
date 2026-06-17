---
title: "CS-351 Advanced Java Revision"
tags: [cs-351, advanced-java, java-ee, jdbc, spring, semester-vi, revision]
subject_code: CS-351-MJ-T
type: revision
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Advanced Java - Quick Revision Summary

> [!tip] How to use this guide
> Review this page for a rapid recall of Collections, Multithreading, JDBC, Servlets/JSP, and Spring Boot concepts before your exam.

---

## 1. Collections Framework

The Collections Framework provides a unified architecture for storing and manipulating a group of objects.

| Interface | Key Classes | Properties |
|---|---|---|
| **List** | `ArrayList`, `LinkedList` | Ordered collection. Allows duplicates. Index-based access. `ArrayList` is faster for read, `LinkedList` for insertion/deletion. |
| **Set** | `HashSet`, `TreeSet` | Unordered collection. **No duplicates allowed**. `TreeSet` maintains sorted order. |
| **Map** | `HashMap`, `TreeMap` | Key-Value pairs. **Keys must be unique**, values can be duplicate. `TreeMap` sorts by key. (Map does NOT extend Collection interface). |

**Iterators:** Used to traverse collections. `Iterator` works for all collections (forward only). `ListIterator` works only for Lists (forward and backward).

---

## 2. Multithreading

A thread is a lightweight sub-process. Multithreading maximizes CPU utilization.

### Creating Threads
1. **Extend `Thread` class:** Override `run()`. Call `start()` to execute.
2. **Implement `Runnable` interface:** Implement `run()`. Pass instance to a `Thread` constructor and call `start()`. (Preferred method as it allows extending another class).

### Thread Lifecycle
New $\rightarrow$ Runnable $\rightarrow$ Running $\rightarrow$ Waiting/Blocked $\rightarrow$ Terminated (Dead)

### Synchronization
Prevents thread interference and memory consistency errors. The `synchronized` keyword ensures that only one thread can execute a block of code or a method on an object at a given time.

### Inter-thread Communication
Uses `wait()`, `notify()`, and `notifyAll()` methods from the `Object` class. Must be called from within a synchronized context.

---

## 3. JDBC (Java Database Connectivity)

JDBC is an API used to connect and execute queries with a database.

### 5 Steps to Connect to Database
1. **Load/Register Driver:** `Class.forName("com.mysql.cj.jdbc.Driver");`
2. **Establish Connection:** `Connection con = DriverManager.getConnection(url, user, pass);`
3. **Create Statement:** `Statement st = con.createStatement();`
4. **Execute Query:** `ResultSet rs = st.executeQuery("SELECT * FROM EMP");` (For SELECT) or `st.executeUpdate()` (For INSERT/UPDATE/DELETE).
5. **Close Connection:** `con.close();`

### Statement Types
- `Statement`: Used for general-purpose access, static SQL at runtime.
- `PreparedStatement`: Used when you plan to use the SQL statement many times. Accepts parameterized SQL (`?`). Prevents SQL Injection.
- `CallableStatement`: Used to access stored procedures in the database.

---

## 4. Servlets and JSP

### Servlets
Java programs that run on a web server, handling client requests and generating dynamic responses.
- **Lifecycle:** `init()` (called once) $\rightarrow$ `service()` (called per request, dispatches to `doGet`/`doPost`) $\rightarrow$ `destroy()` (called once on shutdown).
- **Session Tracking:** Mechanism to maintain state across multiple requests. Techniques: Cookies, Hidden Form Fields, URL Rewriting, `HttpSession`.

### JSP (JavaServer Pages)
A technology to create dynamic web pages using HTML interspersed with Java code. JSPs are translated into Servlets at runtime.
- **Directives:** `<%@ ... %>` (page, include, taglib)
- **Scriptlets:** `<% ... %>` (Java code)
- **Expressions:** `<%= ... %>` (Evaluates and outputs to client)
- **Declarations:** `<%! ... %>` (Declares class-level variables/methods)
- **Implicit Objects:** `request`, `response`, `out`, `session`, `application`, `config`, `pageContext`, `page`, `exception`.

---

## 5. Spring Boot

Spring Boot makes it easy to create stand-alone, production-grade Spring-based applications that you can "just run". It eliminates boilerplate configuration.

- **`@SpringBootApplication`:** A convenience annotation that adds:
  - `@Configuration`: Tags class as a source of bean definitions.
  - `@EnableAutoConfiguration`: Tells Spring Boot to start adding beans based on classpath settings.
  - `@ComponentScan`: Tells Spring to look for other components, configurations, and services in the specified package.
- **MVC Architecture:**
  - **Model:** Data and business logic (Entities, Repositories).
  - **View:** UI (Thymeleaf, React/Angular if acting as REST API).
  - **Controller:** Handles requests, processes them via Services, and returns response (`@RestController`, `@GetMapping`, `@PostMapping`).
- **Spring Data JPA:** Simplifies data access layer. You just create an interface extending `JpaRepository` to get full CRUD operations without writing SQL.

---

[[02-Semester-VI/CS-351-MJ-T-Advanced-Java/Interview-Prep|Interview Prep]] | [[02-Semester-VI/CS-351-MJ-T-Advanced-Java/Unit-1|Unit 1]]
