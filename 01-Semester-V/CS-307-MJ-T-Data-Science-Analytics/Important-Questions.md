---
title: "CS-307 Important Questions"
subject: CS-307-MJ-T
type: important-questions
semester: V
university: SPPU
tags:
  - data-science
  - important-questions
  - exam-prep
  - CS-307
created: 2026-06-16
updated: 2026-06-16
---

#  CS-307: Data Science - Important Questions

> [!warning] Exam Focus
> These questions are based on common SPPU exam patterns. Focus especially on 8-mark and 10-mark questions requiring both theory AND diagrams/code.

---

##  Pattern Analysis

| Marks | Type | Strategy |
|-------|------|---------|
| 2 marks | Definition/short | 3-4 sentences, key terms bolded |
| 5 marks | Explain with diagram | 2 para + 1 diagram |
| 8 marks | Detailed explanation | Full coverage with code/formula |
| 10 marks | Application/Case | Theory + practical + example |

---

##  Unit 1: Introduction to Data Science

### 2-Mark Questions
1. Define Data Science. How is it different from Data Mining?
2. What are the different types of data? Give one example of each.
3. Name the phases of the CRISP-DM process.
4. List any four skills required by a data scientist.
5. What is semi-structured data? Give examples.

### 5-Mark Questions
1. Explain the role of a data scientist with required skill set.
2. Describe the data science pipeline with a neat diagram.
3. Differentiate between structured, unstructured, and semi-structured data with examples.
4. Explain CRISP-DM methodology with all its phases.
5. Discuss real-world applications of data science in any three domains.

### 8-Mark Questions
1. **Explain the data science process/pipeline in detail with a block diagram. What percentage of time is typically spent on each phase?**
2. **Compare Data Science, Machine Learning, and Artificial Intelligence. How do they relate?**
3. **Discuss the roles in a data science team. What is a "unicorn" data scientist?**

---

##  Unit 2: Data Preprocessing

### 2-Mark Questions
1. What is data cleaning? Why is it necessary?
2. Define normalization and standardization.
3. What is the IQR method for outlier detection? Give the formula.
4. What is data discretization?
5. Define: Noisy data, Inconsistent data.

### 5-Mark Questions
1. Explain three methods to handle missing values with advantages and disadvantages.
2. Compare Min-Max normalization and Z-score standardization with formulas.
3. Explain the IQR method for outlier detection. How is it better than Z-score?
4. Describe data integration and the challenges involved.
5. Explain equal-width and equal-frequency binning with examples.

### 8-Mark Questions
1. ** Describe in detail different techniques for handling missing values. When would you use deletion vs imputation?**
2. ** Explain data preprocessing pipeline step by step. Implement a complete preprocessing pipeline in Python using Scikit-learn.**
3. **Compare Min-Max Normalization, Z-Score Standardization, and Robust Scaling. Give formulas and use cases.**
4. **Explain the stages of data reduction. What is dimensionality reduction and when is it needed?**

### Expected Formulas to Know:
- $x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}$
- $z = \frac{x - \mu}{\sigma}$
- $IQR = Q_3 - Q_1$; Bounds: $Q_1 - 1.5 \times IQR$ to $Q_3 + 1.5 \times IQR$

---

##  Unit 3: Data Visualization

### 2-Mark Questions
1. When would you use a box plot vs histogram?
2. What information does a correlation heatmap convey?
3. Differentiate between Matplotlib and Seaborn.
4. What is a dendrogram?
5. When would you use a bubble plot over a scatter plot?

### 5-Mark Questions
1. Explain histogram, bar chart, and scatter plot with their use cases.
2. What is a box plot? Explain its components (five-number summary).
3. Compare Matplotlib, Seaborn, and Plotly libraries.
4. What is a heat map? How is it used to show correlation?
5. Explain word cloud and geospatial visualization.

### 8-Mark Questions
1. ** Write Python code to create: (a) Histogram with KDE (b) Box plot comparing groups (c) Correlation heatmap using Seaborn.**
2. **Discuss advanced visualization techniques: Heat maps, Dendrograms, Treemaps, and 3D scatter plots with examples.**
3. **Explain the principles of choosing the right chart for data. Provide guidelines for each data scenario.**

### Python Code to Know:
```python
# Box plot
sns.boxplot(data=df, x='day', y='total_bill', hue='sex')

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)

# Scatter with regression
sns.regplot(data=df, x='total_bill', y='tip')
```

---

##  Unit 4: Statistics for Data Science

### 2-Mark Questions
1. What is the Central Limit Theorem? What is the significance of n≥30?
2. Define Type I and Type II error.
3. What is p-value? What does p < 0.05 mean?
4. Differentiate between Pearson and Spearman correlation.
5. What is standard error?

### 5-Mark Questions
1. Explain measures of central tendency with formulas. When is mean vs median preferred?
2. Explain the normal distribution and the 68-95-99.7 rule with a diagram.
3. Describe hypothesis testing procedure step by step.
4. When do you use t-test vs chi-square test vs ANOVA?
5. What is Pearson's correlation coefficient? Interpret r values.

### 8-Mark Questions
1. ** Explain hypothesis testing in detail: H₀, H₁, p-value, α, Type I error, Type II error. Give a practical example.**
2. ** Describe descriptive statistics: central tendency, dispersion, skewness, kurtosis. Give all formulas.**
3. **Explain probability distributions used in data science: Normal, Binomial, and Poisson. Give formulas and use cases.**
4. **Demonstrate chi-square test using Python on a contingency table. Interpret the result.**

### Expected Formulas:
$$\bar{x} = \frac{\sum x_i}{n}, \quad s^2 = \frac{\sum(x_i-\bar{x})^2}{n-1}, \quad z = \frac{x-\mu}{\sigma}, \quad r = \frac{Cov(X,Y)}{\sigma_X\sigma_Y}$$

---

##  Unit 5: Data Mining & Machine Learning

### 2-Mark Questions
1. What is the KDD process? Name its steps.
2. Differentiate between Support and Confidence in association rules.
3. What is the Apriori principle?
4. What is feature engineering?
5. Define: Overfitting, Underfitting.

### 5-Mark Questions
1. Explain KDD process with a neat block diagram.
2. Explain linear regression and its cost function. What are the assumptions?
3. Explain K-Means clustering algorithm step by step. How do you find optimal K?
4. Explain Apriori algorithm with an example. Define Support, Confidence, Lift.
5. Compare supervised and unsupervised learning with examples.

### 8-Mark Questions
1. ** Explain the Apriori algorithm in detail with a sample transaction database. Calculate Support, Confidence, and Lift for given rules.**
2. ** Implement K-Means clustering in Python. Explain how to choose optimal K using the Elbow method and Silhouette score.**
3. ** Compare Linear Regression, Polynomial Regression, and Logistic Regression with formulas and Python code.**
4. **Explain feature engineering techniques: Feature creation, Feature transformation, Feature selection. Give code examples.**
5. **Compare KNN and Random Forest classification with advantages, disadvantages, and Python implementation.**

### Critical Apriori Example:
```
Transaction Database:
T1: {Milk, Bread, Butter}
T2: {Milk, Bread}
T3: {Milk, Butter}
T4: {Bread, Butter}
T5: {Milk, Bread, Butter}

min_support = 60% (3/5 transactions)

Support({Milk}) = 4/5 = 0.8 
Support({Bread}) = 4/5 = 0.8 
Support({Milk, Bread}) = 3/5 = 0.6 
Confidence(Milk→Bread) = 0.6/0.8 = 0.75
Lift(Milk→Bread) = 0.75/0.8 = 0.9375
```

---

##  Most Important 10-Mark Questions (High Probability)

> [!warning] Prepare these thoroughly - very likely to appear!

1. **Explain the complete data science pipeline from data collection to deployment. Include preprocessing, visualization, modelling, and evaluation.**

2. **Explain K-Means clustering in detail. Include the algorithm steps, objective function, elbow method, and implement it in Python with visualization.**

3. **Describe hypothesis testing with examples: H₀, H₁, p-value, t-test, chi-square test. Perform a hypothesis test in Python and interpret results.**

4. **Explain Apriori association rule mining algorithm. Derive rules from a sample dataset and calculate Support, Confidence, and Lift.**

5. **Compare supervised learning algorithms: Linear Regression, Logistic Regression, KNN, and Random Forest. Include code, evaluation metrics, and when to use each.**

---

##  Quick Formula Sheet

| Concept | Formula |
|---------|---------|
| Min-Max Norm | $\frac{x - x_{min}}{x_{max} - x_{min}}$ |
| Z-Score | $\frac{x - \mu}{\sigma}$ |
| IQR Outlier | $Q_1 - 1.5\cdot IQR$ to $Q_3 + 1.5\cdot IQR$ |
| Variance (sample) | $\frac{\sum(x_i-\bar{x})^2}{n-1}$ |
| Pearson r | $\frac{Cov(X,Y)}{\sigma_X\sigma_Y}$ |
| Spearman rs | $1 - \frac{6\sum d^2}{n(n^2-1)}$ |
| Support | $\frac{|A \cup B|}{N}$ |
| Confidence | $\frac{Support(A\cup B)}{Support(A)}$ |
| Lift | $\frac{Confidence(A\rightarrow B)}{Support(B)}$ |
| R² | $1 - \frac{SS_{res}}{SS_{tot}}$ |

---

← [[Unit-5]] | [[Revision]] →

#data-science #important-questions #exam-prep #SPPU #semester-5
