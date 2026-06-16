---
title: "CS-304-MJ-T Theory of Computer Science - Overview"
aliases: ["TCS", "CS304", "Theory of Computation", "TOC Overview"]
tags:
  - subject/theory-of-computation
  - semester/V
  - cs/automata
  - cs/formal-languages
  - overview
subject_code: CS-304-MJ-T
subject_name: "Theory of Computer Science"
semester: V
type: overview
credits: 4
last_reviewed: 2026-06-16
---

#  CS-304-MJ-T - Theory of Computer Science

> [!important] Subject at a Glance
> Theory of Computer Science (TOC / TCS) is the mathematical foundation of computing - studying what problems computers **can** and **cannot** solve, and how efficiently. It covers automata, formal languages, grammars, and Turing machines.

---

##  Subject Information

| Field           | Details                                  |
|-----------------|------------------------------------------|
| Subject Code    | CS-304-MJ-T                              |
| Subject Name    | Theory of Computer Science               |
| Semester        | V (Third Year)                           |
| Type            | Major Theory                             |
| Total Chapters  | 5                                        |
| Reference Books | See [[Syllabus|CS-304 Syllabus]]                  |

---

## ️ Chapter Overview

```mermaid
mindmap
  root((Theory of Computer Science))
    Ch1[Chapter 1: Finite Automata]
      Symbols & Alphabets
      DFA
      NFA
      NFA to DFA Conversion
      Moore & Mealy Machines
      DFA Minimization
    Ch2[Chapter 2: Regular Expressions]
      RE Definitions
      Regular Languages
      RE to FA Conversion
      Pumping Lemma
    Ch3[Chapter 3: CFG & CFL]
      Context-Free Grammars
      CFG Simplification
      CNF
      GNF
    Ch4[Chapter 4: Push Down Automata]
      PDA Definition
      Empty Stack Method
      Final State Method
    Ch5[Chapter 5: Turing Machine]
      TM Model
      TM Design
      Language Recognizers
      Accepted Languages
```

---

##  Unit Notes

| Unit | Topic | Hours | Notes | Status |
|------|-------|-------|-------|--------|
| 1 | Finite Automata | 8H | [[Unit-1]] |  |
| 2 | Regular Expressions & Languages | 6H | [[Unit-2]] |  |
| 3 | Context-Free Grammars & Languages | 5H | [[Unit-3]] |  |
| 4 | Push Down Automata | 5H | [[Unit-4]] |  |
| 5 | Turing Machine | 6H | [[Unit-5]] |  |

---

##  Learning Objectives

By the end of this course, students will be able to:

- [ ] Define and differentiate symbols, alphabets, strings, and languages
- [ ] Construct DFAs and NFAs for given languages
- [ ] Convert NFA to equivalent DFA
- [ ] Design and convert Moore and Mealy machines
- [ ] Minimize a DFA using the Table (Myhill-Nerode) method
- [ ] Write and interpret regular expressions
- [ ] Prove languages are non-regular using the Pumping Lemma
- [ ] Define context-free grammars and simplify them
- [ ] Convert CFGs to CNF and GNF
- [ ] Construct push-down automata using empty stack and final state methods
- [ ] Design Turing machines for language recognition

---

##  Chomsky Hierarchy - Big Picture

> [!note] The Chomsky Hierarchy
> All formal languages are classified in a hierarchy of expressive power:

```mermaid
graph TD
    A["Type 0: Recursively Enumerable Languages\n(Turing Machines)"]
    B["Type 1: Context-Sensitive Languages\n(Linear-Bounded Automata)"]
    C["Type 2: Context-Free Languages\n(Push-Down Automata)"]
    D["Type 3: Regular Languages\n(Finite Automata)"]
    A --> B --> C --> D
```

| Type | Grammar | Automaton | Example |
|------|---------|-----------|---------|
| Type 3 | Regular | DFA / NFA | `aⁿbⁿ` - NO; `(ab)*` - YES |
| Type 2 | Context-Free | PDA | `aⁿbⁿ` - YES |
| Type 1 | Context-Sensitive | LBA | `aⁿbⁿcⁿ` - YES |
| Type 0 | Unrestricted | Turing Machine | Halting Problem - NO |

---

##  Quick Links

- [[Syllabus|CS-304 Syllabus]] - Full syllabus with reference books
- [[Unit-1]] - Finite Automata (DFA, NFA, Moore, Mealy)
- [[Unit-2]] - Regular Expressions & Pumping Lemma
- [[Unit-3]] - Context-Free Grammars & Languages
- [[Unit-4]] - Push Down Automata
- [[Unit-5]] - Turing Machine
- [[Important-Questions|CS-304 Important-Questions]] - Exam-focused Q&A
- [[Revision|CS-304 Revision]] - Quick revision notes
- [[Interview-Prep|CS-304 Interview-Prep]] - Interview preparation

---

##  Reference Books

| # | Book | Author |
|---|------|--------|
| 1 | Introduction to the Theory of Computation | Michael Sipser |
| 2 | Introduction to Automata Theory, Languages, and Computation | Hopcroft, Motwani, Ullman |
| 3 | Theory of Computer Science: Automata, Languages and Computation | K.L.P. Mishra & N. Chandrasekaran |
| 4 | Introduction to Languages and the Theory of Computation | John C. Martin |

---

##  Study Plan

```mermaid
gantt
    title CS-304 Study Timeline
    dateFormat  YYYY-MM-DD
    section Chapter 1
    Finite Automata (8H)        :a1, 2026-06-17, 5d
    section Chapter 2
    Regular Expressions (6H)    :a2, after a1, 4d
    section Chapter 3
    CFG & Languages (5H)        :a3, after a2, 4d
    section Chapter 4
    Push Down Automata (5H)     :a4, after a3, 3d
    section Chapter 5
    Turing Machine (6H)         :a5, after a4, 4d
    section Revision
    Full Revision               :a6, after a5, 3d
```

---

*Last Updated: 2026-06-16 | Semester V | CS-304-MJ-T*
