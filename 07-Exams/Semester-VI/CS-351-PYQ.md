---
title: "CS-351 Advanced Java - Expected PYQ"
subject: CS-351
paper: Advanced Java
semester: VI
tags:
  - pyq
  - advanced-java
  - collections
  - multithreading
  - jdbc
  - servlets
  - jsp
  - hibernate
  - spring
  - semester-vi
  - exam
aliases:
  - Advanced Java PYQ
  - CS351 Questions
created: 2026-06-16
type: pyq
---

#  CS-351 Advanced Java - Expected PYQ

> [!important] Exam Strategy
> Advanced Java is broad. Focus on Collections (List/Set/Map), Multithreading (lifecycle, synchronization), JDBC steps, and Servlets/JSP. Hibernate and Spring are theory-heavy - know annotations.

---

## ️ Unit-wise Distribution

| Unit | Topic | Weightage |
|------|-------|-----------|
| I | Collections Framework | 20% |
| II | Multithreading | 20% |
| III | JDBC | 20% |
| IV | Servlets & JSP | 25% |
| V | Hibernate & Spring | 15% |

---

## ️ Section A - Short Answer (2 Marks)

1. **What is the Java Collections Framework? Name the main interfaces.**
2. **Difference between ArrayList and LinkedList.**
3. **Difference between HashSet, TreeSet, and LinkedHashSet.**
4. **What is the difference between HashMap and Hashtable?**
5. **What is an Iterator? How does it differ from ListIterator?**
6. **What is a thread? How is it different from a process?**
7. **List the five states of a thread lifecycle.**
8. **What is synchronization? Why is it needed?**
9. **What is the difference between `wait()`, `notify()`, and `notifyAll()`?**
10. **What is a daemon thread?**
11. **What is JDBC? List the steps to connect to a database.**
12. **Difference between Statement, PreparedStatement, and CallableStatement.**
13. **What is a ResultSet? What are its types?**
14. **What is a Servlet? How does the Servlet lifecycle work?**
15. **Difference between `doGet()` and `doPost()` in Servlet.**
16. **What is JSP? What are JSP directives?**
17. **What are JSP implicit objects? Name any five.**
18. **What is ORM? What is Hibernate?**
19. **What is the Spring Framework? Name its core modules.**
20. **What is Dependency Injection? What are its types?**

---

##  Section B - Long Answer (5–7 Marks)

---

### Q1. Java Collections - List, Set, Map with Code ()

```java
import java.util.*;

public class CollectionsDemo {
  public static void main(String[] args) {
    // ArrayList
    List<String> list = new ArrayList<>();
    list.add("Java"); list.add("Python"); list.add("Java");
    System.out.println("ArrayList: " + list);

    // HashSet (no duplicates)
    Set<String> set = new HashSet<>(list);
    System.out.println("HashSet: " + set);

    // TreeSet (sorted)
    Set<String> treeSet = new TreeSet<>(list);
    System.out.println("TreeSet: " + treeSet);

    // HashMap
    Map<String, Integer> map = new HashMap<>();
    map.put("Alice", 90); map.put("Bob", 85); map.put("Charlie", 92);
    for (Map.Entry<String, Integer> e : map.entrySet()) {
      System.out.println(e.getKey() + " → " + e.getValue());
    }

    // Iterator
    Iterator<String> it = list.iterator();
    while (it.hasNext()) System.out.print(it.next() + " ");
  }
}
```

**Collections Hierarchy:**
```
Collection
├── List        → ArrayList, LinkedList, Vector
├── Set         → HashSet, TreeSet, LinkedHashSet
└── Queue       → PriorityQueue, LinkedList

Map (separate)  → HashMap, TreeMap, LinkedHashMap, Hashtable
```

---

### Q2. Multithreading - Thread Lifecycle + Synchronization ()

**Thread Lifecycle:**
```
New → Runnable → Running → (Blocked/Waiting/Timed Waiting) → Dead
```

**Creating Threads:**
```java
// Method 1: Extending Thread
class MyThread extends Thread {
  public void run() {
    for (int i = 1; i <= 5; i++)
      System.out.println(getName() + ": " + i);
  }
}

// Method 2: Implementing Runnable (preferred)
class Task implements Runnable {
  public void run() {
    System.out.println(Thread.currentThread().getName() + " running");
  }
}

// Main
MyThread t1 = new MyThread();
t1.setName("Thread-1");
t1.start();

Thread t2 = new Thread(new Task(), "Thread-2");
t2.start();
```

**Synchronization:**
```java
class BankAccount {
  private int balance = 1000;

  public synchronized void withdraw(int amount) {
    if (balance >= amount) {
      System.out.println(Thread.currentThread().getName() + " withdrawing: " + amount);
      balance -= amount;
      System.out.println("Remaining balance: " + balance);
    } else {
      System.out.println("Insufficient funds!");
    }
  }
}
```

**Inter-thread Communication:**
```java
class Buffer {
  int item; boolean available = false;

  synchronized void produce(int val) {
    while (available) try { wait(); } catch(Exception e) {}
    item = val; available = true;
    System.out.println("Produced: " + val);
    notifyAll();
  }

  synchronized int consume() {
    while (!available) try { wait(); } catch(Exception e) {}
    available = false;
    notifyAll();
    return item;
  }
}
```

---

### Q3. JDBC - Connect, Query, and Update Database ()

**6 Steps of JDBC:**
1. Load driver: `Class.forName("com.mysql.cj.jdbc.Driver")`
2. Establish connection: `DriverManager.getConnection(url, user, pwd)`
3. Create Statement
4. Execute query
5. Process ResultSet
6. Close connection

```java
import java.sql.*;

public class JDBCDemo {
  public static void main(String[] args) throws Exception {
    // Step 1: Load driver
    Class.forName("com.mysql.cj.jdbc.Driver");

    // Step 2: Connection
    String url = "jdbc:mysql://localhost:3306/college";
    Connection con = DriverManager.getConnection(url, "root", "password");

    // Step 3 & 4: PreparedStatement (INSERT)
    PreparedStatement ps = con.prepareStatement(
      "INSERT INTO students VALUES (?, ?, ?)");
    ps.setInt(1, 101);
    ps.setString(2, "Amit");
    ps.setDouble(3, 8.5);
    ps.executeUpdate();

    // Step 3 & 4: Statement (SELECT)
    Statement stmt = con.createStatement();
    ResultSet rs = stmt.executeQuery("SELECT * FROM students");

    // Step 5: Process ResultSet
    while (rs.next()) {
      System.out.println(rs.getInt(1) + " | " + rs.getString(2));
    }

    // Step 6: Close
    rs.close(); stmt.close(); con.close();
    System.out.println("Done!");
  }
}
```

**Statement vs PreparedStatement vs CallableStatement:**

| Feature | Statement | PreparedStatement | CallableStatement |
|---------|-----------|------------------|-------------------|
| Query | Static SQL | Parameterized SQL | Stored procedures |
| Performance | Slower | Faster (precompiled) | Fastest |
| SQL Injection | Vulnerable | Safe | Safe |

---

### Q4. Servlet - Lifecycle + Request/Response ()

**Servlet Lifecycle:**
1. `init()` - called once when servlet loaded
2. `service()` - called for each request (calls doGet/doPost)
3. `destroy()` - called when servlet removed

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
  public void init() { System.out.println("Servlet initialized"); }

  protected void doGet(HttpServletRequest req, HttpServletResponse res)
      throws IOException {
    res.setContentType("text/html");
    PrintWriter out = res.getWriter();
    String name = req.getParameter("name");
    out.println("<h1>Hello, " + name + "!</h1>");
    out.close();
  }

  protected void doPost(HttpServletRequest req, HttpServletResponse res)
      throws IOException {
    doGet(req, res); // delegate to doGet
  }

  public void destroy() { System.out.println("Servlet destroyed"); }
}
```

**Session Management:**
```java
// Create/get session
HttpSession session = req.getSession(true);
session.setAttribute("user", "Amit");
String user = (String) session.getAttribute("user");
session.invalidate(); // logout
```

---

### Q5. JSP - Directives, Scriptlets, Implicit Objects ()

```jsp
<%-- JSP Page Directive --%>
<%@ page language="java" contentType="text/html; charset=UTF-8" %>
<%@ page import="java.util.*" %>

<%-- Include Directive --%>
<%@ include file="header.jsp" %>

<%-- Taglib Directive --%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<html><body>
  <%-- Declaration --%>
  <%! int count = 0; %>

  <%-- Scriptlet --%>
  <% count++; String user = request.getParameter("name"); %>

  <%-- Expression --%>
  <h2>Hello, <%= user %>!</h2>
  <p>Visit count: <%= count %></p>

  <%-- JSTL --%>
  <c:if test="${count > 5}">
    <p>Visited more than 5 times!</p>
  </c:if>
</body></html>
```

**JSP Implicit Objects:**

| Object | Type | Purpose |
|--------|------|---------|
| `request` | HttpServletRequest | Client request |
| `response` | HttpServletResponse | Server response |
| `session` | HttpSession | User session |
| `application` | ServletContext | Application scope |
| `out` | JspWriter | Output stream |
| `config` | ServletConfig | Servlet configuration |
| `pageContext` | PageContext | Page-level context |

---

### Q6. Hibernate ORM ()

**Hibernate Configuration:**
```java
// Entity class
@Entity
@Table(name = "students")
public class Student {
  @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
  private int id;

  @Column(name = "name")
  private String name;

  @Column(name = "cgpa")
  private double cgpa;

  // getters & setters
}

// CRUD operations
SessionFactory sf = new Configuration().configure().buildSessionFactory();
Session session = sf.openSession();
Transaction tx = session.beginTransaction();

// Save
Student s = new Student(0, "Amit", 8.5);
session.save(s);

// Read
Student found = session.get(Student.class, 1);

// Update
found.setName("Amit Kumar");
session.update(found);

// Delete
session.delete(found);

tx.commit();
session.close();
```

---

### Q7. Spring Framework - IoC & Dependency Injection ()

```java
// Spring Bean
@Component
public class Engine {
  public void start() { System.out.println("Engine started!"); }
}

// Dependency Injection (Constructor Injection)
@Component
public class Car {
  private Engine engine;

  @Autowired
  public Car(Engine engine) { this.engine = engine; }

  public void drive() {
    engine.start();
    System.out.println("Car is moving!");
  }
}

// Spring Boot Main
@SpringBootApplication
public class App {
  public static void main(String[] args) {
    ApplicationContext ctx = SpringApplication.run(App.class, args);
    Car car = ctx.getBean(Car.class);
    car.drive();
  }
}
```

**Spring Annotations:**

| Annotation | Purpose |
|------------|---------|
| `@Component` | Generic Spring bean |
| `@Service` | Business logic layer |
| `@Repository` | Data access layer |
| `@Controller` | MVC controller |
| `@Autowired` | Auto dependency injection |
| `@Bean` | Define bean in @Configuration class |

---

##  Most Expected Questions

> [!tip] High Probability
> 1.  ArrayList vs LinkedList vs Vector comparison
> 2.  Thread lifecycle diagram + synchronization code
> 3.  JDBC complete program with PreparedStatement
> 4.  Servlet lifecycle + doGet/doPost program
> 5.  JSP implicit objects table
> 6.  HashMap iteration with entrySet()
> 7.  Producer-Consumer with wait/notify

---

*Tags: CS-351 Advanced Java | Semester VI | [[07-Exams]]*
