---
title: "CS-307 Unit 4 - Statistics for Data Science"
subject: CS-307-MJ-T
type: unit-notes
unit: 4
semester: V
university: SPPU
tags:
  - data-science
  - unit-4
  - statistics
  - probability
  - hypothesis-testing
  - correlation
  - CS-307
aliases:
  - DS Unit 4
  - Statistics for Data Science
created: 2026-06-16
updated: 2026-06-16
---

#  Unit 4: Statistics for Data Science

> [!note] Navigation
> ← [[Unit-3]] | [[Overview]] | [[Unit-5]] →

---

##  Learning Objectives

- [ ] Calculate and interpret measures of central tendency and dispersion
- [ ] Apply probability distributions to data problems
- [ ] Use the Central Limit Theorem
- [ ] Conduct hypothesis tests (t-test, chi-square, ANOVA)
- [ ] Calculate and interpret Pearson and Spearman correlation

---

## 4.1 Descriptive Statistics

> [!important] Definition
> ==Descriptive Statistics== summarizes and describes the main features of a dataset numerically.

### 4.1.1 Measures of Central Tendency

**Arithmetic Mean:**
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

**Median:** Middle value when data is sorted.
$$Median = \begin{cases} x_{(n+1)/2} & \text{if } n \text{ is odd} \\ \frac{x_{n/2} + x_{n/2+1}}{2} & \text{if } n \text{ is even} \end{cases}$$

**Mode:** Most frequently occurring value.

| Measure | Best Use | Sensitive to Outliers? |
|---------|----------|----------------------|
| **Mean** | Symmetric, normal distribution | YES - highly sensitive |
| **Median** | Skewed distributions, outliers present | No - robust |
| **Mode** | Categorical data, bimodal distributions | No |

> [!tip] Skewness Rule
> - **Positive/Right Skew**: Mean > Median > Mode (tail on right)
> - **Symmetric**: Mean = Median = Mode
> - **Negative/Left Skew**: Mean < Median < Mode (tail on left)

### 4.1.2 Measures of Dispersion

**Range:**
$$Range = x_{max} - x_{min}$$

**Variance:**
$$\sigma^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n} \quad \text{(population)}$$

$$s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1} \quad \text{(sample, Bessel's correction)}$$

**Standard Deviation:**
$$\sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}}$$

**Interquartile Range (IQR):**
$$IQR = Q_3 - Q_1$$

**Coefficient of Variation (CV):**
$$CV = \frac{\sigma}{\bar{x}} \times 100\%$$

```python
import pandas as pd
import numpy as np
from scipy import stats

data = [14, 18, 11, 13, 6, 8, 2, 18, 15, 12, 10, 9]
arr = np.array(data)

# Central tendency
print(f"Mean:   {np.mean(arr):.2f}")
print(f"Median: {np.median(arr):.2f}")
print(f"Mode:   {stats.mode(arr).mode[0]:.2f}")

# Dispersion
print(f"Range:  {np.ptp(arr):.2f}")
print(f"Variance (pop): {np.var(arr):.2f}")
print(f"Variance (sample): {np.var(arr, ddof=1):.2f}")
print(f"Std Dev:  {np.std(arr, ddof=1):.2f}")
print(f"Q1:     {np.percentile(arr, 25):.2f}")
print(f"Q3:     {np.percentile(arr, 75):.2f}")
print(f"IQR:    {np.percentile(arr, 75) - np.percentile(arr, 25):.2f}")

# Using pandas
s = pd.Series(data)
print(s.describe())  # All at once!
print(f"Skewness: {s.skew():.4f}")
print(f"Kurtosis: {s.kurt():.4f}")
```

### 4.1.3 Measures of Shape

**Skewness:**
$$\text{Skewness} = \frac{\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^3}{\left(\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2\right)^{3/2}}$$

**Kurtosis:**
$$\text{Kurtosis} = \frac{\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^4}{\left(\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2\right)^{2}} - 3$$

| Kurtosis | Distribution | Tail Behavior |
|----------|-------------|---------------|
| < 0 | Platykurtic | Light tails |
| = 0 | Mesokurtic (Normal) | Normal tails |
| > 0 | Leptokurtic | Heavy tails |

---

## 4.2 Probability Distributions

### 4.2.1 Normal (Gaussian) Distribution

> [!important] Normal Distribution
> The most important distribution in statistics. Defined by mean (μ) and standard deviation (σ).

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

**Properties:**
- Bell-shaped, symmetric about mean
- Mean = Median = Mode
- **68-95-99.7 Rule (Empirical Rule)**:
  - 68% of data within μ ± 1σ
  - 95% within μ ± 2σ
  - 99.7% within μ ± 3σ

```python
from scipy.stats import norm
import matplotlib.pyplot as plt

mu, sigma = 170, 10  # Mean height, std dev

x = np.linspace(130, 210, 300)
y = norm.pdf(x, mu, sigma)

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'b-', linewidth=2, label='Normal Distribution')

# Shade regions
plt.fill_between(x, y, where=(x >= mu-sigma) & (x <= mu+sigma), 
                 alpha=0.3, color='blue', label='68% (±1σ)')
plt.fill_between(x, y, where=(x >= mu-2*sigma) & (x <= mu+2*sigma), 
                 alpha=0.2, color='green', label='95% (±2σ)')

plt.xlabel('Height (cm)')
plt.ylabel('Probability Density')
plt.title(f'Normal Distribution: N(μ={mu}, σ={sigma})')
plt.legend()
plt.show()

# Calculate probabilities
print(f"P(X < 180): {norm.cdf(180, mu, sigma):.4f}")
print(f"P(X > 160): {1 - norm.cdf(160, mu, sigma):.4f}")
print(f"P(160 < X < 180): {norm.cdf(180, mu, sigma) - norm.cdf(160, mu, sigma):.4f}")
```

### 4.2.2 Z-Score and Standard Normal Distribution

$$z = \frac{x - \mu}{\sigma}$$

The **Standard Normal Distribution** N(0, 1) is the normal distribution with μ=0, σ=1.

```python
# Converting to Z-score
x_value = 185  # height
z = (x_value - mu) / sigma
print(f"Z-score: {z:.2f}")  # How many std devs from mean?

# P-value from Z-score
p_value = 1 - norm.cdf(z)
print(f"P(X > {x_value}): {p_value:.4f}")

# Inverse: Find x for given probability
percentile_95 = norm.ppf(0.95, mu, sigma)
print(f"95th percentile: {percentile_95:.2f} cm")
```

### 4.2.3 Binomial Distribution

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**Mean**: $\mu = np$  
**Variance**: $\sigma^2 = np(1-p)$

```python
from scipy.stats import binom

n, p = 20, 0.3  # 20 trials, 30% success probability
k = 5

print(f"P(X = {k}): {binom.pmf(k, n, p):.4f}")
print(f"P(X <= {k}): {binom.cdf(k, n, p):.4f}")
print(f"Mean: {n*p:.2f}, Variance: {n*p*(1-p):.2f}")
```

### 4.2.4 Central Limit Theorem (CLT)

> [!important] Central Limit Theorem
> If you take sufficiently large random samples (n ≥ 30) from **any** distribution, the **sampling distribution of the sample mean** approaches a **normal distribution**.

$$\bar{X} \sim N\left(\mu, \frac{\sigma}{\sqrt{n}}\right)$$

- **Standard Error (SE)**: $SE = \frac{\sigma}{\sqrt{n}}$

```python
# Demonstrate CLT
population = np.random.exponential(scale=2, size=10000)  # Not normal!

sample_means = []
for _ in range(1000):
    sample = np.random.choice(population, size=50)
    sample_means.append(np.mean(sample))

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(population, bins=50, color='red', alpha=0.7, edgecolor='black')
axes[0].set_title('Original (Exponential) Distribution')

axes[1].hist(sample_means, bins=40, color='blue', alpha=0.7, edgecolor='black')
axes[1].set_title('Sampling Distribution of Means (n=50)\n→ Approaches Normal!')
plt.tight_layout()
plt.show()
```

---

## 4.3 Hypothesis Testing

> [!important] Framework
> 1. State **H₀** (Null Hypothesis) and **H₁** (Alternative Hypothesis)
> 2. Choose significance level **α** (usually 0.05)
> 3. Compute **test statistic** and **p-value**
> 4. If p-value < α → **Reject H₀**; else **Fail to reject H₀**

**Decision Rule:**

| p-value | α = 0.05 | Conclusion |
|---------|---------|------------|
| p < 0.05 | < α | Reject H₀ - **Statistically Significant** |
| p ≥ 0.05 | ≥ α | Fail to reject H₀ - Not significant |

> [!warning] Error Types
> - **Type I Error (α)**: Rejecting H₀ when it's true (False Positive) - "False alarm"
> - **Type II Error (β)**: Failing to reject H₀ when it's false (False Negative) - "Missed"
> - **Power** = 1 - β = Probability of correctly rejecting false H₀

### 4.3.1 One-Sample t-Test

**Test if sample mean equals a known value.**

$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$$

**Degrees of Freedom**: df = n - 1

```python
from scipy import stats

# Example: Is average height = 170 cm?
heights = [172, 175, 168, 180, 165, 173, 178, 169, 171, 174]

t_stat, p_value = stats.ttest_1samp(heights, popmean=170)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject H₀: Average height ≠ 170 cm")
else:
    print("Fail to Reject H₀: Average height could be 170 cm")
```

### 4.3.2 Two-Sample t-Test

**Test if two group means are significantly different.**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

```python
# Is there a significant difference in tip between male and female?
male_tips = df[df['sex'] == 'Male']['tip'].values
female_tips = df[df['sex'] == 'Female']['tip'].values

t_stat, p_value = stats.ttest_ind(male_tips, female_tips, equal_var=False)  # Welch's t-test
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# Paired t-test (before/after)
before = [72, 68, 75, 80, 65, 70, 73, 78]
after  = [68, 65, 70, 74, 60, 68, 70, 72]
t_stat, p_value = stats.ttest_rel(before, after)
print(f"Paired t-test p-value: {p_value:.4f}")
```

### 4.3.3 Chi-Square Test

**Test association between two categorical variables.**

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

where O = Observed frequency, E = Expected frequency under H₀ (independence)

```python
# Is there an association between gender and smoking?
ct = pd.crosstab(df['sex'], df['smoker'])
print("Contingency Table:\n", ct)

chi2, p_value, dof, expected = stats.chi2_contingency(ct)
print(f"\nChi-square statistic: {chi2:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Degrees of freedom: {dof}")

if p_value < 0.05:
    print("Reject H₀: There IS a significant association between gender and smoking")
else:
    print("Fail to Reject H₀: No significant association")
```

### 4.3.4 ANOVA (Analysis of Variance)

**Test if means of 3+ groups are significantly different.**

$$F = \frac{\text{Variance Between Groups}}{\text{Variance Within Groups}} = \frac{MS_{between}}{MS_{within}}$$

```python
# Is there a significant difference in tip across days?
thur = df[df['day'] == 'Thur']['tip']
fri  = df[df['day'] == 'Fri']['tip']
sat  = df[df['day'] == 'Sat']['tip']
sun  = df[df['day'] == 'Sun']['tip']

f_stat, p_value = stats.f_oneway(thur, fri, sat, sun)
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject H₀: At least one day has different mean tip")
```

---

## 4.4 Correlation and Covariance

### Covariance

$$\text{Cov}(X, Y) = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{n-1}$$

- Positive: X and Y move together
- Negative: X and Y move opposite
- 0: No linear relationship (but may still be related non-linearly)

### Pearson Correlation Coefficient

$$r = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \cdot \sum(y_i - \bar{y})^2}}$$

**Range**: $-1 \leq r \leq +1$

| r value | Interpretation |
|---------|---------------|
| +1 | Perfect positive correlation |
| +0.7 to +0.9 | Strong positive |
| +0.4 to +0.6 | Moderate positive |
| 0 | No correlation |
| -0.4 to -0.6 | Moderate negative |
| -1 | Perfect negative correlation |

### Spearman Rank Correlation

$$r_s = 1 - \frac{6 \sum d_i^2}{n(n^2-1)}$$

where $d_i$ = difference in ranks for pair $i$.

> [!tip] Pearson vs Spearman
> - **Pearson**: Measures linear relationships; sensitive to outliers; requires normality
> - **Spearman**: Measures monotonic relationships; rank-based; robust to outliers; non-parametric

```python
# Pearson correlation
corr_pearson, p_val = stats.pearsonr(df['total_bill'], df['tip'])
print(f"Pearson r: {corr_pearson:.4f}, p-value: {p_val:.4f}")

# Spearman correlation
corr_spearman, p_val = stats.spearmanr(df['total_bill'], df['tip'])
print(f"Spearman r: {corr_spearman:.4f}, p-value: {p_val:.4f}")

# Correlation matrix
corr_matrix = df[['total_bill', 'tip', 'size']].corr(method='pearson')
print("\nCorrelation Matrix:")
print(corr_matrix)

# Heatmap
import seaborn as sns
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Pearson Correlation Matrix')
plt.show()
```

> [!warning] Correlation ≠ Causation!
> **Spurious correlations** example: Ice cream sales and drowning deaths are positively correlated - because both increase in summer (confounding variable). Correlation does NOT prove causation!

---

##  Interview Questions - Unit 4

> [!question] Q1: What is the Central Limit Theorem and why is it important?
> **Answer**: CLT states that the sampling distribution of the sample mean approaches a normal distribution as sample size increases (n≥30), regardless of the underlying population distribution. Importance: Allows us to use z-tests and t-tests even when we don't know the population distribution. Foundation of statistical inference.

> [!question] Q2: What is the difference between Type I and Type II errors?
> **Answer**: 
> - **Type I (α)**: Rejecting H₀ when it's actually true - "False Positive". Probability = α (significance level).
> - **Type II (β)**: Failing to reject H₀ when it's actually false - "False Negative". 
> - **Power** = 1 - β = probability of correctly detecting a real effect.
> Trade-off: Reducing α increases β and vice versa.

> [!question] Q3: When do you use t-test vs. chi-square test?
> **Answer**: 
> - **t-test**: When comparing means of continuous numerical data between groups (1 or 2 samples)
> - **Chi-square test**: When testing the association between two categorical variables
> - **ANOVA**: When comparing means across 3+ groups

> [!question] Q4: What is the difference between Pearson and Spearman correlation?
> **Answer**: Pearson measures LINEAR correlation between continuous variables. Requires normality, sensitive to outliers. Spearman is rank-based, measures MONOTONIC relationships (not just linear), robust to outliers, non-parametric. Use Spearman when: data has outliers, data is ordinal, or relationship is monotonic but not linear.

> [!question] Q5: What is p-value? What does p < 0.05 mean?
> **Answer**: The p-value is the probability of observing results at least as extreme as those observed, assuming H₀ is true. p < 0.05 means: if H₀ were true, there's less than 5% chance of seeing results this extreme by random chance - so we reject H₀ and say the result is "statistically significant."

---

##  Key Formulas Quick Reference

| Formula | Expression |
|---------|-----------|
| Mean | $\bar{x} = \frac{\sum x_i}{n}$ |
| Variance (sample) | $s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$ |
| Z-score | $z = \frac{x - \mu}{\sigma}$ |
| Standard Error | $SE = \frac{\sigma}{\sqrt{n}}$ |
| One-sample t | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ |
| Chi-square | $\chi^2 = \sum\frac{(O-E)^2}{E}$ |
| Pearson r | $r = \frac{Cov(X,Y)}{\sigma_X\sigma_Y}$ |
| Spearman r | $r_s = 1 - \frac{6\sum d^2}{n(n^2-1)}$ |

---

##  Revision Summary

> [!summary] Unit 4 Key Points
> 1. **Central tendency**: Mean (normal) > Median (skewed) > Mode (categorical)
> 2. **Skew**: Right skew → Mean > Median; Left skew → Mean < Median
> 3. **68-95-99.7 Rule**: Normal distribution within 1, 2, 3 std deviations
> 4. **CLT**: Sample means → Normal distribution when n ≥ 30
> 5. **Hypothesis testing**: H₀, H₁, α, p-value. Reject if p < α (0.05)
> 6. **Type I (α)**: False positive | **Type II (β)**: False negative
> 7. **Pearson**: Linear, sensitive to outliers | **Spearman**: Rank-based, robust
> 8. **Correlation ≠ Causation** (always remember!)

---

← [[Unit-3]] | [[Unit-5]] →

#data-science #unit-4 #statistics #SPPU #semester-5
