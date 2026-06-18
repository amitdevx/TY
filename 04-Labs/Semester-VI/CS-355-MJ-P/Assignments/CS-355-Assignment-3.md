---
title: "Assignment 3: Component Communication & Lifecycle Hooks"
aliases: [Assignment 3]
tags: [lab, angular, assignment, input, output, lifecycle]
---

[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 3: Component Communication & Lifecycle Hooks

## 1. Problem Statement / Aim
To build a Parent-Child component relationship, pass data from Parent to Child using `@Input`, emit events from Child to Parent using `@Output`, and trace the Angular component lifecycle hooks.

## 2. Theory & Concept

### Component Communication
Angular applications are trees of components. Frequently, these components need to share data.
- **`@Input()`**: Allows a parent component to bind data to a child component.
- **`@Output()`**: Allows a child component to emit custom events (via `EventEmitter`) to notify the parent of an action.

### Lifecycle Hooks
Angular manages the lifecycle of components. We can hook into specific moments using interfaces:
- `ngOnInit()`: Called once after the first `ngOnChanges()`. Best for initialization logic.
- `ngOnChanges()`: Called whenever data-bound input properties (`@Input`) change.
- `ngOnDestroy()`: Called just before Angular destroys the component. Best for cleanup (unsubscribing observables).

## 3. Fully Solved TypeScript/HTML Code

### **Child Component (`child.component.ts`)**
```typescript
import { Component, Input, Output, EventEmitter, OnInit, OnChanges, SimpleChanges, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-child',
  template: `
    <div style="border: 1px solid blue; padding: 10px; margin-top: 10px;">
      <h3>Child Component</h3>
      <p>Received Message: {{ parentMessage }}</p>
      <button (click)="sendMessageToParent()">Send Reply to Parent</button>
    </div>
  `
})
export class ChildComponent implements OnInit, OnChanges, OnDestroy {
  @Input() parentMessage: string = '';
  @Output() childEvent = new EventEmitter<string>();

  ngOnChanges(changes: SimpleChanges) {
    console.log('ngOnChanges triggered!', changes);
  }

  ngOnInit() {
    console.log('ngOnInit triggered! Component initialized.');
  }

  ngOnDestroy() {
    console.log('ngOnDestroy triggered! Component destroyed.');
  }

  sendMessageToParent() {
    this.childEvent.emit('Hello Parent, I received your data!');
  }
}
```

### **Parent Component (`parent.component.ts`)**
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-parent',
  template: `
    <div style="border: 2px solid green; padding: 20px;">
      <h2>Parent Component</h2>
      <input type="text" [(ngModel)]="messageToSend" placeholder="Type message for child">
      <br><br>
      
      <p style="color: red;">Message from Child: {{ replyFromChild }}</p>

      <button (click)="toggleChild()">Toggle Child Component</button>
      
      <!-- Passing data via [parentMessage] and listening via (childEvent) -->
      <app-child 
        *ngIf="showChild"
        [parentMessage]="messageToSend" 
        (childEvent)="receiveMessage($event)">
      </app-child>
    </div>
  `
})
export class ParentComponent {
  messageToSend: string = 'Welcome Child!';
  replyFromChild: string = 'No reply yet.';
  showChild: boolean = true;

  receiveMessage(msg: string) {
    this.replyFromChild = msg;
  }

  toggleChild() {
    this.showChild = !this.showChild;
  }
}
```

## 4. Expected Output
- The Parent component shows an input box. As you type, the `ngOnChanges` hook logs to the console, and the text instantly updates inside the Child component's border.
- Clicking the "Send Reply to Parent" button in the child updates the parent's UI to display the reply.
- Clicking "Toggle Child Component" destroys the child (logging `ngOnDestroy`) and hides it, or re-creates it (logging `ngOnInit`).