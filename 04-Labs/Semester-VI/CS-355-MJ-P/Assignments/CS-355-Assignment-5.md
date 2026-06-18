---
title: "Assignment 5: Services, DI, and Routing"
aliases: [Assignment 5]
tags: [lab, angular, assignment, services, routing, http]
---

[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 5: Services, Dependency Injection, and Routing

## 1. Problem Statement / Aim
To implement a multi-page Angular application. You will create an Injectable Service to fetch mock data, implement Dependency Injection, and use the Angular Router to navigate between a "Home" component and a "Details" component.

## 2. Theory & Concept

### Services and Dependency Injection (DI)
- **Services**: Classes with a specific, well-defined purpose. They are used to share data, business logic, or functions across multiple components.
- **Dependency Injection**: Angular's mechanism for providing a component with the services it needs without the component having to instantiate them. The `@Injectable()` decorator is used to mark a service.

### Routing
Angular Router enables navigation from one view to the next as users perform application tasks.
- `RouterModule.forRoot(routes)`: Configures the router at the application's root level.
- `routerLink`: A directive to bind a clickable HTML element to a route.
- `<router-outlet>`: A placeholder directive that tells the router where to insert the matched component.

## 3. Fully Solved TypeScript/HTML Code

### **Step 1: The Service (`data.service.ts`)**
Generate using `ng generate service data`.
```typescript
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root' // Service is a singleton accessible everywhere
})
export class DataService {
  private users = [
    { id: 1, name: 'Alice', role: 'Admin' },
    { id: 2, name: 'Bob', role: 'Editor' },
    { id: 3, name: 'Charlie', role: 'Subscriber' }
  ];

  constructor() { }

  getUsers() {
    return this.users;
  }

  getUserById(id: number) {
    return this.users.find(user => user.id === id);
  }
}
```

### **Step 2: Home Component (`home.component.ts` & `.html`)**
```typescript
import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-home',
  template: `
    <h2>User List</h2>
    <ul>
      <li *ngFor="let user of users">
        {{ user.name }} 
        <button [routerLink]="['/user', user.id]">View Details</button>
      </li>
    </ul>
  `
})
export class HomeComponent implements OnInit {
  users: any[] = [];
  // Injecting the service
  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.users = this.dataService.getUsers();
  }
}
```

### **Step 3: Details Component (`details.component.ts` & `.html`)**
```typescript
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from '../data.service';

@Component({
  selector: 'app-details',
  template: `
    <h2>User Details</h2>
    <div *ngIf="user; else notFound">
      <p><strong>ID:</strong> {{ user.id }}</p>
      <p><strong>Name:</strong> {{ user.name }}</p>
      <p><strong>Role:</strong> {{ user.role }}</p>
      <a routerLink="/home">Back to List</a>
    </div>
    <ng-template #notFound><p>User not found.</p></ng-template>
  `
})
export class DetailsComponent implements OnInit {
  user: any;

  // Injecting ActivatedRoute to read URL parameters
  constructor(private route: ActivatedRoute, private dataService: DataService) { }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.user = this.dataService.getUserById(id);
  }
}
```

### **Step 4: App Routing Module (`app-routing.module.ts`)**
```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { DetailsComponent } from './details/details.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'user/:id', component: DetailsComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

### **Step 5: App Component Template (`app.component.html`)**
```html
<header style="background: #eee; padding: 10px;">
  <h1>My Angular App</h1>
  <nav>
    <a routerLink="/home">Home</a>
  </nav>
</header>

<main style="padding: 20px;">
  <!-- Components will be rendered here dynamically -->
  <router-outlet></router-outlet>
</main>
```

## 4. Expected Output
- The initial load redirects to `/home` showing a list of 3 users.
- Clicking "View Details" on Alice navigates to `/user/1`.
- The `DetailsComponent` extracts `1` from the URL, fetches the user from `DataService`, and displays the name and role.
- Clicking "Back to List" uses routerLink to return to the `HomeComponent`.