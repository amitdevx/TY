---
title: "CS-351 Advanced Java Interview Preparation"
tags: [cs-351, advanced-java, java, interview, semester-vi]
subject_code: CS-351-MJ-T
type: interview-prep
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Advanced Java Interview Preparation

> [!summary] About
> Top 20+ Advanced Java interview questions covering Collections, Multithreading, JDBC, Servlets, and Spring Boot. Crucial for backend and full-stack developer roles.

---

## 1. Collections Framework

> [!question] 1. What is the difference between ArrayList and LinkedList?
> - **ArrayList:** Uses a dynamic array under the hood. Best for scenarios with frequent read operations (O(1) access time). Insertion/deletion in the middle is slow because elements must be shifted.
> - **LinkedList:** Uses a doubly-linked list. Best for scenarios with frequent insertions and deletions (O(1) if node reference is known). Read operations are slow (O(n)) because it requires traversal.

> [!question] 2. How does a HashMap work internally?
> A HashMap stores elements as Key-Value pairs using an array of Nodes (or linked lists). 
> 1. When `put(key, value)` is called, it calculates the hash code of the key.
> 2. The hash code determines the index (bucket) in the array.
> 3. If multiple keys hash to the same bucket (collision), they are stored in a Linked List (or a Red-Black Tree in Java 8+ if the list gets too long).
> 4. `get(key)` calculates the hash to find the bucket, then uses `.equals()` to find the exact key in the list/tree.

> [!question] 3. Difference between HashSet and TreeSet?
> - **HashSet:** Backed by a HashMap. Does not guarantee any order of elements. Allows one `null` value. Faster operations (O(1)).
> - **TreeSet:** Backed by a TreeMap (NavigableMap). Elements are sorted in ascending/natural order (or by a provided Comparator). Does not allow `null` values. Slower operations (O(log n)).

> [!question] 4. Difference between Iterator and ListIterator?
> - **Iterator:** Can traverse elements only in the forward direction. Can be used for any Collection (List, Set, Queue).
> - **ListIterator:** Can traverse elements in both forward and backward directions. Has extra methods like `add()`, `hasPrevious()`, `previous()`. Can only be used for Lists.

---

## 2. Multithreading

> [!question] 5. Difference between extending Thread vs implementing Runnable?
> Implementing `Runnable` is highly preferred because:
> 1. Java does not support multiple class inheritance. If you extend `Thread`, your class cannot extend any other class. If you implement `Runnable`, you can still extend another class.
> 2. Implementing `Runnable` separates the task (code to run) from the thread (execution mechanism).

> [!question] 6. Explain `wait()`, `notify()`, and `notifyAll()`.
> These methods are used for inter-thread communication and belong to the `Object` class (not `Thread`).
> - `wait()`: Causes the current thread to release the lock on the object and wait until another thread calls `notify()`.
> - `notify()`: Wakes up a single thread that is waiting on this object's monitor.
> - `notifyAll()`: Wakes up all threads that are waiting on this object's monitor.

> [!question] 7. What is a Deadlock and how can it be prevented?
> Deadlock occurs when two or more threads are blocked forever, waiting for each other to release locks.
> **Prevention:** Avoid nested locks, lock objects in a consistent order across all threads, or use a timeout when attempting to acquire locks (e.g., `tryLock()` in `java.util.concurrent.locks`).

---

## 3. JDBC

> [!question] 8. Statement vs PreparedStatement?
> - **Statement:** Used for executing static SQL queries. The query is compiled every time it runs. Vulnerable to SQL injection.
> - **PreparedStatement:** Extends Statement. Used for executing parameterized SQL queries (`?`). The query is pre-compiled by the database, making it faster for repeated executions. **Prevents SQL injection attacks.**

> [!question] 9. What is the difference between `execute()`, `executeQuery()`, and `executeUpdate()`?
> - `executeQuery()`: Used for `SELECT` statements. Returns a `ResultSet`.
> - `executeUpdate()`: Used for `INSERT`, `UPDATE`, `DELETE` statements. Returns an integer representing the number of rows affected.
> - `execute()`: Can be used for any SQL statement. Returns a boolean (true if it returned a ResultSet, false if it returned an update count).

---

## 4. Servlets and JSP

> [!question] 10. Explain the Lifecycle of a Servlet.
> 1. **Class Loading & Instantiation:** Container loads the servlet class and creates an instance.
> 2. **Initialization:** Container calls `init(ServletConfig)` once. Used for setup.
> 3. **Request Handling:** Container calls the `service(ServletRequest, ServletResponse)` method for every client request. It dispatches to `doGet`, `doPost`, etc.
> 4. **Destruction:** Container calls `destroy()` once before removing the servlet instance. Used to clean up resources.

> [!question] 11. Difference between `sendRedirect()` and `forward()`?
> - **`sendRedirect()` (response method):** Sends a status code (302) to the client's browser, telling it to make a completely new request to a new URL. The URL changes in the browser. State/request attributes are lost.
> - **`RequestDispatcher.forward()` (request method):** The request is transferred to another resource on the *same server\* internally. The browser URL does not change. Request attributes are preserved.

> [!question] 12. What are implicit objects in JSP?
> Objects automatically created by the Web Container that you can use in scriptlets/expressions without explicitly declaring them.
> Examples: `request`, `response`, `out`, `session`, `application`, `config`, `pageContext`, `page`, `exception`.

---

## 5. Spring Boot

> [!question] 13. What is Dependency Injection (DI) and Inversion of Control (IoC)?
> - **IoC:** A design principle where the control flow of a program is inverted. Instead of the programmer calling libraries, the framework (Spring) controls the program flow and object creation.
> - **DI:** A specific implementation of IoC where an object receives its dependencies from an external source (the Spring IoC Container) rather than creating them itself using the `new` keyword.

> [!question] 14. What is `@SpringBootApplication`?
> A meta-annotation that combines three annotations:
> 1. `@Configuration`: Marks the class as a source of bean definitions.
> 2. `@EnableAutoConfiguration`: Tells Spring Boot to automatically configure beans based on classpath dependencies.
> 3. `@ComponentScan`: Tells Spring to scan the current package and sub-packages for other components/beans.

> [!question] 15. Difference between `@Controller` and `@RestController`?
> - `@Controller`: Used to create web controllers returning Views (HTML pages). Requires `@ResponseBody` on methods if returning raw data.
> - `@RestController`: A combination of `@Controller` and `@ResponseBody`. Used to create REST APIs. Every method automatically serializes the return object to JSON/XML and writes it directly to the HTTP response body.

---

[[02-Semester-VI/CS-351-MJ-T-Advanced-Java/Revision|Revision Summary]] | [[02-Semester-VI/CS-351-MJ-T-Advanced-Java/Unit-1|Unit 1]]
