---
title: "CS-371 Agile Processes Revision"
tags: [cs-371, agile, scrum, kanban, semester-vi, revision]
subject_code: CS-371-VSC-P
type: revision
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Agile Processes - Quick Revision Summary

> [!tip] How to use this guide
> Review this page the night before your viva or external exam. It contains the core values, principles, and tables needed for rapid recall.

---

## 1. The Agile Manifesto

> [!important] The 4 Core Values
> 1. **Individuals and interactions** over processes and tools
> 2. **Working software** over comprehensive documentation
> 3. **Customer collaboration** over contract negotiation
> 4. **Responding to change** over following a plan

*(While there is value in the items on the right, we value the items on the left more.)*

---

## 2. The Scrum Framework

Scrum is an iterative and incremental agile software development framework for managing product development.

### The 3 Scrum Roles

1. **Product Owner:** Maximizes the value of the product; manages the Product Backlog; represents the customer.
2. **Scrum Master:** Servant-leader; ensures Scrum is understood and enacted; removes impediments; facilitates events.
3. **Development Team:** Self-organizing, cross-functional team of 3-9 members who do the actual work of delivering the product increment.

### The 3 Scrum Artifacts

1. **Product Backlog:** An ordered, evolving list of everything that is known to be needed in the product.
2. **Sprint Backlog:** The set of Product Backlog items selected for the Sprint, plus a plan for delivering the product Increment.
3. **Increment:** The sum of all the Product Backlog items completed during a Sprint and the value of the increments of all previous Sprints. (Must be in a usable, "Done" condition).

### The 5 Scrum Events

| Event | Timebox | Purpose |
|---|---|---|
| **Sprint** | 1-4 Weeks | The container event for all other events. A consistent cycle where an increment is built. |
| **Sprint Planning** | 8 hrs (for 4-wk Sprint) | Defines WHAT can be delivered in the Increment and HOW that work will be achieved. |
| **Daily Scrum** | 15 minutes | Daily sync for the Dev Team. 3 Questions: What did I do yesterday? What will I do today? Are there any impediments? |
| **Sprint Review** | 4 hrs (for 4-wk Sprint) | Inspect the Increment and adapt the Product Backlog. Demonstrate the working software to stakeholders. |
| **Sprint Retrospective** | 3 hrs (for 4-wk Sprint) | Inspect how the last Sprint went regarding people, relationships, process, and tools. Plan improvements. |

---

## 3. Kanban vs Scrum

| Feature | Scrum | Kanban |
|---|---|---|
| **Cadence / Iterations** | Fixed length Sprints (1-4 weeks) | Continuous flow (no fixed iterations) |
| **Roles** | Product Owner, Scrum Master, Team | No predefined roles required |
| **Key Metric** | Velocity (points per sprint) | Cycle Time and Lead Time |
| **Work in Progress (WIP)** | WIP is limited implicitly per Sprint | WIP limits are set explicitly per workflow state (column) |
| **Changes** | No changes allowed during a Sprint | Changes can be made at any time as long as WIP limits allow |

---

## 4. Estimation Techniques

- **Story Points:** A relative unit of measure used to estimate the overall effort required to fully implement a product backlog item or any other piece of work. Factors in volume, complexity, and risk.
- **Planning Poker:** A consensus-based estimating technique. Team members use a deck of cards (usually Fibonacci sequence: 1, 2, 3, 5, 8, 13...) to estimate effort.

---

## 5. Agile Quality & DevOps

> [!note] Continuous Practices
> - **CI (Continuous Integration):** Developers merge code changes into a central repository multiple times a day. Automated builds and tests run on every commit.
> - **CD (Continuous Delivery/Deployment):** Automating the release process so software can be reliably released at any time.

> [!note] TDD (Test-Driven Development) Cycle
> 1. **Red:** Write a failing automated test for a new feature.
> 2. **Green:** Write the minimum code necessary to pass the test.
> 3. **Refactor:** Clean up the code while ensuring tests still pass.

---

[[02-Semester-VI/CS-371-VSC-P-Agile-Processes/Interview-Prep|Interview Prep]] | [[02-Semester-VI/CS-371-VSC-P-Agile-Processes/Unit-1|Unit 1]]
