---
title: "Assignment 4: Banker's Algorithm"
tags: [lab, os-lab, deadlock, bankers-algorithm]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 4: Banker's Algorithm

## 1. Problem Statement / Aim
To write a C program to implement Banker's Algorithm for Deadlock Avoidance. The program should check whether the system is in a safe state by finding a safe sequence, and whether a new resource request can be granted safely.

## 2. Theory & Concept
Deadlock avoidance requires that the OS be given additional information in advance concerning which resources a process will request and use during its lifetime.
**Banker's Algorithm** is a resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation for predetermined maximum possible amounts of all resources, before deciding whether allocation should be allowed to continue.
*   **Available**: Array indicating available resources of each type.
*   **Max**: Matrix defining maximum demand of each process.
*   **Allocation**: Matrix defining currently allocated resources.
*   **Need**: Matrix defining remaining resource needs of each process (`Need[i][j] = Max[i][j] - Allocation[i][j]`).

A state is **Safe** if there exists a sequence of processes such that for each process, its resource needs can be satisfied by currently available resources plus resources held by previously completed processes.

## 3. Fully Solved C Code

### Program: Banker's Algorithm (Safety Sequence)
```c
#include <stdio.h>

int main() {
    int n = 5; // Number of processes
    int m = 3; // Number of resource types
    
    // Allocation Matrix
    int alloc[5][3] = { {0, 1, 0}, {2, 0, 0}, {3, 0, 2}, {2, 1, 1}, {0, 0, 2} };
    
    // Max Matrix
    int max[5][3] = { {7, 5, 3}, {3, 2, 2}, {9, 0, 2}, {2, 2, 2}, {4, 3, 3} };
    
    // Available Resources
    int avail[3] = {3, 3, 2}; 
    
    int f[n], ans[n], ind = 0;
    for (int k = 0; k < n; k++) f[k] = 0; // f is finished array
    
    int need[n][m];
    // Calculate Need Matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            need[i][j] = max[i][j] - alloc[i][j];
        }
    }
    
    for (int k = 0; k < 5; k++) {
        for (int i = 0; i < n; i++) {
            if (f[i] == 0) {
                int flag = 0;
                for (int j = 0; j < m; j++) {
                    if (need[i][j] > avail[j]) {
                        flag = 1;
                        break;
                    }
                }
                
                if (flag == 0) {
                    ans[ind++] = i;
                    for (int y = 0; y < m; y++)
                        avail[y] += alloc[i][y];
                    f[i] = 1;
                }
            }
        }
    }
    
    int safe = 1;
    for(int i=0; i<n; i++) {
        if(f[i] == 0) {
            safe = 0;
            printf("System is NOT in a safe state.\n");
            break;
        }
    }
    
    if(safe) {
        printf("System is in a SAFE state.\nSafe Sequence: ");
        for (int i = 0; i < n - 1; i++)
            printf("P%d -> ", ans[i]);
        printf("P%d\n", ans[n - 1]);
    }

    return 0;
}
```

## 4. Expected Output
```text
System is in a SAFE state.
Safe Sequence: P1 -> P3 -> P4 -> P0 -> P2
```