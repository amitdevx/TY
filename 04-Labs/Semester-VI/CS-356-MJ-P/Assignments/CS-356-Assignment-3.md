# CS-356 Assignment 3: Database Programming

## Problem Statement / Aim
To connect to a database and perform CRUD operations using Java Database Connectivity (JDBC).

## Theory & Concept
JDBC (Java Database Connectivity) is a Java API that manages connecting to a database, issuing queries and commands, and handling result sets obtained from the database. The essential steps include loading the JDBC driver, establishing a connection, creating a statement, executing the query, and closing the connection.

## Fully Solved Code
```java
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
```

## Expected Output
```
Table created successfully.
Record inserted.
ID: 1, Name: Alice, Age: 20
```

---
[[CS-356-Viva-3|View Viva Questions]]
