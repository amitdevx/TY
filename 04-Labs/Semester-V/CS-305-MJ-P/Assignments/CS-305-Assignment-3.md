---
title: "Assignment 3: Page Replacement Algorithms"
tags: [lab, os-lab, page-replacement, fifo, lru, optimal]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 3: Page Replacement Algorithms

## 1. Problem Statement / Aim
To simulate and evaluate the performance of Page Replacement Algorithms: FIFO (First In First Out), LRU (Least Recently Used), and Optimal Page Replacement in C. The program should take a reference string and the number of page frames to calculate the total number of page faults.

## 2. Theory & Concept
Page replacement algorithms decide which memory pages to page out when a page of memory needs to be allocated. Paging happens when a page fault occurs and a free page cannot be used to satisfy the allocation, either because there are none, or because the number of free pages is lower than some threshold.
*   **FIFO**: The oldest page in memory is replaced first. It uses a queue to track pages.
*   **Optimal (OPT)**: Replaces the page that will not be used for the longest period of time in the future. Difficult to implement in practice as it requires future knowledge.
*   **LRU**: Replaces the page that has not been used for the longest period of time. Approximates Optimal.

*Belady's Anomaly*: Specifically in FIFO, sometimes increasing the number of page frames results in an increase in the number of page faults.

## 3. Fully Solved C Code

### Program: FIFO Page Replacement
```c
#include <stdio.h>

int main() {
    int reference_string[] = {1, 3, 0, 3, 5, 6, 3};
    int n = sizeof(reference_string) / sizeof(reference_string[0]);
    int frames = 3;
    int frame_arr[10], page_faults = 0, index = 0;
    
    for (int i = 0; i < frames; i++) {
        frame_arr[i] = -1; // Initialize frames with -1 (empty)
    }
    
    printf("Reference String\t Frames\t\tPage Fault\n");
    for (int i = 0; i < n; i++) {
        int found = 0;
        // Check if page exists in frame
        for (int j = 0; j < frames; j++) {
            if (frame_arr[j] == reference_string[i]) {
                found = 1;
                break;
            }
        }
        
        // If page fault occurs
        if (!found) {
            frame_arr[index] = reference_string[i];
            index = (index + 1) % frames; // FIFO queue mechanism
            page_faults++;
        }
        
        // Printing row
        printf("\t%d\t\t", reference_string[i]);
        for (int j = 0; j < frames; j++) {
            if (frame_arr[j] != -1) printf("%d ", frame_arr[j]);
            else printf("- ");
        }
        if (!found) printf("\t\tYes\n");
        else printf("\t\tNo\n");
    }
    
    printf("\nTotal Page Faults (FIFO): %d\n", page_faults);
    return 0;
}
```

## 4. Expected Output
```text
Reference String	 Frames		Page Fault
	1		1 - - 		Yes
	3		1 3 - 		Yes
	0		1 3 0 		Yes
	3		1 3 0 		No
	5		5 3 0 		Yes
	6		5 6 0 		Yes
	3		5 6 3 		Yes

Total Page Faults (FIFO): 6
```