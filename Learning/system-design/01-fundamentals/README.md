# 🏗️ System Design Fundamentals

**Phase 1: Core Concepts (1-2 Weeks)**

---

## 📖 Overview

Master the fundamental concepts that form the foundation of system design. These principles apply to all distributed systems.

---

## 🎯 Core Concepts

### 1. Scalability

**Definition:** Ability of a system to handle growing workload.

**Types:**

**Vertical Scaling (Scale Up)**
- Add more power to existing machine (CPU, RAM, Storage)
- ✅ Simple to implement
- ❌ Hardware limits
- ❌ Single point of failure
- ❌ Expensive

**Horizontal Scaling (Scale Out)**
- Add more machines to system
- ✅ No hardware limits
- ✅ Better fault tolerance
- ✅ Cost-effective
- ❌ Complex implementation
- ❌ Data consistency challenges

**Example:**
```
Vertical Scaling:
Server: 4 CPU, 8GB RAM → 16 CPU, 64GB RAM

Horizontal Scaling:
1 Server → 10 Servers (Load Balanced)
```

---

### 2. Performance Metrics

**Latency vs Throughput:**

**Latency:**
- Time to complete single request
- Measured in milliseconds (ms)
- Lower is better
- Example: API response time

**Throughput:**
- Number of requests per unit time
- Measured in requests/second (RPS)
- Higher is better
- Example: 10,000 RPS

**Trade-off:**
- High throughput can increase latency
- Low latency might reduce throughput
- Balance based on requirements

---

### 3. Availability

**Definition:** Percentage of time system is operational.

**Availability Levels:**
| Level | Downtime/Year | Use Case |
|-------|--------------|----------|
| 99% (2 nines) | 3.65 days | Internal tools |
| 99.9% (3 nines) | 8.76 hours | Standard apps |
| 99.99% (4 nines) | 52.56 minutes | E-commerce |
| 99.999% (5 nines) | 5.26 minutes | Banking |
| 99.9999% (6 nines) | 31.56 seconds | Mission critical |

**Achieving High Availability:**
1. **Redundancy**: Multiple servers
2. **Load Balancing**: Distribute traffic
3. **Health Checks**: Monitor servers
4. **Failover**: Automatic recovery
5. **Geographic Distribution**: Multiple regions

---

### 4. CAP Theorem

**States:** You can have only 2 of 3:

**Consistency (C):**
- All nodes see same data at same time
- Every read receives most recent write

**Availability (A):**
- Every request gets response (success/failure)
- System always responds

**Partition Tolerance (P):**
- System continues despite network failures
- Always required in distributed systems

**In Reality:** Choose between CP or AP

**CP Systems (Consistency + Partition Tolerance):**
- Banking systems
- Inventory management
- Booking systems
- Examples: MongoDB, HBase, Redis

**AP Systems (Availability + Partition Tolerance):**
- Social media feeds
- Analytics
- Caching systems
- Examples: Cassandra, DynamoDB, Riak

---

### 5. Consistency Models

**Strong Consistency:**
- All reads return most recent write
- High latency
- Example: Banking transactions

**Eventual Consistency:**
- Reads might return stale data temporarily
- Low latency
- Example: Social media likes

**Causal Consistency:**
- Related operations ordered
- Independent operations unordered
- Balance between strong and eventual

---

### 6. Load Balancing

**Purpose:** Distribute traffic across multiple servers

**Algorithms:**

**1. Round Robin:**
```
Server 1 → Server 2 → Server 3 → Server 1 ...
```
- Simple
- Equal distribution
- Ignores server load

**2. Least Connections:**
```
Send to server with fewest active connections
```
- Better for long-lived connections
- More complex

**3. Weighted Round Robin:**
```
Server 1 (weight 3) gets 3x traffic of Server 2 (weight 1)
```
- Account for server capacity
- Flexible

**4. IP Hash:**
```
hash(client_ip) % server_count
```
- Same client → same server
- Good for sessions

**Load Balancer Types:**

**Layer 4 (Transport Layer):**
- Routes based on IP and port
- Fast
- Limited routing logic

**Layer 7 (Application Layer):**
- Routes based on content (URL, headers)
- More intelligent routing
- SSL termination

---

### 7. Caching

**Purpose:** Store frequently accessed data in fast storage

**Cache Levels:**
```
Client → CDN → Load Balancer → Application Cache → Database Cache → Database
```

**Benefits:**
- ✅ Reduce latency
- ✅ Reduce database load
- ✅ Cost savings
- ❌ Cache invalidation complexity
- ❌ Stale data risk

**When to Cache:**
- Frequently read data
- Computation-heavy results
- Slow database queries
- Static content

---

### 8. Database Strategies

**Replication:**
```
Master DB → Replica 1
         → Replica 2
         → Replica 3
```
- Reads from replicas
- Writes to master
- High availability

**Sharding (Partitioning):**
```
Users A-M → Shard 1
Users N-Z → Shard 2
```
- Horizontal partitioning
- Distribute data across servers
- Scale database writes

---

### 9. Message Queues

**Purpose:** Async communication between services

**Benefits:**
- Decoupling
- Load leveling
- Reliability
- Scalability

**Example Flow:**
```
Producer → Message Queue → Consumer
Service A → RabbitMQ/Kafka → Service B
```

**Use Cases:**
- Email notifications
- Order processing
- Video encoding
- Data analytics

---

### 10. Microservices vs Monolith

**Monolithic Architecture:**
```
┌─────────────────────┐
│   Single Application │
│ ┌─────────────────┐ │
│ │   All Features  │ │
│ └─────────────────┘ │
└─────────────────────┘
```

**Pros:**
- ✅ Simple development
- ✅ Easy deployment
- ✅ Simple testing

**Cons:**
- ❌ Scale entire app
- ❌ Technology lock-in
- ❌ Large codebase

**Microservices Architecture:**
```
┌─────────┐  ┌─────────┐  ┌─────────┐
│ Service │  │ Service │  │ Service │
│    A    │  │    B    │  │    C    │
└─────────┘  └─────────┘  └─────────┘
```

**Pros:**
- ✅ Independent scaling
- ✅ Technology flexibility
- ✅ Team autonomy

**Cons:**
- ❌ Complex deployment
- ❌ Network overhead
- ❌ Distributed challenges

---

## 🎯 Key Numbers to Know

### Storage

```
1 KB  = 1,000 bytes = 10³
1 MB  = 1,000 KB = 10⁶
1 GB  = 1,000 MB = 10⁹
1 TB  = 1,000 GB = 10¹²
1 PB  = 1,000 TB = 10¹⁵
```

### Latency

```
RAM access:           100 ns
SSD read:             150 µs
HDD read:             10 ms
Network (same DC):    500 µs
Network (cross DC):   150 ms
```

### Capacity Planning

```
1 Million users
- Storage: 1 user = 10 KB → 10 GB
- Requests: 1 user = 10 req/day → 10M req/day
- Bandwidth: 10M req × 100 KB → 1 TB/day
```

---

## ✅ Interview Checklist

### Questions to Ask

**Functional Requirements:**
- What features are needed?
- Who are the users?
- What are core use cases?

**Non-Functional Requirements:**
- Expected scale (users, requests)?
- Latency requirements?
- Availability requirements?
- Consistency requirements?

**Constraints:**
- Budget?
- Timeline?
- Technology preferences?

---

**👉 Next:** [Scalability →](../02-scalability/README.md)

---

**💡 Pro Tip:** Always start with requirements clarification. Don't jump to solutions!

