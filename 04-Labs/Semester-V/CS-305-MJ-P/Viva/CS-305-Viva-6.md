---
title: "CS-305 Viva 6"
---

[[CS-305-Assignment-6|Back to Assignment 6]]

## 5. Viva Questions
1. **What is Seek Time?**
   The time taken by the disk arm to move the read/write head to the cylinder containing the desired sector.
2. **What is Rotational Latency?**
   The time taken for the desired sector of the disk to rotate into a position underneath the read/write head.
3. **What is the difference between SCAN and C-SCAN?**
   SCAN reverses direction and services requests continuously on both trips. C-SCAN provides a more uniform wait time by returning to the beginning immediately upon reaching the end, without servicing requests on the return journey.
4. **Why might SSTF cause starvation?**
   If there is a continuous stream of requests close to the current head position, requests far away may never get serviced.
5. **Which disk scheduling algorithm is considered best?**
   SCAN and C-SCAN are generally better for systems that place a heavy load on the disk, as they prevent starvation and reduce variance in response time compared to SSTF.