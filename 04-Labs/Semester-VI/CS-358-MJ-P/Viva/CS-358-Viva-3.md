---
title: "CS-358 Viva 3"
---

[[CS-358-Assignment-3|Back to Assignment 3]]

## 5. Viva Questions for this Assignment
**Q1. Why is `RecyclerView` preferred over `ListView`?**
*Answer*: `RecyclerView` is more memory efficient because it recycles item views using the mandatory `ViewHolder` pattern. `ListView` creates new views continuously unless the developer manually implements recycling, which is error-prone.

**Q2. What is the role of the `LayoutManager` in `RecyclerView`?**
*Answer*: The LayoutManager dictates how the items are positioned and scrolled on the screen (e.g., vertically, horizontally, or in a grid).

**Q3. What does the `onCreateViewHolder` method do?**
*Answer*: It is called by the RecyclerView when it needs a new `ViewHolder` object to represent an item. It inflates the XML layout for a single row and returns it inside a new ViewHolder instance.

**Q4. What does the `onBindViewHolder` method do?**
*Answer*: It is called by the RecyclerView to display the data at the specified position. This method updates the contents of the `ViewHolder` to reflect the item at the given position.