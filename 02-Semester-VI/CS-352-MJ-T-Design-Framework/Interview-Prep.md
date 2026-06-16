---
title: "CS-352 Angular Interview Prep"
tags: [cs-352, angular, interview]
---

# Angular Interview Preparation

1. **What is the difference between Angular and AngularJS?**
   Angular is TypeScript-based, component-driven. AngularJS is JS-based, MVC architecture.
2. **Explain the Angular application lifecycle.**
   ngOnChanges, ngOnInit, ngDoCheck, ngAfterContentInit, ngAfterContentChecked, ngAfterViewInit, ngAfterViewChecked, ngOnDestroy.
3. **What are Observables?**
   Used to handle asynchronous operations. More powerful than Promises (can be canceled, emit multiple values).
4. **What is Lazy Loading?**
   Loading feature modules only when their route is accessed, improving initial load time.
5. **How does Dependency Injection work in Angular?**
   Providers configure injectors. When a component requests a service, the injector provides it.
