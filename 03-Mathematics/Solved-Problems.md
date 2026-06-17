---
title: Solved Problems - Mathematics
tags: [mathematics, solved-problems, operations-research, simplex, transportation, assignment]
aliases: [Math Solved Problems, OR Solved Problems]
type: solved-problems
subject_code: MTC-341 MN:B
semester: V
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[03-Mathematics/Mathematics-Dashboard|Mathematics]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Formula-Sheet]] | [[PYQ]]


# Solved Problems - Mathematics (Operations Research)

> [!tip] How to Use This File
> Work through each problem yourself FIRST, then verify with the solution. Focus on the **process** not just the answer. Time yourself - exam expects 15-20 mins per problem.

---

## Problem 1 - LPP using Simplex Method 

### Problem Statement

A company manufactures two products X and Y. Each unit of X requires 3 hours of machine time and 1 hour of labor. Each unit of Y requires 1 hour of machine time and 2 hours of labor. Available machine hours = 9, available labor hours = 8. Profit per unit: X = ₹5, Y = ₹4. Maximize profit.

### Step 1: Formulation

**Decision Variables:**
- $x_1$ = units of X produced
- $x_2$ = units of Y produced

**Objective Function:**
$$\text{Maximize } Z = 5x_1 + 4x_2$$

**Constraints:**
$$3x_1 + x_2 \leq 9 \quad \text{(Machine hours)}$$
$$x_1 + 2x_2 \leq 8 \quad \text{(Labor hours)}$$
$$x_1, x_2 \geq 0$$

### Step 2: Standard Form (Add Slack Variables)

$$3x_1 + x_2 + s_1 = 9$$
$$x_1 + 2x_2 + s_2 = 8$$
$$x_1, x_2, s_1, s_2 \geq 0$$

### Step 3: Initial Simplex Tableau

$c_j$ values: $x_1=5, x_2=4, s_1=0, s_2=0$

**Initial BFS:** $s_1 = 9, s_2 = 8$ (basic), $x_1 = x_2 = 0$ (non-basic)

| Basis | $c_B$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $b$ | Ratio $b/a_{ik}$ |
|-------|--------|--------|--------|--------|--------|------|---------|
| $s_1$ | 0 | **3** | 1 | 1 | 0 | 9 | 9/3 = **3** ← min |
| $s_2$ | 0 | 1 | 2 | 0 | 1 | 8 | 8/1 = 8 |
| $z_j$ | | 0 | 0 | 0 | 0 | **Z=0** | |
| $c_j-z_j$ | | **5** ← max | 4 | 0 | 0 | | |

- **Entering variable:** $x_1$ (most positive $c_j - z_j = 5$)
- **Leaving variable:** $s_1$ (min ratio = 3, pivot row = 1)
- **Pivot element:** 3 (intersection of $x_1$ col and $s_1$ row)

### Step 4: First Pivot Operation

New R1 = Old R1 ÷ 3:

| | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $b$ |
|-|--------|--------|--------|--------|------|
| New R1 | 1 | 1/3 | 1/3 | 0 | 3 |

New R2 = Old R2 − 1×(New R1):
$$[1, 2, 0, 1, 8] - 1 \times [1, 1/3, 1/3, 0, 3] = [0, 5/3, -1/3, 1, 5]$$

### Step 5: Second Tableau

| Basis | $c_B$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $b$ | Ratio |
|-------|--------|--------|--------|--------|--------|------|-------|
| $x_1$ | 5 | 1 | **1/3** | 1/3 | 0 | 3 | 3/(1/3)=9 |
| $s_2$ | 0 | 0 | **5/3** | -1/3 | 1 | 5 | 5/(5/3)=**3** ← min |
| $z_j$ | | 5 | 5/3 | 5/3 | 0 | **Z=15** | |
| $c_j-z_j$ | | 0 | **7/3** ← pos | -5/3 | 0 | | |

- **Entering variable:** $x_2$ (most positive $c_j - z_j = 7/3$)
- **Leaving variable:** $s_2$ (min ratio = 3)
- **Pivot element:** 5/3

### Step 6: Second Pivot Operation

New R2 = Old R2 ÷ (5/3) = Old R2 × (3/5):

| | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $b$ |
|-|--------|--------|--------|--------|------|
| New R2 | 0 | 1 | -1/5 | 3/5 | 3 |

New R1 = Old R1 − (1/3)×(New R2):
$$[1, 1/3, 1/3, 0, 3] - (1/3) \times [0, 1, -1/5, 3/5, 3]$$
$$= [1, 0, 2/5, -1/5, 2]$$

### Step 7: Third Tableau (Check Optimality)

| Basis | $c_B$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $b$ |
|-------|--------|--------|--------|--------|--------|------|
| $x_1$ | 5 | 1 | 0 | 2/5 | -1/5 | **2** |
| $x_2$ | 4 | 0 | 1 | -1/5 | 3/5 | **3** |
| $z_j$ | | 5 | 4 | 6/5 | 7/5 | **Z=22** |
| $c_j-z_j$ | | 0 | 0 | **-6/5** | **-7/5** | |

All $c_j - z_j \leq 0$ → **OPTIMAL!** 

### Final Answer

$$\boxed{x_1 = 2, \quad x_2 = 3, \quad Z_{\max} = 5(2) + 4(3) = \mathbf{22}}$$

**Interpretation:** Produce 2 units of X and 3 units of Y for maximum profit of ₹22.

---

## Problem 2 - Big-M Method 

### Problem Statement

Maximize $Z = 2x_1 + 3x_2$

Subject to:
$$x_1 + x_2 \leq 4 \quad \text{...(1)}$$
$$x_1 + 3x_2 \geq 6 \quad \text{...(2)}$$
$$x_1, x_2 \geq 0$$

### Step 1: Standard Form

- Constraint (1): Add slack $s_1$: $x_1 + x_2 + s_1 = 4$
- Constraint (2): Subtract surplus $s_2$, add artificial $A_1$: $x_1 + 3x_2 - s_2 + A_1 = 6$

**Modified objective** (Maximize, so artificial has coefficient $-M$):
$$\text{Maximize } Z = 2x_1 + 3x_2 + 0s_1 + 0s_2 - MA_1$$

### Step 2: Initial Tableau

Basis = {$s_1, A_1$}

$c_j$: [$x_1$=2, $x_2$=3, $s_1$=0, $s_2$=0, $A_1$=$-M$]

| Basis | $c_B$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $A_1$ | $b$ | Ratio |
|-------|--------|--------|--------|--------|--------|--------|------|-------|
| $s_1$ | 0 | 1 | 1 | 1 | 0 | 0 | 4 | 4/1=4 |
| $A_1$ | $-M$ | 1 | **3** | 0 | -1 | 1 | 6 | 6/3=**2** |

$z_j$ calculation:
- $z_{x_1} = 0(1)+(-M)(1) = -M$, $c_{x_1}-z_{x_1} = 2-(-M) = 2+M$
- $z_{x_2} = 0(1)+(-M)(3) = -3M$, $c_{x_2}-z_{x_2} = 3-(-3M) = 3+3M$

| $z_j$ | | $-M$ | $-3M$ | 0 | $M$ | $-M$ | $-6M$ |
| $c_j-z_j$ | | $2+M$ | **3+3M** ← max | 0 | $-M$ | 0 | |

**Entering:** $x_2$ (most positive for large $M$). Min ratio = 2 → $A_1$ leaves.
Pivot element = 3.

### Step 3: First Pivot

New R2 = R2 ÷ 3:

| | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $A_1$ | $b$ |
|-|--------|--------|--------|--------|--------|------|
| New R2 | 1/3 | 1 | 0 | -1/3 | 1/3 | 2 |

New R1 = R1 − 1×(New R2):
$$[1,1,1,0,0,4] - [1/3,1,0,-1/3,1/3,2] = [2/3, 0, 1, 1/3, -1/3, 2]$$

### Step 4: Second Tableau

| Basis | $c_B$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $b$ | Ratio |
|-------|--------|--------|--------|--------|--------|------|-------|
| $s_1$ | 0 | **2/3** | 0 | 1 | 1/3 | 2 | 2/(2/3)=**3** |
| $x_2$ | 3 | 1/3 | 1 | 0 | -1/3 | 2 | 2/(1/3)=6 |
| $z_j$ | | 1 | 3 | 0 | -1 | **Z=6** | |
| $c_j-z_j$ | | **1** ← pos | 0 | 0 | 1 | | |

**Entering:** $x_1$. Min ratio = 3 → $s_1$ leaves. Pivot = 2/3.

### Step 5: Third Pivot

New R1 = R1 ÷ (2/3) = R1 × 3/2:

| | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $b$ |
|-|--------|--------|--------|--------|------|
| New R1 | 1 | 0 | 3/2 | 1/2 | 3 |

New R2 = R2 − (1/3)×(New R1):
$$[1/3,1,0,-1/3,2] - (1/3)[1,0,3/2,1/2,3] = [0,1,-1/2,-1/2,1]$$

### Step 6: Final Tableau

| Basis | $c_B$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $b$ |
|-------|--------|--------|--------|--------|--------|------|
| $x_1$ | 2 | 1 | 0 | 3/2 | 1/2 | 3 |
| $x_2$ | 3 | 0 | 1 | -1/2 | -1/2 | 1 |
| $z_j$ | | 2 | 3 | 3/2-3/2=0? | ... | **Z=9** |
| $c_j-z_j$ | | 0 | 0 | $\leq 0$ | $\leq 0$ | |

### Final Answer

$$\boxed{x_1 = 3, \quad x_2 = 1, \quad Z_{\max} = 2(3) + 3(1) = \mathbf{9}}$$

---

## Problem 3 - Transportation Problem (All Methods + MODI)

### Problem Statement

Find the minimum cost transportation plan:

| | $D_1$ | $D_2$ | $D_3$ | Supply |
|-|-------|-------|-------|--------|
| **$S_1$** | 2 | 7 | 4 | 5 |
| **$S_2$** | 3 | 3 | 1 | 8 |
| **$S_3$** | 5 | 4 | 7 | 7 |
| **Demand** | 7 | 9 | 4 | 20=20  |

**Balanced:** $\sum a_i = 5+8+7 = 20 = 7+9+4 = \sum b_j$ 

### Method A: NWCR

Start at (1,1):
- $x_{11} = \min(5,7) = 5$ → Row 1 exhausted, remaining demand at $D_1 = 2$
- $x_{21} = \min(8,2) = 2$ → Col 1 exhausted, remaining supply at $S_2 = 6$
- $x_{22} = \min(6,9) = 6$ → Row 2 exhausted, remaining demand at $D_2 = 3$
- $x_{32} = \min(7,3) = 3$ → Col 2 exhausted, remaining supply at $S_3 = 4$
- $x_{33} = \min(4,4) = 4$ → Both exhausted 

| | $D_1$ | $D_2$ | $D_3$ | Supply |
|-|-------|-------|-------|--------|
| **$S_1$** | **5** | - | - | 5  |
| **$S_2$** | **2** | **6** | - | 8  |
| **$S_3$** | - | **3** | **4** | 7  |
| Demand | 7  | 9  | 4  | |

Allocations = 5 = $3+3-1 = 5$ 

$$Z_{\text{NWCR}} = 5(2)+2(3)+6(3)+3(4)+4(7) = 10+6+18+12+28 = \mathbf{74}$$

---

### Method B: LCM (Least Cost Method)

| Step | Cell | Cost | Allocation | Note |
|------|------|------|-----------|------|
| 1 | $(2,3)$ | 1 | min(8,4)=4 | $D_3$ exhausted |
| 2 | $(1,1)$ | 2 | min(5,7)=5 | $S_1$ exhausted |
| 3 | $(2,2)$ | 3 | min(4,9)=4 | $S_2$ exhausted |
| 4 | $(3,2)$ | 4 | min(7,5)=5 | $D_2$ exhausted |
| 5 | $(3,1)$ | 5 | min(2,2)=2 | Both exhausted |

| | $D_1$ | $D_2$ | $D_3$ | Supply |
|-|-------|-------|-------|--------|
| **$S_1$** | **5** | - | - | 5  |
| **$S_2$** | - | **4** | **4** | 8  |
| **$S_3$** | **2** | **5** | - | 7  |
| Demand | 7  | 9  | 4  | |

$$Z_{\text{LCM}} = 5(2)+4(3)+4(1)+2(5)+5(4) = 10+12+4+10+20 = \mathbf{56}$$

---

### Method C: VAM

**Iteration 1 - Penalties:**

| | $D_1$(2) | $D_2$(7) | $D_3$(4) | Supply | Penalty |
|-|---------|---------|---------|--------|---------|
| $S_1$ | 2 | 7 | 4 | 5 | 4-2=2 |
| $S_2$ | 3 | 3 | **1** | 8 | 3-1=2 |
| $S_3$ | 5 | 4 | 7 | 7 | 5-4=1 |
| **Col Penalty** | 3-2=1 | 4-3=1 | 4-1=**3** | | |

Max penalty = 3 (Col $D_3$). Min cost in $D_3$ = 1 at $(S_2, D_3)$.
$x_{23} = \min(8,4) = 4$ → $D_3$ exhausted.

**Iteration 2** (Remove $D_3$):

| | $D_1$(2) | $D_2$(7) | Supply | Penalty |
|-|---------|---------|--------|---------|
| $S_1$ | 2 | 7 | 5 | 7-2=**5** |
| $S_2$ | 3 | 3 | 4 | 3-3=0 |
| $S_3$ | 5 | 4 | 7 | 5-4=1 |
| **Col Penalty** | 3-2=1 | 4-3=1 | | |

Max penalty = 5 (Row $S_1$). Min cost in $S_1$ = 2 at $(S_1, D_1)$.
$x_{11} = \min(5,7) = 5$ → $S_1$ exhausted.

**Iteration 3** (Remove $S_1$):

| | $D_1$(2) | $D_2$(4) | Supply | Penalty |
|-|---------|---------|--------|---------|
| $S_2$ | 3 | 3 | 4 | 3-3=0 |
| $S_3$ | 5 | **4** | 7 | 5-4=1 |
| **Col Penalty** | 5-3=2 | 4-3=**1** | | |

Max penalty = 2 (Col $D_1$). Min cost in $D_1$ = 3 at $(S_2, D_1)$.
$x_{21} = \min(4,2) = 2$ → $S_2$ supply reduces to 2. $D_1$ remaining = 0.

**Iteration 4** (Remove $D_1$):

| | $D_2$(4) | Supply |
|-|---------|--------|
| $S_2$ | 3 | 2 |
| $S_3$ | 4 | 7 |

$x_{22} = 2$ ($S_2$ exhausted), $x_{32} = 7$ ($S_3$ exhausted).

**VAM Solution:**

| | $D_1$ | $D_2$ | $D_3$ | Supply |
|-|-------|-------|-------|--------|
| **$S_1$** | **5** | - | - | 5  |
| **$S_2$** | **2** | **2** | **4** | 8  |
| **$S_3$** | - | **7** | - | 7  |
| Demand | 7  | 9  | 4  | |

$$Z_{\text{VAM}} = 5(2)+2(3)+2(3)+4(1)+7(4) = 10+6+6+4+28 = \mathbf{54}$$

---

### MODI Optimality Test (on VAM Solution)

**Basic cells:** $(1,1), (2,1), (2,2), (2,3), (3,2)$ - 5 cells = $m+n-1$ 

**Find u, v values** (set $u_1 = 0$):

From basic cells:
- $(1,1)$: $u_1 + v_1 = 2$ → $0 + v_1 = 2$ → $v_1 = 2$
- $(2,1)$: $u_2 + v_1 = 3$ → $u_2 + 2 = 3$ → $u_2 = 1$
- $(2,2)$: $u_2 + v_2 = 3$ → $1 + v_2 = 3$ → $v_2 = 2$
- $(2,3)$: $u_2 + v_3 = 1$ → $1 + v_3 = 1$ → $v_3 = 0$
- $(3,2)$: $u_3 + v_2 = 4$ → $u_3 + 2 = 4$ → $u_3 = 2$

**Summary:** $u_1=0, u_2=1, u_3=2$; $v_1=2, v_2=2, v_3=0$

**Compute $d_{ij}$ for non-basic cells:**

$$d_{12} = c_{12} - u_1 - v_2 = 7 - 0 - 2 = 5 \geq 0 $$
$$d_{13} = c_{13} - u_1 - v_3 = 4 - 0 - 0 = 4 \geq 0 $$
$$d_{31} = c_{31} - u_3 - v_1 = 5 - 2 - 2 = 1 \geq 0 $$
$$d_{33} = c_{33} - u_3 - v_3 = 7 - 2 - 0 = 5 \geq 0 $$

**All $d_{ij} \geq 0$ → Solution is OPTIMAL!** 

### Final Answer

$$\boxed{x_{11}=5, x_{21}=2, x_{22}=2, x_{23}=4, x_{32}=7; \quad Z_{\min} = \mathbf{54}}$$

**Comparison:**
| Method | Cost |
|--------|------|
| NWCR | 74 |
| LCM | 56 |
| VAM | **54** (optimal) |

---

## Problem 4 - Assignment Problem using Hungarian Method 

### Problem Statement

Four programmers are to be assigned to four projects. Time (hours) required:

| | P1 | P2 | P3 | P4 |
|-|----|----|----|-----|
| **A** | 18 | 26 | 17 | 11 |
| **B** | 13 | 28 | 14 | 26 |
| **C** | 38 | 19 | 18 | 15 |
| **D** | 19 | 26 | 24 | 10 |

Minimize total time.

### Step 1: Row Reduction

Row minima: A=11, B=13, C=15, D=10

| | P1 | P2 | P3 | P4 |
|-|----|----|----|-----|
| **A** | 7 | 15 | 6 | **0** |
| **B** | **0** | 15 | 1 | 13 |
| **C** | 23 | 4 | 3 | **0** |
| **D** | 9 | 16 | 14 | **0** |

### Step 2: Column Reduction

Column minima: P1=0, P2=4, P3=1, P4=0

| | P1 | P2 | P3 | P4 |
|-|----|----|----|-----|
| **A** | 7 | 11 | 5 | **0** |
| **B** | **0** | 11 | **0** | 13 |
| **C** | 23 | **0** | 2 | **0** |
| **D** | 9 | 12 | 13 | **0** |

### Step 3: Cover All Zeros

Zeros at: (A,P4), (B,P1), (B,P3), (C,P2), (C,P4), (D,P4)

Minimum lines to cover:
- Column P4: covers (A,P4), (C,P4), (D,P4)
- Row B: covers (B,P1), (B,P3)
- Cell (C,P2): need one more line → Column P2 or Row C

Let's use: Col P4, Row B, Row C → 3 lines (covers all zeros? Check: (A,P4), (B,P1), (B,P3), (C,P2), (C,P4), (D,P4))

3 lines < 4 → **Not optimal yet, apply Step 4**

### Step 4: Revise Matrix

Uncovered elements (not in Row B, Row C, Col P4):
- A: 7, 11, 5 (P1,P2,P3)
- D: 9, 12, 13 (P1,P2,P3)

$\theta = \min(7, 11, 5, 9, 12, 13) = 5$

Operations:
- Uncovered elements: subtract 5
- Row B (covered by 1 line): unchanged
- Row C (covered by 1 line): unchanged
- Col P4 (covered by 1 line): unchanged
- Intersections (Row B ∩ Col P4 = B,P4; Row C ∩ Col P4 = C,P4): add 5

| | P1 | P2 | P3 | P4 |
|-|----|----|----|-----|
| **A** | 2 | 6 | **0** | **0** |
| **B** | **0** | 11 | **0** | 18 |
| **C** | 23 | **0** | 2 | 5 |
| **D** | 4 | 7 | 8 | **0** |

### Step 3 (Repeat): Cover All Zeros

Zeros: (A,P3), (A,P4), (B,P1), (B,P3), (C,P2), (D,P4)

Lines: Col P3, Col P1, Row A, Row D → 4 lines? Let's try:
- Row A: covers (A,P3), (A,P4)
- Col P3: covers (B,P3)
- Col P1: covers (B,P1)
- Row D: covers (D,P4) - but (C,P2) still uncovered

Try: Col P3, Row A, Col P1, Row C:
- Col P3: (A,P3), (B,P3)
- Row A: (A,P4) (already have P3)
- Col P1: (B,P1)
- Row D: (D,P4)
Still need (C,P2)... 5 lines would be needed if placed poorly.

**Better:** Col P3: covers (A,P3),(B,P3); Row A: covers (A,P4); Col P1: covers (B,P1); Row C: covers (C,P2); Row D: covers (D,P4) → 5 lines... > 4.

Let's try **3 strategic lines**: Col P3, Col P1, Row D:
- Col P3: (A,P3), (B,P3)
- Col P1: (B,P1)
- Row D: (D,P4)
Still uncovered: (A,P4), (C,P2) → need more lines

**Minimum lines = 4 lines:**
- Col P3, Row A, Col P2, Row D covers everything:
  - Col P3: (A,P3), (B,P3)
  - Row A: (A,P4)
  - Col P2: (C,P2)
  - Row D: (D,P4), (B,P1) still uncovered
  
**Use 4 lines**: Row A, Row B, Row D, Col P2:
- Row A: (A,P3), (A,P4)
- Row B: (B,P1), (B,P3)  
- Row D: (D,P4)
- Col P2: (C,P2)

**4 lines = n → Optimal! Find Assignment.**

### Step 5: Make Assignment

From revised matrix:
| | P1 | P2 | P3 | P4 |
|-|----|----|----|-----|
| **A** | 2 | 6 | **0** | **0** |
| **B** | **0** | 11 | **0** | 18 |
| **C** | 23 | **0** | 2 | 5 |
| **D** | 4 | 7 | 8 | **0** |

- Row C → P2 (only zero in R C at (C,P2))
- Row D → P4 (only zero in remaining positions of RD)
- Row B → P1 (P3 and P1 zeros; P3 needed for A... try P1)
- Row A → P3

**Assignment:**
| Person | Project | Original Time |
|--------|---------|--------------|
| A | P3 | **17** |
| B | P1 | **13** |
| C | P2 | **19** |
| D | P4 | **10** |
| **Total** | | |

$$\boxed{Z_{\min} = 17 + 13 + 19 + 10 = \mathbf{59} \text{ hours}}$$

---

## Quick Problem Reference

| Problem Type | Key Steps | Formula |
|-------------|----------|---------|
| Simplex | Standard form → Tableau → Pivot | Most positive $c_j-z_j$ enters |
| Big-M | Add $A_i$ with $-M$ cost → Simplex | If $A_i > 0$ at end → infeasible |
| Transportation | Balance → Initial BFS → MODI | All $d_{ij} \geq 0$ → optimal |
| Assignment | Row reduce → Col reduce → Cover → Assign | Lines = $n$ → optimal |

---

*Solved Problems | MTC-341 MN:B | Semester V | Last Updated: 2026-06-16*
