# 🗄️ Couchbase - Complete Guide

**For 3.5+ Years Experienced Developers | Interview Preparation**

Master Couchbase NoSQL database for high-performance applications and ace your interviews!

---

## 📖 Overview

Couchbase is a distributed NoSQL document database with a unique combination of memory-first architecture, SQL-like query language (N1QL), and full-text search capabilities.

### Why Couchbase?

✅ **Memory-First** - Sub-millisecond latency  
✅ **SQL for NoSQL** - N1QL query language  
✅ **Scalable** - Easy horizontal scaling  
✅ **Mobile Sync** - Built-in mobile support (Sync Gateway)  
✅ **Multi-Model** - Document, Key-Value, Full-Text Search  
✅ **Enterprise-Ready** - Used by Cisco, eBay, Verizon, PayPal  

---

## 🎯 Learning Path for Experienced Developers

### Phase 1: Couchbase Fundamentals (1 week)
**Master core concepts**

- Architecture overview
- Buckets, Scopes, Collections
- Document structure
- Key-Value operations
- N1QL basics
- Indexing strategies

**👉 Start:** [`01-fundamentals/README.md`](01-fundamentals/README.md)

---

### Phase 2: N1QL & Querying (1 week)
**Master query language**

- N1QL syntax
- JOINs and subqueries
- Aggregations
- Full-Text Search (FTS)
- Query optimization
- Index design

**👉 Continue:** [`02-n1ql-queries/README.md`](02-n1ql-queries/README.md)

---

### Phase 3: Performance & Scaling (1 week)
**Production-ready Couchbase**

- Cluster architecture
- Data distribution
- Replication
- XDCR (Cross Datacenter Replication)
- Memory management
- Performance tuning

**👉 Master:** [`03-performance-scaling/README.md`](03-performance-scaling/README.md)

---

### Phase 4: Spring Boot Integration (1 week)
**Build applications**

- Spring Data Couchbase
- Repository pattern
- Reactive programming
- Multi-document transactions
- Eventing service
- Analytics

**👉 Advanced:** [`04-spring-boot-integration/README.md`](04-spring-boot-integration/README.md)

---

## 💼 Interview Preparation

### Top Interview Questions

**Fundamentals:**
- Couchbase vs MongoDB comparison?
- Memory-first architecture explained
- Document structure best practices
- Bucket types and use cases
- Data modeling in Couchbase

**N1QL:**
- N1QL vs SQL differences?
- Index types in Couchbase
- Query optimization techniques
- JOIN strategies
- Covering indexes

**Performance:**
- Caching in Couchbase
- Replication mechanisms
- XDCR use cases
- Cluster rebalancing
- Memory optimization

**Advanced:**
- Multi-document transactions
- Eventing service use cases
- Analytics vs Query service
- Full-Text Search implementation
- Security best practices

**👉 See:** [`interview-questions/README.md`](interview-questions/README.md)

---

## 🎯 Quick Start

### Installation & Setup

```bash
# Using Docker
docker run -d --name couchbase \
  -p 8091-8096:8091-8096 \
  -p 11210-11211:11210-11211 \
  couchbase:enterprise

# Access UI: http://localhost:8091
# Default credentials: Administrator / password
```

### Basic Operations

```java
// Connect to Couchbase
Cluster cluster = Cluster.connect("localhost", "username", "password");
Bucket bucket = cluster.bucket("travel-sample");
Collection collection = bucket.defaultCollection();

// Insert Document
User user = new User("user::1", "John Doe", "john@example.com");
collection.upsert("user::1", user);

// Get Document
GetResult result = collection.get("user::1");
User retrievedUser = result.contentAs(User.class);

// N1QL Query
QueryResult queryResult = cluster.query(
  "SELECT * FROM `travel-sample` WHERE type = 'airline' LIMIT 10"
);

// Full-Text Search
SearchResult searchResult = cluster.searchQuery(
  "travel-search",
  SearchQuery.queryString("luxury hotel")
);
```

### N1QL Examples

```sql
-- Basic SELECT
SELECT name, email FROM users WHERE age > 25;

-- JOIN
SELECT u.name, o.total 
FROM users u
JOIN orders o ON KEYS u.orderId
WHERE o.status = 'completed';

-- Aggregation
SELECT country, COUNT(*) as count, AVG(age) as avgAge
FROM users
GROUP BY country
HAVING count > 100
ORDER BY count DESC;

-- Subquery
SELECT * FROM products 
WHERE categoryId IN (
  SELECT RAW id FROM categories WHERE active = true
);

-- Array operations
SELECT name FROM users 
WHERE ANY skill IN skills SATISFIES skill = 'Java' END;

-- UNNEST
SELECT u.name, h.hobby
FROM users u
UNNEST u.hobbies h;
```

---

## 🍃 Spring Boot Integration

### Dependencies

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-couchbase</artifactId>
</dependency>
```

### Configuration

```yaml
spring:
  couchbase:
    connection-string: couchbase://localhost
    username: Administrator
    password: password
  data:
    couchbase:
      bucket-name: my-bucket
```

### Entity

```java
@Document
@Data
public class User {
    @Id
    private String id;
    
    @Field
    private String name;
    
    @Field
    private String email;
    
    @Field
    private Integer age;
    
    @Field
    private Address address;
    
    @Field
    private List<String> skills;
    
    @CreatedDate
    private LocalDateTime createdAt;
    
    @LastModifiedDate
    private LocalDateTime updatedAt;
}
```

### Repository

```java
@Repository
public interface UserRepository extends CouchbaseRepository<User, String> {
    
    // Query methods
    List<User> findByName(String name);
    List<User> findByAgeGreaterThan(Integer age);
    
    // N1QL queries
    @Query("#{#n1ql.selectEntity} WHERE email = $1")
    Optional<User> findByEmail(String email);
    
    @Query("#{#n1ql.selectEntity} WHERE age BETWEEN $1 AND $2")
    List<User> findByAgeBetween(Integer minAge, Integer maxAge);
    
    // Full-Text Search
    @Query("SELECT META().id, * FROM #{#n1ql.bucket} WHERE #{#n1ql.filter} " +
           "AND SEARCH(name, $1)")
    List<User> searchByName(String searchTerm);
}
```

### Service

```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private CouchbaseTemplate couchbaseTemplate;
    
    public User createUser(User user) {
        return userRepository.save(user);
    }
    
    public List<User> findUsersBySkill(String skill) {
        String query = "SELECT * FROM users WHERE ANY s IN skills SATISFIES s = $1 END";
        return couchbaseTemplate.findByQuery(User.class)
            .matching(Query.query(QueryCriteria.where("skills").contains(skill)))
            .all();
    }
}
```

---

## 📊 Couchbase vs MongoDB

| Feature | Couchbase | MongoDB |
|---------|-----------|---------|
| **Query Language** | N1QL (SQL-like) | MongoDB Query Language |
| **Architecture** | Memory-first | Disk-based with cache |
| **Indexing** | GSI, Memory-optimized | B-tree indexes |
| **Full-Text Search** | Built-in | Separate Atlas Search |
| **Mobile Sync** | Built-in Sync Gateway | Realm Sync |
| **Transactions** | Multi-document ACID | Multi-document ACID |
| **Scaling** | Auto-sharding | Manual sharding |
| **Use Cases** | High-performance apps, Mobile | General purpose NoSQL |

---

## 🏆 For 3.5+ Years Experience

### What Interviewers Expect

**Technical Knowledge:**
- Couchbase architecture
- N1QL proficiency
- Index optimization
- Cluster management
- XDCR setup

**Production Experience:**
- High-availability setup
- Performance tuning
- Monitoring and alerts
- Backup strategies
- Disaster recovery

**Problem-Solving:**
- Schema design for use cases
- Query optimization
- Handle high throughput
- Implement caching
- Data consistency

---

## 📊 Interview Success Metrics

| Topic | Importance | Interview Frequency |
|-------|------------|-------------------|
| Architecture | 🔴 Critical | 85% |
| N1QL Queries | 🔴 Critical | 90% |
| Indexing | 🔴 Critical | 80% |
| Data Modeling | 🟡 Important | 75% |
| XDCR | 🟡 Important | 60% |
| FTS | 🟢 Good to Know | 50% |
| Eventing | 🟢 Good to Know | 40% |

---

## ✅ Preparation Checklist

### Fundamentals
- [ ] Couchbase architecture
- [ ] Buckets, scopes, collections
- [ ] Document structure
- [ ] Key-value operations
- [ ] N1QL basics

### Advanced
- [ ] Complex N1QL queries
- [ ] JOINs and subqueries
- [ ] Full-Text Search
- [ ] Index strategies
- [ ] Query optimization

### Scaling
- [ ] Cluster architecture
- [ ] Replication
- [ ] XDCR
- [ ] Auto-failover
- [ ] Load balancing

### Integration
- [ ] Spring Data Couchbase
- [ ] Repository pattern
- [ ] Reactive programming
- [ ] Transactions
- [ ] Eventing service

---

## 🚀 Career Impact

**Salary with Couchbase Expertise:**
- **3-5 Years:** $100K-$145K
- **5-7 Years:** $135K-$180K
- **7+ Years:** $160K-$210K+

---

## 🔗 Quick Links

| Topic | Link |
|-------|------|
| Fundamentals | [01-fundamentals/README.md](01-fundamentals/README.md) |
| N1QL & Queries | [02-n1ql-queries/README.md](02-n1ql-queries/README.md) |
| Performance & Scaling | [03-performance-scaling/README.md](03-performance-scaling/README.md) |
| Spring Boot Integration | [04-spring-boot-integration/README.md](04-spring-boot-integration/README.md) |
| Interview Questions | [interview-questions/README.md](interview-questions/README.md) |
| Cheat Sheet | [CHEATSHEET.md](CHEATSHEET.md) |

---

**Ready to master Couchbase?** 🗄️

👉 **[Start with Fundamentals →](01-fundamentals/README.md)**

