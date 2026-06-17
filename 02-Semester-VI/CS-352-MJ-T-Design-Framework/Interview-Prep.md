---
title: "CS-352 Design Framework (Angular) Interview Preparation"
tags: [cs-352, angular, frontend, interview, semester-vi]
subject_code: CS-352-MJ-T
type: interview-prep
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Design Framework (Angular) Interview Preparation

> [!summary] About
> Top 20+ Angular interview questions. Essential for frontend developer roles and campus placements.

---

## 1. Angular Basics

> [!question] 1. What is Angular?
> Angular is a TypeScript-based open-source web application framework led by the Angular Team at Google. It is used for building single-page client applications (SPAs) using HTML and TypeScript.

> [!question] 2. What is the difference between Angular and AngularJS?
> - **AngularJS (v1.x):** Based on JavaScript, uses a scope/controller architecture, not inherently mobile-friendly, uses two-way binding heavily.
> - **Angular (v2+):** Based on TypeScript, uses a component-based architecture, mobile-oriented, faster, uses both one-way and two-way binding.

> [!question] 3. What are Angular Decorators?
> Decorators are core features of TypeScript used by Angular to store metadata about a class, method, or property. They modify the behavior of the element they decorate.
> Examples: `@Component()`, `@NgModule()`, `@Injectable()`, `@Input()`, `@Output()`.

---

## 2. Components & Data Binding

> [!question] 4. Explain the component lifecycle hooks.
> Angular manages the creation, rendering, data-binding, and destruction of components.
> Key hooks (in execution order):
> 1. `ngOnChanges()`: Called when an input/output binding value changes.
> 2. `ngOnInit()`: Called after the first `ngOnChanges`. Used for initialization logic (fetching data).
> 3. `ngDoCheck()`: Developer's custom change detection.
> 4. `ngAfterViewInit()`: Called after component's view has been initialized.
> 5. `ngOnDestroy()`: Called just before Angular destroys the component. Used to unsubscribe from Observables and detach event handlers to avoid memory leaks.

> [!question] 5. What are the four types of Data Binding in Angular?
> 1. **String Interpolation:** `{{ data }}` (Component to DOM)
> 2. **Property Binding:** `[property]="data"` (Component to DOM)
> 3. **Event Binding:** `(event)="handler()"` (DOM to Component)
> 4. **Two-Way Binding:** `[(ngModel)]="data"` (Syncs both ways, requires `FormsModule`)

> [!question] 6. How do components communicate with each other?
> - **Parent to Child:** Using the `@Input()` decorator.
> - **Child to Parent:** Using the `@Output()` decorator with `EventEmitter`.
> - **Unrelated Components:** Using a shared Service with RxJS `Subject` or `BehaviorSubject`.

---

## 3. Directives & Pipes

> [!question] 7. What is the difference between Structural and Attribute Directives?
> - **Structural Directives:** Alter the DOM layout by adding, removing, or replacing elements. Always prefixed with `*`. Examples: `*ngIf`, `*ngFor`.
> - **Attribute Directives:** Alter the appearance or behavior of an existing DOM element. Examples: `ngClass`, `ngStyle`.

> [!question] 8. What are Pipes? Mention some built-in pipes.
> Pipes are simple functions to use in template expressions to accept an input value and return a transformed value (e.g., formatting dates or currency).
> Syntax: `{{ data | pipeName }}`
> Examples: `DatePipe`, `UpperCasePipe`, `LowerCasePipe`, `CurrencyPipe`, `AsyncPipe`.

---

## 4. Services, DI, and Routing

> [!question] 9. What is Dependency Injection (DI) in Angular?
> DI is a design pattern in which a class requests dependencies from external sources rather than creating them. In Angular, the DI framework provides declared dependencies to a class when that class is instantiated (usually through the constructor).

> [!question] 10. What does the `@Injectable({ providedIn: 'root' })` decorator do?
> It tells Angular that the service is available globally across the application. Angular creates a single, shared instance (singleton) of this service and injects it into any class that asks for it.

> [!question] 11. What is a Router in Angular?
> The Angular Router enables navigation from one view to the next as users perform application tasks. It interprets a browser URL as an instruction to navigate to a client-generated view.

> [!question] 12. What are Route Guards?
> Route Guards are interfaces used to control access to a route. They return a boolean (or Observable/Promise resolving to a boolean) determining if navigation is allowed.
> Examples: `CanActivate`, `CanDeactivate`, `Resolve`.

---

## 5. Observables & Forms

> [!question] 13. Observable vs Promise
> - **Promise:** Emits a single value, executes immediately, not cancellable.
> - **Observable:** Can emit multiple values over time, executes only when subscribed to (lazy), can be cancelled using `.unsubscribe()`, provides operators like `map`, `filter`, `retry`.

> [!question] 14. Template-Driven vs Reactive Forms
> - **Template-Driven:** Relies heavily on directives in the HTML template. Angular creates the form object automatically. Best for simple forms. Uses `FormsModule`.
> - **Reactive Forms:** Form logic is written in the component TypeScript class. More scalable, reusable, and testable. Best for complex forms with dynamic validation. Uses `ReactiveFormsModule`.

---

[[02-Semester-VI/CS-352-MJ-T-Design-Framework/Revision|Revision Summary]] | [[02-Semester-VI/CS-352-MJ-T-Design-Framework/Important-Questions|Important Questions]]
