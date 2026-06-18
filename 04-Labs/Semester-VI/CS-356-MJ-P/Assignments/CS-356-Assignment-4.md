# CS-356 Assignment 4: Servlets

## Problem Statement / Aim
To create a basic Java Servlet that handles HTTP GET and POST requests.

## Theory & Concept
A Java Servlet is a Java software component that extends the capabilities of a server. Servlets are typically used to process or store data that was submitted from an HTML form, provide dynamic content such as the results of a database query, and manage state information on top of the stateless HTTP protocol. The lifecycle methods are `init()`, `service()`, and `destroy()`.

## Fully Solved Code
```java
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        String name = request.getParameter("name");
        if(name == null) name = "World";
        
        out.println("<html><body>");
        out.println("<h2>Hello, " + name + "!</h2>");
        out.println("</body></html>");
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        doGet(request, response);
    }
}
```

## Expected Output
```
# When accessed via browser: http://localhost:8080/app/hello?name=John
<html><body>
<h2>Hello, John!</h2>
</body></html>
```

---
[[CS-356-Viva-4|View Viva Questions]]
