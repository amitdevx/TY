# Assignment 3: Inheritance and Interfaces

## Problem Statement / Aim
To implement inheritance and interfaces in Java for code reusability and abstraction.

## Theory & Concept
**Inheritance** is an OOP mechanism where a new class inherits properties and behaviors from an existing class. Java supports single and multilevel inheritance but not multiple inheritance through classes.

An **interface** is a reference type in Java containing abstract methods and constants. It is used to achieve 100% abstraction and multiple inheritance.

## Fully Solved Code
```java
// ShapeInterface.java
interface Shape {
    double calculateArea();
}

class Circle implements Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
}

public class Main {
    public static void main(String[] args) {
        Shape circle = new Circle(5.0);
        System.out.println("Area of Circle: " + circle.calculateArea());
    }
}
```

## Expected Output
```
Area of Circle: 78.53981633974483
```

---
[[CS-306-Viva-3|View Viva Questions]]
