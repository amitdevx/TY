---
title: "CS-355 Viva 2"
---

[[CS-355-Assignment-2|Back to Assignment 2]]

## 5. Viva Questions
1. **How do you use `else` with `*ngIf`?**
   By assigning a template reference variable to an `<ng-template>` element and using `*ngIf="condition; else templateRef"`.
2. **What does the `currency` pipe do?**
   It formats a number as currency according to locale rules.
3. **Can you chain multiple pipes together?**
   Yes, by using the pipe operator multiple times: `{{ value | date | uppercase }}`.