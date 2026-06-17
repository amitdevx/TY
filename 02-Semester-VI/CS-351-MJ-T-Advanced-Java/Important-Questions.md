---
title: "Advanced Java - Important Questions"
subject: "CS-351-MJ-T"
semester: VI
type: important-questions
tags:
  - advanced-java
  - exam-prep
  - important-questions
  - semester-vi
aliases:
  - "AJ IQ"
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-351-MJ-T - Important Questions

> [!warning] Exam Focus
> These questions are frequently asked in university examinations. Questions marked  are highly likely. Practice all code-based questions by writing actual programs.

## Unit 1 - Collections Framework

### 2-Mark Questions
1. What is the Java Collections Framework?
2. What is the difference between `List` and `Set`?
3. What does `Iterator` do? Name its three methods.
4. What is a `Comparator`? How is it different from `Comparable`?
5. What is Generics in Java?

### 5-Mark Questions
6.  Explain `ArrayList` vs `LinkedList` with a comparison table.
7.  Write a program to sort a list of `Student` objects by marks using `Comparator`.
8. Explain `HashMap`, `TreeMap`, and `LinkedHashMap` with differences.
9. Write a program demonstrating `HashSet`, `TreeSet`, and `LinkedHashSet`.
10.  What are generics? Write a generic method to find maximum in an array.

### 10-Mark Questions
11.  Explain the entire Java Collections Framework hierarchy with a diagram. Discuss ArrayList, LinkedList, HashSet, TreeSet, HashMap, TreeMap in detail.
12. Write a Java program that demonstrates `Comparable` for natural sorting and `Comparator` for custom sorting of `Employee` objects.

---

## Unit 2 - Multithreading

### 2-Mark Questions
1. What is a thread? How is it different from a process?
2. Name all states of a thread's lifecycle.
3. What is `synchronized` keyword used for?
4. What is `volatile` keyword in Java?
5. What causes a deadlock?

### 5-Mark Questions
6.  Write a Java program to create threads using `Thread` class and `Runnable` interface.
7.  Explain thread lifecycle with a state diagram.
8.  Write a Producer-Consumer program using `wait()` and `notify()`.
9. What is `ExecutorService`? Write a program using `Executors.newFixedThreadPool()`.
10.  What is deadlock? State the four Coffman conditions and write a deadlock example.

### 10-Mark Questions
11.  Explain all aspects of Java Multithreading: thread creation, lifecycle, priorities, synchronization, wait/notify, thread pools, volatile, and deadlock prevention.
12. Write a complete multi-threaded bank account simulation with proper synchronization.

---

## Unit 3 - JDBC

### 2-Mark Questions
1. What is JDBC? What does it stand for?
2. Name the four types of JDBC drivers.
3. What is `PreparedStatement`? Why is it preferred over `Statement`?
4. What is SQL injection?
5. What is connection pooling?

### 5-Mark Questions
6.  Explain JDBC architecture with a diagram.
7.  Write a complete JDBC program to perform CRUD operations on a `Student` table.
8.  What is the difference between `Statement`, `PreparedStatement`, and `CallableStatement`?
9. Explain transaction management in JDBC with commit and rollback example.
10. What is a `ResultSet`? Explain different types of ResultSet.

### 10-Mark Questions
11.  Write a complete JDBC program demonstrating connection, PreparedStatement, ResultSet, and transaction management with rollback on failure.
12. Explain connection pooling. Why is it needed? Compare HikariCP and Apache DBCP.

---

## Unit 4 - Servlet & JSP

### 2-Mark Questions
1. What is a Servlet? Where does it run?
2. Name the three methods in the Servlet lifecycle.
3. What is session tracking?
4. What are JSP implicit objects?
5. What is JSTL?

### 5-Mark Questions
6.  Explain the Servlet lifecycle with a diagram. What happens during `init()`, `service()`, and `destroy()`?
7.  Write a Login Servlet that validates username/password and uses `HttpSession`.
8.  Compare the four session tracking techniques: Cookies, HttpSession, URL Rewriting, Hidden Fields.
9. What are JSP directives? Explain `page`, `include`, and `taglib` directives with examples.
10.  Write a JSP page using JSTL `c:forEach` to display a list of products from a request attribute.

### 10-Mark Questions
11.  Explain Servlet and JSP together: Servlet lifecycle, HttpServletRequest/Response, session management, JSP lifecycle, and JSTL.
12. Build a complete Servlet-JSP login application with session tracking and logout functionality.

---

## Unit 5 - Hibernate / Spring

### 2-Mark Questions
1. What is ORM?
2. What is the impedance mismatch problem?
3. What is `SessionFactory` in Hibernate?
4. What is `@SpringBootApplication`?
5. What is IoC (Inversion of Control)?

### 5-Mark Questions
6.  Explain Hibernate architecture with diagram. What are SessionFactory, Session, and Transaction?
7.  Write a Hibernate entity class and demonstrate CRUD operations.
8.  Explain Spring IoC and Dependency Injection with the three types (constructor, setter, field).
9.  Write a complete Spring Boot REST API for a `Product` entity (GET, POST, PUT, DELETE).
10. What is HQL? How is it different from SQL? Write 3 HQL queries.

### 10-Mark Questions
11.  Explain Spring Boot from `@SpringBootApplication` to a running REST API. Include entity, repository, service, and controller layers.
12. Compare Hibernate ORM with plain JDBC. What advantages does Hibernate provide?

---

## Previous Year Pattern

```
Section A: 10 × 2 marks = 20 marks (one from each unit × 2)
Section B: 5 × 5 marks = 25 marks (one per unit)
Section C: 2 × 10 marks = 20 marks (choice from 2 questions per 2-unit group)
Optional: 15 marks
```

## Most Important Topics

1. **Collections**: ArrayList vs LinkedList, HashMap vs TreeMap, Comparable vs Comparator, Generics
2. **Multithreading**: Thread lifecycle, synchronized/wait/notify, deadlock, ExecutorService
3. **JDBC**: Architecture, PreparedStatement, Transactions, Connection Pooling
4. **Servlet**: Lifecycle, Session tracking (HttpSession), JSP implicit objects, JSTL
5. **Spring Boot**: REST API with `@RestController`, Hibernate Entity with JpaRepository

---
*CS-351-MJ-T Advanced Java | Important Questions | Semester VI*
