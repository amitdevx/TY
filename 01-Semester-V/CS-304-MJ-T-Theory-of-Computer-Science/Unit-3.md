---
title: "CS-304 Unit-3 - Context-Free Grammars and Languages"
aliases: ["CS304 Unit 3", "CFG Notes", "TCS Ch3", "Context-Free Grammar", "CNF GNF Notes"]
tags:
  - subject/theory-of-computation
  - semester/V
  - unit/3
  - cfg
  - context-free-grammar
  - cnf
  - gnf
  - formal-languages
subject_code: CS-304-MJ-T
unit: 3
chapter: "Chapter 3 - Context-Free Grammars and Languages"
hours: 5
type: unit-notes
last_reviewed: 2026-06-16
---

#  Unit 3 - Context-Free Grammars and Languages

> [!note] Navigation
> [[Overview|CS-304 Overview]] | ← [[Unit-2]] | **Unit 3** → [[Unit-4]] → [[Unit-5]]

---

##  Learning Objectives

- Define context-free grammar (CFG) and its components
- Write CFGs for given context-free languages
- Understand derivations: leftmost, rightmost, parse trees
- Simplify CFGs by removing useless symbols, ε-productions, unit productions
- Convert CFG to Chomsky Normal Form (CNF)
- Convert CFG to Greibach Normal Form (GNF)

---

## 3.1 Context-Free Grammar (CFG) - Definition

> [!important] CFG Definition
> A ==Context-Free Grammar (CFG)== is a 4-tuple:
> **G = (V, T, P, S)** where:
> - **V** = Set of Variables (Non-terminals); uppercase letters
> - **T** = Set of Terminals; lowercase letters, symbols
> - **P** = Set of Productions (rules) of the form **A → α** where A ∈ V, α ∈ (V ∪ T)*
> - **S** = Start symbol (S ∈ V)
> - **V ∩ T = ∅** (variables and terminals are disjoint)

### Terminology

| Term | Meaning | Example |
|------|---------|---------|
| Production | A → α; replaces variable A with string α | S → aSb |
| Derivation | Applying productions to reach terminal string | S ⇒ aSb ⇒ aaSbb ⇒ aabb |
| ⇒ | "Derives in one step" | S ⇒ aSb |
| ⇒* | "Derives in zero or more steps" | S ⇒* aabb |
| Sentential form | Any string derived from S | S, aSb, aaSbb |
| Sentence | Sentential form with only terminals | aabb |
| L(G) | Language of grammar G: {w ∈ T* \| S ⇒* w} | |
| Parse tree | Tree showing derivation structure | |

^cfg-definition

### Example 1: CFG for L = {aⁿbⁿ | n ≥ 1}

```
G = ({S}, {a, b}, P, S)
P: S → aSb | ab
```

**Derivation of "aaabbb":**
```
S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb
```

**Parse tree for "aabb":**
```
        S
      / | \
     a  S  b
       / \
      a   b
```

### Example 2: CFG for Palindromes over {a, b}

```
P: S → aSa | bSb | a | b | ε
```
- ε: empty string is palindrome
- a, b: single chars are palindromes
- aSa: if w is palindrome, awa is palindrome

### Example 3: CFG for Arithmetic Expressions

```
G = ({E, T, F}, {+, *, (, ), id}, P, E)
P:
  E → E + T | T
  T → T * F | F
  F → (E) | id
```

This grammar handles precedence: `*` binds tighter than `+`.

---

## 3.2 Derivations and Parse Trees

### Leftmost Derivation
At each step, replace the **leftmost** variable.

### Rightmost Derivation
At each step, replace the **rightmost** variable.

### Example: Derive "id + id * id" from arithmetic grammar

**Leftmost derivation:**
```
E ⇒ E + T                    (E → E + T)
  ⇒ T + T                    (E → T)
  ⇒ F + T                    (T → F)
  ⇒ id + T                   (F → id)
  ⇒ id + T * F               (T → T * F)
  ⇒ id + F * F               (T → F)
  ⇒ id + id * F              (F → id)
  ⇒ id + id * id             (F → id)
```

### Ambiguous Grammar

> [!warning] Ambiguity
> A grammar G is ==ambiguous== if some string w ∈ L(G) has **more than one parse tree** (or more than one leftmost/rightmost derivation).

**Example of ambiguous grammar:**
```
E → E + E | E * E | (E) | id
```
For `id + id * id`, two parse trees exist - addition-first or multiplication-first. This grammar is inherently ambiguous for precedence.

---

## 3.3 CFG Simplification

> [!important] Simplification Steps (in order!)
> 1. Remove **ε-productions** (nullable variables)
> 2. Remove **unit productions** (A → B)
> 3. Remove **useless symbols** (unreachable or non-generating)

### Step 1: Remove ε-Productions (Nullable Variables)

**Algorithm:**
```
1. Find NULLABLE = {A ∈ V | A ⇒* ε}
   - Base: if A → ε ∈ P, then A is nullable
   - Inductive: if A → B₁B₂...Bₖ and all Bᵢ are nullable, then A is nullable
2. For each production A → α containing nullable variables,
   add all combinations with/without the nullable variables
   (but don't add A → ε unless A is the start symbol)
3. Remove all ε-productions (except S → ε if ε ∈ L)
```

**Example:**

```
G:
S → aAbB
A → ε | a
B → ε | b

Step 1: NULLABLE = {A, B}
Step 2: For S → aAbB, since A and B are nullable:
  Original: S → aAbB
  A absent:  S → abB
  B absent:  S → aAb
  Both absent: S → ab
  All added: S → aAbB | abB | aAb | ab
  
  A → ε | a → A → a (remove ε)
  B → ε | b → B → b (remove ε)
  
New grammar:
S → aAbB | abB | aAb | ab
A → a
B → b
```

^epsilon-removal

### Step 2: Remove Unit Productions (A → B)

**Algorithm:**
```
1. Compute UNIT(A) = {B | A ⇒* B using only unit productions}
   (unit closure of A)
2. For each A and each B ∈ UNIT(A):
   For each non-unit production B → α:
     Add A → α
3. Remove all unit productions
```

**Example:**

```
G:
S → A | B | aS
A → B | a
B → b

Step 1: UNIT(S) = {S, A, B}, UNIT(A) = {A, B}, UNIT(B) = {B}

Step 2:
S → A (unit): look at non-unit from A: A → a → add S → a
                           from B: B → b → add S → b
S → B (unit): B → b → add S → b (already added)

New grammar:
S → aS | a | b
A → a | b
B → b
```

^unit-production-removal

### Step 3: Remove Useless Symbols

**A symbol X is USEFUL if:**
- It is **generating**: X ⇒* w for some terminal string w
- It is **reachable**: S ⇒* αXβ for some α, β

**Algorithm:**
```
Step 3a: Remove non-generating symbols
  1. Find all generating symbols (start with terminals, add variables that can reach terminals)
  2. Remove all non-generating symbols and productions containing them

Step 3b: Remove unreachable symbols
  1. Start with {S}, find all reachable symbols
  2. Remove all unreachable symbols and productions
```

---

## 3.4 Chomsky Normal Form (CNF)

> [!important] Chomsky Normal Form (CNF)
> A CFG is in ==CNF== if every production is of the form:
> - **A → BC** (two variables) or
> - **A → a** (single terminal) or
> - **S → ε** (only if ε ∈ L(G))
>
> Every CFL has a CFG in CNF.

### CNF Conversion Algorithm

```
1. First simplify (remove ε-prods, unit prods, useless symbols)
2. For each production A → X₁X₂...Xₖ (k ≥ 2):
   a. Replace any terminal Xᵢ in a production of length ≥ 2 with a new variable Cₐ
      and add Cₐ → a
   b. Break productions of length > 2:
      A → X₁X₂X₃ becomes A → X₁D₁, D₁ → X₂X₃
      A → X₁X₂X₃X₄ becomes A → X₁D₁, D₁ → X₂D₂, D₂ → X₃X₄
```

### CNF Conversion Example

**Given:**
```
S → aABb
A → a | aA | ε
B → b | bB | ε
```

**Step 1: Remove ε-productions**
NULLABLE = {A, B}
```
S → aABb | aBb | aAb | ab
A → a | aA
B → b | bB
```

**Step 2: Already no unit productions**

**Step 3: No useless symbols**

**Step 4: Convert to CNF**

Productions of length ≥ 2 containing terminals - replace terminals:
- Create: Cₐ → a, C_b → b

```
S → CₐABb → CₐABC_b   (replace 'b' in terminal position of length-4 prod)
    aBb    → CₐBC_b
    aAb    → CₐAC_b
    ab     → CₐC_b           (already length 2)
A → a      
   aA     → CₐA             
B → b      
   bB     → C_bB            
Cₐ → a    
C_b → b   
```

Now break length > 2:
- `S → CₐABC_b`: A → CₐD₁, D₁ → AB, D₂... wait: S → Cₐ(ABCB):
  `S → CₐD₁, D₁ → AD₂, D₂ → BC_b`
- `S → CₐBC_b`: S → CₐD₃, D₃ → BC_b
- `S → CₐAC_b`: S → CₐD₄, D₄ → AC_b

**Final CNF:**
```
S  → CₐD₁ | CₐD₃ | CₐD₄ | CₐC_b
D₁ → AD₂
D₂ → BC_b
D₃ → BC_b
D₄ → AC_b
A  → a | CₐA
B  → b | C_bB
Cₐ → a
C_b → b
```

^cnf-conversion

---

## 3.5 Greibach Normal Form (GNF)

> [!important] Greibach Normal Form (GNF)
> A CFG is in ==GNF== if every production is of the form:
> **A → aα** where a ∈ T (terminal) and α ∈ V* (string of variables, possibly empty)
>
> Every CFL has a CFG in GNF. GNF is useful for constructing PDAs.

### Properties of GNF
- Every production starts with exactly one terminal
- Each derivation step reads exactly one input symbol
- Useful for proving closure properties and PDA construction

### GNF Conversion (Outline)

```
1. Bring grammar to CNF first (easier starting point)
2. Eliminate left recursion:
   - Direct left recursion: A → Aα | β becomes A → βA', A' → αA' | ε
3. Apply substitution so every production starts with terminal
4. May need to introduce new variables
```

### Example: Simple GNF Conversion

**Given CNF:**
```
S → AB | a
A → a | aS
B → b
```

**Already partially in GNF!**
- S → AB: not in GNF (starts with variable) - need to substitute
- S → a 
- A → a 
- A → aS 
- B → b 

**Fix S → AB:**
Substitute A → a | aS:
- S → aB | aSB

Now substitute B → b:
- S → ab | aSb

**Final GNF:**
```
S  → ab | aSb | a
A  → a | aS
B  → b
```

Verify: every production starts with terminal 

---

##  Interview Questions - Unit 3

> [!question] Key Interview/Exam Questions

1. **Define CFG. What are its four components?**
   - CFG = (V, T, P, S); V=non-terminals, T=terminals, P=productions (A→α), S=start symbol

2. **What is the difference between a derivation and a parse tree?**
   - Derivation: sequence of production applications (linear); Parse tree: hierarchical tree structure showing the same derivation

3. **What is an ambiguous grammar?**
   - A grammar where at least one string has two or more distinct parse trees (or leftmost/rightmost derivations)

4. **What are nullable variables? How do you find them?**
   - Variables that can derive ε; found by: base case (A→ε), then close (if A→B₁...Bₖ and all Bᵢ nullable, then A nullable)

5. **What is CNF? Why is it useful?**
   - Every production: A→BC or A→a; useful for CYK parsing algorithm (O(n³)), proves every CFL is generated by such grammar

6. **What is GNF? How does it differ from CNF?**
   - GNF: A→aα (terminal then variables); CNF: A→BC or A→a; GNF useful for PDA construction

7. **How do you remove unit productions?**
   - Compute unit closure; for each (A,B) in unit closure and each non-unit B→α, add A→α; then remove unit productions

8. **What is a context-free language?**
   - Language generated by some CFG; examples: {aⁿbⁿ}, palindromes, balanced parentheses, arithmetic expressions

---

##  Revision Summary

> [!summary] Unit 3 Key Takeaways
>
> **CFG = (V, T, P, S):**
> - Productions: A → α (any string of variables and terminals)
> - Language L(G) = all terminal strings derivable from S
>
> **Simplification Order:**
> 1. Remove ε-productions (find nullable, add combinations)
> 2. Remove unit productions (compute unit closure, add shortcuts)
> 3. Remove useless symbols (non-generating first, then unreachable)
>
> **CNF:**
> - A → BC or A → a
> - Conversion: (1) Simplify (2) Replace terminals in long prods (3) Break long prods
>
> **GNF:**
> - A → aα (terminal first, then variables)
> - Eliminate left recursion, substitute to get terminal first
>
> **Key CFL Examples:**
> - {aⁿbⁿ}: S → aSb | ab
> - Palindromes: S → aSa | bSb | a | b | ε
> - Balanced parens: S → SS | (S) | ε

^unit3-tcs-revision

---

*← [[Unit-2]] | [[Overview|CS-304 Overview]] | Next: [[Unit-4]] →*
