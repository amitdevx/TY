---
title: "Assignment 2: CPU Scheduling Algorithms"
tags: [lab, os-lab, cpu-scheduling, fcfs, sjf, rr, priority]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 2: CPU Scheduling Algorithms

## 1. Problem Statement / Aim
To write a C program to simulate the following non-preemptive and preemptive CPU scheduling algorithms to find turnaround time and waiting time.
1. First Come First Serve (FCFS)
2. Shortest Job First (SJF) - Non-Preemptive
3. Round Robin (RR)
4. Priority Scheduling

## 2. Theory & Concept
CPU scheduling is a process that allows one process to use the CPU while the execution of another process is on hold due to unavailability of any resource like I/O, thereby making full use of the CPU.
*   **FCFS**: Simplest algorithm. Processes are assigned the CPU in the order they request it. It is non-preemptive.
*   **SJF**: The process with the smallest execution time is selected for execution next. Can be preemptive (Shortest Remaining Time First) or non-preemptive.
*   **Round Robin (RR)**: Designed for time-sharing systems. Each process gets a small unit of CPU time (time quantum), usually 10-100 milliseconds. After this time has elapsed, the process is preempted and added to the end of the ready queue.
*   **Priority**: A priority is associated with each process, and the CPU is allocated to the process with the highest priority. Equal-priority processes are scheduled in FCFS order.

*Definitions:*
- **Turnaround Time (TAT)** = Completion Time - Arrival Time
- **Waiting Time (WT)** = Turnaround Time - Burst Time

## 3. Fully Solved C Code

### Program: FCFS and SJF Scheduling
```c
#include <stdio.h>

void calculateFCFS(int n, int bt[]) {
    int wt[20], tat[20], total_wt = 0, total_tat = 0;
    wt[0] = 0; // Waiting time for first process is 0
    
    for (int i = 1; i < n; i++) {
        wt[i] = bt[i - 1] + wt[i - 1];
    }
    
    printf("\n--- FCFS Scheduling ---\n");
    printf("Process\t Burst Time \tWaiting Time\tTurnaround Time\n");
    for (int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
        total_wt += wt[i];
        total_tat += tat[i];
        printf("P%d\t\t %d\t\t %d\t\t %d\n", i + 1, bt[i], wt[i], tat[i]);
    }
    
    printf("Average Waiting Time: %.2f\n", (float)total_wt / n);
    printf("Average Turnaround Time: %.2f\n", (float)total_tat / n);
}

void calculateSJF(int n, int bt[], int p[]) {
    int wt[20], tat[20], total_wt = 0, total_tat = 0, temp;
    
    // Sort burst times and process IDs in ascending order
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (bt[i] > bt[j]) {
                temp = bt[i]; bt[i] = bt[j]; bt[j] = temp;
                temp = p[i]; p[i] = p[j]; p[j] = temp;
            }
        }
    }
    
    wt[0] = 0;
    for (int i = 1; i < n; i++) {
        wt[i] = bt[i - 1] + wt[i - 1];
    }
    
    printf("\n--- SJF Scheduling ---\n");
    printf("Process\t Burst Time \tWaiting Time\tTurnaround Time\n");
    for (int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
        total_wt += wt[i];
        total_tat += tat[i];
        printf("P%d\t\t %d\t\t %d\t\t %d\n", p[i], bt[i], wt[i], tat[i]);
    }
    
    printf("Average Waiting Time: %.2f\n", (float)total_wt / n);
    printf("Average Turnaround Time: %.2f\n", (float)total_tat / n);
}

int main() {
    int n = 4;
    int bt_fcfs[] = {21, 3, 6, 2};
    int bt_sjf[] = {21, 3, 6, 2};
    int p[] = {1, 2, 3, 4};
    
    calculateFCFS(n, bt_fcfs);
    calculateSJF(n, bt_sjf, p);
    
    return 0;
}
```

## 4. Expected Output
```text
--- FCFS Scheduling ---
Process	 Burst Time 	Waiting Time	Turnaround Time
P1		 21		 0		 21
P2		 3		 21		 24
P3		 6		 24		 30
P4		 2		 30		 32
Average Waiting Time: 18.75
Average Turnaround Time: 26.75

--- SJF Scheduling ---
Process	 Burst Time 	Waiting Time	Turnaround Time
P4		 2		 0		 2
P2		 3		 2		 5
P3		 6		 5		 11
P1		 21		 11		 32
Average Waiting Time: 4.50
Average Turnaround Time: 12.50
```