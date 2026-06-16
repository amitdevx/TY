---
title: "CS-351 Advanced Java - Important Topics"
subject: CS-351
semester: VI
tags:
  - important-topics
  - advanced-java
  - collections
  - multithreading
  - jdbc
  - servlets
  - semester-vi
  - exam
aliases:
  - Advanced Java Important
  - CS351 Must-Know
created: 2026-06-16
type: important-topics
---

#  CS-351 Advanced Java - Important Topics

> [!important] Exam Focus
> Advanced Java is broad and practical. Collections and Multithreading are foundational. JDBC programs are guaranteed. Servlet lifecycle + JSP implicit objects are easy marks.

---

##  Top 10 Most Important Topics

| # | Topic | Description | Probability |
|---|-------|-------------|-------------|
| 1 | **Collections Framework** | List/Set/Map implementations, Iterators |  |
| 2 | **Thread Lifecycle & Sync** | States, `synchronized`, `wait/notify` |  |
| 3 | **JDBC - Complete Program** | 6 steps: load driver → connect → query → close |  |
| 4 | **Servlet Lifecycle** | `init()`, `service()`, `destroy()` with code |  |
| 5 | **JSP Implicit Objects** | request, response, session, application, out |  |
| 6 | **PreparedStatement** | Parameterized SQL - safe from SQL injection |  |
| 7 | **Comparable vs Comparator** | Sorting custom objects |  |
| 8 | **Session Management** | Cookies, HttpSession, URL rewriting |  |
| 9 | **Hibernate Annotations** | @Entity, @Table, @Id, @Column, Session CRUD |  |
| 10 | **Spring IoC & DI** | @Component, @Autowired, @Bean |  |

---

##  "Definitely Going to Come" Section

> [!warning] Near-Certain Questions
> 1. **Write a Java program using Collections** - ArrayList operations + HashMap iteration
> 2. **Thread lifecycle diagram + create threads** using Thread class and Runnable interface
> 3. **Synchronization** - synchronized block/method with example
> 4. **Complete JDBC program** - connect to MySQL, insert + read using PreparedStatement
> 5. **Servlet program** - doGet/doPost with HttpServletRequest/Response
> 6. **JSP with scriptlets** - display form data, use implicit objects
> 7. **Compare: Statement vs PreparedStatement vs CallableStatement**

---

##  Must-Know Definitions

| Term | Definition |
|------|-----------|
| **Collection** | Framework providing reusable data structures (List, Set, Map) |
| **ArrayList** | Dynamic array - allows duplicates, ordered, null allowed |
| **LinkedList** | Doubly linked nodes - fast insert/delete at ends |
| **HashSet** | No duplicates, no order, allows one null |
| **HashMap** | Key-value pairs, no order, one null key |
| **Synchronization** | Prevents multiple threads accessing shared resource simultaneously |
| **Deadlock** | Two threads wait for each other's lock - neither proceeds |
| **JDBC** | Java Database Connectivity - API for connecting Java to databases |
| **PreparedStatement** | Pre-compiled SQL with placeholders (?) - prevents SQL injection |
| **Servlet** | Java class that handles HTTP requests/responses |
| **JSP** | Java Server Pages - HTML + Java scriptlets |
| **Session** | Server-side object storing user state across requests |
| **ORM** | Object-Relational Mapping - maps Java objects to DB tables |
| **DI** | Dependency Injection - object dependencies provided externally |

---

##  Quick Code Patterns

### ArrayList + HashMap
```java
List<String> list = new ArrayList<>(Arrays.asList("Java","Python","C++"));
list.add("Go"); list.remove("C++");
Collections.sort(list);

Map<String, Integer> map = new HashMap<>();
map.put("A", 90); map.put("B", 85);
for (Map.Entry<String, Integer> e : map.entrySet())
    System.out.println(e.getKey() + " = " + e.getValue());
```

### Thread Synchronization
```java
class Counter {
    int count = 0;
    synchronized void increment() { count++; }
}
// Two threads calling increment() won't corrupt count
```

### JDBC Template (6 Steps)
```java
Class.forName("com.mysql.cj.jdbc.Driver");          // 1
Connection con = DriverManager.getConnection(url,user,pwd); // 2
PreparedStatement ps = con.prepareStatement("SELECT * FROM t WHERE id=?"); // 3
ps.setInt(1, 101);                                   // Set params
ResultSet rs = ps.executeQuery();                    // 4
while(rs.next()) System.out.println(rs.getString(1)); // 5
rs.close(); ps.close(); con.close();                 // 6
```

### Servlet Template
```java
@WebServlet("/myServlet")
public class MyServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse res)
            throws IOException {
        res.setContentType("text/html");
        PrintWriter out = res.getWriter();
        out.println("<h1>Hello from Servlet!</h1>");
    }
}
```

---

##  Collections Comparison Quick Reference

| Collection | Duplicate | Order | Null | Thread-Safe |
|------------|-----------|-------|------|-------------|
| ArrayList |  | Insertion |  |  |
| LinkedList |  | Insertion |  |  |
| Vector |  | Insertion |  |  |
| HashSet |  | None | One |  |
| TreeSet |  | Sorted |  |  |
| LinkedHashSet |  | Insertion | One |  |
| HashMap | Keys:  | None | One key |  |
| Hashtable | Keys:  | None |  |  |
| TreeMap | Keys:  | Key sorted |  |  |

---

##  Common Mistakes to Avoid

> [!warning] Avoid These Errors
> - **ConcurrentModificationException:** Don't modify a collection while iterating with for-each. Use Iterator.remove() instead.
> - **Thread.sleep() vs wait():** sleep() doesn't release lock; wait() releases lock!
> - **JDBC Connection closing:** Always close in finally block or use try-with-resources.
> - **session vs application scope in JSP:** session is per-user; application is for all users.
> - **Hibernate without transaction:** Always use `tx.commit()` after DML operations.
> - **Deadlock prevention:** Always acquire locks in same order.

---

##  JSP Implicit Objects Reference

| Object | Type | Scope |
|--------|------|-------|
| `request` | HttpServletRequest | Request |
| `response` | HttpServletResponse | Page |
| `session` | HttpSession | Session |
| `application` | ServletContext | Application |
| `out` | JspWriter | Page |
| `config` | ServletConfig | Page |
| `pageContext` | PageContext | Page |
| `page` | Object (this) | Page |
| `exception` | Throwable | Page (error pages) |

---

*Tags: CS-351 Advanced Java | Semester VI | [[07-Exams]]*
