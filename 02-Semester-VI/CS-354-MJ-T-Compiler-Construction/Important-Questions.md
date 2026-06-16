---
title: "Compiler Construction - Important Questions"
subject: "CS-354-MJ-T"
semester: VI
type: important-questions
tags:
  - compiler-construction
  - exam-prep
  - important-questions
  - semester-vi
aliases:
  - "CC IQ"
created: 2026-06-16
updated: 2026-06-16
---

#  CS-354-MJ-T - Compiler Construction Important Questions

> [!warning] Exam Focus
> Unit 4 (Parser) carries the most weight. FIRST/FOLLOW computation, LL(1) table construction, and SLR table construction are **almost always in exams**. Always show full working.

##  Unit 1 - CFG and Languages

### 2-Mark Questions
1. Define Context-Free Grammar (CFG).
2. What is a parse tree?
3. What is an ambiguous grammar?
4. Define leftmost derivation (LMD) and rightmost derivation (RMD).
5. Where do CFGs fit in the Chomsky hierarchy?

### 5-Mark Questions
6.  Show the leftmost and rightmost derivations of `id + id * id` for the expression grammar.
7.  Show that the grammar `E → E + E | E * E | id` is ambiguous by showing two parse trees for `id + id * id`.
8.  Rewrite the grammar `E → E + E | E * E | id` to eliminate ambiguity (apply precedence and associativity).
9. Explain operator precedence and operator associativity as tools for resolving grammar ambiguity.
10. Construct a CFG for the language of balanced parentheses {(), (()), (())(), ...}.

### 10-Mark Questions
11.  Define CFG formally. Explain parse tree, LMD, RMD, and ambiguity with examples. Resolve the dangling-else ambiguity.
12. Write a CFG for arithmetic expressions involving +, -, *, / and show parse trees.

---

##  Unit 2 - Introduction to Compiler

### 2-Mark Questions
1. Define a compiler. How is it different from an interpreter?
2. What are the six phases of a compiler?
3. What is the role of the Symbol Table?
4. What is a cross compiler? Give an example.
5. What is bootstrapping?

### 5-Mark Questions
6.  Draw and explain the structure of a compiler showing all six phases with input/output at each phase.
7.  Trace the compilation of `position = initial + rate * 60` through all phases.
8. Explain the role of the Error Handler. Name 4 types of compilation errors.
9. What is a Symbol Table? How is it implemented? What information does it store?
10. Compare one-pass, two-pass, and cross compilers.

### 10-Mark Questions
11.  Explain all six phases of a compiler in detail with a complete example showing data transformation from source code to machine code.
12. Explain front-end vs back-end of a compiler. Why is this division important?

---

##  Unit 3 - Lexical Analysis

### 2-Mark Questions
1. Define token, lexeme, and pattern with one example each.
2. What is the role of a lexer?
3. What is a transition diagram?
4. What is the difference between DFA and NFA?
5. Name two types of lexical errors.

### 5-Mark Questions
6.  Draw a DFA (transition diagram) for recognizing identifiers (letters/digits, starts with letter).
7.  Draw a transition diagram for recognizing relational operators: `<`, `<=`, `>`, `>=`, `=`, `<>`.
8. List the tokens in the statement: `int count = 10 + 20;` and classify each.
9. Explain the algorithm for scanning an identifier including keyword recognition.
10. What is the two-buffer input scheme? Why is it used?

### 10-Mark Questions
11.  Explain lexical analysis in detail: role of lexer, tokens/lexemes/patterns, DFA for identifier recognition, number recognition, and error handling.
12. Draw DFAs for: (a) identifiers, (b) integers, (c) floating-point numbers, (d) string literals.

---

##  Unit 4 - Syntax Analysis (Largest Unit - Most Questions)

### 2-Mark Questions
1. What is left recursion? Give an example.
2. What is left factoring?
3. Define FIRST(A) for a non-terminal A.
4. Define FOLLOW(A) for a non-terminal A.
5. What is an LL(1) grammar?
6. What is a handle in bottom-up parsing?
7. What is shift-reduce parsing?
8. What are LR(0) items?
9. What is the difference between SLR and LALR parsers?
10. What is a reduce-reduce conflict?

### 5-Mark Questions
11.  Eliminate left recursion from: `E → E + T | T`, `T → T * F | F`.
12.  Apply left factoring to: `S → if E then S | if E then S else S | other`.
13.  Compute FIRST and FOLLOW sets for: `E → TE'`, `E' → +TE'|ε`, `T → FT'`, `T' → *FT'|ε`, `F → (E)|id`.
14.  Construct the LL(1) parsing table for the above expression grammar.
15.  Trace LL(1) parsing of `id * id + id` using the expression grammar.
16.  Write the SLR parsing algorithm (shift-reduce with ACTION/GOTO table).
17. Explain recursive descent parser with code for parsing expressions.
18. What is the difference between top-down and bottom-up parsing?
19. Explain operator precedence parser. Give the precedence table for +, *, id, (, ), $.
20. What is LALR parser? How is it derived from CLR?

### 10-Mark Questions
21.  For grammar `E → E+T|T`, `T → T*F|F`, `F → (E)|id`:
    a. Eliminate left recursion
    b. Compute FIRST and FOLLOW sets
    c. Construct LL(1) parsing table
    d. Trace parsing of `id+id*id`

22.  For augmented grammar `S'→E`, `E→E+T|T`, `T→T*F|F`, `F→(E)|id`:
    a. Build all LR(0) states (items)
    b. Construct SLR ACTION/GOTO table
    c. Trace parsing of `id+id*id`

23.  Explain all types of LR parsers (SLR, CLR, LALR) - construction, power, and when each is used.
24. What is left recursion? Explain direct and indirect left recursion with elimination algorithms and examples.

---

##  Unit 5 - Code Generation & Optimization

### 2-Mark Questions
1. What is postfix notation?
2. What are quadruples?
3. What is common sub-expression elimination?
4. What is dead code elimination?
5. What is strength reduction?

### 5-Mark Questions
6.  Convert `(a + b) * (a + b) - c * d` to three-address code.
7.  Convert `a + b * c - d / e` to postfix notation. Show stack operations.
8.  Generate quadruples for `a = -b * (c + d)`.
9. Explain loop invariant code motion and frequency reduction with an example.
10. What is a DAG? Draw a DAG for `a + a * (b - c) + (b - c) * d`.

### 10-Mark Questions
11.  Explain intermediate code representations: three-address code, postfix, quadruples, triples, and expression trees with examples.
12. Explain the following code optimization techniques with examples: (a) constant folding, (b) CSE, (c) dead code elimination, (d) loop invariant motion, (e) strength reduction.

---

##  Most Critical Problems (Must Practice)

> [!important] These 5 problems appear EVERY YEAR
> 1. **FIRST & FOLLOW** computation for given grammar
> 2. **LL(1) parsing table** construction
> 3. **LL(1) parsing trace** for given input
> 4. **LR(0) items** construction
> 5. **SLR ACTION/GOTO table** construction

---
*CS-354-MJ-T Compiler Construction | Important Questions | Semester VI*
