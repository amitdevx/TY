---
title: "CS-321 AI/ML - Important Questions"
subject: CS-321-VSC-P
type: important-questions
semester: V
university: SPPU
tags:
  - artificial-intelligence
  - machine-learning
  - important-questions
  - exam-prep
  - CS-321
created: 2026-06-16
updated: 2026-06-16
---

#  CS-321: Foundation of AI & ML - Important Questions

> [!warning] Exam Focus
> As a VSC Practical subject, expect both theory questions AND hands-on Python coding. Know how to implement algorithms from scratch and using Scikit-learn/Keras.

---

##  Pattern Analysis

| Marks | Type | Strategy |
|-------|------|---------|
| 2 marks | Definition/concept | 3-4 precise sentences |
| 5 marks | Explain with diagram | Theory + diagram/table |
| 8 marks | Algorithm/Implementation | Full algorithm + Python code |
| 10 marks | Practical/Case study | End-to-end implementation |

---

##  Unit 1: Introduction to AI

### 2-Mark Questions
1. What is the Turing Test? Who proposed it?
2. Differentiate between BFS and DFS.
3. What is the A* algorithm? Give the formula.
4. What is an admissible heuristic?
5. Differentiate Propositional Logic and First-Order Logic.
6. What are the problems with Hill Climbing?

### 5-Mark Questions
1. Explain BFS algorithm with an example. What are its time and space complexities?
2. Describe the A* algorithm. Why is it optimal?
3. Explain Hill Climbing variants and their problems.
4. Explain Propositional Logic with truth table for all connectives.
5. List major milestones in the history of AI.
6. Differentiate ANI, AGI, and ASI.

### 8-Mark Questions
1. ** Implement BFS and DFS in Python. Compare them on time complexity, space complexity, completeness, and optimality.**
2. ** Explain A* algorithm in detail. Why is admissible heuristic important? Implement in Python.**
3. **Explain First-Order Logic with predicates, quantifiers, and inference rules. Give 5 examples of FOL sentences.**
4. **Trace through the 8-puzzle problem using BFS. Show the state space.**

### Python to Know:
```python
from collections import deque
# BFS: queue (deque), popleft()
# DFS: stack (list), pop()
# A*: heapq with f(n) = g(n) + h(n)
```

---

##  Unit 2: Machine Learning Fundamentals

### 2-Mark Questions
1. Define overfitting and underfitting.
2. What is the bias-variance tradeoff?
3. Define: Precision, Recall, F1-Score.
4. What is k-fold cross-validation?
5. Differentiate L1 and L2 regularization.
6. What is AUC-ROC?

### 5-Mark Questions
1. Explain the confusion matrix with TP, TN, FP, FN. Calculate accuracy, precision, recall, F1.
2. Compare supervised, unsupervised, and reinforcement learning with examples.
3. Explain overfitting and underfitting. How do you detect and fix each?
4. What is cross-validation? Why is it better than simple train-test split?
5. Explain bias-variance tradeoff. How does regularization help?

### 8-Mark Questions
1. ** Explain all evaluation metrics: Accuracy, Precision, Recall, F1-Score, AUC-ROC with formulas. When to use each?**
2. ** Implement a complete ML workflow in Python: data loading, preprocessing, model training, evaluation, and cross-validation.**
3. **Explain L1 (Lasso) and L2 (Ridge) regularization with formulas. How do they differ?**
4. **Plot and explain the ROC curve for a classification model in Python.**

### Confusion Matrix to Memorize:
```
           Predicted Pos   Predicted Neg
Actual Pos      TP              FN (Type II)
Actual Neg      FP (Type I)     TN

Accuracy  = (TP+TN)/(TP+TN+FP+FN)
Precision = TP/(TP+FP)
Recall    = TP/(TP+FN)
F1        = 2×P×R/(P+R)
```

---

##  Unit 3: Supervised Learning

### 2-Mark Questions
1. What is the sigmoid function? Give its formula and range.
2. What is the kernel trick in SVM?
3. What is the Naive assumption in Naive Bayes?
4. What is Gini impurity in Decision Trees?
5. What is Bagging in Random Forest?
6. What distance metric does KNN use by default?

### 5-Mark Questions
1. Explain linear regression. What are its assumptions (LINE)?
2. Explain logistic regression and the sigmoid function. What is log-odds?
3. Compare Gini impurity and Entropy in Decision Trees.
4. What is SVM? Explain the maximum margin hyperplane and support vectors.
5. How does KNN classify a new point? How do you choose K?
6. Explain Naive Bayes with Bayes' theorem. What is the Naive assumption?

### 8-Mark Questions
1. ** Implement Linear Regression in Python from scratch and using Scikit-learn. Compare results.**
2. ** Implement a Decision Tree classifier on Iris dataset. Visualize the tree and feature importance.**
3. ** Compare SVM with Linear kernel vs RBF kernel. When does RBF perform better?**
4. **Implement KNN classification. Find optimal K using error rate plot. Compare with Random Forest.**
5. **Build a complete classification pipeline: Naive Bayes on text data. Include TF-IDF preprocessing.**

### Key Formulas:
$$\sigma(z) = \frac{1}{1+e^{-z}}, \quad H(S) = -\sum p_i\log_2(p_i), \quad Gini = 1 - \sum p_i^2$$

$$d_{Euclidean} = \sqrt{\sum(p_i-q_i)^2}, \quad P(C|X) = \frac{P(X|C)P(C)}{P(X)}$$

---

##  Unit 4: Unsupervised Learning & Neural Networks

### 2-Mark Questions
1. What is the objective function of K-Means?
2. What is the Elbow method?
3. What does PCA do? What does "explained variance" mean?
4. What is the vanishing gradient problem?
5. Define: ReLU activation function.
6. What is backpropagation?

### 5-Mark Questions
1. Explain K-Means algorithm step by step. How do you choose optimal K?
2. Compare K-Means and Hierarchical clustering.
3. Explain PCA. What is the scree plot?
4. Describe the perceptron model. What are its limitations?
5. Explain activation functions: Sigmoid, ReLU, Tanh, Softmax with formulas.
6. Explain the backpropagation algorithm.

### 8-Mark Questions
1. ** Implement K-Means clustering in Python. Use Elbow method and Silhouette score to choose K. Visualize clusters.**
2. ** Apply PCA on a high-dimensional dataset. Show the scree plot and visualize data in 2D. Report explained variance.**
3. ** Implement a simple neural network from scratch in Python for XOR problem. Demonstrate backpropagation.**
4. **Compare all activation functions with their formulas, ranges, pros, and cons.**

### Silhouette Score to Know:
$$s = \frac{b - a}{\max(a, b)}$$
where a = mean intra-cluster distance, b = mean nearest-cluster distance

---

##  Unit 5: Deep Learning & Applications

### 2-Mark Questions
1. What is the key advantage of deep learning over traditional ML?
2. What is a convolution operation? What is a filter/kernel?
3. What is Max Pooling? Why is it used?
4. Differentiate RNN and LSTM.
5. What gates does LSTM have?
6. What is TF-IDF?

### 5-Mark Questions
1. Explain CNN architecture: Convolution, Pooling, Fully Connected layers.
2. What is the vanishing gradient problem in RNNs? How does LSTM solve it?
3. Explain LSTM gates: Forget, Input, Output gates.
4. What is Transfer Learning? When and why is it used?
5. Explain NLP text preprocessing pipeline: tokenization, stop words, stemming.
6. What is word embedding? How is it different from BoW/TF-IDF?

### 8-Mark Questions
1. ** Build and train a CNN for MNIST digit classification in Keras. Report test accuracy.**
2. ** Build an LSTM model for sentiment analysis in Keras. Explain the Embedding and LSTM layers.**
3. ** Implement Transfer Learning using pre-trained VGG16 for binary image classification.**
4. **Write Python code for complete NLP pipeline: tokenization → stop word removal → TF-IDF → SVM classifier.**
5. **Compare RNN, LSTM, and GRU architectures. When would you use each?**

### CNN Output Size Formula:
$$O = \left\lfloor\frac{I - K + 2P}{S}\right\rfloor + 1$$
(I=input, K=kernel, P=padding, S=stride)

---

##  Most Important Practical Questions

> [!warning] High probability for practicals!

```python
# 1. Complete ML Pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])
scores = cross_val_score(pipeline, X, y, cv=5, scoring='f1_macro')
print(f"F1: {scores.mean():.4f}")

# 2. CNN in Keras
model = keras.Sequential([
    layers.Conv2D(32, 3, activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D(2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.compile('adam', 'sparse_categorical_crossentropy', metrics=['accuracy'])

# 3. K-Means with Elbow
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
```

---

##  Quick Formula Reference

| Formula | Expression |
|---------|-----------|
| A* | $f(n) = g(n) + h(n)$ |
| Accuracy | $\frac{TP+TN}{TP+TN+FP+FN}$ |
| Precision | $\frac{TP}{TP+FP}$ |
| Recall | $\frac{TP}{TP+FN}$ |
| F1-Score | $\frac{2 \cdot P \cdot R}{P + R}$ |
| Sigmoid | $\frac{1}{1+e^{-z}}$ |
| ReLU | $\max(0, z)$ |
| Entropy | $-\sum p_i\log_2(p_i)$ |
| Gini | $1 - \sum p_i^2$ |
| WCSS | $\sum_j\sum_{x_i\in C_j}\|x_i-\mu_j\|^2$ |
| Backprop | $W = W - \alpha \frac{\partial L}{\partial W}$ |
| L1 Loss | $J + \lambda\sum\|\theta_j\|$ |
| L2 Loss | $J + \lambda\sum\theta_j^2$ |
| Bayes | $P(C\|X) = \frac{P(X\|C)P(C)}{P(X)}$ |
| CNN Output | $\lfloor\frac{I-K+2P}{S}\rfloor + 1$ |

---

← [[Unit-5]] | [[Revision]] →

#AI #machine-learning #important-questions #exam-prep #SPPU #semester-5
