---
title: "CS-321 AI/ML - Revision Notes"
subject: CS-321-VSC-P
type: revision
semester: V
university: SPPU
tags:
  - artificial-intelligence
  - machine-learning
  - revision
  - exam-prep
  - CS-321
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-321: Foundation of AI & ML - Rapid Revision

> [!tip] How to Use
> Read all sections 48 hours before exam. Know every formula, comparison table, and Python snippet below.

---

## Unit 1: Introduction to AI

> [!summary] Must Know

**AI History Key Dates:**
- 1950: Turing Test
- 1956: Dartmouth Conference → "AI" coined by McCarthy
- 1997: Deep Blue beats Kasparov (chess)
- 2012: AlexNet → Deep Learning revolution
- 2022: ChatGPT → LLM revolution

**Turing Test:** Machine passes if human interrogator can't distinguish between machine and human through text. Criticism: Searle's Chinese Room - syntax ≠ semantics.

**Search Algorithm Comparison:**

| Property | BFS | DFS | A\* |
|----------|-----|-----|----|
| Data structure | Queue (FIFO) | Stack (LIFO) | Priority Queue |
| Complete |  |  |  |
| Optimal |  (uniform cost) |  |  (admissible h) |
| Time | O(b^d) | O(b^m) | O(b^d) |
| Space | O(b^d) - HIGH | O(b·m) - LOW | O(b^d) |

**A\* Formula:** $f(n) = g(n) + h(n)$
- g(n) = actual cost from start
- h(n) = heuristic estimate to goal
- Admissible: h(n) ≤ h*(n) (never overestimates)

**Hill Climbing Problems:**
1. Local maxima (stuck at local peak)
2. Plateaux (flat, no gradient)
3. Ridges (narrow diagonal)
Fix: Random restart hill climbing

**Logic:**
- Propositional: T/F statements, connectives (¬, ∧, ∨, →, ↔)
- First-Order: Predicates + Quantifiers (∀, ∃) + Functions
- Modus Ponens: P and P→Q → therefore Q

---

## Unit 2: ML Fundamentals

> [!summary] Must Know

**Types of ML:**
- **Supervised**: Labelled data → Regression + Classification
- **Unsupervised**: Unlabelled → Clustering + Association
- **Reinforcement**: Agent + Environment + Rewards

**Bias-Variance Tradeoff:**
$$\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}$$

| | Bias | Variance | Symptom |
|--|------|---------|---------|
| Underfitting | High | Low | Bad train AND test |
| Overfitting | Low | High | Good train, Bad test |
| Ideal | Low | Low | Good both |

**Confusion Matrix → Metrics:**

$$\text{Accuracy} = \frac{TP+TN}{Total}, \quad \text{Precision} = \frac{TP}{TP+FP}, \quad \text{Recall} = \frac{TP}{TP+FN}$$

$$F1 = \frac{2 \cdot P \cdot R}{P + R}, \quad FPR = \frac{FP}{FP+TN}, \quad TPR = Recall$$

**When to use:**
- Precision: When FP costly (spam filter)
- Recall: When FN costly (cancer detection)
- F1: Imbalanced classes
- AUC-ROC: Model ranking ability; 0.5 = random, 1.0 = perfect

**Regularization:**
- L1 (Lasso): $J + \lambda\sum|\theta_j|$ → Sparse (feature selection)
- L2 (Ridge): $J + \lambda\sum\theta_j^2$ → Weight shrinkage
- Always use stratified K-Fold for imbalanced data!

---

## Unit 3: Supervised Learning

> [!summary] Must Know Algorithms

**Linear Regression:**
- $\hat{y} = \beta_0 + \beta_1 x_1 + ... + \beta_n x_n$
- Cost: $MSE = \frac{1}{n}\sum(y_i - \hat{y}_i)^2$
- Assumptions: LINE (Linearity, Independence, Normality, Equal variance)

**Logistic Regression:**
- $\sigma(z) = \frac{1}{1+e^{-z}} \in (0,1)$
- Decision boundary: p ≥ 0.5 → Class 1
- Loss: Cross-entropy (log-loss)

**Decision Trees:**
- Entropy: $H = -\sum p_i\log_2(p_i)$ (0=pure, 1=max impurity)
- Gini: $1 - \sum p_i^2$ (0=pure, 0.5=max impurity)
- IG = H(parent) - Σ(weighted H(child))

**Random Forest:**
- Bagging + Random feature subsets (√n features)
- OOB score ≈ cross-validation score
- Feature importance automatically computed

**SVM:**
- Maximum margin hyperplane
- C: Regularization (small=soft margin, large=hard margin)
- Kernels: Linear, RBF (most common), Polynomial
- MUST scale features!

**KNN:**
- Lazy learner (no training)
- Euclidean: $\sqrt{\sum(p_i-q_i)^2}$
- Choose K: odd, ~√n, use cross-validation
- MUST scale features!

**Naive Bayes:**
- $P(C|X) \propto P(C) \cdot \prod P(x_i|C)$
- "Naive": assumes conditional independence
- Gaussian NB (continuous), Multinomial NB (text)

**Scale-sensitive algorithms**: Linear Regression, Logistic Regression, SVM, KNN, Neural Networks → MUST scale!
**Scale-invariant**: Decision Trees, Random Forest, Naive Bayes → scaling optional

---

## Unit 4: Unsupervised Learning & Neural Networks

> [!summary] Must Know

**K-Means:**
1. Initialize K centroids (K-Means++ is better)
2. Assign points to nearest centroid
3. Recompute centroids
4. Repeat until convergence

Objective: Minimize WCSS = $\sum_j\sum_{x_i\in C_j}|x_i-\mu_j|^2$

Choose K: **Elbow method** (inertia vs K) + **Silhouette score** (range [-1,1], higher=better)

**Hierarchical vs K-Means:**
| | K-Means | Hierarchical |
|--|---------|------------|
| K required? |  Yes |  No |
| Scalable? |  Yes |  O(n²) |
| Output | Partition | Dendrogram |
| Deterministic |  |  |

Best linkage: **Ward** (minimizes variance)

**PCA:**
1. Standardize data
2. Compute covariance matrix
3. Find eigenvectors/eigenvalues
4. Sort by eigenvalue (= explained variance)
5. Project data onto top K components

Scree plot: Choose K where cumulative variance ≥ 95%

**Neural Networks:**

Perceptron: $z = \mathbf{w}^T\mathbf{x} + b$, then apply activation f(z)

**Activation Functions:**
| Function | Formula | Use |
|----------|---------|-----|
| Sigmoid | $\frac{1}{1+e^{-z}}$ | Output (binary) |
| Softmax | $\frac{e^{z_i}}{\sum e^{z_j}}$ | Output (multiclass) |
| ReLU | max(0, z) | Hidden layers (best) |
| Tanh | tanh(z) | RNNs |

**Backpropagation:**
1. Forward pass → compute output
2. Compute loss (MSE or cross-entropy)
3. Backward pass (chain rule) → compute gradients
4. Update: $W = W - \alpha\frac{\partial L}{\partial W}$

**Vanishing gradient**: Sigmoid/Tanh → gradient → 0 in deep nets → Fix: ReLU

---

## Unit 5: Deep Learning & Applications

> [!summary] Must Know

**Why Deep Learning?** Big data + GPUs + Better algorithms (ReLU, BatchNorm) + Frameworks

**CNN Key Layers:**
- **Conv**: Filter slides over input, extracts local features
- **Pooling**: Reduces spatial dimensions (Max=keep max, Avg=keep mean)
- **FC (Dense)**: Final classification after flattening

Output size: $O = \lfloor\frac{I - K + 2P}{S}\rfloor + 1$

CNN order: Conv → BatchNorm → ReLU → Pool → Dropout → ... → Flatten → Dense → Softmax

**RNN:**
- Sequential data, hidden state h_t
- Vanishing gradient for long sequences

**LSTM Gates (fix vanishing gradient):**
- **Forget Gate**: $f_t = \sigma(W_f[h_{t-1}, x_t] + b_f)$ → What to forget
- **Input Gate**: $i_t = \sigma(W_i[h_{t-1}, x_t] + b_i)$ → What to add
- **Output Gate**: $o_t = \sigma(W_o[h_{t-1}, x_t] + b_o)$ → What to output
- Cell state $C_t$: Long-term memory (additive, not multiplicative → no vanishing!)

**NLP Pipeline:**
Text → Lowercase → Remove punctuation → Tokenize → Remove stop words → Stem/Lemmatize → Vectorize (BoW/TF-IDF/Embeddings)

**TF-IDF:** $TF(t,d) \times IDF(t) = \frac{count(t,d)}{total\_words(d)} \times \log\frac{N}{df(t)}$

**Keras Quick Reference:**
```python
# Sequential model
model = keras.Sequential([layers.Dense(64, activation='relu'),
                           layers.Dense(10, activation='softmax')])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)
model.evaluate(X_test, y_test)
```

---

## All Formulas in One Place

| Formula | Expression |
|---------|-----------|
| A\* | $f(n) = g(n) + h(n)$ |
| Accuracy | $(TP+TN)/Total$ |
| Precision | $TP/(TP+FP)$ |
| Recall | $TP/(TP+FN)$ |
| F1 | $2PR/(P+R)$ |
| Bias-Variance | $Error = Bias^2 + Variance + \epsilon$ |
| Sigmoid | $1/(1+e^{-z})$ |
| ReLU | $\max(0,z)$ |
| Entropy | $-\sum p_i\log_2 p_i$ |
| Gini | $1-\sum p_i^2$ |
| WCSS | $\sum_j\sum_{x\in C_j}|x-\mu_j|^2$ |
| Silhouette | $(b-a)/\max(a,b)$ |
| Bayes | $P(C|X) \propto P(C)\prod P(x_i|C)$ |
| CNN size | $\lfloor(I-K+2P)/S\rfloor+1$ |
| Weight update | $W = W - \alpha\nabla L$ |
| L2 Loss | $J + \lambda\sum\theta_j^2$ |

---

## Last-Hour Checklist

- [ ] BFS=Queue, DFS=Stack, A\*=PriorityQueue + f(n)=g(n)+h(n)
- [ ] A\* admissible heuristic → never overestimates
- [ ] Confusion matrix: TP, TN, FP, FN with all metric formulas
- [ ] Type I = False Positive; Type II = False Negative
- [ ] Bias²+Variance+Noise = Total Error
- [ ] L1=Lasso (sparse); L2=Ridge (shrink)
- [ ] K-Means: assign + update centroids; Elbow + Silhouette
- [ ] PCA: eigendecomposition of covariance matrix; scree plot
- [ ] ReLU solves vanishing gradient in hidden layers
- [ ] CNN output formula; LSTM has 3 gates
- [ ] TF-IDF: important words get high score; common words penalized

---

← [[Important-Questions]] | [[Interview-Prep]] →

#AI #machine-learning #revision #SPPU #semester-5
