# Assignment 6: Frontend Foundations (HTML5 & CSS3)

## Problem Statement / Aim
To design a responsive web page using semantic HTML5 tags and CSS3 styling.

## Theory & Concept
**HTML5** introduces semantic elements (like `<header>`, `<nav>`, `<section>`, `<footer>`) that clearly describe their meaning to the browser and developer.

**CSS3** adds styles, layout, and visual formatting. The **Box Model** dictates how elements are rendered with margins, borders, padding, and content. Flexbox and Grid provide powerful layout systems.

## Fully Solved Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0; padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background: #333;
            color: #fff;
            padding: 1rem;
            text-align: center;
        }
        .container {
            padding: 20px;
            margin: 20px auto;
            width: 80%;
            background: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1, p {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My Portfolio</h1>
    </header>
    <div class="container">
        <h2>About Me</h2>
        <p>I am a computer science student learning Web Technologies.</p>
    </div>
</body>
</html>
```

## Expected Output
```
[A web page displaying a dark header with "Welcome to My Portfolio" and a white container section with "About Me" text.]
```

---
[[CS-306-Viva-6|View Viva Questions]]
