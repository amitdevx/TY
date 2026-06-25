---
title: "CS-358 Viva 5"
---

[[CS-358-Assignment-5|Back to Assignment 5]]

## 5. Viva Questions for this Assignment
**Q1. Why do we need the `<uses-permission android:name="android.permission.INTERNET" />` tag?**
*Answer\*: Accessing the internet is a restricted operation. Android requires apps to explicitly declare this requirement so the OS can grant the app the ability to open network sockets.

**Q2. What is `NetworkOnMainThreadException`?**
*Answer\*: It is an exception thrown when an application attempts to perform a networking operation (like opening an HTTP connection) on its main UI thread.

**Q3. What is `runOnUiThread()`?**
*Answer\*: It is a method in the `Activity` class that allows background threads to execute code on the UI thread. This is mandatory because only the original UI thread can update or alter views.

**Q4. What is JSON?**
*Answer\*: JavaScript Object Notation. It is a lightweight format for storing and transporting data, commonly used when data is sent from a server to a client.