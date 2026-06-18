# CS-371 Assignment 3: Backlog Prioritization and Release Planning

## Problem Statement / Aim
To understand various techniques for prioritizing a Product Backlog and to plan a release by assigning stories to sprints based on team velocity.

## Theory & Concept
**Product Backlog:** An emergent, ordered list of what is needed to improve the product.
**Prioritization Techniques:**
- **MoSCoW Method:** Must have, Should have, Could have, Won't have.
- **Value vs. Effort Matrix:** Prioritizing high-value, low-effort items first.
- **Kano Model:** Categorizing features based on customer satisfaction (Basic, Performance, Excitement).

**Release Planning:**
The process of determining which backlog items will be developed and delivered in upcoming sprints, constrained by the team's estimated velocity.

## Fully Solved Code / Implementation
*Scenario: Prioritizing a backlog for a Food Delivery App.*

**1. Backlog Prioritization using MoSCoW:**

| ID | User Story Summary | MoSCoW Category | Story Points |
|---|---|---|---|
| US1 | User Registration & Login | Must Have | 5 |
| US2 | Browse Restaurant Menu | Must Have | 8 |
| US3 | Add items to cart | Must Have | 3 |
| US4 | Checkout via Credit Card | Must Have | 5 |
| US5 | Live Order Tracking | Should Have | 8 |
| US6 | Save favorite restaurants | Could Have | 2 |
| US7 | Split bill with friends | Won't Have (for now)| 13 |

**2. Release Planning:**
*Assumed Team Velocity:* 15 Story Points per Sprint.

**Sprint 1 Plan:**
- US1: Registration & Login (5 points)
- US2: Browse Menu (8 points)
*Total:* 13 points (Leaves a 2-point buffer)

**Sprint 2 Plan:**
- US3: Add to cart (3 points)
- US4: Checkout via CC (5 points)
- US6: Save favorites (2 points)
*Total:* 10 points (Under capacity, can pull in technical debt or start US5)

## Expected Output
A prioritized backlog categorizing requirements by necessity, and a realistic sprint-by-sprint release plan that respects the team's velocity constraint.

[[CS-371-Viva-3|View Viva Questions]]
