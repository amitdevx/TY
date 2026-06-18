---
title: "Assignment 6: Disk Scheduling Algorithms"
tags: [lab, os-lab, disk-scheduling, fcfs, sstf, scan, c-scan]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 6: Disk Scheduling Algorithms

## 1. Problem Statement / Aim
To write a C program to implement Disk Scheduling Algorithms: FCFS (First Come First Serve) and SSTF (Shortest Seek Time First), calculating the total head movement (seek count).

## 2. Theory & Concept
Disk scheduling is done by operating systems to schedule I/O requests arriving for the disk. Disk scheduling is important because disk is a slow device compared to RAM and CPU, and minimizing seek time drastically improves system performance.
*   **FCFS**: Serves requests in the order they arrive. Fair, but not optimal in terms of seek time.
*   **SSTF**: Selects the disk I/O request which requires the least disk arm movement from its current position regardless of the direction. Reduces total seek time but may cause starvation.
*   **SCAN (Elevator Algorithm)**: The disk arm starts from one end of the disk and moves toward the other end, servicing requests, then reverses direction.
*   **C-SCAN**: Similar to SCAN but when it reaches the other end, it immediately returns to the beginning of the disk without servicing any requests on the return trip.

## 3. Fully Solved C Code

### Program: FCFS Disk Scheduling
```c
#include <stdio.h>
#include <stdlib.h> // For abs()

int main() {
    int request_queue[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int n = sizeof(request_queue) / sizeof(request_queue[0]);
    int initial_head = 53;
    int total_head_movement = 0;
    
    printf("--- FCFS Disk Scheduling ---\n");
    printf("Initial Head Position: %d\n", initial_head);
    printf("Seek Sequence: ");
    
    int current_head = initial_head;
    for (int i = 0; i < n; i++) {
        printf("%d ", request_queue[i]);
        total_head_movement += abs(request_queue[i] - current_head);
        current_head = request_queue[i];
    }
    
    printf("\nTotal Head Movement: %d cylinders\n", total_head_movement);
    return 0;
}
```

## 4. Expected Output
```text
--- FCFS Disk Scheduling ---
Initial Head Position: 53
Seek Sequence: 98 183 37 122 14 124 65 67 
Total Head Movement: 640 cylinders
```