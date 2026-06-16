---
title: Mathematics Revision Notes
tags: [mathematics, revision, quick-reference, exam-prep, operations-research]
aliases: [Math Revision, OR Revision]
type: revision
subject_code: MTC-341 MN:B
semester: V
created: 2026-06-16
updated: 2026-06-16
---

#  Mathematics Revision Notes - MTC-341

> [!warning] Exam Ready Reference
> This file contains **concise summaries** for last-day revision. For full theory, see [[Unit-1]], [[Unit-2]], [[Unit-3]]. For formulas, see [[Formula-Sheet]].

---

##  UNIT 1 LIGHTNING REVIEW - LPP

### Core Concept in 3 Lines

> LPP = Optimize a **linear** objective function subject to **linear** constraints and non-negativity.
> Standard form: all $\leq$ become $=$ via slack variables. All $\geq$ become $=$ via surplus + artificial.
> Simplex moves from BFS to BFS, improving $Z$ at each step.

### Simplex - 5-Step Quick Process

```
① Standard form: add slack s_i to ≤ constraints
② Initial tableau: basis = {all slacks}
③ Enter: most positive c_j - z_j (column)
④ Leave: min ratio b_i/a_ij (row), a_ij > 0
⑤ Pivot → repeat until all c_j - z_j ≤ 0
```

### Entering & Leaving Rules

| Rule | Entering Variable | Leaving Variable |
|------|-----------------|-----------------|
| **Maximization** | Most **positive** $c_j-z_j$ | Minimum **ratio** $b_i/a_{ij}$ ($a_{ij}>0$) |
| **Minimization** | Most **negative** $c_j-z_j$ | Same minimum ratio test |

### Big-M vs Two-Phase

| | Big-M | Two-Phase |
|-|-------|----------|
| Phases | 1 | 2 |
| Artificial cost | $\pm M$ | 0 in Phase II |
| Infeasibility | $A_i>0$ at optimum | Phase I $w^*>0$ |
| Use when | Hand calculations | Computer |

### Special Cases - Quick ID

| Symptom | Case |
|---------|------|
| No positive $a_{ij}$ in pivot col | Unbounded |
| Artificial stays positive at end | Infeasible |
| Min ratio = 0 | Degenerate |
| $c_j-z_j=0$ for non-basic | Multiple optimal |

---

##  UNIT 2 LIGHTNING REVIEW - Transportation

### Core Concept in 3 Lines

> Transportation: ship from $m$ sources to $n$ destinations at min cost.
> Need $m+n-1$ basic allocations (non-degenerate BFS).
> Find initial BFS → test with MODI → improve if $d_{ij}<0$.

### Three Methods for Initial BFS

```
NWCR:    Start top-left → go right or down based on exhaustion
LCM:     Always allocate to MINIMUM COST cell available  
VAM:     Compute penalties → allocate to max-penalty row/col's min-cost cell
```

### Penalty Formula (VAM)

$$\text{Penalty} = c^{(2)}_{\min} - c^{(1)}_{\min} \quad \text{(2nd min − min)}$$

### MODI Algorithm in 5 Steps

```
① Set u_1 = 0
② Solve u_i + v_j = c_ij for all BASIC cells
③ Compute d_ij = c_ij - u_i - v_j for NON-BASIC cells
④ If all d_ij ≥ 0 → OPTIMAL! Stop.
⑤ Else: most negative d_ij enters → form loop → θ = min(−cells) → update
```

### Degeneracy Fix

$$\text{If allocations} < m+n-1: \text{ add } \varepsilon \text{ to independent empty cell}$$

### Balanced Check

$$\sum a_i = \sum b_j? \quad \text{YES → solve directly. NO → add dummy (cost=0)}$$

---

##  UNIT 3 LIGHTNING REVIEW - Assignment

### Core Concept in 2 Lines

> Assignment: assign $n$ persons to $n$ jobs one-to-one to minimize cost.
> Hungarian method: reduce matrix → cover zeros → revise → assign.

### Hungarian Method - 5 Steps

```
① Row reduction: subtract row min from each row
② Column reduction: subtract col min from each col
③ Cover all zeros with minimum lines
④ If lines = n → OPTIMAL (Step 5); else revise:
   θ = min uncovered → subtract θ from uncovered → add θ to intersections
⑤ Assign: find unique zeros (one per row/col)
```

### θ Operation (Step 4) Rules

| Cell Type | Operation |
|-----------|-----------|
| Uncovered | Subtract $\theta$ |
| Covered by 1 line | No change |
| Covered by 2 lines (intersection) | Add $\theta$ |

### Special Cases

| Situation | Solution |
|-----------|---------|
| $n_{jobs} \neq n_{persons}$ | Add dummy row/col (costs = 0) |
| Maximize profit | $c_{ij}^* = \max(C) - c_{ij}$ then minimize |
| Forbidden assignment | Set $c_{ij} = M$ (very large) |
| Multiple optimal | Multiple zero positions allow multiple assignments |

---

##  Master Formula Reference

### LPP
$$Z = \sum c_j x_j, \quad z_j = \sum c_{Bi} a_{ij}, \quad c_j - z_j = c_j - z_j$$

### Transportation
$$Z = \sum\sum c_{ij}x_{ij}, \quad d_{ij} = c_{ij} - u_i - v_j, \quad u_i+v_j=c_{ij}(\text{basic})$$

### Assignment
$$\text{Row reduce: } r_{ij} = c_{ij} - \min_k c_{ik}$$
$$\text{Col reduce: } r'_{ij} = r_{ij} - \min_k r_{kj}$$
$$\text{Maximize: } c^*_{ij} = \max(C) - c_{ij}$$

---

##  Exam Day Checklist

### Before Starting Each Problem

- [ ] Read problem carefully (maximize or minimize?)
- [ ] Check if balanced (transportation)
- [ ] Check if square matrix (assignment)
- [ ] Identify which method to use

### Simplex - Common Mistakes to Avoid

- [ ] Don't forget to convert objective for minimization
- [ ] Check all $c_j-z_j$, not just first one
- [ ] Ratio test: only use rows with **positive** pivot column elements
- [ ] Update $z_j$ row correctly after each pivot

### Transportation - Common Mistakes to Avoid

- [ ] Verify balanced condition first
- [ ] Count allocations: must be $m+n-1$
- [ ] If degenerate: add $\varepsilon$ before MODI
- [ ] MODI: set $u_1=0$, solve equations correctly
- [ ] Loop must alternate $+/-$ at **basic** cells only

### Assignment - Common Mistakes to Avoid

- [ ] Apply BOTH row and column reduction
- [ ] Count lines carefully (minimum number)
- [ ] $\theta$ = minimum **uncovered** element
- [ ] Add $\theta$ to **intersection** cells (doubly covered)
- [ ] Check: each person assigned to exactly one job

---

##  Common Abbreviations

| Term | Full Form |
|------|-----------|
| LPP | Linear Programming Problem |
| BFS | Basic Feasible Solution |
| NWCR | North West Corner Rule |
| LCM | Least Cost Method |
| VAM | Vogel's Approximation Method |
| MODI | Modified Distribution Method |
| AP | Assignment Problem |
| TP | Transportation Problem |
| OR | Operations Research |

---

##  Marks Distribution Guide

| Unit | Expected Marks | Key Topics |
|------|---------------|-----------|
| Unit 1 | 25-30% | Simplex, Big-M |
| Unit 2 | 35-40% | VAM + MODI |
| Unit 3 | 30-35% | Hungarian |

> [!tip] Time Management in Exam
> - **Short answers** (Section A): ~2 min each
> - **Medium problems**: ~15-20 min each
> - **Full transportation/assignment**: ~25 min
> - Always attempt the problem you know best first

---

##  Key Numbers to Remember

| Concept | Number/Formula |
|---------|---------------|
| Transportation BFS count | $m+n-1$ |
| Optimality condition (max) | All $c_j-z_j \leq 0$ |
| Optimality condition (min) | All $c_j-z_j \geq 0$ |
| MODI: start value | $u_1 = 0$ |
| Hungarian: optimal condition | Lines $= n$ |
| Balanced TP | $\sum a_i = \sum b_j$ |

---

## Last 24 Hours - What to Review

### Hour 1: Formulas
- [ ] Skim [[Formula-Sheet]] entirely
- [ ] Memorize $d_{ij} = c_{ij} - u_i - v_j$
- [ ] Memorize Hungarian optimality: lines = n

### Hour 2: Simplex
- [ ] Redo [[Solved-Problems#Problem 1|Problem 1 from Solved Problems]] without looking
- [ ] Practice setting up initial tableau

### Hour 3: Transportation
- [ ] Redo [[Solved-Problems#Problem 3|Problem 3]] - all three methods + MODI
- [ ] Practice loop tracing

### Hour 4: Assignment
- [ ] Redo [[Solved-Problems#Problem 4|Problem 4]] - full Hungarian method
- [ ] Practice θ operation on small matrix

---

*Revision Notes | MTC-341 MN:B | Semester V | Last Updated: 2026-06-16*
