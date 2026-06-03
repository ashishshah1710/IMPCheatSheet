# 💡 Simple Explanations & Interview Prep — Master Index

**Plain-English summaries and must-know interview questions for every topic in this repo.**

Use this when you want a quick refresh before an interview. Each folder's `README.md` also has its own **Simple Explanation** and **Interview Quick Prep** at the bottom.

---

## How to Use This Guide

1. **Skim** the simple explanation for the topic you're revising
2. **Practice** the 3–5 interview questions out loud (don't just read)
3. **Open** the linked folder for code examples and deep dives
4. **Cross-check** with `interview-questions/` folders where they exist

---

## ☕ Java Core

| Topic | In Simple Words | Top Interview Question |
|-------|-----------------|------------------------|
| [01-beginner](../java-core/01-beginner/README.md) | Java basics: variables, loops, arrays, methods | What is JVM and why does Java need it? |
| [02-intermediate](../java-core/02-intermediate/README.md) | OOP, collections, exceptions, generics | Difference between `ArrayList` and `LinkedList`? |
| [03-advanced](../java-core/03-advanced/README.md) | JVM, threads, design patterns, Java 8+ | How does garbage collection work? |
| [Interview Q&A](../java-core/interview-questions/README.md) | Full Java interview bank with simple answers | Explain `HashMap` internal working |

**Must-know:** 8 primitives, stack vs heap, `==` vs `.equals()`, collections time complexity, thread safety basics.

---

## 🌱 Spring Framework & Spring Boot

| Topic | In Simple Words | Top Interview Question |
|-------|-----------------|------------------------|
| [Spring Core](../spring-framework/01-core-concepts/README.md) | IoC container creates and wires objects for you | What is Dependency Injection? |
| [Spring MVC](../spring-framework/02-spring-mvc/README.md) | Handles web requests: controller → service → view | Request lifecycle in Spring MVC? |
| [Data Access](../spring-framework/03-data-access/README.md) | JPA/Hibernate talk to the database | `@Transactional` — how does it work? |
| [AOP & Security](../spring-framework/04-aop-security/README.md) | Cross-cutting logic (logging, security) without clutter | What is AOP? Give a real example |
| [Spring Boot](../spring-boot/01-fundamentals/README.md) | Spring with auto-config — less XML, faster start | What is auto-configuration? |
| [REST APIs](../spring-boot/02-rest-apis/README.md) | Build HTTP APIs with annotations | Difference between `@Controller` and `@RestController`? |
| [Microservices](../spring-boot/microservices/README.md) | Small independent services that talk over network | Monolith vs microservices — when to choose? |

**Must-know:** Bean lifecycle, `@Autowired` types, REST status codes, application.properties vs YAML, actuator endpoints.

---

## 📊 Data Structures & Algorithms

| Topic | In Simple Words | Top Interview Question |
|-------|-----------------|------------------------|
| [Arrays & Strings](../dsa/01-arrays-strings/README.md) | Fixed lists and text — foundation of most problems | Two-pointer technique — when to use? |
| [Linked Lists](../dsa/02-linked-lists/README.md) | Nodes chained together — fast insert, slow random access | Detect cycle in linked list |
| [Stacks & Queues](../dsa/03-stacks-queues/README.md) | LIFO and FIFO — used in parsing, BFS | Valid parentheses using stack |
| [Trees](../dsa/04-trees/README.md) | Hierarchical data — BST, traversals | In-order vs pre-order traversal |
| [Graphs](../dsa/05-graphs/README.md) | Nodes and edges — networks, maps | BFS vs DFS — when to use each? |
| [Sorting & Searching](../dsa/06-sorting-searching/README.md) | Organize and find data fast | Time complexity of merge sort vs quick sort |
| [Dynamic Programming](../dsa/07-dynamic-programming/README.md) | Break problem into overlapping sub-problems | What is memoization? |

**Must-know:** Big-O notation, hash map for O(1) lookup, sliding window, two pointers, know 2–3 problems per pattern.

---

## 💾 Databases (SQL & NoSQL)

| Topic | In Simple Words | Top Interview Question |
|-------|-----------------|------------------------|
| [MongoDB](../mongodb/README.md) | Document DB — JSON-like docs, flexible schema | Embedding vs referencing documents |
| [Couchbase](../couchbase/README.md) | Distributed NoSQL with SQL-like N1QL | Couchbase vs MongoDB — key differences |
| [Kafka](../kafka/README.md) | Event streaming — producers send, consumers read | What is a Kafka topic and partition? |
| [Redis](../redis/README.md) | In-memory key-value store — super fast cache | Cache-aside pattern — how does it work? |
| [SQL](../sql-databases/README.md) | Relational tables with strict schema | INNER JOIN vs LEFT JOIN |
| [Elasticsearch](../elasticsearch/README.md) | Search engine for full-text and analytics | Inverted index — explain simply |

**Must-know:** CAP theorem basics, when NoSQL vs SQL, indexing, replication, eventual consistency.

---

## 🐳 DevOps & Cloud

| Topic | In Simple Words | Top Interview Question |
|-------|-----------------|------------------------|
| [Docker](../docker/01-beginner/README.md) | Package app + dependencies in a portable container | Image vs container? |
| [Kubernetes](../kubernetes/01-beginner/README.md) | Orchestrates containers across many machines | Pod vs Deployment vs Service |
| [AWS](../aws/01-beginner/README.md) | Amazon's cloud — servers, storage, databases on demand | EC2 vs Lambda — when to use? |
| [Git](../git/01-basics/README.md) | Version control — track and merge code changes | `merge` vs `rebase` |

**Must-know:** CI/CD pipeline flow, container vs VM, load balancer, health checks, 12-factor app basics.

---

## 🏗️ System Design

| Topic | In Simple Words | Top Interview Question |
|-------|-----------------|------------------------|
| [Fundamentals](../system-design/01-fundamentals/README.md) | Building blocks: clients, servers, databases | Explain client-server architecture |
| [Scalability](../system-design/02-scalability/README.md) | Handle more users without breaking | Horizontal vs vertical scaling |
| [Caching](../system-design/04-caching/README.md) | Store frequent data closer to user for speed | Cache invalidation strategies |
| [Microservices](../system-design/05-microservices/README.md) | Split system into small deployable services | API Gateway — why needed? |
| [Case Studies](../system-design/case-studies/README.md) | Design URL shortener, chat, etc. | Design a rate limiter |

**Must-know:** Load balancer, CDN, database sharding, message queue, idempotency, REST vs gRPC.

---

## 🌐 Frontend & Full Stack

| Topic | In Simple Words | Top Interview Question |
|-------|-----------------|------------------------|
| [Node.js](../nodejs/README.md) | JavaScript on the server | Event loop in Node — explain simply |
| [React](../reactjs/README.md) | UI library — build pages from components | Virtual DOM — why does React use it? |
| [TypeScript](../typescript/README.md) | JavaScript with types — fewer runtime bugs | Interface vs type in TypeScript |
| [Full Stack Java](../full-stack-java/README.md) | End-to-end Java path: backend + frontend | How does a REST call flow from React to DB? |

---

## 📅 4-Week Interview Revision Plan

| Week | Focus | Folders to Review |
|------|-------|-------------------|
| **Week 1** | Java + DSA | `java-core/`, `dsa/01`–`04`, `dsa/interview-questions/` |
| **Week 2** | Spring + DB | `spring-framework/`, `spring-boot/`, `mongodb/`, `kafka/` |
| **Week 3** | System Design + Advanced Java | `system-design/`, `java-core/03-advanced/` |
| **Week 4** | DevOps + Mock interviews | `docker/`, `kubernetes/`, `git/`, practice explaining out loud |

---

## 🗣️ How to Answer in Interviews (Simple Framework)

1. **One-line definition** — say what it is in plain English
2. **Why it matters** — real problem it solves
3. **How it works** — 2–3 steps or a quick diagram
4. **Example** — from your project or a common scenario
5. **Trade-off** — when NOT to use it (shows depth)

**Example — "What is Docker?"**
> Docker packages your app and everything it needs into a container. It solves "works on my machine" because the same container runs everywhere. You build an image once, run containers from it. Trade-off: not a full VM — shares the host kernel, so isolation is lighter than a virtual machine.

---

## 🔗 Related Guides

- [Interview Prep — Enterprise Technologies](./INTERVIEW-PREP-TECHNOLOGIES.md)
- [Start Here](./START-HERE.md)
- [Navigation](./NAVIGATION.md)

---

**Tip:** Every topic README ends with **💡 Simple Explanation** and **🎯 Interview Quick Prep** — scroll to the bottom of any folder you're studying!
