import os

base_dir = "/home/amitdevx/Downloads/TY/04-Labs/Semester-VI/CS-356-MJ-P"
assignments_dir = os.path.join(base_dir, "Assignments")
viva_dir = os.path.join(base_dir, "Viva")
os.makedirs(assignments_dir, exist_ok=True)
os.makedirs(viva_dir, exist_ok=True)

subject_code = "CS-356"

topics = [
    {
        "id": 1,
        "title": "Collections",
        "aim": "To understand and implement various collection classes such as ArrayList, HashMap, and HashSet in Java.",
        "theory": "The Java Collections Framework provides a set of interfaces and classes to store and manipulate a group of objects. Key interfaces include List (ordered collection), Set (unordered collection without duplicates), and Map (key-value pairs). Implementations include `ArrayList`, `LinkedList`, `HashSet`, `TreeSet`, `HashMap`, and `TreeMap`.",
        "code": """```java
import java.util.*;

public class CollectionsDemo {
    public static void main(String[] args) {
        // List Example
        List<String> list = new ArrayList<>();
        list.add("Java");
        list.add("Python");
        list.add("C++");
        System.out.println("ArrayList: " + list);

        // Set Example
        Set<Integer> set = new HashSet<>();
        set.add(10);
        set.add(20);
        set.add(10); // Duplicate ignored
        System.out.println("HashSet: " + set);

        // Map Example
        Map<String, Integer> map = new HashMap<>();
        map.put("Alice", 90);
        map.put("Bob", 85);
        System.out.println("HashMap: " + map);
    }
}
```""",
        "output": """```
ArrayList: [Java, Python, C++]
HashSet: [20, 10]
HashMap: {Bob=85, Alice=90}
```""",
        "viva_questions": [
            "What is the difference between ArrayList and LinkedList?",
            "How does a HashSet internally store elements?",
            "What is the difference between HashMap and HashTable?",
            "Explain the concept of Iterator and ListIterator.",
            "Why Map interface does not extend the Collection interface?",
            "What are the benefits of using generics with collections?"
        ]
    },
    {
        "id": 2,
        "title": "Multithreading",
        "aim": "To learn and implement multithreading in Java using Thread class and Runnable interface.",
        "theory": "Multithreading is a process of executing multiple threads simultaneously. A thread is a lightweight sub-process, the smallest unit of processing. In Java, multithreading can be achieved either by extending the `Thread` class or by implementing the `Runnable` interface. Synchronization is used to control the access of multiple threads to any shared resource.",
        "code": """```java
class MyRunnable implements Runnable {
    private String threadName;

    MyRunnable(String name) {
        this.threadName = name;
    }

    public void run() {
        try {
            for (int i = 1; i <= 3; i++) {
                System.out.println("Thread: " + threadName + ", Count: " + i);
                Thread.sleep(500); // Sleep for 500ms
            }
        } catch (InterruptedException e) {
            System.out.println("Thread " + threadName + " interrupted.");
        }
        System.out.println("Thread " + threadName + " exiting.");
    }
}

public class MultithreadingDemo {
    public static void main(String[] args) {
        Thread t1 = new Thread(new MyRunnable("T1"));
        Thread t2 = new Thread(new MyRunnable("T2"));

        t1.start();
        t2.start();
    }
}
```""",
        "output": """```
Thread: T1, Count: 1
Thread: T2, Count: 1
Thread: T2, Count: 2
Thread: T1, Count: 2
Thread: T2, Count: 3
Thread: T1, Count: 3
Thread T2 exiting.
Thread T1 exiting.
```""",
        "viva_questions": [
            "What are the two ways to create a thread in Java?",
            "What is the difference between start() and run() methods?",
            "Explain the thread lifecycle in Java.",
            "What is thread synchronization and why is it important?",
            "What is a deadlock in multithreading?",
            "How does wait() differ from sleep()?"
        ]
    },
    {
        "id": 3,
        "title": "Database Programming",
        "aim": "To connect to a database and perform CRUD operations using Java Database Connectivity (JDBC).",
        "theory": "JDBC (Java Database Connectivity) is a Java API that manages connecting to a database, issuing queries and commands, and handling result sets obtained from the database. The essential steps include loading the JDBC driver, establishing a connection, creating a statement, executing the query, and closing the connection.",
        "code": """```java
import java.sql.*;

public class JdbcDemo {
    // Replace with actual database credentials
    static final String DB_URL = "jdbc:mysql://localhost/testdb";
    static final String USER = "root";
    static final String PASS = "password";

    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
             Statement stmt = conn.createStatement()) {
            
            // Create Table
            String sql = "CREATE TABLE IF NOT EXISTS Students " +
                         "(id INTEGER not NULL, " +
                         " name VARCHAR(255), " +
                         " age INTEGER, " + 
                         " PRIMARY KEY ( id ))";
            stmt.executeUpdate(sql);
            System.out.println("Table created successfully.");
            
            // Insert Data
            sql = "INSERT IGNORE INTO Students VALUES (1, 'Alice', 20)";
            stmt.executeUpdate(sql);
            System.out.println("Record inserted.");
            
            // Fetch Data
            ResultSet rs = stmt.executeQuery("SELECT id, name, age FROM Students");
            while (rs.next()) {
                System.out.print("ID: " + rs.getInt("id"));
                System.out.print(", Name: " + rs.getString("name"));
                System.out.println(", Age: " + rs.getInt("age"));
            }
            rs.close();
            
        } catch (SQLException e) {
            e.printStackTrace();
        } 
    }
}
```""",
        "output": """```
Table created successfully.
Record inserted.
ID: 1, Name: Alice, Age: 20
```""",
        "viva_questions": [
            "What are the main components of JDBC API?",
            "Explain the difference between Statement and PreparedStatement.",
            "What is ResultSet and how is it used?",
            "Why is DriverManager used in JDBC?",
            "How do you handle SQL exceptions in Java?",
            "What is a connection pool?"
        ]
    },
    {
        "id": 4,
        "title": "Servlets",
        "aim": "To create a basic Java Servlet that handles HTTP GET and POST requests.",
        "theory": "A Java Servlet is a Java software component that extends the capabilities of a server. Servlets are typically used to process or store data that was submitted from an HTML form, provide dynamic content such as the results of a database query, and manage state information on top of the stateless HTTP protocol. The lifecycle methods are `init()`, `service()`, and `destroy()`.",
        "code": """```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        String name = request.getParameter("name");
        if(name == null) name = "World";
        
        out.println("<html><body>");
        out.println("<h2>Hello, " + name + "!</h2>");
        out.println("</body></html>");
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        doGet(request, response);
    }
}
```""",
        "output": """```
# When accessed via browser: http://localhost:8080/app/hello?name=John
<html><body>
<h2>Hello, John!</h2>
</body></html>
```""",
        "viva_questions": [
            "Describe the lifecycle of a Java Servlet.",
            "What is the difference between doGet() and doPost() methods?",
            "What is the deployment descriptor (web.xml) used for?",
            "Explain the use of the @WebServlet annotation.",
            "How does a Servlet maintain user sessions?",
            "What is the difference between GenericServlet and HttpServlet?"
        ]
    },
    {
        "id": 5,
        "title": "Spring Boot",
        "aim": "To build a simple RESTful API using Spring Boot.",
        "theory": "Spring Boot makes it easy to create stand-alone, production-grade Spring based applications that you can 'just run'. It provides auto-configuration, embedded servers (like Tomcat), and starter POMs to simplify Maven configuration. `@RestController` is used to create RESTful web services, combining `@Controller` and `@ResponseBody`.",
        "code": """```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @GetMapping("/api/greet")
    public String greet(@RequestParam(value = "name", defaultValue = "Spring Boot") String name) {
        return String.format("Hello, %s! Welcome to Spring Boot REST API.", name);
    }
}
```""",
        "output": """```
# HTTP GET request to /api/greet?name=User
Hello, User! Welcome to Spring Boot REST API.
```""",
        "viva_questions": [
            "What are the main advantages of using Spring Boot?",
            "Explain the @SpringBootApplication annotation.",
            "How does Spring Boot auto-configuration work?",
            "What is the difference between @Controller and @RestController?",
            "How can you change the default server port in Spring Boot?",
            "What is dependency injection in the context of Spring?"
        ]
    },
    {
        "id": 6,
        "title": "Secure PostgreSQL Connectivity using Node.js",
        "aim": "To securely connect to a PostgreSQL database using Node.js and the 'pg' module with environment variables.",
        "theory": "Connecting to databases securely requires keeping credentials out of the source code. In Node.js, this is commonly achieved using environment variables (e.g., via the `dotenv` package). The `pg` (node-postgres) module allows establishing connections to a PostgreSQL database using a connection pool, which is efficient for handling multiple concurrent queries.",
        "code": """```javascript
// Install dependencies: npm install pg dotenv

require('dotenv').config();
const { Pool } = require('pg');

// Create a pool instance using environment variables securely
// .env file should contain:
// PGUSER=myuser
// PGHOST=localhost
// PGPASSWORD=mypassword
// PGDATABASE=mydb
// PGPORT=5432

const pool = new Pool();

async function checkDatabaseConnection() {
    try {
        const client = await pool.connect();
        const res = await client.query('SELECT NOW() as current_time');
        console.log('Database connected securely!');
        console.log('Current Database Time:', res.rows[0].current_time);
        client.release();
    } catch (err) {
        console.error('Error connecting to database', err.stack);
    } finally {
        await pool.end();
    }
}

checkDatabaseConnection();
```""",
        "output": """```
Database connected securely!
Current Database Time: 2026-06-18T16:34:56.000Z
```""",
        "viva_questions": [
            "Why should database credentials never be hardcoded in the source code?",
            "What is connection pooling and why is it beneficial in Node.js?",
            "How does the 'dotenv' package work?",
            "What is the difference between a Client and a Pool in the 'pg' module?",
            "Explain asynchronous programming handling using async/await in database operations.",
            "How can you prevent SQL injection attacks in Node.js with PostgreSQL?"
        ]
    },
    {
        "id": 7,
        "title": "CRUD API Development using Express.js, Postman and Swagger",
        "aim": "To build a CRUD API using Express.js, test it via Postman, and document it using Swagger.",
        "theory": "Express.js is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. It facilitates the rapid development of RESTful APIs. Postman is a tool for API testing. Swagger (OpenAPI) provides a standardized way to describe RESTful APIs, allowing for interactive documentation.",
        "code": """```javascript
// Install dependencies: npm install express body-parser swagger-ui-express

const express = require('express');
const bodyParser = require('body-parser');
const swaggerUi = require('swagger-ui-express');
const app = express();

app.use(bodyParser.json());

// In-memory data store
let items = [{ id: 1, name: "Item One" }];

// Simple Swagger Document definition
const swaggerDocument = {
  openapi: '3.0.0',
  info: { title: 'Simple CRUD API', version: '1.0.0' },
  paths: {
    '/items': {
      get: {
        summary: 'Get all items',
        responses: { '200': { description: 'Successful response' } }
      }
    }
  }
};

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// Create
app.post('/items', (req, res) => {
    const newItem = { id: items.length + 1, name: req.body.name };
    items.push(newItem);
    res.status(201).json(newItem);
});

// Read
app.get('/items', (req, res) => {
    res.json(items);
});

// Update
app.put('/items/:id', (req, res) => {
    const item = items.find(i => i.id === parseInt(req.params.id));
    if (!item) return res.status(404).send('Item not found');
    item.name = req.body.name;
    res.json(item);
});

// Delete
app.delete('/items/:id', (req, res) => {
    items = items.filter(i => i.id !== parseInt(req.params.id));
    res.status(204).send();
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```""",
        "output": """```
Server running on port 3000

# GET /items
[{"id": 1, "name": "Item One"}]

# Swagger UI available at: http://localhost:3000/api-docs
```""",
        "viva_questions": [
            "What is Express.js and what are its core features?",
            "What is middleware in Express.js?",
            "Explain the difference between PUT and PATCH methods.",
            "What is the purpose of body-parser?",
            "Why is API documentation important and what role does Swagger play?",
            "How would you validate incoming request data in an Express API?"
        ]
    }
]

# Generate Markdown files
for topic in topics:
    # Assignment
    assign_filename = f"{subject_code}-Assignment-{topic['id']}.md"
    assign_filepath = os.path.join(assignments_dir, assign_filename)
    
    viva_filename = f"{subject_code}-Viva-{topic['id']}.md"
    
    assign_content = f"""# {subject_code} Assignment {topic['id']}: {topic['title']}

## Problem Statement / Aim
{topic['aim']}

## Theory & Concept
{topic['theory']}

## Fully Solved Code
{topic['code']}

## Expected Output
{topic['output']}

---
[[{subject_code}-Viva-{topic['id']}|View Viva Questions]]
"""
    with open(assign_filepath, "w") as f:
        f.write(assign_content)

    # Viva
    viva_filepath = os.path.join(viva_dir, viva_filename)
    
    questions = "\\n".join([f"{i+1}. {q}" for i, q in enumerate(topic['viva_questions'])])
    
    viva_content = f"""[[{subject_code}-Assignment-{topic['id']}|Back to Assignment]]

# Viva Questions: {topic['title']}

{questions}
"""
    with open(viva_filepath, "w") as f:
        f.write(viva_content)

# Update Lab-Overview.md
overview_path = os.path.join(base_dir, "Lab-Overview.md")

overview_content = f"# {subject_code} Lab Overview\\n\\n"
overview_content += "## Assignments\\n"
for topic in topics:
    overview_content += f"- [[{subject_code}-Assignment-{topic['id']}]] : {topic['title']}\\n"

overview_content += "\\n## Viva\\n"
for topic in topics:
    overview_content += f"- [[{subject_code}-Viva-{topic['id']}]] : {topic['title']}\\n"

with open(overview_path, "w") as f:
    f.write(overview_content)

print("Files generated successfully.")
