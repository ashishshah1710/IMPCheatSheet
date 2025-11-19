# ⚡ Scalability Fundamentals

## Overview
Scalability is the ability of a system to handle increased load by adding resources. This guide covers essential scalability concepts for system design interviews.

---

## Types of Scalability

### 1. **Vertical Scaling (Scale Up)**
Adding more power to existing machines

#### ✅ Pros
- Simpler to implement
- No code changes needed
- Data consistency maintained
- Lower network latency

#### ❌ Cons
- Hardware limits
- Single point of failure
- Expensive at high tiers
- Downtime during upgrades

#### Example
```
Before: 4 CPU, 16GB RAM
After:  16 CPU, 64GB RAM
```

### 2. **Horizontal Scaling (Scale Out)**
Adding more machines to the system

#### ✅ Pros
- No hardware limits
- Better fault tolerance
- Cost-effective
- Gradual scaling

#### ❌ Cons
- Complex implementation
- Data consistency challenges
- Network overhead
- Load balancing needed

#### Example
```
Before: 1 server
After:  10 servers behind load balancer
```

---

## Load Balancing

### What is Load Balancing?
Distributes incoming traffic across multiple servers.

### Load Balancing Algorithms

#### 1. **Round Robin**
```
Request 1 → Server A
Request 2 → Server B
Request 3 → Server C
Request 4 → Server A (repeat)
```
- Simple and fair
- No server state needed
- Doesn't consider server load

#### 2. **Least Connections**
```
Server A: 10 connections
Server B: 5 connections  ← Routes here
Server C: 15 connections
```
- Better for long-lived connections
- Requires tracking connections

#### 3. **Weighted Round Robin**
```
Server A (weight 3): Gets 3 requests
Server B (weight 1): Gets 1 request
Server C (weight 2): Gets 2 requests
```
- Different server capacities
- Manual weight configuration

#### 4. **IP Hash**
```
hash(client_ip) % num_servers = target_server
```
- Same client → same server
- Session affinity
- Poor distribution if few clients

#### 5. **Least Response Time**
- Routes to server with fastest response
- Requires health monitoring
- Best for performance

### Load Balancer Types

#### Layer 4 (Transport Layer)
- Routes based on IP and TCP/UDP port
- Fast and simple
- No content awareness
- **Example**: AWS Network Load Balancer

#### Layer 7 (Application Layer)
- Routes based on content (URL, headers, cookies)
- SSL termination
- Content-based routing
- **Example**: AWS Application Load Balancer, Nginx

### Example: Nginx Load Balancer
```nginx
upstream backend {
    least_conn;  # Load balancing method
    server backend1.example.com weight=3;
    server backend2.example.com;
    server backend3.example.com backup;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
```

---

## Caching Strategies

### Cache Levels

1. **Client-side (Browser Cache)**
2. **CDN Cache**
3. **Application Cache (Redis, Memcached)**
4. **Database Cache**

### Caching Patterns

#### 1. **Cache-Aside (Lazy Loading)**
```java
public User getUser(int id) {
    // Check cache first
    User user = cache.get(id);
    
    if (user == null) {
        // Cache miss - load from DB
        user = database.get(id);
        cache.put(id, user);
    }
    
    return user;
}
```
✅ Only cache what's needed  
❌ Cache miss penalty  
❌ Stale data possible

#### 2. **Write-Through**
```java
public void updateUser(User user) {
    database.save(user);
    cache.put(user.id, user); // Update cache immediately
}
```
✅ Cache always consistent  
❌ Write penalty  
❌ Unused data cached

#### 3. **Write-Behind (Write-Back)**
```java
public void updateUser(User user) {
    cache.put(user.id, user);
    // Async write to database later
    asyncQueue.add(() -> database.save(user));
}
```
✅ Fast writes  
❌ Data loss risk  
❌ Complex implementation

#### 4. **Refresh-Ahead**
```java
// Proactively refresh cache before expiry
if (cache.timeToLive(key) < threshold) {
    asyncRefresh(key);
}
```
✅ No cache miss for hot data  
❌ Can waste resources

### Cache Eviction Policies

1. **LRU (Least Recently Used)** - Most common
2. **LFU (Least Frequently Used)**
3. **FIFO (First In First Out)**
4. **Random**
5. **TTL (Time To Live)**

### Cache Example (Redis)
```java
@Cacheable(value = "users", key = "#id")
public User getUserById(Long id) {
    return userRepository.findById(id);
}

@CacheEvict(value = "users", key = "#user.id")
public void updateUser(User user) {
    userRepository.save(user);
}
```

---

## Database Scalability

### Read Scalability

#### 1. **Read Replicas**
```
         Master DB (Writes)
              |
    +---------+---------+
    |         |         |
 Replica1  Replica2  Replica3
(Reads)   (Reads)   (Reads)
```

**Benefits:**
- Distribute read load
- Geographic distribution
- Backup/analytics

**Challenges:**
- Replication lag
- Data consistency

#### 2. **Database Sharding** (Horizontal Partitioning)

**Shard by User ID:**
```
Shard 1: Users 1-10000
Shard 2: Users 10001-20000
Shard 3: Users 20001-30000
```

**Shard by Geography:**
```
Shard US: American users
Shard EU: European users
Shard ASIA: Asian users
```

**Strategies:**
- **Hash-based**: `shard = hash(key) % num_shards`
- **Range-based**: By ID ranges
- **Directory-based**: Lookup table

**Challenges:**
- Joins across shards
- Rebalancing
- Hotspots

### Write Scalability

#### 1. **Master-Master Replication**
```
Master 1 ←→ Master 2
(Both accept writes)
```
- Higher write throughput
- Complex conflict resolution

#### 2. **Write-Ahead Log (WAL)**
- Log writes before applying
- Crash recovery
- Replication

---

## Content Delivery Network (CDN)

### What is CDN?
Geographically distributed servers that cache static content closer to users.

### How It Works
```
User (Japan) → CDN Edge (Tokyo) → Origin Server (US)
                    ↓
              Cached content served
                (Fast!)
```

### Benefits
- Reduced latency
- Bandwidth savings
- DDoS protection
- Better availability

### What to Cache
- Static assets (images, CSS, JS)
- Videos
- API responses (public)
- Downloadable files

### Popular CDNs
- **Cloudflare**
- **AWS CloudFront**
- **Akamai**
- **Fastly**

---

## Microservices Architecture

### Monolith vs Microservices

#### Monolith
```
┌─────────────────────┐
│   Single Application│
│  ┌───────────────┐  │
│  │ User Service  │  │
│  │ Order Service │  │
│  │ Payment Svc   │  │
│  └───────────────┘  │
│   Single Database   │
└─────────────────────┘
```

#### Microservices
```
┌──────────┐  ┌──────────┐  ┌──────────┐
│  User    │  │  Order   │  │ Payment  │
│ Service  │  │ Service  │  │ Service  │
└─────┬────┘  └────┬─────┘  └────┬─────┘
      │            │             │
   UserDB       OrderDB      PaymentDB
```

### Benefits of Microservices
- Independent scaling
- Technology flexibility
- Fault isolation
- Team autonomy

### Challenges
- Distributed system complexity
- Network latency
- Data consistency
- Monitoring/debugging

---

## Asynchronous Processing

### Message Queues

#### Use Cases
- Decouple services
- Handle traffic spikes
- Background jobs
- Event-driven architecture

#### Example: Order Processing
```
Client → API → Queue → Worker → Database
                 ↓
           (Email Service)
           (Inventory Service)
           (Analytics Service)
```

#### Popular Message Queues
- **RabbitMQ**: Feature-rich, AMQP
- **Apache Kafka**: High throughput, event streaming
- **AWS SQS**: Managed, simple
- **Redis**: Fast, simple pub/sub

### Event-Driven Architecture
```java
// Publisher
eventBus.publish("order.created", orderEvent);

// Subscribers
emailService.subscribe("order.created", sendConfirmationEmail);
inventoryService.subscribe("order.created", updateStock);
analyticsService.subscribe("order.created", recordMetrics);
```

---

## Auto-Scaling

### Types

#### 1. **Reactive Scaling**
- Based on current metrics (CPU, memory)
- Threshold-based triggers
- **Example**: Scale when CPU > 70%

#### 2. **Predictive Scaling**
- Based on patterns and forecasts
- Machine learning models
- **Example**: Scale before Black Friday

#### 3. **Scheduled Scaling**
- Based on time
- Known traffic patterns
- **Example**: Scale up during business hours

### AWS Auto Scaling Example
```yaml
AutoScalingGroup:
  MinSize: 2
  MaxSize: 10
  DesiredCapacity: 3
  Metrics:
    - CPUUtilization > 70%: Scale Out
    - CPUUtilization < 30%: Scale In
```

---

## Performance Metrics

### Key Metrics

1. **Latency**: Response time
   - p50: 50th percentile
   - p95: 95th percentile
   - p99: 99th percentile

2. **Throughput**: Requests per second (RPS)

3. **Availability**: Uptime percentage
   - 99.9% = 43.2 min downtime/month
   - 99.99% = 4.32 min downtime/month

4. **Error Rate**: Failed requests / Total requests

### Monitoring Tools
- **Prometheus + Grafana**: Metrics & visualization
- **ELK Stack**: Logging
- **Datadog**: All-in-one
- **New Relic**: APM

---

## Scalability Patterns Summary

| Pattern | Use Case | Trade-offs |
|---------|----------|------------|
| **Load Balancing** | Distribute traffic | Complexity vs performance |
| **Caching** | Reduce DB load | Memory vs freshness |
| **Database Replication** | Read scaling | Consistency vs availability |
| **Sharding** | Write scaling | Complexity vs capacity |
| **CDN** | Static content | Cost vs latency |
| **Microservices** | Independent scaling | Simplicity vs flexibility |
| **Message Queues** | Async processing | Latency vs reliability |

---

## Interview Questions

1. How would you scale a read-heavy application?
2. Explain the difference between vertical and horizontal scaling
3. How do you handle database hotspots in sharding?
4. What's the difference between caching strategies?
5. How do CDNs improve performance?
6. When would you use microservices vs monolith?

---

## Next Steps

- **Databases** → [03-databases](../03-databases/README.md)
- **Caching** → [04-caching](../04-caching/README.md)
- **Microservices** → [05-microservices](../05-microservices/README.md)

---

**💡 Pro Tip**: In interviews, always discuss trade-offs. There's no perfect solution, only the right solution for given constraints!

