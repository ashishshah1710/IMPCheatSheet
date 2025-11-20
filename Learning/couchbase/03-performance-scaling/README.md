# 🚀 Couchbase - Performance & Scaling

Master performance optimization and horizontal scaling!

---

## 📚 Table of Contents

1. [Performance Monitoring](#performance-monitoring)
2. [Index Optimization](#index-optimization)
3. [Caching Strategies](#caching-strategies)
4. [Replication](#replication)
5. [Sharding & XDCR](#sharding-xdcr)
6. [Production Best Practices](#production-best-practices)
7. [Backup & Recovery](#backup-recovery)
8. [Interview Questions](#interview-questions)

---

## 📊 Performance Monitoring

### Key Metrics to Monitor

```yaml
Operations Metrics:
  - ops/sec (operations per second)
  - GET operations
  - SET operations
  - Query operations

Memory Metrics:
  - Memory used
  - Memory quota
  - Cache hit ratio
  - Resident item ratio

Disk Metrics:
  - Disk write queue
  - Disk read rate
  - Disk write rate
  - Disk utilization

Query Metrics:
  - Query latency
  - Index scan rate
  - Query throughput
```

### Using cbstats

```bash
# Memory stats
cbstats localhost:11210 all -b travel-sample

# Operation stats
cbstats localhost:11210 timings -b travel-sample

# Connection stats
cbstats localhost:11210 connections

# DCP (Database Change Protocol) stats
cbstats localhost:11210 dcp

# Index stats
curl -u Administrator:password \
  http://localhost:8091/pools/default/buckets/travel-sample/stats
```

---

## 🎯 Index Optimization

### Index Best Practices

```sql
-- 1. Create selective indexes
CREATE INDEX idx_active_users 
ON users(email, status) 
WHERE status = 'active';

-- 2. Use compound indexes for common queries
CREATE INDEX idx_order_search
ON orders(customerId, orderDate, status);

-- 3. Covering indexes
CREATE INDEX idx_user_profile
ON users(email, name, age);

-- Query uses covering index
SELECT name, age 
FROM users 
WHERE email = 'john@example.com';

-- 4. Partial indexes for large datasets
CREATE INDEX idx_expensive_products
ON products(category, price)
WHERE price > 100;

-- 5. Array indexes
CREATE INDEX idx_tags
ON articles(DISTINCT ARRAY tag FOR tag IN tags END);
```

### Index Performance Analysis

```sql
-- Check index usage
SELECT * FROM system:indexes 
WHERE keyspace_id = 'travel-sample';

-- Monitor index statistics
SELECT idx.name, idx.index_key, idx.condition,
       stats.num_requests, stats.num_rows_returned
FROM system:indexes idx
LEFT JOIN system:index_stats stats 
ON idx.id = stats.index_id
WHERE idx.keyspace_id = 'travel-sample';

-- Find unused indexes
SELECT name, index_key
FROM system:indexes
WHERE keyspace_id = 'travel-sample'
AND name NOT IN (
    SELECT index_name 
    FROM system:completed_requests
    WHERE statement LIKE '%travel-sample%'
);
```

---

## 💾 Caching Strategies

### Memory Management

```java
import com.couchbase.client.java.*;
import com.couchbase.client.java.kv.*;
import java.time.Duration;

public class CachingStrategies {
    
    // Document expiration (TTL)
    public void setWithExpiration() {
        collection.insert(
            "session::12345",
            sessionData,
            InsertOptions.insertOptions()
                .expiry(Duration.ofMinutes(30))
        );
    }
    
    // Touch to extend TTL
    public void extendTTL(String key) {
        collection.touch(key, Duration.ofHours(1));
    }
    
    // Get and touch
    public JsonObject getAndExtend(String key) {
        GetResult result = collection.getAndTouch(
            key, 
            Duration.ofHours(1)
        );
        return result.contentAsObject();
    }
    
    // Application-level caching
    private Map<String, CachedData> localCache = new ConcurrentHashMap<>();
    
    public JsonObject getWithLocalCache(String key) {
        CachedData cached = localCache.get(key);
        
        if (cached != null && !cached.isExpired()) {
            return cached.getData();
        }
        
        // Cache miss - fetch from Couchbase
        GetResult result = collection.get(key);
        JsonObject data = result.contentAsObject();
        
        localCache.put(key, new CachedData(data, result.cas()));
        return data;
    }
}
```

### Cache Warming

```java
public class CacheWarming {
    
    public void warmCache() {
        // Preload frequently accessed documents
        List<String> hotKeys = Arrays.asList(
            "config::main",
            "product::featured",
            "user::admin"
        );
        
        hotKeys.parallelStream().forEach(key -> {
            try {
                collection.get(key);
                System.out.println("Warmed: " + key);
            } catch (Exception e) {
                System.err.println("Failed to warm: " + key);
            }
        });
    }
}
```

---

## 🔄 Replication

### Configuring Replication

```yaml
Replication Modes:
  1. Intra-Cluster Replication:
     - Automatic data replication within cluster
     - Configurable number of replicas (0-3)
     - Active-active within cluster
  
  2. Cross Data Center Replication (XDCR):
     - Replicate data between clusters
     - Unidirectional or bidirectional
     - Conflict resolution strategies
```

### Setting Up Replication

```bash
# Create bucket with replicas
couchbase-cli bucket-create \
  -c localhost:8091 \
  -u Administrator -p password \
  --bucket my-bucket \
  --bucket-type couchbase \
  --bucket-ramsize 1024 \
  --bucket-replica 2 \
  --enable-flush 0

# Configure XDCR replication
couchbase-cli xdcr-setup \
  -c localhost:8091 \
  -u Administrator -p password \
  --create \
  --xdcr-cluster-name remote-cluster \
  --xdcr-hostname remote.example.com:8091 \
  --xdcr-username Administrator \
  --xdcr-password password

# Start replication
couchbase-cli xdcr-replicate \
  -c localhost:8091 \
  -u Administrator -p password \
  --create \
  --xdcr-cluster-name remote-cluster \
  --xdcr-from-bucket my-bucket \
  --xdcr-to-bucket my-bucket
```

### Replication in Application

```java
import com.couchbase.client.java.kv.DurabilityLevel;

public class ReplicationDemo {
    
    // Write with durability
    public void writeWithDurability() {
        collection.insert(
            "important::doc",
            data,
            InsertOptions.insertOptions()
                .durability(DurabilityLevel.MAJORITY)
        );
    }
    
    // Wait for replication
    public void writeAndWait() {
        collection.insert(
            "critical::doc",
            data,
            InsertOptions.insertOptions()
                .durability(DurabilityLevel.PERSIST_TO_MAJORITY)
        );
    }
}
```

---

## 🗺️ Sharding & XDCR

### Automatic Sharding

```yaml
Couchbase Auto-Sharding:
  - Data automatically distributed across nodes
  - 1024 vBuckets per bucket
  - vBuckets assigned to nodes
  - Rebalancing redistributes vBuckets

Benefits:
  - Horizontal scaling
  - Even data distribution
  - Linear performance scaling
  - No manual intervention
```

### XDCR Patterns

```yaml
1. Active-Passive (Disaster Recovery):
   Primary DC: Read/Write
   Secondary DC: Read-only, receives replication
   Use: DR, read scaling

2. Active-Active (Multi-Master):
   DC1: Read/Write ←→ DC2: Read/Write
   Bidirectional replication
   Use: Global applications, low latency

3. Hub and Spoke:
   Central Hub ←→ Multiple Edge Locations
   Use: IoT, branch offices

Conflict Resolution:
  - Sequence number (default)
  - Timestamp
  - Custom resolution
```

---

## 🏭 Production Best Practices

### Cluster Configuration

```yaml
Minimum Production Cluster:
  Nodes: 3 (for high availability)
  RAM per node: 16GB+
  CPU: 4+ cores
  Disk: SSD (NVMe preferred)
  Network: 10Gbps+

Service Distribution:
  Node 1: Data + Query + Index
  Node 2: Data + Query + Index
  Node 3: Data + Analytics

Memory Quotas:
  Data Service: 60% of RAM
  Query Service: 20% of RAM
  Index Service: 15% of RAM
  Search Service: 5% of RAM
```

### Connection Pool Configuration

```java
ClusterEnvironment environment = ClusterEnvironment.builder()
    // Connection pool
    .ioConfig(IoConfig.builder()
        .maxHttpConnections(50)
        .numKvConnections(2)
        .build())
    
    // Timeouts
    .timeoutConfig(TimeoutConfig.builder()
        .kvTimeout(Duration.ofSeconds(10))
        .queryTimeout(Duration.ofSeconds(75))
        .searchTimeout(Duration.ofSeconds(75))
        .build())
    
    // Retry strategy
    .retryStrategy(BestEffortRetryStrategy.INSTANCE)
    
    // Circuit breaker
    .circuitBreakerConfig(CircuitBreakerConfig.builder()
        .enabled(true)
        .volumeThreshold(50)
        .errorThresholdPercentage(50)
        .build())
    
    .build();

Cluster cluster = Cluster.connect(
    "localhost",
    ClusterOptions.clusterOptions("Administrator", "password")
        .environment(environment)
);
```

### Query Optimization

```java
public class QueryOptimization {
    
    // Prepared statements
    public void usePreparedStatement() {
        // Prepare once
        String statement = "SELECT * FROM users WHERE email = $email";
        
        // Execute multiple times
        cluster.query(
            statement,
            QueryOptions.queryOptions()
                .parameters(JsonObject.create().put("email", "john@example.com"))
                .scanConsistency(QueryScanConsistency.REQUEST_PLUS)
        );
    }
    
    // Consistency levels
    public void consistencyDemo() {
        // NOT_BOUNDED - Fastest, eventually consistent
        cluster.query(
            "SELECT * FROM users",
            QueryOptions.queryOptions()
                .scanConsistency(QueryScanConsistency.NOT_BOUNDED)
        );
        
        // REQUEST_PLUS - Read your own writes
        cluster.query(
            "SELECT * FROM users WHERE id = 'user::123'",
            QueryOptions.queryOptions()
                .scanConsistency(QueryScanConsistency.REQUEST_PLUS)
        );
    }
}
```

---

## 💾 Backup & Recovery

### Backup Strategies

```bash
# Full backup
cbbackupmgr backup \
  --archive /backup/archive \
  --repo my-repo \
  --cluster localhost:8091 \
  --username Administrator \
  --password password

# Incremental backup
cbbackupmgr backup \
  --archive /backup/archive \
  --repo my-repo \
  --cluster localhost:8091 \
  --username Administrator \
  --password password

# List backups
cbbackupmgr list \
  --archive /backup/archive

# Restore
cbbackupmgr restore \
  --archive /backup/archive \
  --repo my-repo \
  --cluster localhost:8091 \
  --username Administrator \
  --password password \
  --start 2024-01-01T00:00:00 \
  --end 2024-01-31T23:59:59
```

### Point-in-Time Recovery

```bash
# Restore to specific timestamp
cbbackupmgr restore \
  --archive /backup/archive \
  --repo my-repo \
  --cluster localhost:8091 \
  --username Administrator \
  --password password \
  --end 2024-01-15T14:30:00
```

---

## 🎯 Interview Questions

**Q: How does Couchbase achieve high performance?**

**Answer:**
- Memory-first architecture
- Automatic sharding
- Built-in caching layer
- Asynchronous replication
- Multi-threaded operations

**Q: What is XDCR and when would you use it?**

**Answer:**
Cross Data Center Replication - replicates data between clusters. Use for:
- Disaster recovery
- Geographic distribution
- Read scaling
- Data locality

**Q: How do you handle conflicts in active-active XDCR?**

**Answer:**
- Sequence number (default) - highest wins
- Timestamp - most recent wins  
- Custom conflict resolution
- Metadata-based resolution

---

**Continue to Spring Boot Integration for application development!** 🚀

