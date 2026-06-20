---
title: "Advanced Java - Unit 5: Spring Framework & Data JPA"
subject: "CS-351-MJ-T"
unit: 5
semester: VI
type: unit-note
tags:
  - advanced-java
  - hibernate
  - spring
  - spring-boot
  - rest-api
  - orm
  - java
  - semester-vi
aliases:
  - "AJ Unit 5"
  - "Hibernate Spring"
created: 2026-06-16
updated: 2026-06-16
hours: 6
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# Unit 5 - Hibernate / Spring Basics

> [!important] Industry-Critical Unit
> Spring Boot + Hibernate is the most widely used Java enterprise stack. Virtually every Java backend role requires knowledge of Spring MVC, Spring Boot REST APIs, and Hibernate ORM.

## Learning Objectives

- [ ] Explain ORM and the impedance mismatch problem
- [ ] Describe Hibernate architecture with SessionFactory and Session
- [ ] Write HQL queries and use Hibernate for CRUD
- [ ] Understand Spring IoC and Dependency Injection
- [ ] Explain Spring MVC request flow
- [ ] Build a REST API using Spring Boot

---

## 5.1 ORM - Object-Relational Mapping

==ORM (Object-Relational Mapping)== is a technique that maps Java objects to relational database tables, eliminating the need for manual SQL.

### The Impedance Mismatch Problem

| Aspect | Java (OOP) | Relational DB | Mismatch |
|--------|-----------|---------------|----------|
| Data unit | Object | Row | Object has methods; rows don't |
| Relationships | References | Foreign keys | Different navigation |
| Inheritance | Class hierarchy | No direct support | Must simulate |
| Identity | Object reference | Primary key | Two concepts |

### Without ORM (JDBC - lots of boilerplate)

```java
String sql = "SELECT id, name, email FROM users WHERE id = ?";
PreparedStatement ps = conn.prepareStatement(sql);
ps.setInt(1, userId);
ResultSet rs = ps.executeQuery();
if (rs.next()) {
    User user = new User();
    user.setId(rs.getInt("id"));
    user.setName(rs.getString("name"));
    user.setEmail(rs.getString("email"));
    return user;
}
// Lots of boilerplate!
```

### With ORM (Hibernate - clean)

```java
User user = session.get(User.class, userId);  // Done! No SQL, no mapping!
```

---

## 5.2 Spring Framework Modules
The Spring Framework consists of several modules organized into different layers:
- **Core Container:** Beans, Core, Context, SpEL (Spring Expression Language). Provides IoC and DI.
- **Data Access / Integration:** JDBC, ORM, OXM, JMS, Transaction. Handles database interactions.
- **Web:** Web, Web-Servlet (Spring MVC), Web-Socket. Supports web application creation.
- **AOP & Instrumentation:** Aspect-Oriented Programming support.
- **Test:** Supports unit and integration testing with JUnit and TestNG.

## 5.3 Spring Boot with Database and Data JPA
Spring Data JPA significantly reduces boilerplate code required to implement data access layers. It abstracts away raw Hibernate and JPA configurations.

### Key Concepts
- **Entity:** A Java class mapped to a database table using `@Entity`.
- **Repository Interface:** An interface extending `JpaRepository` or `CrudRepository` which provides built-in CRUD operations.

### Implementation Steps
**1. Entity Class:**
```java
@Entity
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private double salary;
    // Getters and setters
}
```

**2. Repository Interface:**
```java
public interface EmployeeRepository extends JpaRepository<Employee, Long> {
    // Custom query methods can be defined here
    List<Employee> findByName(String name);
}
```

**3. Service / Controller Integration:**
```java
@RestController
@RequestMapping("/api/employees")
public class EmployeeController {
    @Autowired
    private EmployeeRepository repo;
    
    @GetMapping
    public List<Employee> getAll() {
        return repo.findAll();
    }
}
```

## 5.4 Spring IoC / Dependency Injection

### Inversion of Control (IoC)

==IoC== is a design principle where the **framework controls object creation and lifecycle**, instead of the application code.

```
Without IoC:
  Class A creates object of B → A depends on and controls B

With IoC (Spring):
  Spring creates both A and B → Spring injects B into A
  A doesn't know how B is created → loose coupling
```

### Dependency Injection Types

```java
// 1. CONSTRUCTOR INJECTION (Preferred)
@Service
public class OrderService {
    private final ProductRepository productRepo;
    private final EmailService emailService;
    
    // Spring automatically injects these when creating OrderService
    @Autowired  // Optional if only one constructor
    public OrderService(ProductRepository productRepo, EmailService emailService) {
        this.productRepo = productRepo;
        this.emailService = emailService;
    }
}

// 2. SETTER INJECTION
@Service
public class ReportService {
    private DataService dataService;
    
    @Autowired
    public void setDataService(DataService dataService) {
        this.dataService = dataService;
    }
}

// 3. FIELD INJECTION (Convenient but less testable)
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private EmailService emailService;
}
```

### Spring Annotations

| Annotation | Purpose |
|------------|---------|
| `@Component` | Generic Spring bean |
| `@Service` | Business layer bean |
| `@Repository` | Data access layer bean |
| `@Controller` | Web layer (MVC) bean |
| `@RestController` | REST API controller |
| `@Autowired` | Inject dependency |
| `@Bean` | Declare bean in `@Configuration` class |
| `@Configuration` | Class providing Spring configuration |

---

## 5.6 Spring MVC Basics

### Spring MVC Request Flow

```mermaid
sequenceDiagram
  participant Client
  participant DS
  participant HM
  participant C
  participant VR
  participant View

  Client->>DS: HTTP Request
  DS->>HM: Find handler for<br/>/users
  HM->>DS: HandlerMethod<br/>(UserController.getUsers())
  DS->>C: Execute getUsers()
  C->>DS: ModelAndView ("users",<br/>model)
  DS->>VR: Resolve view<br/>"users"
  VR->>DS: users.jsp
  DS->>View: Render with model
  View->>Client: HTML Response
```

---

## 5.7 Spring Boot Introduction

==Spring Boot== simplifies Spring configuration with **auto-configuration, embedded server, and starter dependencies**.

### Spring Boot vs Spring MVC

| Feature | Spring MVC | Spring Boot |
|---------|-----------|-------------|
| Configuration | XML or Java config | **Auto-configured**  |
| Server | Deploy to Tomcat | **Embedded Tomcat**  |
| Dependencies | Manual | **Starter POMs**  |
| Setup time | Hours | **Minutes**  |

### Spring Boot Project Structure

```
spring-boot-app/
├── src/main/java/com/example/
│   ├── SpringBootAppApplication.java  ← Main class
│   ├── controller/
│   │   └── StudentController.java
│   ├── service/
│   │   └── StudentService.java
│   ├── repository/
│   │   └── StudentRepository.java
│   └── entity/
│       └── Student.java
├── src/main/resources/
│   ├── application.properties
│   └── static/
└── pom.xml
```

### Spring Boot Main Class

```java
@SpringBootApplication  // = @Configuration + @ComponentScan + @EnableAutoConfiguration
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

---

## 5.8 REST API with Spring Boot

```java
// Entity
@Entity
@Table(name = "students")
public class Student {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;
    private double marks;
    // Constructors, getters, setters
}

// Repository - Spring Data JPA
public interface StudentRepository extends JpaRepository<Student, Long> {
    List<Student> findByName(String name);
    List<Student> findByMarksGreaterThan(double marks);
    Optional<Student> findByEmail(String email);
}

// Service
@Service
public class StudentService {
    @Autowired
    private StudentRepository studentRepository;
    
    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }
    
    public Optional<Student> getById(Long id) {
        return studentRepository.findById(id);
    }
    
    public Student create(Student student) {
        return studentRepository.save(student);
    }
    
    public Student update(Long id, Student details) {
        Student student = studentRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Student not found: " + id));
        student.setName(details.getName());
        student.setEmail(details.getEmail());
        student.setMarks(details.getMarks());
        return studentRepository.save(student);
    }
    
    public void delete(Long id) {
        studentRepository.deleteById(id);
    }
}

// REST Controller
@RestController
@RequestMapping("/api/students")
public class StudentController {
    
    @Autowired
    private StudentService studentService;
    
    // GET all students
    @GetMapping
    public ResponseEntity<List<Student>> getAllStudents() {
        return ResponseEntity.ok(studentService.getAllStudents());
    }
    
    // GET student by ID
    @GetMapping("/{id}")
    public ResponseEntity<Student> getStudentById(@PathVariable Long id) {
        return studentService.getById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    // POST - create student
    @PostMapping
    public ResponseEntity<Student> createStudent(@RequestBody Student student) {
        Student saved = studentService.create(student);
        return ResponseEntity.status(HttpStatus.CREATED).body(saved);
    }
    
    // PUT - update student
    @PutMapping("/{id}")
    public ResponseEntity<Student> updateStudent(
            @PathVariable Long id, 
            @RequestBody Student details) {
        try {
            Student updated = studentService.update(id, details);
            return ResponseEntity.ok(updated);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }
    
    // DELETE student
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteStudent(@PathVariable Long id) {
        studentService.delete(id);
        return ResponseEntity.noContent().build();
    }
    
    // Query params example
    @GetMapping("/search")
    public ResponseEntity<List<Student>> searchStudents(
            @RequestParam(required = false) String name,
            @RequestParam(required = false, defaultValue = "0") double minMarks) {
        List<Student> results = studentService.getAllStudents()
            .stream()
            .filter(s -> name == null || s.getName().contains(name))
            .filter(s -> s.getMarks() >= minMarks)
            .collect(java.util.stream.Collectors.toList());
        return ResponseEntity.ok(results);
    }
}
```

### application.properties (Spring Boot Config)

```properties
# Database
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=password
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# JPA / Hibernate
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect

# Server
server.port=8080
server.servlet.context-path=/api

# App name
spring.application.name=student-api
```

### REST HTTP Methods Convention

| HTTP Method | Endpoint | Action | Status Code |
|-------------|----------|--------|-------------|
| `GET` | `/students` | Get all | 200 OK |
| `GET` | `/students/{id}` | Get one | 200 / 404 |
| `POST` | `/students` | Create | 201 Created |
| `PUT` | `/students/{id}` | Full update | 200 OK |
| `PATCH` | `/students/{id}` | Partial update | 200 OK |
| `DELETE` | `/students/{id}` | Delete | 204 No Content |

---

## Key Terms Summary

| Term | Definition |
|------|------------|
| ==ORM== | Maps Java objects to DB tables - eliminates manual SQL |
| ==Hibernate== | Popular Java ORM framework |
| ==SessionFactory== | Thread-safe factory for creating Sessions |
| ==Session== | Single DB work unit - not thread-safe |
| ==HQL== | Hibernate Query Language - object-oriented SQL |
| ==IoC== | Inversion of Control - framework controls object lifecycle |
| ==DI== | Dependency Injection - objects receive dependencies externally |
| ==Spring Boot== | Opinionated Spring with auto-configuration |
| ==`@RestController`== | Spring annotation for REST API controllers |
| ==`@Autowired`== | Inject Spring bean dependency |
| ==`JpaRepository`== | Spring Data interface with built-in CRUD methods |

---

## Practice Questions

1. What is ORM? What problem does it solve (impedance mismatch)?
2. Explain Hibernate architecture with SessionFactory and Session.
3. Write Hibernate entity class for a `Product` with id, name, price, category.
4. What are the differences between `session.save()`, `session.persist()`, `session.update()`, and `session.merge()`?
5. What is HQL? How is it different from SQL? Write 3 HQL queries.
6. What is Spring IoC? Explain the concept with a diagram.
7. What is Dependency Injection? Explain its three types with code examples.
8. What is Spring Boot? How does it differ from Spring MVC?
9. Build a complete REST CRUD API for a `Student` entity using Spring Boot.
10. What are the common Spring annotations? Explain `@Component`, `@Service`, `@Repository`, `@Controller`, `@RestController`.

---

## Navigation

- [[Overview]] | [[Syllabus]]
- ← Previous: [[Unit-4|Unit-4 - Servlet & JSP]]
- → Next: (End)
- [[Important-Questions]] | [[Revision]] | [[Interview-Prep]]

---
*CS-351-MJ-T Advanced Java | Unit 5 | Semester VI*
