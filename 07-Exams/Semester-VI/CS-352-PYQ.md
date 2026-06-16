---
title: "CS-352 Angular - Expected PYQ"
subject: CS-352
paper: Angular Framework
semester: VI
tags:
  - pyq
  - angular
  - components
  - directives
  - routing
  - forms
  - services
  - semester-vi
  - exam
aliases:
  - Angular PYQ
  - CS352 Questions
created: 2026-06-16
type: pyq
---

#  CS-352 Angular - Expected PYQ

> [!important] Exam Strategy
> Angular is TypeScript + framework concepts. Focus on components, directives, routing, both reactive and template-driven forms, and services with HttpClient. Know the lifecycle hooks.

---

## ️ Unit-wise Distribution

| Unit | Topic | Weightage |
|------|-------|-----------|
| I | Angular Architecture & Setup | 15% |
| II | Components & Templates | 25% |
| III | Directives & Pipes | 15% |
| IV | Services, DI & Routing | 25% |
| V | Forms & HTTP | 20% |

---

## ️ Section A - Short Answer (2 Marks)

1. **What is Angular? How is it different from AngularJS?**
2. **What is a component in Angular? List its parts.**
3. **What is data binding? List its four types.**
4. **What is the difference between `*ngIf` and `*ngFor`?**
5. **What are structural vs attribute directives?**
6. **What is a pipe in Angular? Name any four built-in pipes.**
7. **What is a service in Angular? Why is it used?**
8. **What is Dependency Injection in Angular?**
9. **What is Angular Router? What is a routing module?**
10. **Difference between template-driven forms and reactive forms.**
11. **What is `ngModel`? What module does it require?**
12. **What is HttpClient? What module does it belong to?**
13. **What is `Observable` in Angular?**
14. **What are lifecycle hooks in Angular? Name all eight.**
15. **What is `@Input()` and `@Output()`?**
16. **What is lazy loading in Angular routing?**
17. **What is a module in Angular (`@NgModule`)?**
18. **What is Angular CLI? Name 3 useful commands.**
19. **What is EventEmitter?**
20. **What is the difference between `subscribe()` and `async` pipe?**

---

##  Section B - Long Answer (5–7 Marks)

---

### Q1. Angular Architecture & Components ()

**Angular Architecture:**
```
AppModule (@NgModule)
├── Components (UI)
├── Services (Business Logic)
├── Directives (DOM Manipulation)
├── Pipes (Data Transformation)
└── Routing Module (Navigation)
```

**Creating and Using Components:**
```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',           // HTML tag to use this component
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'My Angular App';
  items = ['HTML', 'CSS', 'TypeScript'];
  isVisible = true;

  toggleVisibility() {
    this.isVisible = !this.isVisible;
  }
}
```

```html
<!-- app.component.html -->
<h1>{{ title }}</h1>

<!-- *ngIf -->
<p *ngIf="isVisible">This is visible!</p>
<button (click)="toggleVisibility()">Toggle</button>

<!-- *ngFor -->
<ul>
  <li *ngFor="let item of items; let i = index">{{ i + 1 }}. {{ item }}</li>
</ul>
```

---

### Q2. Data Binding - All Four Types ()

```typescript
// component.ts
export class DemoComponent {
  name = 'Amit';
  imageUrl = 'logo.png';
  value = '';

  onClick() { alert('Button clicked!'); }
}
```

```html
<!-- 1. Interpolation (one-way: Component → View) -->
<h2>{{ name }}</h2>

<!-- 2. Property Binding (one-way: Component → DOM Property) -->
<img [src]="imageUrl" [alt]="name">
<button [disabled]="value.length === 0">Submit</button>

<!-- 3. Event Binding (one-way: View → Component) -->
<button (click)="onClick()">Click Me</button>
<input (keyup)="onKey($event)">

<!-- 4. Two-Way Binding (requires FormsModule) -->
<input [(ngModel)]="name">
<p>Hello, {{ name }}!</p>
```

---

### Q3. Directives - Structural and Attribute ()

```html
<!-- Structural Directives (change DOM structure) -->
<div *ngIf="isLoggedIn; else loginBlock">
  <p>Welcome!</p>
</div>
<ng-template #loginBlock><p>Please login</p></ng-template>

<ul>
  <li *ngFor="let user of users; trackBy: trackById">
    {{ user.name }} - {{ user.age }}
  </li>
</ul>

<div [ngSwitch]="role">
  <p *ngSwitchCase="'admin'">Admin Panel</p>
  <p *ngSwitchCase="'user'">User Dashboard</p>
  <p *ngSwitchDefault>Guest View</p>
</div>

<!-- Attribute Directives (change appearance/behavior) -->
<p [ngClass]="{'active': isActive, 'error': hasError}">Styled Text</p>
<p [ngStyle]="{'color': textColor, 'font-size': fontSize + 'px'}">Styled</p>
```

**Custom Directive:**
```typescript
@Directive({ selector: '[appHighlight]' })
export class HighlightDirective {
  @Input('appHighlight') color: string = 'yellow';

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  @HostListener('mouseenter') onEnter() {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }

  @HostListener('mouseleave') onLeave() {
    this.renderer.removeStyle(this.el.nativeElement, 'backgroundColor');
  }
}
```

---

### Q4. Services and Dependency Injection ()

```typescript
// product.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'  // Singleton - available app-wide
})
export class ProductService {
  private apiUrl = 'https://api.example.com/products';

  constructor(private http: HttpClient) {}

  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  addProduct(product: any): Observable<any> {
    return this.http.post(this.apiUrl, product);
  }
}

// product.component.ts - Inject and Use
@Component({ /* ... */ })
export class ProductComponent implements OnInit {
  products: any[] = [];

  constructor(private productService: ProductService) {}

  ngOnInit() {
    this.productService.getProducts().subscribe(
      data => this.products = data,
      err => console.error(err)
    );
  }
}
```

---

### Q5. Angular Routing ()

```typescript
// app-routing.module.ts
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/:id', component: ProductDetailComponent },
  { path: '**', component: NotFoundComponent }  // wildcard
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

```html
<!-- app.component.html -->
<nav>
  <a routerLink="/" routerLinkActive="active">Home</a>
  <a routerLink="/about">About</a>
  <a routerLink="/products">Products</a>
</nav>
<router-outlet></router-outlet>
```

```typescript
// product-detail.component.ts - Read route params
constructor(private route: ActivatedRoute) {}

ngOnInit() {
  const id = this.route.snapshot.paramMap.get('id');
}
```

**Lazy Loading:**
```typescript
{ path: 'admin', loadChildren: () =>
    import('./admin/admin.module').then(m => m.AdminModule) }
```

---

### Q6. Angular Forms - Template-Driven vs Reactive ()

**Template-Driven Form:**
```html
<!-- Requires FormsModule -->
<form #loginForm="ngForm" (ngSubmit)="onSubmit(loginForm)">
  <input type="text" name="username" ngModel required minlength="3">
  <div *ngIf="loginForm.controls['username']?.invalid && loginForm.submitted">
    Username is required (min 3 chars)
  </div>
  <input type="password" name="password" ngModel required>
  <button type="submit">Login</button>
</form>
```

**Reactive Form:**
```typescript
// Requires ReactiveFormsModule
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

export class RegisterComponent {
  form: FormGroup;

  constructor(private fb: FormBuilder) {
    this.form = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]]
    });
  }

  onSubmit() {
    if (this.form.valid) console.log(this.form.value);
  }
}
```

```html
<form [formGroup]="form" (ngSubmit)="onSubmit()">
  <input formControlName="name">
  <div *ngIf="form.get('name')?.hasError('required')">Name required</div>
  <input formControlName="email">
  <button type="submit" [disabled]="form.invalid">Register</button>
</form>
```

---

### Q7. Lifecycle Hooks ()

| Hook | When Called | Common Use |
|------|-------------|------------|
| `ngOnChanges` | Input property changes | React to parent changes |
| `ngOnInit` | After first ngOnChanges | Initialize data, API calls |
| `ngDoCheck` | Every change detection | Custom change detection |
| `ngAfterContentInit` | After content projection | Access projected content |
| `ngAfterContentChecked` | After content check | Respond to content changes |
| `ngAfterViewInit` | After view initialized | Access child components |
| `ngAfterViewChecked` | After view check | Respond to view changes |
| `ngOnDestroy` | Before component destroyed | Cleanup subscriptions |

```typescript
export class LifecycleDemo implements OnInit, OnDestroy {
  subscription: Subscription;

  ngOnInit() {
    this.subscription = this.service.getData().subscribe(/* ... */);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe(); // prevent memory leaks!
  }
}
```

---

### Q8. Parent-Child Communication ()

```typescript
// parent.component.ts
export class ParentComponent {
  parentMessage = "Hello from Parent";
  childMessage = '';

  receiveFromChild(msg: string) { this.childMessage = msg; }
}

// child.component.ts
export class ChildComponent {
  @Input() message: string = '';           // Receive from parent
  @Output() messageEvent = new EventEmitter<string>(); // Send to parent

  sendToParent() {
    this.messageEvent.emit("Hello from Child!");
  }
}
```

```html
<!-- parent template -->
<app-child [message]="parentMessage" (messageEvent)="receiveFromChild($event)">
</app-child>

<!-- child template -->
<p>{{ message }}</p>
<button (click)="sendToParent()">Send to Parent</button>
```

---

##  Most Expected Questions

> [!tip] High Probability
> 1.  Data binding - all 4 types with code
> 2.  *ngIf, *ngFor, *ngSwitch usage
> 3.  Service with HttpClient - CRUD operations
> 4.  Angular routing with parameters
> 5.  Reactive form with validators
> 6.  Lifecycle hooks - ngOnInit & ngOnDestroy
> 7.  @Input / @Output for parent-child communication

---

*Tags: [[Angular|CS-352 Angular]] | Semester VI | [[07-Exams]]*
