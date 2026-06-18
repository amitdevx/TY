---
tags: [data-science, lab, assignment, matplotlib, seaborn, visualization]
title: Assignment 2 - Data Visualization
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 2: Data Visualization with Matplotlib & Seaborn

## 1. Problem Statement / Aim
**Aim:** To visualize data distributions and relationships using Python libraries Matplotlib and Seaborn by creating Line, Bar, and Scatter plots.

## 2. Theory & Concept
**Data Visualization** is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, visualization tools provide an accessible way to see and understand trends, outliers, and patterns.
- **Matplotlib**: The core, standard library for creating static, animated, and interactive visualizations in Python.
- **Seaborn**: A Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
- **Plots**:
  - *Line Plot*: Displays information as a series of data points connected by straight line segments.
  - *Bar Plot*: Represents categorical data with rectangular bars.
  - *Scatter Plot*: Uses Cartesian coordinates to display values for typically two variables for a set of data.

## 3. Fully Solved Python Code
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 12, 78]

x = np.arange(1, 11)
y = 2 * x + 3 + np.random.randn(10)*2

# 1. Line Plot using Matplotlib
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Trend')
plt.title('Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True)

# 2. Bar Plot using Seaborn
plt.subplot(1, 3, 2)
df_bar = pd.DataFrame({'Category': categories, 'Values': values})
sns.barplot(x='Category', y='Values', data=df_bar, palette='viridis')
plt.title('Bar Plot')

# 3. Scatter Plot using Seaborn
plt.subplot(1, 3, 3)
df_scatter = pd.DataFrame({'X': x, 'Y': y})
sns.scatterplot(x='X', y='Y', data=df_scatter, color='r', s=100)
plt.title('Scatter Plot')

plt.tight_layout()
plt.show()
```

## 4. Expected Output
- A window displaying a grid of 3 plots (1 row, 3 columns).
- **Plot 1**: A Line Plot showing a generally increasing trend with blue markers and lines.
- **Plot 2**: A Bar Plot with 5 categories (A-E) using a color gradient from Seaborn's `viridis` palette.
- **Plot 3**: A Scatter Plot showing red dots corresponding to the `(x, y)` coordinate pairs.