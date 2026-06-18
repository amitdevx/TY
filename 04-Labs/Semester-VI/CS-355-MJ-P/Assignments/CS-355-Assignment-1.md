---
title: "Assignment 1: Components and Data Binding"
aliases: [Assignment 1]
tags: [lab, angular, assignment, components, data-binding]
---

[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 1: Components and Data Binding

## 1. Problem Statement / Aim
To understand the creation of Angular components and demonstrate the four types of data binding: Interpolation, Property Binding, Event Binding, and Two-Way Data Binding.

## 2. Theory & Concept

### Components
A component controls a patch of screen called a view. It consists of:
- A TypeScript class defining behavior.
- An HTML template defining the UI.
- CSS for styling the UI.
The `@Component` decorator identifies the class as a component.

### Data Binding
Data binding connects the application's logic (TypeScript) with the UI (HTML).
1. **Interpolation `{{ }}`**: Embeds dynamic string values into the HTML.
2. **Property Binding `[property]`**: Sets values for properties of HTML elements or directives.
3. **Event Binding `(event)`**: Listens to specific UI events (clicks, key presses) and executes class methods.
4. **Two-Way Binding `[(ngModel)]`**: Combines property and event binding. It requires the `FormsModule`.

## 3. Fully Solved TypeScript/HTML Code

### **Step 1: Update `app.module.ts`**
To use Two-way binding, import `FormsModule`.
```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms'; // <-- Import this

import { AppComponent } from './app.component';
import { ProfileComponent } from './profile/profile.component';

@NgModule({
  declarations: [
    AppComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    FormsModule // <-- Add to imports
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

### **Step 2: Component TypeScript (`profile.component.ts`)**
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  // Interpolation & Property Binding
  userName: string = 'John Doe';
  userRole: string = 'Developer';
  profileImage: string = 'https://via.placeholder.com/150';
  isDisabled: boolean = false;

  // Event Binding
  clickCount: number = 0;

  onButtonClick() {
    this.clickCount++;
  }

  toggleDisable() {
    this.isDisabled = !this.isDisabled;
  }
}
```

### **Step 3: Component Template (`profile.component.html`)**
```html
<div class="profile-card">
  <!-- Interpolation -->
  <h2>User Profile: {{ userName }}</h2>
  <p>Role: {{ userRole }}</p>

  <!-- Property Binding -->
  <img [src]="profileImage" alt="Profile" />
  <br>
  
  <!-- Event Binding -->
  <button [disabled]="isDisabled" (click)="onButtonClick()">
    Click Me
  </button>
  <p>Button clicked: {{ clickCount }} times</p>

  <button (click)="toggleDisable()">Toggle Button State</button>

  <hr>

  <!-- Two-Way Data Binding -->
  <h3>Edit Profile (Two-Way Binding)</h3>
  <label>Name: </label>
  <input type="text" [(ngModel)]="userName" />
  
  <br><br>
  
  <label>Role: </label>
  <input type="text" [(ngModel)]="userRole" />
</div>
```

## 4. Expected Output
- A web page showing a user profile card with an image.
- Text displays "User Profile: John Doe".
- Clicking the "Click Me" button increments the click counter below it.
- Clicking the "Toggle Button State" dynamically disables/enables the first button.
- Typing inside the "Name" or "Role" input boxes immediately updates the text at the top of the page in real-time.