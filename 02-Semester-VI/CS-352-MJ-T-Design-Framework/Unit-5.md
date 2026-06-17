---
title: "Unit 5: Forms and Validation in Angular"
subject: CS-352-MJ-T
unit_number: 5
status: completed
completion_percentage: 100
tags: [cs-352, angular, forms, validation, unit-5, semester-vi]
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Unit 5: Forms and Validation in Angular

> [!important] Learning Objectives
> - Understand the two approaches to forms in Angular.
> - Implement Template-driven forms.
> - Implement Reactive forms.
> - Apply built-in and custom validators to form controls.
> - Handle form submission and display validation errors.

---

## 1. Introduction to Angular Forms

Handling user input with forms is the cornerstone of many common applications. Applications use forms to log in users, update profiles, enter sensitive information, and perform many other data-entry tasks.

Angular provides two different approaches to handling user input through forms:
1. **Template-driven forms:** Rely on directives in the template to create and manipulate the underlying object model.
2. **Reactive forms:** Provide direct, explicit access to the underlying form's object model in the component class.

### Comparison

| Feature | Template-Driven | Reactive |
|---|---|---|
| **Setup Module** | `FormsModule` | `ReactiveFormsModule` |
| **Logic Location** | HTML Template | Component Class |
| **Form Model Creation** | Implicit (created by Angular directives) | Explicit (created in TypeScript code) |
| **Data Binding** | Two-way (`[(ngModel)]`) | Mostly synchronous (Observables) |
| **Validation** | HTML5 attributes (`required`, `minlength`) | Custom Validator functions in class |
| **Testing** | Difficult | Easier |
| **Use Case** | Simple, basic forms | Complex, dynamic, scalable forms |

---

## 2. Template-Driven Forms

In template-driven forms, you write most of the logic directly in the HTML template using Angular directives.

### Step-by-Step Implementation

**1. Import FormsModule:**
In your `app.module.ts`:
```typescript
import { FormsModule } from '@angular/forms';

@NgModule({
  imports: [
    FormsModule
  ]
})
```

**2. Create the Template:**
Use `ngForm` and `ngModel` directives.

```html
<div class="container">
  <h2>User Registration (Template-Driven)</h2>
  
  <!-- #userForm creates a local template variable referencing the ngForm directive -->
  <form #userForm="ngForm" (ngSubmit)="onSubmit(userForm)">
    
    <div class="form-group">
      <label>Name:</label>
      <!-- ngModel tells Angular to create a FormControl for this input -->
      <!-- name attribute is strictly required when using ngModel in a form -->
      <input type="text" name="name" ngModel required #nameRef="ngModel">
      
      <!-- Validation Error Display -->
      <div *ngIf="nameRef.invalid && (nameRef.dirty || nameRef.touched)" class="error">
        Name is required.
      </div>
    </div>

    <div class="form-group">
      <label>Email:</label>
      <input type="email" name="email" ngModel required email #emailRef="ngModel">
      <div *ngIf="emailRef.errors?.['required'] && emailRef.touched" class="error">
        Email is required.
      </div>
      <div *ngIf="emailRef.errors?.['email'] && emailRef.touched" class="error">
        Invalid email format.
      </div>
    </div>

    <!-- Submit button disabled until form is fully valid -->
    <button type="submit" [disabled]="userForm.invalid">Register</button>
  </form>
</div>
```

**3. Component Class:**
```typescript
import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html'
})
export class RegistrationComponent {
  
  onSubmit(form: NgForm) {
    console.log('Form Submitted!', form.value);
    console.log('Is Form Valid?', form.valid);
  }
}
```

---

## 3. Reactive Forms

Reactive forms provide a model-driven approach to handling form inputs whose values change over time. You create a tree of Angular form control objects in the component class and bind them to native form control elements in the component template.

### Core Classes
- `FormControl`: Tracks the value and validation status of an individual form control.
- `FormGroup`: Tracks the same values and status for a collection of form controls.
- `FormBuilder`: A helper class to easily generate controls and groups.

### Step-by-Step Implementation

**1. Import ReactiveFormsModule:**
```typescript
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  imports: [
    ReactiveFormsModule
  ]
})
```

**2. Component Class (Logic):**
```typescript
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html'
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;

  // Inject FormBuilder
  constructor(private fb: FormBuilder) {}

  ngOnInit() {
    // Define the form model explicitly
    this.loginForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(4)]],
      password: ['', [Validators.required]]
    });
  }

  // Getter for easy access in template
  get f() { return this.loginForm.controls; }

  onSubmit() {
    if (this.loginForm.valid) {
      console.log('Login Data:', this.loginForm.value);
    } else {
      console.log('Form is invalid');
    }
  }
}
```

**3. HTML Template:**
Bind the HTML form to the `FormGroup` using `[formGroup]`, and bind inputs to `FormControl` using `formControlName`.

```html
<div class="container">
  <h2>Login (Reactive Form)</h2>
  
  <form [formGroup]="loginForm" (ngSubmit)="onSubmit()">
    
    <div class="form-group">
      <label>Username:</label>
      <input type="text" formControlName="username">
      
      <!-- Validation Display -->
      <div *ngIf="f['username'].touched && f['username'].invalid" class="error">
        <div *ngIf="f['username'].errors?.['required']">Username is required.</div>
        <div *ngIf="f['username'].errors?.['minlength']">Minimum 4 characters required.</div>
      </div>
    </div>

    <div class="form-group">
      <label>Password:</label>
      <input type="password" formControlName="password">
      
      <div *ngIf="f['password'].touched && f['password'].invalid" class="error">
        Password is required.
      </div>
    </div>

    <button type="submit" [disabled]="loginForm.invalid">Login</button>
  </form>
</div>
```

---

## 4. Form Validation

Validation ensures that user input is correct and complete. Angular provides built-in validators and allows you to create custom ones.

### Form Control States

Angular automatically applies CSS classes to form controls based on their state:
- `ng-untouched` / `ng-touched` (Has the user visited the field?)
- `ng-pristine` / `ng-dirty` (Has the user modified the value?)
- `ng-valid` / `ng-invalid` (Does it pass validation?)

### Built-in Validators
Provided by the `Validators` class (for Reactive forms) or as HTML attributes (for Template-driven forms):
- `required`
- `minlength` / `maxlength`
- `min` / `max`
- `email`
- `pattern` (Regex validation)

### Custom Validators

You can create custom validation logic. A validator is a simple function that takes a `AbstractControl` and returns an error object if validation fails, or `null` if it passes.

**Example: Password Match Validator (Reactive Form)**

```typescript
import { AbstractControl, ValidationErrors } from '@angular/forms';

export function MustMatch(controlName: string, matchingControlName: string) {
    return (formGroup: AbstractControl): ValidationErrors | null => {
        const control = formGroup.get(controlName);
        const matchingControl = formGroup.get(matchingControlName);

        if (!control || !matchingControl) {
          return null;
        }

        // return if another validator has already found an error
        if (matchingControl.errors && !matchingControl.errors['mustMatch']) {
            return null;
        }

        // set error on matchingControl if validation fails
        if (control.value !== matchingControl.value) {
            matchingControl.setErrors({ mustMatch: true });
            return { mustMatch: true };
        } else {
            matchingControl.setErrors(null);
            return null;
        }
    };
}
```

Usage in FormBuilder:
```typescript
this.registerForm = this.fb.group({
    password: ['', Validators.required],
    confirmPassword: ['', Validators.required]
}, {
    validators: MustMatch('password', 'confirmPassword')
});
```

---

> [!tip] Revision Summary
> - Use **Template-Driven Forms** for simple scenarios (login, basic contact form). Rely on `ngModel`.
> - Use **Reactive Forms** for complex, dynamic scenarios, or when you need strict testing. Build the model in TS using `FormBuilder`.
> - Use the `[disabled]` property to prevent submission of invalid forms.
> - Display error messages using `*ngIf` by checking `control.invalid` and `control.touched`.

---

[[02-Semester-VI/CS-352-MJ-T-Design-Framework/Unit-4|Previous: Unit 4]] | [[02-Semester-VI/CS-352-MJ-T-Design-Framework/Important-Questions|Important Questions]]
