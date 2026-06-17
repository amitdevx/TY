---
title: "CS-321 AI/ML - Interview Preparation (40+ Questions)"
subject: CS-321-VSC-P
type: interview-prep
semester: V
university: SPPU
tags:
  - artificial-intelligence
  - machine-learning
  - deep-learning
  - interview-prep
  - CS-321
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-321: Foundation of AI & ML - Interview Preparation

> [!important] 40+ Interview Questions
> Covers AI fundamentals, all ML algorithms, deep learning, and practical Python. Ideal for campus placements, internships, and academic exams.

---

## Section 1: AI Fundamentals (Q1–Q6)

> [!question] Q1: What is Artificial Intelligence? What are the different types?
> **Answer**: AI is the simulation of human intelligence processes by machines, especially computer systems. Processes include: learning, reasoning, problem-solving, perception, and language understanding.
> **Types**: 
> - **ANI (Narrow AI)**: Specific task - Siri, chess engines, image recognition
> - **AGI (General AI)**: Human-level general intelligence - theoretical
> - **ASI (Super AI)**: Surpasses human intelligence - theoretical
> Also: Reactive, Limited Memory, Theory of Mind, Self-Aware (Arend Hintze's classification)

> [!question] Q2: What is the Turing Test? Why is it controversial?
> **Answer**: The Turing Test (1950) proposes that if a machine can hold a conversation indistinguishable from a human, it can be considered intelligent. **Controversies**: (1) John Searle's Chinese Room: Symbol manipulation ≠ understanding. A program can fake conversation without "thinking." (2) ELIZA Effect: Humans anthropomorphize simple programs. (3) Measures behavior, not intelligence. (4) A program optimized to pass the Turing Test (deceptive responses) isn't necessarily intelligent.

> [!question] Q3: Explain BFS vs DFS. Which would you use for shortest path?
> **Answer**: 
> - **BFS**: Queue (FIFO), explores level by level, guaranteed shortest path (if uniform costs), high memory O(b^d)
> - **DFS**: Stack (LIFO), goes deep first, not optimal, low memory O(b·m)
> For **shortest path** → BFS (or Dijkstra's for weighted, A* for heuristic). DFS for: when any solution is acceptable, memory-constrained, deep search spaces (maze solving), topological sort.

> [!question] Q4: What is A* and why is it better than BFS and Dijkstra's?
> **Answer**: A* uses f(n) = g(n) + h(n) where g(n) is the actual cost and h(n) is an admissible heuristic estimate. It's better than BFS (which assumes uniform costs) and Dijkstra's (which has no heuristic). A*: Complete + Optimal (with admissible h) + efficient (doesn't explore unpromising paths). BFS explores all directions; A* uses heuristic to focus toward the goal. Example: GPS navigation uses A* with straight-line distance as heuristic.

> [!question] Q5: What is First-Order Logic? Give examples.
> **Answer**: FOL (Predicate Logic) extends propositional logic with predicates, variables, and quantifiers. Components: Objects (John, 5), Predicates (IsStudent(x), Loves(x,y)), Functions (FatherOf(x)), Quantifiers: ∀ (for all), ∃ (there exists).
> **Examples**:
> - All students are humans: ∀x [Student(x) → Human(x)]
> - There exists a genius student: ∃x [Student(x) ∧ Genius(x)]
> - Everyone loves someone: ∀x ∃y Loves(x,y)
> - Modus Ponens: {P, P→Q} ⊢ Q

> [!question] Q6: What is Hill Climbing? What are its limitations?
> **Answer**: Hill Climbing is a local search algorithm that moves from current state to the best neighboring state (always moving uphill). Variants: Steepest Ascent (best of all neighbors), First-Choice (first better neighbor), Stochastic (random better neighbor).
> **Limitations**: (1) **Local maxima**: Stops at local peak, not global; (2) **Plateaux**: Flat area, no improvement → stuck; (3) **Ridges**: Sequence of local maxima with narrow path → oscillation.
> **Fix**: Random Restart Hill Climbing - restart from multiple random positions, take best solution.

---

## Section 2: ML Fundamentals (Q7–Q15)

> [!question] Q7: What is machine learning? How does it differ from rule-based programming?
> **Answer**: ML is a paradigm where algorithms learn patterns from data without explicit programming. **Rule-based**: Human experts write explicit IF-THEN rules (brittle, hard to maintain). **ML**: System learns rules from data automatically (adaptable, scalable). Example: Rule-based spam filter has hand-crafted rules; ML spam filter learns from labeled emails. ML excels when: rules are too complex, data is abundant, patterns change over time.

> [!question] Q8: Explain the Bias-Variance Tradeoff in detail.
> **Answer**: 
> **Bias**: Error from wrong assumptions → Underfitting. Model too simple, misses real patterns. High bias = poor training AND test performance.
> **Variance**: Error from sensitivity to training data → Overfitting. Model memorizes training data, doesn't generalize. High variance = great training, poor test performance.
> **Total Error = Bias² + Variance + Irreducible Noise**
> **Tradeoff**: As model complexity increases, bias decreases but variance increases. Goal: Find model complexity that minimizes total error.
> **Remedies**: Overfitting → Regularization, dropout, more data, simpler model. Underfitting → More features, more complex model, less regularization.

> [!question] Q9: What is cross-validation and why is it needed?
> **Answer**: Cross-validation (CV) provides a reliable estimate of model generalization performance. K-Fold CV: Divide data into K folds; train on K-1, test on 1; rotate; average K scores. **Why needed**: Single train-test split can be lucky/unlucky (high variance estimate). CV uses all data for both training and testing, gives more stable performance estimate. Essential for: hyperparameter tuning, model selection, small datasets. Stratified K-Fold: Preserves class ratio in each fold - crucial for imbalanced datasets.

> [!question] Q10: Explain all evaluation metrics for classification: Accuracy, Precision, Recall, F1, AUC-ROC.
> **Answer**:
> - **Accuracy** = (TP+TN)/Total: % correct predictions. Misleading for imbalanced data (95% negative class → predict all negative = 95% accuracy!)
> - **Precision** = TP/(TP+FP): Of predicted positives, % actually positive. High when FP is costly.
> - **Recall** = TP/(TP+FN): Of actual positives, % correctly detected. High when FN is costly.
> - **F1** = 2PR/(P+R): Harmonic mean of Precision and Recall. Use for imbalanced classes.
> - **AUC-ROC**: Area under ROC curve (TPR vs FPR). 0.5=random, 1.0=perfect. Threshold-independent. Best when you need to compare models across all thresholds.

> [!question] Q11: What is L1 vs L2 regularization? Which produces sparse models?
> **Answer**:
> - **L1 (Lasso)**: Adds λΣ|θj| to loss. Drives some coefficients to exactly zero → sparse model → feature selection! The L1 ball has corners at axes, so optimization tends to hit corners (zero values).
> - **L2 (Ridge)**: Adds λΣθj² to loss. Shrinks all coefficients toward zero (but rarely exactly zero). The L2 ball is smooth, gradient pushes toward zero but not exactly.
> - **Elastic Net**: α×L1 + (1-α)×L2 - best of both.
> Use L1 when: many irrelevant features, need interpretable sparse model. Use L2 when: all features are relevant, correlated features.

> [!question] Q12: What is overfitting? How do you diagnose and fix it?
> **Answer**: Overfitting: Model performs well on training data but poorly on new data. It has memorized training data including noise.
> **Diagnosis**: Large gap between training accuracy (high) and validation accuracy (low). Learning curves diverge.
> **Fixes**: (1) Regularization (L1/L2/Dropout); (2) More training data; (3) Feature selection (less features); (4) Simpler model (reduce layers, depth); (5) Cross-validation; (6) Ensemble methods (Random Forest, Gradient Boosting); (7) Early stopping (track val_loss); (8) Data augmentation (for images).

> [!question] Q13: What is the difference between model parameters and hyperparameters?
> **Answer**:
> - **Parameters**: Learned from data during training. E.g., weights (w) and biases (b) in neural networks, β coefficients in linear regression. Model automatically optimizes these.
> - **Hyperparameters**: Set before training, not learned from data. E.g., learning rate, number of trees, K in KNN, number of layers, regularization strength λ. Tuned via cross-validation (GridSearchCV, RandomSearchCV, Optuna).

> [!question] Q14: Explain the ROC curve and AUC. When is AUC better than Accuracy?
> **Answer**: **ROC** (Receiver Operating Characteristic) plots True Positive Rate (Recall) vs False Positive Rate at various classification thresholds (from 0 to 1). **AUC** = Area under ROC = single number summary. AUC=0.5 means random classifier; AUC=1.0 is perfect.
> **AUC better than Accuracy when**: (1) Imbalanced datasets - predicting all majority class gives high accuracy but AUC=0.5; (2) When you need to compare model ability to discriminate, not just performance at default threshold; (3) When optimal threshold isn't known at model design time.

> [!question] Q15: What is the difference between regression and classification?
> **Answer**:
> - **Regression**: Predicts continuous numerical value. Output ∈ (-∞, +∞). Examples: house price, temperature. Loss: MSE, MAE. Metrics: R², RMSE.
> - **Classification**: Predicts discrete class label. Binary (spam/not spam), Multi-class (0-9 digits), Multi-label (image tags). Loss: Cross-entropy. Metrics: Accuracy, F1, AUC.
> Some algorithms handle both (Decision Trees, Neural Networks, SVM). Some are specific (Linear Regression, Logistic Regression).

---

## Section 3: Supervised Learning Algorithms (Q16–Q25)

> [!question] Q16: Explain Linear Regression. What are its assumptions?
> **Answer**: Linear Regression models linear relationship between features and continuous target: ŷ = β₀ + β₁x₁ + ... + βₙxₙ. Coefficients found by OLS (minimizing MSE) or gradient descent.
> **Assumptions (LINE)**: (1) **L**inearity: Relationship between X and y is linear; (2) **I**ndependence: Observations are independent; (3) **N**ormality: Residuals are normally distributed; (4) **E**qual variance (Homoscedasticity): Residuals have constant variance across fitted values. Violations reduce reliability of inference.

> [!question] Q17: What is Logistic Regression? Why is it called regression if it's classification?
> **Answer**: Logistic Regression applies the sigmoid function to linear regression output, producing probabilities for binary classification: P(y=1|X) = σ(β₀ + β₁x) = 1/(1+e^(-z)). Named "regression" because it models the log-odds linearly. Decision: predict class 1 if P ≥ 0.5. Trained by maximizing likelihood (minimizing log-loss/cross-entropy). Assumptions: Binary target, no multicollinearity, independent observations. It's a **linear classifier** - linear decision boundary in feature space.

> [!question] Q18: How does a Decision Tree choose the best split?
> **Answer**: Decision Tree evaluates all possible splits on all features and chooses the one that maximizes **Information Gain** (ID3) or minimizes **Gini Impurity** (CART).
> - Entropy: H(S) = -Σpᵢlog₂(pᵢ). Pure node: H=0. Equal split: H=1.
> - IG(S, A) = H(S) - Σ(|Sv|/|S|)H(Sv)
> - Gini: 1 - Σpᵢ². Pure: 0. Equal: 0.5.
> The split that maximizes IG (or minimizes Gini) is chosen. Greedy algorithm - locally optimal at each node.

> [!question] Q19: What is Random Forest? How does it reduce overfitting?
> **Answer**: Random Forest is an ensemble of Decision Trees trained using Bagging + Random feature selection.
> **Bagging**: Each tree trained on a random bootstrap sample (sampling with replacement). **Random features**: At each split, only √n features are considered (not all). This decorrelates trees.
> **Reduces overfitting**: Single trees overfit (high variance). Averaging many diverse trees reduces variance significantly while keeping bias low. OOB (out-of-bag) samples provide internal validation without separate test set.

> [!question] Q20: Explain SVM. What is the kernel trick?
> **Answer**: SVM finds the hyperplane that maximizes the margin between classes. Support vectors are the training points closest to the hyperplane. Hard margin (linearly separable): minimize ‖w‖² subject to yᵢ(w·xᵢ+b)≥1. Soft margin (C parameter): allows misclassifications.
> **Kernel Trick**: When data is not linearly separable in original space, kernels implicitly map data to higher-dimensional space where it is separable. Instead of computing the transformation φ(x) (expensive), the kernel K(x,z) = φ(x)·φ(z) computes the inner product directly. Common kernels: RBF = exp(-γ||x-z||²), Polynomial = (x·z+c)^d.

> [!question] Q21: Why does SVM require feature scaling?
> **Answer**: SVM tries to maximize the margin measured by Euclidean distance in feature space. If one feature has values 0-1000 and another 0-1, the distance is dominated by the first feature. The hyperplane will be biased toward the large-scale feature. Scaling ensures all features contribute equally to the distance metric. Similarly for KNN and any distance-based algorithm.

> [!question] Q22: What is KNN? How does it differ from other algorithms?
> **Answer**: KNN (K-Nearest Neighbors) is a lazy, non-parametric, instance-based learner. No training phase - stores all training data. For prediction: compute distance to all training points, find K nearest, take majority vote (classification) or mean (regression). **Differences**: (1) No model learned (stores data); (2) Computation at prediction time, not training; (3) Non-parametric (no assumptions about data distribution); (4) Locally adaptive (decision boundary adapts to local structure). **Drawbacks**: Slow prediction O(n·d), sensitive to irrelevant features, requires scaling, large memory.

> [!question] Q23: What is Naive Bayes? When does it fail?
> **Answer**: Naive Bayes uses Bayes' theorem with the "naive" conditional independence assumption: P(C|x₁,...,xₙ) ∝ P(C)∏P(xᵢ|C). Fast training, good for high dimensions, works well with small data.
> **Failures**: When features are highly correlated (violates independence assumption). Example: In text classification, "New York" - "New" and "York" are not independent. Despite this, NB often works surprisingly well in practice. Types: Gaussian (continuous), Multinomial (word counts), Bernoulli (binary features).

> [!question] Q24: Gradient Descent - explain variants.
> **Answer**:
> - **Batch GD**: Compute gradient on ENTIRE dataset. Stable but slow for large data.
> - **Stochastic GD (SGD)**: Compute gradient on ONE sample. Fast, noisy, can escape local minima.
> - **Mini-batch GD**: Compute gradient on small batch (32/64/128). Best of both worlds. Default in deep learning.
> Update: W = W - η·∇L. Learning rate η: Too large → overshoot; Too small → slow convergence. Adaptive: Adam, RMSprop, Adagrad adjust learning rate per parameter.

> [!question] Q25: What is the difference between Bagging and Boosting?
> **Answer**:
> - **Bagging** (Bootstrap Aggregating): Train models independently on random data subsets. Combine by voting/averaging. Reduces **variance**. Example: Random Forest.
> - **Boosting**: Train models sequentially. Each model focuses on errors of previous. Weighted combination. Reduces **bias** and **variance**. Example: AdaBoost, Gradient Boosting, XGBoost.
> Bagging: parallel training, simpler. Boosting: sequential, more powerful but prone to overfitting noisy data.

---

## Section 4: Unsupervised Learning (Q26–Q30)

> [!question] Q26: Explain K-Means. What are its limitations and how to overcome them?
> **Answer**: K-Means: Initialize K centroids → Assign points to nearest centroid → Recompute centroids → Repeat. Minimizes WCSS.
> **Limitations**: (1) K must be specified → Use Elbow/Silhouette; (2) Sensitive to initialization → K-Means++ initialization; (3) Assumes spherical, equal-size clusters → Use DBSCAN for arbitrary shapes; (4) Sensitive to outliers → Use K-Medoids; (5) Stuck in local optima → Multiple restarts (n_init=10); (6) Only numerical → Encode categorical.

> [!question] Q27: What is PCA? When should you use it?
> **Answer**: PCA finds orthogonal axes (principal components) that capture maximum variance. It projects data onto fewer dimensions while preserving most information. Process: Standardize → Covariance matrix → Eigendecomposition → Sort by eigenvalue → Project.
> **Use when**: (1) High-dimensional data (visualization in 2D/3D); (2) Multicollinearity in features; (3) Speed up training (fewer features); (4) Noise reduction. **Don't use when**: Interpretability required (PCs are abstract combinations), feature selection needed (PCA transforms, not selects), data is non-linear (use t-SNE, UMAP instead).

> [!question] Q28: What is the Silhouette Score? How do you interpret it?
> **Answer**: Silhouette score measures how well each point fits its assigned cluster vs. other clusters.
> $$s = \frac{b - a}{\max(a, b)}$$
> where a = mean intra-cluster distance (same cluster), b = mean distance to nearest other cluster.
> Range [-1, 1]: +1 = perfectly in own cluster, 0 = on boundary, -1 = probably in wrong cluster.
> Use average silhouette score across all points to choose optimal K (higher is better).

> [!question] Q29: What is the difference between K-Means and Hierarchical clustering?
> **Answer**: 
> K-Means: iterative, must specify K, stochastic (random init), scalable O(n·K·d·i), assumes spherical clusters, produces flat partition.
> Hierarchical: deterministic, no K needed, O(n²) or O(n³) space, flexible cluster shapes, produces dendrogram (tree), choose K by "cutting" dendrogram.
> When to use: K-Means for large datasets with known K; Hierarchical when K unknown, small dataset, or hierarchical structure of interest.

> [!question] Q30: What is dimensionality reduction? Why is it needed?
> **Answer**: Dimensionality reduction reduces the number of features (dimensions) while preserving important information. **Needed because**: (1) Curse of dimensionality (distances meaningless in high-D); (2) Visualization (can't plot >3D); (3) Computational efficiency; (4) Remove noise/redundancy; (5) Prevent overfitting. **Methods**: PCA (linear, preserves variance), t-SNE (non-linear, preserves local structure, for visualization), UMAP (non-linear, faster than t-SNE), Autoencoders (neural network-based).

---

## Section 5: Deep Learning (Q31–Q40)

> [!question] Q31: What is deep learning? Why does it work well for images and text?
> **Answer**: Deep Learning uses neural networks with many layers to automatically learn hierarchical feature representations. For images: early layers learn edges/textures, middle layers learn parts (eyes, noses), deep layers learn objects (faces). This hierarchical representation is hard to engineer manually. For text: layers learn characters → words → phrases → sentences → semantics. Deep learning removes the need for manual feature engineering that traditional ML requires.

> [!question] Q32: Explain CNN architecture in detail.
> **Answer**: CNN architecture for image classification:
> 1. **Input**: Image (H×W×C channels)
> 2. **Conv layer**: Filters slide over input, computing dot products → feature maps. Learns local patterns.
> 3. **BatchNorm**: Normalize activations → stable training
> 4. **Activation (ReLU)**: Introduce non-linearity
> 5. **Pooling (Max/Avg)**: Reduce spatial dimensions, translation invariance
> 6. **Dropout**: Randomly zero neurons → regularization
> 7. Repeat Conv-Pool blocks
> 8. **Flatten**: Convert feature maps to 1D vector
> 9. **Dense layers**: Classification
> 10. **Softmax**: Class probabilities
> Output size: O = (I - K + 2P)/S + 1

> [!question] Q33: What is the difference between pooling types in CNNs?
> **Answer**:
> - **Max Pooling**: Takes maximum value in window. Detects presence of features, translation invariant, more information loss. Most common in classification.
> - **Average Pooling**: Takes mean of window. Smoother representation, good for backgrounds. Used in Global Average Pooling (GAP) at the end.
> - **Global Average Pooling**: Reduces entire feature map to single value per channel. Replaces flattening + dense layers, fewer parameters, less overfitting. Used in modern architectures.
> Max pooling is preferred in classification. Average pooling in detection and segmentation.

> [!question] Q34: What is the vanishing gradient problem? How is it solved?
> **Answer**: In deep networks, during backpropagation, gradients are multiplied through layers using the chain rule. Sigmoid and Tanh saturate (gradient ≈ 0) for large inputs. Multiplying many small gradients → gradient → 0 in early layers → early layers learn very slowly.
> **Solutions**: (1) **ReLU**: Gradient = 1 for positive inputs, no saturation; (2) **Residual connections** (ResNet): Skip connections allow gradients to flow directly; (3) **Batch Normalization**: Keeps activations in good range; (4) **Better initialization** (Xavier, He); (5) **Gradient clipping**: Cap gradient magnitude.

> [!question] Q35: Explain LSTM and its gates.
> **Answer**: LSTM (Long Short-Term Memory) solves vanishing gradient in RNNs using a cell state (Ct) that acts as long-term memory.
> - **Forget Gate**: $f_t = \sigma(W_f[h_{t-1}, x_t])$ - Controls what to forget from cell state
> - **Input Gate**: $i_t = \sigma(W_i[h_{t-1}, x_t])$ - Controls what new information to store
> - **Candidate**: $\tilde{C}_t = \tanh(W_C[h_{t-1}, x_t])$ - Candidate values
> - **Cell State Update**: $C_t = f_t \cdot C_{t-1} + i_t \cdot \tilde{C}_t$ - Additive update (not multiplicative → no vanishing!)
> - **Output Gate**: $o_t = \sigma(W_o[h_{t-1}, x_t])$ - Controls output
> - **Hidden State**: $h_t = o_t \cdot \tanh(C_t)$
> The key insight: Cell state uses **addition** to update, allowing gradients to flow unchanged over long sequences.

> [!question] Q36: What is Transfer Learning? Give practical examples.
> **Answer**: Transfer learning reuses a model trained on a large source task for a different but related target task. Process: Take pre-trained model (e.g., VGG16 on ImageNet) → Freeze early layers (general features) → Replace final layers → Fine-tune on target data.
> **Examples**: (1) VGG16/ResNet for medical image classification (small dataset); (2) BERT for sentiment analysis (trained on Wikipedia); (3) ImageNet weights for aerial image detection. **Why it works**: Early layers of any image network learn universal features (edges, textures). Fine-tuning only teaches task-specific patterns.

> [!question] Q37: What is Batch Normalization? Why is it effective?
> **Answer**: Batch Normalization normalizes each layer's inputs to mean=0, std=1 (then applies learnable scale/shift). Benefits: (1) Reduces **internal covariate shift** (distribution of layer inputs keeps changing during training); (2) Allows higher learning rates → faster training; (3) Acts as regularizer (reduces need for dropout); (4) Reduces sensitivity to initialization. Applied before activation function (Conv → BatchNorm → ReLU). During inference: uses running statistics from training.

> [!question] Q38: What is Dropout? How does it prevent overfitting?
> **Answer**: Dropout randomly deactivates neurons with probability p (e.g., 0.5) during each training step. At test time: all neurons are active, outputs scaled by (1-p). **Why it works**: (1) Forces network to learn redundant representations (each neuron can't rely on specific others); (2) Equivalent to training and averaging 2^n different networks; (3) Prevents co-adaptation of neurons. Applied AFTER activation function. Not used in BatchNorm layers (they complement each other).

> [!question] Q39: Compare BoW, TF-IDF, and Word Embeddings.
> **Answer**:
> - **BoW**: Count of each word. Simple, sparse (vocab size), no semantics, no order.
> - **TF-IDF**: TF×IDF. Weights important words, sparse, no semantics, no order. Better than BoW.
> - **Word Embeddings (Word2Vec, GloVe)**: Dense (100-300 dim), semantic similarity (king-man+woman≈queen), handles analogies. Learned from context. Requires pre-training or loading pre-trained vectors.
> For classical ML (SVM, NB): TF-IDF. For deep learning (LSTM, Transformer): Word embeddings.

> [!question] Q40: What are the practical steps to build a deep learning model?
> **Answer**:
> 1. **Problem framing**: Classification, regression, sequence?
> 2. **Data preparation**: Normalize, augment (images), tokenize (text), split train/val/test
> 3. **Architecture design**: Choose CNN/RNN/Transformer; depth, width, activation
> 4. **Loss function**: Categorical cross-entropy (multiclass), Binary CE (binary), MSE (regression)
> 5. **Optimizer**: Adam (default), SGD with momentum
> 6. **Regularization**: Dropout, BatchNorm, L2, EarlyStopping
> 7. **Training**: Monitor train/val loss, use callbacks (EarlyStopping, ReduceLROnPlateau)
> 8. **Evaluation**: Evaluate on held-out test set
> 9. **Iterate**: Diagnose (over/underfit?) → adjust architecture, data, regularization

---

## Quick Answer Cheatsheet

| Question | One-Line Answer |
|----------|----------------|
| Bias vs Variance | Bias=underfitting, Variance=overfitting |
| L1 vs L2 | L1=sparse (feature selection), L2=weight shrink |
| BFS vs DFS | BFS=optimal+complete, DFS=memory efficient |
| A* formula | f(n) = g(n) + h(n) |
| Admissible heuristic | Never overestimates actual cost |
| F1 formula | 2PR/(P+R) |
| Use Precision when | FP costly (spam filter) |
| Use Recall when | FN costly (cancer detection) |
| SVM C parameter | Small=soft margin, Large=hard margin |
| KNN lazy learner | No training, classify at prediction time |
| Naive assumption | Features conditionally independent given class |
| Gini impurity | 1 - Σpi² |
| Entropy | -Σpi·log₂(pi) |
| WCSS | Σ||xi - μj||² |
| Elbow method | K where inertia reduction slows |
| PCA | Eigenvectors of covariance matrix |
| Vanishing gradient fix | ReLU, ResNet, BatchNorm |
| LSTM key idea | Additive cell state update (not multiplicative) |
| LSTM gates | Forget + Input + Output |
| CNN output size | (I-K+2P)/S + 1 |
| Transfer learning | Pre-trained model + custom head |
| BatchNorm benefit | Stable training, higher LR, regularization |
| Dropout | Random deactivation prevents co-adaptation |
| TF-IDF vs Embeddings | Sparse/no-semantics vs Dense/semantic |

---

← [[Revision]] | [[Overview]] →

#AI #machine-learning #interview-prep #deep-learning #SPPU #semester-5
