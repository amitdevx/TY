---
title: "Assignment 2: Directives and Pipes"
aliases: [Assignment 2]
tags: [lab, angular, assignment, directives, pipes]
---

[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 2: Directives and Pipes

## 1. Problem Statement / Aim
To effectively use Angular's built-in structural directives (`*ngIf`, `*ngFor`, `[ngSwitch]`), attribute directives (`[ngClass]`, `[ngStyle]`), and Built-in Pipes to format data dynamically in the template.

## 2. Theory & Concept

### Directives
Directives are classes that add additional behavior to elements in your Angular applications.
- **Structural Directives**: Alter the DOM layout.
  - `*ngIf`: Conditionally includes/excludes a DOM element.
  - `*ngFor`: Renders a list of items.
  - `[ngSwitch]`: Conditionally swaps DOM structure based on a value.
- **Attribute Directives**: Change the appearance or behavior.
  - `[ngClass]`: Dynamically adds/removes CSS classes.
  - `[ngStyle]`: Dynamically sets inline styles.

### Pipes
Pipes are simple functions to use in template expressions to accept an input value and return a transformed value (e.g., date formatting, casing, currency).
- Syntax: `{{ value | pipeName: argument }}`

## 3. Fully Solved TypeScript/HTML Code

### **Component TypeScript (`inventory.component.ts`)**
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-inventory',
  templateUrl: './inventory.component.html',
  styleUrls: ['./inventory.component.css']
})
export class InventoryComponent {
  isVisible: boolean = true;
  viewMode: string = 'list'; // can be 'list' or 'grid'

  products = [
    { name: 'Laptop', category: 'Electronics', price: 1200, dateAdded: new Date('2023-01-15'), stock: 5 },
    { name: 'Desk Chair', category: 'Furniture', price: 150, dateAdded: new Date('2023-03-22'), stock: 0 },
    { name: 'Headphones', category: 'Electronics', price: 80, dateAdded: new Date('2023-06-10'), stock: 15 }
  ];

  toggleVisibility() {
    this.isVisible = !this.isVisible;
  }

  setViewMode(mode: string) {
    this.viewMode = mode;
  }
}
```

### **Component Template (`inventory.component.html`)**
```html
<div class="inventory-container">
  <h2>Inventory Management</h2>
  
  <button (click)="toggleVisibility()">
    {{ isVisible ? 'Hide' : 'Show' }} Inventory
  </button>
  
  <button (click)="setViewMode('list')">List View</button>
  <button (click)="setViewMode('grid')">Grid View</button>

  <!-- Structural Directive: *ngIf -->
  <div *ngIf="isVisible; else hiddenMsg" class="inventory-box">
    
    <!-- Structural Directive: [ngSwitch] -->
    <div [ngSwitch]="viewMode">
      <h3 *ngSwitchCase="'list'">Displaying in List Format</h3>
      <h3 *ngSwitchCase="'grid'">Displaying in Grid Format</h3>
      <h3 *ngSwitchDefault>Unknown View Mode</h3>
    </div>

    <table border="1" cellpadding="10" *ngIf="viewMode === 'list'">
      <thead>
        <tr>
          <th>Name</th>
          <th>Category</th>
          <th>Price</th>
          <th>Date Added</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <!-- Structural Directive: *ngFor -->
        <tr *ngFor="let product of products">
          <!-- Pipes: uppercase, lowercase -->
          <td>{{ product.name | uppercase }}</td>
          <td>{{ product.category | lowercase }}</td>
          
          <!-- Pipes: currency -->
          <td>{{ product.price | currency:'USD' }}</td>
          
          <!-- Pipes: date -->
          <td>{{ product.dateAdded | date:'mediumDate' }}</td>
          
          <!-- Attribute Directives: [ngStyle] and [ngClass] -->
          <td 
            [ngStyle]="{ 'color': product.stock > 0 ? 'green' : 'red' }"
            [ngClass]="{ 'out-of-stock': product.stock === 0 }">
            {{ product.stock > 0 ? 'In Stock (' + product.stock + ')' : 'Out of Stock' }}
          </td>
        </tr>
      </tbody>
    </table>
    
    <div *ngIf="viewMode === 'grid'">
       <p><i>Grid View HTML Implementation goes here...</i></p>
    </div>
  </div>

  <ng-template #hiddenMsg>
    <p>The inventory is currently hidden.</p>
  </ng-template>
</div>
```

## 4. Expected Output
- A table displaying products.
- Button toggles the table visibility (showing a fallback message using `<ng-template #hiddenMsg>`).
- Values are formatted using pipes (e.g., "$1,200.00", "Jan 15, 2023").
- Items with 0 stock are rendered in red text automatically via `[ngStyle]`.