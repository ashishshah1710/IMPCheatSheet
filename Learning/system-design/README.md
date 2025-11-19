# 🏗️ System Design

**For 3.5+ Years Experienced Developers | Interview Preparation**

Master System Design for senior engineering roles and architect positions!

---

## 📖 Overview

System Design is crucial for senior developer interviews. It tests your ability to design scalable, reliable, and maintainable systems. Essential for roles at FAANG and top tech companies.

### Why System Design?

✅ **Senior Roles** - Required for L5+ positions  
✅ **Architecture Skills** - Design scalable systems  
✅ **Real-World Impact** - Solve actual business problems  
✅ **High Compensation** - Commands premium salaries  
✅ **Leadership** - Technical decision making  
✅ **Career Growth** - Path to Staff/Principal Engineer  

---

## 🎯 Learning Path

### Phase 1: Fundamentals (1-2 weeks)
**Core concepts and building blocks**

- Scalability basics
- Performance vs Scalability
- Latency vs Throughput
- CAP Theorem
- ACID vs BASE
- Vertical vs Horizontal scaling
- Load balancing

**👉 Start:** [`01-fundamentals/README.md`](01-fundamentals/README.md)

---

### Phase 2: Scalability (1-2 weeks)
**Scaling systems**

- Load Balancers
- Reverse Proxies
- Application layer scaling
- Database scaling (Replication, Sharding)
- Caching strategies
- CDN (Content Delivery Network)
- Message Queues

**👉 Continue:** [`02-scalability/README.md`](02-scalability/README.md)

---

### Phase 3: Databases (1-2 weeks)
**Data storage strategies**

- SQL vs NoSQL
- Database sharding
- Replication strategies
- Indexing
- ACID properties
- Eventual consistency
- Database selection criteria

**👉 Master:** [`03-databases/README.md`](03-databases/README.md)

---

### Phase 4: Caching (1 week)
**Speed up your systems**

- Cache strategies (LRU, LFU)
- Cache patterns (Cache-aside, Write-through)
- Redis architecture
- Memcached
- Cache invalidation
- CDN caching
- Browser caching

**👉 Advanced:** [`04-caching/README.md`](04-caching/README.md)

---

### Phase 5: Microservices (1-2 weeks)
**Modern architecture**

- Microservices vs Monolith
- Service discovery
- API Gateway
- Circuit breakers
- Saga pattern
- Event-driven architecture
- Service mesh

**👉 Advanced:** [`05-microservices/README.md`](05-microservices/README.md)

---

### Phase 6: Real-World Systems (2-3 weeks)
**Design popular systems**

- URL Shortener
- Twitter/Social Media
- WhatsApp/Chat System
- YouTube/Video Streaming
- Uber/Ride Sharing
- Instagram
- Amazon/E-commerce
- Netflix
- Google Search

**👉 Practice:** [`06-real-world-systems/README.md`](06-real-world-systems/README.md)

---

## 💼 Interview Preparation

### System Design Interview Format

**Duration:** 45-60 minutes

**Structure:**
1. **Requirements (5-10 min)**: Clarify functional & non-functional requirements
2. **High-Level Design (10-15 min)**: Draw architecture diagram
3. **Deep Dive (20-30 min)**: Detailed component design
4. **Trade-offs (5-10 min)**: Discuss alternatives

---

### Common System Design Questions

**Easy:**
1. Design a URL Shortener (bit.ly)
2. Design a Pastebin
3. Design a Key-Value Store
4. Design a Parking Lot System
5. Design a Rate Limiter

**Medium:**
6. Design Twitter
7. Design Instagram
8. Design WhatsApp/Messenger
9. Design Uber/Lyft
10. Design YouTube
11. Design Netflix
12. Design TikTok
13. Design LinkedIn
14. Design Dropbox
15. Design Google Drive

**Hard:**
16. Design Google Search
17. Design Amazon E-commerce
18. Design Payment System
19. Design Distributed Cache
20. Design Stock Exchange

**👉 See:** [`interview-questions/README.md`](interview-questions/README.md)

---

## 📚 Content Structure

```
system-design/
├── 01-fundamentals/
│   ├── README.md                    # System design basics
│   ├── scalability.md              # Scalability concepts
│   ├── cap-theorem.md              # CAP theorem
│   └── load-balancing.md           # Load balancers
│
├── 02-scalability/
│   ├── README.md                    # Scaling strategies
│   ├── horizontal-scaling.md       # Scale out
│   ├── database-scaling.md         # DB scaling
│   └── caching.md                  # Caching layer
│
├── 03-databases/
│   ├── README.md                    # Database design
│   ├── sql-vs-nosql.md            # Database types
│   ├── sharding.md                # Partitioning
│   └── replication.md             # Data replication
│
├── 04-caching/
│   ├── README.md                    # Caching strategies
│   ├── redis.md                    # Redis architecture
│   ├── cdn.md                      # Content delivery
│   └── cache-patterns.md          # Caching patterns
│
├── 05-microservices/
│   ├── README.md                    # Microservices arch
│   ├── api-gateway.md             # API Gateway
│   ├── service-discovery.md       # Service registry
│   └── event-driven.md            # Event architecture
│
├── 06-real-world-systems/
│   ├── README.md                    # System designs
│   ├── url-shortener.md           # URL shortener
│   ├── twitter.md                 # Twitter design
│   ├── whatsapp.md                # Chat system
│   ├── youtube.md                 # Video streaming
│   ├── uber.md                    # Ride sharing
│   └── instagram.md               # Photo sharing
│
├── interview-questions/
│   ├── README.md                    # Interview prep
│   ├── approach.md                # How to approach
│   ├── checklist.md               # Interview checklist
│   └── common-mistakes.md         # Avoid these
│
├── case-studies/
│   ├── README.md                    # Real case studies
│   ├── netflix.md                 # Netflix architecture
│   ├── uber.md                    # Uber's tech stack
│   ├── airbnb.md                  # Airbnb design
│   └── amazon.md                  # Amazon services
│
└── CHEATSHEET.md                    # Quick reference
```

---

## 🎯 Key Concepts

### Scalability Principles

1. **Stateless Services**: No server-side state
2. **Horizontal Scaling**: Add more machines
3. **Load Balancing**: Distribute traffic
4. **Caching**: Speed up reads
5. **Database Optimization**: Sharding, replication
6. **Async Processing**: Queue-based systems
7. **CDN**: Static content delivery
8. **Microservices**: Independent services

---

### CAP Theorem

**Choose 2 of 3:**
- **Consistency**: All nodes see same data
- **Availability**: System always responds
- **Partition Tolerance**: Works despite network failures

**Examples:**
- **CP Systems**: Banking, inventory (need consistency)
- **AP Systems**: Social media, DNS (need availability)
- **CA Systems**: Traditional RDBMS (network reliable)

---

### Performance Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Latency** | Time to get response | < 100ms |
| **Throughput** | Requests per second | Depends on scale |
| **Availability** | Uptime percentage | 99.99% (4 nines) |
| **Consistency** | Data accuracy | Varies by system |

---

## 🏆 For Experienced Developers

### What Interviewers Expect

**Technical Knowledge:**
- Deep understanding of distributed systems
- Trade-offs between different approaches
- Real-world experience with scale
- Knowledge of modern technologies
- Performance optimization

**Design Process:**
1. **Gather Requirements**: Ask clarifying questions
2. **Estimate Scale**: Users, requests, storage
3. **Define APIs**: Core functionalities
4. **High-Level Design**: Components and flow
5. **Database Schema**: Data model
6. **Deep Dive**: Specific components
7. **Bottlenecks**: Identify and solve
8. **Trade-offs**: Discuss alternatives

**Communication:**
- Think aloud
- Draw diagrams
- Explain decisions
- Handle feedback
- Discuss trade-offs

---

## 📊 Numbers You Should Know

### Latency Comparison

```
L1 cache reference:              0.5 ns
Branch mispredict:               5 ns
L2 cache reference:              7 ns
Mutex lock/unlock:               25 ns
Main memory reference:           100 ns
Compress 1K with Zippy:          3,000 ns = 3 µs
Send 1K over 1 Gbps network:     10,000 ns = 10 µs
SSD random read:                 150,000 ns = 150 µs
Read 1 MB sequentially from SSD: 1,000,000 ns = 1 ms
Disk seek:                       10,000,000 ns = 10 ms
Read 1 MB from network:          10,000,000 ns = 10 ms
```

### Storage

```
1 KB = 1,000 bytes = 10³ bytes
1 MB = 1,000 KB = 10⁶ bytes
1 GB = 1,000 MB = 10⁹ bytes
1 TB = 1,000 GB = 10¹² bytes
1 PB = 1,000 TB = 10¹⁵ bytes
```

---

## 🎓 Learning Resources

### Books
- "Designing Data-Intensive Applications" by Martin Kleppmann
- "System Design Interview" by Alex Xu (Volumes 1 & 2)
- "Web Scalability for Startup Engineers" by Artur Ejsmont
- "Building Microservices" by Sam Newman

### Websites
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [High Scalability](http://highscalability.com/)
- [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- [Netflix Tech Blog](https://netflixtechblog.com/)

### Courses
- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)
- [System Design Course by ByteByteGo](https://bytebytego.com/)
- Coursera: Cloud Computing Concepts

---

## ✅ Preparation Checklist

### Week 1-2: Fundamentals
- [ ] CAP Theorem
- [ ] Scalability basics
- [ ] Load balancing
- [ ] Caching basics
- [ ] Database fundamentals

### Week 3-4: Components
- [ ] API design
- [ ] Database design
- [ ] Caching strategies
- [ ] Message queues
- [ ] CDN usage

### Week 5-6: Systems
- [ ] Design 10 common systems
- [ ] Practice whiteboarding
- [ ] Calculate capacity
- [ ] Identify bottlenecks
- [ ] Discuss trade-offs

### Week 7-8: Practice
- [ ] Mock interviews
- [ ] Time yourself (45 min)
- [ ] Get feedback
- [ ] Review case studies
- [ ] Study tech blogs

---

## 🚀 Career Impact

### Salary Ranges (with System Design skills)

**3-5 Years:**
- **Backend Engineer** - $120K-$160K
- **Senior Engineer** - $150K-$200K

**5-7 Years:**
- **Staff Engineer** - $180K-$250K
- **Principal Engineer** - $220K-$320K

**FAANG (Senior+):**
- **L5/E5** - $300K-$450K
- **L6/E6** - $450K-$600K
- **L7/E7** - $600K-$900K+

---

## 🔗 Quick Links

| Topic | Link |
|-------|------|
| Fundamentals | [01-fundamentals/README.md](01-fundamentals/README.md) |
| Scalability | [02-scalability/README.md](02-scalability/README.md) |
| Databases | [03-databases/README.md](03-databases/README.md) |
| Caching | [04-caching/README.md](04-caching/README.md) |
| Microservices | [05-microservices/README.md](05-microservices/README.md) |
| Real-World Systems | [06-real-world-systems/README.md](06-real-world-systems/README.md) |
| Interview Questions | [interview-questions/README.md](interview-questions/README.md) |
| Case Studies | [case-studies/README.md](case-studies/README.md) |
| Cheat Sheet | [CHEATSHEET.md](CHEATSHEET.md) |

---

## 🎯 Next Steps

1. **Start with Fundamentals** - [`01-fundamentals/README.md`](01-fundamentals/README.md)
2. **Design Daily** - Practice one system per day
3. **Read Tech Blogs** - Learn from companies at scale
4. **Mock Interviews** - Practice with peers
5. **Build Systems** - Apply concepts in projects

---

**Ready to master System Design?** 🏗️

👉 **[Start with Fundamentals →](01-fundamentals/README.md)**

---

**💡 Pro Tip:** System Design interviews test your thought process, not memorization. Focus on understanding trade-offs and communicating clearly!

