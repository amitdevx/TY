---
title: "CS-304 Unit-4 - Push Down Automata"
aliases: ["CS304 Unit 4", "PDA Notes", "TCS Ch4", "Push Down Automata"]
tags:
  - subject/theory-of-computation
  - semester/V
  - unit/4
  - pda
  - push-down-automata
  - context-free-languages
subject_code: CS-304-MJ-T
unit: 4
chapter: "Chapter 4 - Push Down Automata"
hours: 5
type: unit-notes
last_reviewed: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# Unit 4 - Push Down Automata (PDA)

> [!note] Navigation
> [[Overview|CS-304 Overview]] | ← [[Unit-3]] | **Unit 4** → [[Unit-5]]

---

## Learning Objectives

- Define PDA formally as a 7-tuple
- Understand the role of the stack in PDA computation
- Build PDAs using acceptance by empty stack
- Build PDAs using acceptance by final state
- Understand the equivalence of these two methods
- Construct PDAs for given context-free languages

---

## 4.1 What is a PDA?

> [!important] Push Down Automaton (PDA)
> A ==Push Down Automaton (PDA)== is a finite automaton enhanced with a **stack** (unbounded memory). This allows it to recognize **context-free languages** - languages that finite automata (DFA/NFA) cannot recognize (like `{aⁿbⁿ}`).

### Why Stack?

- DFA/NFA: only **finite** memory (states)
- The stack provides **infinite** but restricted memory (LIFO - Last In, First Out)
- A PDA can count (by pushing a's onto stack and popping for b's)
- This is exactly the power needed to match `aⁿbⁿ`!

### Stack Operations

| Operation | Meaning |
|-----------|---------|
| Push(a) | Put symbol 'a' on top of stack |
| Pop | Remove top symbol from stack |
| Top/Peek | Read top symbol without removing |
| Empty | Stack is empty |

---

## 4.2 Formal Definition of PDA

> [!important] PDA - 7-tuple
> A ==PDA== is a 7-tuple:
> **M = (Q, Σ, Γ, δ, q₀, Z₀, F)** where:
> - **Q** = Finite set of states
> - **Σ** = Input alphabet
> - **Γ** = Stack alphabet (can be different from Σ)
> - **δ** = Transition function: **Q × (Σ ∪ {ε}) × Γ → 2^(Q × Γ*)** (non-deterministic)
> - **q₀** = Start state (q₀ ∈ Q)
> - **Z₀** = Initial stack symbol (Z₀ ∈ Γ); bottom-of-stack marker
> - **F** = Set of accepting final states (F ⊆ Q)

### Transition Function δ Explained

**δ(q, a, A) = {(p, γ), ...}** means:
- In state `q`
- Reading input symbol `a` (or ε for empty move)
- With `A` on top of stack
- → Move to state `p`
- → Replace `A` on stack with string `γ` (γ can be ε = pop; γ = BA = push B above A)

### Stack Replacement Rules

| Action | Stack Before | γ | Stack After |
|--------|-------------|---|-------------|
| Push B | A... | BA | B on top, A below |
| Replace A with BC | A... | BC | B on top, C below A's place |
| Pop (remove A) | A... | ε | A removed |
| No change | A... | A | Same |

^pda-definition

---

## 4.3 Instantaneous Description (ID)

> [!note] Configuration (ID)
> An **Instantaneous Description** (ID) captures the complete state of a PDA at any moment:
> **(q, w, γ)** where:
> - q = current state
> - w = remaining input string
> - γ = current stack contents (top symbol first)

### Moves

- **⊢** : One move
- **⊢\*** : Zero or more moves

**Example:** δ(q₀, a, Z₀) = {(q₁, AZ₀)}
- ID before: (q₀, aw, Z₀...)
- ID after: (q₁, w, AZ₀...)

---

## 4.4 Acceptance by Empty Stack (N(M))

> [!important] Acceptance by Empty Stack
> A PDA accepts a string w by ==empty stack== if, starting from the initial configuration, after processing all of w, the stack becomes **empty**.
>
> **L(M) = N(M) = {w ∈ Σ* | (q₀, w, Z₀) ⊢\* (q, ε, ε) for some q ∈ Q}**

> [!note] Note: When using empty stack acceptance, F is irrelevant (any state is acceptable if stack is empty).

### Example 1: PDA for L = {aⁿbⁿ | n ≥ 1} by Empty Stack

**Strategy:**
- Push 'A' for each 'a' read
- Pop 'A' for each 'b' read
- Accept when stack is empty after reading all input

**PDA:** M = ({q₀, q₁, q₂}, {a,b}, {A, Z₀}, δ, q₀, Z₀, ∅)

**Transitions:**
```
δ(q₀, a, Z₀) = {(q₀, AZ₀)}   Push A, stay (first a)
δ(q₀, a, A)  = {(q₀, AA)}    Push A (subsequent a's)
δ(q₀, b, A)  = {(q₁, ε)}     Pop A (first b, switch to q₁)
δ(q₁, b, A)  = {(q₁, ε)}     Pop A (subsequent b's)
δ(q₁, ε, Z₀) = {(q₁, ε)}     Pop Z₀ (empty the stack - accept!)
```

**Trace for "aabb":**
```
(q₀, aabb, Z₀)
⊢ (q₀, abb, AZ₀)    [read a, push A]
⊢ (q₀, bb, AAZ₀)    [read a, push A]
⊢ (q₁, b, AZ₀)      [read b, pop A]
⊢ (q₁, ε, Z₀)       [read b, pop A]
⊢ (q₁, ε, ε)        [ε-move, pop Z₀]
→ ACCEPT (stack empty, input empty) 
```

**Trace for "ab":**
```
(q₀, ab, Z₀)
⊢ (q₀, b, AZ₀)
⊢ (q₁, ε, Z₀)
⊢ (q₁, ε, ε)
→ ACCEPT 
```

**Trace for "aab" (reject):**
```
(q₀, aab, Z₀)
⊢ (q₀, ab, AZ₀)
⊢ (q₀, b, AAZ₀)
⊢ (q₁, ε, AZ₀)    [only one b]
→ No more transitions! Stack not empty → REJECT 
```

^pda-empty-stack

---

## 4.5 Acceptance by Final State (L(M))

> [!important] Acceptance by Final State
> A PDA accepts a string w by ==final state== if, starting from initial configuration, after processing all of w, the PDA is in an **accepting state** (regardless of stack content).
>
> **L(M) = {w ∈ Σ* | (q₀, w, Z₀) ⊢\* (q, ε, γ) for some q ∈ F, γ ∈ Γ*}**

### Example 2: PDA for L = {aⁿbⁿ | n ≥ 1} by Final State

**PDA:** M = ({q₀, q₁, q₂}, {a,b}, {A, Z₀}, δ, q₀, Z₀, {q₂})

**Transitions:**
```
δ(q₀, a, Z₀) = {(q₀, AZ₀)}   Push A on Z₀ (first a)
δ(q₀, a, A)  = {(q₀, AA)}    Push A (more a's)
δ(q₀, b, A)  = {(q₁, ε)}     First b: switch to q₁, pop A
δ(q₁, b, A)  = {(q₁, ε)}     Subsequent b's: pop A
δ(q₁, ε, Z₀) = {(q₂, Z₀)}   Stack has only Z₀: go to final state q₂
```

**Trace for "aabb":**
```
(q₀, aabb, Z₀)
⊢ (q₀, abb, AZ₀)
⊢ (q₀, bb, AAZ₀)
⊢ (q₁, b, AZ₀)
⊢ (q₁, ε, Z₀)
⊢ (q₂, ε, Z₀)
→ ACCEPT (q₂ is final state) 
```

^pda-final-state

---

## 4.6 Empty Stack vs Final State - Equivalence

> [!important] Theorem
> For any PDA M₁ that accepts by **empty stack**, there is a PDA M₂ that accepts by **final state**, and vice versa. The two methods are **equivalent** in power.

### Conversion: Empty Stack → Final State

```
Given PDA M₁ accepting by empty stack:
Construct M₂:
1. Add new start state q_new, new final state q_f
2. Add transition: δ(q_new, ε, Z_new) = {(q₀, Z₀Z_new)}
   (Push old Z₀ and new bottom marker)
3. For every state q and γ with δ(q, ε, Z_new): add (q_f, Z_new)
   (When we see Z_new - old stack was empty → go to final state)
```

### Conversion: Final State → Empty Stack

```
Given PDA M₁ accepting by final state:
Construct M₂:
1. Add new start state q_new, new bottom symbol Z_new
2. From q_new, push old Z₀ over Z_new
3. From every final state of M₁, on any stack symbol, pop that symbol
   (Empty the stack)
```

---

## 4.7 More PDA Examples

### Example 3: PDA for Palindromes over {a, b} - L = {w ∈ {a,b}* | w = wᴿ}

**Strategy (non-deterministic):**
- Phase 1: Push all input onto stack (guess we're in first half)
- Non-deterministically switch to Phase 2 in the middle
- Phase 2: Pop from stack and match remaining input

**PDA:**

```
States: {q₀, q₁, q₂}
Σ = {a, b}, Γ = {a, b, Z₀}
Start: q₀, Bottom: Z₀, Final: {q₂}

Transitions:
Phase 1 (push):
  δ(q₀, a, Z₀) = {(q₀, aZ₀)}     push a
  δ(q₀, b, Z₀) = {(q₀, bZ₀)}     push b
  δ(q₀, a, a)  = {(q₀, aa)}       push a
  δ(q₀, a, b)  = {(q₀, ab)}       push a
  δ(q₀, b, a)  = {(q₀, ba)}       push b
  δ(q₀, b, b)  = {(q₀, bb)}       push b
  
  δ(q₀, ε, Z₀) = {(q₁, Z₀)}      ε-move: guess middle (even palindrome)
  δ(q₀, a, a)  ∪= {(q₁, a)}      guess after reading 'a' (odd palindrome)
  δ(q₀, b, b)  ∪= {(q₁, b)}      guess after reading 'b'
  
Phase 2 (match and pop):
  δ(q₁, a, a)  = {(q₁, ε)}       match and pop
  δ(q₁, b, b)  = {(q₁, ε)}       match and pop
  δ(q₁, ε, Z₀) = {(q₂, Z₀)}      accept: stack has only Z₀
```

### Example 4: PDA for L = {w ∈ {a,b}* | #a(w) = #b(w)} (equal a's and b's)

**Strategy:**
- Push 'A' for each 'a', 'B' for each 'b'
- If top is same kind, push; if opposite kind, pop

```
δ(q₀, a, Z₀) = {(q₀, AZ₀)}    first a
δ(q₀, b, Z₀) = {(q₀, BZ₀)}    first b
δ(q₀, a, A)  = {(q₀, AA)}     another a
δ(q₀, b, B)  = {(q₀, BB)}     another b
δ(q₀, a, B)  = {(q₀, ε)}      a cancels b
δ(q₀, b, A)  = {(q₀, ε)}      b cancels a
δ(q₀, ε, Z₀) = {(q₁, Z₀)}     accept: only Z₀ left
```

**Final State:** {q₁}

### Example 5: PDA for Balanced Parentheses L = {ww' | w ∈ {(}*, w' ∈ {)}*, |w|=|w'|}

```
δ(q₀, (, Z₀) = {(q₀, (Z₀)}    push (
δ(q₀, (, ()  = {(q₀, (()}      push (
δ(q₀, ), ()  = {(q₀, ε)}       pop ( for )
δ(q₀, ε, Z₀) = {(q₁, Z₀)}     accept
```

**Final State:** {q₁}

---

## 4.8 CFG to PDA Construction

> [!important] Theorem
> For every CFG G, there is a PDA M such that L(G) = N(M) (acceptance by empty stack).

### Construction Algorithm

Given G = (V, T, P, S):
```
PDA M = ({q}, T, V ∪ T, δ, q, S, ∅) where:
1. For each production A → α ∈ P:
   δ(q, ε, A) = {(q, α)}    [expand non-terminal]
2. For each terminal a ∈ T:
   δ(q, a, a) = {(q, ε)}    [match and consume terminal]
```

**This PDA simulates leftmost derivations!**

### Example: CFG for {aⁿbⁿ} → PDA

```
CFG: S → aSb | ε (for n ≥ 0)

PDA:
δ(q, ε, S) = {(q, aSb), (q, ε)}   [S → aSb | ε]
δ(q, a, a) = {(q, ε)}             [match a]
δ(q, b, b) = {(q, ε)}             [match b]
```

**Trace for "aabb":**
```
Stack: S; Input: aabb
→ (q, aabb, S) 
⊢ (q, aabb, aSb)    [S → aSb]
⊢ (q, abb, Sb)      [match a]
⊢ (q, abb, aSbb)    [S → aSb]
⊢ (q, bb, Sbb)      [match a]
⊢ (q, bb, bb)       [S → ε]
⊢ (q, b, b)         [match b]
⊢ (q, ε, ε)         [match b - stack empty → ACCEPT!]
```

---

## Interview Questions - Unit 4

> [!question] Key Interview/Exam Questions

1. **What is a PDA? How is it different from a DFA/NFA?**
   - PDA = NFA + stack; the stack allows it to count/match nested structures; DFA/NFA can't recognize {aⁿbⁿ} but PDA can

2. **Define PDA as a 7-tuple. What is each component?**
   - (Q, Σ, Γ, δ, q₀, Z₀, F): states, input alphabet, stack alphabet, transition fn (Q×Σ_ε×Γ→2^{Q×Γ*}), start state, initial stack symbol, final states

3. **Explain the transition function of a PDA.**
   - δ(q, a, A) = {(p, γ)}: in state q, reading 'a', with A on top, go to p and replace A with γ

4. **What are the two methods of acceptance in PDA?**
   - Empty stack: accept when stack is empty after processing input
   - Final state: accept when in a final state after processing input
   - Both are equivalent in power

5. **Construct a PDA for L = {aⁿbⁿ | n ≥ 1}.**
   - See §4.4 (empty stack) and §4.5 (final state) with complete transitions

6. **What is the relationship between PDAs and CFGs?**
   - Every CFL is accepted by some PDA; every PDA accepts a CFL; PDA ≡ CFG in expressive power

7. **Is PDA deterministic or non-deterministic?**
   - Generally non-deterministic (NPDA); DPDA is strictly less powerful (some CFLs need NPDA)

8. **What is an Instantaneous Description (ID)?**
   - Snapshot of PDA: (current state, remaining input, stack contents) - represents configuration

---

## Revision Summary

> [!summary] Unit 4 Key Takeaways
>
> **PDA = (Q, Σ, Γ, δ, q₀, Z₀, F):**
> - Stack is the key addition over NFA
> - δ: Q × (Σ ∪ {ε}) × Γ → 2^(Q × Γ*)
>
> **Acceptance Methods:**
> - Empty Stack: (q₀, w, Z₀) ⊢* (q, ε, ε) - any state, empty stack
> - Final State: (q₀, w, Z₀) ⊢* (q, ε, γ) - q ∈ F, any stack
> - Both are **equivalent** in power
>
> **Key PDA Constructions:**
> - {aⁿbⁿ}: push for a's, pop for b's
> - Palindromes: push first half, non-deterministically switch, match second half
> - CFG to PDA: one state q; expand non-terminals (ε-move), match terminals
>
> **Equivalence:**
> - PDA ≡ CFG ≡ CFL (all three characterize the same class)

^unit4-tcs-revision

---

*← [[Unit-3]] | [[Overview|CS-304 Overview]] | Next: [[Unit-5]] →*
