---
title: "CS-307 Data Science - Expected PYQ"
subject: CS-307
paper: Data Science
semester: V
tags:
  - pyq
  - data-science
  - machine-learning
  - visualization
  - preprocessing
  - semester-v
  - exam
aliases:
  - Data Science PYQ
  - CS307 Questions
created: 2026-06-16
type: pyq
---

#  CS-307 Data Science - Expected PYQ

> [!important] Exam Strategy
> Data Science paper balances theory and practical. Focus on preprocessing techniques, visualization types, ML algorithms (Linear Regression, KNN, K-Means), and evaluation metrics. Expect short Python code snippets too.

---

## ️ Unit-wise Distribution

| Unit | Topic | Weightage |
|------|-------|-----------|
| I | Introduction & Data Types | 15% |
| II | Data Preprocessing | 25% |
| III | Data Visualization | 20% |
| IV | Machine Learning Algorithms | 30% |
| V | Evaluation & Model Selection | 10% |

---

## ️ Section A - Short Answer Questions (2 Marks)

1. **Define Data Science. List its key components.**
2. **What is the difference between structured and unstructured data?**
3. **What is a missing value? How can it be handled?**
4. **Define outlier. What methods detect outliers?**
5. **What is normalization? How does it differ from standardization?**
6. **What is one-hot encoding? When is it used?**
7. **Define feature selection vs. feature extraction.**
8. **What is a histogram? When do you use it?**
9. **What is a scatter plot used for in data visualization?**
10. **What is overfitting? How is it prevented?**
11. **Define bias and variance in ML.**
12. **What is the difference between supervised and unsupervised learning?**
13. **What is K in K-Nearest Neighbors? How is K chosen?**
14. **Define inertia/WCSS in K-Means clustering.**
15. **What is the elbow method?**
16. **What is a confusion matrix? Define TP, TN, FP, FN.**
17. **Define precision, recall, and F1-score.**
18. **What is cross-validation? Why is it used?**
19. **What is the difference between regression and classification?**
20. **Define entropy in decision trees.**

---

##  Section B - Long Answer Questions (5–7 Marks)

---

### Q1. Data Preprocessing Techniques ( HIGH PROBABILITY)

**Explain the following preprocessing steps:**

**a) Handling Missing Values:**
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})

# Method 1: Drop rows/columns
df.dropna(inplace=True)

# Method 2: Fill with mean/median/mode
df['A'].fillna(df['A'].mean(), inplace=True)

# Method 3: Forward/backward fill
df.fillna(method='ffill', inplace=True)
```

**b) Handling Outliers:**
```python
# IQR Method
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df_clean = df[(df['col'] >= lower) & (df['col'] <= upper)]
```

**c) Normalization vs Standardization:**

| Technique | Formula | Range | Use When |
|-----------|---------|-------|----------|
| Min-Max Normalization | (x - min)/(max - min) | [0, 1] | Bounded range needed |
| Z-score Standardization | (x - μ)/σ | [-∞, +∞] | Normal distribution assumed |

```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler = MinMaxScaler()
X_norm = scaler.fit_transform(X)

std_scaler = StandardScaler()
X_std = std_scaler.fit_transform(X)
```

---

### Q2. Data Visualization ()

**Explain different types of plots with use cases:**

| Plot Type | Best For | Python Code |
|-----------|----------|-------------|
| Line Plot | Trends over time | `plt.plot(x, y)` |
| Bar Chart | Category comparison | `plt.bar(categories, values)` |
| Histogram | Distribution | `plt.hist(data, bins=10)` |
| Scatter Plot | Correlation | `plt.scatter(x, y)` |
| Box Plot | Outlier detection | `plt.boxplot(data)` |
| Heatmap | Correlation matrix | `sns.heatmap(corr, annot=True)` |
| Pie Chart | Proportions | `plt.pie(values, labels=labels)` |

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram
plt.hist(df['Age'], bins=20, color='blue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age'); plt.ylabel('Frequency')
plt.show()

# Correlation Heatmap
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
```

---

### Q3. Linear Regression ( HIGH PROBABILITY)

**Explain Simple and Multiple Linear Regression with Python code.**

*Simple Linear Regression:*
- y = β₀ + β₁x
- β₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
- β₀ = ȳ - β₁x̄

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

X = df[['feature1', 'feature2']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
```

**Evaluation Metrics for Regression:**

| Metric | Formula | Best Value |
|--------|---------|------------|
| MAE | Σ|yᵢ - ŷᵢ|/n | 0 |
| MSE | Σ(yᵢ - ŷᵢ)²/n | 0 |
| RMSE | √MSE | 0 |
| R² | 1 - SS_res/SS_tot | 1 |

---

### Q4. K-Nearest Neighbors (KNN) Algorithm ()

**Explain KNN with algorithm steps and implementation.**

*Algorithm:*
1. Choose value of K
2. Calculate Euclidean distance to all training points
3. Select K nearest neighbors
4. Majority vote (classification) or average (regression)
5. Predict class/value

*Distance Metric:*
$$d(x, y) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}$$

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

**Choosing K:**
- Small K → high variance, low bias (overfitting)
- Large K → low variance, high bias (underfitting)
- Use **cross-validation** or **elbow method** on error rate

---

### Q5. K-Means Clustering ( HIGH PROBABILITY)

**Explain K-Means algorithm with steps.**

*Algorithm:*
1. Initialize K cluster centroids randomly
2. Assign each point to nearest centroid (Euclidean distance)
3. Recalculate centroids as mean of cluster members
4. Repeat steps 2-3 until convergence (no change in centroids)

**Elbow Method to choose K:**
```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    wcss.append(km.inertia_)

plt.plot(range(1, 11), wcss, 'bo-')
plt.xlabel('Number of Clusters K')
plt.ylabel('WCSS (Inertia)')
plt.title('Elbow Method')
plt.show()
```

```python
# Final K-Means
km = KMeans(n_clusters=3, random_state=42)
labels = km.fit_predict(X)
centroids = km.cluster_centers_
```

---

### Q6. Decision Tree Algorithm

**Explain ID3 algorithm with Entropy and Information Gain.**

*Entropy:* H(S) = -Σ pᵢ log₂(pᵢ)
*Information Gain:* IG(S, A) = H(S) - Σ (|Sv|/|S|) × H(Sv)

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

dt = DecisionTreeClassifier(criterion='entropy', max_depth=5)
dt.fit(X_train, y_train)

# Visualize
plt.figure(figsize=(15, 8))
tree.plot_tree(dt, feature_names=X.columns, filled=True)
plt.show()
```

---

### Q7. Evaluation Metrics - Confusion Matrix ()

**Explain confusion matrix and derive all metrics.**

```
Confusion Matrix:
                 Predicted
                 Pos  | Neg
Actual | Pos  |  TP  |  FN  |
       | Neg  |  FP  |  TN  |
```

**Formulas:**

| Metric | Formula |
|--------|---------|
| Accuracy | (TP + TN) / (TP + TN + FP + FN) |
| Precision | TP / (TP + FP) |
| Recall (Sensitivity) | TP / (TP + FN) |
| F1-Score | 2 × (Precision × Recall) / (Precision + Recall) |
| Specificity | TN / (TN + FP) |

```python
from sklearn.metrics import confusion_matrix, classification_report

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)
print(classification_report(y_test, y_pred))
```

---

### Q8. Cross-Validation

```python
from sklearn.model_selection import cross_val_score

# 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"CV Accuracy: {scores.mean():.4f} ± {scores.std():.4f}")
```

**Types:**
- **K-Fold:** Split into K parts, train on K-1, test on 1
- **Stratified K-Fold:** Maintains class distribution
- **LOOCV:** K = n (leave one out)

---

### Q9. Numerical Problem - Linear Regression Calculation

**Given data:**

| x | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| y | 2 | 4 | 5 | 4 | 5 |

**Calculate β₀ and β₁:**

x̄ = 3, ȳ = 4

Σ(xᵢ - x̄)(yᵢ - ȳ) = (-2)(-2) + (-1)(0) + (0)(1) + (1)(0) + (2)(1) = 4 + 0 + 0 + 0 + 2 = 6
Σ(xᵢ - x̄)² = 4 + 1 + 0 + 1 + 4 = 10

β₁ = 6/10 = **0.6**
β₀ = 4 - 0.6×3 = 4 - 1.8 = **2.2**

**Regression line: y = 2.2 + 0.6x**

---

##  Most Expected Questions

> [!tip] High Probability Questions
> 1.  Data Preprocessing - missing values, outliers, normalization
> 2.  Linear Regression with numerical calculation
> 3.  KNN algorithm with code
> 4.  K-Means with elbow method
> 5.  Confusion matrix - all metrics derivation
> 6.  Data visualization types and Python code
> 7.  Decision Tree with entropy/information gain
> 8.  Cross-validation types

---

##  Quick Formulas

| Formula | Expression |
|---------|-----------|
| Min-Max | (x - min)/(max - min) |
| Z-Score | (x - μ)/σ |
| Euclidean Dist | √Σ(xᵢ - yᵢ)² |
| Entropy | -Σ p log₂(p) |
| R² Score | 1 - SS_res/SS_tot |
| F1-Score | 2PR/(P+R) |

---

*Tags: CS-307 Data Science | Semester V | [[07-Exams]]*
