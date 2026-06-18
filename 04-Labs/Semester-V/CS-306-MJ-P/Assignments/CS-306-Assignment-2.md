# Assignment 2: Objects and Classes

## Problem Statement / Aim
To understand object-oriented programming concepts by creating classes and objects in Java.

## Theory & Concept
A **class** is a blueprint or template for creating objects. It defines state (fields/attributes) and behavior (methods). An **object** is an instance of a class.

**Constructors** are special methods used to initialize objects. The `this` keyword refers to the current object instance, often used to resolve variable hiding.

## Fully Solved Code
```java
// Student.java
public class Student {
    private String name;
    private int rollNo;

    // Constructor
    public Student(String name, int rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }

    // Method to display details
    public void display() {
        System.out.println("Student Name: " + name);
        System.out.println("Roll Number: " + rollNo);
    }

    public static void main(String[] args) {
        // Object creation
        Student s1 = new Student("Alice", 101);
        Student s2 = new Student("Bob", 102);

        s1.display();
        s2.display();
    }
}
```

## Expected Output
```
Student Name: Alice
Roll Number: 101
Student Name: Bob
Roll Number: 102
```

---
[[CS-306-Viva-2|View Viva Questions]]
