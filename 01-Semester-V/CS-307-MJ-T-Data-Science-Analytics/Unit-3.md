---
title: "CS-307 Unit 3 - Data Visualization"
subject: CS-307-MJ-T
type: unit-notes
unit: 3
semester: V
university: SPPU
tags:
  - data-science
  - unit-3
  - visualization
  - matplotlib
  - seaborn
  - plotly
  - CS-307
aliases:
  - DS Unit 3
  - Data Visualization
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# Unit 3: Data Visualization

> [!note] Navigation
> ← [[Unit-2]] | [[Overview]] | [[Unit-4]] →

---

## Learning Objectives

- [ ] Choose the right chart type for each data scenario
- [ ] Create histograms, bar charts, scatter plots, line charts, pie charts
- [ ] Create advanced visualizations: boxplots, heatmaps, dendrograms, word clouds
- [ ] Use Matplotlib, Seaborn, and Plotly effectively
- [ ] Apply visualization for EDA (Exploratory Data Analysis)

---

## 3.1 Why Visualize Data?

> [!important] Key Insight
> ==Data Visualization== transforms raw numbers into visual representations that the human brain processes 60,000× faster than text.

**Goals of Visualization:**
1. **Exploration**: Understand data distributions and patterns
2. **Communication**: Share findings with stakeholders
3. **Confirmation**: Verify assumptions and hypotheses
4. **Detection**: Find outliers, anomalies, patterns

> [!tip] Anscombe's Quartet
> Four datasets with identical statistical properties (mean, variance, correlation) but completely different patterns - only visible through visualization! This proves why you MUST visualize your data.

---

## 3.2 Python Visualization Libraries

| Library | Purpose | Interactivity | Best For |
|---------|---------|---------------|----------|
| **Matplotlib** | Low-level, full control | Static | Custom, publication-quality |
| **Seaborn** | Statistical, high-level | Static | Statistical analysis |
| **Plotly** | Web-based | Interactive | Dashboards, web apps |
| **Pandas** | Built-in plotting | Static | Quick exploration |

```python
# Setup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load sample dataset
df = pd.read_csv('tips.csv')  # or use seaborn built-in
df = sns.load_dataset('tips')   # tips dataset

# Matplotlib style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')

print(df.head())
print(df.shape)
print(df.describe())
```

---

## 3.3 Fundamental Visualizations

### 3.3.1 Histogram

> [!note] Histogram
> Displays the ==distribution of a single continuous variable== by dividing values into bins and showing frequency.

**When to use**: Understand data distribution, check normality, detect skewness.

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Basic histogram
axes[0].hist(df['total_bill'], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].set_title('Total Bill Distribution')
axes[0].set_xlabel('Total Bill ($)')
axes[0].set_ylabel('Frequency')

# With KDE (density curve) - Seaborn
sns.histplot(data=df, x='total_bill', bins=20, kde=True, ax=axes[1])
axes[1].set_title('Histogram with KDE')

# Multiple distributions
sns.histplot(data=df, x='total_bill', hue='sex', bins=20, ax=axes[2])
axes[2].set_title('By Gender')

plt.tight_layout()
plt.savefig('histograms.png', dpi=150)
plt.show()
```

### 3.3.2 Bar Chart

> [!note] Bar Chart
> Compares ==categorical variables== using rectangular bars.

**When to use**: Compare categories, frequency counts, show discrete data.

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Vertical bar chart
day_counts = df['day'].value_counts()
axes[0].bar(day_counts.index, day_counts.values, color=['#3498db','#e74c3c','#2ecc71','#f39c12'])
axes[0].set_title('Count by Day')
axes[0].set_xlabel('Day')
axes[0].set_ylabel('Count')

# Horizontal bar chart
axes[1].barh(day_counts.index, day_counts.values)
axes[1].set_title('Horizontal Bar Chart')

# Grouped bar chart - Seaborn
sns.barplot(data=df, x='day', y='total_bill', hue='sex', ax=axes[2])
axes[2].set_title('Average Bill by Day & Gender')

plt.tight_layout()
plt.show()
```

### 3.3.3 Scatter Plot

> [!note] Scatter Plot
> Shows the ==relationship between two continuous variables==. Each point represents one observation.

**When to use**: Correlation analysis, outlier detection, trend identification.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic scatter
axes[0].scatter(df['total_bill'], df['tip'], alpha=0.6, c='steelblue', s=50)
axes[0].set_xlabel('Total Bill ($)')
axes[0].set_ylabel('Tip ($)')
axes[0].set_title('Bill vs Tip')

# Seaborn scatter with regression line
sns.regplot(data=df, x='total_bill', y='tip', scatter_kws={'alpha':0.5}, ax=axes[1])
axes[1].set_title('Scatter with Regression Line')

# Color by category
scatter = sns.scatterplot(data=df, x='total_bill', y='tip', 
                          hue='sex', size='size', sizes=(50, 200))
plt.show()
```

### 3.3.4 Line Chart

> [!note] Line Chart
> Displays ==trends over time== or ordered categories by connecting data points with lines.

**When to use**: Time series, sequential data, trends.

```python
# Time series example
import numpy as np

dates = pd.date_range('2024-01-01', periods=100, freq='D')
values = np.cumsum(np.random.randn(100)) + 100

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(dates, values, 'b-', linewidth=1.5, label='Stock Price')
ax.fill_between(dates, values.min(), values, alpha=0.1)  # Shaded area
ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.set_title('Stock Price Over Time')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Multiple lines
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_2023 = [120, 135, 150, 180, 200, 175]
sales_2024 = [140, 155, 170, 200, 225, 210]

plt.plot(months, sales_2023, 'b-o', label='2023')
plt.plot(months, sales_2024, 'r-s', label='2024')
plt.legend()
plt.title('Monthly Sales Comparison')
plt.show()
```

### 3.3.5 Pie and Donut Charts

> [!note] Pie Chart
> Shows ==proportions of a whole==. Use sparingly - bar charts are usually clearer.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
sizes = [30, 25, 20, 25]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.05, 0.05, 0.05, 0.05)

# Pie chart
axes[0].pie(sizes, labels=labels, colors=colors, explode=explode,
            autopct='%1.1f%%', shadow=True, startangle=90)
axes[0].set_title('Traffic by Day (Pie)')

# Donut chart
wedge_props = dict(width=0.5)
axes[1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            startangle=90, wedgeprops=wedge_props)
axes[1].set_title('Traffic by Day (Donut)')

plt.tight_layout()
plt.show()
```

### 3.3.6 Area Plot

> [!note] Area Plot
> Line chart with the area ==filled below the line== - emphasizes magnitude and cumulative values.

```python
months = range(1, 13)
category_A = [10, 15, 20, 25, 30, 28, 32, 35, 40, 38, 42, 45]
category_B = [5, 8, 12, 10, 15, 20, 18, 22, 25, 28, 30, 35]

plt.figure(figsize=(10, 5))
plt.stackplot(months, category_A, category_B, 
              labels=['Category A', 'Category B'],
              colors=['#3498db', '#e74c3c'], alpha=0.7)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Stacked Area Plot - Monthly Sales')
plt.legend(loc='upper left')
plt.show()
```

### 3.3.7 Bubble Plot

> [!note] Bubble Plot
> Scatter plot where ==bubble size represents a third variable==.

```python
# Plotly interactive bubble chart
import plotly.express as px

# Using built-in gapminder dataset
df_gap = px.data.gapminder().query("year==2007")

fig = px.scatter(df_gap, x="gdpPercap", y="lifeExp",
                 size="pop", color="continent",
                 hover_name="country",
                 log_x=True, size_max=60,
                 title="Gapminder 2007: GDP vs Life Expectancy (bubble=population)")
fig.show()
```

---

## 3.4 Advanced Visualizations

### 3.4.1 Box Plot (Whisker Plot)

> [!important] Box Plot
> Shows the ==five-number summary==: Min, Q1, Median (Q2), Q3, Max. Outliers appear as individual points.

```
    Min   Q1  Median  Q3   Max    Outlier
     |-----|    |     |-----|       *
         [==========]
              IQR
```

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Matplotlib boxplot
axes[0].boxplot([df[df['day']==day]['total_bill'].values 
                 for day in ['Thur', 'Fri', 'Sat', 'Sun']],
               labels=['Thu', 'Fri', 'Sat', 'Sun'])
axes[0].set_title('Total Bill by Day')

# Seaborn boxplot (easier)
sns.boxplot(data=df, x='day', y='total_bill', hue='sex', ax=axes[1])
axes[1].set_title('Bill by Day and Gender')

plt.tight_layout()
plt.show()

# Violin plot - richer: shows distribution shape
plt.figure(figsize=(10, 5))
sns.violinplot(data=df, x='day', y='total_bill', hue='sex', split=True)
plt.title('Violin Plot - Distribution Shape by Day')
plt.show()
```

### 3.4.2 Heat Map

> [!note] Heat Map
> Displays data as a ==color-encoded matrix==. Essential for correlation matrices and 2D density.

```python
# Correlation heatmap
plt.figure(figsize=(8, 6))
correlation = df[['total_bill', 'tip', 'size']].corr()

sns.heatmap(correlation, 
            annot=True,           # Show values
            fmt='.2f',            # Format
            cmap='coolwarm',      # Color scheme
            vmin=-1, vmax=1,      # Range
            square=True,
            linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Heatmap of cross-tabulation
ct = pd.crosstab(df['day'], df['sex'])
plt.figure(figsize=(6, 4))
sns.heatmap(ct, annot=True, cmap='YlOrRd', fmt='d')
plt.title('Day vs Gender Count Heatmap')
plt.show()
```

### 3.4.3 Pair Plot

```python
# Pair plot - all pairwise scatter plots
sns.pairplot(df[['total_bill', 'tip', 'size', 'sex']], 
             hue='sex',
             diag_kind='kde',
             plot_kws={'alpha': 0.5})
plt.suptitle('Pairplot of Tips Dataset', y=1.02)
plt.show()
```

### 3.4.4 Word Cloud

```python
from wordcloud import WordCloud

text = "data science machine learning python analytics visualization big data AI neural network deep learning"

wordcloud = WordCloud(
    width=800, height=400,
    background_color='white',
    max_words=100,
    colormap='viridis',
    max_font_size=100
).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud Example')
plt.tight_layout()
plt.show()
```

### 3.4.5 Geospatial Visualization

```python
import plotly.express as px

# Choropleth map
df_world = px.data.gapminder().query("year==2007")
fig = px.choropleth(df_world, 
                    locations="iso_alpha",
                    color="lifeExp",
                    hover_name="country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Life Expectancy by Country (2007)")
fig.show()
```

### 3.4.6 3D Scatter Plot

```python
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px

# Plotly 3D (interactive)
fig = px.scatter_3d(df, x='total_bill', y='tip', z='size',
                     color='sex', symbol='smoker',
                     title='3D Scatter: Bill, Tip, Size')
fig.show()

# Matplotlib 3D (static)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['total_bill'], df['tip'], df['size'], 
           c='steelblue', marker='o', alpha=0.6)
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
ax.set_zlabel('Size')
plt.title('3D Scatter Plot')
plt.show()
```

### 3.4.7 Dendrogram

```python
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist

# Generate sample data
np.random.seed(42)
X = np.vstack([np.random.randn(10, 2) + [5, 5],
               np.random.randn(10, 2) + [0, 0],
               np.random.randn(10, 2) + [5, 0]])

# Compute linkage matrix
Z = linkage(X, method='ward', metric='euclidean')

plt.figure(figsize=(10, 5))
dendrogram(Z,
           labels=[f'P{i}' for i in range(len(X))],
           color_threshold=5.0,
           leaf_font_size=10)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.tight_layout()
plt.show()
```

### 3.4.8 Treemap

```python
import plotly.express as px

# Treemap
data = {
    'category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'subcategory': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'],
    'value': [25, 35, 20, 15, 30, 40]
}
df_tree = pd.DataFrame(data)

fig = px.treemap(df_tree,
                 path=['category', 'subcategory'],
                 values='value',
                 color='value',
                 color_continuous_scale='RdBu',
                 title='Treemap Example')
fig.show()
```

---

## 3.5 Choosing the Right Chart

| Data | Relationship | Recommended Chart |
|------|-------------|------------------|
| Single continuous | Distribution | Histogram, KDE |
| Single categorical | Frequency | Bar chart |
| Two continuous | Correlation | Scatter plot |
| Time + Continuous | Trend | Line chart |
| Proportions | Part-of-whole | Pie/Donut chart |
| Two categoricals | Comparison | Grouped bar chart |
| Numerical matrix | Patterns | Heatmap |
| Distribution summary | Outliers | Box plot |
| Text data | Frequency | Word cloud |
| 3 variables | All relationships | Bubble plot |
| Multiple pairs | Overview | Pair plot |

> [!warning] Common Visualization Mistakes
> 1. **Pie charts with too many slices** (>5) → Use bar chart instead
> 2. **3D charts that distort perception** → Use 2D unless depth matters
> 3. **Dual Y-axis charts** → Can be misleading
> 4. **Not labelling axes and title** → Always add labels!
> 5. **Bright rainbow colors** → Use sequential/diverging palettes

---

## Interview Questions - Unit 3

> [!question] Q1: When would you use a boxplot over a histogram?
> **Answer**: Use a boxplot when comparing distributions across multiple categories (e.g., sales by department), or when you specifically want to see Q1, Q3, IQR, and outliers. Use a histogram when you want to see the detailed shape of a single distribution.

> [!question] Q2: What is the difference between Seaborn and Matplotlib?
> **Answer**: Matplotlib is a low-level plotting library with full control but verbose syntax. Seaborn is built on top of Matplotlib, providing higher-level functions for statistical plots with better default aesthetics. Seaborn is better for statistical analysis; Matplotlib is better for custom/publication-quality plots.

> [!question] Q3: What are the advantages of Plotly over Matplotlib?
> **Answer**: Plotly produces interactive plots (zoom, hover, pan) that can be embedded in web applications. Matplotlib produces static images. For dashboards and presentations, Plotly is superior. For PDFs and papers, Matplotlib is used.

> [!question] Q4: What does a correlation heatmap tell you?
> **Answer**: A correlation heatmap shows the Pearson correlation coefficient between all pairs of numerical features. Values range from -1 (perfect negative correlation) to +1 (perfect positive correlation). 0 means no linear relationship. It helps identify: redundant features (high correlation), features related to target, and multicollinearity issues.

> [!question] Q5: What is a dendrogram used for?
> **Answer**: A dendrogram visualizes the output of hierarchical clustering. It shows how individual data points are progressively merged into clusters. The height at which branches merge indicates the distance/dissimilarity between clusters. Used to determine the optimal number of clusters by cutting the dendrogram.

---

## Revision Summary

> [!summary] Unit 3 Key Points
> 1. **Histogram**: Single variable distribution
> 2. **Bar chart**: Categorical comparisons
> 3. **Scatter plot**: Two continuous variable relationship
> 4. **Line chart**: Time series, trends
> 5. **Pie/Donut**: Proportions (use sparingly)
> 6. **Box plot**: Five-number summary + outliers; comparison across groups
> 7. **Heatmap**: Correlation matrix visualization
> 8. **Word cloud**: Text frequency
> 9. **Dendrogram**: Hierarchical clustering output
> 10. **Matplotlib** (static) → **Seaborn** (statistical) → **Plotly** (interactive)

---

← [[Unit-2]] | [[Unit-4]] →

#data-science #unit-3 #visualization #matplotlib #seaborn #SPPU #semester-5
