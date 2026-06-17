---
title: "CS-304 Theory of Computer Science - Expected PYQ"
subject: CS-304
paper: Theory of Computer Science
semester: V
tags:
  - pyq
  - tcs
  - automata
  - dfa
  - nfa
  - cfg
  - pumping-lemma
  - turing-machine
  - semester-v
  - exam
aliases:
  - TCS PYQ
  - Automata PYQ
  - CS304 Questions
created: 2026-06-16
type: pyq
---

[[00-Dashboard/Home|Home]] | [[07-Exams/Exams-Dashboard|Exams Dashboard]]


# CS-304 Theory of Computer Science - Expected PYQ

> [!important] Exam Strategy
> TCS is highly numerical. Expect DFA/NFA construction, CFG problems, FIRST & FOLLOW, PDA, and Turing Machine design. Pumping Lemma is a MUST. Memorize conversion algorithms step by step.

---

## Unit-wise Distribution

| Unit | Topic | Marks Weightage |
|------|-------|----------------|
| I | DFA / NFA | 25% |
| II | Regular Expressions & FA | 20% |
| III | CFG - CNF, GNF | 20% |
| IV | PDA & CFL | 15% |
| V | Turing Machine | 20% |

---

## Section A - Short Answer (2 Marks)

1. **Define DFA. What are its 5 components?**
   > M = (Q, Σ, δ, q₀, F) - States, Alphabet, Transition function, Start state, Accept states

2. **What is the difference between DFA and NFA?**
   > DFA: exactly one transition per input. NFA: zero or more transitions, ε-moves allowed.

3. **Define ε-closure of a state in NFA.**

4. **What is a Regular Language? Give an example.**

5. **Define the Pumping Lemma for regular languages.**
   > For any regular language L, ∃ p (pumping length) such that any string w ∈ L with |w| ≥ p can be split as w = xyz where |y| ≥ 1, |xy| ≤ p, and xyⁿz ∈ L for all n ≥ 0.

6. **What is a Context-Free Grammar (CFG)? Define its four components.**
   > G = (V, T, P, S) - Variables, Terminals, Productions, Start symbol

7. **What is Chomsky Normal Form (CNF)?**
   > Every production is of the form A → BC or A → a

8. **What is Greibach Normal Form (GNF)?**
   > Every production is of the form A → aα where a ∈ T, α ∈ V*

9. **Define a Pushdown Automaton (PDA).**

10. **What is the difference between deterministic and non-deterministic PDA?**

11. **Define a Turing Machine. What are its components?**
    > M = (Q, Σ, Γ, δ, q₀, B, F) - B is blank symbol, Γ is tape alphabet

12. **What is the Church-Turing Thesis?**

13. **Define decidable and undecidable problems.**

14. **What is the Halting Problem? Why is it undecidable?**

15. **Differentiate between Regular, CFL, and Recursively Enumerable languages.**

---

## Section B - Long Answer / Numerical Problems (5–7 Marks)

---

### Q1. DFA Construction ( HIGH PROBABILITY)

**Construct a DFA that accepts strings over {0,1} ending with '01'.**

```
States: q0 (start), q1, q2 (final)

Transition Table:
State | 0  | 1
------|----|-
 q0   | q1 | q0
 q1   | q1 | q2
 q2   | q1 | q0

Start: q0
Final: {q2}
```

*Explanation: q0=initial, q1=seen '0', q2=seen '01' (accept)*

---

**Construct a DFA accepting strings with even number of 0s and even number of 1s.**

```
States: q00 (even0,even1), q01 (even0,odd1), q10 (odd0,even1), q11 (odd0,odd1)

Transition Table:
State | 0   | 1
------|-----|----
q00   | q10 | q01   ← START & FINAL
q01   | q11 | q00
q10   | q00 | q11
q11   | q01 | q10
```

---

### Q2. NFA to DFA Conversion ( HIGH PROBABILITY)

**Convert NFA to DFA using subset construction.**

*Steps:*
1. Start with ε-closure(q₀)
2. For each state in DFA, compute δ*(state, a) for each symbol a
3. Repeat until no new states
4. DFA final states: any state containing an NFA final state

**Example NFA:** States {q0, q1, q2}, Σ={a,b}, δ:
- q0 -a→ {q0, q1}
- q0 -b→ {q0}
- q1 -b→ {q2}
- Final: {q2}

| DFA State | a | b |
|-----------|---|---|
| {q0}* | {q0,q1} | {q0} |
| {q0,q1} | {q0,q1} | {q0,q2}** |
| {q0,q2} | {q0,q1} | {q0} |

*start state; **final state (contains q2)*

---

### Q3. Regular Expression to NFA/DFA (Thompson's Construction)

**Convert RE: (a+b)*abb to NFA.**

Steps of Thompson's Construction:
1. Each symbol → basic NFA
2. Concatenation: connect final of first to start of second
3. Union (a+b): create new start/end with ε-transitions
4. Kleene Star (*): add ε-loops

*Apply for (a+b)*:*
- Create NFA for 'a', NFA for 'b'
- Union them
- Apply Kleene star
- Concatenate with 'a', then 'b', then 'b'

---

### Q4. Pumping Lemma - Prove a language is NOT regular ()

**Prove that L = {aⁿbⁿ | n ≥ 0} is NOT regular.**

*Proof by contradiction:*
1. Assume L is regular. Then pumping length p exists.
2. Choose w = aᵖbᵖ ∈ L, |w| = 2p ≥ p 
3. By Pumping Lemma: w = xyz where |y| ≥ 1, |xy| ≤ p
4. Since |xy| ≤ p, y consists entirely of a's. Let y = aᵏ (k ≥ 1)
5. Pump: xy²z = aᵖ⁺ᵏbᵖ
6. Since k ≥ 1, number of a's > number of b's → **xy²z ∉ L**  Contradiction!
7. ∴ L is NOT regular. ■

---

**Prove L = {aⁿ | n is a perfect square} is NOT regular.**

1. Assume regular, pumping length p.
2. Choose w = a^(p²), |w| = p² ≥ p 
3. w = xyz, |y| = k (1 ≤ k ≤ p)
4. xy²z = a^(p²+k)
5. Need p²+k to be a perfect square. But p² < p²+k ≤ p²+p < (p+1)²
6. No perfect square between p² and (p+1)² → Contradiction! ■

---

### Q5. CFG Simplification - Remove Useless Symbols, ε-productions, Unit productions

**Given CFG:**
```
S → AB | ε
A → aA | ε
B → bB | b
```

**Step 1: Remove ε-productions**
```
Nullable: {A, S}
New productions (without A, with all combinations):
S → AB | B | A | ε (keep ε only if S is start)
A → aA | a
B → bB | b
```

**Step 2: Remove unit productions (A → B)**
- Identify unit pairs
- Replace with non-unit productions

**Step 3: Remove useless symbols**
- Generating: can derive terminal string
- Reachable: can be reached from S

---

### Q6. Convert CFG to CNF ( HIGH PROBABILITY)

**Convert to Chomsky Normal Form:**
```
S → ASB | ε
A → aAS | a
B → SbS | A | bb
```

**Steps:**
1. Add new start S₀ → S (if S appears in RHS)
2. Remove ε-productions
3. Remove unit productions
4. Replace long productions with binary:
   - X → ABC becomes X → AX₁, X₁ → BC
5. Replace terminals in mixed rules:
   - a → Tₐ, Tₐ → a

**Final CNF has only:**
- A → BC (two variables)
- A → a (single terminal)

---

### Q7. Convert CFG to GNF

**Every production: A → aα where a ∈ terminal, α ∈ V***

**Steps:**
1. Order variables: A₁, A₂, ..., Aₙ
2. Eliminate left recursion
3. Substitute to ensure every RHS starts with terminal

---

### Q8. PDA Construction ()

**Design a PDA for L = {aⁿbⁿ | n ≥ 1}**

```
M = ({q0, q1, q2}, {a,b}, {Z,A}, δ, q0, Z, {q2})

δ(q0, a, Z) = {(q0, AZ)}   ← push A for each 'a'
δ(q0, a, A) = {(q0, AA)}
δ(q0, b, A) = {(q1, ε)}    ← pop A for each 'b'
δ(q1, b, A) = {(q1, ε)}
δ(q1, ε, Z) = {(q2, Z)}    ← stack empty → accept
```

*Trace for "aabb":*
```
(q0, aabb, Z) ⊢ (q0, abb, AZ) ⊢ (q0, bb, AAZ)
⊢ (q1, b, AZ) ⊢ (q1, ε, Z) ⊢ (q2, ε, Z) ACCEPT 
```

---

**Design PDA for L = {ww^R | w ∈ {a,b}*}**

```
Phase 1 (q0): Push all symbols onto stack
Phase 2 (q1): Pop and match with remaining input
δ(q0, a, Z) = {(q0, aZ)}
δ(q0, b, Z) = {(q0, bZ)}
δ(q0, a, a) = {(q0, aa)}
δ(q0, ε, a) = {(q1, a)}   ← nondeterministic guess for middle
δ(q1, a, a) = {(q1, ε)}
δ(q1, b, b) = {(q1, ε)}
δ(q1, ε, Z) = {(q2, Z)}
```

---

### Q9. Turing Machine Design ()

**Design a Turing Machine for L = {aⁿbⁿ | n ≥ 1}**

```
States: q0, q1, q2, q3, q4 (accept), qr (reject)
Tape alphabet: {a, b, X, Y, B}

Algorithm:
q0: Scan right; if 'a', replace with X, go to q1
q1: Scan right past a's and Y's; if 'b', replace with Y, go to q2
q2: Scan left past Y's and a's; if X, go to q0
q0: If all a's replaced (see only Y's), go to q4 (accept)

Transitions:
δ(q0, a) = (q1, X, R)
δ(q0, Y) = (q0, Y, R)
δ(q0, B) = (q4, B, R)   ← accept
δ(q1, a) = (q1, a, R)
δ(q1, Y) = (q1, Y, R)
δ(q1, b) = (q2, Y, L)
δ(q2, Y) = (q2, Y, L)
δ(q2, a) = (q2, a, L)
δ(q2, X) = (q0, X, R)
```

---

**Design TM to compute f(n) = n+1 (increment unary number)**

```
Unary: n = "111...1" (n ones)
Simply scan to end and add one more 1:
δ(q0, 1) = (q0, 1, R)
δ(q0, B) = (q1, 1, R)
δ(q1, B) = (qf, B, R)
```

---

### Q10. Chomsky Hierarchy - Language Classification

| Class | Grammar | Automaton | Example |
|-------|---------|-----------|---------|
| Type 0 | Unrestricted | Turing Machine | L = {ww | w ∈ Σ*} |
| Type 1 | Context-Sensitive | LBA | aⁿbⁿcⁿ |
| Type 2 | Context-Free | PDA | aⁿbⁿ |
| Type 3 | Regular | DFA/NFA | (ab)* |

---

## Most Expected Questions

> [!tip] High Probability
> 1.  DFA construction (ending pattern, count of symbols)
> 2.  NFA → DFA conversion (subset construction)
> 3.  Pumping Lemma proof (aⁿbⁿ or similar)
> 4.  CFG → CNF conversion
> 5.  PDA design for balanced parentheses or aⁿbⁿ
> 6.  TM design for aⁿbⁿ or binary addition
> 7.  Chomsky Hierarchy table
> 8.  ε-NFA to DFA conversion

---

## Key Theorems to Remember

1. **Kleene's Theorem:** Regular languages = languages recognized by FA = languages defined by RE
2. **Pumping Lemma:** Used to prove a language is NOT regular / NOT CFL
3. **CFL Pumping Lemma:** w = uvxyz, |vx| ≥ 1, |vxy| ≤ p, uvⁿxyⁿz ∈ L
4. **Church-Turing Thesis:** Any effective computation can be done by a TM
5. **Halting Problem:** Undecidable - no TM can decide if another TM halts

---

*Tags: CS-304 Theory of Computer Science | Semester V | [[07-Exams/Exams-Dashboard|Exams]]*
