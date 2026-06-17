---
title: Semester V Final Revision
tags:
  - revision
  - final-revision
  - semester-v
  - exam-prep
aliases:
  - Sem V Final
  - Semester 5 Cheat Sheet
created: 2026-06-16
last_modified: 2026-06-16
---

[[00-Dashboard/Home|Home]] | [[06-Revision/Revision-Dashboard|Revision Dashboard]]


# Semester V - Final Revision

> [!important] Last-Minute Strategy
> - Read this in the last 48–72 hours before exam
> - Focus on ==highlighted terms== and formulas
> - Don't study new topics now - reinforce what you know!

---

## CS-301 - Core Java

### Critical Topics
1. **OOP Concepts** - Encapsulation, Inheritance, Polymorphism, Abstraction
2. **Java Basics** - Data types, operators, control flow, arrays
3. **Strings** - String vs StringBuilder, String methods
4. **Collections** - ArrayList, LinkedList, HashMap, HashSet
5. **Exception Handling** - try-catch-finally, throw vs throws, custom exceptions
6. **File I/O** - FileReader, FileWriter, BufferedReader, Scanner
7. **Multithreading** - Thread class, Runnable, synchronized, lifecycle
8. **JavaFX** - Stage, Scene, FXML, event handling

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| Inheritance | Child class inherits parent's properties using `extends` |
| Polymorphism | Same method name, different behavior (overloading/overriding) |
| Interface | Blueprint with abstract methods, implemented using `implements` |
| Abstract Class | Can't be instantiated; has abstract + concrete methods |
| Exception | Disruption in normal flow; handled by try-catch-finally |
| Thread | Lightweight process; extends Thread or implements Runnable |
| HashMap | Key-value pairs, O(1) average lookup, no ordering |
| ArrayList | Dynamic array, O(1) access, O(n) insert/delete |

### Formula / Syntax Quick Reference

```java
// Thread creation
class MyThread extends Thread {
    public void run() { /* code */ }
}
new MyThread().start();

// Exception handling
try { riskyCode(); }
catch (Exception e) { e.printStackTrace(); }
finally { cleanup(); }

// Generic class
class Box<T> { T item; }

// Lambda (Java 8+)
list.forEach(item -> System.out.println(item));
```

### Last-Minute Checklist - CS-301
- [ ] OOP pillars explained with examples
- [ ] Difference: abstract class vs interface
- [ ] Collections hierarchy diagram recalled
- [ ] Exception hierarchy recalled
- [ ] Thread lifecycle states
- [ ] File I/O code example ready
- [ ] JavaFX basic app structure

---

## CS-302 - Operating Systems

### Critical Topics
1. **OS Types & Structure** - Monolithic, microkernel, layered
2. **Process Management** - PCB, process states, context switching
3. **CPU Scheduling** - FCFS, SJF, Round Robin, Priority scheduling
4. **Deadlock** - Conditions, prevention, avoidance (Banker's algorithm)
5. **Memory Management** - Paging, segmentation, virtual memory
6. **Page Replacement** - FIFO, LRU, Optimal
7. **File Systems** - FAT, inode, directory structure
8. **Disk Scheduling** - FCFS, SSTF, SCAN, C-SCAN

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| Process | Program in execution with its own memory space |
| Thread | Lightweight process; shares memory with parent |
| Deadlock | Circular wait where no process can proceed |
| Paging | Divides memory into fixed-size frames to eliminate fragmentation |
| Virtual Memory | Allows execution of processes larger than physical memory |
| Semaphore | Synchronization tool using wait (P) and signal (V) operations |
| Banker's Algorithm | Deadlock avoidance by checking safe state before allocation |

### Formula Quick Reference

```
Turnaround Time = Completion Time - Arrival Time
Waiting Time    = Turnaround Time - Burst Time
Response Time   = First Response Time - Arrival Time

Page Fault Rate = Page Faults / Total Memory Accesses

Effective Access Time (EAT) = (1-p) × memory access time + p × page fault time
```

### Scheduling Algorithm Comparison

| Algorithm | Type | Preemptive | Starvation | Overhead |
|-----------|------|-----------|-----------|---------|
| FCFS | Non-preemptive | No | No | Low |
| SJF | Both | Optional | Yes | Medium |
| Round Robin | Preemptive | Yes | No | High |
| Priority | Both | Optional | Yes | Medium |
| SRTF | Preemptive | Yes | Yes | High |

### Last-Minute Checklist - CS-302
- [ ] Draw process state diagram from memory
- [ ] Solve 1 scheduling problem of each type
- [ ] Banker's algorithm steps memorized
- [ ] Paging formula and translation
- [ ] Deadlock 4 conditions (Coffman conditions)
- [ ] Disk scheduling: SCAN vs C-SCAN difference

---

## CS-303 - Web Technology-I

### Critical Topics
1. **HTML5** - Semantic tags, forms, media, tables
2. **CSS3** - Box model, flexbox, grid, animations, media queries
3. **JavaScript** - DOM manipulation, events, ES6+, AJAX, Fetch API
4. **Node.js** - HTTP module, Express.js, routing, middleware
5. **File Handling** - fs module, reading/writing files

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| HTML5 Semantic Tags | `<header>`, `<nav>`, `<section>`, `<article>`, `<footer>` for structure |
| CSS Flexbox | 1D layout system using `display: flex` for rows/columns |
| CSS Grid | 2D layout using `display: grid` with rows and columns |
| JavaScript Closure | Function that remembers its outer scope even after outer function returns |
| Promise | Object representing eventual completion/failure of async operation |
| async/await | Syntactic sugar over Promises for cleaner async code |
| Node.js | Server-side JavaScript runtime built on V8 engine |
| Express.js | Minimal web framework for Node.js |

### Quick Reference Code

```javascript
// Fetch API
fetch('/api/data')
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// Express.js basic server
const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Hello World'));
app.listen(3000);
```

### Last-Minute Checklist - CS-303
- [ ] HTML5 semantic structure drawn from memory
- [ ] CSS specificity rules
- [ ] Flexbox vs Grid: when to use which
- [ ] JS: difference between var, let, const
- [ ] JS: callback vs promise vs async/await
- [ ] Node.js: create basic HTTP server
- [ ] Express.js: routing with middleware

---

## CS-304 - Theory of Computer Science

### Critical Topics
1. **Automata** - DFA, NFA, ε-NFA construction and conversion
2. **Regular Expressions** - to DFA/NFA conversion, minimization
3. **Context-Free Grammar (CFG)** - derivations, parse trees, ambiguity
4. **Pushdown Automata (PDA)** - construction, acceptance modes
5. **Turing Machines** - construction, halting problem
6. **Pumping Lemma** - for regular and CFL
7. **Decidability** - decidable vs undecidable problems

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| DFA | Deterministic: exactly one transition per input per state |
| NFA | Non-deterministic: multiple transitions allowed per input |
| CFG | Grammar with productions of form A → α (Variable → string) |
| PDA | Automaton with a stack for recognizing CFLs |
| Turing Machine | Theoretical model of computation on infinite tape |
| Pumping Lemma | Tool to prove a language is NOT regular |
| Halting Problem | Undecidable - no algorithm can determine if TM halts |

### Key Formulas

```
DFA States: q0, q1, ..., qn
δ: Q × Σ → Q (transition function)

NFA to DFA: Subset construction (powerset of states)

CFL Pumping Lemma: For s ∈ L, |s| ≥ p, s = uvxyz where:
  |vy| ≥ 1, |vxy| ≤ p, ∀i≥0: uv^i xy^i z ∈ L
```

### Last-Minute Checklist - CS-304
- [ ] Convert NFA to DFA (subset construction)
- [ ] Minimize DFA (table-filling algorithm)
- [ ] Derive string from CFG
- [ ] Construct PDA for a^n b^n
- [ ] State Pumping Lemma for Regular Languages
- [ ] Prove a language is not regular using PL
- [ ] Turing Machine: definition and components

---

## CS-307 - Data Science

### Critical Topics
1. **Data Science Lifecycle** - CRISP-DM model
2. **Python Libraries** - NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
3. **Data Preprocessing** - missing values, normalization, encoding
4. **EDA** - exploratory data analysis, visualization types
5. **ML Basics** - supervised vs unsupervised, train-test split
6. **Regression** - Linear, Polynomial regression, R², MSE
7. **Classification** - Logistic regression, KNN, Decision Tree
8. **Clustering** - K-means, hierarchical

### One-Line Summaries

| Concept | One-Line Summary |
|---------|-----------------|
| CRISP-DM | 6-phase DS methodology: Business→Data→Preparation→Modeling→Evaluation→Deployment |
| Pandas DataFrame | 2D labeled data structure; rows=records, columns=features |
| Normalization | Scale features to [0,1] range; `(x - min) / (max - min)` |
| Standardization | Scale to mean=0, std=1; `(x - μ) / σ` |
| Overfitting | Model memorizes training data, fails on test data |
| Bias-Variance | High bias = underfitting; high variance = overfitting |
| K-means | Partition n points into k clusters by minimizing inertia |

### Key Formulas

```
MSE  = (1/n) Σ (y_actual - y_pred)²
RMSE = √MSE
R²   = 1 - (SS_res / SS_tot)

Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
F1        = 2 × (Precision × Recall) / (Precision + Recall)
```

### Last-Minute Checklist - CS-307
- [ ] CRISP-DM phases in order
- [ ] Pandas: read_csv, dropna, fillna, groupby, merge
- [ ] NumPy: array operations, broadcasting
- [ ] Types of plots: when to use what
- [ ] Difference: normalization vs standardization
- [ ] Difference: supervised vs unsupervised
- [ ] K-means algorithm steps

---

## CS-321 - AI/ML (VSC)

### Critical Topics
1. **AI Fundamentals** - agents, rationality, PEAS
2. **Search Algorithms** - BFS, DFS, A*, greedy, heuristics
3. **Knowledge Representation** - propositional and predicate logic
4. **ML Types** - supervised, unsupervised, reinforcement
5. **Neural Networks** - perceptron, backpropagation, activation functions
6. **Deep Learning** - CNN, RNN basics

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| PEAS | Performance, Environment, Actuators, Sensors - defines AI agent |
| A* Search | Optimal path search using f(n) = g(n) + h(n) |
| Admissible Heuristic | Never overestimates true cost; guarantees A* optimality |
| Perceptron | Simplest neural network; binary linear classifier |
| Backpropagation | Algorithm to compute gradients in neural networks |
| CNN | Uses convolution to extract spatial features from images |
| Reinforcement Learning | Agent learns by reward/penalty from environment interaction |

### Key Formulas

```
A* f(n) = g(n) + h(n)
  g(n) = cost from start to n
  h(n) = heuristic cost from n to goal

Sigmoid: σ(x) = 1 / (1 + e^(-x))
ReLU:    f(x) = max(0, x)
Softmax: P(class_i) = e^(z_i) / Σ e^(z_j)
```

### Last-Minute Checklist - CS-321
- [ ] PEAS framework for a given agent
- [ ] BFS vs DFS: time/space complexity
- [ ] A* vs Greedy Best-First: difference
- [ ] Propositional logic: truth tables
- [ ] Neural network forward pass steps
- [ ] Difference: CNN vs RNN use cases

---

## Formula Quick Reference - All Subjects

| Formula | Subject | Context |
|---------|---------|---------|
| TAT = CT - AT | OS | Turnaround time |
| WT = TAT - BT | OS | Waiting time |
| EAT = (1-p)×m + p×t | OS | Effective access time with paging |
| MSE = (1/n)Σ(y-ŷ)² | DS | Regression error |
| R² = 1 - SS_res/SS_tot | DS | Regression goodness of fit |
| f(n) = g(n) + h(n) | AI | A* search evaluation |
| Accuracy = (TP+TN)/Total | DS/AI | Classification metric |

---

## Last-Minute 48-Hour Checklist

### 48 Hours Before Exam
- [ ] Review all one-line summaries above
- [ ] Solve at least 2 past exam papers
- [ ] Review all formulas
- [ ] Check lab assignments
- [ ] Sleep ≥ 7 hours

### 24 Hours Before Exam
- [ ] Light revision of weak topics only
- [ ] Revise this final revision sheet
- [ ] Prepare exam materials (pen, ID card, etc.)
- [ ] Sleep early (at least 8 hours)

### Morning of Exam
- [ ] Eat a proper breakfast
- [ ] Quickly skim formula reference
- [ ] Arrive 15 minutes early
- [ ] Stay calm - you've prepared well! 

---

## Related Notes

- [[06-Revision/Monthly/Monthly-Review]] - Monthly progress
- [[06-Revision/Weekly/Weekly-Summary]] - Weekly breakdown
- [[05-Projects/Semester-V-Project/Project-Overview]] - Project reference
- [[11-Tracking/Exam-Tasks]] - Exam schedule database

---

*TY B.Sc. CS - Semester V Final Revision Sheet | Updated: 2026-06-16*
