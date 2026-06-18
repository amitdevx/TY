import os

base_dir = "/home/amitdevx/Downloads/TY/04-Labs/Semester-V/CS-306-MJ-P"
assignments_dir = os.path.join(base_dir, "Assignments")
viva_dir = os.path.join(base_dir, "Viva")

os.makedirs(assignments_dir, exist_ok=True)
os.makedirs(viva_dir, exist_ok=True)

subject_code = "CS-306"

assignments = [
    {
        "id": 1,
        "topic": "Java Tools and IDE",
        "aim": "To familiarize with Java Tools (JDK, javac, java) and IDE by writing and executing a simple Java program.",
        "theory": "Java is a high-level, object-oriented programming language. The Java Development Kit (JDK) provides the environment to develop and run Java programs. It includes the Java Runtime Environment (JRE) and development tools like the compiler (`javac`) and the interpreter (`java`).\n\nThe compilation process converts Java source code (`.java` files) into platform-independent bytecode (`.class` files), which is then executed by the Java Virtual Machine (JVM).",
        "code": "```java\n// HelloWorld.java\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n        System.out.println(\"Welcome to Java Programming.\");\n    }\n}\n```",
        "output": "```\nHello, World!\nWelcome to Java Programming.\n```",
        "viva_qs": [
            "What is the difference between JDK, JRE, and JVM?",
            "Why is Java considered platform-independent?",
            "What is bytecode in Java?",
            "What is the role of the `javac` command?",
            "Explain the `public static void main` method signature."
        ]
    },
    {
        "id": 2,
        "topic": "Objects and Classes",
        "aim": "To understand object-oriented programming concepts by creating classes and objects in Java.",
        "theory": "A **class** is a blueprint or template for creating objects. It defines state (fields/attributes) and behavior (methods). An **object** is an instance of a class.\n\n**Constructors** are special methods used to initialize objects. The `this` keyword refers to the current object instance, often used to resolve variable hiding.",
        "code": "```java\n// Student.java\npublic class Student {\n    private String name;\n    private int rollNo;\n\n    // Constructor\n    public Student(String name, int rollNo) {\n        this.name = name;\n        this.rollNo = rollNo;\n    }\n\n    // Method to display details\n    public void display() {\n        System.out.println(\"Student Name: \" + name);\n        System.out.println(\"Roll Number: \" + rollNo);\n    }\n\n    public static void main(String[] args) {\n        // Object creation\n        Student s1 = new Student(\"Alice\", 101);\n        Student s2 = new Student(\"Bob\", 102);\n\n        s1.display();\n        s2.display();\n    }\n}\n```",
        "output": "```\nStudent Name: Alice\nRoll Number: 101\nStudent Name: Bob\nRoll Number: 102\n```",
        "viva_qs": [
            "What is a class and how does it differ from an object?",
            "What is a constructor and what are its rules?",
            "Can a class have multiple constructors? If yes, what is it called?",
            "What is the purpose of the `this` keyword?",
            "What is the difference between a default constructor and a parameterized constructor?"
        ]
    },
    {
        "id": 3,
        "topic": "Inheritance and Interfaces",
        "aim": "To implement inheritance and interfaces in Java for code reusability and abstraction.",
        "theory": "**Inheritance** is an OOP mechanism where a new class inherits properties and behaviors from an existing class. Java supports single and multilevel inheritance but not multiple inheritance through classes.\n\nAn **interface** is a reference type in Java containing abstract methods and constants. It is used to achieve 100% abstraction and multiple inheritance.",
        "code": "```java\n// ShapeInterface.java\ninterface Shape {\n    double calculateArea();\n}\n\nclass Circle implements Shape {\n    private double radius;\n\n    public Circle(double radius) {\n        this.radius = radius;\n    }\n\n    @Override\n    public double calculateArea() {\n        return Math.PI * radius * radius;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Shape circle = new Circle(5.0);\n        System.out.println(\"Area of Circle: \" + circle.calculateArea());\n    }\n}\n```",
        "output": "```\nArea of Circle: 78.53981633974483\n```",
        "viva_qs": [
            "Why doesn't Java support multiple inheritance using classes?",
            "What is the `super` keyword used for?",
            "What is the difference between an abstract class and an interface?",
            "Can an interface extend another interface?",
            "What is method overriding?"
        ]
    },
    {
        "id": 4,
        "topic": "Exception and File Handling",
        "aim": "To demonstrate exception handling mechanisms and basic file I/O operations in Java.",
        "theory": "**Exceptions** are runtime errors that disrupt the normal flow of the program. Java uses `try`, `catch`, `finally`, `throw`, and `throws` to handle exceptions.\n\n**File Handling** involves reading from and writing to files. The `java.io` package provides classes like `File`, `FileReader`, and `FileWriter` for text-based I/O.",
        "code": "```java\nimport java.io.*;\n\npublic class FileExceptionExample {\n    public static void main(String[] args) {\n        String fileName = \"example.txt\";\n\n        // Writing to a file\n        try (FileWriter writer = new FileWriter(fileName)) {\n            writer.write(\"Hello, Exception and File Handling in Java!\");\n            System.out.println(\"Successfully wrote to the file.\");\n        } catch (IOException e) {\n            System.out.println(\"An error occurred while writing.\");\n            e.printStackTrace();\n        }\n\n        // Reading from a file\n        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {\n            String line = reader.readLine();\n            System.out.println(\"Read from file: \" + line);\n        } catch (FileNotFoundException e) {\n            System.out.println(\"File not found exception caught.\");\n        } catch (IOException e) {\n            System.out.println(\"I/O Exception caught.\");\n        }\n    }\n}\n```",
        "output": "```\nSuccessfully wrote to the file.\nRead from file: Hello, Exception and File Handling in Java!\n```",
        "viva_qs": [
            "What is the difference between Checked and Unchecked exceptions?",
            "What is the purpose of the `finally` block?",
            "Explain the difference between `throw` and `throws`.",
            "What is try-with-resources in Java?",
            "Which classes are used for reading and writing characters to a file?"
        ]
    },
    {
        "id": 5,
        "topic": "GUI Designing and Event Handling",
        "aim": "To design a basic Graphical User Interface and handle user events using Java Swing.",
        "theory": "**Java Swing** is a lightweight GUI toolkit that includes components like `JFrame`, `JButton`, `JLabel`, and `JTextField`.\n\n**Event Handling** allows a program to respond to user actions (like button clicks). It requires a source object, an event object, and an event listener interface (e.g., `ActionListener`).",
        "code": "```java\nimport javax.swing.*;\nimport java.awt.event.*;\n\npublic class ClickCounter {\n    public static void main(String[] args) {\n        JFrame frame = new JFrame(\"Click Counter\");\n        JButton button = new JButton(\"Click Me\");\n        JLabel label = new JLabel(\"Clicks: 0\");\n\n        button.setBounds(50, 50, 100, 30);\n        label.setBounds(60, 90, 100, 30);\n\n        final int[] count = {0};\n\n        button.addActionListener(new ActionListener() {\n            public void actionPerformed(ActionEvent e) {\n                count[0]++;\n                label.setText(\"Clicks: \" + count[0]);\n            }\n        });\n\n        frame.add(button);\n        frame.add(label);\n        frame.setSize(250, 200);\n        frame.setLayout(null);\n        frame.setVisible(true);\n        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n    }\n}\n```",
        "output": "```\n[A window pops up with a \"Click Me\" button. Clicking the button increments the \"Clicks: 0\" counter.]\n```",
        "viva_qs": [
            "What is the difference between AWT and Swing?",
            "What is the role of an `ActionListener`?",
            "How does the Event Delegation Model work?",
            "Why do we use layout managers in Java GUI?",
            "What is the default layout manager for a `JFrame`?"
        ]
    },
    {
        "id": 6,
        "topic": "Frontend Foundations (HTML5 & CSS3)",
        "aim": "To design a responsive web page using semantic HTML5 tags and CSS3 styling.",
        "theory": "**HTML5** introduces semantic elements (like `<header>`, `<nav>`, `<section>`, `<footer>`) that clearly describe their meaning to the browser and developer.\n\n**CSS3** adds styles, layout, and visual formatting. The **Box Model** dictates how elements are rendered with margins, borders, padding, and content. Flexbox and Grid provide powerful layout systems.",
        "code": "```html\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <title>My Portfolio</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 0; padding: 0;\n            background-color: #f4f4f4;\n        }\n        header {\n            background: #333;\n            color: #fff;\n            padding: 1rem;\n            text-align: center;\n        }\n        .container {\n            padding: 20px;\n            margin: 20px auto;\n            width: 80%;\n            background: #fff;\n            box-shadow: 0 0 10px rgba(0,0,0,0.1);\n        }\n        h1, p {\n            margin: 10px 0;\n        }\n    </style>\n</head>\n<body>\n    <header>\n        <h1>Welcome to My Portfolio</h1>\n    </header>\n    <div class=\"container\">\n        <h2>About Me</h2>\n        <p>I am a computer science student learning Web Technologies.</p>\n    </div>\n</body>\n</html>\n```",
        "output": "```\n[A web page displaying a dark header with \"Welcome to My Portfolio\" and a white container section with \"About Me\" text.]\n```",
        "viva_qs": [
            "What are semantic elements in HTML5? Give examples.",
            "Explain the CSS Box Model.",
            "What is the difference between `margin` and `padding`?",
            "How can you make a website responsive?",
            "What is the difference between inline and block-level elements?"
        ]
    },
    {
        "id": 7,
        "topic": "Interactive Web Logic (JavaScript & DOM)",
        "aim": "To add interactivity to a web page using JavaScript and DOM manipulation.",
        "theory": "The **Document Object Model (DOM)** represents an HTML document as a tree of objects. JavaScript can access and manipulate these objects to change the structure, style, and content of the page dynamically.\n\n**Event listeners** are used to execute JavaScript code when a specific event (like a click, mouseover, or keypress) occurs on an element.",
        "code": "```html\n<!DOCTYPE html>\n<html>\n<head>\n    <title>Interactive DOM</title>\n</head>\n<body>\n    <h2 id=\"status\">Status: Waiting</h2>\n    <button id=\"actionBtn\">Click to Update</button>\n\n    <script>\n        const btn = document.getElementById('actionBtn');\n        const statusText = document.getElementById('status');\n\n        btn.addEventListener('click', function() {\n            statusText.innerText = \"Status: Updated via JavaScript!\";\n            statusText.style.color = \"green\";\n        });\n    </script>\n</body>\n</html>\n```",
        "output": "```\n[Clicking the \"Click to Update\" button changes the text to \"Status: Updated via JavaScript!\" and turns the text green.]\n```",
        "viva_qs": [
            "What is the DOM?",
            "How do `document.getElementById` and `document.querySelector` differ?",
            "What is an event listener?",
            "Explain event bubbling and event capturing.",
            "How do you change the CSS class of an element using JavaScript?"
        ]
    },
    {
        "id": 8,
        "topic": "Modern JavaScript ES6+",
        "aim": "To implement modern JavaScript (ES6+) features such as arrow functions, destructuring, and let/const.",
        "theory": "ECMAScript 6 (ES6) introduced significant updates to JavaScript:\n- **`let` and `const`**: Block-scoped variable declarations.\n- **Arrow Functions**: Shorter syntax for writing functions.\n- **Template Literals**: Multi-line strings and string interpolation using backticks (``).\n- **Destructuring**: Unpacking values from arrays or properties from objects into distinct variables.",
        "code": "```javascript\n// Using const and let\nconst greeting = \"Hello\";\nlet count = 5;\n\n// Arrow function\nconst multiply = (a, b) => a * b;\n\n// Object destructuring\nconst student = { name: \"John\", age: 20, grade: \"A\" };\nconst { name, grade } = student;\n\n// Template literals\nconst message = `${greeting}, ${name}! You scored grade ${grade} and the result is ${multiply(count, 2)}.`;\n\nconsole.log(message);\n\n// Spread Operator\nconst arr1 = [1, 2, 3];\nconst arr2 = [...arr1, 4, 5];\nconsole.log(\"Spread array:\", arr2);\n```",
        "output": "```\nHello, John! You scored grade A and the result is 10.\nSpread array: [ 1, 2, 3, 4, 5 ]\n```",
        "viva_qs": [
            "What is the difference between `var`, `let`, and `const`?",
            "How does `this` behave differently in an arrow function compared to a regular function?",
            "What is object destructuring?",
            "Explain the use of template literals.",
            "What is the difference between the spread and rest operators?"
        ]
    },
    {
        "id": 9,
        "topic": "Asynchronous Programming",
        "aim": "To perform asynchronous operations in JavaScript using Callbacks, Promises, and async/await.",
        "theory": "JavaScript is single-threaded but handles asynchronous operations via the **Event Loop**.\n- **Callbacks** are functions passed as arguments to be executed later.\n- **Promises** represent the eventual completion (or failure) of an asynchronous operation (States: pending, fulfilled, rejected).\n- **`async/await`** provides a cleaner, synchronous-looking syntax over Promises.",
        "code": "```javascript\n// Function returning a Promise\nfunction fetchData() {\n    return new Promise((resolve, reject) => {\n        setTimeout(() => {\n            resolve(\"Data successfully fetched from server.\");\n        }, 2000);\n    });\n}\n\n// Using async/await to consume the Promise\nasync function displayData() {\n    console.log(\"Fetching data...\");\n    try {\n        const data = await fetchData();\n        console.log(\"Success:\", data);\n    } catch (error) {\n        console.log(\"Error:\", error);\n    }\n}\n\ndisplayData();\n```",
        "output": "```\nFetching data...\n(Wait for 2 seconds)\nSuccess: Data successfully fetched from server.\n```",
        "viva_qs": [
            "What is callback hell?",
            "What are the three states of a Promise?",
            "Why do we use `async` and `await`?",
            "How does the JavaScript Event Loop work?",
            "How do you handle errors in a Promise chain and in async/await?"
        ]
    },
    {
        "id": 10,
        "topic": "Server-Side Basics with Node.js",
        "aim": "To create a basic server using Node.js and its core modules.",
        "theory": "**Node.js** is an open-source, cross-platform JavaScript runtime environment built on Chrome's V8 engine. It allows executing JavaScript code outside a web browser.\n\nThe core `http` module allows Node.js to transfer data over the Hyper Text Transfer Protocol (HTTP), making it possible to create a web server.",
        "code": "```javascript\n// server.js\nconst http = require('http');\n\nconst server = http.createServer((req, res) => {\n    // Set response header\n    res.writeHead(200, { 'Content-Type': 'text/plain' });\n    \n    if (req.url === '/') {\n        res.end('Welcome to Node.js Server Basics!\\n');\n    } else if (req.url === '/about') {\n        res.end('About Us Page\\n');\n    } else {\n        res.writeHead(404);\n        res.end('404 Not Found\\n');\n    }\n});\n\nconst PORT = 3000;\nserver.listen(PORT, () => {\n    console.log(`Server running at http://localhost:${PORT}/`);\n});\n```",
        "output": "```\nServer running at http://localhost:3000/\n(When visited in browser, displays \"Welcome to Node.js Server Basics!\")\n```",
        "viva_qs": [
            "What is Node.js and how does it differ from front-end JavaScript?",
            "Explain the purpose of the `require` function.",
            "What does the `http` module do?",
            "Is Node.js single-threaded or multi-threaded?",
            "What is NPM?"
        ]
    },
    {
        "id": 11,
        "topic": "File System and API Fundamentals",
        "aim": "To interact with the File System and understand fundamental API concepts in Node.js.",
        "theory": "The **`fs` (File System)** module in Node.js provides an API for interacting with the file system. It supports both synchronous and asynchronous methods.\n\nAn **API (Application Programming Interface)** in the context of web servers is a set of endpoints (URLs) that respond with data (usually JSON), forming the basis of RESTful services.",
        "code": "```javascript\n// file-api.js\nconst fs = require('fs');\nconst http = require('http');\n\nconst server = http.createServer((req, res) => {\n    if (req.url === '/api/data' && req.method === 'GET') {\n        // Read data asynchronously from a file\n        fs.readFile('data.txt', 'utf8', (err, data) => {\n            if (err) {\n                res.writeHead(500, { 'Content-Type': 'application/json' });\n                res.end(JSON.stringify({ error: 'Internal Server Error' }));\n            } else {\n                res.writeHead(200, { 'Content-Type': 'application/json' });\n                res.end(JSON.stringify({ message: 'Success', content: data.trim() }));\n            }\n        });\n    } else {\n        res.writeHead(404, { 'Content-Type': 'application/json' });\n        res.end(JSON.stringify({ error: 'Endpoint not found' }));\n    }\n});\n\n// Create a dummy data.txt file for testing\nfs.writeFileSync('data.txt', 'This is some sample text data from the file system.');\n\nserver.listen(3000, () => {\n    console.log('API Server running on port 3000');\n});\n```",
        "output": "```\nAPI Server running on port 3000\n// Request to /api/data returns:\n// {\"message\":\"Success\",\"content\":\"This is some sample text data from the file system.\"}\n```",
        "viva_qs": [
            "What is the difference between `fs.readFile` and `fs.readFileSync`?",
            "What is REST API?",
            "List some common HTTP methods and their uses.",
            "Why is JSON the standard format for API responses?",
            "What does a 404 and 500 HTTP status code indicate?"
        ]
    }
]

overview_content = "# CS-306-MJ-P Lab Overview\n\nWelcome to the CS-306-MJ-P Lab. Here are all the completed assignments and corresponding viva questions.\n\n## Assignments\n"

ass_links = []
viva_links = []

for a in assignments:
    # Write Assignment File
    ass_filename = f"{subject_code}-Assignment-{a['id']}.md"
    ass_path = os.path.join(assignments_dir, ass_filename)
    
    ass_content = f"# Assignment {a['id']}: {a['topic']}\n\n"
    ass_content += f"## Problem Statement / Aim\n{a['aim']}\n\n"
    ass_content += f"## Theory & Concept\n{a['theory']}\n\n"
    ass_content += f"## Fully Solved Code\n{a['code']}\n\n"
    ass_content += f"## Expected Output\n{a['output']}\n\n"
    ass_content += f"---\n"
    ass_content += f"[[{subject_code}-Viva-{a['id']}|View Viva Questions]]\n"
    
    with open(ass_path, "w") as f:
        f.write(ass_content)
        
    # Write Viva File
    viva_filename = f"{subject_code}-Viva-{a['id']}.md"
    viva_path = os.path.join(viva_dir, viva_filename)
    
    viva_content = f"[[{subject_code}-Assignment-{a['id']}|Back to Assignment]]\n\n"
    viva_content += f"# Viva Questions: {a['topic']}\n\n"
    
    for i, q in enumerate(a['viva_qs'], 1):
        viva_content += f"{i}. {q}\n"
        
    with open(viva_path, "w") as f:
        f.write(viva_content)
        
    ass_links.append(f"- [[{subject_code}-Assignment-{a['id']}|Assignment {a['id']}: {a['topic']}]]")
    viva_links.append(f"- [[{subject_code}-Viva-{a['id']}|Viva {a['id']}: {a['topic']}]]")

overview_content += "\n".join(ass_links) + "\n\n## Viva Questions\n" + "\n".join(viva_links) + "\n"

overview_path = os.path.join(base_dir, "Lab-Overview.md")
with open(overview_path, "w") as f:
    f.write(overview_content)

print("Successfully generated all files.")
