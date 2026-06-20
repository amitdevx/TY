---
title: Unit 2 - Objects and Classes
unit_number: 2
hours: 6
subject: CS-301-MJ-T
subject_name: Core Java
tags:
  - cs-301
  - java
  - unit-2
  - classes
  - objects
  - semester-v
aliases:
  - Java Unit 2
  - Objects and Classes
created: 2026-06-16
last_modified: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# Unit 2 - Objects and Classes
> [!important] **Hours:** 6 | **Subject:** CS-301-MJ-T Core Java | **Semester:** V
> **Previous:** [[Unit-1|Unit 1: Introduction to Java]] | **Next:** [[Unit-3|Unit 3: Inheritance and Interface]]

---

## Learning Objectives

- Define classes with fields and methods
- Use access specifiers to control visibility
- Understand constructors and constructor overloading
- Use `this` keyword and static members
- Work with Object class methods
- Use String and StringBuffer classes effectively
- Organize code using packages
- Use wrapper classes with autoboxing/unboxing

---

## 2.1 Defining Classes

> [!note] Definition
> A ==class== is a **blueprint** or **template** that defines the structure (fields) and behavior (methods) of objects. An ==object== is an **instance** of a class.

```java
// Class definition
class Student {
    // Fields (instance variables / attributes)
    String name;
    int age;
    double marks;
    
    // Method (behavior)
    void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
    
    double getGrade() {
        return marks >= 90 ? 'A' : marks >= 75 ? 'B' : 'C';
    }
}

// Creating and using objects
public class Main {
    public static void main(String[] args) {
        Student s1 = new Student();    // object creation using 'new'
        s1.name = "Alice";             // accessing fields
        s1.age = 20;
        s1.marks = 92.5;
        s1.display();                  // calling method
        
        Student s2 = new Student();    // another object (separate memory)
        s2.name = "Bob";
    }
}
```

### Class vs Object

| Feature | Class | Object |
|---------|-------|--------|
| Definition | Blueprint/template | Instance of a class |
| Memory | No memory allocated | Memory allocated on heap |
| Exists | Logically in code | Physically in memory |
| Example | `class Dog` | `Dog myDog = new Dog()` |

---

## 2.2 Access Specifiers (Modifiers)

==Access specifiers== control the **visibility and accessibility** of class members (fields and methods).

| Specifier | Same Class | Same Package | Subclass (different pkg) | Any Class |
|-----------|-----------|--------------|--------------------------|-----------|
| **private** |  |  |  |  |
| **default** (no modifier) |  |  |  |  |
| **protected** |  |  |  |  |
| **public** |  |  |  |  |

```java
class AccessDemo {
    private int priv = 1;        // only within this class
    int deflt = 2;               // package-private (default)
    protected int prot = 3;      // package + subclasses
    public int pub = 4;          // everywhere
    
    // Proper encapsulation: private field + public getter/setter
    private String name;
    public String getName() { return name; }
    public void setName(String n) { this.name = n; }
}
```

> [!tip] Best Practice
> Always declare fields as **`private`** and provide **public getters/setters** - this is the principle of **encapsulation**.

---

## 2.3 Array of Objects

```java
// Creating an array of objects
Student[] students = new Student[3]; // array of 3 Student references

// Each element must be individually instantiated
students[0] = new Student("Alice", 20, 95.0);
students[1] = new Student("Bob", 21, 88.5);
students[2] = new Student("Charlie", 19, 76.0);

// Iterating array of objects
for (Student s : students) {
    s.display();
}
```

---

## 2.4 Constructors

> [!note] Definition
> A ==constructor== is a **special method** that is **automatically called** when an object is created using `new`. It has the **same name as the class** and **no return type** (not even void).

### Types of Constructors

```java
class Box {
    double length, width, height;
    
    // 1. Default Constructor (no parameters)
    Box() {
        length = 1.0; width = 1.0; height = 1.0;
        System.out.println("Default box created");
    }
    
    // 2. Parameterized Constructor
    Box(double l, double w, double h) {
        length = l; width = w; height = h;
    }
    
    // 3. Copy Constructor (Java - not built-in, must write manually)
    Box(Box other) {
        this.length = other.length;
        this.width = other.width;
        this.height = other.height;
    }
    
    double volume() { return length * width * height; }
}
```

### Constructor Overloading

> [!note]
> ==Constructor Overloading== means having **multiple constructors** with different parameter lists in the same class.

```java
class Circle {
    double radius;
    String color;
    
    Circle() { radius = 1.0; color = "Red"; }           // default
    Circle(double r) { radius = r; color = "Red"; }     // one param
    Circle(double r, String c) { radius = r; color = c; } // two params
}

// Usage
Circle c1 = new Circle();              // calls default
Circle c2 = new Circle(5.0);           // calls one-param
Circle c3 = new Circle(3.0, "Blue");   // calls two-param
```

> [!important] Constructor vs Method
> - Constructor name = class name; Method name can be anything
> - Constructor has no return type; Methods have return types
> - Constructor is called automatically with `new`; Methods are called explicitly
> - If no constructor defined, Java provides a **default no-arg constructor**

---

## 2.5 `this` Keyword

The ==`this`== keyword is a **reference to the current object** (the object on which the method is called).

```java
class Employee {
    String name;
    int id;
    double salary;
    
    // Use 'this' to resolve name conflict (parameter vs field)
    Employee(String name, int id, double salary) {
        this.name = name;         // this.name = field, name = parameter
        this.id = id;
        this.salary = salary;
    }
    
    // Use this() to call another constructor (must be first statement)
    Employee(String name) {
        this(name, 0, 0.0);       // calls the 3-param constructor
    }
    
    // Return current object
    Employee getSelf() { return this; }
    
    // Method chaining using 'this'
    Employee setName(String n) { this.name = n; return this; }
    Employee setSalary(double s) { this.salary = s; return this; }
}
// Method chaining example:
emp.setName("Alice").setSalary(50000);
```

---

## 2.6 Static Members

| Static Member | Description |
|---------------|-------------|
| **Static Variable** | Shared across ALL instances; belongs to class, not object |
| **Static Method** | Can be called without creating an object; cannot access instance variables |
| **Static Block** | Executed once when class is loaded, before any objects created |
| **Static Import** | `import static java.lang.Math.*;` - access static members without class name |

```java
class Counter {
    static int count = 0;    // static - shared by all objects
    int id;
    
    // Static block - runs once when class loads
    static {
        System.out.println("Counter class loaded!");
        count = 100; // initialize static variable
    }
    
    Counter() {
        count++;
        id = count;
    }
    
    // Static method - accessed as Counter.getCount()
    static int getCount() {
        return count;          // can only access static members
        // return id;          // ERROR: cannot access instance variable
    }
}

// Usage
System.out.println(Counter.getCount()); // 100 (from static block)
Counter c1 = new Counter();             // count = 101
Counter c2 = new Counter();             // count = 102
System.out.println(Counter.getCount()); // 102
```

---

## 2.7 Object Class Methods

Every Java class **implicitly extends** `java.lang.Object`. The Object class provides key methods:

| Method | Signature | Description |
|--------|-----------|-------------|
| `toString()` | `public String toString()` | String representation (default: classname@hashcode) |
| `equals()` | `public boolean equals(Object obj)` | Compares objects for equality (default: reference comparison) |
| `hashCode()` | `public int hashCode()` | Returns hash code (must override with equals()) |
| `getClass()` | `public final Class<?> getClass()` | Returns runtime class of the object |
| `clone()` | `protected Object clone()` | Creates a shallow copy (must implement Cloneable) |
| `finalize()` | `protected void finalize()` | Called by GC before object destruction (deprecated Java 9+) |

```java
class Point {
    int x, y;
    
    Point(int x, int y) { this.x = x; this.y = y; }
    
    // Override toString for readable output
    @Override
    public String toString() {
        return "Point(" + x + ", " + y + ")";
    }
    
    // Override equals for content-based comparison
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Point)) return false;
        Point p = (Point) obj;
        return this.x == p.x && this.y == p.y;
    }
    
    // Override hashCode (always override when overriding equals)
    @Override
    public int hashCode() {
        return 31 * x + y;
    }
}

Point p1 = new Point(3, 4);
Point p2 = new Point(3, 4);
System.out.println(p1.toString());     // Point(3, 4)
System.out.println(p1.equals(p2));     // true (content comparison)
System.out.println(p1.getClass().getName()); // Point
```

---

## 2.8 String Class

> [!important] Strings are Immutable
> In Java, `String` objects are **immutable** - once created, their content **cannot be changed**. Any operation that "modifies" a String actually creates a **new String object**.

```java
String s = "Hello";
s = s + " World";  // Creates new String "Hello World"; old "Hello" is garbage
```

### String Pool

```mermaid
graph TD
    A["String s1 =<br/>\"Hello\""] --> P["String Pool<br/>\"Hello\""]
    B["String s2 =<br/>\"Hello\""] --> P
    C["String s3 = new<br/>String(\"Hello\")"] --> H["Heap<br/>\"Hello\" (separate object)"]
```

- String literals go into the **String Pool** (interning)
- `new String()` always creates a **new object in heap**
- `s1 == s2` is `true` (same pool reference)
- `s1 == s3` is `false` (different memory locations)

### Common String Methods

```java
String s = "Hello, World!";

// Length and access
s.length()           // 13
s.charAt(0)          // 'H'
s.indexOf('o')       // 4 (first occurrence)
s.lastIndexOf('o')   // 8

// Substring
s.substring(7)       // "World!"
s.substring(7, 12)   // "World"

// Comparison
s.equals("Hello, World!") // true
s.equalsIgnoreCase("HELLO, WORLD!") // true
s.compareTo("Hello") // positive (longer)
s.contains("World")  // true
s.startsWith("Hello") // true
s.endsWith("!")      // true

// Transformation
s.toLowerCase()      // "hello, world!"
s.toUpperCase()      // "HELLO, WORLD!"
s.trim()             // removes leading/trailing spaces
s.replace('l', 'r')  // "Herro, Worrd!"
s.replace("World", "Java") // "Hello, Java!"

// Splitting
String[] parts = "a,b,c".split(","); // ["a", "b", "c"]

// Concatenation
"Hello" + " World"   // "Hello World"
s.concat(" Bye")     // "Hello, World! Bye"

// Type conversion
String.valueOf(42)   // "42"
Integer.parseInt("42") // 42

// String checking
s.isEmpty()          // false
s.isBlank()          // false (Java 11+)
```

---

## 2.9 StringBuffer Class

> [!note] StringBuffer vs String
> ==StringBuffer== is a **mutable** sequence of characters. Unlike `String`, it can be modified **in-place** without creating new objects. Use when you have **many string modifications**.
> 
> `StringBuilder` is like StringBuffer but **not thread-safe** (faster for single-threaded use).

```java
StringBuffer sb = new StringBuffer("Hello");

// append - add at end
sb.append(" World");     // "Hello World"
sb.append(42);           // "Hello World42"

// insert - add at position
sb.insert(5, ",");       // "Hello, World42"

// delete - remove range [start, end)
sb.delete(5, 6);         // "Hello World42"

// deleteCharAt
sb.deleteCharAt(11);     // removes char at index 11

// replace - replace range with string
sb.replace(6, 11, "Java"); // "Hello Java42"

// reverse - reverse the entire buffer
sb.reverse();            // "24avaJ olleH"

// length and capacity
sb.length()              // current length
sb.capacity()            // current capacity (default 16 + initial length)

// convert to String
String result = sb.toString();
```

| Feature | String | StringBuffer | StringBuilder |
|---------|--------|--------------|---------------|
| Mutability | Immutable | Mutable | Mutable |
| Thread-safe | Yes (immutable) | Yes (synchronized) | No |
| Performance | Slow for concat | Medium | Fast |
| Use case | Read-only text | Multi-threaded concat | Single-threaded concat |

---

## 2.10 String Formatting

```java
// String.format() - printf-style formatting
String name = "Alice";
int age = 25;
double gpa = 3.85;

String formatted = String.format("Name: %s, Age: %d, GPA: %.2f", name, age, gpa);
// "Name: Alice, Age: 25, GPA: 3.85"

// printf - formatted print (no newline)
System.out.printf("%-10s | %5d | %8.2f%n", name, age, gpa);

// Format specifiers
// %s  → String
// %d  → integer
// %f  → floating point (%.2f = 2 decimal places)
// %c  → character
// %b  → boolean
// %n  → newline (platform-independent)
// %-5s → left-aligned with width 5
// %05d → zero-padded with width 5
```

---

## 2.11 Packages

> [!note] Definition
> A ==package== is a **namespace** that organizes related classes and interfaces, preventing naming conflicts and controlling access.

### Built-in Packages

| Package | Contents |
|---------|---------|
| `java.lang` | Auto-imported; String, Math, Object, System, Thread, Exception |
| `java.util` | Collections, Scanner, Date, Arrays, ArrayList, HashMap |
| `java.io` | File I/O streams - FileReader, BufferedReader, etc. |
| `java.net` | Networking - Socket, URL, HttpURLConnection |
| `java.awt` | Abstract Window Toolkit (legacy GUI) |
| `javax.swing` | Swing GUI components |
| `javafx.*` | JavaFX GUI framework |

### Creating and Using Packages

```java
// File: com/example/myapp/Student.java
package com.example.myapp;    // package declaration (must be first statement)

public class Student {
    public String name;
    public void display() { System.out.println(name); }
}
```

```java
// File: Main.java
import com.example.myapp.Student;        // import specific class
// import com.example.myapp.*;           // import all classes from package

public class Main {
    public static void main(String[] args) {
        Student s = new Student();
        s.name = "Alice";
        s.display();
    }
}
```

```bash
# Compilation with packages
javac -d . com/example/myapp/Student.java
javac Main.java
java Main
```

---

## 2.12 Wrapper Classes

> [!note] Definition
> ==Wrapper classes== provide **object representations** of Java's 8 primitive data types. They allow primitives to be used in contexts that require objects (e.g., collections).

| Primitive | Wrapper Class |
|-----------|--------------|
| `byte` | `Byte` |
| `short` | `Short` |
| `int` | `Integer` |
| `long` | `Long` |
| `float` | `Float` |
| `double` | `Double` |
| `char` | `Character` |
| `boolean` | `Boolean` |

### Autoboxing and Unboxing

```java
// Autoboxing - primitive → wrapper (automatic, Java 5+)
int n = 42;
Integer wrapped = n;          // autoboxing: int → Integer
Integer w2 = Integer.valueOf(n); // explicit boxing

// Unboxing - wrapper → primitive (automatic)
Integer obj = 100;
int primitive = obj;          // unboxing: Integer → int
int p2 = obj.intValue();      // explicit unboxing
```

### Useful Wrapper Methods

```java
// Integer methods
Integer.parseInt("123")          // String → int
Integer.valueOf(123)             // int → Integer object
Integer.toBinaryString(10)       // "1010"
Integer.toHexString(255)         // "ff"
Integer.toOctalString(8)         // "10"
Integer.MAX_VALUE                // 2147483647
Integer.MIN_VALUE                // -2147483648
Integer.compare(5, 3)            // positive (5 > 3)

// Double methods
Double.parseDouble("3.14")       // String → double
Double.isNaN(0.0/0.0)           // true (Not a Number)
Double.isInfinite(1.0/0.0)      // true

// Character methods
Character.isDigit('5')           // true
Character.isLetter('A')          // true
Character.isUpperCase('A')       // true
Character.toLowerCase('A')       // 'a'
Character.toUpperCase('a')       // 'A'

// Boolean methods
Boolean.parseBoolean("true")     // true
Boolean.parseBoolean("false")    // false
Boolean.parseBoolean("hello")    // false (anything else = false)
```

---

## Key Concepts

```mermaid
mindmap
  root((Unit 2 Concepts))
    Classes & Objects
      Fields
      Methods
      new keyword
      Heap allocation
    Access Specifiers
      private
      default
      protected
      public
    Constructors
      Default
      Parameterized
      Constructor Overloading
      this()
    static Members
      Static Variable
      Static Method
      Static Block
    Strings
      Immutable String
      String Pool
      StringBuffer mutable
      StringBuilder fast
    Packages
      Namespace
      import statement
      java.lang auto-imported
    Wrappers
      Autoboxing
      Unboxing
      parseXxx methods
```

---

## Interview Questions

> [!tip] Commonly Asked in Exams and Interviews

1. **What is the difference between `String`, `StringBuffer`, and `StringBuilder`?**
   - `String`: Immutable, thread-safe, slow for concatenation in loops
   - `StringBuffer`: Mutable, thread-safe (synchronized), moderate performance
   - `StringBuilder`: Mutable, NOT thread-safe, fastest for single-threaded concatenation

2. **Why are Strings immutable in Java?**
   - Security (class loading uses string class names, can't be tampered)
   - String pool efficiency (pooling requires immutability)
   - Thread-safety (immutable objects are inherently thread-safe)
   - Cached `hashCode` (since it can't change)

3. **What is autoboxing and unboxing?**
   - **Autoboxing:** Automatic conversion from primitive to wrapper (`int` → `Integer`)
   - **Unboxing:** Automatic conversion from wrapper to primitive (`Integer` → `int`)

4. **What is the purpose of the `this` keyword?**
   - Refers to current object's instance
   - Resolves name conflicts between fields and parameters
   - `this()` calls another constructor (constructor chaining)
   - Returns current object (for method chaining)

5. **Can a constructor call another constructor?**
   - Yes, using `this()` - must be the **first statement** in the constructor body.

6. **What is the difference between `equals()` and `==`?**
   - `==`: Compares references (memory addresses) for objects
   - `equals()`: Compares content/values (if overridden)

7. **What is a static block? When does it execute?**
   - Static block runs **once** when the class is loaded into memory (before any object is created). Used for static initialization.

8. **What is the difference between instance variable and static variable?**
   - Instance variable: Each object has its own copy; allocated per object
   - Static variable: ONE copy shared by ALL objects; allocated when class loads

9. **What is the String Pool?**
   - A special area in the heap (PermGen/Metaspace) where string literals are cached. When you create `"hello"`, Java checks if it exists in pool. If yes, returns existing reference.

10. **What happens if we don't define a constructor?**
    - Java provides a **default no-arg constructor** that calls `super()`. Once you define any constructor, the default is no longer provided.

---

## Revision Summary

> [!note] Quick Revision - Unit 2
> 
> **Class = Blueprint** | **Object = Instance** (created with `new` on heap)
> 
> **Access:** private (class) < default (package) < protected (+subclass) < public (everywhere)
> 
> **Constructor:** Same name as class, no return type, auto-called on `new`
> 
> **`this`:** Current object reference; `this()` = call another constructor (must be first)
> 
> **static:** Belongs to class, shared by all; static block runs once on class loading
> 
> **String:** Immutable, String Pool; StringBuffer: mutable, thread-safe; StringBuilder: mutable, fast
> 
> **Wrappers:** Integer, Double, etc. - autoboxing/unboxing since Java 5
> 
> **Packages:** Namespaces; `java.lang` is auto-imported

---

## Navigation

| Previous                                 | Current                         | Next                                          |
| ---------------------------------------- | ------------------------------- | --------------------------------------------- |
| [[Unit-1|Unit 1: Introduction to Java]] | **Unit 2: Objects and Classes** | [[Unit-3|Unit 3: Inheritance and Interface]] |
