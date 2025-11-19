# 💾 Databases in System Design

## Overview
Choosing the right database is crucial for system design. This guide covers database types, when to use them, and common patterns.

---

## Database Types

### 1. **Relational Databases (SQL)**

#### Characteristics
- **Structured**: Fixed schema (tables, rows, columns)
- **ACID**: Atomicity, Consistency, Isolation, Durability
- **Relationships**: Foreign keys, joins
- **Query Language**: SQL

#### Popular Options
- **PostgreSQL**: Feature-rich, open-source
- **MySQL**: Fast, widely used
- **Oracle**: Enterprise-grade
- **MS SQL Server**: Microsoft ecosystem

#### When to Use
✅ Structured data with relationships  
✅ Complex queries and joins  
✅ ACID compliance needed  
✅ Financial transactions  
✅ User management systems  

#### Example
```sql
-- Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders table with foreign key
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    total_amount DECIMAL(10, 2),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Complex join query
SELECT u.username, COUNT(o.order_id) as order_count
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id
HAVING COUNT(o.order_id) > 5;
```

---

### 2. **NoSQL Databases**

#### A. Document Stores

**MongoDB, CouchDB, Couchbase**

**Characteristics:**
- Schema-less (flexible documents)
- JSON-like documents
- Embedded data
- Horizontal scaling

**When to Use:**
✅ Flexible/evolving schema  
✅ Nested/hierarchical data  
✅ Rapid development  
✅ Content management  
✅ Product catalogs  

**Example:**
```javascript
// MongoDB document
{
  "_id": "user123",
  "username": "john_doe",
  "email": "john@example.com",
  "profile": {
    "firstName": "John",
    "lastName": "Doe",
    "address": {
      "city": "San Francisco",
      "state": "CA"
    }
  },
  "orders": [
    { "orderId": "ord1", "amount": 99.99 },
    { "orderId": "ord2", "amount": 149.99 }
  ]
}
```

#### B. Key-Value Stores

**Redis, DynamoDB, Memcached**

**Characteristics:**
- Simplest NoSQL model
- Extremely fast (in-memory)
- No complex queries
- High throughput

**When to Use:**
✅ Session storage  
✅ Caching layer  
✅ Real-time analytics  
✅ Leaderboards  
✅ Rate limiting  

**Example:**
```java
// Redis operations
redis.set("user:1001:session", sessionData, EX, 3600); // Expire in 1 hour
String session = redis.get("user:1001:session");

// Counter
redis.incr("page:views:homepage");

// Leaderboard (sorted set)
redis.zadd("leaderboard", 9500, "player1");
redis.zrevrange("leaderboard", 0, 9); // Top 10
```

#### C. Column-Family Stores

**Cassandra, HBase, ScyllaDB**

**Characteristics:**
- Column-oriented storage
- Optimized for writes
- Distributed by design
- Eventual consistency

**When to Use:**
✅ Time-series data  
✅ IoT sensor data  
✅ Event logging  
✅ High write throughput  
✅ Analytics workloads  

**Example:**
```cql
-- Cassandra
CREATE TABLE sensor_data (
    sensor_id UUID,
    timestamp TIMESTAMP,
    temperature DOUBLE,
    humidity DOUBLE,
    PRIMARY KEY ((sensor_id), timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);

-- Query recent data for a sensor
SELECT * FROM sensor_data 
WHERE sensor_id = 123e4567-e89b-12d3-a456-426614174000
  AND timestamp > '2024-01-01'
LIMIT 100;
```

#### D. Graph Databases

**Neo4j, Amazon Neptune, ArangoDB**

**Characteristics:**
- Nodes and relationships
- Optimized for connections
- Graph traversal queries
- Social networks

**When to Use:**
✅ Social networks  
✅ Recommendation engines  
✅ Fraud detection  
✅ Knowledge graphs  
✅ Network analysis  

**Example:**
```cypher
// Neo4j - Create nodes and relationships
CREATE (alice:Person {name: "Alice"})
CREATE (bob:Person {name: "Bob"})
CREATE (alice)-[:FOLLOWS]->(bob)

// Find friends of friends
MATCH (user:Person {name: "Alice"})-[:FOLLOWS]->()-[:FOLLOWS]->(fof)
WHERE NOT (user)-[:FOLLOWS]->(fof) AND user <> fof
RETURN fof.name
```

---

### 3. **Specialized Databases**

#### A. Search Engines

**Elasticsearch, Solr, Algolia**

**When to Use:**
- Full-text search
- Log analytics
- Faceted search
- Autocomplete

**Example:**
```json
// Elasticsearch query
{
  "query": {
    "multi_match": {
      "query": "machine learning",
      "fields": ["title^3", "description", "tags"]
    }
  },
  "aggs": {
    "categories": {
      "terms": { "field": "category" }
    }
  }
}
```

#### B. Time-Series Databases

**InfluxDB, TimescaleDB, Prometheus**

**When to Use:**
- Metrics monitoring
- IoT data
- Stock prices
- Server metrics

**Example:**
```sql
-- TimescaleDB (PostgreSQL extension)
SELECT time_bucket('5 minutes', timestamp) AS five_min,
       AVG(cpu_usage) AS avg_cpu
FROM metrics
WHERE timestamp > NOW() - INTERVAL '1 day'
GROUP BY five_min
ORDER BY five_min DESC;
```

---

## Database Selection Matrix

| Requirement | Database Type | Examples |
|------------|--------------|----------|
| **ACID transactions** | SQL | PostgreSQL, MySQL |
| **Flexible schema** | Document | MongoDB, Couchbase |
| **High-speed cache** | Key-Value | Redis, Memcached |
| **Time-series data** | Column/Time-series | Cassandra, InfluxDB |
| **Graph relationships** | Graph | Neo4j, Neptune |
| **Full-text search** | Search | Elasticsearch |
| **Analytics (OLAP)** | Columnar | Redshift, BigQuery |
| **Geospatial** | Spatial | PostGIS, MongoDB |

---

## CAP Theorem

**You can only have 2 out of 3:**

### C - Consistency
Every read receives the most recent write

### A - Availability
Every request receives a response (success/failure)

### P - Partition Tolerance
System continues despite network failures

### Trade-offs

```
      Consistency
          /\
         /  \
        /    \
       /  CA  \
      / MySQL  \
     /PostgreSQL\
    /____________\
   AP            CP
 Cassandra    MongoDB
 DynamoDB     HBase
```

**CA** (Consistency + Availability): Traditional RDBMS  
**CP** (Consistency + Partition Tolerance): MongoDB, Redis  
**AP** (Availability + Partition Tolerance): Cassandra, DynamoDB  

---

## Database Patterns

### 1. **Database Sharding**

#### Horizontal Sharding (by rows)
```
Shard 1: Users with ID 1-100000
Shard 2: Users with ID 100001-200000
Shard 3: Users with ID 200001-300000
```

#### Vertical Sharding (by columns)
```
DB1: user_id, username, email
DB2: user_id, profile_data, preferences
```

#### Sharding Strategies
```java
// Hash-based sharding
int shard = hash(userId) % numShards;

// Range-based sharding
if (userId <= 100000) return shard1;
else if (userId <= 200000) return shard2;

// Geographic sharding
if (userCountry == "US") return usaShard;
else if (userCountry == "EU") return euShard;
```

**Challenges:**
- Cross-shard queries
- Rebalancing data
- Hotspots
- Distributed transactions

### 2. **Database Replication**

#### Master-Slave Replication
```
        Master (writes)
           |
    +------+------+
    |      |      |
 Slave1 Slave2 Slave3
(reads)(reads)(reads)
```

**Benefits:**
- Read scaling
- Data backup
- Geographic distribution

**Challenges:**
- Replication lag
- Read-after-write consistency

#### Master-Master Replication
```
Master A ←→ Master B
(Both read & write)
```

**Benefits:**
- Write scaling
- High availability

**Challenges:**
- Conflict resolution
- Complexity

### 3. **CQRS (Command Query Responsibility Segregation)**

```
           Commands (Writes)
                ↓
           Write Database
                ↓
          Event Stream
                ↓
          Read Database
                ↓
         Queries (Reads)
```

**Benefits:**
- Optimized read/write models
- Scalability
- Event sourcing

**Use Cases:**
- Complex domains
- High read/write ratio difference
- Event-driven systems

### 4. **Database Per Service (Microservices)**

```
┌─────────────┐     ┌─────────────┐
│   User      │     │   Order     │
│  Service    │     │  Service    │
└─────┬───────┘     └─────┬───────┘
      │                   │
   UserDB              OrderDB
```

**Benefits:**
- Service independence
- Technology choice per service
- Isolated failures

**Challenges:**
- Distributed transactions
- Data consistency
- Joins across services

---

## Indexing Strategies

### Types of Indexes

#### 1. Primary Index
```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,  -- Automatically indexed
    username VARCHAR(50)
);
```

#### 2. Secondary Index
```sql
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
```

#### 3. Composite Index
```sql
CREATE INDEX idx_user_created ON users(user_id, created_at);
```

#### 4. Unique Index
```sql
CREATE UNIQUE INDEX idx_email_unique ON users(email);
```

#### 5. Full-Text Index
```sql
CREATE FULLTEXT INDEX idx_content ON articles(title, body);
```

### Index Best Practices

✅ Index columns used in WHERE clauses  
✅ Index foreign keys  
✅ Index columns used in ORDER BY  
✅ Use composite indexes for multi-column queries  
❌ Don't over-index (slows writes)  
❌ Don't index high-cardinality columns randomly  

---

## Connection Pooling

### Why Connection Pooling?

**Without Pooling:**
```java
// Each request creates new connection (SLOW!)
Connection conn = DriverManager.getConnection(url, user, password);
// ... use connection ...
conn.close();
```

**With Pooling:**
```java
// HikariCP example
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setMaximumPoolSize(20);
config.setMinimumIdle(5);
config.setConnectionTimeout(30000);

HikariDataSource dataSource = new HikariDataSource(config);
Connection conn = dataSource.getConnection(); // Fast! Reuses connection
```

**Benefits:**
- Faster connection reuse
- Limited concurrent connections
- Better resource management

---

## Database Transactions

### ACID Properties

#### Atomicity
All or nothing - transaction fully completes or fully rolls back

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT; -- Both succeed or both fail
```

#### Consistency
Database remains in valid state

#### Isolation
Concurrent transactions don't interfere

**Isolation Levels:**
1. **Read Uncommitted**: Dirty reads possible
2. **Read Committed**: No dirty reads (default in PostgreSQL)
3. **Repeatable Read**: Consistent snapshot
4. **Serializable**: Strictest, no anomalies

#### Durability
Committed data survives crashes

---

## Performance Optimization

### Query Optimization

```sql
-- BAD: Table scan
SELECT * FROM users WHERE LOWER(email) = 'john@example.com';

-- GOOD: Use index
SELECT * FROM users WHERE email = 'john@example.com';

-- BAD: N+1 queries
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)

-- GOOD: Single query with join
SELECT u.*, o.* FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id;
```

### Denormalization

**Normalized (3NF):**
```
users: id, name
posts: id, user_id, content
comments: id, post_id, user_id, text
```

**Denormalized (for reads):**
```
posts: id, user_id, user_name, content, comment_count
```

**Trade-off:** Read speed vs write complexity

---

## Common Interview Questions

1. **SQL vs NoSQL: When to use each?**
2. **How would you handle 1 billion writes/day?**
3. **Explain database sharding and its challenges**
4. **How do you ensure data consistency in distributed systems?**
5. **What is the CAP theorem?**
6. **How would you design a database for a social network?**
7. **Explain ACID properties**
8. **What are database indexes? How do they work?**

---

## Real-World Examples

### Twitter
- **MySQL**: User data, tweets
- **Manhattan (Key-Value)**: Timelines
- **FlockDB**: Social graph

### Netflix
- **Cassandra**: Viewing history, user preferences
- **MySQL**: Billing, user accounts
- **Elasticsearch**: Search

### Uber
- **PostgreSQL**: Persistent data
- **Redis**: Caching, geospatial
- **Cassandra**: Trip history

---

## Next Steps

- **Caching** → [04-caching](../04-caching/README.md)
- **Microservices** → [05-microservices](../05-microservices/README.md)
- **Case Studies** → [06-real-world-systems](../06-real-world-systems/README.md)

---

**💡 Pro Tip**: In interviews, there's no "best" database. Always discuss trade-offs based on requirements: consistency vs availability, read vs write patterns, scaling needs!

