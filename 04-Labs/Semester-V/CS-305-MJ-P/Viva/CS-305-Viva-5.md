---
title: "CS-305 Viva 5"
---

[[CS-305-Assignment-5|Back to Assignment 5]]

## 5. Viva Questions
1. **What is Contiguous Allocation?**
   It requires each file to occupy a set of contiguous addresses on the disk. It is easy to implement and provides excellent read performance.
2. **What is the main drawback of Contiguous Allocation?**
   External fragmentation. Over time, free space is broken into small chunks that might be too small to accommodate new files.
3. **How does Linked Allocation solve external fragmentation?**
   In linked allocation, file blocks can be scattered anywhere on the disk. Each block contains a pointer to the next block, so space is never wasted as long as there are free blocks available.
4. **Why is Indexed Allocation useful?**
   It supports direct (random) access effectively by storing all block pointers in an index block, unlike linked allocation where you have to traverse the list from the beginning to reach a specific block.
5. **What is FAT?**
   File Allocation Table (FAT) is a variation of linked allocation where the pointers are kept in a separate table in memory rather than within the disk blocks themselves.