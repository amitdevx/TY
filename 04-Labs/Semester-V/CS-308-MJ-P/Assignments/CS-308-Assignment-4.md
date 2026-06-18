---
tags: [data-science, lab, assignment, machine-learning, regression]
title: Assignment 4 - Simple Linear Regression
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 4: Simple Linear Regression using Scikit-Learn

## 1. Problem Statement / Aim
**Aim:** To train a Simple Linear Regression model to predict a dependent variable based on an independent variable, evaluate the model's performance, and plot the regression line.

## 2. Theory & Concept
**Linear Regression** is a fundamental supervised machine learning algorithm used for predictive analysis. It models the relationship between a scalar response and one explanatory variable.
- **Equation**: $y = mx + c$ (where $m$ is the slope, $c$ is the intercept).
- **Mean Squared Error (MSE)**: Measures the average of the squares of the errors (the difference between estimated values and the actual value).
- **R-squared ($R^2$) Score**: Represents the proportion of variance for a dependent variable that's explained by an independent variable (a score closer to 1 is better).

## 3. Fully Solved Python Code
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Generate Synthetic Data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # Independent variable (e.g., Years of Experience)
y = 4 + 3 * X + np.random.randn(100, 1)  # Dependent variable (e.g., Salary)

# 2. Split Data into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

print(f"Model Intercept (c): {model.intercept_[0]:.4f}")
print(f"Model Coefficient (m): {model.coef_[0][0]:.4f}\n")

# 4. Predictions
y_pred = model.predict(X_test)

# 5. Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R-squared Score (R2): {r2:.4f}")

# 6. Visualization
plt.scatter(X_test, y_test, color='black', label='Actual Data')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regression Line')
plt.xlabel('Independent Variable (X)')
plt.ylabel('Dependent Variable (y)')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
```

## 4. Expected Output
```text
Model Intercept (c): 4.1429
Model Coefficient (m): 2.7993

Mean Squared Error (MSE): 0.6537
R-squared Score (R2): 0.8072
```
- A plot displaying black dots representing the actual test data points, and a solid blue line representing the model's line of best fit.