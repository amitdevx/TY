---
title: "Assignment 1: Process Operations"
tags: [lab, os-lab, process, fork, exec, wait]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 1: Process Operations

## 1. Problem Statement / Aim
To understand and implement system calls related to process management in a UNIX/Linux environment. Specifically, the aim is to write C programs using the `fork()`, `exec()`, `wait()`, `getpid()`, and `getppid()` system calls to create and manage processes.

## 2. Theory & Concept
### Process Management System Calls
1. **`fork()`**: This system call is used to create a new process. The new process is called the "child" process, and the process that calls `fork()` is the "parent" process. `fork()` returns `0` to the child process and the Process ID (PID) of the child to the parent process. If `fork()` fails, it returns `-1`.
2. **`exec()` family**: This system call is used to replace the current process image with a new process image. Commonly used functions include `execlp`, `execv`, etc. When `exec()` is called, the current process is overwritten, and the new program starts executing.
3. **`wait()`**: This system call blocks the calling process until one of its child processes exits or a signal is received. It helps in synchronizing parent and child execution, preventing zombie processes.
4. **`getpid()` and `getppid()`**: These functions return the PID of the calling process and its parent process, respectively.

## 3. Fully Solved C Code

### Program 1: Creating a child process using fork()
```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    printf("Starting Process. PID = %d\n", getpid());
    
    // Creating a child process
    pid = fork();
    
    if (pid < 0) {
        printf("Fork Failed!\n");
        return 1;
    } else if (pid == 0) {
        // Child process
        printf("Inside Child Process! PID = %d, Parent PID = %d\n", getpid(), getppid());
    } else {
        // Parent process
        printf("Inside Parent Process! PID = %d, Child PID = %d\n", getpid(), pid);
    }
    
    return 0;
}
```

### Program 2: Using exec() and wait()
```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        printf("Fork Failed\n");
        return 1;
    } else if (pid == 0) {
        // Child Process executes a new program (e.g., 'ls')
        printf("Child Process (PID: %d) executing 'ls -l'...\n\n", getpid());
        execlp("/bin/ls", "ls", "-l", NULL);
        // If execlp fails
        printf("Exec Failed\n");
        exit(1);
    } else {
        // Parent Process
        printf("Parent Process (PID: %d) waiting for child to complete...\n", getpid());
        wait(NULL); // Wait for child
        printf("\nChild completed. Parent terminating.\n");
    }
    
    return 0;
}
```

## 4. Expected Output
### Output for Program 1
```
Starting Process. PID = 1234
Inside Parent Process! PID = 1234, Child PID = 1235
Inside Child Process! PID = 1235, Parent PID = 1234
```

### Output for Program 2
```
Parent Process (PID: 1234) waiting for child to complete...
Child Process (PID: 1235) executing 'ls -l'...

total 16
-rwxrwxr-x 1 user user 8432 Jun 18 10:00 a.out
-rw-rw-r-- 1 user user  541 Jun 18 09:59 fork_exec.c

Child completed. Parent terminating.
```