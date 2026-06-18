---
title: "CS-308 Viva 5"
---

[[CS-308-Assignment-5|Back to Assignment 5]]

## 5. Viva Questions
1. **What is Logistic Regression?**
   - Despite its name, Logistic Regression is a classification algorithm. It predicts the probability of a categorical dependent variable using a logistic (sigmoid) function.
2. **What does the Confusion Matrix tell us?**
   - It details the number of correct and incorrect predictions made by the classification model broken down by each class.
3. **What is the difference between Precision and Recall?**
   - Precision is the ratio of correctly predicted positive observations to total predicted positive observations. Recall (Sensitivity) is the ratio of correctly predicted positive observations to all observations in actual class.
4. **Why do we use `max_iter` in the LogisticRegression function?**
   - The underlying optimization algorithm iteratively updates weights. If the data is complex, it may require more iterations to converge to an optimal solution.
5. **Is Logistic Regression used for continuous target variables?**
   - No, it is strictly used for categorical (discrete) target variables. Linear Regression is used for continuous targets.