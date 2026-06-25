---
title: "CS-304 Theory of Computer Science - Important Topics"
subject: CS-304
semester: V
tags:
  - important-topics
  - tcs
  - automata
  - cfg
  - turing-machine
  - semester-v
  - exam
aliases:
  - TCS Important
  - Automata Must-Know
created: 2026-06-16
type: important-topics
---

[[00-Dashboard/Home|Home]] | [[07-Exams/Exams-Dashboard|Exams Dashboard]]


# CS-304 Theory of Computer Science - Important Topics

> [!important] Exam Focus
> TCS is 80% numerical. Master DFA construction, NFA→DFA conversion, CFG→CNF, Pumping Lemma, and Turing Machine design. Definitions fetch marks in short answers.

---

## Top 10 Most Important Topics

| # | Topic | Description | Probability |
|---|-------|-------------|-------------|
| 1 | **DFA Construction** | Build DFA from language description - ending pattern, count parity |  |
| 2 | **NFA → DFA Conversion** | Subset construction algorithm, ε-closure |  |
| 3 | **Pumping Lemma** | Prove languages not regular (aⁿbⁿ, palindromes) |  |
| 4 | **CFG → CNF Conversion** | Step-by-step CNF transformation |  |
| 5 | **PDA Design** | PDA for aⁿbⁿ, balanced brackets, ww^R |  |
| 6 | **Turing Machine Design** | TM for aⁿbⁿ, binary addition |  |
| 7 | **RE to NFA (Thompson's)** | Convert regular expression to NFA |  |
| 8 | **CFG Simplification** | Remove ε-productions, unit productions, useless symbols |  |
| 9 | **GNF Conversion** | Greibach Normal Form transformation |  |
| 10 | **Chomsky Hierarchy** | Type 0-3 classification with examples |  |

---

## "Definitely Going to Come" Section

> [!warning] Almost Certain Exam Questions
> 1. **Construct DFA** for: strings ending in '01', strings with even 0s & even 1s
> 2. **NFA → DFA conversion** using subset construction (draw transition table)
> 3. **Pumping Lemma proof** - Show {aⁿbⁿ} or {aⁿbⁿcⁿ} is not regular
> 4. **Convert CFG to CNF** - given grammar with 3-4 productions
> 5. **Design PDA** for aⁿbⁿ (acceptance by empty stack or final state)
> 6. **Design Turing Machine** for aⁿbⁿ or simple computation
> 7. **Chomsky Hierarchy table** - all 4 types with automaton and grammar type

---

## Must-Know Definitions

| Term | Definition |
|------|-----------|
| **DFA** | Deterministic Finite Automaton - exactly one transition per (state, symbol) |
| **NFA** | Nondeterministic FA - zero or more transitions, ε-moves allowed |
| **ε-closure** | Set of all states reachable from state q via ε-transitions only |
| **Regular Language** | Language accepted by DFA/NFA = defined by regular expression |
| **Pumping Lemma** | For regular L: any long enough string can be split as xyz, yⁿ pumped ∈ L |
| **CFG** | Context-Free Grammar G = (V, T, P, S); productions: A → α |
| **CNF** | Chomsky Normal Form: A → BC or A → a |
| **GNF** | Greibach Normal Form: A → aα (terminal first) |
| **PDA** | Pushdown Automaton - FA + stack memory |
| **Turing Machine** | Mathematical model of computation with infinite tape |
| **Decidable** | There exists a TM that always halts with yes/no answer |
| **Halting Problem** | Undecidable: cannot determine if TM halts on input |
| **CFL Pumping Lemma** | w = uvxyz; vⁿxⁿ pumping preserves membership |

---

## Key Algorithms to Remember

### Algorithm 1: NFA → DFA (Subset Construction)
```
1. Start state of DFA = ε-closure({q₀_NFA})
2. For each DFA state S and input symbol a:
   - Compute: move(S, a) = U δ(q, a) for all q ∈ S
   - New DFA state = ε-closure(move(S, a))
3. DFA final states = any state containing an NFA final state
4. Repeat until no new states
```

### Algorithm 2: CFG → CNF Conversion
```
Step 1: Add S₀ → S if S appears on any RHS
Step 2: Eliminate ε-productions
  - Find all nullable variables
  - Add productions with nullable vars removed (all combinations)
Step 3: Eliminate unit productions (A → B)
  - Replace with what B produces
Step 4: Eliminate long productions
  - A → BCD becomes A → BA₁, A₁ → CD
Step 5: Replace terminals in mixed productions
  - A → aBC: create Tₐ → a, replace: A → TₐBC
```

### Algorithm 3: Pumping Lemma Proof Template
```
Proof that L is NOT regular:
1. Assume L is regular → pumping length p exists
2. Choose string w = [carefully chosen] ∈ L with |w| ≥ p
3. By PL: w = xyz, |y| ≥ 1, |xy| ≤ p
4. Analyze: y must consist of [only a's / only b's / etc.]
5. Show xy²z or xy⁰z = xz ∉ L
6. Contradiction! ∴ L is NOT regular ■
```

### Algorithm 4: PDA for aⁿbⁿ
```
Push 'A' for each 'a' read
Pop 'A' for each 'b' read  
Accept when stack empty and input empty
```

### Algorithm 5: TM for aⁿbⁿ
```
1. Scan left to right; mark 'a' with X, move right
2. Find first 'b', mark with Y, move left
3. Return to first 'a', repeat
4. If all 'a's marked and all 'b's marked → ACCEPT
5. If mismatch → REJECT
```

---

## Quick Formulas & Key Facts

| Fact | Detail |
|------|--------|
| DFA components | M = (Q, Σ, δ, q₀, F) - 5 components |
| CFG components | G = (V, T, P, S) - 4 components |
| TM components | M = (Q, Σ, Γ, δ, q₀, B, F) - 7 components |
| CFL Pumping Lemma | w = uvxyz; |vxy| ≤ p; |vy| ≥ 1 |
| Regular PL | w = xyz; |y| ≥ 1; |xy| ≤ p |
| Kleene's Theorem | FA ↔ RE ↔ Regular Language |
| Church-Turing | Any effective computation ≡ Turing Machine |

---

## Common Mistakes to Avoid

> [!warning] Don't Make These Errors
> - **DFA must be complete:** Every state must have a transition for every input symbol. Add a dead/trap state if needed.
> - **Subset construction:** Don't forget ε-closure! Many students skip this step.
> - **Pumping Lemma:** You must show the pumped string is NOT in L (contradiction), NOT that it IS in L.
> - **CNF Step 3:** Remove unit productions AFTER removing ε-productions, not before.
> - **PDA:** Clearly specify whether acceptance is by final state or empty stack.
> - **TM transitions:** Format is δ(state, read) = (new_state, write, direction). L/R is Left/Right.
> - **Chomsky Hierarchy:** Type 0 is most general, Type 3 is most restricted (not the other way around).

---

## Chomsky Hierarchy Quick Reference

| Type | Name | Grammar | Automaton | Language Example |
|------|------|---------|-----------|-----------------|
| Type 0 | Unrestricted | αAβ → γ | Turing Machine | {ww | w ∈ Σ\*} |
| Type 1 | Context-Sensitive | αAβ → αγβ | LBA | {aⁿbⁿcⁿ | n≥1} |
| Type 2 | Context-Free | A → γ | PDA | {aⁿbⁿ | n≥1} |
| Type 3 | Regular | A → aB or A → a | DFA/NFA | (ab)* |

---

## DFA Construction Tips

### Recognizing String Patterns:
- **Ending in "ab":** Need states tracking recent chars seen
- **Count parity (even/odd):** Use XOR states (2 states per symbol being counted)
- **Divisibility:** Number of states = modulus (e.g., divisible by 3 → 3 states)
- **Contains substring:** States represent longest matching prefix of substring

---

*Tags: CS-304 Theory of Computer Science | Semester V | [[07-Exams/Exams-Dashboard|Exams]]*
