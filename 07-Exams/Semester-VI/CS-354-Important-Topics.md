---
title: "CS-354 Compiler Construction - Important Topics"
subject: CS-354
semester: VI
tags:
  - important-topics
  - compiler
  - first-follow
  - ll1-parsing
  - slr
  - code-optimization
  - semester-vi
  - exam
aliases:
  - Compiler Important
  - CS354 Must-Know
created: 2026-06-16
type: important-topics
---

[[00-Dashboard/Home|Home]] | [[07-Exams/Exams-Dashboard|Exams Dashboard]]


# CS-354 Compiler Construction - Important Topics

> [!important] Exam Focus
> Compiler is the most numerical paper in Sem VI. FIRST/FOLLOW computation and LL(1) table construction alone can carry 15-20 marks. Master the algorithms before anything else.

---

## Top 10 Most Important Topics

| # | Topic | Description | Probability |
|---|-------|-------------|-------------|
| 1 | **FIRST & FOLLOW Sets** | Manual computation on given grammar |  |
| 2 | **LL(1) Parsing Table** | Build table using FIRST/FOLLOW, trace parsing |  |
| 3 | **Shift-Reduce Parsing** | Manual trace using stack + input |  |
| 4 | **Parse Tree + Derivation** | LMD, RMD, parse tree for given string |  |
| 5 | **Ambiguous Grammar** | Identify ambiguity, resolve using precedence |  |
| 6 | **Three-Address Code** | Generate TAC from expressions/code |  |
| 7 | **Code Optimization Techniques** | CSE, constant folding, dead code elimination |  |
| 8 | **SLR vs CLR vs LALR** | Comparison, differences, LR items |  |
| 9 | **Compiler Phases** | All 6 phases with inputs/outputs |  |
| 10 | **Lexical Analysis** | Tokenize given source code |  |

---

## "Definitely Going to Come" Section

> [!warning] Near-Certain Exam Questions
> 1. **Compute FIRST and FOLLOW** for a given grammar (5-6 productions) - numerical
> 2. **Construct LL(1) parsing table** and **trace parsing** of a string
> 3. **Shift-reduce parsing trace** - stack + input + action table
> 4. **Derive parse tree** and show LMD and RMD for given grammar and string
> 5. **Identify if grammar is ambiguous** and fix it
> 6. **Generate Three-Address Code** from arithmetic/conditional expression
> 7. **List and explain code optimization techniques** with before/after examples

---

## Must-Know Definitions

| Term | Definition |
|------|-----------|
| **Token** | Basic lexical unit - keyword, identifier, operator, literal |
| **Lexeme** | Actual string in source code matching a token pattern |
| **Parse Tree** | Tree showing derivation of string from grammar |
| **AST** | Abstract Syntax Tree - simplified parse tree, no redundant nodes |
| **LMD** | Leftmost Derivation - always expand leftmost non-terminal |
| **RMD** | Rightmost Derivation - always expand rightmost non-terminal |
| **Ambiguous Grammar** | Grammar where some string has ≥ 2 parse trees |
| **FIRST(α)** | Set of terminals that begin strings derivable from α |
| **FOLLOW(A)** | Set of terminals that can appear right after A |
| **LL(1)** | Left-to-right scan, Leftmost derivation, 1 token lookahead |
| **LR Parsing** | Bottom-up: Left-to-right, Rightmost derivation in reverse |
| **Handle** | Rightmost production used to reduce in shift-reduce parsing |
| **TAC** | Three-Address Code - max one operator per instruction |
| **Basic Block** | Max straight-line code with no branches in/out |

---

## Key Algorithms to Remember

### Algorithm: FIRST Set Computation
```
For terminal a: FIRST(a) = {a}
For A → ε:     FIRST(A) includes ε
For A → X₁X₂...Xₙ:
  Add FIRST(X₁) - {ε}
  If ε ∈ FIRST(X₁): Add FIRST(X₂) - {ε}
  If ε ∈ FIRST(X₁) and FIRST(X₂): Add FIRST(X₃) - {ε}
  ...
  If ε ∈ FIRST(all Xᵢ): Add ε
```

### Algorithm: FOLLOW Set Computation
```
FOLLOW(S) = {$}
For each production A → αBβ:
  Add FIRST(β) - {ε} to FOLLOW(B)
  If ε ∈ FIRST(β): Add FOLLOW(A) to FOLLOW(B)
For each production A → αB:
  Add FOLLOW(A) to FOLLOW(B)
Repeat until no changes
```

### Algorithm: LL(1) Table Construction
```
For each production A → α:
  For each a in FIRST(α) - {ε}: M[A, a] = A → α
  If ε ∈ FIRST(α):
    For each b in FOLLOW(A): M[A, b] = A → α
```

### Algorithm: Shift-Reduce Parsing
```
Stack: $   Input: w$
While True:
  Let a = next input symbol
  Let s = top of stack
  If action[s, a] = shift t:
    Push (a, t); advance input
  Elif action[s, a] = reduce A → β:
    Pop |β| pairs; goto[top, A] → push A and new state
  Elif action[s, a] = accept: DONE
  Else: ERROR
```

---

## Quick Formulas & Key Facts

| Fact | Detail |
|------|--------|
| LL(1) condition | No cell in parsing table has more than 1 entry |
| SLR uses | FOLLOW sets for reduce decisions |
| CLR uses | Lookahead in LR(1) items directly |
| LALR merges | CLR states with same core (different lookahead) |
| TAC form | `result = operand1 op operand2` |
| Quadruples | (op, arg1, arg2, result) |
| Triples | (op, arg1, arg2) - no explicit result |

---

## FIRST & FOLLOW Practice Template

**Standard Grammar to Practice:**
```
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → ( E ) | id
```

**Results to memorize:**
```
FIRST(F) = {(, id}      FOLLOW(F) = {*, +, ), $}
FIRST(T) = {(, id}      FOLLOW(T) = {+, ), $}
FIRST(E) = {(, id}      FOLLOW(E) = {), $}
FIRST(T') = {*, ε}      FOLLOW(T') = {+, ), $}
FIRST(E') = {+, ε}      FOLLOW(E') = {), $}
```

---

## TAC Generation from Code

```
Expression: a = -b + c * d
TAC:
  t1 = -b           (unary minus)
  t2 = c * d
  t3 = t1 + t2
  a  = t3

if-else: if (x > 0) { y = 1 } else { y = -1 }
TAC:
  if x > 0 goto L1
  y = -1
  goto L2
L1: y = 1
L2: ...
```

---

## Common Mistakes to Avoid

> [!warning] Critical Errors to Avoid
> - **FIRST of non-terminal:** Don't put the non-terminal itself - always drill down to terminals.
> - **FOLLOW of start symbol:** Always includes `$`. Never forget this!
> - **ε in FIRST:** Only add ε to FOLLOW computation - don't put ε in FOLLOW set itself.
> - **Ambiguous grammar ≠ wrong grammar:** Ambiguous grammars can be valid but problematic for parsers.
> - **LL(1) conflicts:** If grammar is left-recursive or not left-factored, LL(1) table will have conflicts.
> - **Shift-reduce trace:** Always check BOTH shift and reduce possibilities; choose action from table.
> - **LR(0) vs LR(1) items:** LR(0) items have no lookahead; LR(1) items have one lookahead symbol after the comma.

---

## Phases of Compiler - Quick Reference

| Phase | Input | Output | Key Activity |
|-------|-------|--------|-------------|
| Lexical Analysis | Source code | Token stream | Tokenization |
| Syntax Analysis | Tokens | Parse tree | Grammar checking |
| Semantic Analysis | Parse tree | Annotated AST | Type checking |
| Intermediate Code Gen | AST | TAC | Code abstraction |
| Code Optimization | TAC | Optimized TAC | Performance |
| Code Generation | Optimized TAC | Machine code | Target mapping |

---

*Tags: CS-354 Compiler Construction | Semester VI | [[07-Exams/Exams-Dashboard|Exams]]*
