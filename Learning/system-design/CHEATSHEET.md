# 🏗️ System Design Cheat Sheet

**Quick Reference Guide**

---

## CAP Theorem

**Choose 2 of 3:**
- **C**onsistency: All nodes see same data
- **A**vailability: System always responds
- **P**artition Tolerance: Works despite network failures

**Examples:**
- **CP**: Banking, MongoDB
- **AP**: Social media, Cassandra

---

## Availability Levels

| Nines | Uptime | Downtime/Year | Use Case |
|-------|--------|---------------|----------|
| 99% | Two nines | 3.65 days | Internal tools |
| 99.9% | Three nines | 8.76 hours | Standard |
| 99.99% | Four nines | 52.56 minutes | E-commerce |
| 99.999% | Five nines | 5.26 minutes | Banking |

---

## Latency Numbers

```
RAM access:             100 ns
SSD read:               150 µs
HDD seek:               10 ms
Network (same DC):      500 µs
Network (CA to NY):     50 ms
Network (US to EU):     150 ms
```

---

## Load Balancing Algorithms

1. **Round Robin**: Distribute equally
2. **Least Connections**: Send to least busy
3. **IP Hash**: Same client → same server
4. **Weighted**: Based on capacity

---

## Caching Strategies

### Cache Patterns

**1. Cache-Aside**
```
Read: Check cache → If miss, read DB → Update cache
Write: Write to DB → Invalidate cache
```

**2. Write-Through**
```
Write: Write to cache → Sync write to DB
Read: Check cache → If miss, read DB
```

**3. Write-Behind**
```
Write: Write to cache → Async write to DB
Read: Check cache
```

### Eviction Policies
- **LRU**: Least Recently Used
- **LFU**: Least Frequently Used
- **FIFO**: First In First Out
- **TTL**: Time To Live

---

## Database Strategies

### Replication
```
Master-Slave:
Write → Master
Read → Slaves

Master-Master:
Write → Any Master
Read → Any Master
```

### Sharding
```
Horizontal: Split rows across servers
Vertical: Split columns across servers
```

**Shard Keys:**
- User ID
- Geographic location
- Hash-based
- Range-based

---

## Scaling Patterns

### Vertical Scaling (Scale Up)
```
✅ Simple
❌ Hardware limits
❌ Single point of failure
```

### Horizontal Scaling (Scale Out)
```
✅ No limits
✅ Fault tolerant
❌ Complex
❌ Data consistency
```

---

## System Design Interview Template

### 1. Requirements (5 min)
- Functional requirements
- Non-functional requirements
- Scale estimates

### 2. Capacity Estimation (5 min)
- Users (total, DAU)
- Requests per second
- Storage needs
- Bandwidth

### 3. API Design (5 min)
```
POST /resource
GET /resource/{id}
PUT /resource/{id}
DELETE /resource/{id}
```

### 4. High-Level Design (15 min)
```
Client → Load Balancer → Servers
       ↓
    Cache → Database
```

### 5. Database Schema (10 min)
```sql
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    username VARCHAR(50),
    created_at TIMESTAMP
);
```

### 6. Deep Dive (15 min)
- Specific components
- Bottlenecks
- Optimizations

### 7. Trade-offs (5 min)
- Alternatives
- Pros/Cons
- Why this approach

---

## Capacity Calculation

### Storage
```
1 Million users × 1 KB/user = 1 GB
1 Million tweets/day × 500 bytes = 500 MB/day
```

### Requests
```
1 Million DAU × 50 requests/day = 50M requests/day
50M / 86400 seconds ≈ 580 requests/second
```

### Bandwidth
```
1000 requests/second × 100 KB = 100 MB/second
```

---

## Common Components

### CDN
- Static content delivery
- Global distribution
- Reduce latency

### Message Queue
- Async processing
- Decouple services
- Load leveling
- Examples: RabbitMQ, Kafka

### API Gateway
- Single entry point
- Authentication
- Rate limiting
- Routing

### Service Discovery
- Dynamic service registration
- Health checks
- Load balancing
- Examples: Consul, Eureka

---

## Database Selection

### SQL (Relational)
```
✅ ACID transactions
✅ Complex queries
✅ Structured data
❌ Scaling challenges

Use: Banking, E-commerce
Examples: PostgreSQL, MySQL
```

### NoSQL

**Document DB**
```
✅ Flexible schema
✅ Easy scaling
❌ Limited joins

Use: Content management
Example: MongoDB
```

**Key-Value**
```
✅ Very fast
✅ Simple
❌ Limited queries

Use: Caching, sessions
Example: Redis
```

**Column-Family**
```
✅ Large datasets
✅ Time-series data
❌ Complex queries

Use: Analytics
Example: Cassandra
```

**Graph DB**
```
✅ Relationships
❌ Complex
❌ Scaling

Use: Social networks
Example: Neo4j
```

---

## Performance Optimization

### Database
- Indexing
- Query optimization
- Connection pooling
- Read replicas
- Sharding

### Application
- Caching
- Async processing
- Load balancing
- CDN for static files
- Minimize network calls

### Network
- Compression
- HTTP/2
- CDN
- Persistent connections

---

## Monitoring Metrics

```
Latency: Response time
Throughput: Requests/second
Error Rate: Failed requests %
Saturation: Resource utilization
Availability: Uptime %
```

---

## Trade-offs to Discuss

### Consistency vs Availability
- Strong consistency: Lower availability
- Eventual consistency: Higher availability

### Latency vs Throughput
- Optimize one, sacrifice other
- Balance based on requirements

### SQL vs NoSQL
- SQL: ACID, complex queries
- NoSQL: Scalability, flexibility

### Monolith vs Microservices
- Monolith: Simpler, faster initially
- Microservices: Scalable, complex

---

## Quick Checklist

### Before Interview
- [ ] Review CAP theorem
- [ ] Know latency numbers
- [ ] Practice 10+ systems
- [ ] Draw diagrams
- [ ] Calculate capacity

### During Interview
- [ ] Clarify requirements
- [ ] Estimate capacity
- [ ] Draw high-level design
- [ ] Design database schema
- [ ] Discuss trade-offs
- [ ] Think aloud

---

**Happy Designing! 🏗️**

