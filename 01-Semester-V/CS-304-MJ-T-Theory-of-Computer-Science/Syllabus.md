---
title: "CS-304 Theory of Computer Science - Complete Syllabus"
subject_code: "CS-304-MJ-T"
course_type: "Major"
semester: "V"
credits: 2
teaching_hours: "2 Hours/Week"
exam_marks: "IE: 15 | EE: 35 | Total: 50"
tags:
  - cs-304
  - theory-of-computer-science
  - tcs
  - automata
  - formal-languages
  - semester-v
  - syllabus
aliases:
  - "TCS Syllabus"
  - "CS304 Syllabus"
  - "Automata Theory Syllabus"
status: "not-started"
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-304 Theory of Computer Science - Complete Syllabus

> [!info] Course Information
> **Semester:** V | **Credits:** 2 | **IE:** 15 | **EE:** 35
> **Teaching:** 2 Hours/Week | **Total:** 30 Hours

## Prerequisites
- Knowledge of Sets, relations, functions, and logic in discrete mathematics
- Fundamental algorithms and data structures
- Basic knowledge of programming concepts

## Course Objectives
- Introduce the **mathematical foundations of computation**
- Examine computational complexity of algorithms and problems
- Learn about **grammars and formal languages**
- Gain knowledge of formal computation models like **Turing machines and automata**
- Develop strong problem-solving and proof-building abilities

## Course Outcomes (COs)

| CO | Description |
|----|-------------|
| CO1 | Utilize grammars, automata, and formal language principles to simulate computational issues |
| CO2 | Sort or classify issues according to decidability and computability |
| CO3 | Understand theoretical ideas applied to cryptography, algorithms, AI and compilers |
| CO4 | Build formal proofs for decidability, complexity, and language recognition |
| CO5 | Understand Turing machines design and finite automata |
| CO6 | Use formal languages and automata to model real world problems |

## Chapter-wise Syllabus

### Chapter 1: Finite Automaton *(8 Hours)* 
→ [[Unit-1|Unit 1 Notes]]

| Section | Topics |
|---------|--------|
| 1.1 | **Introduction**: Symbol, Alphabet, String, Prefix and Suffix of Strings |
| 1.2 | **DFA** (Deterministic Finite Automaton): Definition and Examples |
| 1.3 | **NFA** (Nondeterministic Finite Automaton): Definition and Examples |
| 1.4 | **NFA to DFA Conversion** (without Epsilon) |
| 1.5 | **Finite Automaton with Output**: Moore machine and Mealy machine (Definitions, Examples) |
| 1.6 | Difference between Moore machine and Mealy machine |
| 1.7 | **Minimization of DFA**: Algorithm and Problems using Table Method |

> [!tip] Connection to Compiler Construction
> FA concepts from this chapter are **directly used in CS-354** for Lexical Analysis (token recognition)

### Chapter 2: Regular Expressions and Languages *(6 Hours)*
→ [[Unit-2|Unit 2 Notes]]

| Section | Topics |
|---------|--------|
| 2.1 | **Regular Expressions (RE)**: Definition and Examples |
| 2.2 | **Regular Language**: Definition and Examples |
| 2.3 | **Conversion of RE to FA**: Examples |
| 2.4 | **Pumping Lemma** for regular languages and applications |

### Chapter 3: Context-Free Grammars and Languages *(5 Hours)*
→ [[Unit-3|Unit 3 Notes]]

> [!note] Connection to CS-354
> This chapter is the direct prerequisite for CS-354 Compiler Construction Chapter 1

| Section | Topics |
|---------|--------|
| 3.1 | **CFG Definition**: Non-terminals, Terminals, Production Rules, Start Symbol |
| 3.2 | **Simplification of CFG**: Removing Useless Symbols, Unit Productions, ε-productions, Nullable Symbols |
| 3.3 | **Normal Forms**: **CNF** (Chomsky Normal Form) with Examples |
| 3.4 | **GNF** (Greibach Normal Form) with Examples |

### Chapter 4: Push Down Automata *(5 Hours)*
→ [[Unit-4|Unit 4 Notes]]

| Section | Topics |
|---------|--------|
| 4.1 | **PDA Definition** and Examples |
| 4.2 | **Construction of PDA** using empty stack and final state method: Examples using stack method |

### Chapter 5: Turing Machine *(6 Hours)*
→ [[Unit-5|Unit 5 Notes]]

| Section | Topics |
|---------|--------|
| 5.1 | **The Turing Machine Model**: Definition and Design |
| 5.2 | Problems on language recognizers |
| 5.3 | Language accepted by TM |

## Reference Books

| # | Book | Author | Publisher |
|---|------|--------|-----------|
| R1 | Introduction to the Theory of Computation | Michael Sipser | Cengage |
| R2 | Introduction to Automata Theory, Languages and Computation | Hopcroft, Motwani, Ullman | Pearson |
| R3 | Theory of Computer Science: Automata, Languages and Computation | K.L.P. Mishra, N. Chandrasekaran | PHI |
| R4 | Introduction to Languages and Theory of Computation | John C. Martin | McGraw-Hill |
| R5 | Languages and Machines | Thomas A. Sudkamp | - |

## Most Important Topics for Exam

> [!warning] Always in Exam
> 1. **DFA/NFA construction** from given language description
> 2. **NFA to DFA conversion** (subset construction method)
> 3. **DFA Minimization** using table method
> 4. **Regular Expression to FA** conversion
> 5. **Pumping Lemma** to prove a language is not regular
> 6. **CFG simplification** (removing useless productions, ε, unit)
> 7. **CNF conversion** from given CFG
> 8. **PDA construction** for given CFL
> 9. **Turing Machine design** for simple languages
> 10. **Moore vs Mealy** machine differences and conversions

## Chomsky Hierarchy (Quick Reference)

| Type | Grammar | Language | Automaton |
|------|---------|----------|-----------|
| Type 0 | Unrestricted | Recursively Enumerable | Turing Machine |
| Type 1 | Context-Sensitive | Context-Sensitive | LBA |
| Type 2 | Context-Free | Context-Free | PDA |
| Type 3 | Regular | Regular | DFA/NFA |

## Quick Navigation

| File | Purpose |
|------|---------|
| [[Overview|Overview.md]] | Subject overview |
| [[Unit-1|Unit 1: Finite Automaton]] | DFA, NFA, Moore, Mealy, Minimization |
| [[Unit-2|Unit 2: Regular Expressions]] | RE, Regular languages, Pumping Lemma |
| [[Unit-3|Unit 3: Context-Free Grammars]] | CFG, Simplification, CNF, GNF |
| [[Unit-4|Unit 4: Push Down Automata]] | PDA construction |
| [[Unit-5|Unit 5: Turing Machine]] | TM model and design |
| [[Important-Questions|Important Questions]] | Exam Q&A |
| [[Revision|Revision Notes]] | Quick revision |
| [[Interview-Prep|Interview Prep]] | TCS interview questions |
| [[Home| Dashboard]] | Main vault dashboard |

---
*← [[01-Semester-V/CS-303-MJ-T-Web-Technology-I/Syllabus|CS-303 Web I]] | [[Home| Dashboard]] | [[01-Semester-V/CS-307-MJ-T-Data-Science-Analytics/Syllabus|CS-307 Data Science →]]*
