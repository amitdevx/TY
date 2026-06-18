---
title: "CS-355 Viva 3"
---

[[CS-355-Assignment-3|Back to Assignment 3]]

## 5. Viva Questions
1. **What is an `EventEmitter`?**
   A class used to emit custom events synchronously or asynchronously, typically used with the `@Output()` decorator.
2. **Which lifecycle hook fires first: `ngOnInit` or `ngOnChanges`?**
   `ngOnChanges` fires first (if there are bound input properties), followed immediately by `ngOnInit`.
3. **Why do we need `ngOnDestroy`?**
   To avoid memory leaks by cleaning up resources, like unsubscribing from Observables or detaching event handlers.