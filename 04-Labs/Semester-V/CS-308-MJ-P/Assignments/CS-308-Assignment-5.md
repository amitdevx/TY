---
tags: [data-science, lab, assignment, classification, logistic-regression]
title: Assignment 5 - Classification
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 5: Classification using Logistic Regression

## 1. Problem Statement / Aim
**Aim:** To train a Classification model (Logistic Regression) to categorize data into classes, predict target labels for unseen data, and evaluate the model using accuracy, precision, recall, and a Confusion Matrix.

## 2. Theory & Concept
**Classification** is a supervised learning approach where the target variable is discrete (categorical).
- **Logistic Regression**: A statistical model used for binary classification. It uses the logistic function (sigmoid) to map predictions to probabilities between 0 and 1.
- **Confusion Matrix**: A table used to describe the performance of a classification model. It shows True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN).
- **Accuracy**: The ratio of correctly predicted observations to total observations.

## 3. Fully Solved Python Code
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load Dataset (Breast Cancer Dataset - Binary Classification)
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. Model Training
model = LogisticRegression(max_iter=10000) # Increased max_iter for convergence
model.fit(X_train, y_train)

# 4. Predictions
y_pred = model.predict(X_test)

# 5. Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=data.target_names)

print(f"Accuracy: {accuracy * 100:.2f}%\n")
print("Classification Report:")
print(class_report)

# 6. Confusion Matrix Visualization
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=data.target_names, yticklabels=data.target_names)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix')
plt.show()
```

## 4. Expected Output
```text
Accuracy: 95.80%

Classification Report:
              precision    recall  f1-score   support

   malignant       0.96      0.93      0.94        54
      benign       0.96      0.98      0.97        89

    accuracy                           0.96       143
   macro avg       0.96      0.95      0.95       143
weighted avg       0.96      0.96      0.96       143
```
- A heatmap displaying the Confusion Matrix with counts of TP, TN, FP, FN. For example, True Benign=87, True Malignant=50, etc.