---
title: "CS-321 Foundation of AI and ML - Syllabus"
subject: CS-321-VSC-P
type: syllabus
semester: V
university: SPPU
tags:
  - artificial-intelligence
  - machine-learning
  - syllabus
  - semester-5
  - CS-321
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-321-VSC-P: Foundation of AI and ML - Syllabus

> [!note] University: Savitribai Phule Pune University (SPPU) | Semester V | VSC Practical

---

## Unit 1: Introduction to Artificial Intelligence (8 hrs)

### 1.1 History of AI
- Dartmouth Conference (1956) - Birth of AI
- Key milestones: Logic Theorist, LISP, Expert Systems, Deep Blue, AlphaGo
- AI winters and revivals
- Modern AI: Big Data, GPUs, Deep Learning renaissance

### 1.2 Turing Test
- Alan Turing's "Computing Machinery and Intelligence" (1950)
- Imitation Game
- CAPTCHA, ELIZA - Historical context
- Criticisms: Chinese Room argument (Searle)

### 1.3 AI Applications
- Healthcare (diagnosis), Finance (fraud detection), Autonomous vehicles
- Natural Language Processing, Computer Vision, Robotics
- Recommendation systems, Game playing

### 1.4 Problem Solving and Search Strategies
- **State space representation**: States, operators, initial/goal state
- **Uninformed (Blind) Search**:
  - BFS (Breadth-First Search) - Complete, Optimal (uniform cost)
  - DFS (Depth-First Search) - Not complete, not optimal; memory efficient
  - IDDFS (Iterative Deepening DFS)
  - UCS (Uniform Cost Search)
- **Informed (Heuristic) Search**:
  - Greedy Best-First Search
  - A\* Algorithm - f(n) = g(n) + h(n); admissible heuristic
  - Hill Climbing (Steepest Ascent, Stochastic, First-choice)

### 1.5 Knowledge Representation
- **Propositional Logic**: Sentences, connectives (∧, ∨, ¬, →, ↔), truth tables
- **First-Order Logic (Predicate Logic)**: Predicates, quantifiers (∀, ∃), functions
- Forward chaining, Backward chaining
- Inference rules: Modus Ponens, Resolution

---

## Unit 2: Machine Learning Fundamentals (8 hrs)

### 2.1 Types of Machine Learning
- **Supervised Learning**: Labelled data; Regression & Classification
- **Unsupervised Learning**: Unlabelled data; Clustering & Association
- **Semi-Supervised Learning**: Mix of labelled and unlabelled
- **Reinforcement Learning**: Agent-environment, rewards; Q-learning

### 2.2 ML Workflow
- Problem formulation → Data collection → Preprocessing → Feature engineering → Model selection → Training → Evaluation → Deployment

### 2.3 Data Splitting
- Training set (70%), Validation set (15%), Test set (15%)
- K-Fold Cross Validation
- Stratified cross-validation

### 2.4 Overfitting and Underfitting
- **Overfitting**: High training accuracy, low test accuracy (high variance)
- **Underfitting**: Low training accuracy, low test accuracy (high bias)
- Regularization: L1 (Lasso), L2 (Ridge)
- Dropout (for neural networks)

### 2.5 Bias-Variance Tradeoff
- Total Error = Bias² + Variance + Irreducible Noise
- Low bias + low variance = ideal model

### 2.6 Evaluation Metrics
- **Confusion Matrix**: TP, TN, FP, FN
- **Accuracy**: (TP + TN) / Total
- **Precision**: TP / (TP + FP)
- **Recall (Sensitivity)**: TP / (TP + FN)
- **F1-Score**: 2 × (Precision × Recall) / (Precision + Recall)
- **ROC-AUC**: Receiver Operating Characteristic - Area Under Curve
- **MAE, MSE, RMSE, R²** for regression

---

## Unit 3: Supervised Learning (10 hrs)

### 3.1 Linear Regression
- Simple and multiple linear regression
- Ordinary Least Squares (OLS)
- Cost function (MSE), Gradient Descent
- Assumptions: Linearity, Independence, Homoscedasticity, Normality

### 3.2 Logistic Regression
- Binary classification using sigmoid function
- Log-odds, Maximum Likelihood Estimation
- Decision boundary

### 3.3 Decision Trees
- ID3, C4.5, CART algorithms
- Entropy, Information Gain, Gini Impurity
- Pruning: Pre-pruning, Post-pruning

### 3.4 Random Forest
- Ensemble method: Bagging + Random feature selection
- OOB (Out-of-Bag) error
- Feature importance

### 3.5 Support Vector Machine (SVM)
- Maximum margin hyperplane
- Support vectors, kernel trick
- Kernels: Linear, RBF (Gaussian), Polynomial
- Hard margin vs. Soft margin (C parameter)

### 3.6 K-Nearest Neighbors (KNN)
- Instance-based, lazy learner
- Distance metrics: Euclidean, Manhattan, Minkowski
- Choosing K (Elbow method)

### 3.7 Naive Bayes
- Bayes' Theorem: P(A|B) = P(B|A)·P(A) / P(B)
- Types: Gaussian, Multinomial, Bernoulli
- Independence assumption

---

## Unit 4: Unsupervised Learning & Neural Networks (10 hrs)

### 4.1 K-Means Clustering
- Algorithm: Initialize → Assign → Update centroids → Repeat
- Choosing K: Elbow method, Silhouette score
- Limitations: Sensitive to outliers, requires K, assumes spherical clusters

### 4.2 Hierarchical Clustering
- Agglomerative (bottom-up) vs. Divisive (top-down)
- Linkage methods: Single, Complete, Average, Ward
- Dendrogram interpretation

### 4.3 Dimensionality Reduction - PCA
- Principal Component Analysis: Eigenvectors of covariance matrix
- Explained variance ratio
- Use: Visualization, noise reduction, computational efficiency

### 4.4 Introduction to Neural Networks
- Biological neuron analogy
- **Perceptron**: Inputs → Weights → Activation → Output
- Multi-Layer Perceptron (MLP)
- Input layer, Hidden layers, Output layer

### 4.5 Activation Functions
- Step function, Sigmoid, Tanh
- **ReLU** (Rectified Linear Unit): max(0, x) - most common
- Leaky ReLU, Softmax (for multiclass output)

### 4.6 Backpropagation
- Forward pass: Compute output
- Compute loss (Cross-entropy, MSE)
- Backward pass: Chain rule for gradients
- Update weights: w = w - η·∂L/∂w

---

## Unit 5: Deep Learning & Applications (12 hrs)

### 5.1 Introduction to Deep Learning
- Deep networks vs. shallow networks
- Why deep learning works: Feature hierarchy
- Challenges: Vanishing gradient, computational cost

### 5.2 Convolutional Neural Networks (CNN)
- Convolution operation, kernels/filters
- Pooling (Max, Average), Stride, Padding
- Architecture: Conv → Pool → FC → Output
- Applications: Image classification, Object detection

### 5.3 Recurrent Neural Networks (RNN)
- Sequential data, hidden state
- Vanishing gradient problem
- **LSTM** (Long Short-Term Memory): Forget, Input, Output gates
- **GRU** (Gated Recurrent Unit)
- Applications: Text generation, Speech recognition, Time series

### 5.4 NLP Basics
- Tokenization, Stop words, Stemming/Lemmatization
- Bag of Words (BoW), TF-IDF
- Word Embeddings: Word2Vec, GloVe

### 5.5 Computer Vision Applications
- Image classification, Object detection (YOLO, R-CNN)
- Semantic segmentation
- Face recognition, OCR

### 5.6 Practical: Python Libraries
- **NumPy**: Arrays, broadcasting, linear algebra
- **Pandas**: DataFrames, groupby, merge
- **Scikit-learn**: Pipeline, train_test_split, model evaluation
- **TensorFlow/Keras**: Sequential model, layers, compile, fit, evaluate

---

## Unit-wise Hours Distribution

| Unit | Title | Hours |
|------|-------|-------|
| 1 | Introduction to AI | 8 |
| 2 | ML Fundamentals | 8 |
| 3 | Supervised Learning | 10 |
| 4 | Unsupervised Learning & Neural Networks | 10 |
| 5 | Deep Learning & Applications | 12 |
| **Total** | | **48** |

---

## Text Books
1. *Artificial Intelligence: A Modern Approach*, 4th Ed - Russell & Norvig
2. *Hands-On Machine Learning* - Aurélien Géron (O'Reilly)
3. *Deep Learning* - Goodfellow, Bengio, Courville (MIT Press)

## Reference Books
1. *Pattern Recognition and Machine Learning* - Bishop
2. *Machine Learning* - Tom Mitchell
3. *Python Machine Learning* - Sebastian Raschka

---

← [[Overview]] | [[Unit-1]] →
