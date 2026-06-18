# CS-356 Assignment 5: Spring Boot

## Problem Statement / Aim
To build a simple RESTful API using Spring Boot.

## Theory & Concept
Spring Boot makes it easy to create stand-alone, production-grade Spring based applications that you can 'just run'. It provides auto-configuration, embedded servers (like Tomcat), and starter POMs to simplify Maven configuration. `@RestController` is used to create RESTful web services, combining `@Controller` and `@ResponseBody`.

## Fully Solved Code
```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @GetMapping("/api/greet")
    public String greet(@RequestParam(value = "name", defaultValue = "Spring Boot") String name) {
        return String.format("Hello, %s! Welcome to Spring Boot REST API.", name);
    }
}
```

## Expected Output
```
# HTTP GET request to /api/greet?name=User
Hello, User! Welcome to Spring Boot REST API.
```

---
[[CS-356-Viva-5|View Viva Questions]]
