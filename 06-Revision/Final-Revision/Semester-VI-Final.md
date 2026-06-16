---
title: Semester VI Final Revision
tags:
  - revision
  - final-revision
  - semester-vi
  - exam-prep
aliases:
  - Sem VI Final
  - Semester 6 Cheat Sheet
created: 2026-06-16
last_modified: 2026-06-16
---

#  Semester VI - Final Revision

> [!important] Last-Minute Strategy
> - Read in the last 48–72 hours before exam
> - Focus on ==highlighted terms== and formulas
> - Don't panic - reinforce what you already know!

---

##  CS-351 - Advanced Java

### Critical Topics
1. **JDBC** - Connection, Statement, PreparedStatement, ResultSet
2. **Servlets** - lifecycle, doGet, doPost, request/response, sessions
3. **JSP** - directives, scriptlets, expressions, JSTL, EL
4. **Hibernate / JPA** - ORM, annotations, CRUD operations
5. **Spring Framework** - IoC, DI, Spring Boot basics
6. **REST APIs** - HTTP methods, status codes, JSON, JAX-RS / Spring REST
7. **Collections Advanced** - Iterator, Comparator, Comparable, Stream API
8. **Design Patterns** - Singleton, Factory, Observer, MVC

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| JDBC | Java API for connecting to and executing queries on relational databases |
| Servlet | Server-side Java component handling HTTP requests/responses |
| JSP | Java Server Pages - HTML with embedded Java; compiled to servlet |
| Hibernate | ORM framework mapping Java objects to database tables |
| Spring IoC | Spring container manages object creation and dependency injection |
| REST | Stateless, resource-based architecture using HTTP methods |
| Singleton Pattern | Ensures only one instance of a class exists throughout application |
| Factory Pattern | Creates objects without specifying exact class to instantiate |

### Quick Reference Code

```java
// JDBC Connection
Connection conn = DriverManager.getConnection(url, user, pass);
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id=?");
ps.setInt(1, userId);
ResultSet rs = ps.executeQuery();

// Spring Boot REST endpoint
@RestController
@RequestMapping("/api")
public class UserController {
    @GetMapping("/users")
    public List<User> getAllUsers() { return userService.findAll(); }
    
    @PostMapping("/users")
    public User createUser(@RequestBody User user) { return userService.save(user); }
}

// Stream API
List<String> filtered = list.stream()
    .filter(s -> s.startsWith("A"))
    .sorted()
    .collect(Collectors.toList());
```

### Last-Minute Checklist - CS-351
- [ ] JDBC steps in order (Load Driver→Connect→Statement→Execute→Process→Close)
- [ ] Servlet lifecycle: init, service, destroy
- [ ] JSP implicit objects list
- [ ] Hibernate: @Entity, @Table, @Id, @Column annotations
- [ ] Spring DI: constructor vs setter injection
- [ ] HTTP methods: GET, POST, PUT, DELETE, PATCH
- [ ] Design patterns: Singleton with lazy initialization

---

##  CS-352 - Computer Networks

### Critical Topics
1. **OSI Model** - 7 layers, functions, protocols
2. **TCP/IP Model** - 4 layers, comparison with OSI
3. **IP Addressing** - IPv4, subnetting, CIDR, IPv6
4. **Routing** - RIP, OSPF, BGP, routing tables
5. **Transport Layer** - TCP vs UDP, 3-way handshake, flow/congestion control
6. **Application Layer** - HTTP, HTTPS, DNS, DHCP, FTP, SMTP
7. **Network Security** - SSL/TLS, firewalls, VPN, cryptography basics
8. **Wireless Networks** - WiFi (802.11), Bluetooth, cellular

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| OSI Model | 7-layer conceptual framework: Physical→Data Link→Network→Transport→Session→Presentation→Application |
| IP Address | 32-bit logical identifier for devices (IPv4) or 128-bit (IPv6) |
| Subnetting | Dividing a network into smaller subnetworks using subnet mask |
| TCP | Reliable, connection-oriented, ordered delivery with flow control |
| UDP | Unreliable, connectionless, fast delivery without guarantees |
| DNS | Translates domain names to IP addresses |
| DHCP | Automatically assigns IP addresses to devices on a network |
| SSL/TLS | Cryptographic protocols for secure data transmission over networks |

### Key Formulas & Tables

```
Subnetting:
Hosts per subnet = 2^(host bits) - 2
Subnets = 2^(subnet bits)

IPv4 Classes:
Class A: 1.0.0.0 – 126.255.255.255  /8
Class B: 128.0.0.0 – 191.255.255.255 /16
Class C: 192.0.0.0 – 223.255.255.255 /24

TCP 3-Way Handshake: SYN → SYN-ACK → ACK
TCP 4-Way Termination: FIN → ACK → FIN → ACK

Bandwidth-Delay Product = Bandwidth × RTT
Throughput = min(send_rate, receive_rate, bottleneck_link)
```

### OSI Layer Quick Reference

| Layer | Name | Protocol | PDU |
|-------|------|---------|-----|
| 7 | Application | HTTP, FTP, DNS, SMTP | Data |
| 6 | Presentation | SSL, TLS, JPEG | Data |
| 5 | Session | NetBIOS, RPC | Data |
| 4 | Transport | TCP, UDP | Segment |
| 3 | Network | IP, ICMP, ARP | Packet |
| 2 | Data Link | Ethernet, PPP | Frame |
| 1 | Physical | USB, Fiber | Bits |

### Last-Minute Checklist - CS-352
- [ ] Draw OSI 7 layers with protocols from memory
- [ ] Calculate subnet mask given CIDR notation
- [ ] TCP handshake sequence (SYN, SYN-ACK, ACK)
- [ ] Difference: TCP vs UDP with use cases
- [ ] DNS resolution process step by step
- [ ] Routing: distance vector vs link state

---

##  CS-353 - Web Technology-II

### Critical Topics
1. **React.js** - components, props, state, hooks, lifecycle
2. **Angular / Vue.js** - directives, data binding, routing
3. **Database Integration** - MySQL with Node.js, MongoDB with Mongoose
4. **REST API Design** - CRUD with Express.js, authentication with JWT
5. **Security** - XSS, CSRF, SQL injection prevention
6. **Deployment** - Nginx, Apache, cloud deployment basics
7. **WebSockets** - real-time communication, Socket.io

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| React Component | Reusable UI piece - functional or class-based |
| React Hooks | Functions (useState, useEffect) that add state to functional components |
| Props | Read-only data passed from parent to child component |
| State | Internal, mutable data of a component |
| JWT | Stateless token for authentication: header.payload.signature |
| XSS | Cross-Site Scripting - attacker injects malicious scripts into web pages |
| CSRF | Cross-Site Request Forgery - tricks user's browser into making unauthorized requests |
| WebSocket | Full-duplex communication channel over a single TCP connection |

### Quick Reference

```jsx
// React functional component with hooks
import React, { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);
  
  useEffect(() => {
    fetch('/api/users').then(r => r.json()).then(setUsers);
  }, []);
  
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

// JWT verification (Express middleware)
const jwt = require('jsonwebtoken');
function authMiddleware(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
}
```

### Last-Minute Checklist - CS-353
- [ ] React component lifecycle (class-based)
- [ ] useState vs useRef vs useContext
- [ ] useEffect: dependencies array behavior
- [ ] REST API: proper HTTP status codes
- [ ] JWT structure and flow
- [ ] How to prevent SQL injection (parameterized queries)
- [ ] Same-Origin Policy and CORS

---

##  CS-354 - Compiler Construction

### Critical Topics
1. **Compiler Phases** - Lexical → Syntax → Semantic → IR → Optimization → Code Gen
2. **Lexical Analysis** - tokens, lexemes, patterns, LEX/FLEX
3. **Syntax Analysis** - parse trees, CFG, top-down vs bottom-up parsing
4. **Parsing Techniques** - LL(1), LR(0), SLR(1), LALR(1), CLR(1)
5. **Semantic Analysis** - type checking, scope analysis, symbol table
6. **Intermediate Code** - three-address code, quadruples, DAG
7. **Code Optimization** - constant folding, dead code elimination, loop optimization
8. **Code Generation** - register allocation, instruction selection

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| Lexical Analysis | Converts source code into sequence of tokens |
| Token | Atomic unit of language (keyword, identifier, operator, literal) |
| Parse Tree | Tree representation of syntactic structure of a program |
| AST | Abstract Syntax Tree - simplified parse tree without redundant nodes |
| LL(1) | Left-to-right scan, Leftmost derivation, 1 token lookahead; top-down |
| LR(0) | Left-to-right scan, Rightmost derivation; bottom-up parsing |
| LALR(1) | Merges LR(1) states with same core; practical parser (used by YACC) |
| Symbol Table | Data structure mapping identifiers to type, scope, and value info |

### Compiler Phases Diagram

```
Source Code
    ↓
[Lexical Analyzer] → Tokens
    ↓
[Syntax Analyzer] → Parse Tree
    ↓
[Semantic Analyzer] → Annotated Tree
    ↓
[Intermediate Code Generator] → IR Code
    ↓
[Code Optimizer] → Optimized IR
    ↓
[Code Generator] → Target Code
```

### Key Concepts

```
FIRST(A)  = set of terminals that can begin strings derived from A
FOLLOW(A) = set of terminals that can appear immediately after A

LL(1) Parsing Table Construction:
  For each production A → α:
    For each terminal a in FIRST(α): add A → α to M[A,a]
    If ε ∈ FIRST(α): for each terminal b in FOLLOW(A): add A → α to M[A,b]

Three-Address Code example:
  a = b + c * d
  → t1 = c * d
  → t2 = b + t1
  → a = t2
```

### Last-Minute Checklist - CS-354
- [ ] All 6 compiler phases with outputs
- [ ] Difference: compiler vs interpreter
- [ ] Construct FIRST and FOLLOW sets
- [ ] Build LL(1) parsing table
- [ ] LR(0) items and closure/goto operations
- [ ] SLR vs LALR vs CLR difference
- [ ] Write 3-address code for given expression
- [ ] Common code optimizations list

---

##  CS-357 - Cloud Computing

### Critical Topics
1. **Cloud Fundamentals** - characteristics, deployment models, service models
2. **Service Models** - IaaS, PaaS, SaaS with examples
3. **Deployment Models** - Public, Private, Hybrid, Community cloud
4. **Virtualization** - hypervisors (Type 1 & 2), containers, Docker
5. **Cloud Platforms** - AWS, Azure, GCP services overview
6. **Storage** - object storage, block storage, distributed file systems
7. **Security** - cloud security challenges, IAM, encryption
8. **Scalability** - auto-scaling, load balancing, microservices

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| IaaS | Infrastructure as a Service - rent virtualized hardware (EC2, Azure VMs) |
| PaaS | Platform as a Service - develop/deploy apps without managing infra (Heroku, App Engine) |
| SaaS | Software as a Service - use software over internet (Gmail, Salesforce) |
| Hypervisor | Software creating and managing virtual machines on physical hardware |
| Docker | Container platform packaging app with dependencies for consistent deployment |
| Kubernetes | Orchestration system for automating Docker container deployment and scaling |
| Auto-scaling | Automatically adding/removing instances based on load |
| IAM | Identity and Access Management - controls who can do what in cloud |

### Service Model Comparison

| Model | You Manage | Provider Manages | Example |
|-------|-----------|-----------------|---------|
| IaaS | OS, Runtime, App | Hardware, Network, Storage | AWS EC2 |
| PaaS | App, Data | Everything else | Heroku, GAE |
| SaaS | Just use it | Everything | Gmail, Office 365 |

### Last-Minute Checklist - CS-357
- [ ] 5 essential NIST characteristics of cloud
- [ ] Difference: IaaS vs PaaS vs SaaS with examples
- [ ] Type 1 vs Type 2 hypervisor
- [ ] Docker vs Virtual Machine comparison
- [ ] CAP theorem (Consistency, Availability, Partition tolerance)
- [ ] AWS core services: EC2, S3, RDS, Lambda
- [ ] Cloud security: shared responsibility model

---

##  CS-371 - Android Development

### Critical Topics
1. **Android Architecture** - Linux Kernel, HAL, ART, Framework, Apps
2. **Activity Lifecycle** - onCreate, onStart, onResume, onPause, onStop, onDestroy
3. **Intents** - explicit vs implicit, Intent Filters
4. **UI Components** - Views, ViewGroups, Fragments, RecyclerView
5. **Data Storage** - SharedPreferences, SQLite, Room, files
6. **Networking** - Retrofit, Volley, OkHttp
7. **Background Work** - Services, BroadcastReceivers, WorkManager
8. **Jetpack Compose** - declarative UI basics (if in syllabus)

### One-Line Summaries

| Topic | One-Line Summary |
|-------|-----------------|
| Activity | Single screen with UI; fundamental building block of Android apps |
| Fragment | Reusable portion of UI that can be combined within activities |
| Intent | Message object for starting activities, services, or delivering broadcasts |
| RecyclerView | Efficient scrollable list/grid view replacing ListView |
| ViewModel | Stores UI-related data that survives configuration changes |
| Room | SQLite abstraction layer with compile-time query verification |
| Retrofit | Type-safe HTTP client for Android API calls |
| Service | Background component performing long-running operations without UI |

### Activity Lifecycle Diagram

```
       [App Launch]
            ↓
        onCreate()
            ↓
        onStart()
            ↓
        onResume()  ← ─── ─── ─── ─── ─── ─── ┐
            ↓                                   │
      [App Visible & Active]                    │
            ↓                              onRestart()
        onPause()                               │
            ↓                                   │
        onStop()  ─── ─── ─── ─── ─── ─── ─── ┘
            ↓
       onDestroy()
            ↓
      [App Terminated]
```

### Quick Reference Code

```kotlin
// Explicit Intent
val intent = Intent(this, SecondActivity::class.java)
intent.putExtra("key", "value")
startActivity(intent)

// RecyclerView Adapter
class MyAdapter(private val items: List<String>) 
    : RecyclerView.Adapter<MyAdapter.ViewHolder>() {
    
    class ViewHolder(view: View) : RecyclerView.ViewHolder(view)
    
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_layout, parent, false)
        return ViewHolder(view)
    }
    
    override fun onBindViewHolder(holder: ViewHolder, position: Int) { 
        // bind data
    }
    
    override fun getItemCount() = items.size
}
```

### Last-Minute Checklist - CS-371
- [ ] Android 5-layer architecture
- [ ] Activity lifecycle: 6 methods in order
- [ ] Fragment lifecycle vs Activity lifecycle
- [ ] Explicit vs Implicit intent with examples
- [ ] RecyclerView: Adapter, ViewHolder, LayoutManager
- [ ] SharedPreferences vs Room: when to use
- [ ] Permission model: normal vs dangerous

---

##  Formula Quick Reference - Semester VI

| Formula | Subject | Context |
|---------|---------|---------|
| Hosts = 2^h - 2 | CN | Subnetting |
| Subnets = 2^s | CN | Subnetting |
| EAT = h×t1 + (1-h)×t2 | CN | Cache memory |
| Throughput = min(links) | CN | Bottleneck |
| FIRST/FOLLOW | CC | Parsing table construction |
| t1=c*d → t2=b+t1 | CC | 3-address code pattern |

---

##  Last-Minute 48-Hour Checklist - Semester VI

### 48 Hours Before Exam
- [ ] Review all one-line summaries
- [ ] Solve 2 past exam papers per subject
- [ ] Revise all code snippets and algorithms
- [ ] Check lab assignments for each subject
- [ ] Sleep ≥ 7 hours

### 24 Hours Before Exam
- [ ] Light revision of weak topics only
- [ ] Revise this final revision sheet
- [ ] Prepare exam materials
- [ ] Sleep early - at least 8 hours!

### Morning of Exam
- [ ] Eat a proper breakfast
- [ ] Quickly skim formula reference
- [ ] Arrive 15 minutes early
- [ ] You've got this! 

---

##  Related Notes

- [[06-Revision/Final-Revision/Semester-V-Final]] - Semester V reference
- [[06-Revision/Monthly/Monthly-Review]] - Monthly progress
- [[05-Projects/Semester-VI-OJT/OJT-Overview]] - OJT reference
- [[11-Tracking/Exam-Tasks]] - Exam schedule database

---

*TY B.Sc. CS - Semester VI Final Revision Sheet | Updated: 2026-06-16*
