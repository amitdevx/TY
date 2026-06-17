---
title: "CS-354 Unit 4 - Syntax Analysis (Parser)"
tags: [cs-354, compiler, unit-4]
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# Unit 4: Syntax Analysis (Parser)

## Introduction
Syntax analysis, or parsing, is the second phase of the compiler. It takes the token stream from the lexical analyzer and generates a parse tree or syntax tree.

## Types of Parsers
1. **Top-Down Parsers**: Construct the parse tree from the root to the leaves. Examples: Recursive Descent, LL(1).
2. **Bottom-Up Parsers**: Construct the parse tree from leaves to the root. Examples: Shift-Reduce, LR parsers.

## Top-Down Parsing
- **Backtracking**: Brute-force approach, tries all possibilities. Very inefficient.
- **Left Recursion**: A grammar is left recursive if it has a non-terminal A such that A -> A alpha. Top-down parsers can enter infinite loops.
  - Elimination: A -> A alpha | beta becomes A -> beta A', A' -> alpha A' | epsilon.
- **Left Factoring**: Used when two or more grammar rules share a common prefix.
- **Recursive Descent Parser**: A set of recursive procedures to process the input.
- **FIRST and FOLLOW Sets**:
  - FIRST(A): Set of terminals that begin strings derived from A.
  - FOLLOW(A): Set of terminals that can appear immediately to the right of A.
- **LL(1) Predictive Parser**: Uses a parsing table. No backtracking.

## Bottom-Up Parsing
- **Shift-Reduce Parsing**: Uses a stack. Actions are Shift, Reduce, Accept, Error.
- **LR Parsers**: Powerful, works for a large class of grammars.
  - SLR (Simple LR): Easiest to implement, uses FOLLOW sets.
  - CLR (Canonical LR): Most powerful, uses lookaheads.
  - LALR (Look-Ahead LR): Merges states in CLR, used in YACC.
- **Operator Precedence Parser**: Based on precedence relations between operators.
