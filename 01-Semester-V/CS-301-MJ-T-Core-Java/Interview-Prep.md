---
title: "CS-301 Core Java Interview Preparation"
tags: [cs-301, core-java, interview, semester-v]
subject_code: CS-301-MJ-T
type: interview-prep
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Core Java Interview Preparation

> [!summary] About
> Top 30+ Core Java interview questions categorized by topic, with detailed answers and code snippets. Essential for technical interviews and placement drives.

---

## 1. Object-Oriented Programming (OOP) Concepts

> [!question] 1. What are the core concepts of OOP in Java?
> The four core concepts are:
> 1. **Encapsulation:** Wrapping data (variables) and code acting on the data (methods) together as a single unit (Class).
> 2. **Inheritance:** Mechanism where one class acquires the properties and behaviors of a parent class.
> 3. **Polymorphism:** The ability of a variable, function or object to take on multiple forms (Overloading, Overriding).
> 4. **Abstraction:** Hiding internal implementation details and showing only functionality to the user (Abstract classes, Interfaces).

> [!question] 2. What is the difference between Abstraction and Encapsulation?
> - **Abstraction** hides the implementation details (shows *what* it does).
> - **Encapsulation** hides the data (protects *how* it does it) by making fields private and providing getters/setters.

> [!question] 3. What is a Constructor? Can a constructor be private?
> A constructor is a special method invoked automatically when an object is created. It has the same name as the class and no return type.
> Yes, constructors can be private (used in the Singleton design pattern to prevent instantiation from outside).

---

## 2. Java Basics & Environment

> [!question] 4. Explain JVM, JRE, and JDK.
> - **JVM (Java Virtual Machine):** An abstract machine that provides the runtime environment to execute Java bytecode (`.class` files).
> - **JRE (Java Runtime Environment):** Contains JVM + core libraries/classes required to run Java applications.
> - **JDK (Java Development Kit):** Contains JRE + development tools (compiler `javac`, debugger `jdb`, etc.).

> [!question] 5. Why is Java platform independent?
> Java code is compiled into intermediate bytecode rather than machine-specific code. This bytecode can be executed on any system that has a JVM, making Java "Write Once, Run Anywhere" (WORA).

> [!question] 6. What is the `static` keyword in Java?
> The `static` keyword means the member belongs to the class itself, rather than to instances of the class.
> - **Static variables:** Shared among all objects.
> - **Static methods:** Can be called without creating an object. Cannot access non-static members.
> - **Static block:** Used for static initialization of a class.

---

## 3. String & Wrapper Classes

> [!question] 7. What is the difference between String, StringBuilder, and StringBuffer?
> - **String:** Immutable (cannot be changed once created). Slower when performing many concatenations.
> - **StringBuffer:** Mutable and thread-safe (synchronized). Slower than StringBuilder.
> - **StringBuilder:** Mutable but NOT thread-safe. Fastest for single-threaded string manipulation.

> [!question] 8. What is Autoboxing and Unboxing?
> - **Autoboxing:** Automatic conversion of primitive types to their corresponding wrapper classes (e.g., `int` to `Integer`).
> - **Unboxing:** Automatic conversion of wrapper classes back to primitive types.
> ```java
> Integer wrapperObj = 10; // Autoboxing
> int primitiveVar = wrapperObj; // Unboxing
> ```

---

## 4. Inheritance & Polymorphism

> [!question] 9. Does Java support multiple inheritance? Why?
> Java does NOT support multiple inheritance with classes to avoid the "Diamond Problem" (ambiguity if two parent classes have methods with the same signature). However, Java supports multiple inheritance through **Interfaces**.

> [!question] 10. What is the difference between Method Overloading and Method Overriding?
> - **Overloading (Compile-time Polymorphism):** Same method name, different parameters within the same class. Return type can vary.
> - **Overriding (Runtime Polymorphism):** Same method name and parameters in a child class that exists in the parent class. Used to provide a specific implementation.

> [!question] 11. What are the `super` and `this` keywords?
> - `this`: Refers to the current class instance. Used to resolve naming conflicts between instance variables and parameters.
> - `super`: Refers to the immediate parent class instance. Used to call parent methods, variables, or constructors.

> [!question] 12. Can we override a `static` method?
> No. Static methods are bound at compile time (static binding) to the class. If a child class defines a static method with the same signature, it "hides" the parent method rather than overriding it (Method Hiding).

---

## 5. Interfaces & Abstract Classes

> [!question] 13. Abstract Class vs Interface
> | Feature | Abstract Class | Interface |
> |---------|----------------|-----------|
> | Implementation | Can have abstract and concrete methods | Only abstract methods (until Java 8 introduced default/static) |
> | Variables | Can have final, non-final, static, non-static | Only `public static final` constants |
> | Multiple Inheritance | A class can extend only one abstract class | A class can implement multiple interfaces |
> | Constructors | Has constructors | Does not have constructors |

> [!question] 14. What is a Functional Interface?
> An interface that contains exactly **one abstract method**. They can have multiple default or static methods. Used extensively with Lambda expressions (introduced in Java 8). Annotated with `@FunctionalInterface`. Example: `Runnable`, `Callable`.

> [!question] 15. What is a Marker Interface?
> An interface with no methods or fields. It is an empty interface used to signal to the JVM that a class has a specific property. Examples: `Serializable`, `Cloneable`.

---

## 6. Exception Handling

> [!question] 16. What is the difference between Checked and Unchecked Exceptions?
> - **Checked Exceptions:** Checked at compile-time. Must be handled using `try-catch` or declared using `throws`. Inherit from `Exception` (e.g., `IOException`, `SQLException`).
> - **Unchecked Exceptions:** Checked at runtime. Do not need to be explicitly handled. Inherit from `RuntimeException` (e.g., `NullPointerException`, `ArithmeticException`).

> [!question] 17. Explain `try`, `catch`, `finally`, `throw`, and `throws`.
> - `try`: Block of code where exceptions might occur.
> - `catch`: Block to handle the exception thrown in the try block.
> - `finally`: Block that always executes regardless of whether an exception occurred or not (used to close resources).
> - `throw`: Used to explicitly throw a single exception from within a method.
> - `throws`: Used in method signature to declare that the method might throw exceptions.

> [!question] 18. What happens if an exception is thrown inside a `finally` block?
> The exception thrown in the `finally` block will override any exception that was originally thrown in the `try` block, and it will propagate up the call stack unless caught within the `finally` block.

---

## 7. File Handling & Streams

> [!question] 19. Difference between InputStream and Reader?
> - `InputStream` (and `OutputStream`) deal with **byte streams** (8-bit bytes). Used for binary data like images or audio (`FileInputStream`).
> - `Reader` (and `Writer`) deal with **character streams** (16-bit Unicode characters). Used for text data (`FileReader`).

> [!question] 20. What is the purpose of `BufferedReader`?
> `BufferedReader` reads text from a character-input stream, buffering characters to provide efficient reading of characters, arrays, and lines. It minimizes the number of expensive physical disk reads.

---

## 8. JavaFX

> [!question] 21. JavaFX vs Swing
> - **Swing:** Older, heavier GUI toolkit. Uses absolute positioning primarily. No built-in support for modern CSS/animations.
> - **JavaFX:** Modern, lightweight framework. Uses a Scene Graph architecture. Built-in support for CSS styling, 3D graphics, media, and animations. Separates UI design (FXML) from business logic.

> [!question] 22. Explain the JavaFX Application Lifecycle.
> 1. `init()`: Called once before the application starts. Cannot create scenes here.
> 2. `start(Stage)`: The main entry point. All UI is created and shown here.
> 3. `stop()`: Called when the application is shutting down.

> [!question] 23. What are the common Layout Panes in JavaFX?
> - **HBox:** Arranges nodes horizontally in a single row.
> - **VBox:** Arranges nodes vertically in a single column.
> - **BorderPane:** Arranges nodes in top, bottom, left, right, and center regions.
> - **GridPane:** Arranges nodes in a flexible grid of rows and columns.

---

[[01-Semester-V/CS-301-MJ-T-Core-Java/Unit-1|Unit 1]] | [[01-Semester-V/CS-301-MJ-T-Core-Java/Revision|Revision Summary]]
