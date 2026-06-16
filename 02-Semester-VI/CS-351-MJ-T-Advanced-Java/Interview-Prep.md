---
title: "CS-351 Advanced Java Interview Prep"
tags: [cs-351, advanced-java, interview]
---

# Advanced Java Interview Preparation

1. **Difference between HashMap and ConcurrentHashMap?**
   HashMap is not thread-safe. ConcurrentHashMap is thread-safe and highly concurrent.
2. **What is the difference between Statement and PreparedStatement?**
   PreparedStatement is precompiled, faster for repeated execution, and prevents SQL injection.
3. **Explain the Servlet lifecycle.**
   Class loaded -> Instantiated -> `init()` called once -> `service()` called for each request -> `destroy()` called on shutdown.
4. **What is Dependency Injection in Spring?**
   The framework injects the dependent objects instead of the class creating them itself. Promotes loose coupling.
5. **What is the purpose of the `volatile` keyword?**
   It ensures that the value of a variable is always read from main memory, not from a thread's local cache.
