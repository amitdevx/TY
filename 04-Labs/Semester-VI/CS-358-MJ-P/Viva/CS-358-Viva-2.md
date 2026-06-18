---
title: "CS-358 Viva 2"
---

[[CS-358-Assignment-2|Back to Assignment 2]]

## 5. Viva Questions for this Assignment
**Q1. What is an Intent in Android?**
*Answer*: It is an abstract description of an operation to be performed, acting as a messaging object to request an action from another component.

**Q2. How is an Explicit Intent different from an Implicit Intent?**
*Answer*: Explicit Intents specify the exact Java class name of the activity to start. Implicit Intents do not specify a class, but rather an action (like `ACTION_VIEW`), allowing the Android system to resolve which application should handle it.

**Q3. How do you retrieve data passed via an Intent in the receiving Activity?**
*Answer*: By calling `getIntent()` to grab the intent that started the activity, followed by methods like `getStringExtra(key)` or `getIntExtra(key, defaultVal)` to extract the specific data.

**Q4. What happens if you forget to register an Activity in the `AndroidManifest.xml`?**
*Answer*: The application will crash at runtime with an `ActivityNotFoundException` when attempting to navigate to that Activity using an Intent.