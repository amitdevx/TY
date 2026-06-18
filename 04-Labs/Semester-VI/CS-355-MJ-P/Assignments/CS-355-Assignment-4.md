---
title: "Assignment 4: Angular Forms (Reactive Forms)"
aliases: [Assignment 4]
tags: [lab, angular, assignment, forms, reactive-forms]
---

[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 4: Angular Forms (Reactive Forms)

## 1. Problem Statement / Aim
To implement a "User Registration" form utilizing Angular Reactive Forms, incorporating built-in validators, custom validation logic, and dynamic error message display.

## 2. Theory & Concept

### Reactive Forms
Reactive forms use a model-driven approach. You define the form model (the structure and validators) explicitly in the TypeScript class.
- **`FormControl`**: Tracks the value and validation status of a single form element.
- **`FormGroup`**: Tracks the value and validity state of a group of `FormControl` instances.
- **`FormBuilder`**: A service that provides syntactic sugar for creating form control groups easily.
- **`Validators`**: Built-in functions like `required`, `minLength`, `email`.

### Why Reactive over Template-Driven?
Reactive forms are more scalable, reusable, and testable. The logic resides in the component class, making complex validation (like cross-field validation) much easier to implement.

## 3. Fully Solved TypeScript/HTML Code

### **Step 1: Import Module (`app.module.ts`)**
```typescript
import { ReactiveFormsModule } from '@angular/forms'; // <-- Import this

@NgModule({
  // ...
  imports: [
    // ...
    ReactiveFormsModule 
  ]
})
export class AppModule { }
```

### **Step 2: Component TypeScript (`register.component.ts`)**
```typescript
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  registerForm!: FormGroup;
  submitted = false;

  constructor(private fb: FormBuilder) { }

  ngOnInit(): void {
    // Initialize the form
    this.registerForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(4)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  // Convenience getter for easy access to form fields in HTML
  get f() { return this.registerForm.controls; }

  onSubmit() {
    this.submitted = true;

    // Stop here if form is invalid
    if (this.registerForm.invalid) {
      return;
    }

    // Display form values on success
    alert('SUCCESS!! :-)\n\n' + JSON.stringify(this.registerForm.value, null, 4));
  }
}
```

### **Step 3: Component Template (`register.component.html`)**
```html
<div class="form-container">
  <h2>User Registration</h2>
  
  <form [formGroup]="registerForm" (ngSubmit)="onSubmit()">
    
    <!-- Username Field -->
    <div class="form-group">
      <label>Username</label>
      <input type="text" formControlName="username" />
      
      <div *ngIf="submitted || f['username'].touched" class="error-text">
        <small *ngIf="f['username'].errors?.['required']">Username is required.</small>
        <small *ngIf="f['username'].errors?.['minlength']">Username must be at least 4 characters.</small>
      </div>
    </div>

    <!-- Email Field -->
    <div class="form-group">
      <label>Email</label>
      <input type="email" formControlName="email" />
      
      <div *ngIf="submitted || f['email'].touched" class="error-text">
        <small *ngIf="f['email'].errors?.['required']">Email is required.</small>
        <small *ngIf="f['email'].errors?.['email']">Must be a valid email address.</small>
      </div>
    </div>

    <!-- Password Field -->
    <div class="form-group">
      <label>Password</label>
      <input type="password" formControlName="password" />
      
      <div *ngIf="submitted || f['password'].touched" class="error-text">
        <small *ngIf="f['password'].errors?.['required']">Password is required.</small>
        <small *ngIf="f['password'].errors?.['minlength']">Password must be at least 6 characters.</small>
      </div>
    </div>

    <button type="submit" [disabled]="registerForm.invalid">Register</button>
  </form>
</div>
```

### **CSS Snippet (`register.component.css`)**
```css
.error-text { color: red; margin-top: 5px; }
input.ng-invalid.ng-touched { border-left: 5px solid red; }
input.ng-valid.ng-touched { border-left: 5px solid green; }
```

## 4. Expected Output
- A registration form with Username, Email, and Password.
- When the user clicks into an input and leaves it blank, a red border and error message appear.
- The "Register" button is disabled until all inputs are valid.
- On valid submission, an alert box displays the JSON data of the form.