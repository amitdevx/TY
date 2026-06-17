---
title: "CS-352 Design Framework (Angular) Revision"
tags: [cs-352, angular, frontend, framework, semester-vi, revision]
subject_code: CS-352-MJ-T
type: revision
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Design Framework (Angular) - Quick Revision Summary

> [!tip] How to use this guide
> Review this page for a rapid recall of all Angular concepts. Focus heavily on Data Binding, Decorators, and Services for exams.

---

## 1. Angular Architecture & Basics

- **Angular vs AngularJS:** Angular is a complete rewrite using TypeScript, component-based, faster, and mobile-oriented. AngularJS is JavaScript-based and uses scope/controllers.
- **TypeScript:** A superset of JavaScript that adds static typing and OOP features. Transpiles to standard JS.
- **Core Building Blocks:** Modules, Components, Templates, Metadata, Data Binding, Directives, Services, Dependency Injection.

### Important CLI Commands
| Command | Purpose |
|---|---|
| `ng new <app-name>` | Create a new Angular workspace/app |
| `ng serve --open` | Build and serve the app locally, open browser |
| `ng generate component <name>` | Generate a new component (`ng g c <name>`) |
| `ng generate service <name>` | Generate a new service (`ng g s <name>`) |

---

## 2. Components and Data Binding

A component controls a patch of screen (a view). It consists of:
1. A TypeScript class (logic)
2. An HTML template (view)
3. A CSS file (styles)

### Data Binding Types

| Type | Syntax | Direction | Description |
|---|---|---|---|
| **Interpolation** | `{{ value }}` | Component $\rightarrow$ DOM | Evaluates expression and embeds in HTML |
| **Property Binding** | `[property]="value"` | Component $\rightarrow$ DOM | Sets an element property to a component value |
| **Event Binding** | `(event)="handler()"` | DOM $\rightarrow$ Component | Listens for DOM events and calls component method |
| **Two-Way Binding** | `[(ngModel)]="value"` | Component $\leftrightarrow$ DOM | Keeps property and input field in sync |

*(Note: Two-way binding requires importing `FormsModule`).*

---

## 3. Directives

Directives are classes that add new behavior to the elements in the template.

- **Component Directives:** Directives with a template.
- **Structural Directives:** Change the DOM layout by adding/removing elements. Prefix with `*`.
  - `*ngIf`: Conditionally includes a template.
  - `*ngFor`: Repeats a node for each item in a list.
  - `*ngSwitch`: Conditionally switches between multiple templates.
- **Attribute Directives:** Change the appearance or behavior of an element.
  - `ngClass`: Adds/removes CSS classes dynamically.
  - `ngStyle`: Adds/removes inline styles dynamically.

---

## 4. Routing and Navigation

Enables navigation from one view to the next as users perform application tasks.
- **RouterModule:** Module that provides routing services.
- **Routes Array:** Maps URL paths to components.
  `{ path: 'home', component: HomeComponent }`
- **RouterOutlet:** Directive (`<router-outlet>`) acting as a placeholder where router inserts components.
- **RouterLink:** Directive used to bind clickable HTML elements to a route.
  `<a routerLink="/home">Home</a>`

---

## 5. Services and Dependency Injection (DI)

- **Service:** A broad category encompassing any value, function, or feature that an app needs (e.g., fetching data, logging). Keeps components lean.
- **Dependency Injection (DI):** A design pattern where a class receives its dependencies from external sources rather than creating them itself.
- **`@Injectable()`:** Decorator marking a class as participating in the DI system. The `providedIn: 'root'` option creates a single, shared instance (singleton).

### HttpClient and Observables
- `HttpClientModule` is used to make HTTP requests (GET, POST, PUT, DELETE).
- Returns **Observables** (from RxJS library) instead of Promises.
- Observables emit multiple values over time. Must `.subscribe()` to them to execute the request.

---

## 6. Forms

| Feature | Template-Driven Forms | Reactive Forms |
|---|---|---|
| **Setup** | Import `FormsModule` | Import `ReactiveFormsModule` |
| **Logic Location** | HTML Template | Component Class |
| **Form Model** | Created automatically by Angular | Created explicitly in code (`FormGroup`, `FormControl`) |
| **Use Case** | Simple forms | Complex forms, dynamic validation |
| **Validation** | HTML5 attributes (`required`, `minlength`) | Custom Validator functions in class |

---

[[02-Semester-VI/CS-352-MJ-T-Design-Framework/Important-Questions|Important Questions]] | [[02-Semester-VI/CS-352-MJ-T-Design-Framework/Unit-1|Unit 1]]
