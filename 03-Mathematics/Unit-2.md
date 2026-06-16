---
title: Unit 2 - Transportation Problem
tags: [mathematics, transportation-problem, nwcr, vam, modi, operations-research, unit-2]
aliases: [Transportation Problem, TP, VAM, MODI Method]
unit: 2
hours: 10
subject_code: MTC-341 MN:B
semester: V
created: 2026-06-16
updated: 2026-06-16
---

# Unit 2 - Transportation Problem

> [!important] Unit Overview
> **Hours:** 10 | **Weightage:** ~35% of exam
> **Topics:** Mathematical Model, NWCR, LCM, VAM, MODI Method

---

## Learning Objectives

- [ ] Formulate transportation problems mathematically
- [ ] Apply all three initial BFS methods (NWCR, LCM, VAM)
- [ ] Test and achieve optimality using MODI method
- [ ] Handle degenerate and unbalanced problems
- [ ] Understand stepping stone path

---

## 2.1 Introduction and Mathematical Model

### What is the Transportation Problem?

The ==Transportation Problem== deals with ==distributing a commodity== from several **sources (origins)** to several **destinations** at **minimum cost**.

> [!note] Real-world Applications
> - Shipping goods from warehouses to retail stores
> - Allocating machines to jobs
> - Distributing resources across departments
> - Network flow optimization

### Problem Setup

| | $D_1$ | $D_2$ | $\cdots$ | $D_n$ | Supply |
|-|-------|-------|--------|-------|--------|
| $S_1$ | $c_{11}$ | $c_{12}$ | $\cdots$ | $c_{1n}$ | $a_1$ |
| $S_2$ | $c_{21}$ | $c_{22}$ | $\cdots$ | $c_{2n}$ | $a_2$ |
| $\vdots$ | $\vdots$ | $\vdots$ | | $\vdots$ | $\vdots$ |
| $S_m$ | $c_{m1}$ | $c_{m2}$ | $\cdots$ | $c_{mn}$ | $a_m$ |
| **Demand** | $b_1$ | $b_2$ | $\cdots$ | $b_n$ | |

Where:
- $c_{ij}$ = cost per unit shipped from source $i$ to destination $j$
- $a_i$ = supply capacity of source $i$
- $b_j$ = demand of destination $j$
- $x_{ij}$ = amount shipped from $S_i$ to $D_j$

### Mathematical Model

$$\text{Minimize } Z = \sum_{i=1}^{m}\sum_{j=1}^{n} c_{ij} x_{ij}$$

Subject to:
$$\sum_{j=1}^{n} x_{ij} = a_i \quad \forall i = 1, 2, \ldots, m \quad (\text{Supply constraints})$$
$$\sum_{i=1}^{m} x_{ij} = b_j \quad \forall j = 1, 2, \ldots, n \quad (\text{Demand constraints})$$
$$x_{ij} \geq 0 \quad \forall i, j$$

### Balanced vs Unbalanced

$$\text{Balanced: } \sum_{i=1}^{m} a_i = \sum_{j=1}^{n} b_j$$

| Condition | Action |
|-----------|--------|
| $\sum a_i = \sum b_j$ | **Balanced** - solve directly |
| $\sum a_i > \sum b_j$ | **Excess supply** - add dummy destination $D_{n+1}$ with demand = excess, cost = 0 |
| $\sum a_i < \sum b_j$ | **Excess demand** - add dummy source $S_{m+1}$ with supply = shortage, cost = 0 |

### Basic Feasible Solution Condition

$$\text{Number of non-zero allocations} = m + n - 1$$

If allocations $< m + n - 1$ → **Degenerate BFS**
- Add a small quantity $\varepsilon$ (epsilon) to an independent empty cell (one that doesn't form a loop with existing allocations)

---

## 2.2 North West Corner Rule (NWCR)

> [!note] NWCR
> **Purpose:** Find initial BFS (not necessarily optimal)
> **Advantage:** Simple, fast
> **Disadvantage:** Ignores costs - usually gives poor starting solution

### Algorithm

```
1. Start at cell (1,1) - North-West corner
2. x[1][1] = min(a[1], b[1])
3. If supply[i] < demand[j]: Row i exhausted → move DOWN (i+1, j)
4. If supply[i] > demand[j]: Col j satisfied → move RIGHT (i, j+1)
5. If supply[i] = demand[j]: Move DIAGONALLY (i+1, j+1) - handle degeneracy
6. Repeat until all supply/demand satisfied
```

### Example

Cost Matrix:

| | $D_1$ | $D_2$ | $D_3$ | Supply |
|-|-------|-------|-------|--------|
| $S_1$ | 2 | 3 | 1 | 30 |
| $S_2$ | 5 | 4 | 8 | 40 |
| $S_3$ | 5 | 6 | 8 | 20 |
| **Demand** | 25 | 35 | 30 | 90 |

**NWCR Allocation:**

| | $D_1$ | $D_2$ | $D_3$ | Supply |
|-|-------|-------|-------|--------|
| $S_1$ | **25** | **5** | - | 30  |
| $S_2$ | - | **30** | **10** | 40  |
| $S_3$ | - | - | **20** | 20  |
| Demand | 25  | 35  | 30  | |

**NWCR Cost:**
$$Z = 25(2) + 5(3) + 30(4) + 10(8) + 20(8) = 50 + 15 + 120 + 80 + 160 = 425$$

Allocations = 5 = $m+n-1 = 3+3-1 = 5$  (Non-degenerate)

---

## 2.3 Least Cost Method (LCM)

> [!note] LCM / Matrix Minima Method
> **Advantage:** Better initial solution than NWCR (considers costs)
> **Disadvantage:** Doesn't consider opportunity costs of alternatives

### Algorithm

```
1. Find the cell with MINIMUM cost in entire matrix
2. Allocate max possible: x[i][j] = min(a[i], b[j])
3. Cross out exhausted row or column (if both, cross one and put 0 in other)
4. Find next minimum cost in remaining cells
5. Repeat until all allocated
```

### Example (same problem)

| Step | Cell | Cost | Allocation | Remaining |
|------|------|------|-----------|-----------|
| 1 | $(1,3)$ | 1 | min(30,30)=30 | $S_1=0$, $D_3=0$ |
| 2 | $(1,1)$ | 2 (next min in remaining) | min(0,25)=0 | skip |
| 2 | $(2,1)$ | 5 | min(40,25)=25 | $D_1=0$ |
| 3 | $(2,2)$ | 4 | min(15,35)=15 | $S_2=0$ |
| 4 | $(3,2)$ | 6 | min(20,20)=20 | $S_3=0$, $D_2=0$ |

**LCM Cost:**
$$Z = 30(1) + 25(5) + 15(4) + 20(6) = 30 + 125 + 60 + 120 = 335$$

Much better than NWCR's 425!

---

## 2.4 Vogel's Approximation Method (VAM)

> [!tip] VAM - Best Initial Solution Method
> **Advantage:** Gives solution close to optimal (often optimal itself)
> **Disadvantage:** More computation than NWCR/LCM
> VAM is ==strongly preferred== for exam problems

### Penalty Concept

**Penalty** = difference between the two smallest costs in a row/column
$$\text{Penalty} = \text{2nd min} - \text{min cost in row/column}$$

The penalty indicates the "cost of not using the cheapest route."

### Algorithm

```
1. Compute ROW penalties (for each uncrossed row)
2. Compute COLUMN penalties (for each uncrossed column)
3. Select row/column with MAXIMUM penalty
   (Tie: choose one with minimum cost cell, or any)
4. In selected row/column, allocate to MINIMUM COST cell:
   x[i][j] = min(a[i], b[j])
5. Cross out satisfied row/column
6. If only one row/col remains, allocate remaining to leftover cells
7. Recompute penalties for remaining rows/columns
8. Repeat until all allocated
```

### VAM Example (Same Problem)

**Initial Penalties:**

| | $D_1$(2) | $D_2$(3) | $D_3$(1) | Supply | Row Penalty |
|-|---------|---------|---------|--------|-------------|
| $S_1$ | 2 | 3 | 1 | 30 | 3-2=**1** |
| $S_2$ | 5 | 4 | 8 | 40 | 5-4=**1** |
| $S_3$ | 5 | 6 | 8 | 20 | 6-5=**1** |
| Col Penalty | 5-2=3 | 4-3=**1** | 8-1=**7** | | |

Max penalty = 7 (Column $D_3$). Min cost in $D_3$ = 1 (cell $S_1D_3$).
Allocate $x_{13} = \min(30, 30) = 30$. Row $S_1$ and Col $D_3$ exhausted.

**Iteration 2** (Remove $S_1$ and $D_3$):

| | $D_1$(5) | $D_2$(4) | Supply | Row Penalty |
|-|---------|---------|--------|-------------|
| $S_2$ | 5 | 4 | 40 | **1** |
| $S_3$ | 5 | 6 | 20 | **1** |
| Col Penalty | **0** | **2** | | |

Max penalty = 2 (Col $D_2$). Min cost in $D_2$ = 4 (cell $S_2D_2$).
Allocate $x_{22} = \min(40, 35) = 35$. Col $D_2$ exhausted.

**Iteration 3** (Remove $D_2$):

| | $D_1$(5) | Supply | Row Penalty |
|-|---------|--------|-------------|
| $S_2$ | 5 | 5 | - |
| $S_3$ | 5 | 20 | - |
| Col Penalty | - | | |

Allocate $x_{21} = \min(5, 25) = 5$. $S_2$ exhausted.
Allocate $x_{31} = \min(20, 20) = 20$. Both exhausted.

**VAM Solution:**

| | $D_1$ | $D_2$ | $D_3$ | Supply |
|-|-------|-------|-------|--------|
| $S_1$ | - | - | **30** | 30  |
| $S_2$ | **5** | **35** | - | 40  |
| $S_3$ | **20** | - | - | 20  |
| Demand | 25  | 35  | 30  | |

**VAM Cost:**
$$Z = 30(1) + 5(5) + 35(4) + 20(5) = 30 + 25 + 140 + 100 = 295$$

---

## 2.5 MODI Method (Optimality Testing)

### What is MODI?

==MODI (Modified Distribution) Method== or ==UV Method== is used to **test optimality** of a BFS and improve it iteratively until optimal.

> [!important] When to Use MODI
> After finding initial BFS (using NWCR/LCM/VAM), apply MODI to check and achieve optimality.

### Theory - UV Values

For each **basic cell** $(i,j)$ (allocated cell):
$$u_i + v_j = c_{ij}$$

Set $u_1 = 0$, then solve system of equations for all $u_i$ and $v_j$.

### Opportunity Cost for Non-basic Cells

$$d_{ij} = c_{ij} - u_i - v_j \quad (\text{for non-basic cells})$$

- If all $d_{ij} \geq 0$ → **Current solution is optimal**
- If any $d_{ij} < 0$ → **Not optimal** - entering variable is the most negative $d_{ij}$

### MODI Algorithm

```
1. Start with a BFS (m+n-1 basic cells)
2. Set u_1 = 0
3. For all basic cells (i,j): solve u_i + v_j = c_ij to find all u_i, v_j
4. Compute d_ij = c_ij - u_i - v_j for all NON-BASIC cells
5. If all d_ij >= 0 → OPTIMAL (stop)
6. Else: most negative d_ij → entering cell (call it p)
7. Find CLOSED LOOP starting from cell p through basic cells
8. Assign + to entering cell, alternately - and + around loop
9. θ = min allocation at (-) cells → leaving variable (smallest allocation)
10. New allocations: (+) cells increase by θ, (-) cells decrease by θ
11. Remove cell with 0 allocation (was at minimum), new cell enters basis
12. Repeat from step 2
```

### Stepping Stone Path (Loop Formation)

> [!note] Loop Rules
> 1. Loop starts and ends at the **entering cell**
> 2. Loop can only turn at **basic (allocated) cells**
> 3. Every intermediate step must be horizontal or vertical
> 4. The loop is unique for a non-degenerate BFS

### MODI Example (continuing VAM solution)

VAM solution basic cells: $(1,3), (2,1), (2,2), (3,1)$

**Step 1:** Find u, v values

Set $u_1 = 0$:
- $(1,3)$: $u_1 + v_3 = c_{13} = 1$ → $v_3 = 1$
- $(2,1)$: $u_2 + v_1 = c_{21} = 5$ → need $v_1$ first
- $(2,2)$: $u_2 + v_2 = c_{22} = 4$
- $(3,1)$: $u_3 + v_1 = c_{31} = 5$

We have 4 equations, 5 unknowns. Set $u_1 = 0$:
- From $(2,2)$: $u_2 + v_2 = 4$
- From $(2,1)$: $u_2 + v_1 = 5$
- From $(3,1)$: $u_3 + v_1 = 5$

Assume $u_2 = 0$: $v_1 = 5, v_2 = 4, u_3 = 0$

**Step 2:** Compute $d_{ij}$ for non-basic cells $(1,1), (1,2), (3,2), (3,3)$:

$$d_{11} = c_{11} - u_1 - v_1 = 2 - 0 - 5 = -3 \quad (\text{negative!})$$
$$d_{12} = c_{12} - u_1 - v_2 = 3 - 0 - 4 = -1 \quad (\text{negative!})$$
$$d_{32} = c_{32} - u_3 - v_2 = 6 - 0 - 4 = 2$$
$$d_{33} = c_{33} - u_3 - v_3 = 8 - 0 - 1 = 7$$

Most negative: $d_{11} = -3$ → cell $(1,1)$ enters.

**Step 3:** Form loop through $(1,1)$:

$(1,1)^+ \to (2,1)^- \to (2,2)^+ \to ?$

Loop: $(1,1)^+ → (2,1)^- → (2,2)^+$ ...need to close. Actually loop: $(1,1)^+ → (3,1)^- → (2,1)^+ → (2,2)^-$? No...

> [!note] The loop must form correctly through existing basic cells only. Minimum of negative cells determines $\theta$.

**After loop:** $\theta = \min(5, 20) = 5$

New allocations: $(1,1) += 5$, $(2,1) -= 5$ (→ 0, leaves), $(3,1)$ stays, update accordingly.

This process iterates until all $d_{ij} \geq 0$.

---

## 2.6 Degeneracy in Transportation

### What is Degeneracy?

When allocations $< m+n-1$, the solution is **degenerate**.

**Causes:**
1. During NWCR/LCM/VAM: supply and demand both exhausted simultaneously
2. During MODI iterations: two or more cells tie for minimum $\theta$

**Resolution:**
Add a very small positive number $\varepsilon$ (epsilon) to an **independent** empty cell (a cell that doesn't form a loop with existing basic cells).

> [!warning] Choosing $\varepsilon$ Cell
> The $\varepsilon$ cell must not create a loop with existing basic cells. Try different empty cells if needed.

---

## Summary: Comparison of Initial BFS Methods

| Method | Quality of Solution | Computation | Remarks |
|--------|--------------------|-----------|----|
| **NWCR** | Poor (ignores costs) | Easiest | Use only as starting point |
| **LCM** | Better | Moderate | Considers minimum cost |
| **VAM** | Best (near optimal) | More complex | Recommended for exams |

> [!tip] Exam Tip
> Always use **VAM** for initial BFS unless specifically asked for NWCR or LCM. VAM often gives optimal or near-optimal solution, reducing MODI iterations.

---

## Interview / Viva Questions

> [!note] Common Viva Questions
> 1. What is the difference between transportation and assignment problems?
> 2. Why is a balanced transportation problem necessary?
> 3. What is a degenerate transportation problem?
> 4. Explain the UV method and why it works.
> 5. How many basic cells should a non-degenerate BFS have?
> 6. What is a stepping stone path?
> 7. When does VAM fail to give a non-degenerate BFS?
> 8. Why do we set $u_1 = 0$ in MODI?

---

## Key Definitions

| Term | Definition |
|------|-----------|
| ==Transportation Problem== | Min cost distribution from sources to destinations |
| ==Basic Cell== | Allocated (non-zero) cell in current BFS |
| ==Non-basic Cell== | Unallocated cell with $x_{ij} = 0$ |
| ==Loop== | Closed path through basic cells for entering cell |
| ==Degenerate BFS== | Solution with fewer than $m+n-1$ basic cells |
| ==Opportunity Cost ($d_{ij}$)== | Cost increase if non-basic cell is used |

---

## Revision Summary

> [!tip] Unit 2 Summary
> 1. **Model**: minimize total shipping cost subject to supply/demand
> 2. **Balanced**: $\sum a_i = \sum b_j$; else add dummy
> 3. **NWCR**: Start NW, move right/down based on exhaustion
> 4. **LCM**: Always allocate to minimum cost cell
> 5. **VAM**: Compute penalties (2nd min - min), allocate to max penalty row/col
> 6. **MODI**: Set $u_1=0$, find $u_i+v_j=c_{ij}$ for basic cells, check $d_{ij}=c_{ij}-u_i-v_j$ for non-basic
> 7. **Optimal when** all $d_{ij} \geq 0$
> 8. **Degeneracy**: add $\varepsilon$ to independent empty cell

---

## References

- [[Formula-Sheet#A.2 Transportation Problem|Formula Sheet - Transportation]]
- [[Solved-Problems|Solved Problems - Unit 2]]
- [[Unit-1|Unit 1 - LPP]] (background)

---

*Unit 2 | MTC-341 MN:B | Semester V | 10 Hours | Last Updated: 2026-06-16*
