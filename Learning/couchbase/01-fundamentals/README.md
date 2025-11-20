# 🪣 Couchbase - Fundamentals

Master the basics of Couchbase NoSQL database!

---

## 📚 Table of Contents

1. [What is Couchbase?](#what-is-couchbase)
2. [Installation & Setup](#installation-setup)
3. [Key Concepts](#key-concepts)
4. [CRUD Operations](#crud-operations)
5. [Document Structure](#document-structure)
6. [Basic Queries](#basic-queries)
7. [Indexes](#indexes)
8. [Interview Questions](#interview-questions)

---

## 🎯 What is Couchbase?

Couchbase is a **NoSQL document database** with a distributed architecture, designed for interactive applications.

### Key Features:
- **Memory-First Architecture:** Sub-millisecond data operations
- **SQL-Like Query Language:** N1QL (SQL for JSON)
- **Flexible JSON Documents:** Schema-less data model
- **Built-in Caching:** Integrated Memcached
- **Multi-Model:** Key-value + Document + Full-text search
- **Mobile Sync:** Couchbase Lite for offline-first apps

### Couchbase vs Other NoSQL

| Feature | Couchbase | MongoDB | Redis |
|---------|-----------|---------|-------|
| **Data Model** | JSON documents | BSON documents | Key-value |
| **Query Language** | N1QL (SQL++) | MongoDB Query | Commands |
| **Performance** | Sub-millisecond | Milliseconds | Microseconds |
| **Caching** | Built-in | External | Native |
| **ACID** | Yes (7.0+) | Yes (4.0+) | Transactions |
| **Scalability** | Horizontal | Horizontal | Vertical/Horizontal |

---

## 🛠️ Installation & Setup

### Install Couchbase Server

```bash
# Docker (Recommended for development)
docker run -d --name couchbase \
  -p 8091-8096:8091-8096 \
  -p 11210-11211:11210-11211 \
  couchbase:latest

# Access Web Console
# http://localhost:8091

# Setup wizard:
# 1. Configure new cluster
# 2. Set admin credentials
# 3. Setup services (Data, Query, Index, Search)
# 4. Configure memory quotas
# 5. Create sample bucket
```

### Install Couchbase SDK (Java)

```xml
<!-- Maven -->
<dependency>
    <groupId>com.couchbase.client</groupId>
    <artifactId>java-client</artifactId>
    <version>3.4.11</version>
</dependency>
```

```gradle
// Gradle
implementation 'com.couchbase.client:java-client:3.4.11'
```

### Basic Connection

```java
import com.couchbase.client.java.*;
import com.couchbase.client.java.kv.*;

public class CouchbaseConnection {
    public static void main(String[] args) {
        // Connect to cluster
        Cluster cluster = Cluster.connect(
            "localhost",
            "Administrator",
            "password"
        );
        
        // Open bucket
        Bucket bucket = cluster.bucket("travel-sample");
        Collection collection = bucket.defaultCollection();
        
        // Your operations here
        
        // Cleanup
        cluster.disconnect();
    }
}
```

---

## 🔑 Key Concepts

### Cluster Architecture

```
┌─────────────────────────────────────────────────────┐
│              Couchbase Cluster                       │
├─────────────────────────────────────────────────────┤
│  Node 1          Node 2          Node 3              │
│  ┌────────┐     ┌────────┐     ┌────────┐          │
│  │ Data   │     │ Data   │     │ Data   │          │
│  │ Query  │     │ Query  │     │ Index  │          │
│  │ Index  │     │ Search │     │ Search │          │
│  └────────┘     └────────┘     └────────┘          │
├─────────────────────────────────────────────────────┤
│  Buckets (similar to databases)                     │
│  ├── Bucket 1                                        │
│  │   ├── Scope 1                                     │
│  │   │   ├── Collection A (like tables)             │
│  │   │   └── Collection B                           │
│  │   └── Scope 2                                     │
│  └── Bucket 2                                        │
└─────────────────────────────────────────────────────┘
```

### Hierarchy

```
Cluster
  └── Bucket (like database)
      └── Scope (namespace)
          └── Collection (like table)
              └── Documents (JSON)
```

### Services

```yaml
Data Service:
  - Store and retrieve documents
  - Automatic sharding and replication

Query Service:
  - N1QL query processing
  - SQL++ for JSON

Index Service:
  - Secondary indexes
  - Primary indexes
  - Array indexes

Search Service:
  - Full-text search
  - Fuzzy matching

Analytics Service:
  - Complex analytical queries
  - Parallel query processing

Eventing Service:
  - Real-time event processing
  - Triggers on data changes
```

---

## ✍️ CRUD Operations

### Create (Insert)

```java
import com.couchbase.client.java.json.*;

public class CRUDOperations {
    public static void main(String[] args) {
        Cluster cluster = Cluster.connect("localhost", "Administrator", "password");
        Bucket bucket = cluster.bucket("travel-sample");
        Collection collection = bucket.defaultCollection();
        
        // Create JSON document
        JsonObject user = JsonObject.create()
            .put("type", "user")
            .put("name", "John Doe")
            .put("email", "john@example.com")
            .put("age", 30)
            .put("address", JsonObject.create()
                .put("city", "New York")
                .put("country", "USA")
            )
            .put("hobbies", JsonArray.from("reading", "gaming"));
        
        // Insert document
        MutationResult result = collection.insert("user::123", user);
        System.out.println("CAS: " + result.cas());
        
        // Insert with options
        InsertOptions options = InsertOptions.insertOptions()
            .timeout(Duration.ofSeconds(5));
        collection.insert("user::124", user, options);
        
        cluster.disconnect();
    }
}
```

### Read (Get)

```java
// Get document by key
GetResult result = collection.get("user::123");
JsonObject content = result.contentAsObject();

System.out.println("Name: " + content.getString("name"));
System.out.println("Email: " + content.getString("email"));
System.out.println("Age: " + content.getInt("age"));

// Get with projection (specific fields)
GetResult projected = collection.get(
    "user::123",
    GetOptions.getOptions().project("name", "email")
);

// Check if document exists
boolean exists = collection.exists("user::123").exists();
System.out.println("Document exists: " + exists);

// Get and touch (extend TTL)
GetResult touched = collection.getAndTouch(
    "user::123",
    Duration.ofHours(24)
);
```

### Update (Replace/Upsert)

```java
// Replace entire document
GetResult getResult = collection.get("user::123");
JsonObject doc = getResult.contentAsObject();
doc.put("age", 31);
collection.replace("user::123", doc);

// Upsert (insert or replace)
JsonObject newUser = JsonObject.create()
    .put("name", "Jane Doe")
    .put("email", "jane@example.com");
collection.upsert("user::125", newUser);

// Conditional update (CAS - Compare and Swap)
GetResult current = collection.get("user::123");
JsonObject updated = current.contentAsObject();
updated.put("age", 32);

try {
    collection.replace(
        "user::123",
        updated,
        ReplaceOptions.replaceOptions().cas(current.cas())
    );
    System.out.println("Update successful");
} catch (CasMismatchException e) {
    System.out.println("Document was modified by another process");
}
```

### Update (Subdocument Operations)

```java
// Update specific field
collection.mutateIn("user::123", Arrays.asList(
    MutateInSpec.upsert("age", 33),
    MutateInSpec.upsert("city", "Los Angeles")
));

// Increment counter
collection.mutateIn("user::123", Arrays.asList(
    MutateInSpec.increment("loginCount", 1)
));

// Array operations
collection.mutateIn("user::123", Arrays.asList(
    MutateInSpec.arrayAppend("hobbies", Arrays.asList("cooking")),
    MutateInSpec.arrayPrepend("hobbies", Arrays.asList("traveling"))
));

// Remove field
collection.mutateIn("user::123", Arrays.asList(
    MutateInSpec.remove("tempField")
));
```

### Delete

```java
// Remove document
collection.remove("user::123");

// Remove with CAS
GetResult doc = collection.get("user::123");
collection.remove(
    "user::123",
    RemoveOptions.removeOptions().cas(doc.cas())
);

// Remove with durability
collection.remove(
    "user::123",
    RemoveOptions.removeOptions()
        .durability(DurabilityLevel.MAJORITY)
);
```

---

## 📊 Document Structure

### Well-Designed Document

```json
{
  "type": "user",
  "userId": "user::12345",
  "profile": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "phone": "+1-555-0123",
    "dateOfBirth": "1990-01-15"
  },
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zipCode": "10001",
    "country": "USA"
  },
  "preferences": {
    "newsletter": true,
    "notifications": {
      "email": true,
      "sms": false,
      "push": true
    }
  },
  "metadata": {
    "createdAt": "2024-01-15T10:30:00Z",
    "updatedAt": "2024-01-20T15:45:00Z",
    "version": 2
  }
}
```

### Document Design Best Practices

```java
// 1. Include type field
JsonObject doc = JsonObject.create()
    .put("type", "order");

// 2. Use consistent naming (camelCase recommended)
doc.put("firstName", "John")
   .put("lastName", "Doe");

// 3. Store dates in ISO 8601 format
doc.put("createdAt", Instant.now().toString());

// 4. Use nested objects for related data
JsonObject address = JsonObject.create()
    .put("street", "123 Main St")
    .put("city", "New York");
doc.put("address", address);

// 5. Use arrays for collections
JsonArray items = JsonArray.from("item1", "item2", "item3");
doc.put("items", items);

// 6. Avoid deeply nested structures (max 3-4 levels)
// BAD: doc.a.b.c.d.e.f
// GOOD: Flatten or use references
```

---

## 🔍 Basic Queries

### N1QL Queries

```java
// Simple SELECT
QueryResult result = cluster.query(
    "SELECT * FROM `travel-sample` WHERE type = 'airline' LIMIT 10"
);

for (JsonObject row : result.rowsAsObject()) {
    System.out.println(row);
}

// Query with parameters
QueryResult paramResult = cluster.query(
    "SELECT * FROM `travel-sample` WHERE type = $type AND country = $country",
    QueryOptions.queryOptions()
        .parameters(JsonObject.create()
            .put("type", "airline")
            .put("country", "United States")
        )
);

// Count documents
QueryResult count = cluster.query(
    "SELECT COUNT(*) as total FROM `travel-sample` WHERE type = 'airline'"
);
System.out.println("Total airlines: " + 
    count.rowsAsObject().get(0).getInt("total"));

// Filtering
QueryResult filtered = cluster.query(
    "SELECT name, country, callsign " +
    "FROM `travel-sample` " +
    "WHERE type = 'airline' AND country = 'United States' " +
    "ORDER BY name LIMIT 5"
);

// Aggregation
QueryResult agg = cluster.query(
    "SELECT country, COUNT(*) as count " +
    "FROM `travel-sample` " +
    "WHERE type = 'airline' " +
    "GROUP BY country " +
    "ORDER BY count DESC " +
    "LIMIT 10"
);
```

---

## 📇 Indexes

### Primary Index

```sql
-- Create primary index
CREATE PRIMARY INDEX ON `travel-sample`;

-- Drop primary index
DROP PRIMARY INDEX ON `travel-sample`;
```

### Secondary Indexes

```sql
-- Create index on single field
CREATE INDEX idx_type ON `travel-sample`(type);

-- Create index on multiple fields
CREATE INDEX idx_airline_country 
ON `travel-sample`(type, country) 
WHERE type = 'airline';

-- Create index on nested field
CREATE INDEX idx_address_city 
ON `travel-sample`(address.city);

-- Create index on array
CREATE INDEX idx_hobbies 
ON `travel-sample`(DISTINCT ARRAY hobby FOR hobby IN hobbies END);

-- List all indexes
SELECT * FROM system:indexes WHERE keyspace_id = 'travel-sample';

-- Drop index
DROP INDEX `travel-sample`.idx_type;
```

### Using Indexes in Java

```java
// Query will use index automatically
QueryResult result = cluster.query(
    "SELECT * FROM `travel-sample` WHERE type = 'airline'"
);

// Explain query plan
QueryResult explain = cluster.query(
    "EXPLAIN SELECT * FROM `travel-sample` WHERE type = 'airline'"
);
System.out.println(explain.rowsAsObject());

// Build index programmatically
cluster.queryIndexes().createIndex(
    "travel-sample",
    "idx_country",
    Arrays.asList("country")
);
```

---

## 🎯 Interview Questions

**Q1: What is Couchbase and when should you use it?**

**Answer:**
Couchbase is a NoSQL document database with built-in caching. Use it when:
- Need sub-millisecond latency
- Building interactive applications
- Require SQL-like queries on JSON
- Need mobile/offline sync
- Horizontal scaling is important

**Q2: What is the difference between bucket, scope, and collection?**

**Answer:**
- **Bucket:** Top-level container (like database)
- **Scope:** Namespace within bucket
- **Collection:** Group of documents (like table)

**Q3: What is CAS in Couchbase?**

**Answer:**
CAS (Compare-And-Swap) is a value that changes each time a document is modified. Used for optimistic locking to prevent lost updates in concurrent scenarios.

**Q4: Primary vs Secondary Index?**

**Answer:**
- **Primary Index:** Indexes document keys, allows full bucket scans
- **Secondary Index:** Indexes document fields, optimizes specific queries

---

## 💡 Practice Exercises

```java
// Exercise 1: Create a user management system
// - Insert 10 users with different ages
// - Query users older than 25
// - Update a user's email
// - Delete a user

// Exercise 2: Implement blog system
// - Create blog posts with title, content, author
// - Query posts by author
// - Add comments to posts (subdocument)
// - Count posts per author

// Exercise 3: Build e-commerce product catalog
// - Insert products with categories
// - Create index on category
// - Query products by price range
// - Update product inventory
```

---

**Continue to N1QL & Queries for advanced querying!** 🚀

