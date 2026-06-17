---
title: "CS-371 Agile Methodology - Expected PYQ"
subject: CS-371
paper: Agile Methodology & Software Development
semester: VI
tags:
  - pyq
  - agile
  - scrum
  - kanban
  - xp
  - sdlc
  - semester-vi
  - exam
aliases:
  - Agile PYQ
  - CS371 Questions
created: 2026-06-16
type: pyq
---

[[00-Dashboard/Home|Home]] | [[07-Exams/Exams-Dashboard|Exams Dashboard]]


# CS-371 Agile Methodology - Expected PYQ

> [!important] Exam Strategy
> Agile is mostly theory-based. Master Scrum roles, events, artifacts, Agile Manifesto values and principles, and comparison of Scrum vs Kanban vs XP. Diagrams (Sprint burndown chart, Scrum framework) fetch extra marks.

---

## Unit-wise Distribution

| Unit | Topic | Weightage |
|------|-------|-----------|
| I | Agile Overview & Manifesto | 20% |
| II | Scrum Framework | 30% |
| III | Kanban & Lean | 15% |
| IV | Extreme Programming (XP) | 15% |
| V | Agile Tools & Scaling | 20% |

---

## Section A - Short Answer (2 Marks)

1. **What is Agile methodology? How does it differ from Waterfall?**
2. **List the 4 values of the Agile Manifesto.**
3. **List any 4 of the 12 Agile Principles.**
4. **What is Scrum? What are its three pillars?**
5. **What are the three Scrum roles?**
6. **What are the four Scrum events/ceremonies?**
7. **What are the three Scrum artifacts?**
8. **What is a Sprint? How long is a Sprint typically?**
9. **What is a Product Backlog?**
10. **What is a Sprint Backlog?**
11. **What is the Definition of Done (DoD)?**
12. **What is the role of the Scrum Master?**
13. **What is the role of the Product Owner?**
14. **What is a User Story? What is the INVEST criteria?**
15. **What is Story Points estimation?**
16. **What is Velocity in Scrum?**
17. **What is a Burndown Chart?**
18. **What is Kanban? What are its core principles?**
19. **What is WIP (Work in Progress) limit?**
20. **What is Extreme Programming (XP)? Name its key practices.**
21. **What is Test-Driven Development (TDD)?**
22. **What is Pair Programming?**
23. **What is Continuous Integration (CI)?**
24. **What is a Retrospective? What three questions does it answer?**
25. **What is SAFe (Scaled Agile Framework)?**

---

## Section B - Long Answer (5–7 Marks)

---

### Q1. Agile Manifesto - Values and Principles ()

**4 Core Values:**

| We value... | Over... |
|------------|---------|
| **Individuals and interactions** | Processes and tools |
| **Working software** | Comprehensive documentation |
| **Customer collaboration** | Contract negotiation |
| **Responding to change** | Following a plan |

> Note: "The items on the right have value, but we value the items on the left more."

**12 Agile Principles (Key ones):**

1. Customer satisfaction through early and continuous delivery of valuable software
2. Welcome changing requirements, even late in development
3. Deliver working software frequently (2 weeks to 2 months)
4. Business people and developers work together daily
5. Build projects around motivated individuals
6. Face-to-face conversation is most efficient (co-location)
7. Working software is the primary measure of progress
8. Agile processes promote sustainable development
9. Continuous attention to technical excellence
10. Simplicity - the art of maximizing work NOT done
11. Best architectures emerge from self-organizing teams
12. Team reflects on how to become more effective (retrospective)

---

### Q2. Scrum Framework - Complete Overview ()

**Scrum Framework Diagram:**
```
Product Backlog
    ↓ (Sprint Planning)
Sprint Backlog
    ↓
Sprint (2-4 weeks)
├── Daily Scrum (15 min standup)
├── Development Work
└── Testing & Integration
    ↓
Potentially Shippable Product Increment
    ↓ (Sprint Review → Demo to stakeholders)
    ↓ (Sprint Retrospective → Process improvement)
Next Sprint →
```

**Three Pillars of Scrum (SIA):**
- **Transparency:** All work visible to stakeholders
- **Inspection:** Frequent check of progress toward goals
- **Adaptation:** Adjust processes if deviation detected

**Scrum Roles:**

| Role | Responsibilities |
|------|----------------|
| **Product Owner** | Defines product vision, manages Product Backlog, prioritizes features, represents stakeholders |
| **Scrum Master** | Facilitates Scrum process, removes impediments, coaches team, shields from interruptions |
| **Development Team** | Self-organizing, cross-functional, builds the product increment (3-9 members) |

**Scrum Events:**

| Event | Duration | Purpose |
|-------|----------|---------|
| Sprint Planning | 8 hrs (for 4-wk sprint) | Select PBI, create Sprint Backlog |
| Daily Scrum | 15 min | Sync, plan next 24 hrs, identify blockers |
| Sprint Review | 4 hrs | Demo increment to stakeholders, get feedback |
| Sprint Retrospective | 3 hrs | Inspect process, plan improvements |

**Scrum Artifacts:**

| Artifact | Description |
|----------|-------------|
| **Product Backlog** | Ordered list of all desired work; maintained by PO |
| **Sprint Backlog** | Items selected for current Sprint + plan |
| **Increment** | Sum of all completed PBIs - must be "Done" |

---

### Q3. User Stories and Story Points ()

**User Story Format:**
```
As a [type of user],
I want [some goal]
so that [some reason/benefit].
```

**Example:**
```
As a student,
I want to view my attendance records online
so that I can track my eligibility for exams.
```

**INVEST Criteria for Good User Stories:**

| Letter | Stands For | Meaning |
|--------|-----------|---------|
| I | Independent | Can be developed in any order |
| N | Negotiable | Details can be discussed |
| V | Valuable | Provides value to user/customer |
| E | Estimable | Can be estimated in story points |
| S | Small | Can fit in a Sprint |
| T | Testable | Has clear acceptance criteria |

**Acceptance Criteria (Given-When-Then):**
```
Given: Student is logged in
When:  Student clicks "View Attendance"
Then:  System shows attendance percentage and dates
```

**Story Points (Fibonacci: 1, 2, 3, 5, 8, 13, 21):**
- Small task = 1-2 points
- Medium task = 3-5 points
- Large task = 8-13 points
- Epic (needs splitting) = 21+

---

### Q4. Kanban Board and WIP Limits ()

**Kanban Board Columns:**
```
| Backlog | To Do | In Progress | Review | Done |
|---------|-------|-------------|--------|------|
|  Story1 | Story2|   Story3    |Story4  |Story5|
|  Story6 | Story7|             |        |Story8|
```

**WIP (Work In Progress) Limit:**
- Each column has a max number of items allowed
- Example: In Progress column max = 3
- Forces team to finish work before starting new items
- Reduces context switching, identifies bottlenecks

**Kanban vs Scrum:**

| Feature | Scrum | Kanban |
|---------|-------|--------|
| Iterations | Fixed Sprints (2-4 wks) | Continuous flow |
| Roles | PO, SM, Dev Team | No prescribed roles |
| Velocity | Measures story points | Measures cycle time |
| Changes | After Sprint ends | Any time |
| Board | Sprint Board | Kanban Board |
| Best for | Feature development | Support/maintenance |

---

### Q5. Extreme Programming (XP) Practices ()

**12 XP Practices:**

1. **Planning Game** - Collaborative sprint planning
2. **Small Releases** - Frequent, small deployments
3. **Simple Design** - YAGNI (You Aren't Gonna Need It)
4. **Test-Driven Development (TDD)** - Tests before code
5. **Pair Programming** - Two developers, one computer
6. **Refactoring** - Continuously improve code
7. **Continuous Integration** - Merge and build frequently
8. **Collective Code Ownership** - Anyone can change any code
9. **Coding Standards** - Consistent code style
10. **On-site Customer** - Customer available always
11. **40-Hour Week** - No overtime (sustainable pace)
12. **Metaphor** - Simple shared story of system

**TDD Cycle (Red-Green-Refactor):**
```
RED:     Write failing test
GREEN:   Write minimum code to pass test
REFACTOR: Clean up code without breaking tests
Repeat...
```

---

### Q6. Agile vs Waterfall ()

| Aspect | Waterfall | Agile |
|--------|-----------|-------|
| Approach | Sequential phases | Iterative sprints |
| Requirements | Fixed upfront | Evolving |
| Customer involvement | Mostly at start/end | Throughout |
| Delivery | Single delivery at end | Frequent small releases |
| Testing | After development | Throughout |
| Risk | High (late discovery) | Low (early feedback) |
| Documentation | Comprehensive | Minimal, just enough |
| Flexibility | Rigid | Highly flexible |
| Team | Functional silos | Cross-functional |
| Best for | Fixed, well-defined projects | Complex, changing projects |

---

### Q7. Sprint Burndown Chart ()

```
Story Points Remaining vs. Days in Sprint

40 |*
35 | \
30 |  *
25 |   \   (Ideal line)
20 |    *----
15 |   / \
10 |  *   \
 5 |       *
 0 |--------*
   0  2  4  6  8  10 (Days)
   
* = Actual remaining work
\ = Ideal burndown line
```

- **Above ideal line:** Team is behind schedule
- **Below ideal line:** Team is ahead of schedule
- **Flat line:** No work getting done (blocked?)

---

### Q8. Agile Estimation - Planning Poker ()

**Planning Poker Process:**
1. PO reads/explains User Story
2. Each team member picks a card (story point estimate) - kept hidden
3. All reveal simultaneously
4. Discuss outliers
5. Re-estimate until consensus

**Why Fibonacci? (1, 2, 3, 5, 8, 13, 21)**
- Reflects natural uncertainty in estimation
- Large gaps force meaningful discussion
- Prevents false precision

---

## Most Expected Questions

> [!tip] High Probability
> 1.  Agile Manifesto - 4 values and 12 principles
> 2.  Scrum framework - roles, events, artifacts complete explanation
> 3.  User Story with INVEST + acceptance criteria
> 4.  Scrum vs Kanban vs Waterfall comparison table
> 5.  Sprint Burndown Chart explanation + diagram
> 6.  TDD Red-Green-Refactor cycle
> 7.  Daily Scrum - what 3 questions are answered?
> 8.  Story Points and Planning Poker

---

## Daily Scrum - 3 Questions

> [!note] Every day, each team member answers:
> 1. **What did I do yesterday?** (Progress)
> 2. **What will I do today?** (Plan)
> 3. **Are there any impediments?** (Blockers)

---

*Tags: CS-371 Agile Methodology | Semester VI | [[07-Exams/Exams-Dashboard|Exams]]*
