---
title: "CS-307 Data Science and Analytics - Syllabus"
subject: CS-307-MJ-T
type: syllabus
semester: V
university: SPPU
tags:
  - data-science
  - syllabus
  - semester-5
  - CS-307
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-307-MJ-T: Data Science and Analytics - Syllabus

> [!note] University: Savitribai Phule Pune University (SPPU) | Semester V

---

## Unit 1: Introduction to Data Science (8 hrs)

### 1.1 Fundamentals
- Definition and scope of Data Science
- Data Science vs. Traditional Statistics vs. Business Intelligence
- Applications of Data Science (Healthcare, Finance, E-commerce, Social Media)
- Data Science ecosystem

### 1.2 Data Scientist Role
- Skills required: Statistics, Programming, Domain Knowledge
- Data Science team roles: Data Engineer, Data Analyst, Data Scientist, ML Engineer
- The "Unicorn" data scientist

### 1.3 Data Types
- **Structured Data**: Tabular, relational databases (SQL)
- **Unstructured Data**: Text, images, audio, video
- **Semi-structured Data**: JSON, XML, CSV, log files
- Quantitative vs. Qualitative data
- Discrete vs. Continuous data
- Nominal, Ordinal, Interval, Ratio scales

### 1.4 Data Science Process / Pipeline
- Business understanding → Data acquisition → Data preprocessing → Exploratory Data Analysis (EDA) → Modelling → Evaluation → Deployment
- CRISP-DM (Cross Industry Standard Process for Data Mining)

---

## Unit 2: Data Preprocessing (10 hrs)

### 2.1 Data Quality Issues
- Noisy data, incomplete data, inconsistent data

### 2.2 Data Cleaning
- Handling missing values (deletion, mean/median/mode imputation, regression imputation)
- Handling outliers (Z-score method, IQR method, visualization)
- Removing duplicates
- Smoothing noisy data (binning, regression, clustering)

### 2.3 Data Integration
- Schema integration
- Entity identification problem
- Handling redundancy (correlation analysis)

### 2.4 Data Transformation
- Normalization: Min-Max scaling, Z-score normalization, Decimal scaling
- Attribute construction
- Aggregation, Generalization

### 2.5 Data Reduction
- Dimensionality reduction (PCA, Feature selection)
- Numerosity reduction (sampling, clustering, histograms)
- Data compression

### 2.6 Data Discretization
- Binning (equal-width, equal-frequency)
- Histogram analysis
- Cluster analysis, entropy-based discretization

---

## Unit 3: Data Visualization (8 hrs)

### 3.1 Fundamentals of Visualization
- Goals and principles of visualization
- **Histograms**: Distribution of single continuous variable
- **Bar Charts**: Categorical comparisons (vertical/horizontal)
- **Scatter Plots**: Relationship between two continuous variables
- **Line Charts**: Trends over time (time-series)
- **Area Plots**: Cumulative values over time
- **Pie/Donut Charts**: Proportions/percentages
- **Bubble Plots**: Three-variable relationships

### 3.2 Advanced Visualizations
- **Box Plots (Whisker Plots)**: Five-number summary, outlier detection
- **Heat Maps**: Matrix-based, correlation matrices
- **Dendrograms**: Hierarchical clustering output
- **Venn Diagrams**: Set relationships
- **Treemaps**: Hierarchical part-to-whole relationships
- **3D Scatter Plots**: Three-dimensional data exploration
- **Word Clouds**: Frequency of text data
- **Geospatial Plots (Choropleth)**: Geographical data visualization

### 3.3 Python Visualization Libraries
- **Matplotlib**: `pyplot`, figure/axes, customization
- **Seaborn**: Statistical plots, `sns.heatmap()`, `sns.pairplot()`
- **Plotly**: Interactive, web-based, `plotly.express`
- Pandas built-in plotting

---

## Unit 4: Statistics for Data Science (10 hrs)

### 4.1 Descriptive Statistics
- Measures of Central Tendency: Mean, Median, Mode
- Measures of Dispersion: Range, Variance, Standard Deviation, IQR
- Measures of Shape: Skewness, Kurtosis
- Five-number summary

### 4.2 Probability Distributions
- Discrete distributions: Binomial, Poisson
- Continuous distributions: Normal (Gaussian), Exponential
- Central Limit Theorem (CLT)
- Z-score, Standard Normal Distribution

### 4.3 Hypothesis Testing
- Null Hypothesis (H₀) and Alternative Hypothesis (H₁)
- Type I error (α) and Type II error (β)
- p-value and significance level
- t-test (one-sample, two-sample, paired)
- Chi-square test
- ANOVA (Analysis of Variance)

### 4.4 Correlation and Covariance
- Pearson Correlation Coefficient
- Spearman Rank Correlation
- Covariance matrix
- Correlation vs. Causation

---

## Unit 5: Introduction to Data Mining & Machine Learning (12 hrs)

### 5.1 Data Mining Concepts
- Definition and need for data mining
- KDD (Knowledge Discovery in Databases) process
- Data mining vs. Machine Learning
- Applications of data mining

### 5.2 Machine Learning Fundamentals
- Types of ML: Supervised, Unsupervised, Semi-supervised, Reinforcement
- Modelling process: Define → Train → Validate → Predict
- Feature engineering: Feature selection, Feature extraction, Feature creation
- Overfitting and underfitting, Bias-Variance tradeoff
- Training set, Validation set, Test set (70-15-15 split)
- Cross-validation (k-fold)

### 5.3 Supervised Learning: Regression
- **Linear Regression**: Simple and Multiple; OLS method
- **Polynomial Regression**: Non-linear relationships
- **Logistic Regression**: Binary classification, Sigmoid function

### 5.4 Supervised Learning: Classification
- **K-Nearest Neighbors (KNN)**: Distance metrics, choosing k
- **Random Forest**: Ensemble of decision trees, bagging

### 5.5 Unsupervised Learning
- **K-Means Clustering**: Centroids, Elbow method, Inertia
- **Apriori Algorithm**: Association rule mining, Support, Confidence, Lift

---

## Unit-wise Hours Distribution

| Unit | Title | Hours |
|------|-------|-------|
| 1 | Introduction to Data Science | 8 |
| 2 | Data Preprocessing | 10 |
| 3 | Data Visualization | 8 |
| 4 | Statistics for Data Science | 10 |
| 5 | Data Mining & Machine Learning | 12 |
| **Total** | | **48** |

---

## Text Books
1. *Python for Data Analysis*, 2nd Ed - Wes McKinney (O'Reilly)
2. *Data Science from Scratch* - Joel Grus (O'Reilly)
3. *Hands-On Machine Learning with Scikit-Learn & TensorFlow* - Aurélien Géron

## Reference Books
1. *Introduction to Data Mining* - Tan, Steinbach, Kumar
2. *The Art of Data Science* - Roger Peng & Elizabeth Matsui
3. *Statistics for Data Scientists* - Bruce & Bruce

---

← [[Overview]] | [[Unit-1]] →
