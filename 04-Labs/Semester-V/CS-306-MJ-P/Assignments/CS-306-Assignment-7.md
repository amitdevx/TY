# Assignment 7: Interactive Web Logic (JavaScript & DOM)

## Problem Statement / Aim
To add interactivity to a web page using JavaScript and DOM manipulation.

## Theory & Concept
The **Document Object Model (DOM)** represents an HTML document as a tree of objects. JavaScript can access and manipulate these objects to change the structure, style, and content of the page dynamically.

**Event listeners** are used to execute JavaScript code when a specific event (like a click, mouseover, or keypress) occurs on an element.

## Fully Solved Code
```html
<!DOCTYPE html>
<html>
<head>
    <title>Interactive DOM</title>
</head>
<body>
    <h2 id="status">Status: Waiting</h2>
    <button id="actionBtn">Click to Update</button>

    <script>
        const btn = document.getElementById('actionBtn');
        const statusText = document.getElementById('status');

        btn.addEventListener('click', function() {
            statusText.innerText = "Status: Updated via JavaScript!";
            statusText.style.color = "green";
        });
    </script>
</body>
</html>
```

## Expected Output
```
[Clicking the "Click to Update" button changes the text to "Status: Updated via JavaScript!" and turns the text green.]
```

---
[[CS-306-Viva-7|View Viva Questions]]
