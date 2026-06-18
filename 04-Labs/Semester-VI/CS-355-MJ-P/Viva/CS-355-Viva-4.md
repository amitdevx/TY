---
title: "CS-355 Viva 4"
---

[[CS-355-Assignment-4|Back to Assignment 4]]

## 5. Viva Questions
1. **What is `FormBuilder`?**
   A service that provides syntactic sugar to reduce boilerplate when creating `FormGroups`, `FormControls`, and `FormArrays`.
2. **How do you access the validation status of a form group?**
   By checking the `valid` or `invalid` property (e.g., `this.registerForm.valid`).
3. **What is the difference between `touched` and `dirty` in form controls?**
   - `touched`: The user has blurred (lost focus) the form control element.
   - `dirty`: The user has changed the value in the form control.