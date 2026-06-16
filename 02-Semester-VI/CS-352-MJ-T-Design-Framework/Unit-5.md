---
title: "CS-352 Unit 5 - Angular Forms & Validation"
tags: [cs-352, angular, unit-5]
---

# Unit 5: Angular Forms & Validation

## Introduction to Angular Forms
Angular provides two different approaches to handling forms:
1. **Template-driven forms**: Relies on directives in the template.
2. **Reactive forms**: Model-driven, created in the component class.

## Template-Driven Forms
- Easy to use, suitable for simple forms.
- Uses `FormsModule`.
- Two-way data binding with `[(ngModel)]`.
- **Validation**: Uses standard HTML5 attributes (required, minlength, maxlength).
- **State classes**: `ng-touched`, `ng-dirty`, `ng-invalid`.

## Reactive Forms
- Robust, scalable, suitable for complex forms.
- Uses `ReactiveFormsModule`.
- Built around `FormControl`, `FormGroup`, and `FormArray`.
- **FormBuilder**: A service providing convenient methods for generating controls.
- **Validation**: Synchronous and asynchronous validators defined in the component class.
- Dynamic form controls can be added or removed at runtime.

## Custom Validators
- Functions that take a `AbstractControl` and return an error object or null.
- Example: Validating a specific password pattern or ensuring two fields match.
