---
title: "CS-303 Unit-1 - Web Basics: HTML5 & CSS3"
aliases: ["Web Tech Unit 1", "HTML5 CSS3 Notes", "CS303 Ch1"]
tags:
  - subject/web-technology
  - semester/V
  - unit/1
  - html5
  - css3
  - flexbox
  - grid
  - responsive-design
subject_code: CS-303-MJ-T
unit: 1
chapter: "Chapter 1 - Web Basics"
type: unit-notes
last_reviewed: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# Unit 1 - Web Basics: HTML5 & CSS3

> [!note] Navigation
> [[Overview|CS-303 Overview]] | [[Syllabus|CS-303 Syllabus]] | **Unit 1** → [[Unit-2]] → [[Unit-3]] → [[Unit-4]]

---

## Learning Objectives

- Understand HTML5 semantic elements and their purpose
- Master the CSS box model and all selector types
- Build responsive layouts using Flexbox and Grid
- Apply media queries and responsive design principles
- Create CSS animations and transitions

---

## 1.1 HTML5 Semantic Elements

> [!important] What is HTML5 Semantics?
> ==Semantic HTML== means using elements that convey **meaning** about their content - not just presentation. This improves accessibility, SEO, and code readability.

### The Old vs New Way

**Before HTML5:**
```html
<div id="header"> ... </div>
<div id="nav"> ... </div>
<div id="main"> ... </div>
<div id="footer"> ... </div>
```

**With HTML5 Semantics:**
```html
<header> ... </header>
<nav> ... </nav>
<main>
  <section> ... </section>
  <article> ... </article>
  <aside> ... </aside>
</main>
<footer> ... </footer>
```

### Key Semantic Elements

| Element | Purpose | Usage |
|---------|---------|-------|
| `<header>` | Introductory content, logo, navigation | Page/section header |
| `<nav>` | Navigation links | Main menu, breadcrumbs |
| `<main>` | Dominant content (one per page) | Central page content |
| `<section>` | Thematic grouping of content | Chapters, tabs |
| `<article>` | Self-contained content | Blog post, news item |
| `<aside>` | Tangentially related content | Sidebar, pull quotes |
| `<footer>` | Footer information | Copyright, links |
| `<figure>` | Self-contained media | Images with captions |
| `<figcaption>` | Caption for `<figure>` | Image description |
| `<time>` | Machine-readable date/time | `<time datetime="2026-06-16">` |
| `<mark>` | Highlighted/marked text | Search highlights |
| `<details>` / `<summary>` | Expandable content | FAQ accordion |

### Complete Semantic Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Semantic HTML5 Page</title>
</head>
<body>
  <header>
    <h1>My Website</h1>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section id="featured">
      <h2>Featured Articles</h2>
      <article>
        <header>
          <h3>Article Title</h3>
          <time datetime="2026-06-16">June 16, 2026</time>
        </header>
        <p>Article content goes here...</p>
        <footer>
          <p>Author: John Doe</p>
        </footer>
      </article>
    </section>

    <aside>
      <h2>Related Links</h2>
      <ul>
        <li><a href="#">Related Article 1</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2026 My Website. All rights reserved.</p>
  </footer>
</body>
</html>
```

^html5-semantic-structure

---

## 1.2 CSS Fundamentals - The Box Model

> [!important] The Box Model
> ==Every HTML element== is rendered as a rectangular box consisting of four layers:

```
┌─────────────────────────────────┐
│           MARGIN                │
│  ┌───────────────────────────┐  │
│  │         BORDER            │  │
│  │  ┌─────────────────────┐  │  │
│  │  │       PADDING       │  │  │
│  │  │  ┌───────────────┐  │  │  │
│  │  │  │    CONTENT    │  │  │  │
│  │  │  │  width×height │  │  │  │
│  │  │  └───────────────┘  │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

### Box Model Properties

```css
.box {
  /* Content */
  width: 300px;
  height: 200px;
  
  /* Padding (space inside border) */
  padding: 20px;           /* all sides */
  padding: 10px 20px;      /* top/bottom left/right */
  padding: 10px 15px 20px 25px; /* top right bottom left */
  
  /* Border */
  border: 2px solid #333;
  border-radius: 8px;
  
  /* Margin (space outside border) */
  margin: 10px auto;       /* centered horizontally */
}
```

### `box-sizing` Property

> [!tip] Critical: `box-sizing`
> By default, `width` only sets the content area. Use `box-sizing: border-box` to include padding and border in the width.

```css
/* Default (content-box): total width = 300 + 40 + 4 = 344px */
.default {
  width: 300px;
  padding: 20px;
  border: 2px solid black;
  box-sizing: content-box; /* default */
}

/* Border-box: total width = 300px (padding/border included) */
.better {
  width: 300px;
  padding: 20px;
  border: 2px solid black;
  box-sizing: border-box;  /* recommended */
}

/* Universal reset (best practice) */
*, *::before, *::after {
  box-sizing: border-box;
}
```

^box-sizing-tip

---

## 1.3 CSS Selectors

### Selector Reference Table

| Selector Type | Syntax | Description | Example |
|--------------|--------|-------------|---------|
| Type/Element | `p` | All `<p>` elements | `p { color: red; }` |
| Class | `.classname` | Elements with class | `.btn { ... }` |
| ID | `#idname` | Specific element by ID | `#header { ... }` |
| Universal | `*` | All elements | `* { margin: 0; }` |
| Attribute | `[attr]` | Has attribute | `[disabled] { ... }` |
| Attribute Value | `[attr=val]` | Exact value | `[type="text"] { ... }` |
| Attribute Contains | `[attr*=val]` | Contains value | `[class*="btn"] { ... }` |
| Attribute Starts | `[attr^=val]` | Starts with | `[href^="https"] { ... }` |
| Attribute Ends | `[attr$=val]` | Ends with | `[src$=".png"] { ... }` |
| Descendant | `A B` | B inside A | `div p { ... }` |
| Child | `A > B` | Direct child | `ul > li { ... }` |
| Adjacent Sibling | `A + B` | Immediately after A | `h2 + p { ... }` |
| General Sibling | `A ~ B` | After A, same parent | `h2 ~ p { ... }` |
| Pseudo-class | `:hover` | State-based | `a:hover { ... }` |
| Pseudo-element | `::before` | Virtual element | `p::first-line { ... }` |

### Common Pseudo-Classes

```css
/* Link states */
a:link    { color: blue; }
a:visited { color: purple; }
a:hover   { color: red; }
a:active  { color: orange; }

/* Form states */
input:focus    { border-color: blue; }
input:disabled { opacity: 0.5; }
input:checked  { /* for checkboxes */ }
input:valid    { border-color: green; }
input:invalid  { border-color: red; }

/* Structural pseudo-classes */
li:first-child  { font-weight: bold; }
li:last-child   { margin-bottom: 0; }
li:nth-child(2) { background: yellow; }
li:nth-child(odd)  { background: #f0f0f0; }
li:nth-child(even) { background: #fff; }
li:nth-child(3n)   { /* every 3rd */ }

/* Negation */
p:not(.special) { color: gray; }
```

### Pseudo-Elements

```css
/* First letter of paragraph */
p::first-letter {
  font-size: 2em;
  font-weight: bold;
  float: left;
}

/* First line */
p::first-line { font-style: italic; }

/* Generated content */
.quote::before { content: '"'; }
.quote::after  { content: '"'; }

/* Custom selection highlight */
::selection {
  background-color: yellow;
  color: black;
}
```

### CSS Specificity

> [!warning] Specificity Rules
> When multiple rules apply to the same element, specificity determines which wins.

```
Specificity = (inline styles, ID, class/attr/pseudo-class, element/pseudo-element)
              (  1000,         100,  10,                     1)

Examples:
style=""           → 1000
#header            → 100
.nav               → 10
a:hover            → 11  (element=1, pseudo-class=10)
div.nav > a        → 12  (div=1, .nav=10, a=1)
```

---

## 1.4 CSS Flexbox

> [!important] Flexbox
> ==Flexbox== (Flexible Box Layout) is a one-dimensional layout method for arranging items in rows or columns.

### Flex Container Properties

```css
.container {
  display: flex;                    /* or inline-flex */
  
  /* Direction */
  flex-direction: row;              /* row | row-reverse | column | column-reverse */
  
  /* Wrapping */
  flex-wrap: nowrap;                /* nowrap | wrap | wrap-reverse */
  
  /* Shorthand for direction + wrap */
  flex-flow: row wrap;
  
  /* Alignment along main axis */
  justify-content: flex-start;     /* flex-start | flex-end | center | space-between | space-around | space-evenly */
  
  /* Alignment along cross axis */
  align-items: stretch;            /* stretch | flex-start | flex-end | center | baseline */
  
  /* Multi-line alignment */
  align-content: flex-start;       /* (when flex-wrap: wrap) */
  
  /* Spacing between items */
  gap: 10px;
  row-gap: 10px;
  column-gap: 20px;
}
```

### Flex Item Properties

```css
.item {
  /* Order (default: 0) */
  order: 2;
  
  /* Grow factor (how much to grow) */
  flex-grow: 1;
  
  /* Shrink factor (how much to shrink) */
  flex-shrink: 1;
  
  /* Base size before grow/shrink */
  flex-basis: 200px;
  
  /* Shorthand */
  flex: 1 1 200px;   /* grow shrink basis */
  flex: 1;           /* flex-grow: 1, flex-shrink: 1, flex-basis: 0% */
  flex: auto;        /* flex-grow: 1, flex-shrink: 1, flex-basis: auto */
  
  /* Override container align-items for this item */
  align-self: center;
}
```

### Flexbox Layout Example

```css
/* Navigation bar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  background: #333;
}

/* Card layout */
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.card {
  flex: 1 1 300px;   /* each card is at least 300px wide */
  max-width: 400px;
}

/* Centering anything */
.centered {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
```

### Flexbox Visual Reference

```
flex-direction: row
┌────────────────────────────────────────┐
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│ │  1   │ │  2   │ │  3   │ │  4   │  │  ← main axis →
│ └──────┘ └──────┘ └──────┘ └──────┘  │
└────────────────────────────────────────┘

justify-content values (main axis):
flex-start:   [1][2][3]          
center:       [  [1][2][3]  ]
flex-end:          [1][2][3]
space-between:[1]  [2]  [3]
space-around: [ 1 ][ 2 ][ 3 ]
space-evenly: [  1  ][  2  ][  3  ]
```

^flexbox-reference

---

## 1.5 CSS Grid

> [!important] CSS Grid
> ==CSS Grid== is a two-dimensional layout system, handling both rows AND columns simultaneously.

### Grid Container Properties

```css
.grid-container {
  display: grid;
  
  /* Define columns */
  grid-template-columns: 200px 1fr 1fr;    /* fixed + flexible */
  grid-template-columns: repeat(3, 1fr);   /* 3 equal columns */
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); /* responsive */
  
  /* Define rows */
  grid-template-rows: 100px auto 100px;
  
  /* Grid template areas */
  grid-template-areas:
    "header  header  header"
    "sidebar content content"
    "footer  footer  footer";
  
  /* Gaps */
  gap: 20px;
  row-gap: 10px;
  column-gap: 20px;
  
  /* Alignment of all items */
  justify-items: stretch;    /* start | end | center | stretch */
  align-items: stretch;
  
  /* Alignment of grid in container */
  justify-content: start;
  align-content: start;
}
```

### Grid Item Properties

```css
.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.content { grid-area: content; }
.footer  { grid-area: footer; }

/* Manual placement */
.item {
  grid-column: 1 / 3;      /* from line 1 to line 3 */
  grid-row: 2 / 4;
  
  /* Span shorthand */
  grid-column: span 2;      /* span 2 columns */
  
  /* Self alignment */
  justify-self: center;
  align-self: end;
}
```

### Grid Layout Example

```css
/* Classic 3-column layout */
.page-layout {
  display: grid;
  grid-template-columns: 250px 1fr 200px;
  grid-template-rows: 80px 1fr 60px;
  grid-template-areas:
    "header  header  header"
    "sidebar content aside"
    "footer  footer  footer";
  min-height: 100vh;
  gap: 20px;
}

/* Responsive card grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}
```

```html
<div class="page-layout">
  <header style="grid-area: header">Header</header>
  <nav style="grid-area: sidebar">Sidebar</nav>
  <main style="grid-area: content">Main Content</main>
  <aside style="grid-area: aside">Aside</aside>
  <footer style="grid-area: footer">Footer</footer>
</div>
```

^grid-layout-example

---

## 1.6 Responsive Design & Media Queries

> [!important] Responsive Web Design (RWD)
> ==Responsive design== ensures a website looks and works well on all screen sizes - from mobile phones to 4K monitors.

### Core Principles

1. **Fluid Layouts** - Use percentages/`fr` instead of fixed pixels
2. **Flexible Images** - `max-width: 100%` prevents overflow
3. **Media Queries** - Apply different CSS at different screen widths
4. **Mobile-First** - Start with mobile styles, then scale up

### Viewport Meta Tag (Required!)

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

> [!warning] Without this tag, mobile browsers will render at desktop width and then zoom out, breaking responsive layouts!

### Media Query Syntax

```css
/* Basic syntax */
@media media-type and (condition) {
  /* CSS rules */
}

/* Common breakpoints (Mobile-first) */
/* Mobile: default (no media query) */
.container { width: 100%; }

/* Tablet: 768px and up */
@media (min-width: 768px) {
  .container { width: 750px; }
  .card { width: 48%; }
}

/* Desktop: 1024px and up */
@media (min-width: 1024px) {
  .container { width: 960px; }
  .card { width: 30%; }
}

/* Large screens: 1440px and up */
@media (min-width: 1440px) {
  .container { max-width: 1200px; margin: 0 auto; }
}

/* Print styles */
@media print {
  .no-print { display: none; }
  body { font-size: 12pt; }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  body { background: #1a1a1a; color: #fff; }
}

/* Landscape orientation */
@media (orientation: landscape) { ... }

/* High resolution screens */
@media (-webkit-min-device-pixel-ratio: 2) { ... }
```

### Common Breakpoints (Industry Standard)

| Breakpoint | Size | Target |
|-----------|------|--------|
| xs | < 576px | Small phones |
| sm | ≥ 576px | Large phones |
| md | ≥ 768px | Tablets |
| lg | ≥ 992px | Desktops |
| xl | ≥ 1200px | Large desktops |
| xxl | ≥ 1400px | Extra-large screens |

### Responsive Navigation Example

```css
/* Mobile: hamburger menu */
.nav-links { display: none; }
.hamburger { display: block; }

/* Tablet and above: full nav */
@media (min-width: 768px) {
  .nav-links {
    display: flex;
    gap: 20px;
    list-style: none;
  }
  .hamburger { display: none; }
}
```

---

## 1.7 CSS Animations & Transitions

### CSS Transitions

> [!tip] Transitions
> ==Transitions== animate property changes smoothly from one state to another.

```css
/* Syntax: transition: property duration timing-function delay */
.btn {
  background-color: blue;
  color: white;
  padding: 10px 20px;
  
  /* Single property */
  transition: background-color 0.3s ease;
  
  /* Multiple properties */
  transition: background-color 0.3s ease,
              transform 0.2s ease-in-out,
              box-shadow 0.3s ease;
  
  /* All properties */
  transition: all 0.3s ease;
}

.btn:hover {
  background-color: darkblue;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
```

### Timing Functions

| Function | Description |
|----------|-------------|
| `ease` | Slow → Fast → Slow (default) |
| `linear` | Constant speed |
| `ease-in` | Slow start |
| `ease-out` | Slow end |
| `ease-in-out` | Slow start and end |
| `cubic-bezier(x1,y1,x2,y2)` | Custom curve |
| `steps(n)` | Stepped animation |

### CSS Animations with @keyframes

```css
/* Define the animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-30px); }
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

@keyframes colorChange {
  0%   { background-color: red; }
  33%  { background-color: green; }
  66%  { background-color: blue; }
  100% { background-color: red; }
}

/* Apply the animation */
.hero-text {
  animation-name: fadeIn;
  animation-duration: 1s;
  animation-timing-function: ease-out;
  animation-delay: 0.5s;
  animation-iteration-count: 1;     /* or infinite */
  animation-direction: normal;      /* normal | reverse | alternate */
  animation-fill-mode: forwards;    /* none | forwards | backwards | both */
  
  /* Shorthand */
  animation: fadeIn 1s ease-out 0.5s 1 normal forwards;
}

.loader {
  animation: spin 1s linear infinite;
}

.card:hover {
  animation: bounce 0.5s ease alternate 2;
}
```

### Transform Properties

```css
.element {
  /* Translate */
  transform: translateX(50px);
  transform: translateY(-20px);
  transform: translate(50px, -20px);
  
  /* Scale */
  transform: scale(1.5);         /* uniform scale */
  transform: scaleX(2);          /* horizontal only */
  
  /* Rotate */
  transform: rotate(45deg);
  transform: rotate3d(1, 1, 0, 45deg);
  
  /* Skew */
  transform: skew(10deg, 5deg);
  
  /* Multiple transforms */
  transform: translateY(-5px) scale(1.05) rotate(2deg);
  
  /* Origin point */
  transform-origin: center;
  transform-origin: top left;
  transform-origin: 50% 50%;
}
```

---

## Interview Questions - Unit 1

> [!question] Commonly Asked Questions

1. **What is the difference between `<section>`, `<article>`, and `<div>`?**
   - `<article>`: Self-contained, syndication-ready content (blog post, news)
   - `<section>`: Thematic grouping; needs a heading; part of the page
   - `<div>`: No semantic meaning; used for styling/scripting grouping

2. **Explain the CSS Box Model. What is `box-sizing: border-box`?**
   - Box Model = content + padding + border + margin
   - `content-box` (default): width = content only
   - `border-box`: width = content + padding + border (easier to calculate)

3. **What is specificity? How do you resolve conflicts?**
   - Specificity: inline(1000) > ID(100) > class/attr(10) > element(1)
   - Use `!important` as last resort; prefer more specific selectors

4. **Flexbox vs CSS Grid - when to use which?**
   - **Flexbox**: 1D layout (a row OR a column); navigation bars, card rows
   - **Grid**: 2D layout (rows AND columns); full-page layouts

5. **What is a media query? Write one for tablet view.**
   ```css
   @media (min-width: 768px) and (max-width: 1023px) {
     .container { width: 740px; }
   }
   ```

6. **Difference between `transition` and `animation`?**
   - `transition`: Triggered by state change (hover, focus); needs a trigger
   - `animation`: Runs automatically; uses `@keyframes`; more control

7. **What is `flex: 1` shorthand for?**
   - `flex: 1` = `flex-grow: 1; flex-shrink: 1; flex-basis: 0%`

8. **What does `position: sticky` do?**
   - Element is positioned relative until it reaches a threshold, then acts as fixed

---

## Revision Summary

> [!summary] Unit 1 Key Takeaways
> 
> **HTML5 Semantics:**
> - Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` for meaningful structure
> - One `<main>` per page; `<article>` is self-contained; `<section>` needs a heading
> 
> **Box Model:**
> - Content → Padding → Border → Margin
> - Always use `box-sizing: border-box` as a reset
> 
> **Selectors:**
> - Specificity: inline > ID > class > element
> - Combinators: descendant (space), child (>), sibling (+, ~)
> 
> **Flexbox (1D):**
> - Container: `display:flex`, `justify-content`, `align-items`, `flex-direction`
> - Items: `flex-grow`, `flex-shrink`, `flex-basis`, `align-self`
> 
> **Grid (2D):**
> - `grid-template-columns`, `grid-template-rows`, `grid-template-areas`
> - `repeat()`, `fr` unit, `minmax()`, `auto-fill`
> 
> **Responsive Design:**
> - Always add viewport meta tag
> - Mobile-first: start with mobile, add `min-width` media queries
> - Common breakpoints: 576px, 768px, 992px, 1200px
> 
> **Animations:**
> - `transition`: State-based, smooth change; `animation` + `@keyframes`: auto-running

^unit1-revision

---

*[[Overview|CS-303 Overview]] | Next: [[Unit-2]] →*
