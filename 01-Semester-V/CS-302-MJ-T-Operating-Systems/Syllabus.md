---
title: "CS-302 Operating Systems - Complete Syllabus"
subject_code: "CS-302-MJ-T"
course_type: "Major"
semester: "V"
credits: 2
teaching_hours: "2 Hours/Week"
exam_marks: "IE: 15 | EE: 35 | Total: 50"
tags:
  - cs-302
  - operating-systems
  - semester-v
  - syllabus
  - os
aliases:
  - "OS Syllabus"
  - "CS302 Syllabus"
status: "not-started"
---

#  CS-302 Operating Systems - Complete Syllabus

> [!info] Course Information
> **Semester:** V | **Credits:** 2 | **IE:** 15 Marks | **EE:** 35 Marks
> **Teaching:** 2 Hours/Week | **Total:** 30 Hours

##  Prerequisites
- Data structures: stack, queue, linked list, tree, graph, hashing, file structures
- Any structured programming language

##  Course Objectives
- Understand concepts that underlie operating systems
- Study Modern OS and their principles
- Study process scheduling, CPU scheduling algorithms, memory management, Deadlock handling, file system and Disk Management

##  Course Outcomes (COs)

| CO | Description |
|----|-------------|
| CO1 | Understand concepts of OS, its structure and services |
| CO2 | Understand mechanisms of context switching, Scheduling |
| CO3 | Analyze efficiency and performance of CPU scheduling algorithms |
| CO4 | Analyze efficiency of paging, segmentation, virtual memory |
| CO5 | Understand techniques of deadlock handling |
| CO6 | Implement Scheduling algorithms, memory management, disk scheduling |

##  Chapter-wise Syllabus

### Chapter 1: Introduction to Operating System *(3 Hours)*
→ [[Unit-1|Unit 1 Notes]]

| Section | Topics |
|---------|--------|
| 1.1 | Definition, OS functions and services, need/purpose |
| 1.2 | Operating System Structure |
| 1.3 | Types of Operating System (Batch, Time-sharing, Real-time, Distributed, Embedded) |
| 1.4 | Operating System Operation |
| 1.5 | Booting process of OS |
| 1.6 | Advantages and disadvantages of OS |

### Chapter 2: Process and Process Scheduling *(7 Hours)*
→ [[Unit-2|Unit 2 Notes]]

| Section | Topics |
|---------|--------|
| 2.1 | Process, Process States (New/Ready/Running/Waiting/Terminated), PCB, Operations on Process |
| 2.2 | Process Scheduling: Scheduling queues, CPU Schedulers, Context switching, CPU/IO Burst Cycle, Scheduling Criteria, types |
| 2.3 | Scheduling Algorithms: **FCFS**, **SJF**, **Priority Scheduling**, **Round Robin (RR)** |

### Chapter 3: Memory Management *(8 Hours)*
→ [[Unit-3|Unit 3 Notes]]

| Section | Topics |
|---------|--------|
| 3.1 | Introduction, address binding, Logical vs Physical address, MMU |
| 3.2 | Paging concepts - page table structure, working |
| 3.3 | Segmentation - Hardware, Paging vs Segmentation |
| 3.4 | Virtual Memory - Concept, Demand Paging, Performance |
| 3.5 | Page replacement algorithms: **FIFO**, **Optimal**, **LRU**, **MFU** |

### Chapter 4: Deadlock *(7 Hours)*
→ [[Unit-4|Unit 4 Notes]]

| Section | Topics |
|---------|--------|
| 4.1 | Deadlock definition, Process synchronization, Resource Allocation Graph, Necessary conditions (4 conditions) |
| 4.2 | Deadlock Handling: Prevention, Avoidance (Safe state, **Banker's Algorithm**), Detection |
| 4.3 | Recovery from Deadlock: Process termination, Resource preemption |

### Chapter 5: File System Management and Disk Scheduling *(5 Hours)*
→ [[Unit-5|Unit 5 Notes]]

| Section | Topics |
|---------|--------|
| 5.1 | File, File attributes, File operations |
| 5.2 | Allocation Methods: Contiguous, Linked, Indexed |
| 5.3 | Free Space Management: Bit vector, Linked list, Grouping, Counting |
| 5.4 | Disk Structure |
| 5.5 | Disk Scheduling algorithms: **FCFS**, **SSTF**, **SCAN**, **LOOK** |

##  Reference Books

| # | Book | Author |
|---|------|--------|
| R1 | Operating System Concepts (Dinosaur Book) | Silberschatz, Galvin, Gagne |
| R2 | Operating Systems: Internals and Design Principles | William Stallings |
| R3 | Advanced Concepts in Operating Systems | M. Singhal, N.G. Shivaratri |

##  High-Importance Topics for Exam

> [!warning] Must Study
> - **CPU Scheduling**: Gantt charts for FCFS, SJF, Priority, RR
> - **Page Replacement**: Trace tables for FIFO, LRU, Optimal, MFU
> - **Banker's Algorithm**: Safety algorithm + resource request algorithm
> - **Deadlock**: 4 necessary conditions + Coffman's conditions
> - **Disk Scheduling**: Seek time calculation for SSTF, SCAN, LOOK

## ️ Quick Navigation

| File | Purpose |
|------|---------|
| [[Overview|Overview.md]] | Subject overview |
| [[Unit-1|Unit 1: Introduction to OS]] | OS types, structure, booting |
| [[Unit-2|Unit 2: Process & Scheduling]] | Scheduling algorithms with examples |
| [[Unit-3|Unit 3: Memory Management]] | Paging, segmentation, page replacement |
| [[Unit-4|Unit 4: Deadlock]] | Banker's algorithm |
| [[Unit-5|Unit 5: File & Disk Management]] | Disk scheduling |
| [[Important-Questions|Important Questions]] | Exam Q&A |
| [[Revision|Revision Notes]] | Quick revision |
| [[Interview-Prep|Interview Prep]] | OS interview questions |
| [[Home| Dashboard]] | Main vault dashboard |

---
*← [[01-Semester-V/CS-301-MJ-T-Core-Java/Syllabus|CS-301 Java]] | [[Home| Dashboard]] | [[01-Semester-V/CS-303-MJ-T-Web-Technology-I/Syllabus|CS-303 Web →]]*
