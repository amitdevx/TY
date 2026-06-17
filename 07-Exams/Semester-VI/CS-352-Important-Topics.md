---
title: "CS-352 Angular - Important Topics"
subject: CS-352
semester: VI
tags:
  - important-topics
  - angular
  - typescript
  - components
  - routing
  - forms
  - semester-vi
  - exam
aliases:
  - Angular Important
  - CS352 Must-Know
created: 2026-06-16
type: important-topics
---

[[00-Dashboard/Home|Home]] | [[07-Exams/Exams-Dashboard|Exams Dashboard]]


# CS-352 Angular - Important Topics

> [!important] Exam Focus
> Angular requires knowing both concepts and TypeScript code. Data binding, directives, services, and routing are the core. Reactive Forms with validation and lifecycle hooks are high-value topics.

---

## Top 10 Most Important Topics

| # | Topic | Description | Probability |
|---|-------|-------------|-------------|
| 1 | **Data Binding - All 4 Types** | Interpolation, Property, Event, Two-way |  |
| 2 | **Structural Directives** | `*ngIf`, `*ngFor`, `*ngSwitch` with examples |  |
| 3 | **Services + HttpClient** | `@Injectable`, GET/POST/PUT/DELETE API calls |  |
| 4 | **Angular Routing** | Routes, routerLink, params, wildcard |  |
| 5 | **Reactive Forms** | FormBuilder, FormGroup, Validators |  |
| 6 | **Lifecycle Hooks** | `ngOnInit`, `ngOnDestroy`, `ngOnChanges` |  |
| 7 | **@Input / @Output** | Parent-child component communication |  |
| 8 | **Template-Driven Forms** | `ngModel`, form validation in HTML |  |
| 9 | **Custom Directives** | `@Directive`, HostListener, ElementRef |  |
| 10 | **Lazy Loading** | `loadChildren` for performance optimization |  |

---

## Definitely Going to Come

> [!warning] Near-Certain Questions
> 1. **Data binding** - show all 4 types with code snippets
> 2. **`*ngFor` and `*ngIf`** - use in a list component
> 3. **Create a service** with HttpClient to fetch data from API
> 4. **Angular routing** - set up routes, use routerLink, read params
> 5. **Reactive Form** with at least 3 validators (required, email, minLength)
> 6. **Lifecycle hooks** - ngOnInit for API call, ngOnDestroy for cleanup
> 7. **@Input/@Output** - pass data from parent to child and emit back

---

## Must-Know Definitions

| Term | Definition |
|------|-----------|
| **Component** | Building block of Angular UI - has template, class, and styles |
| **Module** | Container for components, directives, pipes, services (`@NgModule`) |
| **Directive** | Instructions in the DOM - structural (change structure) or attribute (change appearance) |
| **Pipe** | Transform displayed data (date, currency, uppercase, custom) |
| **Service** | Business logic class - injectable, singleton by default |
| **DI** | Dependency Injection - Angular provides dependencies via constructor |
| **Observable** | RxJS stream - async data sequence that can be subscribed to |
| **Subject** | Observable + Observer - can both emit and subscribe |
| **Lazy Loading** | Load feature modules only when route is visited |
| **Guard** | Service that determines if route can be activated |

---

## Quick Code Patterns

### Component Skeleton
```typescript
@Component({
  selector: 'app-demo',
  template: `<h2>{{ title }}</h2>`,
  styleUrls: ['./demo.component.css']
})
export class DemoComponent implements OnInit {
  title = 'Demo';
  constructor(private service: DataService) {}
  ngOnInit() { /* fetch data */ }
}
```

### Service with HttpClient
```typescript
@Injectable({ providedIn: 'root' })
export class DataService {
  constructor(private http: HttpClient) {}
  getAll(): Observable<any[]> { return this.http.get<any[]>('/api/items'); }
  create(item: any): Observable<any> { return this.http.post('/api/items', item); }
}
```

### Reactive Form
```typescript
form = this.fb.group({
  name: ['', [Validators.required, Validators.minLength(3)]],
  email: ['', [Validators.required, Validators.email]]
});
// Template: [formGroup]="form", formControlName="name"
```

### Route Params
```typescript
// Define: { path: 'item/:id', component: ItemComponent }
// Navigate: this.router.navigate(['/item', id])
// Read: this.route.snapshot.paramMap.get('id')
```

---

## Angular Directives Quick Reference

| Directive | Type | Purpose |
|-----------|------|---------|
| `*ngIf` | Structural | Show/hide element |
| `*ngFor` | Structural | Repeat element for each item |
| `*ngSwitch` | Structural | Switch between views |
| `[ngClass]` | Attribute | Conditionally add CSS classes |
| `[ngStyle]` | Attribute | Conditionally add inline styles |
| `[(ngModel)]` | Attribute | Two-way binding (FormsModule) |
| `routerLink` | Attribute | Navigate to route |
| `routerLinkActive` | Attribute | Add class when route is active |

---

## Common Mistakes to Avoid

> [!warning] Avoid These Errors
> - **Forgetting to import HttpClientModule** in AppModule - `http.get()` won't work!
> - **FormsModule vs ReactiveFormsModule:** `ngModel` needs FormsModule; `FormGroup` needs ReactiveFormsModule.
> - **Memory leaks:** Always `unsubscribe()` in `ngOnDestroy()` or use `async` pipe.
> - **Using `*ngIf` and `*ngFor` on same element:** Not allowed! Use `<ng-container>` wrapper.
> - **Route `**` (wildcard) must be LAST** in routes array.
> - **`@Input()` data not available in constructor:** Use `ngOnChanges` or `ngOnInit` instead.
> - **`EventEmitter` output:** Don't forget `(eventName)="handler($event)"` in parent template.

---

## Angular CLI Commands

```bash
ng new my-app                        # Create new Angular app
ng generate component my-comp        # Create component
ng generate service my-service       # Create service
ng generate module my-module --route # Create lazy-loaded module
ng serve                             # Run dev server
ng build --prod                      # Production build
ng test                              # Run unit tests
```

---

*Tags: [[02-Semester-VI/CS-352-MJ-T-Design-Framework/Overview|Design Framework Overview]] | Semester VI | [[07-Exams/Exams-Dashboard|Exams]]*
