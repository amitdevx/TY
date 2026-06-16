---
title: Mathematics Past Year Questions
tags: [pyq, mathematics, exam, operations-research, mtc-341]
aliases: [Math PYQ, OR PYQ, Past Year Questions Mathematics]
type: pyq
subject_code: MTC-341 MN:B
semester: V
created: 2026-06-16
updated: 2026-06-16
---

#  Past Year Questions - Mathematics (MTC-341)

> [!important] Exam Strategy
> Focus on **Problems 3, 4, 5** (Transportation & Assignment) - they carry maximum marks.
> Always show **complete working** including all tableau iterations.

---

## Section A - Short Answer Questions (2 marks each)

> [!note] These appear as compulsory questions

### Unit 1 - LPP

**Q1.** Define Linear Programming Problem. State its assumptions.
> **Expected Answer:** LPP = optimize linear objective subject to linear constraints. Assumptions: linearity, certainty, divisibility, non-negativity, additivity.

**Q2.** What is a slack variable? When is it used?
> **Expected Answer:** Slack variable added to convert $\leq$ to $=$: $ax + s = b$. It represents unused capacity.

**Q3.** Define basic feasible solution (BFS).
> **Expected Answer:** A BFS is a solution where: (1) exactly $m$ variables are basic (non-zero), (2) all basic variables $\geq 0$, (3) constraints are satisfied.

**Q4.** State the optimality condition for maximization in Simplex.
> **Expected Answer:** All $c_j - z_j \leq 0$ for all non-basic variables.

**Q5.** What is degeneracy in Simplex? How is it resolved?
> **Expected Answer:** Occurs when a basic variable becomes zero (tie in minimum ratio test). Resolved by Bland's rule or perturbation.

**Q6.** When is an LPP said to be unbounded?
> **Expected Answer:** When no positive $a_{ij}$ exists in the pivot column → objective can increase indefinitely.

**Q7.** Distinguish between Big-M and Two-Phase methods.
> **Expected Answer:** Big-M: single phase, adds $\pm M$ penalty. Two-Phase: Phase I minimizes artificials, Phase II optimizes original objective.

**Q8.** What are artificial variables? Why are they introduced?
> **Expected Answer:** Artificial variables provide an initial BFS for $\geq$ or $=$ constraints. They are removed (→0) in optimal solution.

### Unit 2 - Transportation

**Q9.** State the mathematical model of the transportation problem.
> **Expected Answer:** Min $Z = \sum\sum c_{ij}x_{ij}$, subject to supply constraints $\sum x_{ij} = a_i$, demand constraints $\sum x_{ij} = b_j$, $x_{ij} \geq 0$.

**Q10.** How many basic cells should a non-degenerate BFS have?
> **Expected Answer:** $m + n - 1$ basic cells for an $m \times n$ transportation problem.

**Q11.** What is a balanced transportation problem?
> **Expected Answer:** $\sum a_i = \sum b_j$ (total supply = total demand).

**Q12.** Define opportunity cost in MODI method.
> **Expected Answer:** $d_{ij} = c_{ij} - u_i - v_j$ for non-basic cells. If all $d_{ij} \geq 0$, solution is optimal.

**Q13.** What is degeneracy in transportation? How to handle it?
> **Expected Answer:** Occurs when allocations $< m+n-1$. Add $\varepsilon$ (small positive) to an independent empty cell.

**Q14.** Explain penalty in Vogel's Approximation Method.
> **Expected Answer:** Penalty = 2nd smallest cost − smallest cost in row/column. Represents cost of NOT using the cheapest route.

### Unit 3 - Assignment

**Q15.** What is an assignment problem? How does it differ from transportation?
> **Expected Answer:** AP = special TP with all supply/demand = 1, 0-1 variables, $n \times n$ matrix. Solved by Hungarian method.

**Q16.** State the Hungarian method steps.
> **Expected Answer:** (1) Row reduce, (2) Col reduce, (3) Cover zeros with min lines, (4) If lines $= n$ → assign; else revise matrix, (5) Make assignment.

**Q17.** How do you convert a maximization assignment to minimization?
> **Expected Answer:** $c_{ij}^* = \max(C) - c_{ij}$, then solve for minimization.

**Q18.** What is an unbalanced assignment problem? How to handle?
> **Expected Answer:** When $n_{persons} \neq n_{jobs}$. Add dummy row/column with zero costs to make it square ($n \times n$).

---

## Section B - Problems (10–15 marks each)

### Unit 1 Problems

**Q19.**  [10 marks] Solve by Simplex method:

Maximize $Z = 3x_1 + 5x_2$

Subject to:
$$x_1 \leq 4, \quad 2x_2 \leq 12, \quad 3x_1 + 5x_2 \leq 25, \quad x_1, x_2 \geq 0$$

> **Hint:** Add slacks $s_1, s_2, s_3$. Initial basis = {$s_1, s_2, s_3$}. Optimal: $x_1=0, x_2=5, Z=25$.

---

**Q20.**  [10 marks] Use Big-M method to solve:

Minimize $Z = x_1 + 2x_2$

Subject to:
$$2x_1 + x_2 \geq 4, \quad x_1 + 7x_2 \geq 7, \quad x_1, x_2 \geq 0$$

> **Hint:** Subtract surplus variables, add artificials with $+M$ cost. Expected: $x_1=3.5, x_2=0$ or check constraints.

---

**Q21.** [8 marks] Formulate as LPP and solve graphically:

A farmer has 100 acres. Wheat gives profit ₹200/acre, rice gives ₹300/acre. Rice requires 1 unit water/acre, wheat requires 0.5 unit. Total water available = 80 units. Find optimal allocation.

> **Hint:** Let $x_1$ = acres of wheat, $x_2$ = acres of rice. Max $Z = 200x_1 + 300x_2$ subject to $x_1+x_2 \leq 100$, $0.5x_1+x_2 \leq 80$.

---

**Q22.** [6 marks] A company makes products A and B. A contributes ₹3 profit and needs 1 hour machine time + 4 hours labor. B contributes ₹5 profit and needs 3 hours machine time + 2 hours labor. Total: 6 machine hours, 16 labor hours. Write LPP formulation and state the optimal solution.

---

### Unit 2 Problems

**Q23.**  [15 marks] Find minimum cost for:

| | $D_1$ | $D_2$ | $D_3$ | $D_4$ | Supply |
|-|-------|-------|-------|-------|--------|
| $S_1$ | 1 | 2 | 6 | 4 | 40 |
| $S_2$ | 3 | 5 | 2 | 1 | 50 |
| $S_3$ | 4 | 6 | 3 | 5 | 30 |
| Demand | 30 | 40 | 25 | 25 | 120 |

Using (i) VAM for initial BFS and (ii) MODI for optimality.

> **Hint:** Total supply=demand=120  (balanced). Apply VAM step-by-step. Then verify with MODI.

---

**Q24.**  [15 marks] Solve transportation problem using NWCR for initial BFS, then optimize with MODI:

| | W1 | W2 | W3 | Supply |
|-|----|----|----|--------|
| F1 | 2 | 3 | 5 | 30 |
| F2 | 7 | 1 | 4 | 40 |
| F3 | 4 | 6 | 8 | 20 |
| Demand | 35 | 30 | 25 | 90 |

---

**Q25.** [10 marks] The following transportation problem is unbalanced. Balance it, find initial solution using LCM, and test for optimality:

| | D1 | D2 | D3 | Supply |
|-|----|----|----|----|
| S1 | 4 | 8 | 1 | 70 |
| S2 | 7 | 2 | 3 | 50 |
| Demand | 40 | 35 | 30 | |

> **Total supply** = 120, **Total demand** = 105. Add dummy $D_4$ with demand 15 and costs 0.

---

### Unit 3 Problems

**Q26.**  [12 marks] Solve using Hungarian method:

| | M1 | M2 | M3 | M4 |
|-|----|----|----|-----|
| W1 | 10 | 5 | 13 | 15 |
| W2 | 3 | 9 | 18 | 3 |
| W3 | 10 | 7 | 2 | 2 |
| W4 | 7 | 11 | 9 | 14 |

> **Hint:** Row reduce → col reduce → cover zeros → if <4 lines apply θ step. Expected: W1→M2, W2→M1, W3→M4, W4→M3 or similar.

---

**Q27.**  [12 marks] A company has 4 salespeople and 5 territories. Profit matrix (in thousands):

| | T1 | T2 | T3 | T4 | T5 |
|-|----|----|----|----|----|
| S1 | 24 | 15 | 35 | 27 | 40 |
| S2 | 28 | 20 | 30 | 25 | 36 |
| S3 | 32 | 18 | 25 | 30 | 28 |
| S4 | 19 | 25 | 22 | 28 | 35 |

Find the optimal assignment to maximize profit.

> **Hint:** Add dummy salesperson with 0 profits. Convert to minimization: $c_{ij}^* = 40 - c_{ij}$.

---

**Q28.** [10 marks] Solve restricted assignment problem:

Worker A cannot be assigned Job 2.
Worker C cannot be assigned Job 1.

| | J1 | J2 | J3 | J4 |
|-|----|----|----|-----|
| A | 9 | ∞ | 7 | 4 |
| B | 5 | 6 | 3 | 8 |
| C | ∞ | 7 | 4 | 6 |
| D | 7 | 5 | 8 | 3 |

---

## Section C - Conceptual Questions

**Q29.** [5 marks] Explain the economic interpretation of $c_j - z_j$ in the Simplex method.

> **Answer:** $z_j$ represents the profit sacrificed by introducing one unit of non-basic variable $j$ (in terms of reduced basic variables). $c_j - z_j$ = net profit of bringing variable $j$ into the basis. If positive, bringing $x_j$ into basis improves objective.

**Q30.** [5 marks] Why is VAM considered superior to NWCR and LCM? Justify with an example.

> **Answer:** VAM considers the penalty (opportunity cost) of not using the cheapest route. This gives a much better initial BFS, often optimal or near-optimal, reducing MODI iterations.

**Q31.** [5 marks] Explain with proof why the number of allocations in a non-degenerate transportation solution must be exactly $m+n-1$.

> **Answer:** Transportation problem has $m+n$ constraints but one is redundant (supply=demand). So rank of constraint matrix = $m+n-1$ → need exactly $m+n-1$ basic variables.

---

## Important Topics Priority Matrix

| Topic | Frequency | Marks | Priority |
|-------|-----------|-------|---------|
| Simplex Method |  | 10-12 |  Must |
| Transportation (VAM+MODI) |  | 12-15 |  Must |
| Hungarian Method |  | 10-12 |  Must |
| Big-M Method |  | 8-10 |  High |
| LPP Formulation |  | 5-8 |  High |
| NWCR / LCM |  | 5-8 |  High |
| Two-Phase Method |  | 6-8 |  Medium |
| Maximization AP |  | 6-8 |  Medium |

---

## Answer Key - Short Questions Summary

| Q# | Key Point |
|----|---------|
| Q1 | Optimize linear objective, linear constraints |
| Q2 | Add to ≤ constraint, represents slack capacity |
| Q3 | m basic variables, all ≥ 0 |
| Q4 | All $c_j - z_j \leq 0$ |
| Q5 | Zero basic variable; Bland's rule |
| Q6 | No positive element in pivot column |
| Q7 | Big-M: one phase; Two-phase: two phases |
| Q8 | Initial BFS for ≥/= constraints |
| Q9 | Min $\sum\sum c_{ij}x_{ij}$ s.t. supply/demand |
| Q10 | $m+n-1$ |
| Q11 | $\sum a_i = \sum b_j$ |
| Q12 | $d_{ij} = c_{ij} - u_i - v_j$ |
| Q13 | Less than $m+n-1$ allocations; add ε |
| Q14 | 2nd min − min cost in row/col |
| Q15 | Special TP, all supply/demand=1, 0-1 vars |
| Q16 | Row reduce→col reduce→cover→revise→assign |
| Q17 | $c_{ij}^* = \max(C) - c_{ij}$ |
| Q18 | Unequal persons/jobs; add dummy with 0 |

---

*PYQ | MTC-341 MN:B | Semester V | Last Updated: 2026-06-16*
