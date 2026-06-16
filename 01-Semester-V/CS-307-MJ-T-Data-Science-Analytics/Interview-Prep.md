---
title: "CS-307 Data Science - Interview Preparation"
subject: CS-307-MJ-T
type: interview-prep
semester: V
university: SPPU
tags:
  - data-science
  - interview-prep
  - ML-interviews
  - CS-307
created: 2026-06-16
updated: 2026-06-16
---

#  CS-307: Data Science - Interview Preparation

> [!tip] Strategy
> Read each question aloud and answer it fully before checking the answer below. The goal is to be able to explain clearly, not just recognize.

---

##  Category 1: Data Science Fundamentals (Q1–Q8)

> [!question] Q1: What is data science? How is it different from machine learning and statistics?
> **Answer**: Data Science is an interdisciplinary field that extracts knowledge from data using scientific methods, algorithms, and systems. **Statistics** focuses on mathematical analysis of data. **Machine Learning** is a technique where algorithms learn patterns from data without explicit programming. **Data Science** is broader - it encompasses data engineering, EDA, statistics, and ML to drive business decisions. Statistics = math; ML = algorithms that learn; Data Science = full pipeline from business problem to insights.

> [!question] Q2: What is the data science pipeline? Describe each step.
> **Answer**: The data science pipeline (CRISP-DM):
> 1. **Business Understanding**: Define the problem and objectives
> 2. **Data Understanding**: Collect and explore data
> 3. **Data Preparation**: Clean, transform, and engineer features
> 4. **Modelling**: Select and train ML models
> 5. **Evaluation**: Assess model performance against business criteria
> 6. **Deployment**: Put model into production
> Data preparation takes 60-70% of time in practice.

> [!question] Q3: What are the different types of data?
> **Answer**: 
> - **Structured**: Organized in rows/columns (tables, CSV). Easy to query with SQL. Example: customer database
> - **Unstructured**: No predefined format. Requires NLP/CV to analyze. Example: tweets, videos, X-rays (~80% of all data)
> - **Semi-structured**: Has some organization (tags/metadata) but not purely tabular. Example: JSON, XML, email
> Also classified as: Nominal, Ordinal, Interval, Ratio (NOIR measurement scales)

> [!question] Q4: What is EDA and why is it important?
> **Answer**: EDA (Exploratory Data Analysis) is the practice of visually and statistically exploring a dataset before modeling. It helps:
> - Understand data distributions and detect outliers
> - Identify missing values and patterns
> - Discover relationships between features
> - Check assumptions for modeling
> - Generate hypotheses
> Without EDA, you might build models on bad data or miss important patterns. "Plot your data before fitting a model!"

> [!question] Q5: What is the difference between a data analyst, data scientist, and data engineer?
> **Answer**:
> - **Data Analyst**: Analyzes historical data, creates dashboards and reports. Tools: SQL, Excel, Tableau. Answers "what happened?"
> - **Data Scientist**: Builds predictive models, applies ML, statistical analysis. Tools: Python, R, Scikit-learn. Answers "what will happen?"
> - **Data Engineer**: Builds and maintains data pipelines, ETL processes, databases. Tools: Spark, Kafka, Airflow. Creates the infrastructure for data scientists.

> [!question] Q6: What is the curse of dimensionality?
> **Answer**: As the number of features (dimensions) increases, data becomes increasingly sparse in the high-dimensional space. Issues: (1) Distance metrics become meaningless - all points appear equidistant, (2) Need exponentially more data to cover the space, (3) Models become harder to train and overfit easily. Solutions: Feature selection, PCA/dimensionality reduction, regularization.

> [!question] Q7: What is data leakage? How do you prevent it?
> **Answer**: Data leakage occurs when information from the test set "leaks" into the training process, giving artificially optimistic results in evaluation. Types: (1) **Target leakage**: Features contain information about the target that wouldn't be available at prediction time, (2) **Train-test contamination**: Fitting scalers/imputers on the full dataset including test data. Prevention: Always fit preprocessing on TRAINING data only, then transform test data. Use pipelines to prevent leakage.

> [!question] Q8: What are the steps of feature engineering?
> **Answer**:
> 1. **Feature Creation**: Derive new features (BMI = weight/height², age from birthdate)
> 2. **Feature Transformation**: Log transform for skewed data, polynomial features for non-linear
> 3. **Feature Encoding**: Label encoding (ordinal), One-hot encoding (nominal)
> 4. **Feature Scaling**: Normalization/Standardization
> 5. **Feature Selection**: Remove irrelevant/redundant features (correlation analysis, RFE, Lasso)

---

##  Category 2: Data Preprocessing (Q9–Q15)

> [!question] Q9: How do you handle missing values?
> **Answer**:
> - **Deletion**: Listwise (row) or Pairwise deletion - only if <5% missing and random
> - **Mean imputation**: For normally distributed numerical features
> - **Median imputation**: For skewed distributions or outlier-prone data
> - **Mode imputation**: For categorical features
> - **KNN imputation**: Use K similar records to impute
> - **Regression imputation**: Predict missing value from other features
> - **Forward/Backward fill**: For time series data
> Choice depends on: % missing, missing mechanism (MCAR/MAR/MNAR), distribution.

> [!question] Q10: What is the difference between normalization and standardization? When use each?
> **Answer**:
> - **Normalization (Min-Max)**: $\frac{x-x_{min}}{x_{max}-x_{min}}$ → scales to [0,1]. Use when: bounded output needed, no extreme outliers, algorithms sensitive to magnitude (Neural networks, KNN)
> - **Standardization (Z-score)**: $\frac{x-\mu}{\sigma}$ → mean=0, std=1. Use when: distribution unknown, outliers present, algorithms assuming normality (SVM, Linear regression, PCA)
> - **Robust Scaler** (uses IQR): Best when many outliers exist

> [!question] Q11: How do you detect and handle outliers?
> **Answer**: 
> **Detection**: (1) Z-score: |z| > 3 is outlier; (2) IQR: below Q1-1.5×IQR or above Q3+1.5×IQR; (3) Visual: boxplot, scatter plot
> **Handling**: (1) Remove if clearly erroneous; (2) Cap/Winsorize to boundary values; (3) Transform (log transform reduces impact); (4) Use robust algorithms (tree-based, median-based); (5) Keep if valid extreme values

> [!question] Q12: What is the difference between Label Encoding and One-Hot Encoding?
> **Answer**:
> - **Label Encoding**: Assigns integer to each category (A=0, B=1, C=2). Implies ordinal order. Use only for ordinal data (e.g., education: High School<Bachelor<Master<PhD). Risk: Misleads algorithms into thinking there's numerical ordering.
> - **One-Hot Encoding**: Creates binary column for each category. No ordinal implication. Use for nominal data (colors, cities). Drawback: High cardinality → many columns (curse of dimensionality). Solution: Target encoding for high-cardinality features.

> [!question] Q13: What is data discretization? Give examples.
> **Answer**: Discretization converts continuous numerical data into discrete categories (bins). 
> Methods: (1) **Equal-width**: width = (max-min)/k, each bin has same range; (2) **Equal-frequency (quantile)**: each bin has same number of points; (3) **Entropy-based**: split at point that maximizes information gain.
> Example: Age [0-17] = Youth, [18-35] = Young Adult, [36-60] = Adult, [60+] = Senior
> Use when: Algorithm requires categorical input, reduce noise, improve interpretability.

> [!question] Q14: What is the difference between data transformation and data reduction?
> **Answer**: 
> - **Data Transformation**: Changes the representation/scale of data. Examples: Normalization, log transform, one-hot encoding. Data volume stays the same.
> - **Data Reduction**: Reduces the volume of data while preserving analysis integrity. Methods: Dimensionality reduction (PCA, feature selection), Numerosity reduction (sampling, aggregation), Data compression.

> [!question] Q15: What is the IQR method? Why is it preferred over Z-score for outlier detection?
> **Answer**: IQR (Interquartile Range) = Q3 - Q1. Outliers: below Q1-1.5×IQR or above Q3+1.5×IQR. **Preference over Z-score**: Z-score uses mean and std dev - both are sensitive to outliers! A single extreme outlier shifts the mean and inflates std dev, masking itself. IQR uses median and quartiles which are resistant to outliers (robust statistics). Z-score is better only for normally distributed data with moderate outliers.

---

##  Category 3: Statistics (Q16–Q22)

> [!question] Q16: Explain the Central Limit Theorem and its importance.
> **Answer**: CLT states that the sampling distribution of the sample mean approaches a normal distribution as sample size n → ∞, regardless of the underlying population distribution (when n ≥ 30 in practice). **Importance**: (1) Allows use of z-tests and t-tests even when population distribution is unknown; (2) Foundation of confidence intervals; (3) Explains why so many things in nature are normally distributed; (4) Enables statistical inference from samples to populations.

> [!question] Q17: What is hypothesis testing? Explain Type I and Type II errors.
> **Answer**: Hypothesis testing is a statistical procedure to test a claim about a population. Process: state H₀ and H₁ → collect data → compute p-value → compare with α.
> - **Type I Error (α)**: Reject H₀ when it's true = "False Alarm" = False Positive. Probability = α (significance level, usually 0.05)
> - **Type II Error (β)**: Fail to reject H₀ when it's false = "Missed" = False Negative
> - **Power** = 1 - β = probability of correctly detecting a real effect
> Trade-off: Reducing α (stricter test) increases β. Want both low, but can't always achieve simultaneously.

> [!question] Q18: What is p-value? Common misconceptions?
> **Answer**: The p-value is the probability of observing data as extreme or more extreme than the actual data, assuming H₀ is true. If p < α (0.05), we reject H₀.
> **Misconceptions**: (1) p-value is NOT the probability H₀ is true; (2) Statistical significance ≠ practical significance (effect size matters); (3) p < 0.05 does not mean "discovered truth" - requires replication; (4) p > 0.05 doesn't prove H₀ is true, just insufficient evidence to reject.

> [!question] Q19: What is the difference between Pearson and Spearman correlation?
> **Answer**:
> - **Pearson**: Measures strength of LINEAR relationship. Assumes normality. Sensitive to outliers. Formula: r = Cov(X,Y)/(σx·σy). Good for: continuous, normally distributed data.
> - **Spearman**: Measures MONOTONIC relationship (can be non-linear). Rank-based. Robust to outliers. Non-parametric. Formula: rs = 1 - 6Σd²/n(n²-1). Good for: ordinal data, skewed distributions, when outliers present.
> Both range from -1 to +1. Use Spearman when: outliers exist, data is ordinal, relationship is monotonic but not linear.

> [!question] Q20: When do you use t-test, chi-square, and ANOVA?
> **Answer**:
> - **One-sample t-test**: Test if sample mean = hypothesized value. E.g., "Is avg height 170cm?"
> - **Two-sample t-test**: Compare means of two independent groups. E.g., "Do males earn more than females?"
> - **Paired t-test**: Compare two related measurements (before-after). E.g., "Did medication lower blood pressure?"
> - **Chi-square test**: Test association between two CATEGORICAL variables. E.g., "Is there association between gender and smoking?"
> - **ANOVA**: Compare means across 3+ groups. E.g., "Is mean salary different across 5 departments?"

> [!question] Q21: What is skewness and kurtosis?
> **Answer**: 
> - **Skewness**: Measures asymmetry of distribution. Positive (right skew): long tail right, Mean > Median (income, prices). Negative (left skew): long tail left, Mean < Median. Zero: Symmetric (normal distribution)
> - **Kurtosis**: Measures "tailedness" (heaviness of tails). Positive (leptokurtic): heavy tails, sharp peak, more extreme outliers. Zero (mesokurtic = normal). Negative (platykurtic): light tails, flat peak.
> Both affect which statistical tests are appropriate.

> [!question] Q22: Explain normal distribution and the 68-95-99.7 rule.
> **Answer**: Normal distribution is a symmetric, bell-shaped probability distribution defined by mean (μ) and standard deviation (σ). The 68-95-99.7 (Empirical) Rule: 68% of data falls within μ ± 1σ, 95% within μ ± 2σ, 99.7% within μ ± 3σ. Importance: Many natural phenomena follow normal distribution, underpins statistical tests (t-test, z-test), Z-scores are calculated assuming normality.

---

##  Category 4: Machine Learning & Data Mining (Q23–Q30)

> [!question] Q23: What is the KDD process? How is it different from CRISP-DM?
> **Answer**: KDD (Knowledge Discovery in Databases) has 5 steps: Data Selection → Preprocessing → Transformation → Data Mining → Interpretation/Evaluation. KDD is older, more database-focused, and academic. CRISP-DM is more comprehensive, includes Business Understanding, is iterative, and is industry-oriented. Both describe the data science workflow but at different abstraction levels. CRISP-DM is more widely used in industry.

> [!question] Q24: What is the Apriori algorithm? Explain with the Apriori principle.
> **Answer**: Apriori mines frequent itemsets and association rules from transaction databases.
> **Apriori Principle**: If an itemset is infrequent, ALL its supersets are also infrequent → Prune search space dramatically.
> **Algorithm**: (1) Find frequent 1-itemsets; (2) Generate candidate k-itemsets from (k-1)-itemsets; (3) Prune infrequent; (4) Repeat until no new frequent itemsets; (5) Generate rules from frequent itemsets.
> **Metrics**: Support = P(A∩B), Confidence = P(B|A) = Sup(A∪B)/Sup(A), Lift = Conf(A→B)/Sup(B). Lift > 1 = positive association.

> [!question] Q25: What is the difference between linear regression and logistic regression?
> **Answer**:
> - **Linear Regression**: Predicts CONTINUOUS output. Output ∈ (-∞, +∞). Uses MSE loss. Line equation: y = β₀ + β₁x. Evaluation: R², RMSE.
> - **Logistic Regression**: Predicts BINARY CLASS (classification). Output ∈ (0,1) via sigmoid. Uses cross-entropy loss. Decision boundary at p=0.5. Evaluation: Accuracy, F1, AUC.
> Logistic regression is a CLASSIFICATION algorithm despite the name "regression"!

> [!question] Q26: How does K-Means work? What are its limitations?
> **Answer**: K-Means iteratively: (1) Initialize K centroids; (2) Assign each point to nearest centroid; (3) Recompute centroids as cluster means; (4) Repeat until no assignment changes. Minimizes WCSS = Σ||xi - μj||².
> **Limitations**: (1) Must choose K; (2) Sensitive to initialization (K-Means++ helps); (3) Assumes spherical, equal-size clusters; (4) Sensitive to outliers; (5) Local optima possible; (6) Only numerical data; (7) Doesn't work for non-convex shapes. Choose K: Elbow method + Silhouette score.

> [!question] Q27: What is the bias-variance tradeoff?
> **Answer**: Total Error = Bias² + Variance + Irreducible Noise. **Bias**: Error from wrong assumptions (underfitting - model too simple). **Variance**: Error from model sensitivity to training data fluctuations (overfitting - model too complex). Tradeoff: Simple model = high bias, low variance. Complex model = low bias, high variance. Goal: Find sweet spot. Strategies: Cross-validation to estimate true error, regularization to reduce variance, more data reduces variance.

> [!question] Q28: What is overfitting? How do you detect and fix it?
> **Answer**: Overfitting: model performs well on training data but poorly on new data (memorized training data). **Detection**: Large gap between training accuracy and validation/test accuracy. **Fixes**: (1) Regularization (L1/L2); (2) More training data; (3) Feature selection (reduce features); (4) Simplify model (reduce complexity); (5) Cross-validation; (6) Ensemble methods (Random Forest); (7) Early stopping (for neural networks); (8) Dropout (neural networks).

> [!question] Q29: What is cross-validation? Why is it better than simple train-test split?
> **Answer**: K-Fold CV divides data into K equal folds. Each fold serves as test set once, rest as training. K results averaged. **Benefits over simple split**: (1) Uses ALL data for both training and testing; (2) More reliable estimate (less dependent on specific split); (3) Reduces variance of model evaluation; (4) Better for small datasets. Common K=5 or K=10. Stratified K-Fold preserves class distribution.

> [!question] Q30: What is feature selection? Name three methods.
> **Answer**: Feature selection identifies the most relevant features and removes irrelevant/redundant ones to: improve accuracy, reduce overfitting, speed up training, improve interpretability.
> **Methods**: (1) **Filter**: Statistical tests - correlation matrix, chi-square test, mutual information (fast, model-independent); (2) **Wrapper**: RFE (Recursive Feature Elimination) - evaluates feature subsets by model performance (slow but effective); (3) **Embedded**: Lasso L1 regularization drives irrelevant feature coefficients to 0, tree feature importances (combines filter+wrapper benefits).

---

##  Category 5: Python & Tools (Q31–Q35)

> [!question] Q31: What is the difference between Pandas, NumPy, and Scikit-learn?
> **Answer**:
> - **NumPy**: Numerical computing, n-dimensional arrays, fast mathematical operations, linear algebra. Foundation of all Python scientific computing.
> - **Pandas**: Data manipulation and analysis using DataFrames (2D labeled arrays). Reading CSV/Excel, groupby, merge, pivot tables. Built on NumPy.
> - **Scikit-learn**: ML library with preprocessing (scalers, encoders), models (linear regression, SVM, RF), evaluation metrics, cross-validation, pipelines. Uses NumPy arrays internally.

> [!question] Q32: What is a Scikit-learn Pipeline? Why use it?
> **Answer**: `sklearn.pipeline.Pipeline` chains preprocessing steps and a model into one object. Benefits: (1) **Prevents data leakage**: fit_transform on train, transform on test automatically; (2) **Convenience**: Single fit() and predict() call; (3) **Cross-validation ready**: CV over entire pipeline; (4) **Reproducibility**: Prevents mistakes in ordering steps.
> `Pipeline([('scaler', StandardScaler()), ('model', RandomForestClassifier())])`

> [!question] Q33: When would you use Plotly over Matplotlib?
> **Answer**: **Plotly**: Interactive (zoom, hover, pan), web-ready, great for dashboards and presentations, HTML output. Use for: dashboards, web apps (Dash), presentations where interaction is needed. **Matplotlib**: Static, publication-quality, fine-grained control, fast, PDF/PNG output. Use for: research papers, reports, quick exploration. **Rule**: Exploration/production web apps → Plotly; Publications/reports → Matplotlib; Statistical analysis → Seaborn.

> [!question] Q34: What is GridSearchCV? How does it work?
> **Answer**: GridSearchCV performs exhaustive hyperparameter tuning via cross-validation. You provide a grid of parameter values; it tries all combinations and returns the best. It uses k-fold CV for each combination to avoid overfitting to validation set.
> ```python
> param_grid = {'C': [0.1, 1, 10], 'kernel': ['rbf', 'linear']}
> grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
> grid_search.fit(X_train, y_train)
> print(grid_search.best_params_)
> ```
> Alternative: RandomizedSearchCV (faster, samples parameters randomly) for large search spaces.

> [!question] Q35: How do you handle imbalanced datasets?
> **Answer**: Imbalanced data (e.g., 99% negative, 1% positive - fraud detection) causes models to always predict majority class.
> **Techniques**: (1) **Resampling**: Oversample minority (SMOTE) or undersample majority; (2) **Class weights**: `class_weight='balanced'` in Scikit-learn; (3) **Evaluation**: Use F1, AUC-ROC instead of accuracy; (4) **Threshold adjustment**: Lower decision threshold from 0.5; (5) **Ensemble methods**: BalancedBaggingClassifier.

---

##  Quick Answer Reference Table

| Question | 5-Second Answer |
|----------|----------------|
| Data types | Structured, Unstructured, Semi-structured |
| CRISP-DM | Business→Data→Prepare→Model→Evaluate→Deploy |
| Missing value for normal dist | Mean imputation |
| Missing value for skewed | Median imputation |
| Outlier detection | Z-score (|z|>3) or IQR (Q1-1.5×IQR to Q3+1.5×IQR) |
| Normalization range | [0, 1] |
| Standardization | Mean=0, Std=1 |
| p-value < 0.05 | Reject H₀ (statistically significant) |
| Type I error | False Positive (rejected H₀ when true) |
| Type II error | False Negative (kept H₀ when false) |
| Pearson vs Spearman | Pearson=linear; Spearman=monotonic/robust |
| Correlation ≠ Causation | Always remember this! |
| KDD steps | Select→Preprocess→Transform→Mine→Interpret |
| Apriori principle | Infrequent → all supersets infrequent |
| Lift > 1 | Positive association |
| K-Means choose K | Elbow method + Silhouette score |

---

← [[Revision]] | [[Overview]] →

#data-science #interview-prep #SPPU #semester-5
