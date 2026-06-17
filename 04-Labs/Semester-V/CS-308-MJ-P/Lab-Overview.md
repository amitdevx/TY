---
title: CS-308-MJ-P Data Science Lab
tags: [lab, data-science-lab, semester-v, cs-308, python, jupyter, machine-learning]
aliases: [Data Science Lab, CS-308 Lab, DS Lab]
lab_code: CS-308-MJ-P
based_on: CS-307-MJ-T Data Science and Machine Learning
language: Python 3.8+
platform: Jupyter Notebook
semester: V
total_assignments: 6
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs Dashboard]]


# CS-308-MJ-P - Data Science Lab

> [!important] Lab Info
> **Code:** CS-308-MJ-P | **Based On:** CS-307-MJ-T Data Science
> **Language:** Python 3.8+ | **Platform:** Jupyter Notebook
> **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn

---

## Lab Navigation

| Assignment | Topic | Link | Status |
|-----------|-------|------|--------|
| Exp-01 | Data Processing & Cleaning | Experiments/Exp-01-Data-Processing | ⬜ |
| Exp-02 | Basic Visualization | Experiments/Exp-02-Basic-Visualization | ⬜ |
| Exp-03 | Advanced Visualization | Experiments/Exp-03-Advanced-Visualization | ⬜ |
| Exp-04 | Regression (ML) | Experiments/Exp-04-Regression | ⬜ |
| Exp-05 | Classification (ML) | Experiments/Exp-05-Classification | ⬜ |
| Exp-06 | Unsupervised ML | Experiments/Exp-06-Unsupervised-ML | ⬜ |

---

## Assignment Details

### Assignment 1 - Data Processing & Cleaning (2 slots)

**Objective:** Load, explore, and clean real-world datasets

**Libraries:** NumPy, Pandas

**Programs:**
1. Load CSV/Excel dataset with Pandas (`pd.read_csv`)
2. Explore data: `.shape`, `.info()`, `.describe()`, `.head()`
3. Handle missing values: `.isnull()`, `.fillna()`, `.dropna()`
4. Data type conversion: `.astype()`
5. Remove duplicates: `.drop_duplicates()`
6. String operations on columns
7. Data aggregation: `.groupby()`, `.pivot_table()`
8. Merge/join DataFrames: `pd.merge()`

**Expected Dataset:** Titanic, Iris, or custom student marks data

### Assignment 2 - Basic Visualization (2 slots)

**Objective:** Create effective visualizations for data exploration

**Libraries:** Matplotlib, Seaborn

**Programs:**
1. Line plot - time series data
2. Bar chart - categorical comparison
3. Histogram - distribution of values
4. Pie chart - proportion display
5. Box plot - outlier detection
6. Scatter plot - relationship between variables

**Expected Output:** Publication-quality graphs with titles, labels, legends

### Assignment 3 - Advanced Visualization (2 slots)

**Objective:** Multi-variable and complex visualizations

**Libraries:** Seaborn, Matplotlib subplots

**Programs:**
1. Heatmap - correlation matrix
2. Pair plot - multi-variable relationships
3. Violin plot - distribution + box plot
4. Subplot grids - multiple plots in one figure
5. 3D scatter plot with mpl_toolkits
6. Interactive plots with Plotly (optional)

### Assignment 4 - Regression ML (2 slots)

**Objective:** Supervised ML for continuous prediction

**Libraries:** Scikit-learn, Matplotlib

**Programs:**
1. **Linear Regression** - predict house prices
   - `train_test_split`, `LinearRegression`
   - Metrics: MSE, RMSE, R² score
2. **Multiple Linear Regression** - multiple features
3. **Polynomial Regression** - non-linear patterns
4. **Ridge & Lasso Regression** - regularization

**Key Code:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")
```

### Assignment 5 - Classification ML (2 slots)

**Objective:** Supervised ML for categorical prediction

**Programs:**
1. **KNN (K-Nearest Neighbors)** - classify Iris dataset
2. **Naive Bayes** - spam email detection
3. **Decision Tree** - visualization with `plot_tree`
4. **Random Forest** - ensemble classifier
5. **SVM (Support Vector Machine)** - binary classification
6. Confusion Matrix, Precision, Recall, F1-Score

**Evaluation Metrics:**
```python
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```

### Assignment 6 - Unsupervised ML (2 slots)

**Objective:** Pattern discovery without labels

**Programs:**
1. **K-Means Clustering** - cluster customers
   - Elbow method for optimal K
   - Silhouette score
2. **Hierarchical Clustering** - dendrogram
3. **DBSCAN** - density-based clustering
4. **PCA (Principal Component Analysis)** - dimensionality reduction
   - Explained variance ratio
   - 2D visualization of high-dimensional data

---

## Completion Tracker

- [ ] **Exp-01 - Data Processing**
  - [ ] Load and explore dataset
  - [ ] Handle missing values
  - [ ] Data cleaning + transformation
  - [ ] Notebook submitted

- [ ] **Exp-02 - Basic Visualization**
  - [ ] Line, bar, histogram
  - [ ] Box plot, scatter plot
  - [ ] Notebook submitted

- [ ] **Exp-03 - Advanced Visualization**
  - [ ] Heatmap + pairplot
  - [ ] Subplots
  - [ ] Notebook submitted

- [ ] **Exp-04 - Regression**
  - [ ] Linear Regression with metrics
  - [ ] Multiple/Polynomial regression
  - [ ] Notebook submitted

- [ ] **Exp-05 - Classification**
  - [ ] KNN + Decision Tree
  - [ ] Confusion matrix
  - [ ] Notebook submitted

- [ ] **Exp-06 - Unsupervised**
  - [ ] K-Means + Elbow
  - [ ] PCA visualization
  - [ ] Notebook submitted

---

## Setup Guide

### Environment Setup

```bash
# Install Anaconda (recommended) or pip packages
pip install numpy pandas matplotlib seaborn scikit-learn jupyter

# Launch Jupyter Notebook
jupyter notebook

# Or use JupyterLab
jupyter lab
```

### Essential Imports Template

```python
# Standard imports for Data Science
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Set display options
pd.set_option('display.max_columns', None)
sns.set_theme(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
```

### Libraries Quick Reference

| Library | Import | Primary Use |
|---------|--------|------------|
| NumPy | `import numpy as np` | Array operations |
| Pandas | `import pandas as pd` | DataFrames |
| Matplotlib | `import matplotlib.pyplot as plt` | Plotting |
| Seaborn | `import seaborn as sns` | Statistical plots |
| Scikit-learn | `from sklearn...` | ML algorithms |

---

## Algorithm Comparison

| Algorithm | Type | Hyperparameters | Best For |
|-----------|------|----------------|---------|
| Linear Regression | Regression | none | Linear relationships |
| KNN | Classification | k | Small datasets |
| Decision Tree | Both | max_depth | Interpretable |
| Random Forest | Both | n_estimators | General purpose |
| SVM | Both | C, kernel | High-dimensional |
| K-Means | Clustering | k | Known clusters |
| PCA | Dimensionality | n_components | Visualization |

---

## Related

- [[11-Tracking/Lab-Tracker|Lab Tracker]]

---

*Lab Overview | CS-308-MJ-P | Semester V | Last Updated: 2026-06-16*
