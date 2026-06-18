---
title: "CS-305 Viva 1"
---

[[CS-305-Assignment-1|Back to Assignment 1]]

## 5. Viva Questions
1. **What is a process?**
   A process is a program in execution. It is an active entity that requires resources like CPU time, memory, files, and I/O devices to accomplish its task.
2. **What does the `fork()` system call do?**
   It creates a new child process by duplicating the calling parent process. Both processes run concurrently starting from the next instruction.
3. **What is the difference between `fork()` and `exec()`?**
   `fork()` creates a new process that is a duplicate of the parent, while `exec()` replaces the memory space of the current process with a new program.
4. **Why do we use the `wait()` system call?**
   To make the parent process wait until its child terminates. This synchronization ensures that the child process does not become a zombie process.
5. **What is a Zombie Process?**
   A zombie process is a terminated process that still has an entry in the process table because its parent hasn't read its exit status (hasn't called `wait()`).