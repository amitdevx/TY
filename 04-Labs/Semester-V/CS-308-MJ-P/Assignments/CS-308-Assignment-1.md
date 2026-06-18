---
tags: [data-science, lab, assignment, pandas]
title: Assignment 1 - Data Wrangling with Pandas
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 1: Data Wrangling with Pandas

## 1. Problem Statement / Aim
**Aim:** To perform data wrangling and cleaning operations using the Pandas library in Python, including handling missing values, filtering data, and basic transformations.

## 2. Theory & Concept
**Pandas** is a powerful Python data analysis toolkit providing fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive.
- **DataFrame**: A two-dimensional, size-mutable, potentially heterogeneous tabular data structure.
- **Data Cleaning**: The process of detecting and correcting (or removing) corrupt or inaccurate records from a dataset.
- **Handling Missing Values**: Dealing with `NaN` (Not a Number) values either by dropping them (`dropna()`) or imputing them (`fillna()`).

## 3. Fully Solved Python Code
```python
import pandas as pd
import numpy as np

# Creating a sample dataset with missing values
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan, 'Frank'],
    'Age': [25, np.nan, 30, 22, 28, 35],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Salary': [60000, 45000, 70000, 50000, np.nan, 55000]
}

df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
print("\n")

# 1. Handling Missing Values
# Imputing Age with Mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Dropping rows where Name is missing
df = df.dropna(subset=['Name'])

# Imputing Salary with Median
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("--- DataFrame After Cleaning ---")
print(df)
print("\n")

# 2. Filtering Data
# Selecting IT Department employees
it_employees = df[df['Department'] == 'IT']
print("--- IT Employees ---")
print(it_employees)
print("\n")

# 3. Data Transformation
# Adding a new column: Bonus (10% of Salary)
df['Bonus'] = df['Salary'] * 0.10
print("--- DataFrame with Bonus Column ---")
print(df)
```

## 4. Expected Output
```text
--- Original DataFrame ---
   Employee_ID     Name   Age Department   Salary
0          101    Alice  25.0         IT  60000.0
1          102      Bob   NaN         HR  45000.0
2          103  Charlie  30.0         IT  70000.0
3          104    David  22.0    Finance  50000.0
4          105      NaN  28.0    Finance      NaN
5          106    Frank  35.0         HR  55000.0

--- DataFrame After Cleaning ---
   Employee_ID     Name   Age Department   Salary
0          101    Alice  25.0         IT  60000.0
1          102      Bob  28.0         HR  45000.0
2          103  Charlie  30.0         IT  70000.0
3          104    David  22.0    Finance  50000.0
5          106    Frank  35.0         HR  55000.0

--- IT Employees ---
   Employee_ID     Name   Age Department   Salary
0          101    Alice  25.0         IT  60000.0
2          103  Charlie  30.0         IT  70000.0

--- DataFrame with Bonus Column ---
   Employee_ID     Name   Age Department   Salary   Bonus
0          101    Alice  25.0         IT  60000.0  6000.0
1          102      Bob  28.0         HR  45000.0  4500.0
2          103  Charlie  30.0         IT  70000.0  7000.0
3          104    David  22.0    Finance  50000.0  5000.0
5          106    Frank  35.0         HR  55000.0  5500.0
```