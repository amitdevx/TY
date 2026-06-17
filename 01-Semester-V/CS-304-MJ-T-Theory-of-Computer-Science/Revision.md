---
title: "CS-304 Theory of Computer Science - Revision Notes"
aliases: ["CS304 Revision", "TCS Quick Revision", "TOC Cheat Sheet"]
tags:
  - subject/theory-of-computation
  - semester/V
  - revision
  - cheat-sheet
subject_code: CS-304-MJ-T
type: revision
last_reviewed: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-304 Theory of Computer Science - Revision Notes

> [!note] Navigation
> [[Overview|CS-304 Overview]] | [[Important-Questions|CS-304 Important-Questions]] | [[Interview-Prep|CS-304 Interview-Prep]]

---

> [!tip] How to Use
> This is your **last-minute revision guide**. Read this the night before your exam!

---

## Chapter 1 - Finite Automata

### Core Definitions (Must Know)
```
Symbol    - atomic element (a, b, 0, 1)
Alphabet Σ - finite, non-empty set of symbols
String    - finite sequence of symbols from Σ
ε         - empty string (length 0)
Σ*        - all strings over Σ including ε
Σ⁺        - Σ* \ {ε} (no empty string)
Language  - any subset of Σ*
```

### DFA = (Q, Σ, δ, q₀, F)
```
Q  = finite set of states
Σ  = input alphabet
δ  = Q × Σ → Q  (EXACTLY ONE next state - deterministic)
q₀ = start state
F  = set of accepting states (F ⊆ Q)

Accepts w if: starting q₀, processing w, ends in state ∈ F
```

### NFA = (Q, Σ, δ, q₀, F) 
```
δ = Q × (Σ ∪ {ε}) → 2^Q  (ZERO or MORE next states)

Accepts w if: ANY path through NFA ends in F
```

### NFA → DFA (Subset Construction)
```
1. DFA start = {q₀_NFA}
2. For each DFA state S (set of NFA states):
   δ_DFA(S, a) = ∪ { δ_NFA(q, a) | q ∈ S }
3. DFA state is accepting if it contains any NFA accepting state
4. Repeat until no new states
Max DFA states = 2ⁿ (n = NFA states)
```

### Moore Machine
```
6-tuple: (Q, Σ, Δ, δ, λ, q₀)
Output λ: Q → Δ  (output per STATE)
Output length = |w| + 1
```

### Mealy Machine
```
6-tuple: (Q, Σ, Δ, δ, λ, q₀)
Output λ: Q × Σ → Δ  (output per TRANSITION)
Output length = |w|
```

### DFA Minimization (Table-Filling)
```
1. Remove unreachable states
2. Mark all pairs (p,q) where exactly one is accepting
3. For each unmarked (p,q), symbol a:
   if (δ(p,a), δ(q,a)) is marked → mark (p,q)
4. Repeat step 3 until no new marks
5. Unmarked pairs = equivalent → merge
```

---

## Chapter 2 - Regular Expressions & Languages

### RE Definition (Recursive)
```
Base:      ∅, ε, a (for each a ∈ Σ)
Inductive: r + s (union), rs (concat), r* (Kleene star)

Precedence: () > * > concat > +
```

### Important RE Identities
```
r + ∅ = r       (identity for union)
r · ε = r       (identity for concatenation)
r · ∅ = ∅       (annihilator)
r* * = r*       (star is idempotent)
(r+s)* = (r*s*)* (mixing)
ε + rr* = r*    (r* = ε or one or more r's)
Arden: X = Q + XP → X = QP*  (if ε ∉ L(P))
```

### Pumping Lemma (Proof Structure)
```
To prove L is NOT regular:

1. Assume L is regular; let p = pumping length
2. Choose w ∈ L with |w| ≥ p  (choose w carefully!)
3. By PL: w = xyz, |xy| ≤ p, |y| ≥ 1
4. Argue what x, y, z must look like (usually y in first block)
5. Choose i (usually 0 or 2) such that xyⁱz ∉ L
6. Contradiction! → L is NOT regular

Classic example:  w = aᵖbᵖ → y must be all a's → pump out of balance
```

### Closure Properties of Regular Languages
```
Closed under: ∪, ∩, ¬, ·, *, reversal, homomorphism
NOT closed under: ??? (all operations close regular!)
```

---

## Chapter 3 - Context-Free Grammars

### CFG = (V, T, P, S)
```
V = variables (non-terminals), uppercase
T = terminals, lowercase / symbols
P = productions: A → α, where A ∈ V, α ∈ (V ∪ T)*
S = start symbol ∈ V
V ∩ T = ∅
```

### Simplification Order (IMPORTANT!)
```
Step 1: Remove ε-productions
  a. Find NULLABLE = {A | A ⇒* ε}
  b. For each production, add versions with nullable vars absent
  c. Remove A → ε (keep S → ε if ε ∈ L)

Step 2: Remove unit productions (A → B)
  a. Compute UNIT(A) = {B | A ⇒* B via unit prods}
  b. For each B ∈ UNIT(A) and each non-unit B → α: add A → α
  c. Remove all unit productions

Step 3: Remove useless symbols
  a. Non-generating: can't reach terminal string → remove
  b. Unreachable from S → remove
```

### CNF Conversion
```
Every production must be: A → BC or A → a

Steps after simplification:
1. For terminal in long production: create Cₐ → a, replace terminal with Cₐ
2. Break long productions: A → X₁X₂X₃ becomes A → X₁D, D → X₂X₃
```

### GNF Conversion
```
Every production must be: A → aα (terminal first, then variables)

Steps:
1. Eliminate left recursion (A → Aα | β becomes A → βA', A' → αA' | ε)
2. Substitute so all RHS start with terminals
```

### Key CFG Examples
```
{aⁿbⁿ | n ≥ 1}:   S → aSb | ab
{aⁿbⁿ | n ≥ 0}:   S → aSb | ε
Palindromes:        S → aSa | bSb | a | b | ε
{ww^R}:            S → aSa | bSb | ε
Balanced parens:    S → SS | (S) | ε
```

---

## Chapter 4 - Push Down Automata

### PDA = (Q, Σ, Γ, δ, q₀, Z₀, F)
```
Q  = states
Σ  = input alphabet
Γ  = stack alphabet (includes Z₀)
δ  = Q × (Σ ∪ {ε}) × Γ → 2^(Q × Γ*)
q₀ = start state
Z₀ = initial stack symbol (bottom marker)
F  = accepting states

δ(q, a, A) = {(p, γ)}: in state q, reading a, top=A
             → go to p, replace A with γ on stack
γ = ε means POP; γ = BA means push B above A
```

### Acceptance Methods
```
Empty Stack:  (q₀, w, Z₀) ⊢* (q, ε, ε)  [any state, empty stack]
Final State:  (q₀, w, Z₀) ⊢* (q, ε, γ)  [q ∈ F, any stack]
BOTH ARE EQUIVALENT!
```

### PDA for {aⁿbⁿ} - Key Transitions
```
Empty Stack method:
δ(q₀, a, Z₀) = {(q₀, AZ₀)}   push A on Z₀
δ(q₀, a, A)  = {(q₀, AA)}    push A
δ(q₀, b, A)  = {(q₁, ε)}     pop A (first b)
δ(q₁, b, A)  = {(q₁, ε)}     pop A
δ(q₁, ε, Z₀) = {(q₁, ε)}     pop Z₀ → ACCEPT
```

### CFG → PDA (One-State Construction)
```
PDA has ONE state q.
For each A → α: δ(q, ε, A) = {(q, α)}  [expand]
For each a ∈ T: δ(q, a, a) = {(q, ε)}  [match]
Start: (q, w, S), accept by empty stack
```

---

## Chapter 5 - Turing Machine

### TM = (Q, Σ, Γ, δ, q₀, B, F)
```
Q  = states
Σ  = input alphabet (Σ ⊆ Γ, B ∉ Σ)
Γ  = tape alphabet (includes B = blank)
δ  = Q × Γ → Q × Γ × {L, R}  [PARTIAL function]
q₀ = start state
B  = blank symbol
F  = accepting states (halt and accept)

δ(q, a) = (p, b, D): read a, write b, move direction D
```

### Configuration (ID): αqβ
```
α = tape content LEFT of head
q = current state  
β = content from head rightward (head reads β[0])

Move R: αqaγ ⊢ αbpγ  (if δ(q,a)=(p,b,R))
Move L: αcqaγ ⊢ αpcbγ (if δ(q,a)=(p,b,L))
```

### Language Classes
```
Regular ⊂ CFL ⊂ Recursive ⊂ RE ⊂ All Languages

Regular     → DFA/NFA    (finite memory)
CFL         → PDA        (stack)
Recursive   → TM always halts (decidable)
RE          → TM may loop (semidecidable)
Non-RE      → No TM
```

### TM for {aⁿbⁿ} - Strategy
```
1. If input starts with B → accept (empty string? check if ε ∈ L)
2. Mark leftmost 'a' → 'X'
3. Scan right to first unmarked 'b', mark 'b' → 'Y'
4. Scan left to leftmost 'X', go one right (find next 'a')
5. Repeat 2-4
6. If only Y's remain (no more a's or b's) → ACCEPT
7. If mismatch → REJECT
```

### Halting Problem
```
HALT = {⟨M, w⟩ | TM M accepts input w}
Status: RE but NOT Recursive (UNDECIDABLE)
Proof: Diagonalization - assume TM H decides HALT,
       build paradoxical TM D(⟨M⟩): runs H on ⟨M,M⟩,
       does opposite → D(⟨D⟩) is a contradiction!
```

---

## Master Comparison Table

| Machine | Memory | δ Return | Input | Language Class |
|---------|--------|----------|-------|---------------|
| DFA | States | One state | L→R | Regular |
| NFA | States | Set of states | L→R | Regular |
| PDA | Stack | (state, stack str) | L→R | CFL |
| TM | Infinite tape | (state, symbol, dir) | Both | RE |

| Grammar | Production Form | Machine | Class |
|---------|----------------|---------|-------|
| Regular (Type 3) | A→aB or A→a | DFA/NFA | Regular |
| Context-Free (Type 2) | A→α | PDA | CFL |
| Context-Sensitive (Type 1) | αAβ→αγβ | LBA | CSL |
| Unrestricted (Type 0) | α→β | TM | RE |

---

## Exam Tips

> [!warning] Common Mistakes to Avoid
>
> 1. **NFA→DFA**: Don't forget to process the ∅ (dead) state!
> 2. **Pumping Lemma**: Choose w carefully - y must be "pumpable out of the language"
> 3. **CNF conversion order**: ALWAYS simplify first (ε, unit, useless) BEFORE converting to CNF
> 4. **PDA traces**: Write complete IDs with all three components (state, input, stack)
> 5. **Moore vs Mealy**: Moore output length = |w|+1; Mealy = |w|
> 6. **DFA minimization**: Cannot merge states from different equivalence classes!
> 7. **TM**: δ is a PARTIAL function - not all (state, symbol) pairs need transitions

> [!tip] Last-Minute Tips
>
> - For DFA problems: think "what do I need to REMEMBER?" → each memory = one dimension of states
> - For PL proofs: the challenge is choosing the right w AND showing pumping fails for ALL splits
> - For CFG simplification: do ε-removal FIRST, otherwise you'll have to redo it
> - For PDA: empty stack method is usually simpler to construct; final state is easier to verify
> - For TM: use marking (X, Y) on tape to track progress across the tape

---

*[[Overview|CS-304 Overview]] | [[Important-Questions|CS-304 Important-Questions]] | [[Interview-Prep|CS-304 Interview-Prep]]*
