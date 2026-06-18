---
title: "CS-305 Viva 3"
---

[[CS-305-Assignment-3|Back to Assignment 3]]

## 5. Viva Questions
1. **What is a page fault?**
   A page fault occurs when a program attempts to access a block of memory (a page) that is not currently stored in the physical memory (RAM).
2. **Which page replacement algorithm suffers from Belady's Anomaly?**
   FIFO (First-In-First-Out) page replacement algorithm.
3. **What is Belady's Anomaly?**
   It is a phenomenon where increasing the number of page frames allocated to a process can cause an increase in the number of page faults.
4. **How does LRU differ from FIFO?**
   FIFO replaces the oldest loaded page, ignoring its usage frequency. LRU replaces the page that has not been accessed for the longest time, considering recent usage history.
5. **Why is Optimal Page Replacement practically impossible?**
   Because the operating system cannot know the future memory access requests of a process beforehand. It is used primarily as a benchmark for evaluating other algorithms.