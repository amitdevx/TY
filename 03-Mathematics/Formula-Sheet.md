---
title: Mathematics Formula Sheet
tags: [formulas, mathematics, revision, operations-research, quick-reference]
aliases: [Math Formulas, OR Formulas, Formula Reference]
type: formula-sheet
subject_code: MTC-341 MN:B
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[03-Mathematics/Mathematics-Dashboard|Mathematics]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Formula-Sheet]] | [[PYQ]]


# Mathematics Formula Sheet - TY B.Sc. CS

> [!tip] Usage
> This is your go-to quick reference. Memorize highlighted formulas before exams. Use  markers to indicate priority.

---

## PART A: Operations Research

### A.1 Linear Programming Problem (LPP)

#### Standard Form of LPP

$$\text{Maximize (or Minimize)} \quad Z = c_1x_1 + c_2x_2 + \cdots + c_nx_n$$

Subject to:
$$a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \leq b_1$$
$$a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n \leq b_2$$
$$\vdots$$
$$a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n \leq b_m$$
$$x_1, x_2, \ldots, x_n \geq 0$$

#### Matrix Form

$$\text{Maximize } Z = \mathbf{c}^T\mathbf{x}, \quad \text{subject to } A\mathbf{x} \leq \mathbf{b}, \quad \mathbf{x} \geq 0$$

#### Converting to Standard Equality Form (Add Slack Variables)

$$a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n + s_i = b_i \quad (s_i \geq 0)$$

For **≥ constraints** (subtract surplus, add artificial):
$$a_{i1}x_1 + \cdots + a_{in}x_n - s_i + A_i = b_i$$

#### Simplex Method Steps

1. Convert to standard form (add slack variables $s_1, s_2, \ldots$)
2. Set up initial **Simplex Tableau**
3. Find **most negative** $c_j - z_j$ → **entering variable** (pivot column)
4. Compute **minimum ratio test**: $\min\left(\frac{b_i}{a_{ij}}\right)$ for $a_{ij} > 0$ → **leaving variable** (pivot row)
5. **Pivot operation**: make pivot element = 1 (divide row), then eliminate in other rows
6. Repeat until all $c_j - z_j \leq 0$ (for maximization) → **Optimal**

#### Optimality Conditions

| Problem Type | Optimality Condition |
|-------------|---------------------|
| Maximization | All $c_j - z_j \leq 0$ |
| Minimization | All $c_j - z_j \geq 0$ |

#### $z_j$ and $c_j - z_j$ Formulas

$$z_j = \sum_{i=1}^{m} c_{Bi} \cdot a_{ij}$$

$$c_j - z_j = c_j - \sum_{i=1}^{m} c_{Bi} \cdot a_{ij}$$

where $c_{Bi}$ = cost of basic variable in row $i$

#### Big-M Method Steps

1. Add **artificial variables** $A_i$ to equality/≥ constraints
2. Assign cost $-M$ (maximization) or $+M$ (minimization) to artificial variables ($M$ = very large)
3. Set up initial tableau with artificial variables as basis
4. Proceed with Simplex iterations
5. **Optimal if no artificial variable in final basis** (if artificial remains, problem is infeasible)

#### Two-Phase Method

- **Phase I:** Minimize $\sum A_i$ subject to original constraints + artificials
  - If Phase I optimal value $> 0$ → **Infeasible**
  - If Phase I optimal value $= 0$ → proceed to Phase II
- **Phase II:** Use Phase I optimal BFS, replace objective with original, proceed with Simplex

#### Special Cases

| Case | Indication | Action |
|------|-----------|--------|
| Unbounded | No positive ratios in minimum ratio test | Problem unbounded |
| Infeasible | No feasible solution | Check constraints |
| Degenerate | Zero in minimum ratio test | Perturbation/Bland's rule |
| Multiple Optimal | $c_j - z_j = 0$ for non-basic variable at optimum | Alternate optima exist |

---

### A.2 Transportation Problem

#### Mathematical Model

$$\text{Minimize } Z = \sum_{i=1}^{m}\sum_{j=1}^{n} c_{ij} x_{ij}$$

Subject to:
$$\sum_{j=1}^{n} x_{ij} = a_i \quad \forall i = 1, 2, \ldots, m \quad (\text{Supply})$$
$$\sum_{i=1}^{m} x_{ij} = b_j \quad \forall j = 1, 2, \ldots, n \quad (\text{Demand})$$
$$x_{ij} \geq 0 \quad \forall i, j$$

#### Balanced Transportation Problem

$$\sum_{i=1}^{m} a_i = \sum_{j=1}^{n} b_j \quad (\text{Total Supply = Total Demand})$$

If unbalanced: add **dummy source** or **dummy destination** with zero costs.

#### Basic Feasible Solution (BFS) Condition

$$\text{Number of allocations} = m + n - 1$$

If allocations $< m+n-1$ → **Degenerate** (add $\epsilon$ to empty cell)

#### North West Corner Rule (NWCR) Steps

1. Start at top-left (NW) corner cell $(1,1)$
2. Allocate $x_{ij} = \min(a_i, b_j)$
3. If $a_i < b_j$: exhausted row $i$, move **down** (to next row)
4. If $a_i > b_j$: exhausted column $j$, move **right** (to next col)
5. If $a_i = b_j$: exhausted both, move diagonally (handle degeneracy)
6. Repeat until all supply/demand satisfied

#### Least Cost Method (LCM) Steps

1. Find cell with **minimum cost** in entire table
2. Allocate as much as possible $x_{ij} = \min(a_i, b_j)$
3. Cross out exhausted row/column
4. Repeat with remaining cells

#### Vogel's Approximation Method (VAM) Steps

1. Compute **penalty** for each row and column:
   $$\text{Penalty}_i = \text{2nd smallest cost} - \text{smallest cost in row/col}$$
2. Select row/col with **maximum penalty**
3. Allocate to **minimum cost cell** in that row/col
4. Eliminate satisfied row/col, recompute penalties
5. Repeat until all allocated

#### MODI Method (Modified Distribution Method / UV Method) Steps

1. Start with a basic feasible solution (m+n-1 allocations)
2. Assign $u_i$ to rows, $v_j$ to columns such that:
   $$u_i + v_j = c_{ij} \quad \text{for all basic cells}$$
   Set $u_1 = 0$, solve for others
3. Compute **opportunity cost** for non-basic cells:
   $$d_{ij} = c_{ij} - u_i - v_j$$
4. If all $d_{ij} \geq 0$ → **Optimal**
5. If any $d_{ij} < 0$: most negative enters basis (form loop, alternate +/−)
6. Repeat until optimal

#### Stepping Stone Path (Loop)

- Form a **closed loop** through basic cells starting/ending at entering cell
- Alternate + and − signs
- Add entering cell with +, find minimum of − cells
- Reallocate: add min to + cells, subtract from − cells
- The − cell with minimum value leaves basis

---

### A.3 Assignment Problem

#### Mathematical Model

$$\text{Minimize } Z = \sum_{i=1}^{n}\sum_{j=1}^{n} c_{ij} x_{ij}$$

Subject to:
$$\sum_{j=1}^{n} x_{ij} = 1 \quad \forall i \quad (\text{each person assigned exactly once})$$
$$\sum_{i=1}^{n} x_{ij} = 1 \quad \forall j \quad (\text{each job assigned to exactly one person})$$
$$x_{ij} \in \{0, 1\}$$

#### Hungarian Method Steps

**Step 1 - Row Reduction:**
$$c_{ij}' = c_{ij} - \min_j(c_{ij}) \quad \text{for each row } i$$

**Step 2 - Column Reduction:**
$$c_{ij}'' = c_{ij}' - \min_i(c_{ij}') \quad \text{for each col } j$$

**Step 3 - Cover all zeros with minimum lines:**
- Draw minimum number of horizontal/vertical lines to cover all zeros
- If number of lines $= n$ → **Optimal assignment found**

**Step 4 - Revise matrix (if lines $< n$):**
$$\theta = \min(\text{uncovered elements})$$
- Subtract $\theta$ from all uncovered elements
- Add $\theta$ to elements covered by **two lines** (intersection)
- Elements covered by exactly one line: **unchanged**
- Return to Step 3

**Step 5 - Make assignment:**
- Find rows/columns with exactly one zero → assign
- Cross out assigned zeros, repeat

#### Unbalanced Assignment Problem
Add dummy row/column with costs = 0 to make $n \times n$

#### Maximization Assignment Problem
$$c_{ij}^* = \max(c_{ij}) - c_{ij}$$
Then solve as minimization with $c_{ij}^*$

#### Restricted Assignment (Forbidden Cells)
Assign very large cost $M$ to forbidden cell $(i, j)$

---

## PART B: Discrete Mathematics

### B.1 Set Theory

$$A \cup B = \{x : x \in A \text{ or } x \in B\}$$
$$A \cap B = \{x : x \in A \text{ and } x \in B\}$$
$$A - B = \{x : x \in A \text{ and } x \notin B\}$$
$$A' = U - A \quad (\text{Complement})$$
$$|A \cup B| = |A| + |B| - |A \cap B| \quad (\text{Inclusion-Exclusion})$$
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|$$

### B.2 Logic - De Morgan's Laws

$$\neg(P \wedge Q) \equiv \neg P \vee \neg Q$$
$$\neg(P \vee Q) \equiv \neg P \wedge \neg Q$$

#### Logical Equivalences

| Law | Formula |
|-----|---------|
| Double Negation | $\neg\neg P \equiv P$ |
| Identity | $P \wedge T \equiv P$, $P \vee F \equiv P$ |
| Domination | $P \vee T \equiv T$, $P \wedge F \equiv F$ |
| Idempotent | $P \wedge P \equiv P$, $P \vee P \equiv P$ |
| Absorption | $P \vee (P \wedge Q) \equiv P$ |
| Distributive | $P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$ |

### B.3 Graph Theory

#### Euler's Formula (Planar Graphs)

$$V - E + F = 2$$

where $V$ = vertices, $E$ = edges, $F$ = faces (including outer face)

#### Graph Properties

$$\sum_{v \in V} \deg(v) = 2|E| \quad (\text{Handshaking Lemma})$$

For complete graph $K_n$:
$$|E| = \frac{n(n-1)}{2}$$

For bipartite $K_{m,n}$: $|E| = mn$

#### Euler Path/Circuit

| Type | Condition |
|------|----------|
| Euler Circuit | All vertices have even degree |
| Euler Path | Exactly 2 vertices have odd degree |
| Hamiltonian | Visits each vertex exactly once (no simple formula) |

### B.4 Combinatorics

$$P(n, r) = \frac{n!}{(n-r)!} \quad (\text{Permutation})$$

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!} \quad (\text{Combination})$$

$$\binom{n}{r} = \binom{n}{n-r}$$

$$\binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n} = 2^n$$

#### Multinomial Coefficient

$$\frac{n!}{n_1! \cdot n_2! \cdots n_k!} \quad \text{where } n_1 + n_2 + \cdots + n_k = n$$

#### Stars and Bars

Number of ways to place $n$ identical objects into $k$ distinct boxes:
$$\binom{n+k-1}{k-1}$$

### B.5 Probability

#### Basic Axioms

$$0 \leq P(A) \leq 1, \quad P(\Omega) = 1$$
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$P(A') = 1 - P(A)$$

#### Conditional Probability

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

#### Bayes' Theorem

$$P(A_i|B) = \frac{P(B|A_i) \cdot P(A_i)}{\sum_{j=1}^{n} P(B|A_j) \cdot P(A_j)}$$

where $A_1, A_2, \ldots, A_n$ are mutually exclusive and exhaustive events.

#### Total Probability Theorem

$$P(B) = \sum_{i=1}^{n} P(B|A_i) \cdot P(A_i)$$

#### Independence

$$P(A \cap B) = P(A) \cdot P(B) \quad (\text{if A, B independent})$$

#### Expected Value & Variance

$$E[X] = \sum_{x} x \cdot P(X = x) \quad (\text{discrete})$$
$$\text{Var}(X) = E[X^2] - (E[X])^2$$
$$\sigma = \sqrt{\text{Var}(X)}$$

---

## PART C: Number Theory & Algebra

### C.1 Modular Arithmetic

$$a \equiv b \pmod{n} \iff n \mid (a - b)$$

#### Fermat's Little Theorem

$$a^{p-1} \equiv 1 \pmod{p} \quad \text{(p prime, } \gcd(a,p) = 1\text{)}$$

#### Euler's Theorem

$$a^{\phi(n)} \equiv 1 \pmod{n} \quad (\gcd(a,n) = 1)$$

where $\phi(n) = n \prod_{p|n}\left(1 - \frac{1}{p}\right)$

### C.2 Recurrence Relations

#### Linear Recurrence (Homogeneous)

$$a_n = c_1 a_{n-1} + c_2 a_{n-2}$$

Characteristic equation: $r^2 = c_1 r + c_2$

- Two distinct roots $r_1, r_2$: $a_n = A r_1^n + B r_2^n$
- Repeated root $r$: $a_n = (A + Bn)r^n$

#### Fibonacci Numbers

$$F_n = F_{n-1} + F_{n-2}, \quad F_0 = 0, F_1 = 1$$
$$F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}, \quad \phi = \frac{1+\sqrt{5}}{2} \approx 1.618$$

---

## PART D: Calculus & Linear Algebra Review

### D.1 Matrix Operations

$$\det(A) = \sum_{j=1}^{n} a_{1j} C_{1j} \quad (\text{Cofactor expansion})$$

$$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$

$$\text{Rank}(A) = \text{number of non-zero rows in row echelon form}$$

### D.2 Eigenvalues

$$\det(A - \lambda I) = 0 \quad (\text{Characteristic equation})$$

$$\text{trace}(A) = \sum \lambda_i, \quad \det(A) = \prod \lambda_i$$

---

> [!warning] Exam Alert
> Always verify **balanced condition** in transportation before starting. Always check **optimality condition** at each simplex iteration. Hungarian method requires **square matrix** - add dummy if needed.

---

*Formula Sheet | MTC-341 MN:B | Semester V | Last Updated: 2026-06-16*
