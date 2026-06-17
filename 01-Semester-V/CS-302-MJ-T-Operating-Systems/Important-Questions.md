---
title: CS-302 Operating Systems - Important Questions
subject_code: CS-302-MJ-T
subject_name: Operating Systems
tags:
  - cs-302
  - os
  - important-questions
  - exam-prep
  - semester-v
aliases:
  - OS Important Questions
  - CS-302 Question Bank
created: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]


# CS-302 Operating Systems - Important Questions

> [!important] Exam Strategy
> **External Exam: 35 Marks** | Focus heavily on **numericals** (Scheduling, Page Replacement, Banker's Algorithm, Disk Scheduling). Theory + examples = full marks!

---

## Unit 1 - Introduction to OS

### Short Answer (2 Marks)

1. Define Operating System. What are its two main goals?
2. List any 5 functions of an Operating System.
3. What is the difference between User Mode and Kernel Mode?
4. What is a system call? Give 4 examples.
5. What is the difference between Multiprogramming and Time-sharing OS?
6. What is a Real-time OS? Differentiate Hard RTOS and Soft RTOS.
7. What is a Distributed Operating System?
8. What is the difference between Monolithic and Microkernel OS structure?
9. What is the booting process? List the steps in order.
10. What is the difference between BIOS and UEFI?

### Long Answer (5-7 Marks)

1. **Explain the structure of OS (Monolithic, Layered, Microkernel, Modular, Hybrid). Which is best and why?**
2. **Describe all types of Operating Systems with examples and advantages/disadvantages.**
3. **Explain the booting process in detail with a flowchart.**
4. **Explain OS services provided to users and for efficient operation.**
5. **Explain dual-mode operation in OS. Why is it important for protection?**

---

## Unit 2 - Process and CPU Scheduling

### Short Answer (2 Marks)

1. What is a process? How is it different from a program?
2. Draw and explain the process state diagram.
3. What is a PCB? List 6 fields stored in PCB.
4. What is context switching? Is it overhead?
5. Differentiate long-term, short-term, and medium-term schedulers.
6. What is the convoy effect? Which algorithm causes it?
7. What is starvation? How does aging solve it?
8. What is the difference between preemptive and non-preemptive scheduling?
9. What is the ideal time quantum for Round Robin?
10. Write the formulas for TAT and WT.

### Scheduling Numericals (5-7 Marks)

> [!tip] Numerical Questions - Always draw Gantt chart first, then compute TAT and WT

**Problem Set 1:**
| Process | Arrival Time | Burst Time |
|---------|-------------|-----------|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

Solve with: (a) FCFS (b) SJF Non-preemptive (c) SJF Preemptive (SRTF) (d) Round Robin (q=2)
*For each: draw Gantt chart, compute TAT and WT for each process, find averages.*

**Problem Set 2:**
| Process | AT | BT | Priority |
|---------|----|----|---------|
| P1 | 0 | 10 | 3 |
| P2 | 2 | 5 | 1 |
| P3 | 4 | 8 | 4 |
| P4 | 6 | 3 | 2 |

Solve with: (a) Priority Preemptive (b) Priority Non-preemptive (c) Round Robin q=3

**Problem Set 3 (Common Exam Pattern):**
5 processes, all arriving at time 0: P1(BT=6), P2(BT=3), P3(BT=8), P4(BT=1), P5(BT=4)
Solve: FCFS, SJF, Round Robin (q=2). Which has minimum average WT?

---

## Unit 3 - Memory Management

### Short Answer (2 Marks)

1. What is address binding? Name its three types.
2. What is the role of MMU?
3. What is the difference between logical and physical address?
4. What is internal fragmentation vs external fragmentation?
5. What is paging? What are pages and frames?
6. What is TLB? What is its purpose?
7. Write the formula for Effective Access Time (EAT).
8. What is virtual memory? What is demand paging?
9. What is a page fault? How is it handled?
10. What is Belady's Anomaly?
11. What is thrashing? How is it prevented?
12. Compare paging and segmentation.

### Memory Numericals (5-7 Marks)

**Paging/Address Translation:**
- Logical address space = 32 pages of 4KB each. Physical memory = 16 frames of 4KB. Logical address = 12345. Find page number, offset, and physical address.
- TLB hit ratio = 90%, TLB access = 20ns, Memory access = 100ns. Find EAT.

**Page Replacement:**

> [!tip] Reference String: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1 | Frames: 3

For each algorithm (FIFO, OPT, LRU):
- Show page table at each step
- Count total page faults
- Calculate hit ratio = (Total references - Page faults) / Total references

**Common Problem:**
Reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 | Frames: 3
(a) FIFO - page faults: 9
(b) OPT - page faults: 6
(c) LRU - page faults: 8

---

## Unit 4 - Deadlock

### Short Answer (2 Marks)

1. Define deadlock. Give a real-world example.
2. State the four necessary conditions for deadlock.
3. What is a Resource Allocation Graph (RAG)?
4. When does a cycle in RAG indicate deadlock?
5. What is the difference between deadlock prevention and avoidance?
6. What is a safe state? What is an unsafe state?
7. What is the Need matrix? Write its formula.
8. What is deadlock detection? When is it used?
9. What are recovery methods from deadlock?
10. How does aging differ from starvation prevention in deadlock avoidance?

### Banker's Algorithm Numericals (7-10 Marks)

> [!warning] This is the most important numerical in Unit 4!

**Standard Problem:**

System: 5 processes (P0-P4), 3 resources (A=10, B=5, C=7)

| Process | Allocation (A,B,C) | Max (A,B,C) |
|---------|-------------------|-------------|
| P0 | 0, 1, 0 | 7, 5, 3 |
| P1 | 2, 0, 0 | 3, 2, 2 |
| P2 | 3, 0, 2 | 9, 0, 2 |
| P3 | 2, 1, 1 | 2, 2, 2 |
| P4 | 0, 0, 2 | 4, 3, 3 |

Tasks:
(a) Compute the Need matrix
(b) Find the Available vector
(c) Is the system in a safe state? If yes, find the safe sequence.
(d) If P1 requests [1,0,2], can it be granted?

**Answer:** Available=[3,3,2]; Safe sequence: P1→P3→P4→P0→P2; P1's request can be granted.

**Practice Problem 2:**
System: 3 processes, 3 resources (A=9, B=3, C=6)

| Process | Allocation (A,B,C) | Max (A,B,C) |
|---------|-------------------|-------------|
| P0 | 2, 0, 0 | 3, 2, 2 |
| P1 | 3, 0, 2 | 3, 3, 2 |
| P2 | 2, 1, 1 | 3, 1, 3 |

Find: Need matrix, Available, safe sequence, whether P2 requesting [1,0,0] can be granted.

---

## Unit 5 - File System and Disk Scheduling

### Short Answer (2 Marks)

1. What is a file? List its attributes.
2. What are the different directory structures?
3. Compare contiguous and linked file allocation.
4. What is indexed allocation? What is an inode?
5. What is FAT? How does it improve linked allocation?
6. Explain free space management using bitmap.
7. List the components of disk access time.
8. What is the main goal of disk scheduling?
9. Compare SSTF and SCAN algorithms.
10. What is C-SCAN? How does it differ from SCAN?
11. What is Belady's Anomaly? (Answer: Page replacement, not disk scheduling!)
12. What is LOOK? How is it better than SCAN?

### Disk Scheduling Numericals (5-7 Marks)

> [!tip] Standard Disk Scheduling Problem

**Given:**
- Initial head position: 53
- Request queue: 98, 183, 37, 122, 14, 124, 65, 67
- Disk size: 0 to 199

**Solve with all algorithms:**

| Algorithm | Sequence | Total Movement |
|-----------|----------|---------------|
| FCFS | 53→98→183→37→122→14→124→65→67 | 640 |
| SSTF | 53→65→67→37→14→98→122→124→183 | 236 |
| SCAN (toward 0) | 53→37→14→0→65→67→98→122→124→183 | 236 |
| C-SCAN | 53→65→67→98→122→124→183→199→0→14→37 | 382 |
| LOOK (toward 0) | 53→37→14→65→67→98→122→124→183 | 208 |
| C-LOOK | 53→65→67→98→122→124→183→14→37 | 153 |

**Practice Problem 2:**
Head at: 100 | Queue: 55, 58, 39, 18, 90, 160, 150, 38, 184
Disk: 0-199
Calculate total head movement for FCFS, SSTF, SCAN (moving toward 0), LOOK.

---

## Tricky Conceptual Questions

> [!warning] These questions test deeper understanding

1. **"All deadlocked processes are starved, but not all starved processes are deadlocked."** - Explain.

2. **Can an unsafe state lead to deadlock?**  
   (Answer: Not necessarily. Unsafe state means there's NO guarantee of avoiding deadlock, but it might not happen. Unsafe ≠ Deadlock.)

3. **If a system has only one process, can deadlock occur?**  
   (Answer: Only if the process requests a resource it already holds AND the system doesn't have multiple instances. Typically No for single process.)

4. **Why is FIFO subject to Belady's Anomaly but LRU is not?**  
   (FIFO is not a "stack algorithm". Stack algorithms (OPT, LRU) guarantee more frames → fewer faults.)

5. **What happens if all processes in the ready queue have the same priority in Priority Scheduling?**  
   (Falls back to FCFS among equal-priority processes.)

6. **Why does TLB have high hit ratio in practice?**  
   (Locality of reference - programs tend to access the same pages repeatedly in short time periods.)

7. **Can context switching time be zero?**  
   (Theoretically yes in some specialized hardware, but practically always takes some time.)

8. **Why can't the OS simply kill any deadlocked process to recover?**  
   (Process may be in the middle of updating a file - killing it could corrupt data. Must roll back to a safe state.)

9. **What is the difference between a directory and a folder?**  
   (Directory is the OS-level data structure. Folder is the GUI metaphor for the same concept.)

10. **How does contiguous allocation work for CDs/DVDs?**  
    (Sequential read-only media - contiguous allocation is perfect since files never change and fast sequential access is needed.)

---

## One-liner Answers (Quick Review)

| Question | Answer |
|----------|--------|
| OS dual mode? | User mode (restricted) + Kernel mode (full access) |
| Process states? | New → Ready → Running → Waiting → Terminated |
| PCB stores? | PID, state, PC, registers, memory info, I/O info |
| FCFS problem? | Convoy effect - short waits for long |
| SJF optimal for? | Minimum average waiting time |
| SJF problem? | Starvation; solution: aging |
| Context switch = ? | Pure overhead (save/restore PCB) |
| Internal fragmentation? | Wasted space inside allocated block (paging) |
| External fragmentation? | Wasted space between blocks (segmentation) |
| Belady's Anomaly? | FIFO: more frames → more page faults! |
| Deadlock conditions? | ME + HW + NP + CW (all four!) |
| Need matrix? | Max - Allocation |
| Safe state means? | Safe sequence exists for all processes to finish |
| Banker's grants if? | System stays in safe state after allocation |
| Contiguous drawback? | External fragmentation; file can't grow |
| Linked drawback? | No random access; pointer overhead |
| Indexed advantage? | Direct access + no external fragmentation |
| inode has? | Metadata + 12 direct + single/double/triple indirect blocks |
| SSTF problem? | Starvation of faraway requests |
| Best disk scheduling? | C-LOOK (uniform wait time, efficient) |
| Total disk access? | Seek time + Rotational latency + Transfer time |
