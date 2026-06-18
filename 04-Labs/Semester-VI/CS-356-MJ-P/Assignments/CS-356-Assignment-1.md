# CS-356 Assignment 1: Collections

## Problem Statement / Aim
To understand and implement various collection classes such as ArrayList, HashMap, and HashSet in Java.

## Theory & Concept
The Java Collections Framework provides a set of interfaces and classes to store and manipulate a group of objects. Key interfaces include List (ordered collection), Set (unordered collection without duplicates), and Map (key-value pairs). Implementations include `ArrayList`, `LinkedList`, `HashSet`, `TreeSet`, `HashMap`, and `TreeMap`.

## Fully Solved Code
```java
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
```

## Expected Output
```
ArrayList: [Java, Python, C++]
HashSet: [20, 10]
HashMap: {Bob=85, Alice=90}
```

---
[[CS-356-Viva-1|View Viva Questions]]
