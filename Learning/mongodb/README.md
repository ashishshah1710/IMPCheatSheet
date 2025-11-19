# 🍃 MongoDB - Complete Guide

**For 3.5+ Years Experienced Developers | Interview Preparation**

Master MongoDB NoSQL database and ace your technical interviews!

---

## 📖 Overview

MongoDB is a document-oriented NoSQL database used for high volume data storage. Instead of tables and rows as in traditional relational databases, MongoDB uses collections and documents.

### Why MongoDB?

✅ **Schema-less** - Flexible data models  
✅ **Scalable** - Horizontal scaling with sharding  
✅ **High Performance** - Fast read/write operations  
✅ **Rich Query Language** - Powerful aggregation framework  
✅ **Replication** - High availability with replica sets  
✅ **Industry Leader** - Used by EA, Google, Adobe, eBay  

---

## 🎯 Learning Path for Experienced Developers

### Phase 1: MongoDB Fundamentals (1 week)
**Master core concepts**

- Document model vs Relational
- BSON data types
- CRUD operations
- Query operators
- Indexes and performance
- Data modeling principles

**👉 Start:** [`01-fundamentals/README.md`](01-fundamentals/README.md)

---

### Phase 2: Advanced Queries & Aggregation (1 week)
**Master complex operations**

- Aggregation Pipeline
- $lookup (joins)
- $group, $project, $match
- Text search
- Geospatial queries
- Array operations

**👉 Continue:** [`02-advanced-queries/README.md`](02-advanced-queries/README.md)

---

### Phase 3: Performance & Optimization (1 week)
**Production-ready MongoDB**

- Index strategies
- Query optimization
- Explain plans
- Connection pooling
- Memory management
- Monitoring tools

**👉 Master:** [`03-performance/README.md`](03-performance/README.md)

---

### Phase 4: Replication & Sharding (1 week)
**Scale MongoDB**

- Replica sets
- Read preferences
- Write concerns
- Sharding architecture
- Shard keys
- Data distribution

**👉 Advanced:** [`04-scaling/README.md`](04-scaling/README.md)

---

## 💼 Interview Preparation

### Top Interview Questions

**Fundamentals:**
- SQL vs NoSQL databases?
- When to use MongoDB?
- Document structure best practices
- ACID in MongoDB
- Atomicity at document level

**Queries:**
- Difference between find() and aggregate()?
- How to join collections?
- Text search implementation
- Array query operations
- Regular expressions in queries

**Performance:**
- Types of indexes
- Compound index order
- Index intersection
- Covered queries
- Query optimization strategies

**Scaling:**
- Replica set architecture
- Automatic failover
- Sharding vs Replication
- Choosing shard key
- Handling hotspots

**👉 See:** [`interview-questions/README.md`](interview-questions/README.md)

---

## 📚 Content Structure

```
mongodb/
├── 01-fundamentals/
│   ├── README.md                      # MongoDB basics
│   ├── data-modeling.md              # Document design
│   ├── crud-operations.md            # Create, Read, Update, Delete
│   ├── query-operators.md            # Comparison, Logical ops
│   └── basic-indexes.md              # Index fundamentals
│
├── 02-advanced-queries/
│   ├── README.md                      # Advanced querying
│   ├── aggregation-pipeline.md       # Aggregation framework
│   ├── lookup-joins.md               # Joining collections
│   ├── text-search.md                # Full-text search
│   └── geospatial.md                 # Location queries
│
├── 03-performance/
│   ├── README.md                      # Performance tuning
│   ├── index-strategies.md           # Index best practices
│   ├── query-optimization.md         # Optimize queries
│   ├── explain-plans.md              # Analyze queries
│   └── monitoring.md                 # Performance monitoring
│
├── 04-scaling/
│   ├── README.md                      # Scaling MongoDB
│   ├── replica-sets.md               # High availability
│   ├── sharding.md                   # Horizontal scaling
│   ├── backup-restore.md             # Data backup
│   └── security.md                   # Authentication & encryption
│
├── spring-boot-integration/
│   ├── README.md                      # Spring Boot + MongoDB
│   ├── spring-data-mongodb.md        # Spring Data integration
│   ├── repository-pattern.md         # Repository interfaces
│   └── transactions.md               # Multi-document transactions
│
├── interview-questions/
│   ├── README.md                      # All questions
│   ├── fundamentals.md               # Basic questions
│   ├── queries.md                    # Query questions
│   ├── performance.md                # Performance Q&A
│   ├── scaling.md                    # Scaling questions
│   └── scenario-based.md             # Real scenarios
│
├── real-world-examples/
│   ├── e-commerce-schema/            # Product catalog
│   ├── social-media-posts/           # Posts & comments
│   ├── time-series-data/             # IoT data
│   └── user-management/              # User profiles
│
└── CHEATSHEET.md                      # Quick reference
```

---

## 🎯 Quick Start

### Installation & Setup

```bash
# Install MongoDB (macOS)
brew tap mongodb/brew
brew install mongodb-community

# Start MongoDB
brew services start mongodb-community

# Connect to MongoDB
mongosh
```

### Basic CRUD Operations

```javascript
// Switch to database
use mydb

// Insert Documents
db.users.insertOne({
  name: "John Doe",
  email: "john@example.com",
  age: 30,
  address: {
    street: "123 Main St",
    city: "New York",
    country: "USA"
  },
  hobbies: ["reading", "coding"],
  createdAt: new Date()
})

db.users.insertMany([
  { name: "Jane Smith", email: "jane@example.com", age: 25 },
  { name: "Bob Johnson", email: "bob@example.com", age: 35 }
])

// Find Documents
db.users.find()
db.users.find({ age: { $gt: 25 } })
db.users.find({ name: /John/ })
db.users.findOne({ email: "john@example.com" })

// Update Documents
db.users.updateOne(
  { email: "john@example.com" },
  { $set: { age: 31 } }
)

db.users.updateMany(
  { age: { $lt: 30 } },
  { $set: { status: "young" } }
)

// Delete Documents
db.users.deleteOne({ email: "john@example.com" })
db.users.deleteMany({ age: { $gt: 50 } })

// Count Documents
db.users.countDocuments({ age: { $gt: 25 } })
```

### Aggregation Pipeline

```javascript
// Group by age and count
db.users.aggregate([
  {
    $group: {
      _id: "$age",
      count: { $sum: 1 },
      names: { $push: "$name" }
    }
  },
  {
    $sort: { count: -1 }
  }
])

// Join collections (lookup)
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "userDetails"
    }
  },
  {
    $unwind: "$userDetails"
  },
  {
    $project: {
      orderId: 1,
      userName: "$userDetails.name",
      total: 1
    }
  }
])

// Complex aggregation
db.sales.aggregate([
  {
    $match: {
      date: { $gte: ISODate("2024-01-01") }
    }
  },
  {
    $group: {
      _id: {
        year: { $year: "$date" },
        month: { $month: "$date" }
      },
      totalSales: { $sum: "$amount" },
      averageSale: { $avg: "$amount" },
      count: { $sum: 1 }
    }
  },
  {
    $sort: { "_id.year": 1, "_id.month": 1 }
  }
])
```

### Indexes

```javascript
// Create indexes
db.users.createIndex({ email: 1 })  // Single field
db.users.createIndex({ age: 1, name: 1 })  // Compound
db.users.createIndex({ name: "text" })  // Text index
db.users.createIndex({ location: "2dsphere" })  // Geospatial

// View indexes
db.users.getIndexes()

// Drop index
db.users.dropIndex("email_1")

// Analyze query
db.users.find({ email: "john@example.com" }).explain("executionStats")
```

---

## 🍃 Spring Boot Integration

### Dependencies (pom.xml)

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```

### Configuration

```yaml
spring:
  data:
    mongodb:
      uri: mongodb://localhost:27017/mydb
      # Or detailed configuration
      host: localhost
      port: 27017
      database: mydb
      username: admin
      password: password
      authentication-database: admin
```

### Entity

```java
@Document(collection = "users")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    
    @Id
    private String id;
    
    @Indexed(unique = true)
    private String email;
    
    private String name;
    private Integer age;
    
    @DBRef
    private Address address;
    
    private List<String> hobbies;
    
    @CreatedDate
    private LocalDateTime createdAt;
    
    @LastModifiedDate
    private LocalDateTime updatedAt;
}
```

### Repository

```java
public interface UserRepository extends MongoRepository<User, String> {
    
    // Query methods
    Optional<User> findByEmail(String email);
    List<User> findByAgeGreaterThan(Integer age);
    List<User> findByNameContainingIgnoreCase(String name);
    
    // Custom queries
    @Query("{ 'age': { $gte: ?0, $lte: ?1 } }")
    List<User> findByAgeBetween(Integer minAge, Integer maxAge);
    
    @Query("{ 'hobbies': ?0 }")
    List<User> findByHobby(String hobby);
    
    // Aggregation
    @Aggregation(pipeline = {
        "{ $match: { age: { $gte: ?0 } } }",
        "{ $group: { _id: '$age', count: { $sum: 1 } } }",
        "{ $sort: { count: -1 } }"
    })
    List<AgeCount> countUsersByAge(Integer minAge);
}
```

### Service

```java
@Service
@Slf4j
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private MongoTemplate mongoTemplate;
    
    public User createUser(User user) {
        return userRepository.save(user);
    }
    
    public List<User> findUsersByAgeRange(Integer minAge, Integer maxAge) {
        Query query = new Query();
        query.addCriteria(
            Criteria.where("age").gte(minAge).lte(maxAge)
        );
        return mongoTemplate.find(query, User.class);
    }
    
    public List<User> searchUsers(String searchTerm) {
        TextCriteria criteria = TextCriteria.forDefaultLanguage()
            .matchingAny(searchTerm);
        Query query = TextQuery.queryText(criteria);
        return mongoTemplate.find(query, User.class);
    }
}
```

---

## 🏆 For 3.5+ Years Experience

### What Interviewers Expect

**Technical Depth:**
- Document design patterns
- Aggregation mastery
- Index optimization
- Replica set understanding
- Sharding concepts

**Real-World Experience:**
- Production deployment
- Performance tuning
- Data migration
- Backup strategies
- Monitoring setup

**Problem-Solving:**
- Design schemas for use cases
- Optimize slow queries
- Handle large datasets
- Implement caching
- Data consistency strategies

---

## 📊 Interview Success Metrics

| Topic | Importance | Interview Frequency |
|-------|------------|-------------------|
| Document Model | 🔴 Critical | 90% |
| CRUD Operations | 🔴 Critical | 85% |
| Aggregation Pipeline | 🔴 Critical | 80% |
| Indexes | 🔴 Critical | 85% |
| Replica Sets | 🟡 Important | 70% |
| Sharding | 🟡 Important | 60% |
| Transactions | 🟢 Good to Know | 50% |

---

## ✅ Preparation Checklist

### Fundamentals
- [ ] Document vs Relational model
- [ ] BSON data types
- [ ] CRUD operations
- [ ] Query operators
- [ ] Data modeling patterns

### Advanced
- [ ] Aggregation pipeline
- [ ] $lookup operations
- [ ] Text search
- [ ] Array queries
- [ ] Geospatial queries

### Performance
- [ ] Index types
- [ ] Query optimization
- [ ] Explain plans
- [ ] Covered queries
- [ ] Index strategies

### Scaling
- [ ] Replica sets
- [ ] Read/Write concerns
- [ ] Sharding architecture
- [ ] Shard key selection
- [ ] Backup strategies

---

## 🚀 Career Impact

**Salary with MongoDB Expertise:**
- **3-5 Years:** $95K-$140K
- **5-7 Years:** $130K-$175K
- **7+ Years:** $150K-$200K+

---

## 🔗 Quick Links

| Topic | Link |
|-------|------|
| Fundamentals | [01-fundamentals/README.md](01-fundamentals/README.md) |
| Advanced Queries | [02-advanced-queries/README.md](02-advanced-queries/README.md) |
| Performance | [03-performance/README.md](03-performance/README.md) |
| Scaling | [04-scaling/README.md](04-scaling/README.md) |
| Spring Boot Integration | [spring-boot-integration/README.md](spring-boot-integration/README.md) |
| Interview Questions | [interview-questions/README.md](interview-questions/README.md) |
| Cheat Sheet | [CHEATSHEET.md](CHEATSHEET.md) |

---

**Ready to master MongoDB?** 🍃

👉 **[Start with Fundamentals →](01-fundamentals/README.md)**

