---
title: "CS-305 Viva 4"
---

[[CS-305-Assignment-4|Back to Assignment 4]]

## 5. Viva Questions
1. **What is a Deadlock?**
   A situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
2. **What are the four necessary conditions for Deadlock?**
   Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.
3. **What is the difference between Deadlock Prevention and Avoidance?**
   Prevention ensures that at least one of the four necessary conditions cannot hold. Avoidance requires the OS to have prior knowledge of resource requests to make decisions dynamically and maintain a safe state.
4. **Why is Banker's algorithm called so?**
   Because it models the banking system, ensuring the bank never allocates its available cash in such a way that it can no longer satisfy the needs of all its customers.
5. **What happens if a state is unsafe?**
   An unsafe state does not necessarily mean a deadlock has occurred, but it means that the system could potentially enter a deadlock situation if processes request their maximum resources.