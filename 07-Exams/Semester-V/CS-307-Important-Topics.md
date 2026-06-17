---
title: "CS-307 Data Science - Important Topics"
subject: CS-307
semester: V
tags:
  - important-topics
  - data-science
  - machine-learning
  - visualization
  - semester-v
  - exam
aliases:
  - Data Science Important
  - CS307 Must-Know
created: 2026-06-16
type: important-topics
---

[[00-Dashboard/Home|Home]] | [[07-Exams/Exams-Dashboard|Exams Dashboard]]


# CS-307 Data Science - Important Topics

> [!important] Exam Focus
> Data Science is a mix of theory and coding. Focus on preprocessing, visualization, ML algorithms, and evaluation metrics. Expect numerical problems on Linear Regression and confusion matrix.

---

## Top 10 Most Important Topics

| # | Topic | Description | Probability |
|---|-------|-------------|-------------|
| 1 | **Data Preprocessing** | Missing values, outliers, normalization, encoding |  |
| 2 | **Linear Regression** | Simple/Multiple LR, β₀, β₁ calculation, R² |  |
| 3 | **K-Means Clustering** | Algorithm, WCSS, Elbow Method, centroids |  |
| 4 | **Confusion Matrix & Metrics** | Precision, Recall, F1, Accuracy |  |
| 5 | **KNN Algorithm** | Distance metric, choosing K, classification |  |
| 6 | **Data Visualization** | Plot types, matplotlib/seaborn, when to use each |  |
| 7 | **Decision Tree** | Entropy, Information Gain, ID3 |  |
| 8 | **Cross-Validation** | K-fold, Stratified K-fold, LOOCV |  |
| 9 | **Feature Engineering** | Feature selection vs extraction, PCA |  |
| 10 | **Supervised vs Unsupervised** | Types of ML, examples of each |  |

---

## "Definitely Going to Come" Section

> [!warning] Near-Certain Exam Questions
> 1. **Data preprocessing** - handle missing values + normalize data (code)
> 2. **Linear Regression** - numerical: find β₀, β₁ given data table, draw regression line
> 3. **K-Means** - explain algorithm + elbow method code
> 4. **Confusion Matrix** - given TP/FP/TN/FN, calculate precision, recall, F1, accuracy
> 5. **KNN** - explain with diagram, code implementation
> 6. **Plot types** - when to use histogram vs scatter plot vs box plot

---

## Must-Know Definitions

| Term | Definition |
|------|-----------|
| **Data Science** | Interdisciplinary field using stats, ML, and computing to extract insights from data |
| **Feature** | Input variable (column) used for prediction |
| **Label/Target** | Output variable to be predicted |
| **Overfitting** | Model performs well on training data but poorly on test data |
| **Underfitting** | Model is too simple to capture data patterns |
| **Bias** | Error from incorrect assumptions (underfitting) |
| **Variance** | Error from sensitivity to training data (overfitting) |
| **Normalization** | Scale features to [0,1] using Min-Max |
| **Standardization** | Scale features to mean=0, std=1 using Z-score |
| **Inertia/WCSS** | Sum of squared distances from cluster centroid |
| **Entropy** | Measure of impurity: H = -Σ p log₂(p) |
| **Cross-Validation** | Technique to evaluate model generalization |

---

## Quick Formulas to Remember

| Formula | Expression |
|---------|-----------|
| **Min-Max Normalization** | x' = (x - min) / (max - min) |
| **Z-Score Standardization** | x' = (x - μ) / σ |
| **Euclidean Distance** | d = √[Σ(xᵢ - yᵢ)²] |
| **Linear Regression** | y = β₀ + β₁x |
| **β₁** | Σ(xᵢ-x̄)(yᵢ-ȳ) / Σ(xᵢ-x̄)² |
| **β₀** | ȳ - β₁x̄ |
| **R² Score** | 1 - SS_res/SS_tot |
| **Entropy** | H(S) = -Σ pᵢ log₂(pᵢ) |
| **Information Gain** | IG = H(S) - Σ(|Sv|/|S|)H(Sv) |
| **Precision** | TP / (TP + FP) |
| **Recall** | TP / (TP + FN) |
| **F1-Score** | 2 × P × R / (P + R) |
| **Accuracy** | (TP + TN) / Total |

---

## Quick Code Patterns

### Data Preprocessing Pipeline
```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data.csv')

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Remove outliers (IQR)
Q1, Q3 = df['col'].quantile([0.25, 0.75])
IQR = Q3 - Q1
df = df[(df['col'] >= Q1 - 1.5*IQR) & (df['col'] <= Q3 + 1.5*IQR)]

# Normalize
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
```

### Linear Regression
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"R²: {r2_score(y_test, y_pred):.4f}")
print(f"β₀: {model.intercept_:.4f}, β₁: {model.coef_}")
```

### K-Means + Elbow Method
```python
from sklearn.cluster import KMeans

wcss = [KMeans(n_clusters=k).fit(X).inertia_ for k in range(1, 11)]
# Plot to find elbow
km = KMeans(n_clusters=3)
labels = km.fit_predict(X)
```

### Confusion Matrix
```python
from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))
```

### KNN
```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
```

---

## Visualization Cheat Sheet

| Chart Type | When to Use | Code |
|------------|-------------|------|
| Line Plot | Trends over time | `plt.plot(x, y)` |
| Bar Chart | Category comparison | `plt.bar(cat, val)` |
| Histogram | Single variable distribution | `plt.hist(data, bins=20)` |
| Scatter | Correlation between 2 vars | `plt.scatter(x, y)` |
| Box Plot | Outlier detection | `plt.boxplot(data)` |
| Heatmap | Correlation matrix | `sns.heatmap(corr, annot=True)` |
| Pair Plot | All feature pairs | `sns.pairplot(df)` |

---

## Common Mistakes to Avoid

> [!warning] Mistakes to Avoid
> - **Fitting scaler on test data:** ALWAYS fit scaler on training data only, then transform both train and test.
> - **K-Means is sensitive to initialization:** Use `n_init=10` or `init='k-means++'` to get stable results.
> - **Precision vs Recall trade-off:** High precision → few false positives; High recall → few false negatives.
> - **R² can be negative:** If model is worse than a horizontal line through mean.
> - **Entropy = 0 means pure node** (all same class), not impure.
> - **KNN requires feature scaling** - unscaled features distort distance calculations.
> - **Cross-validation:** Don't peek at test data before choosing hyperparameters.

---

## Numerical Problem Template - Linear Regression

**Given table: Calculate β₀, β₁, and predict y for given x**

| Step | Formula | Action |
|------|---------|--------|
| 1 | x̄ = Σx/n | Calculate mean of x |
| 2 | ȳ = Σy/n | Calculate mean of y |
| 3 | Σ(xᵢ-x̄)(yᵢ-ȳ) | Numerator for β₁ |
| 4 | Σ(xᵢ-x̄)² | Denominator for β₁ |
| 5 | β₁ = Step3/Step4 | Slope |
| 6 | β₀ = ȳ - β₁x̄ | Intercept |
| 7 | y = β₀ + β₁x | Predict |

---

*Tags: CS-307 Data Science | Semester V | [[07-Exams/Exams-Dashboard|Exams]]*
