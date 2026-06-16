---
title: "CS-371 Agile Processes - Syllabus"
subject: "Agile Processes"
subject_code: "CS-371-VSC-P"
semester: VI
year: "TY B.Sc. CS"
type: Vocational/Skill Course Practical
credits: 2
tags:
  - semester-vi
  - agile
  - scrum
  - syllabus
created: 2026-06-16
updated: 2026-06-16
---

#  CS-371 Agile Processes - Syllabus

> [!note] Course Details
> **Subject Code:** CS-371-VSC-P | **Type:** Vocational/Skill Course (Practical)
> **Semester:** VI | **Program:** TY B.Sc. Computer Science
> **Credits:** 2 | **Total Assignments:** 8

---

##  Assignment-wise Syllabus

### Assignment 1: Agile Fundamentals & Team Setup *(2 Slots)*

> [!note] Unit 1 → [[Unit-1|See detailed notes]]

| Topic | Details |
|-------|---------|
| Agile Manifesto | 4 values: Individuals & interactions, Working software, Customer collaboration, Responding to change |
| 12 Agile Principles | Full list - customer satisfaction, welcome change, frequent delivery, collaboration, motivation, face-to-face, working software, sustainable pace, technical excellence, simplicity, self-organization, regular reflection |
| Git Setup | `git init`, `.gitignore`, branching strategy (main/develop/feature) |
| Agile Board Setup | Jira/Azure DevOps board: Backlog → To Do → In Progress → Done columns |
| Team Roles | Product Owner, Scrum Master, Development Team |
| Scrum Overview | Sprints, artifacts, ceremonies |

---

### Assignment 2: User Stories & Acceptance Criteria *(1 Slot)*

> [!note] Unit 1 → [[Unit-1|See detailed notes]]

| Topic | Details |
|-------|---------|
| User Story Format | "As a [role], I want [goal], so that [benefit]" |
| Acceptance Criteria | Given-When-Then (Gherkin) format |
| Story Attributes | INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable |
| Definition of Ready (DoR) | Criteria for a story to enter a sprint |
| Definition of Done (DoD) | Criteria for a story to be considered complete |
| Story Splitting | Techniques for breaking large stories (epics) into smaller ones |
| Epics vs Stories | Hierarchy: Theme → Epic → Feature → User Story → Task |

---

### Assignment 3: Backlog Prioritization & Release Planning *(1 Slot)*

> [!note] Unit 2 → [[Unit-2|See detailed notes]]

| Topic | Details |
|-------|---------|
| Product Backlog | Creating, maintaining, and ordering the backlog |
| MoSCoW Technique | Must have, Should have, Could have, Won't have |
| WSJF | Weighted Shortest Job First = CoD / Duration |
| Cost of Delay | User business value, time criticality, risk reduction |
| Sprint Planning | Sprint goal, selecting stories from backlog |
| MVP Definition | Minimum Viable Product - minimum feature set for value delivery |
| Release Planning | Release roadmap, release burndown |

---

### Assignment 4: Agile Estimation & Sprint Planning *(2 Slots)*

> [!note] Unit 2 → [[Unit-2|See detailed notes]]

| Topic | Details |
|-------|---------|
| Story Points | Relative estimation (not time), Fibonacci scale (1,2,3,5,8,13,21) |
| Planning Poker | Process: reveal cards simultaneously, discuss outliers, re-estimate |
| T-shirt Sizing | XS, S, M, L, XL as rough estimates |
| Velocity | Historical average story points per sprint |
| Capacity Planning | Team availability, sprint capacity in story points |
| Sprint Backlog | Selected stories + tasks for the sprint |
| Task Breakdown | Splitting stories into technical tasks (hours) |

---

### Assignment 5: Sprint Execution *(2 Slots)*

> [!note] Unit 3 → [[Unit-3|See detailed notes]]

| Topic | Details |
|-------|---------|
| Daily Scrum | 15-minute standup: What did I do? What will I do? Blockers? |
| Sprint Tracking | Updating task board, moving cards |
| Burndown Chart | X-axis: days; Y-axis: remaining story points; ideal line vs actual |
| Burnup Chart | Tracks completed work vs total scope |
| Velocity Metrics | Sprint velocity, rolling average, predictability |
| Impediment Resolution | Scrum Master's role in removing blockers |
| WIP Limits | Work in Progress limits on Kanban boards |
| Sprint Goal | Maintaining focus on the sprint goal |

---

### Assignment 6: Testing & Quality *(2 Slots)*

> [!note] Unit 4 → [[Unit-4|See detailed notes]]

| Topic | Details |
|-------|---------|
| Unit Testing | Purpose, test anatomy (Arrange-Act-Assert) |
| JUnit (Java) | `@Test`, `assertEquals`, `@BeforeEach`, `@AfterEach` |
| PyTest (Python) | `def test_*`, `assert`, fixtures, parametrize |
| Test Coverage | Line, branch, statement coverage |
| CI/CD Basics | What is CI? What is CD? Why it matters in Agile |
| GitHub Actions | `.github/workflows/`, YAML syntax, jobs, steps |
| Basic Pipeline | Trigger → Checkout → Install → Test → Build |
| Code Review | Pull request process, review checklist, constructive feedback |
| Static Analysis | Linters, code quality tools |

---

### Assignment 7: Sprint Review & Demo *(2 Slots)*

> [!note] Unit 5 → [[Unit-5|See detailed notes]]

| Topic | Details |
|-------|---------|
| Sprint Review | Purpose, attendees (PO, team, stakeholders), time-box |
| Working Increment | Demonstrating only "done" stories |
| Demo Preparation | Scripting the demo, test data, environment setup |
| Stakeholder Feedback | Collecting feedback, updating backlog based on feedback |
| Backlog Refinement | Grooming, splitting, re-estimating, re-prioritizing |
| Sprint Review vs Retrospective | Review = product; Retrospective = process |
| Acceptance | Product Owner accepts/rejects stories |

---

### Assignment 8: Sprint Retrospective *(1 Slot)*

> [!note] Unit 5 → [[Unit-5|See detailed notes]]

| Topic | Details |
|-------|---------|
| Retrospective Purpose | Inspect team process, adapt for improvement |
| Start-Stop-Continue | What to start doing, stop doing, continue doing |
| 4Ls Format | Liked, Learned, Lacked, Longed for |
| Mad-Sad-Glad | Emotional temperature check format |
| Action Items | Concrete, assignable improvements from retro |
| Continuous Improvement | Kaizen mindset, incremental process enhancement |
| Psychological Safety | Creating safe environment for honest feedback |
| Metrics Review | Velocity trend, defect rate, team health |

---

## ️ Unit → Assignment Mapping

| Unit | Assignments | Slots | Key Focus |
|------|-------------|-------|-----------|
| [[Unit-1\|Unit 1: Agile Fundamentals]] | 1, 2 | 3 slots | Manifesto, User Stories, DoR/DoD |
| [[Unit-2\|Unit 2: Planning & Estimation]] | 3, 4 | 3 slots | MoSCoW, Story Points, Planning Poker |
| [[Unit-3\|Unit 3: Sprint Execution]] | 5 | 2 slots | Daily Scrum, Burndown, Velocity |
| [[Unit-4\|Unit 4: Quality Assurance]] | 6 | 2 slots | Unit Tests, CI/CD, Code Review |
| [[Unit-5\|Unit 5: Review & Retro]] | 7, 8 | 3 slots | Sprint Review, Demo, Retrospective |

---

## ️ Tools & Technologies

| Tool | Purpose | Used In |
|------|---------|---------|
| Git / GitHub | Version control, CI/CD | All units |
| Jira / Azure DevOps | Agile boards, backlog management | Units 1-3 |
| JUnit 5 | Java unit testing | Unit 4 |
| PyTest | Python unit testing | Unit 4 |
| GitHub Actions | CI/CD pipeline | Unit 4 |

---

##  Reference Books

| # | Title | Author |
|---|-------|--------|
| 1 | Agile Estimating and Planning | Mike Cohn |
| 2 | Scrum: The Art of Doing Twice the Work in Half the Time | Jeff Sutherland |
| 3 | Succeeding with Agile | Mike Cohn |
| 4 | Agile Testing: A Practical Guide | Lisa Crispin & Janet Gregory |

---

##  Related Notes

- [[Overview|Subject Overview]]
- [[Unit-1|Unit 1: Agile Fundamentals]]
- [[Unit-2|Unit 2: Planning & Estimation]]
- [[Unit-3|Unit 3: Sprint Execution]]
- [[Unit-4|Unit 4: Quality Assurance]]
- [[Unit-5|Unit 5: Review & Retrospective]]
- [[Important-Questions]]
- [[Revision]]
- [[Interview-Prep]]
