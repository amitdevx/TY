---
title: "CS-307 Data Science - Revision Notes"
subject: CS-307-MJ-T
type: revision
semester: V
university: SPPU
tags:
  - data-science
  - revision
  - exam-prep
  - quick-notes
  - CS-307
created: 2026-06-16
updated: 2026-06-16
---

#  CS-307: Data Science - Rapid Revision

> [!tip] How to Use
> Read through all sections 48 hours before exam. Focus on ==highlighted terms== and formulas in boxes.

---

##  Unit 1: Introduction to Data Science

> [!summary] Must Know
> - ==Data Science== = Statistics + Programming + Domain Knowledge
> - **Structured**: Tables/SQL | **Unstructured**: Text/Images | **Semi-structured**: JSON/XML
> - **CRISP-DM**: Business → Data Understanding → Preparation → Modelling → Evaluation → Deployment
> - 60-70% of time spent on **data preprocessing**
> - **NOIR scales**: Nominal < Ordinal < Interval < Ratio

**Key Roles:**
- Data Engineer (pipelines) → Data Analyst (reports) → Data Scientist (models) → ML Engineer (deploy)

**Applications:** Healthcare (diagnosis), Finance (fraud), E-commerce (recommendations), NLP, Computer Vision

---

##  Unit 2: Data Preprocessing

> [!summary] Must Know Formulas

$$\text{Min-Max} = \frac{x - x_{min}}{x_{max} - x_{min}} \rightarrow [0,1]$$

$$\text{Z-Score} = \frac{x - \mu}{\sigma} \rightarrow \mu=0, \sigma=1$$

$$IQR = Q_3 - Q_1 \quad \text{Outlier if: } x < Q_1 - 1.5 \cdot IQR \text{ or } x > Q_3 + 1.5 \cdot IQR$$

$$\text{Z-score Outlier: } |z| > 3$$

**Missing Value Strategies:**
| Situation | Strategy |
|-----------|---------|
| Normal distribution | Mean imputation |
| Skewed / Outliers | Median imputation |
| Categorical data | Mode imputation |
| Complex patterns | KNN imputation |
| <5% missing | Deletion |

**Normalization vs. Standardization:**
- Normalization: Use when bounds are known, no extreme outliers (KNN, Neural Networks)
- Standardization: Use when distribution is unknown or has outliers (SVM, Linear Regression)

**️ ALWAYS**: `fit_transform()` on train, `transform()` only on test!

**Binning:**
- Equal-Width: `width = (max - min) / k`
- Equal-Frequency: Each bin has same number of points (quantile-based)

---

##  Unit 3: Data Visualization

> [!summary] Chart Selection Guide

| Data Type | Chart |
|-----------|-------|
| Single continuous distribution | Histogram |
| Categories comparison | Bar chart |
| Two continuous variables relationship | Scatter plot |
| Time trend | Line chart |
| Proportions | Pie/Donut chart |
| Five-number summary + outliers | Box plot |
| Matrix of correlations | Heatmap |
| Hierarchical clustering | Dendrogram |
| Text frequency | Word cloud |

**Box Plot Components:**
- Whisker Min = Q1 - 1.5×IQR
- Box: Q1 to Q3 (contains 50% of data)
- Line: Median (Q2)
- Whisker Max = Q3 + 1.5×IQR
- Points beyond whiskers = Outliers

**Libraries:**
- `Matplotlib`: Low-level, full control, static
- `Seaborn`: High-level, statistical, attractive defaults
- `Plotly`: Interactive, web-friendly

---

##  Unit 4: Statistics for Data Science

> [!summary] Must Know Formulas

$$\bar{x} = \frac{\sum x_i}{n}, \quad s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}, \quad SE = \frac{\sigma}{\sqrt{n}}$$

**Skewness:**
- Right (+) skew: Mean > Median (long tail right)
- Left (-) skew: Mean < Median (long tail left)
- Symmetric: Mean = Median = Mode

**Normal Distribution:**
- 68% within μ ± 1σ
- 95% within μ ± 2σ
- 99.7% within μ ± 3σ

**Central Limit Theorem**: Sample means → Normal when n ≥ 30, regardless of population distribution.

**Hypothesis Testing Steps:**
1. H₀: No effect; H₁: Effect exists
2. Set α = 0.05
3. Compute test statistic + p-value
4. p < α → Reject H₀ (significant!)

| Test | When to Use |
|------|------------|
| One-sample t-test | Mean vs known value |
| Two-sample t-test | Two group means |
| Paired t-test | Same group, before-after |
| Chi-square | Two categorical variables |
| ANOVA | 3+ group means |

**Correlation:**
- Pearson: Linear, sensitive to outliers → $r = \frac{Cov(X,Y)}{\sigma_X\sigma_Y}$
- Spearman: Rank-based, robust → $r_s = 1 - \frac{6\sum d^2}{n(n^2-1)}$
- Range: [-1, +1] | 0 = no correlation | 1 = perfect positive

**️ Correlation ≠ Causation!**

---

##  Unit 5: Data Mining & Machine Learning

> [!summary] KDD Process
> Selection → Preprocessing → Transformation → Data Mining → Interpretation/Evaluation

**Association Rules:**

$$Support(A \rightarrow B) = \frac{|A \cup B|}{N}$$

$$Confidence(A \rightarrow B) = \frac{Support(A \cup B)}{Support(A)}$$

$$Lift = \frac{Confidence(A\rightarrow B)}{Support(B)} \quad \begin{cases} >1 & \text{positive association} \\ =1 & \text{independent} \\ <1 & \text{negative association} \end{cases}$$

**Apriori Principle**: If an itemset is INFREQUENT, all its SUPERSETS are also infrequent. (Prunes search!)

**K-Means Steps:**
1. Initialize K centroids
2. Assign each point to nearest centroid
3. Recompute centroids (mean of cluster)
4. Repeat 2-3 until convergence

**Choosing K:**
- Elbow method: Plot inertia (WCSS) vs K → look for "elbow"
- Silhouette score: Range [-1, 1], higher = better

**Regression Evaluation:**
- $R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$ (closer to 1 = better)
- RMSE (lower = better, same units as target)

**Regression types:**
- Linear: $\hat{y} = \beta_0 + \beta_1 x$
- Polynomial: Adds $x^2, x^3$ terms
- Logistic: Sigmoid function → binary classification

**Feature Engineering:**
- Creation: Derive new features (BMI, day of week)
- Transformation: Log transform, polynomial
- Selection: Remove redundant/irrelevant features

---

##  All Formulas in One Place

| Formula | Expression |
|---------|-----------|
| Mean | $\bar{x} = \frac{\sum x_i}{n}$ |
| Sample Variance | $s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}$ |
| Z-Score | $z = \frac{x-\mu}{\sigma}$ |
| Standard Error | $SE = \frac{\sigma}{\sqrt{n}}$ |
| Min-Max | $\frac{x - x_{min}}{x_{max} - x_{min}}$ |
| IQR | $Q_3 - Q_1$ |
| IQR Outlier Lower | $Q_1 - 1.5 \cdot IQR$ |
| IQR Outlier Upper | $Q_3 + 1.5 \cdot IQR$ |
| Pearson r | $\frac{Cov(X,Y)}{\sigma_X \sigma_Y}$ |
| Spearman rs | $1 - \frac{6\sum d^2}{n(n^2-1)}$ |
| t-stat (1-sample) | $\frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ |
| Chi-square | $\sum \frac{(O-E)^2}{E}$ |
| Support | $\frac{count(A\cup B)}{N}$ |
| Confidence | $\frac{Support(A\cup B)}{Support(A)}$ |
| Lift | $\frac{Confidence(A\rightarrow B)}{Support(B)}$ |
| R² | $1 - \frac{SS_{res}}{SS_{tot}}$ |
| WCSS (K-Means) | $\sum_j\sum_{x_i\in C_j}\|x_i-\mu_j\|^2$ |

---

##  Last-Hour Checklist

- [ ] Know the difference: Data Science / ML / AI
- [ ] Can write CRISP-DM phases from memory
- [ ] Can write Min-Max, Z-score formulas
- [ ] Can write IQR outlier detection formula
- [ ] Understand hypothesis testing: H₀, H₁, p-value, α
- [ ] Know when to use t-test vs chi-square vs ANOVA
- [ ] Can define Support, Confidence, Lift and write formulas
- [ ] Know Apriori principle
- [ ] Can sketch K-Means elbow curve
- [ ] Know correlation ≠ causation!

---

← [[Important-Questions]] | [[Interview-Prep]] →

#data-science #revision #SPPU #semester-5
