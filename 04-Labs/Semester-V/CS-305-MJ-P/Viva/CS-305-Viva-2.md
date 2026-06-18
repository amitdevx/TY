---
title: "CS-305 Viva 2"
---

[[CS-305-Assignment-2|Back to Assignment 2]]

## 5. Viva Questions
1. **Define Turnaround Time and Waiting Time.**
   - Turnaround Time: The interval from the time of submission of a process to the time of completion.
   - Waiting Time: The sum of the periods spent waiting in the ready queue.
2. **Which scheduling algorithm provides the minimum average waiting time?**
   Shortest Job First (SJF) is provably optimal, giving the minimum average waiting time for a given set of processes.
3. **What is the Convoy Effect?**
   It occurs in FCFS when many short processes wait for one long process to release the CPU, leading to lower CPU and device utilization.
4. **What is Time Quantum in Round Robin?**
   It is a small unit of time (e.g., 10 to 100 milliseconds) allocated to each process in the ready queue before preempting it.
5. **What is starvation and how can it be avoided?**
   Starvation is when low-priority processes wait indefinitely because the CPU is always occupied by high-priority processes. It can be solved by *aging*, which gradually increases the priority of long-waiting processes.