---
title: CS-301 Core Java - Revision Notes
subject_code: CS-301-MJ-T
tags:
  - cs-301
  - java
  - revision
  - semester-v
  - quick-review
aliases:
  - Core Java Revision
  - CS-301 Quick Review
created: 2026-06-16
---

# CS-301 Core Java - Revision Notes

> [!important] Last-minute revision guide. Read these notes 1 day before exam!

---

##  Unit 1 - Introduction to Java

> [!note] Unit 1 Summary (5 Hours)

### OOP Pillars (AIPE)
| Pillar | Keyword | One-liner |
|--------|---------|-----------|
| **A**bstraction | `abstract`, `interface` | Show WHAT, hide HOW |
| **I**nheritance | `extends`, `implements` | Child reuses parent's code |
| **P**olymorphism | `@Override`, overloading | One name, many forms |
| **E**ncapsulation | `private` + getters/setters | Bundle data + methods; data hiding |

### Java History
- **Creator:** James Gosling | **Company:** Sun Microsystems | **Year:** 1995
- **Original name:** Oak | **Oracle acquired** Sun in 2010
- **WORA:** Write Once, Run Anywhere

### JDK ⊃ JRE ⊃ JVM
```
JDK = JRE + Tools (javac, javadoc, jar, jdb)
JRE = JVM + Class Libraries (rt.jar)
JVM = ClassLoader + Bytecode Verifier + JIT Compiler + Interpreter
```

### Data Types (mnemonics)
```
byte(1) short(2) int(4) long(8) → integer family
float(4) double(8) → decimal family
char(2) → 2 bytes because Unicode!
boolean → true/false
```

### Variables
- **Local:** Inside method, no default, must initialize before use
- **Instance:** Inside class, has defaults (0, null, false)
- **Static:** Shared by all objects, class level

### Control Flow
```
if-else | switch-case | for | while | do-while (runs at least once)
break (exits loop) | continue (skips iteration) | labeled break (exits outer loop)
```

### Arrays
- **1D:** `int[] arr = new int[5];` or `int[] arr = {1,2,3};`
- **2D:** `int[][] m = new int[3][4];`
- **Jagged:** `int[][] j = new int[3][]; j[0] = new int[2];` - rows have different sizes

---

##  Unit 2 - Objects and Classes

> [!note] Unit 2 Summary (6 Hours)

### Access Specifiers (remember: private < default < protected < public)
```
private → only same class
default (no modifier) → same package
protected → same package + subclasses
public → everywhere
```

### Constructor Rules
- Same name as class, no return type
- Automatically called with `new`
- Default constructor provided ONLY if no constructor defined
- `this()` calls another constructor - must be FIRST statement

### `this` Keyword
```java
this.field = field;    // resolve naming conflict
this(args)            // call another constructor (first statement!)
return this;          // method chaining
```

### Static
```
static variable: ONE copy shared by ALL objects
static method: called without object (ClassName.method())
static block: runs ONCE when class loads
```

### String Methods (must know)
```
length() charAt(i) indexOf(c) substring(s,e)
toLowerCase() toUpperCase() trim() replace(a,b)
equals() equalsIgnoreCase() compareTo() contains()
split(regex) concat(s) startsWith() endsWith()
```

### String vs StringBuffer vs StringBuilder
```
String → Immutable → Thread-safe (trivially) → Slow for concat
StringBuffer → Mutable → Thread-safe (synchronized) → Medium
StringBuilder → Mutable → NOT thread-safe → FASTEST
```

### Wrapper Classes
```
int → Integer | double → Double | char → Character | boolean → Boolean
Autoboxing: int n = 5; Integer w = n;  (automatic)
Unboxing:   Integer w = 5; int n = w;  (automatic)
parseInt("42") → 42 | valueOf(42) → Integer object
```

---

##  Unit 3 - Inheritance and Interface

> [!note] Unit 3 Summary (6 Hours)

### Inheritance Types
```
Single: A → B (one parent, one child)
Multilevel: A → B → C (chain)
Hierarchical: A → B, A → C, A → D (one parent, many children)
Multiple: NOT via classes (Diamond Problem)!
          BUT possible via interfaces (implements multiple)
```

### super Keyword
```java
super()          // call parent constructor (first statement!)
super.method()   // call parent's overridden method
super.field      // access shadowed parent field
```

### Overriding vs Overloading
```
Overriding: same class hierarchy, same signature, runtime polymorphism
Overloading: same class, different params, compile-time polymorphism
```

### final
```
final variable = constant (cannot reassign)
final method = cannot be overridden
final class = cannot be extended
Examples: String, Integer, Math classes are final
```

### abstract
```
abstract method: no body; must be overridden by concrete subclass
abstract class: cannot instantiate; can have both abstract + concrete methods
```

### Interface
```java
interface I {
    void abstractMethod();              // public abstract (default)
    int CONSTANT = 10;                  // public static final (default)
    default void defaultMethod() { }    // Java 8+ has body
    static void staticMethod() { }     // Java 8+ belongs to interface
}
// implements multiple interfaces → Java's answer to multiple inheritance
```

### @FunctionalInterface + Lambda
```
Functional Interface = interface with EXACTLY 1 abstract method
Lambda = (params) -> expression/block
Example: Runnable r = () -> System.out.println("Run!");
```

---

##  Unit 4 - Exception and File Handling

> [!note] Unit 4 Summary (5 Hours)

### Exception Hierarchy
```
Throwable
├── Error (don't catch: OutOfMemoryError, StackOverflowError)
└── Exception
    ├── RuntimeException (Unchecked - optional to handle)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   └── ArithmeticException
    └── Checked Exceptions (MUST handle)
        ├── IOException → FileNotFoundException
        └── SQLException
```

### Keywords
```
try    → wrap risky code
catch  → handle exception (specific BEFORE general)
finally → ALWAYS runs (cleanup) - even on return!
throw  → manually throw: throw new MyException("msg");
throws → declare in signature: void m() throws IOException
```

### User-Defined Exception
```java
class MyException extends Exception {  // or RuntimeException
    MyException(String msg) { super(msg); }
}
throw new MyException("Something went wrong");
```

### Logger Levels (High → Low)
```
SEVERE → WARNING → INFO → CONFIG → FINE → FINER → FINEST
```

### I/O Stream Quick Reference
```
Byte Streams (for binary):
  FileInputStream/FileOutputStream → raw bytes
  BufferedInput/OutputStream → buffered (faster)
  DataInput/OutputStream → primitives (readInt/writeInt etc.)

Character Streams (for text):
  FileReader/FileWriter → characters
  BufferedReader/BufferedWriter → lines (readLine/newLine)

Bridge Streams:
  InputStreamReader → byte stream → character stream (with encoding)
  OutputStreamWriter → character stream → byte stream
```

---

##  Unit 5 - User Interface with JavaFX

> [!note] Unit 5 Summary (8 Hours)

### JavaFX vs Swing
```
JavaFX: CSS styling, FXML, built-in charts/media, modern, scene graph
Swing: Older, no FXML, maintenance mode
```

### Architecture
```
Scene Graph → Prism (render) + Glass (windows) + Media Engine + WebView
Quantum Toolkit orchestrates Prism + Glass
```

### Lifecycle Order
```
launch() → init() [non-UI] → start(Stage) [build UI] → [running] → stop() [cleanup]
```

### Hierarchy
```
Stage (window) → Scene (content) → Root Node (layout) → Nodes (controls)
```

### Layouts
```
HBox  → horizontal row (toolbars)
VBox  → vertical column (forms)
BorderPane → 5 regions: TOP, BOTTOM, LEFT, RIGHT, CENTER
GridPane → rows + columns table
FlowPane → wrapping flow
StackPane → overlapping layers
```

### Charts
```
PieChart → pie slices (ObservableList<PieChart.Data>)
LineChart → connected points (XYChart.Series + XYChart.Data)
AreaChart → filled area
BarChart → vertical bars (CategoryAxis for X)
```

### Events
```java
btn.setOnAction(e -> System.out.println("Clicked!")); // lambda (preferred)
btn.addEventHandler(ActionEvent.ACTION, handler);      // multiple handlers
btn.removeEventHandler(ActionEvent.ACTION, handler);   // remove handler
```

---

##  Key Terms Glossary

| Term | Subject | Definition |
|------|---------|-----------|
| WORA | Java | Write Once, Run Anywhere - Java's platform independence |
| JIT | Java | Just-In-Time compiler - converts bytecode to native at runtime |
| Autoboxing | Java | Automatic int → Integer conversion |
| String Pool | Java | Cache for string literals in heap/metaspace |
| Abstract method | Java | Method with no body; must be overridden |
| SAM | Java | Single Abstract Method - functional interface has exactly 1 |
| Lambda | Java | `(params) -> body` - concise function implementation |
| Checked exception | Java | Must handle at compile time (IOException) |
| Stage | JavaFX | Window representation |
| Scene Graph | JavaFX | Hierarchical tree of all visual nodes |

---

## ️ Common Mistakes to Avoid

> [!warning] Don't make these errors in exams!

1. **Catch order:** Always specific exceptions BEFORE general (`Exception` last)
2. **this() placement:** `this()` MUST be the FIRST statement in constructor
3. **Static context:** Static methods CANNOT access instance variables directly
4. **String equality:** Use `.equals()` for content comparison, not `==`
5. **char size:** Java `char` is **2 bytes** (not 1 byte like in C)
6. **Multiple inheritance:** Not possible via classes; ONLY via interfaces
7. **Abstract class:** Cannot create object of abstract class (no `new AbstractClass()`)
8. **Interface constants:** All interface fields are implicitly `public static final`
9. **finally vs return:** `finally` runs EVEN IF there's a `return` in try/catch
10. **super() call:** If not explicitly written, Java adds `super()` implicitly (no-arg only)

---

##  Last-Minute Tips

> [!tip] 30 Minutes Before Exam

1. **Memorize the Exception Hierarchy** - Throwable → Error/Exception → RuntimeException
2. **Know all 8 data types** and their sizes (especially char=2 bytes)
3. **Practice writing class code** - constructor, getter/setter, toString() override
4. **Remember interface rules** - no instance fields, no constructors, multiple implementation allowed
5. **Know lambda syntax** - `(params) -> expression` - very commonly asked
6. **For JavaFX questions** - always mention: Stage → Scene → Root Node hierarchy
7. **File I/O** - remember: BufferedReader has `readLine()`, BufferedWriter has `newLine()`
8. **String methods** - prepare to list 5-6 methods with correct signatures
9. **This keyword** - `this(args)` must be FIRST statement (write this explicitly)
10. **All stream types** - know which is for bytes (Input/OutputStream) vs chars (Reader/Writer)

---

##  One-Page Summary

```mermaid
mindmap
  root((CS-301 Core Java))
    Unit 1
      OOP: AIPE
      JDK/JRE/JVM
      8 Primitives
      Control Flow
      Arrays
    Unit 2
      Access Specifiers
      Constructors + this()
      static + Object class
      String immutable
      StringBuffer mutable
      Packages
      Wrapper + autoboxing
    Unit 3
      Inheritance: extends
      super keyword
      Overriding runtime
      Overloading compile
      final abstract
      Interface implements
      Lambda expressions
    Unit 4
      Exception Hierarchy
      try-catch-finally
      throw vs throws
      User-defined Exception
      Byte vs Char Streams
      Buffered for speed
    Unit 5
      JavaFX architecture
      Stage-Scene-Node
      Layouts
      Charts
      Event handling
```

---

##  Navigation

- [[Overview| Subject Overview]]
- [[Syllabus| Syllabus]]
- [[Important-Questions| Important Questions]]
- [[Interview-Prep| Interview Preparation]]
