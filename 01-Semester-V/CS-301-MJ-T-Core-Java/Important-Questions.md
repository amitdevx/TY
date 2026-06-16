---
title: CS-301 Important Questions
subject_code: CS-301-MJ-T
subject_name: Core Java
tags:
  - cs-301
  - java
  - important-questions
  - exam-prep
  - semester-v
aliases:
  - Core Java Important Questions
  - CS-301 Question Bank
created: 2026-06-16
---

# CS-301 Core Java - Important Questions

> [!important] Exam Strategy
> **External Exam: 35 Marks** | **Duration:** ~2 hours
> Focus on understanding code behavior, not just memorizing. Always back theory with code examples.

---

##  Unit 1 - Introduction to Java

### Short Answer (2 Marks)

1. Define OOP. List and briefly explain its four pillars.
2. Who created Java? When and where was it developed?
3. What is the difference between JDK, JRE, and JVM?
4. Explain the "Write Once, Run Anywhere" principle.
5. List any 5 features of Java with one-line explanation each.
6. What is Bytecode? How is it different from machine code?
7. What is the difference between `break` and `continue` statements?
8. What is a jagged array? How is it different from a 2D array?
9. List the 8 primitive data types in Java with their sizes.
10. What is type casting? Differentiate widening and narrowing.

### Long Answer (5-7 Marks)

1. **Explain OOP concepts with real-world examples and code snippets.** (Encapsulation, Inheritance, Polymorphism, Abstraction)
2. **Compare Java environment components: JDK, JRE, JVM, Bytecode, JIT. Draw a diagram.**
3. **Write a Java program to find the largest element in a 2D array.**
4. **Explain all Java features in detail (at least 6 features).**
5. **Write a program demonstrating: Scanner input, for loop, if-else, and array traversal.**
6. **What are the types of variables in Java? Explain with code.**

### Program Questions

```java
// 1. Print Pascal's Triangle using 2D array
// 2. Find second largest in an array without sorting
// 3. Matrix multiplication using 2D arrays
// 4. Read N integers from Scanner, find sum and average
// 5. Print Fibonacci using for loop and while loop
// 6. Check if a number is prime (using for loop and break)
```

---

##  Unit 2 - Objects and Classes

### Short Answer (2 Marks)

1. What is the difference between a class and an object?
2. Explain access specifiers with their scope.
3. What is constructor overloading? Give an example.
4. What is the purpose of the `this` keyword?
5. What is the difference between instance variable and static variable?
6. What is a static block? When does it execute?
7. What is String immutability? Why are Strings immutable?
8. What is the difference between `String`, `StringBuffer`, and `StringBuilder`?
9. What is autoboxing and unboxing?
10. What is the String pool?
11. List any 5 methods of the String class with signatures.
12. List any 5 methods of the StringBuffer class with signatures.

### Long Answer (5-7 Marks)

1. **Explain the Object class methods: equals(), toString(), hashCode(), getClass() with code.**
2. **Explain Packages in Java. How to create and use packages? What are built-in packages?**
3. **Write a class `Student` with name, roll, marks. Define constructors, getters/setters, display method, and override toString().**
4. **Explain Wrapper classes with autoboxing and unboxing examples. List useful methods.**
5. **Explain static members in Java (static variable, static method, static block) with code.**

### Program Questions

```java
// 1. Class 'BankAccount' with deposit(), withdraw(), getBalance() methods
//    Handle insufficient balance in withdraw()
// 2. Program demonstrating constructor chaining using this()
// 3. Program comparing String vs StringBuffer performance (append in loop)
// 4. Class 'Circle' with overloaded constructors (no-arg, radius, radius+color)
// 5. Program to format output using String.format() - student marks report
```

---

##  Unit 3 - Inheritance and Interface

### Short Answer (2 Marks)

1. What is inheritance? What keyword is used?
2. Why doesn't Java support multiple inheritance through classes?
3. What are the uses of `super` keyword?
4. What is the difference between method overloading and method overriding?
5. What is `final` keyword? Explain its three uses.
6. What is an abstract class? Can we instantiate it?
7. What is the difference between abstract class and interface?
8. What is a functional interface? Give an example.
9. What is a lambda expression? What is its syntax?
10. What is an anonymous inner class? When is it used?
11. What is a Marker interface? Give two examples.
12. Can an interface have variables? What type?

### Long Answer (5-7 Marks)

1. **Explain all types of inheritance in Java with diagrams and code examples. Why is multiple inheritance not supported?**
2. **Explain interface with all features: traditional, default methods, static methods (Java 8+), functional interface, lambda expressions.**
3. **Write code demonstrating: abstract class Shape with abstract method area(), concrete subclasses Circle, Rectangle, Triangle.**
4. **Explain method overriding rules. Write a program showing runtime polymorphism.**
5. **Explain super keyword with all three uses and corresponding code.**

### Program Questions

```java
// 1. Employee → Manager → Director (multilevel inheritance, super() calls)
// 2. Interface Drawable + Resizable, class Image implementing both
// 3. Functional interface 'Greeting' with greet(String name) method,
//    implement with lambda for English, French, Spanish
// 4. Abstract class Vehicle, concrete classes Car, Bike, Truck
// 5. Anonymous inner class to sort array of strings by length
```

---

##  Unit 4 - Exception and File Handling

### Short Answer (2 Marks)

1. What is the difference between Error and Exception in Java?
2. Differentiate checked and unchecked exceptions with examples.
3. What is the difference between `throw` and `throws`?
4. Does `finally` always execute? When doesn't it?
5. Can we catch multiple exceptions in a single catch block? How?
6. What is try-with-resources?
7. How to create a user-defined exception?
8. List the log levels in java.util.logging.Logger.
9. What is the difference between `FileReader` and `FileInputStream`?
10. What is the purpose of `BufferedReader` class?
11. What is `InputStreamReader`? Why is it used?
12. What is the hierarchy of Java I/O stream classes?

### Long Answer (5-7 Marks)

1. **Draw and explain the exception class hierarchy in Java. Give examples of each type.**
2. **Explain try-catch-finally with multiple catch blocks and nested try. Write a program.**
3. **Write a program demonstrating user-defined exceptions for invalid age (<0 or >150) and invalid salary (<0).**
4. **Compare byte streams and character streams. Write a program to copy a text file using BufferedReader/Writer.**
5. **Explain DataInputStream/DataOutputStream with a program that writes and reads different data types.**

### Program Questions

```java
// 1. Read 10 integers, handle InputMismatchException, 
//    find average, catch ArithmeticException on division
// 2. File copy utility using FileInputStream/FileOutputStream with finally
// 3. WordCountProgram - read file, count words, lines, characters using BufferedReader
// 4. Student class with fields, write to file using DataOutputStream,
//    read back using DataInputStream
// 5. Custom exception 'InsufficientFundsException' for BankAccount
```

---

##  Unit 5 - User Interface with JavaFX

### Short Answer (2 Marks)

1. List any 5 differences between Swing and JavaFX.
2. Explain JavaFX application lifecycle (init, start, stop).
3. What is a Scene Graph?
4. What is the difference between Stage and Scene?
5. List any 4 layout panes in JavaFX with their usage.
6. What is the difference between `setOnAction()` and `addEventHandler()`?
7. List any 3 JavaFX charts with their use cases.
8. How do you handle events using lambda in JavaFX?
9. What is ObservableList?
10. What is `Platform.exit()` and `System.exit(0)` in JavaFX?

### Long Answer (5-7 Marks)

1. **Explain JavaFX architecture with all components. Draw a diagram.**
2. **Explain all JavaFX layout panes with diagrams and code snippets: HBox, VBox, BorderPane, GridPane.**
3. **Write a JavaFX application with a registration form (name, email, mobile, gender, city) using appropriate layouts and controls.**
4. **Write a JavaFX program to display a BarChart/LineChart showing monthly sales data.**
5. **Explain event handling in JavaFX with three different approaches (anonymous class, lambda, method reference).**

### Program Questions

```java
// 1. Simple Calculator JavaFX app - buttons for +,-,*,/ with text fields
// 2. JavaFX login form with validation - username + password
// 3. Student mark entry form → display PieChart of grade distribution
// 4. To-Do List app using JavaFX ListView, TextField, and buttons (Add, Delete, Clear)
// 5. Temperature converter JavaFX app (Celsius ↔ Fahrenheit ↔ Kelvin) using Slider
```

---

##  Tricky/Conceptual Questions

> [!warning] High-value questions likely in exams

1. **What happens when you run `String s1 = "Hello"; String s2 = "Hello"; System.out.println(s1 == s2);`?** (Answer: `true` - same String Pool object)

2. **What is the output?**
   ```java
   try {
       System.out.println("try");
       return;
   } finally {
       System.out.println("finally");
   }
   // Output: "try" then "finally" - finally runs even on return!
   ```

3. **Can we override a static method in Java?** (Answer: No - it's method hiding, not overriding)

4. **What is the output?**
   ```java
   class A { void show() { System.out.println("A"); } }
   class B extends A { void show() { System.out.println("B"); } }
   A obj = new B();
   obj.show(); // Output: "B" - runtime polymorphism!
   ```

5. **What happens if we don't call super() in a subclass constructor?** (Java implicitly calls `super()` - default parent constructor. Error if parent has no default constructor.)

6. **Can an interface extend another interface?** (Answer: YES! `interface A extends B, C { ... }`)

7. **Can abstract class have constructors?** (Answer: Yes - called via super() from concrete subclass)

8. **What is the difference between `==` and `equals()` for strings?**
   ```java
   String a = new String("hello");
   String b = new String("hello");
   a == b       // false (different objects in heap)
   a.equals(b)  // true (same content)
   ```

9. **What is Belady's Anomaly?** (Wait - that's OS, not Java! Don't mix subjects!)

10. **What is the difference between `ArrayList` and `LinkedList`?** (Preview of Collections)

---

##  One-liner Answers (Quick Review)

| Question | Answer |
|----------|--------|
| Java created by? | James Gosling, Sun Microsystems, 1995 |
| Originally called? | Oak |
| WORA means? | Write Once, Run Anywhere |
| JVM is? | Platform-specific; executes bytecode |
| JDK includes? | JRE + development tools (javac, javadoc) |
| String is? | Immutable, from java.lang, String Pool |
| StringBuffer vs StringBuilder? | Buffer: thread-safe; Builder: faster, not thread-safe |
| Default access? | Package-private |
| `this()` must be? | First statement in constructor |
| static block runs? | Once, when class is loaded |
| final class example? | String, Integer, Math |
| Abstract class can have? | Fields, constructors, concrete + abstract methods |
| Interface fields are? | public static final (constants) |
| Functional interface has? | Exactly 1 abstract method |
| Lambda syntax? | `(params) -> expression` |
| Checked exception must? | Be caught or declared with throws |
| finally always runs? | Yes, except System.exit() |
| try-with-resources needs? | AutoCloseable implementation |
| JavaFX entry point? | `start(Stage primaryStage)` |
| ObservableList is? | List that auto-updates UI when modified |
