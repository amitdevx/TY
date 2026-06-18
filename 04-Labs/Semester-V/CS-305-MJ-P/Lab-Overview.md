---
title: CS-305-MJ-P OS Lab
tags: [lab, os-lab, semester-v, cs-305, operating-systems, c-programming]
aliases: [OS Lab, CS-305 Lab]
lab_code: CS-305-MJ-P
based_on: CS-302-MJ-T Operating Systems
language: C
platform: Linux
semester: V
total_assignments: 6
total_slots: 12
created: 2026-06-16
updated: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs Dashboard]]


# CS-305-MJ-P - Operating Systems Lab

> [!important] Lab Info
> **Code:** CS-305-MJ-P | **Based On:** CS-302-MJ-T Operating Systems
> **Language:** C | **Platform:** Linux (Ubuntu/Debian)
> **Assignments:** 6 | **Lab Slots:** 12 (2 per assignment)

---

## Lab Navigation

| Experiment | Topic | Link | Status |
|-----------|-------|------|--------|
| Exp-01 | Process Operations (fork/exec) | [[CS-305-Assignment-1]] | ⬜ |
| Exp-02 | CPU Scheduling Algorithms | [[CS-305-Assignment-2]] | ⬜ |
| Exp-03 | Page Replacement Algorithms | [[CS-305-Assignment-3]] | ⬜ |
| Exp-04 | Banker's Algorithm | [[CS-305-Assignment-4]] | ⬜ |
| Exp-05 | File Allocation Methods | [[CS-305-Assignment-5]] | ⬜ |
| Exp-06 | Disk Scheduling Algorithms | [[CS-305-Assignment-6]] | ⬜ |

---

## Syllabus Overview

### Assignment 1 - Process Operations (2 slots)
- **Topics:** `fork()`, `exec()`, `wait()`, `getpid()`, `getppid()`
- **Programs:**
  1. Create child process using fork(), print parent and child PID
  2. Use exec() to replace process image
  3. Parent-child synchronization using wait()
- **Theory:** Process creation, PCB, process states

### Assignment 2 - CPU Scheduling (2 slots)
- **Topics:** FCFS, SJF (non-preemptive), Round Robin, Priority Scheduling
- **Programs:**
  1. FCFS Scheduling - compute waiting time, turnaround time
  2. SJF Non-preemptive Scheduling
  3. Round Robin with time quantum
  4. Priority Scheduling (non-preemptive)
- **Output:** Gantt chart, average waiting time, average turnaround time

### Assignment 3 - Page Replacement (2 slots)
- **Topics:** FIFO, Optimal, LRU, LFU page replacement
- **Programs:**
  1. FIFO Page Replacement - count page faults
  2. Optimal Page Replacement
  3. LRU (Least Recently Used)
- **Theory:** Demand paging, thrashing, Belady's anomaly

### Assignment 4 - Banker's Algorithm (2 slots)
- **Topics:** Deadlock avoidance, safety algorithm, resource request
- **Programs:**
  1. Safety algorithm - check if system is in safe state
  2. Resource request algorithm - can request be granted?
- **Theory:** Deadlock conditions, prevention vs avoidance

### Assignment 5 - File Allocation (2 slots)
- **Topics:** Contiguous, linked, indexed allocation
- **Programs:**
  1. Contiguous allocation - simulate file storage
  2. Linked allocation - simulate with linked list
  3. Indexed allocation - simulate with index block
- **Theory:** File system structure, directories

### Assignment 6 - Disk Scheduling (2 slots)
- **Topics:** FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK
- **Programs:**
  1. FCFS Disk Scheduling - total head movement
  2. SSTF (Shortest Seek Time First)
  3. SCAN (Elevator Algorithm)
  4. C-SCAN Circular SCAN
- **Theory:** Disk structure, seek time, rotational latency

---

## Completion Tracker

### Assignment Completion

- [ ] **Exp-01 - Process Operations**
  - [ ] Slot 1: Theory + Algorithm
  - [ ] Slot 2: Program + Output
  - [ ] Viva Completed
  - [ ] Journal Submitted

- [ ] **Exp-02 - CPU Scheduling**
  - [ ] Slot 1: FCFS + SJF
  - [ ] Slot 2: RR + Priority
  - [ ] Viva Completed
  - [ ] Journal Submitted

- [ ] **Exp-03 - Page Replacement**
  - [ ] Slot 1: FIFO + Optimal
  - [ ] Slot 2: LRU + LFU
  - [ ] Viva Completed
  - [ ] Journal Submitted

- [ ] **Exp-04 - Banker's Algorithm**
  - [ ] Slot 1: Safety Algorithm
  - [ ] Slot 2: Resource Request
  - [ ] Viva Completed
  - [ ] Journal Submitted

- [ ] **Exp-05 - File Allocation**
  - [ ] Slot 1: Contiguous + Linked
  - [ ] Slot 2: Indexed
  - [ ] Viva Completed
  - [ ] Journal Submitted

- [ ] **Exp-06 - Disk Scheduling**
  - [ ] Slot 1: FCFS + SSTF
  - [ ] Slot 2: SCAN + C-SCAN
  - [ ] Viva Completed
  - [ ] Journal Submitted

---

## Setup and Environment

### Prerequisites

```bash
# Install GCC compiler
sudo apt-get install gcc

# Verify installation
gcc --version

# Compile C program
gcc -o output_name program.c

# Run compiled program
./output_name
```

### Useful Linux Commands for OS Lab

| Command | Purpose |
|---------|---------|
| `ps aux` | List all processes |
| `ps -ef` | Full process listing |
| `top` | Real-time process monitor |
| `kill -9 PID` | Kill process by PID |
| `strace ./program` | Trace system calls |
| `valgrind ./program` | Memory leak detection |
| `man fork` | Manual for fork() |

### Essential System Calls Reference

| System Call | Header | Purpose |
|------------|--------|---------|
| `fork()` | `<unistd.h>` | Create child process |
| `exec()` family | `<unistd.h>` | Replace process image |
| `wait()` | `<sys/wait.h>` | Wait for child |
| `getpid()` | `<unistd.h>` | Get process ID |
| `getppid()` | `<unistd.h>` | Get parent PID |

---

## Journal Format

### Page Layout for Each Assignment

1. **Title** - Experiment number and name
2. **Aim/Objective** - What the experiment achieves
3. **Theory** - Relevant concepts (½ page)
4. **Algorithm** - Step-by-step pseudocode
5. **Program** - C code (properly indented)
6. **Output/Sample Run** - Expected output with explanation
7. **Conclusion** - What was learned
8. **Viva Questions** - 5 expected questions with answers

---

## Lab Materials

- [[Universal-Assignments]]: Comprehensive assignment sets covering all major OS concepts.
- [[Lab-Preparation]]: Step-by-step procedures, theories, and exam tips for all experiments.
- [[Viva-Questions]]: Topic-wise questions and answers for viva preparation.
- [[Question-Bank]]: Short, long, practical, and programming questions for exam prep.

---

## Related Resources

- [[01-Semester-V/CS-302-MJ-T-Operating-Systems/Overview|CS-302 OS Theory Dashboard]]
- [[07-Exams/Exams-Dashboard|Exam Prep]]
- [[11-Tracking/Lab-Tracker|Lab Completion Tracker]]

---

*Lab Overview | CS-305-MJ-P | Semester V | Last Updated: 2026-06-16*

## Viva Questions
- [[CS-305-Viva-1]]
- [[CS-305-Viva-2]]
- [[CS-305-Viva-3]]
- [[CS-305-Viva-4]]
- [[CS-305-Viva-5]]
- [[CS-305-Viva-6]]
