# Assignment 4: Exception and File Handling

## Problem Statement / Aim
To demonstrate exception handling mechanisms and basic file I/O operations in Java.

## Theory & Concept
**Exceptions** are runtime errors that disrupt the normal flow of the program. Java uses `try`, `catch`, `finally`, `throw`, and `throws` to handle exceptions.

**File Handling** involves reading from and writing to files. The `java.io` package provides classes like `File`, `FileReader`, and `FileWriter` for text-based I/O.

## Fully Solved Code
```java
import java.io.*;

public class FileExceptionExample {
    public static void main(String[] args) {
        String fileName = "example.txt";

        // Writing to a file
        try (FileWriter writer = new FileWriter(fileName)) {
            writer.write("Hello, Exception and File Handling in Java!");
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred while writing.");
            e.printStackTrace();
        }

        // Reading from a file
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line = reader.readLine();
            System.out.println("Read from file: " + line);
        } catch (FileNotFoundException e) {
            System.out.println("File not found exception caught.");
        } catch (IOException e) {
            System.out.println("I/O Exception caught.");
        }
    }
}
```

## Expected Output
```
Successfully wrote to the file.
Read from file: Hello, Exception and File Handling in Java!
```

---
[[CS-306-Viva-4|View Viva Questions]]
