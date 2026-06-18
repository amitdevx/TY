---
tags: [data-science, lab, assignment, clustering, unsupervised]
title: Assignment 6 - Unsupervised ML
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 6: Unsupervised Machine Learning (Clustering)

## 1. Problem Statement / Aim
**Aim:** To apply unsupervised learning techniques, specifically K-Means clustering, to discover hidden patterns or groupings in an unlabelled dataset, and to use the Elbow method to find the optimal number of clusters.

## 2. Theory & Concept
**Unsupervised Learning** models find hidden patterns or intrinsic structures in input data without labels.
- **Clustering**: Grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups.
- **K-Means Clustering**: A partition-based algorithm that divides data into $K$ non-overlapping subsets (clusters) based on the distance to the centroid of the cluster.
- **Elbow Method**: A heuristic used in determining the number of clusters in a data set. It plots the explained variation (WCSS - Within-Cluster Sum of Squares) as a function of the number of clusters.

## 3. Fully Solved Python Code
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 1. Generate Synthetic Unlabelled Data
# 300 samples, 4 centers (clusters)
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# 2. Elbow Method to find optimal K
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(range(1, 11), wcss, marker='o')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters (K)')
plt.ylabel('WCSS')

# 3. Apply K-Means with optimal K (which is 4)
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# 4. Visualization of Clusters
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title('K-Means Clustering (K=4)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()
```

## 4. Expected Output
- A window displaying a 1x2 grid of plots.
- **Plot 1**: A line graph (Elbow curve) showing WCSS decreasing rapidly and forming an "elbow" at K=4.
- **Plot 2**: A scatter plot where data points are colored according to 4 distinct clusters, with red 'X' markers indicating the centroid of each cluster.