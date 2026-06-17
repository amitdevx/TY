---
title: "CS-304 Theory of Computer Science - Important Questions"
aliases: ["CS304 Important Questions", "TCS IQ", "CS304 Exam Questions", "TOC Important Questions"]
tags:
  - subject/theory-of-computation
  - semester/V
  - exam-prep
  - important-questions
subject_code: CS-304-MJ-T
type: important-questions
last_reviewed: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-304 Theory of Computer Science - Important Questions

> [!note] Navigation
> [[Overview|CS-304 Overview]] | [[Revision|CS-304 Revision]] | [[Interview-Prep|CS-304 Interview-Prep]]

---

> [!important] Legend
>  = Most likely to appear |  = Descriptive |  = Numerical/Design |  = Proof-based

---

## Chapter 1 - Finite Automata (8H)

### Short Answer (2-3 marks)

1.  Define: (a) Symbol, (b) Alphabet, (c) String, (d) Language, (e) ε (epsilon).
2.  Define a DFA. What are its five components?
3. What is the difference between DFA and NFA?
4. Define Moore machine and Mealy machine. State one difference.
5. What is DFA minimization? Why is it needed?
6. What is the maximum number of states in a DFA derived from an NFA with n states?
7. Define δ* (extended transition function) for a DFA.

### Long Answer (5-10 marks)

8.  Construct a DFA over Σ = {a, b} that accepts all strings:
   - (a) ending with 'ab'
   - (b) containing 'aa' as substring
   - (c) with even number of a's and odd number of b's

9.  Construct an NFA for the language L = {w ∈ {a,b}* | w ends with 'abb'}. Convert it to an equivalent DFA using subset construction. Draw the transition table and diagram.

10.  Convert the following NFA to a DFA using subset construction:
    ```
    States: q₀, q₁, q₂ (q₂ = final)
    Input: {a, b}
    δ(q₀, a) = {q₀, q₁}
    δ(q₀, b) = {q₀}
    δ(q₁, b) = {q₂}
    ```

11.  Design a Moore machine that outputs:
    - 1 if the last two symbols are 'ab'
    - 0 otherwise
    Also convert it to an equivalent Mealy machine.

12.  Minimize the following DFA using the Table-Filling method:
    ```
    States: {A, B, C, D, E, F}, Start: A, Final: {C, D}
    Input: {0, 1}
    [Provide a transition table here]
    ```

13.  Construct a DFA for the following languages over Σ = {0, 1}:
    - (a) All binary strings divisible by 3
    - (b) All binary strings with an even number of 0s and even number of 1s

14.  Explain the subset construction algorithm (NFA to DFA). What is its time and space complexity?

### Numerical Practice Problems

15.  Given NFA: q₀ →a→ {q₀,q₁}, q₁ →b→ {q₂}, q₂ is accepting; Σ={a,b}. Draw DFA.
16.  Draw transition table for DFA accepting strings over {0,1} that start and end with same symbol.
17.  Design Mealy machine to output 'E'/'O' indicating even/odd number of 1s seen so far.

---

## Chapter 2 - Regular Expressions and Languages (6H)

### Short Answer (2-3 marks)

18.  Define a regular expression. Give its recursive definition.
19. What is a regular language? Give two examples.
20. State the Pumping Lemma for regular languages.
21.  Are regular languages closed under intersection and complementation? Justify.
22. Give the RE for: (a) all binary strings with at least two 1s, (b) strings starting and ending with 'a'.

### Long Answer (5-10 marks)

23.  State and prove the Pumping Lemma for regular languages. Use it to prove that L = {aⁿbⁿ | n ≥ 1} is not regular.

24.  Use the Pumping Lemma to prove the following are NOT regular:
    - (a) L = {aⁿbⁿ | n ≥ 0}
    - (b) L = {ww | w ∈ {a,b}*}
    - (c) L = {aⁿ | n is a perfect square}

25.  Convert the regular expression `(a+b)*abb` to an NFA and then to a DFA.

26.  Explain Arden's Theorem. Use it to find the RE for the DFA:
    ```
    q₀ →a→ q₀, q₀ →b→ q₁ (final)
    q₁ →a→ q₀, q₁ →b→ q₁
    ```

27.  List and prove any 5 properties/identities for regular expressions.

28.  Write regular expressions for:
    - (a) Strings over {a,b} with no two consecutive b's
    - (b) Strings over {0,1} with even number of 0s
    - (c) Valid identifiers: starts with letter, followed by letters/digits

---

## Chapter 3 - Context-Free Grammars and Languages (5H)

### Short Answer (2-3 marks)

29.  Define a Context-Free Grammar (CFG). Give its 4-tuple definition.
30. What are nullable variables? How are they identified?
31. What is a unit production? Give an example.
32. Define CNF. What is its significance?
33. Define GNF. How does it differ from CNF?
34. What is an ambiguous grammar?

### Long Answer (5-10 marks)

35.  Write a CFG for the following languages:
    - (a) L = {aⁿbⁿ | n ≥ 1}
    - (b) L = palindromes over {a, b}
    - (c) L = {ww^R | w ∈ {a,b}*}
    - (d) Balanced parentheses

36.  Simplify the following CFG by removing ε-productions, unit productions, and useless symbols:
    ```
    S → aAbB
    A → a | aA | ε
    B → b | bB | ε
    C → cC (useless)
    ```

37.  Convert the following CFG to Chomsky Normal Form (CNF):
    ```
    S → aABb | ab
    A → aA | a
    B → bB | b
    ```

38.  Convert the given CFG to Greibach Normal Form (GNF):
    ```
    S → AB | a
    A → a | aS
    B → b
    ```

39.  Explain leftmost and rightmost derivations. Show both for the string "id + id * id" using the arithmetic expression grammar.

---

## Chapter 4 - Push Down Automata (5H)

### Short Answer (2-3 marks)

40.  Define a PDA. Give its 7-tuple definition.
41. What is the role of the stack in a PDA?
42. What are the two methods of acceptance in PDA?
43. What is an Instantaneous Description (ID) of a PDA?
44. What is the relationship between PDAs and CFGs?

### Long Answer (5-10 marks)

45.  Construct a PDA by empty stack for L = {aⁿbⁿ | n ≥ 1}. Show the trace for input "aaabbb".

46.  Construct a PDA by final state for L = {aⁿbⁿ | n ≥ 0}. Draw the transition diagram and table.

47.  Construct a PDA for the following languages:
    - (a) L = {ww^R | w ∈ {a,b}*} (palindromes)
    - (b) L = {w ∈ {a,b}* | #a(w) = #b(w)}
    - (c) L = {aⁿbᵐ | n ≤ m}

48.  Prove that acceptance by empty stack and acceptance by final state are equivalent for PDAs.

49.  Using the CFG to PDA construction, design a PDA for:
    ```
    CFG: S → aSb | ab
    ```
    Show a complete trace for the string "aabb".

---

## Chapter 5 - Turing Machine (6H)

### Short Answer (2-3 marks)

50.  Define a Turing Machine. Give its 7-tuple definition.
51. What are the three possible outcomes when a TM processes an input?
52. Define: (a) Recursive language, (b) Recursively Enumerable language.
53. What is the Halting Problem? Why is it undecidable?
54. Is every CFL a recursive language? Justify.

### Long Answer (5-10 marks)

55.  Design a Turing Machine that accepts L = {aⁿbⁿ | n ≥ 1}. Give:
    - Complete state diagram or transition table
    - Trace execution for input "aabb"

56.  Design a Turing Machine for:
    - (a) L = {ww^R | w ∈ {a,b}*} (palindromes)
    - (b) Computing f(n) = n+1 in unary representation
    - (c) Recognizing balanced parentheses

57.  Explain the hierarchy of language classes:
    Regular → CFL → Recursive → RE → Non-RE.
    Give examples of languages in each class and the corresponding machine model.

58.  State and prove (or sketch proof of) the undecidability of the Halting Problem.

59.  Explain the Chomsky Hierarchy. For each type, give:
    - The grammar type
    - The machine model
    - An example language

60.  Design a TM that decides whether a given binary number (input) is even or odd.

---

## Cross-Chapter Questions

61.  Draw the Chomsky Hierarchy diagram. Explain where each language class fits.
62. Given a language L, describe how you would determine which class it belongs to (approach for each class).
63. Compare DFA, NFA, PDA, and TM in terms of memory, transitions, and accepted language class.

| Machine | Memory | Transitions | Language Class |
|---------|--------|-------------|---------------|
| DFA | States only | Deterministic | Regular |
| NFA | States only | Non-deterministic | Regular |
| PDA | Stack | Non-deterministic | CFL |
| TM | Infinite tape | Partial function | RE |

---

## Exam-Style Questions (Previous Year Pattern)

### 5-Mark Questions
1.  Construct DFA for strings over {a,b} ending with "aba". Give transition table.
2.  Convert NFA to DFA using subset construction (with given NFA).
3.  Prove L = {aⁿbⁿ | n ≥ 0} is not regular using Pumping Lemma.
4.  Construct PDA for {aⁿbⁿ | n ≥ 1} using empty stack method.
5.  Design TM for aⁿbⁿ. Show trace for "aaabbb".

### 10-Mark Questions
1.  Explain NFA to DFA conversion with full worked example including transition tables.
2.  Simplify CFG to CNF (complete worked example).
3.  Compare Moore and Mealy machines. Design one for each, and convert between them.
4.  Explain DFA minimization (Table-Filling method) with complete example.
5.  Explain the Chomsky Hierarchy with language classes, machine models, closure properties, and examples.

---

*[[Overview|CS-304 Overview]] | [[Revision|CS-304 Revision]] | [[Interview-Prep|CS-304 Interview-Prep]]*
