---
title: "CS-354 Compiler Construction - Expected PYQ"
subject: CS-354
paper: Compiler Construction
semester: VI
tags:
  - pyq
  - compiler
  - parsing
  - lexical-analysis
  - first-follow
  - ll1
  - slr
  - code-optimization
  - semester-vi
  - exam
aliases:
  - Compiler PYQ
  - CS354 Questions
created: 2026-06-16
type: pyq
---

#  CS-354 Compiler Construction - Expected PYQ

> [!important] Exam Strategy
> Compiler is highly numerical! FIRST & FOLLOW computation, LL(1) table construction, and SLR parsing are guaranteed. Lexical analysis theory, ambiguous grammar, and code optimization are important for theory marks. Master the algorithms step by step.

---

## ️ Unit-wise Distribution

| Unit | Topic | Weightage |
|------|-------|-----------|
| I | Intro, Lexical Analysis | 15% |
| II | Syntax Analysis - CFG, Parsing | 20% |
| III | FIRST, FOLLOW, LL(1) | 25% |
| IV | Bottom-Up Parsing - SLR/CLR/LALR | 20% |
| V | Semantic Analysis & Code Gen | 20% |

---

## ️ Section A - Short Answer (2 Marks)

1. **What are the phases of a compiler? List them in order.**
2. **What is a token? Give examples of token types.**
3. **Difference between a compiler and an interpreter.**
4. **What is a parse tree? How does it differ from a derivation?**
5. **Define Leftmost Derivation (LMD) and Rightmost Derivation (RMD).**
6. **What is an ambiguous grammar? Give an example.**
7. **What is FIRST set? Define formally.**
8. **What is FOLLOW set? Define formally.**
9. **What is an LL(1) parser? What does "LL(1)" stand for?**
10. **What is a predictive parsing table?**
11. **What is a shift-reduce conflict?**
12. **What is the difference between SLR, CLR, and LALR parsers?**
13. **What is an LR item? What is a canonical collection?**
14. **What are semantic actions? What is an annotated parse tree?**
15. **Define synthesized and inherited attributes.**
16. **What are the types of intermediate code representations?**
17. **What is Three-Address Code (TAC)?**
18. **What is code optimization? List its types.**
19. **What is a basic block in code optimization?**
20. **What is peephole optimization?**

---

##  Section B - Long Answer / Numerical Problems (5–7 Marks)

---

### Q1. Compiler Phases ()

**Complete Compilation Pipeline:**

```
Source Code
    ↓
[1. Lexical Analyzer / Scanner]
    → Tokens
    ↓
[2. Syntax Analyzer / Parser]
    → Parse Tree (AST)
    ↓
[3. Semantic Analyzer]
    → Annotated AST, Type Checking
    ↓
[4. Intermediate Code Generator]
    → Three-Address Code / TAC
    ↓
[5. Code Optimizer]
    → Optimized TAC
    ↓
[6. Code Generator]
    → Target Code (Assembly / Machine Code)
```

**Symbol Table:** Used by phases 1-6 to store identifier information.
**Error Handler:** Used by all phases.

---

### Q2. Lexical Analysis - Tokens and Patterns ()

**Token Types:**

| Token Type | Example |
|------------|---------|
| Keyword | `int`, `if`, `for`, `while`, `return` |
| Identifier | `x`, `myVar`, `count` |
| Integer Literal | `0`, `42`, `100` |
| Float Literal | `3.14`, `0.5` |
| String Literal | `"hello"`, `"world"` |
| Operator | `+`, `-`, `*`, `/`, `=`, `==` |
| Delimiter | `(`, `)`, `{`, `}`, `;`, `,` |

**Example: Tokenize `x = a + b * 2;`**

| Token | Type |
|-------|------|
| x | Identifier |
| = | Assignment Op |
| a | Identifier |
| + | Arithmetic Op |
| b | Identifier |
| * | Arithmetic Op |
| 2 | Integer Literal |
| ; | Delimiter |

---

### Q3. Parse Tree, LMD, and RMD ()

**Grammar:** E → E + E | E * E | (E) | id

**String:** id + id * id

**Leftmost Derivation:**
```
E → E + E
  → id + E
  → id + E * E
  → id + id * E
  → id + id * id
```

**Rightmost Derivation:**
```
E → E + E
  → E + E * E
  → E + E * id
  → E + id * id
  → id + id * id
```

**Parse Tree (for id + id * id):**
```
        E
      / | \
     E  +  E
     |    / | \
    id   E  *  E
         |     |
        id    id
```

---

### Q4. Ambiguous Grammar - Detection and Resolution ()

**Ambiguous grammar:** A grammar where some string has MORE THAN ONE parse tree (or LMD/RMD).

**Example - Dangling Else Problem:**
```
S → if E then S | if E then S else S | other
```
String `if E₁ then if E₂ then S₁ else S₂` is ambiguous.

**Resolution:** Add associativity/precedence rules:
```
E → E + T | T
T → T * F | F
F → (E) | id
```
This grammar enforces: `*` before `+`, left-associativity.

---

### Q5. FIRST and FOLLOW Sets - Numerical ( VERY HIGH PROBABILITY)

**Grammar:**
```
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → ( E ) | id
```

**Computing FIRST Sets:**

*Rules for FIRST:*
1. If A → aα: FIRST(A) includes {a}
2. If A → ε: FIRST(A) includes {ε}
3. If A → B₁B₂...Bₙ: add FIRST(B₁) - {ε}; if ε ∈ FIRST(B₁), add FIRST(B₂) - {ε}; etc.

```
FIRST(F)  = { (, id }
FIRST(T') = { *, ε }
FIRST(T)  = FIRST(F) = { (, id }
FIRST(E') = { +, ε }
FIRST(E)  = FIRST(T) = { (, id }
```

**Computing FOLLOW Sets:**

*Rules for FOLLOW:*
1. FOLLOW(S) = {$}  ($ = end-of-input marker)
2. If A → αBβ: add FIRST(β) - {ε} to FOLLOW(B)
3. If A → αBβ and ε ∈ FIRST(β): add FOLLOW(A) to FOLLOW(B)
4. If A → αB: add FOLLOW(A) to FOLLOW(B)

```
FOLLOW(E)  = { ), $ }
FOLLOW(E') = FOLLOW(E) = { ), $ }
FOLLOW(T)  = FIRST(E') - {ε} ∪ FOLLOW(E') = { +, ), $ }
FOLLOW(T') = FOLLOW(T) = { +, ), $ }
FOLLOW(F)  = FIRST(T') - {ε} ∪ FOLLOW(T') = { *, +, ), $ }
```

---

### Q6. LL(1) Parsing Table Construction ( VERY HIGH PROBABILITY)

**LL(1) Table Rule:**
- For production A → α:
  - For each terminal a in FIRST(α): add A → α in M[A, a]
  - If ε ∈ FIRST(α): for each b in FOLLOW(A): add A → α in M[A, b]

**Parsing Table for above grammar:**

| Non-Terminal | id | + | * | ( | ) | $ |
|---|---|---|---|---|---|---|
| E | E→TE' | | | E→TE' | | |
| E' | | E'→+TE' | | | E'→ε | E'→ε |
| T | T→FT' | | | T→FT' | | |
| T' | | T'→ε | T'→*FT' | | T'→ε | T'→ε |
| F | F→id | | | F→(E) | | |

**LL(1) Parsing Trace for `id + id * id`:**

| Stack | Input | Action |
|-------|-------|--------|
| $E | id+id*id$ | Use E→TE' |
| $E'T | id+id*id$ | Use T→FT' |
| $E'T'F | id+id*id$ | Use F→id |
| $E'T'id | id+id*id$ | Match id |
| $E'T' | +id*id$ | Use T'→ε |
| $E' | +id*id$ | Use E'→+TE' |
| $E'T+ | +id*id$ | Match + |
| $E'T | id*id$ | Use T→FT' |
| $E'T'F | id*id$ | Use F→id |
| $E'T'id | id*id$ | Match id |
| $E'T' | *id$ | Use T'→*FT' |
| $E'T'F* | *id$ | Match * |
| $E'T'F | id$ | Use F→id |
| $E'T'id | id$ | Match id |
| $E'T' | $ | T'→ε |
| $E' | $ | E'→ε |
| $ | $ | ACCEPT  |

---

### Q7. SLR, CLR, LALR - Differences ()

| Feature | SLR(1) | CLR(1) | LALR(1) |
|---------|--------|--------|---------|
| Lookahead computed from | FOLLOW sets | LR(1) items | Merged CLR states |
| Power | Weakest | Strongest | Between SLR & CLR |
| States | Fewer | More | Same as SLR |
| Conflicts | More possible | Fewer | Some possible |
| Real-world use | Rare | Rare | Most practical (yacc, bison) |

**LR(0) Item Example:**
```
Production: E → E + T

LR(0) Items:
E → .E + T     (dot at start)
E → E. + T     (after E)
E → E +. T     (after +)
E → E + T.     (after T - REDUCE)
```

---

### Q8. Shift-Reduce Parsing ()

**Algorithm:**
```
Stack: $
Input: w$
Repeat:
  - If top of stack + input ⊢ SHIFT: push input symbol, advance input
  - If stack top = handle: REDUCE using appropriate production
  - If stack = $S and input = $: ACCEPT
  - Else: ERROR
```

**Trace for `id * id + id` with grammar S→S+T|T, T→T*F|F, F→id:**

| Step | Stack | Input | Action |
|------|-------|-------|--------|
| 1 | $ | id*id+id$ | Shift |
| 2 | $id | *id+id$ | Reduce F→id |
| 3 | $F | *id+id$ | Reduce T→F |
| 4 | $T | *id+id$ | Shift |
| 5 | $T* | id+id$ | Shift |
| 6 | $T*id | +id$ | Reduce F→id |
| 7 | $T*F | +id$ | Reduce T→T*F |
| 8 | $T | +id$ | Reduce S→T |
| 9 | $S | +id$ | Shift |
| 10 | $S+ | id$ | Shift |
| 11 | $S+id | $ | Reduce F→id |
| 12 | $S+F | $ | Reduce T→F |
| 13 | $S+T | $ | Reduce S→S+T |
| 14 | $S | $ | ACCEPT  |

---

### Q9. Three-Address Code (TAC) and Intermediate Code ()

**Expression:** `a = b + c * d - e`

**TAC:**
```
t1 = c * d
t2 = b + t1
t3 = t2 - e
a  = t3
```

**Quadruples form:**

| # | Op | Arg1 | Arg2 | Result |
|---|----|----|------|--------|
| 0 | * | c | d | t1 |
| 1 | + | b | t1 | t2 |
| 2 | - | t2 | e | t3 |
| 3 | = | t3 | - | a |

**Triples form:**

| # | Op | Arg1 | Arg2 |
|---|----|----|------|
| 0 | * | c | d |
| 1 | + | b | (0) |
| 2 | - | (1) | e |
| 3 | = | a | (2) |

---

### Q10. Code Optimization Techniques ()

**Local Optimizations:**

1. **Constant Folding:** `x = 3 * 4` → `x = 12`

2. **Constant Propagation:** 
   ```
   x = 5; y = x + 3  →  y = 8
   ```

3. **Dead Code Elimination:**
   ```
   x = 10;
   x = 20;   // x=10 is dead code - removed
   ```

4. **Common Subexpression Elimination (CSE):**
   ```
   t1 = a + b
   t2 = a + b  →  t2 = t1  (eliminate recomputation)
   ```

5. **Strength Reduction:** Replace expensive ops with cheaper ones
   ```
   x = y * 2  →  x = y + y  (or x = y << 1)
   ```

6. **Loop Invariant Code Motion:**
   ```
   for (i=0; i<n; i++) {
     x = a * b;    // Move outside loop!
     arr[i] = x + i;
   }
   ```

7. **Peephole Optimization:** Examine small window of instructions
   ```
   STORE R0, a     →  (eliminate: store then immediate load)
   LOAD R0, a
   ```

---

##  Most Expected Questions

> [!tip] These questions MUST be prepared
> 1.  FIRST and FOLLOW sets computation (numerical)
> 2.  LL(1) parsing table construction + parsing trace
> 3.  Shift-reduce parsing trace
> 4.  Parse tree + LMD/RMD derivation
> 5.  Ambiguous grammar identification and resolution
> 6.  SLR vs CLR vs LALR comparison table
> 7.  Three-address code generation from expression
> 8.  Code optimization techniques with examples
> 9.  Compiler phases diagram
> 10.  Lexical analysis - tokenize given source code

---

##  FIRST & FOLLOW Quick Rules

**FIRST Rules:**
- FIRST(terminal) = {terminal}
- FIRST(A → ε) includes ε
- FIRST(A → Bα): FIRST(B) - {ε}; if ε ∈ FIRST(B), also add FIRST(α)

**FOLLOW Rules:**
- FOLLOW(S) includes $
- A → αBβ: add FIRST(β) - {ε} to FOLLOW(B)
- A → αBβ, ε ∈ FIRST(β): add FOLLOW(A) to FOLLOW(B)
- A → αB: add FOLLOW(A) to FOLLOW(B)

---

*Tags: CS-354 Compiler Construction | Semester VI | [[07-Exams]]*
