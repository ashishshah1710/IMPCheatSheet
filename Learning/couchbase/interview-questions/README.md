# 🎯 Couchbase - Interview Questions

Comprehensive interview questions and answers for Couchbase!

---

## 📚 Categories

1. [Fundamentals](#fundamentals)
2. [Architecture](#architecture)
3. [Performance](#performance)
4. [Scaling & Replication](#scaling-replication)
5. [Security](#security)
6. [Troubleshooting](#troubleshooting)
7. [Scenario-Based](#scenario-based)

---

## 🎯 Fundamentals

**Q1: What is Couchbase and how does it differ from other NoSQL databases?**

**Answer:**
Couchbase is a distributed NoSQL document database with:
- Memory-first architecture for sub-millisecond latency
- N1QL (SQL for JSON) query language
- Built-in caching layer
- Multi-model support (key-value + document + search)

**Key Differences:**
- vs MongoDB: Built-in caching, SQL-like queries, memory-first
- vs Redis: Persistent storage, document model, N1QL
- vs Cassandra: Easier querying, better consistency options

---

**Q2: Explain the hierarchy: Cluster → Bucket → Scope → Collection**

**Answer:**
```
Cluster (entire Couchbase deployment)
  └── Bucket (like database, memory allocation unit)
      └── Scope (namespace for collections)
          └── Collection (like table, group of documents)
              └── Documents (JSON data)
```

**Example:**
- Cluster: Production cluster
- Bucket: my-app (2GB RAM)
- Scope: users, orders
- Collection: profiles, sessions
- Document: user::12345

---

**Q3: What is CAS and why is it important?**

**Answer:**
CAS (Compare-And-Swap) is a unique value that changes with each document modification.

**Use Cases:**
- Optimistic locking
- Prevent lost updates
- Concurrent modification detection

**Example:**
```java
GetResult result = collection.get("user::123");
long cas = result.cas();

// Update only if CAS matches
collection.replace(
    "user::123", 
    updatedDoc,
    ReplaceOptions.replaceOptions().cas(cas)
);
```

---

## 🏗️ Architecture

**Q4: Explain Couchbase's service architecture**

**Answer:**

**Services:**
1. **Data Service:** Store/retrieve documents, automatic sharding
2. **Query Service:** Process N1QL queries
3. **Index Service:** Manage secondary indexes
4. **Search Service:** Full-text search
5. **Analytics Service:** Complex analytical queries
6. **Eventing Service:** Real-time data processing

**Distribution:**
- Services can run on same or different nodes
- Data Service must be on all data nodes
- Other services can be distributed for load balancing

---

**Q5: How does Couchbase handle data distribution?**

**Answer:**

**Auto-Sharding:**
- 1024 vBuckets (virtual buckets) per bucket
- Documents hashed to vBuckets
- vBuckets distributed across nodes
- Automatic rebalancing when nodes added/removed

**Benefits:**
- Linear scalability
- Even data distribution
- No hotspots
- Zero downtime scaling

---

**Q6: What is the difference between primary and secondary indexes?**

**Answer:**

| Feature | Primary Index | Secondary Index |
|---------|---------------|-----------------|
| **Indexes** | Document keys | Document fields |
| **Required** | Yes (for N1QL) | Optional |
| **Performance** | Full bucket scan | Optimized queries |
| **Use Case** | Ad-hoc queries | Production queries |

**Examples:**
```sql
-- Primary index (slow)
CREATE PRIMARY INDEX ON bucket;
SELECT * FROM bucket WHERE field = 'value';

-- Secondary index (fast)
CREATE INDEX idx_field ON bucket(field);
SELECT * FROM bucket WHERE field = 'value';
```

---

## ⚡ Performance

**Q7: How do you optimize query performance in Couchbase?**

**Answer:**

**Strategies:**
1. **Create appropriate indexes**
2. **Use covering indexes**
3. **Optimize query structure**
4. **Use query hints**
5. **Monitor with EXPLAIN**

**Example:**
```sql
-- Create covering index
CREATE INDEX idx_user_email ON users(email, name, age);

-- Query uses covering index (no document fetch)
SELECT name, age FROM users WHERE email = 'john@example.com';

-- Check plan
EXPLAIN SELECT name FROM users WHERE email = 'john@example.com';
```

---

**Q8: What is a covering index and why is it beneficial?**

**Answer:**

**Covering Index:** Index that contains all fields needed by a query.

**Benefits:**
- No document fetch required
- Faster query execution
- Reduced I/O
- Lower latency

**Example:**
```sql
CREATE INDEX idx_covering 
ON users(type, email, name, age)
WHERE type = 'user';

-- Covered query (fast)
SELECT email, name, age 
FROM users 
WHERE type = 'user' AND email = 'john@example.com';
```

---

**Q9: How does Couchbase's memory architecture work?**

**Answer:**

**Memory-First Architecture:**
1. All documents stored in RAM (working set)
2. Mutations logged to disk asynchronously
3. LRU eviction when memory full
4. Cache hit ratio critical for performance

**Memory Breakdown:**
- Data Service: 60% of RAM
- Index Service: 20%
- Query Service: 15%
- Other: 5%

**Best Practices:**
- Size RAM for working set
- Monitor cache hit ratio (>90%)
- Use TTL for temporary data

---

## 🔄 Scaling & Replication

**Q10: Explain XDCR and its use cases**

**Answer:**

**XDCR (Cross Data Center Replication):**
Replicates data between Couchbase clusters.

**Modes:**
1. **Unidirectional:** A → B
2. **Bidirectional:** A ↔ B

**Use Cases:**
- Disaster recovery
- Geographic distribution
- Data migration
- Read scaling
- Data locality

**Conflict Resolution:**
- Sequence number (default)
- Timestamp
- Custom resolution

---

**Q11: How do you handle scaling in Couchbase?**

**Answer:**

**Horizontal Scaling:**
1. Add nodes to cluster
2. Rebalance (redistribute vBuckets)
3. No downtime required

**Process:**
```bash
# Add node
couchbase-cli server-add \
  -c localhost:8091 \
  --server-add 192.168.1.101:8091

# Rebalance
couchbase-cli rebalance \
  -c localhost:8091
```

**Scaling Strategies:**
- Add data nodes for storage
- Add query nodes for query load
- Add index nodes for indexing load

---

## 🔒 Security

**Q12: What security features does Couchbase provide?**

**Answer:**

**Security Layers:**
1. **Authentication:** LDAP, SASL, Certificate-based
2. **Authorization:** RBAC (Role-Based Access Control)
3. **Encryption:**
   - At rest (Enterprise only)
   - In transit (TLS/SSL)
   - Field-level encryption
4. **Auditing:** Comprehensive audit logs
5. **Network:** Firewall, IP whitelisting

**Example RBAC:**
```bash
# Create user with read-only access
couchbase-cli user-manage \
  --create \
  --username readonly_user \
  --password password \
  --roles data_reader[my-bucket]
```

---

## 🔧 Troubleshooting

**Q13: How do you troubleshoot slow queries?**

**Answer:**

**Steps:**
1. Use EXPLAIN to check query plan
2. Verify indexes exist
3. Check index scan rate
4. Monitor query metrics
5. Use query profiler

**Tools:**
```sql
-- Explain query
EXPLAIN SELECT * FROM bucket WHERE field = 'value';

-- Monitor slow queries
SELECT * FROM system:completed_requests 
WHERE elapsedTime > 1000 
ORDER BY elapsedTime DESC;

-- Index stats
SELECT * FROM system:indexes 
WHERE keyspace_id = 'my-bucket';
```

---

**Q14: Common issues and solutions**

**Answer:**

| Issue | Cause | Solution |
|-------|-------|----------|
| High latency | Missing indexes | Create indexes |
| OOM errors | Working set > RAM | Add nodes, increase RAM |
| Rebalance failures | Network issues | Check connectivity |
| Slow writes | Disk I/O | Use SSD, tune disk queue |
| Query timeouts | Complex queries | Optimize, add indexes |

---

## 🎬 Scenario-Based

**Q15: Design a high-availability e-commerce system with Couchbase**

**Answer:**

**Architecture:**
```yaml
Production Cluster (3 nodes):
  - Node 1: Data + Query + Index
  - Node 2: Data + Query + Index
  - Node 3: Data + Query + Index
  - Replica count: 2

Buckets:
  - products: Product catalog
  - orders: Order data
  - sessions: User sessions (TTL: 1 hour)

DR Cluster (3 nodes):
  - XDCR replication from production
  - Read-only access
  - Automatic failover ready

Indexes:
  - products: category, price, name
  - orders: customerId, status, date
  - Covering indexes for common queries

Caching:
  - Application-level cache for hot products
  - TTL-based session management
```

---

**Q16: How would you migrate from MongoDB to Couchbase?**

**Answer:**

**Migration Steps:**
1. **Analyze MongoDB schema**
2. **Design Couchbase schema**
3. **Setup Couchbase cluster**
4. **Data migration:**
   - Export MongoDB to JSON
   - Transform data if needed
   - Import to Couchbase
5. **Create indexes**
6. **Update application code**
7. **Testing:**
   - Functional testing
   - Performance testing
   - Load testing
8. **Gradual cutover:**
   - Dual-write period
   - Switch reads to Couchbase
   - Decommission MongoDB

---

**Q17: Design a real-time analytics pipeline with Couchbase**

**Answer:**

**Architecture:**
```yaml
Data Ingestion:
  - REST API writes to Couchbase
  - High-throughput document inserts

Real-Time Processing:
  - Eventing Service for triggers
  - Process data on mutations
  - Update aggregate documents

Analytics:
  - Analytics Service for queries
  - N1QL for aggregations
  - Separate analytics nodes

Visualization:
  - Query results via REST API
  - Stream to dashboard
  - WebSocket for live updates

Example:
  1. Order placed → Document inserted
  2. Eventing triggers → Update inventory
  3. Analytics query → Real-time dashboard
  4. Alert if stock low
```

---

## 🎓 Advanced Topics

**Q18: Explain Couchbase's consistency model**

**Answer:**

**Consistency Levels:**
1. **Eventually Consistent (default)**
2. **Read Your Own Writes**
3. **Strong Consistency (with durability)**

**Scan Consistency:**
- `NOT_BOUNDED`: Fastest, eventually consistent
- `AT_PLUS`: Read your writes
- `REQUEST_PLUS`: Consistent with all mutations

---

**Q19: Best practices for production deployment**

**Answer:**

**Infrastructure:**
- Minimum 3 nodes (HA)
- SSD storage
- 16GB+ RAM per node
- Dedicated network (10Gbps)

**Configuration:**
- Enable replicas (2+)
- Configure memory quotas
- Setup monitoring
- Enable audit logging
- Configure backups

**Application:**
- Use connection pooling
- Handle failures gracefully
- Implement retry logic
- Use appropriate consistency
- Monitor performance

---

**Master these concepts for Couchbase interviews!** 🚀

