# CS-356 Assignment 2: Multithreading

## Problem Statement / Aim
To learn and implement multithreading in Java using Thread class and Runnable interface.

## Theory & Concept
Multithreading is a process of executing multiple threads simultaneously. A thread is a lightweight sub-process, the smallest unit of processing. In Java, multithreading can be achieved either by extending the `Thread` class or by implementing the `Runnable` interface. Synchronization is used to control the access of multiple threads to any shared resource.

## Fully Solved Code
```java
class MyRunnable implements Runnable {
    private String threadName;

    MyRunnable(String name) {
        this.threadName = name;
    }

    public void run() {
        try {
            for (int i = 1; i <= 3; i++) {
                System.out.println("Thread: " + threadName + ", Count: " + i);
                Thread.sleep(500); // Sleep for 500ms
            }
        } catch (InterruptedException e) {
            System.out.println("Thread " + threadName + " interrupted.");
        }
        System.out.println("Thread " + threadName + " exiting.");
    }
}

public class MultithreadingDemo {
    public static void main(String[] args) {
        Thread t1 = new Thread(new MyRunnable("T1"));
        Thread t2 = new Thread(new MyRunnable("T2"));

        t1.start();
        t2.start();
    }
}
```

## Expected Output
```
Thread: T1, Count: 1
Thread: T2, Count: 1
Thread: T2, Count: 2
Thread: T1, Count: 2
Thread: T2, Count: 3
Thread: T1, Count: 3
Thread T2 exiting.
Thread T1 exiting.
```

---
[[CS-356-Viva-2|View Viva Questions]]
