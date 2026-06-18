---
title: "Assignment 5: File Allocation Methods"
tags: [lab, os-lab, file-allocation, contiguous, linked, indexed]
---
[[00-Dashboard/Home|Home]] | [[04-Labs/Labs-Dashboard|Labs]] | [[Lab-Overview|Overview]]

# Assignment 5: File Allocation Methods

## 1. Problem Statement / Aim
To simulate different file allocation strategies (Contiguous, Linked, and Indexed) used in Operating Systems to allocate disk space to files.

## 2. Theory & Concept
The operating system must keep track of the disk space assigned to each file. The main allocation methods are:
1. **Contiguous Allocation**: Each file occupies a set of contiguous blocks on the disk. Directory entry stores the starting block and length. Very fast for sequential access but suffers from external fragmentation.
2. **Linked Allocation**: Each file is a linked list of disk blocks. The directory contains a pointer to the first and last blocks. Good for dynamic files, no external fragmentation, but does not support direct access efficiently.
3. **Indexed Allocation**: Brings all pointers together into one location: the index block. Each file has its own index block, which is an array of disk-block addresses. Supports direct access without external fragmentation.

## 3. Fully Solved C Code

### Program: Contiguous Allocation
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int disk[100] = {0}; // 0 indicates free block
    int num_files, start, length;
    
    printf("Enter number of files to allocate: ");
    scanf("%d", &num_files);
    
    for (int i = 0; i < num_files; i++) {
        printf("\nFile %d:\n", i+1);
        printf("Enter starting block: ");
        scanf("%d", &start);
        printf("Enter length of file: ");
        scanf("%d", &length);
        
        int can_allocate = 1;
        // Check if blocks are free
        for (int j = start; j < start + length; j++) {
            if (disk[j] == 1) {
                can_allocate = 0;
                break;
            }
        }
        
        if (can_allocate) {
            for (int j = start; j < start + length; j++) {
                disk[j] = 1; // Mark as allocated
            }
            printf("File %d allocated from block %d to %d\n", i+1, start, start + length - 1);
        } else {
            printf("Error: Blocks already allocated. Cannot allocate File %d sequentially.\n", i+1);
        }
    }
    return 0;
}
```

## 4. Expected Output
```text
Enter number of files to allocate: 2

File 1:
Enter starting block: 10
Enter length of file: 5
File 1 allocated from block 10 to 14

File 2:
Enter starting block: 13
Enter length of file: 3
Error: Blocks already allocated. Cannot allocate File 2 sequentially.
```