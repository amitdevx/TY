---
title: "CS-302 Operating Systems Interview Preparation"
tags: [cs-302, operating-systems, interview, semester-v]
subject_code: CS-302-MJ-T
type: interview-prep
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Operating Systems Interview Preparation

> [!summary] About
> Top 30+ Operating Systems interview questions categorized by topic, with detailed explanations and scheduling algorithms. Essential for core CS interviews and placement drives.

---

## 1. Operating System Fundamentals

> [!question] 1. What is an Operating System? What are its main functions?
> An Operating System (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.
> **Main functions:**
> 1. Process Management
> 2. Memory Management
> 3. File System Management
> 4. I/O Device Management
> 5. Security and Protection

> [!question] 2. What is the difference between a Monolithic kernel and a Microkernel?
> - **Monolithic Kernel:** All OS services (memory, processes, VFS, device drivers) run in kernel space. High performance but less stable (a bug in a driver can crash the entire OS). Example: Linux.
> - **Microkernel:** Only essential services run in kernel space; other services run as user-level servers. More stable and secure but slower due to message passing overhead. Example: MINIX, QNX.

> [!question] 3. Explain the Booting Process.
> 1. Power on -> BIOS/UEFI initializes hardware (POST - Power On Self Test).
> 2. BIOS loads the MBR (Master Boot Record) from the boot device.
> 3. MBR loads the Bootloader (e.g., GRUB).
> 4. Bootloader loads the OS Kernel into memory.
> 5. Kernel initializes system, mounts root filesystem, and starts the first process (`init` or `systemd`).

---

## 2. Process Management

> [!question] 4. What is the difference between a Program and a Process?
> - **Program:** Passive entity (an executable file residing on disk).
> - **Process:** Active entity (a program in execution loaded in memory). A process has its own memory space (code, data, heap, stack).

> [!question] 5. What is a Process Control Block (PCB)?
> PCB is a data structure maintained by the OS for every process. It contains information required to manage the process, such as:
> Process ID (PID), Process State, Program Counter, CPU registers, Memory limits, and List of open files.

> [!question] 6. What are the different states of a process?
> 1. **New:** Process is being created.
> 2. **Ready:** Waiting to be assigned to a processor.
> 3. **Running:** Instructions are being executed.
> 4. **Waiting/Blocked:** Waiting for some event to occur (e.g., I/O completion).
> 5. **Terminated:** Finished execution.

> [!question] 7. What is Context Switching?
> The process of saving the state (context) of a currently running process (in its PCB) and loading the state of the next process to run. It introduces overhead because the CPU does no useful work while switching.

---

## 3. Process Scheduling

> [!question] 8. What are the types of CPU Schedulers?
> 1. **Long-Term Scheduler (Job Scheduler):** Selects processes from the pool and loads them into memory for execution. Controls degree of multiprogramming.
> 2. **Short-Term Scheduler (CPU Scheduler):** Selects from among the processes that are ready to execute and allocates the CPU to one of them. Executes very frequently.
> 3. **Mid-Term Scheduler:** Swaps processes in and out of memory to manage multiprogramming level and memory constraints.

> [!question] 9. Differentiate between Preemptive and Non-Preemptive scheduling.
> - **Preemptive:** A running process can be interrupted and moved to the ready state by the OS (e.g., if a higher priority process arrives or time quantum expires). Example: Round Robin.
> - **Non-Preemptive:** Once the CPU has been allocated to a process, the process keeps the CPU until it terminates or switches to the waiting state. Example: FCFS.

> [!question] 10. Explain FCFS, SJF, and Round Robin scheduling.
> - **FCFS (First Come First Serve):** Simple queue. Processes are executed in the order they arrive. Can cause the "Convoy Effect" (short processes waiting for a long process).
> - **SJF (Shortest Job First):** Executes the process with the shortest burst time next. Gives minimum average waiting time. Difficult to predict actual burst time.
> - **Round Robin (RR):** Each process gets a small unit of CPU time (time quantum). After the time has elapsed, the process is preempted and added to the end of the ready queue. Ideal for time-sharing systems.

---

## 4. Memory Management

> [!question] 11. What is Virtual Memory?
> A memory management capability of an OS that uses hardware and software to allow a computer to compensate for physical memory shortages by temporarily transferring data from RAM to disk storage. It gives the illusion of a very large main memory.

> [!question] 12. Paging vs. Segmentation
> - **Paging:** Divides memory into fixed-size blocks (Frames) and logical memory into blocks of the same size (Pages). Solves external fragmentation. Hidden from the user.
> - **Segmentation:** Divides memory into variable-sized blocks based on logical units (e.g., main program, function, symbol table). Solves internal fragmentation. Visible to the user.

> [!question] 13. What is Thrashing?
> A situation where a system spends more time paging (swapping pages in and out of memory) than executing actual instructions, leading to severe performance degradation. Caused by high degree of multiprogramming.

> [!question] 14. What is a Translation Lookaside Buffer (TLB)?
> A high-speed hardware cache used by the MMU (Memory Management Unit) to store recent translations of virtual memory to physical memory. It drastically reduces the time taken to access a user memory location.

---

## 5. Deadlocks

> [!question] 15. What is a Deadlock?
> A state where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.

> [!question] 16. What are the 4 necessary conditions for Deadlock? (Coffman conditions)
> 1. **Mutual Exclusion:** At least one resource must be held in a non-shareable mode.
> 2. **Hold and Wait:** A process is holding at least one resource and requesting additional resources held by other processes.
> 3. **No Preemption:** Resources cannot be forcibly taken away from a process.
> 4. **Circular Wait:** A set of processes {$P_0, P_1, ..., P_n$} exist such that $P_0$ waits for $P_1$, $P_1$ waits for $P_2$, and $P_n$ waits for $P_0$.

> [!question] 17. How does Banker's Algorithm work?
> It is a Deadlock Avoidance algorithm. It checks if granting a resource request will leave the system in a "Safe State". A state is safe if there exists a sequence of all processes such that each process can complete its execution. If it leads to an unsafe state, the request is denied.

---

## 6. Disk & File Management

> [!question] 18. What are the File Allocation Methods?
> 1. **Contiguous:** Each file occupies a set of contiguous blocks on the disk. Fast access, but suffers from external fragmentation.
> 2. **Linked:** Each file is a linked list of disk blocks. No external fragmentation, but slow direct access and pointers take up space.
> 3. **Indexed:** Brings all pointers together into an index block. Supports direct access and no external fragmentation, but requires space for the index block.

> [!question] 19. Explain SCAN and SSTF disk scheduling.
> - **SSTF (Shortest Seek Time First):** Selects the request that is closest to the current head position. Can cause starvation for requests far away.
> - **SCAN (Elevator Algorithm):** The disk arm starts at one end, moves to the other end servicing requests, and then reverses direction.

---

[[01-Semester-V/CS-302-MJ-T-Operating-Systems/Unit-1|Unit 1]] | [[01-Semester-V/CS-302-MJ-T-Operating-Systems/Revision|Revision Summary]]
