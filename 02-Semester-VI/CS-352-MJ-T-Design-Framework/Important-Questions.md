---
title: "CS-352 Design Framework (Angular) Important Questions"
tags: [cs-352, angular, frontend, exams, semester-vi]
subject_code: CS-352-MJ-T
type: important-questions
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Design Framework (Angular) - Important Questions

> [!summary] About
> Highly probable exam questions for CS-352 (University Exam: 35 Marks). Focused on Angular concepts.

---

## Section A: Short Answer Questions (2 Marks)

1. Define Single Page Application (SPA).
2. What is TypeScript? Why is it used in Angular?
3. State the purpose of the `ngOnInit()` lifecycle hook.
4. List the four types of data binding available in Angular.
5. Differentiate between `*ngIf` and `hidden` attribute.
6. What is a structural directive? Give an example.
7. What is the role of `RouterModule` in Angular?
8. Define Dependency Injection.
9. What is the difference between a Promise and an Observable?
10. Name the two modules required for Template-driven and Reactive forms.

---

## Section B: Medium Answer Questions (5 Marks)

11. Explain the architecture of an Angular application with a block diagram.
12. Discuss the difference between Angular and AngularJS.
13. Explain the component lifecycle hooks in detail with their execution sequence.
14. What are decorators in Angular? Explain `@Component` and `@NgModule` with code snippets.
15. How does component communication happen? Explain `@Input()` and `@Output()` with an example.
16. Explain Structural Directives (`*ngIf`, `*ngFor`, `*ngSwitch`) with suitable code examples.
17. What are pipes in Angular? Explain any three built-in pipes.
18. Explain the concept of Route Guards. Why are they used?
19. Discuss Dependency Injection in Angular. How do you create and inject a service?
20. Compare Template-driven forms with Reactive forms.

---

## Section C: Long Answer / Programming Questions (7-10 Marks)
*(Depending on paper pattern, these might be split into 5-mark segments)*

21. **Angular Application Design:**
    Write an Angular component (HTML and TS) to accept a student's Roll Number, Name, and Marks using Two-Way data binding. Display the details in a tabular format below the form upon clicking an "Add Student" button.
    
22. **Services and HTTP:**
    Write an Angular Service using `HttpClient` to fetch user data from a REST API (`https://jsonplaceholder.typicode.com/users`). Create a component that injects this service and displays the list of users using `*ngFor`.

23. **Reactive Forms:**
    Design a Reactive Form for User Registration containing fields: Username, Email, and Password. Implement the following validations:
    - Username: Required, min length 3.
    - Email: Required, valid email format.
    - Password: Required, min length 6.
    Display appropriate error messages if validation fails.

---

[[02-Semester-VI/CS-352-MJ-T-Design-Framework/Revision|Revision Summary]] | [[02-Semester-VI/CS-352-MJ-T-Design-Framework/Interview-Prep|Interview Prep]]
