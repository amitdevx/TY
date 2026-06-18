---
tags: [data-science, lab, assignment, eda]
title: Assignment 3 - Exploratory Data Analysis (EDA)
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 3: Exploratory Data Analysis (EDA)

## 1. Problem Statement / Aim
**Aim:** To perform Exploratory Data Analysis (EDA) on a standard dataset (e.g., the Iris dataset) to summarize its main characteristics, often using visual methods and descriptive statistics.

## 2. Theory & Concept
**Exploratory Data Analysis (EDA)** is an approach to analyzing datasets to summarize their main characteristics. EDA is crucial before formal modeling to discover patterns, spot anomalies, and test hypotheses.
- **Descriptive Statistics**: Summarizing data using measures like mean, median, standard deviation.
- **Correlation Matrix**: A table showing correlation coefficients between variables, useful for finding linear relationships.
- **Pair Plot**: Visualizing pairwise relationships in a dataset, helping to identify clusters and distributions across multiple dimensions simultaneously.

## 3. Fully Solved Python Code
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print("--- Dataset Info ---")
print(df.info())
print("\n")

print("--- Descriptive Statistics ---")
print(df.describe())
print("\n")

print("--- Checking for Missing Values ---")
print(df.isnull().sum())
print("\n")

# Visualization 1: Pairplot
print("Generating Pairplot...")
sns.pairplot(df, hue='species', diag_kind='kde')
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()

# Visualization 2: Correlation Heatmap
print("Generating Correlation Heatmap...")
# Calculate correlation only for numeric columns
corr_matrix = df.drop('species', axis=1).corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()
```

## 4. Expected Output
- Text outputs showing:
  - Dataset Info (150 rows, 5 columns, no nulls).
  - Descriptive Statistics (Count, Mean, Std, Min, Max, Quartiles for each numeric feature).
  - Missing Values sum (0 for all columns).
- Graphical outputs:
  - A Pair Plot highlighting the differences in feature distributions across the three iris species (setosa, versicolor, virginica).
  - A Heatmap indicating high positive correlation (e.g., between petal length and petal width) and negative correlations.