---
title: "CS-308 Viva 1"
---

[[CS-308-Assignment-1|Back to Assignment 1]]

## 5. Viva Questions
1. **What is a DataFrame in Pandas?**
   - A DataFrame is a 2D labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table.
2. **How do you handle missing values in a dataset?**
   - By using `dropna()` to remove missing values or `fillna()` to impute them with mean, median, or mode.
3. **What is the difference between mean and median imputation?**
   - Mean is the average and is sensitive to outliers. Median is the middle value and is more robust against outliers.
4. **How can you filter rows in a Pandas DataFrame based on a condition?**
   - By using boolean indexing, e.g., `df[df['Age'] > 25]`.
5. **What is the purpose of the `axis` parameter in Pandas?**
   - `axis=0` refers to operations across rows, and `axis=1` refers to operations across columns.