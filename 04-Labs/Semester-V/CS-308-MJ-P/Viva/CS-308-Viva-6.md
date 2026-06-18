---
title: "CS-308 Viva 6"
---

[[CS-308-Assignment-6|Back to Assignment 6]]

## 5. Viva Questions
1. **What is Unsupervised Learning?**
   - It is a machine learning technique used to draw inferences from datasets consisting of input data without labeled responses.
2. **Explain K-Means Clustering.**
   - It aims to partition $N$ observations into $K$ clusters in which each observation belongs to the cluster with the nearest mean (centroid).
3. **What is the significance of the "Elbow Method"?**
   - It helps to identify the optimal number of clusters ($K$) by plotting the within-cluster sum of squares (WCSS) against $K$. The "elbow" point represents the optimal $K$ where adding more clusters doesn't significantly decrease WCSS.
4. **What does WCSS stand for?**
   - Within-Cluster Sum of Squares, which is the sum of squared distances between each point and the centroid of its assigned cluster.
5. **Can K-Means handle categorical variables?**
   - No, standard K-Means uses Euclidean distance, which requires numerical variables. (K-Modes or K-Prototypes can be used for categorical data).