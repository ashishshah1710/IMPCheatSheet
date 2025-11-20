# 🍃 MongoDB - Intermediate Level

Master advanced MongoDB queries, performance optimization, and production patterns!

---

## 📚 Table of Contents

1. [Advanced Aggregation](#advanced-aggregation)
2. [Schema Design Patterns](#schema-design-patterns)
3. [Transactions](#transactions)
4. [Replication](#replication)
5. [Sharding](#sharding)
6. [Performance Optimization](#performance-optimization)
7. [Data Validation](#data-validation)
8. [Interview Questions](#interview-questions)

---

## 📊 Advanced Aggregation

### Complex Pipeline Example

```javascript
db.sales.aggregate([
  // Stage 1: Match documents
  {
    $match: {
      date: {
        $gte: ISODate("2024-01-01"),
        $lt: ISODate("2024-12-31")
      },
      status: "completed"
    }
  },
  
  // Stage 2: Lookup (join) with products
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "productDetails"
    }
  },
  
  // Stage 3: Unwind array
  {
    $unwind: "$productDetails"
  },
  
  // Stage 4: Add computed fields
  {
    $addFields: {
      revenue: { $multiply: ["$quantity", "$productDetails.price"] },
      year: { $year: "$date" },
      month: { $month: "$date" }
    }
  },
  
  // Stage 5: Group by month
  {
    $group: {
      _id: { year: "$year", month: "$month" },
      totalRevenue: { $sum: "$revenue" },
      totalOrders: { $sum: 1 },
      avgOrderValue: { $avg: "$revenue" },
      topProduct: { $first: "$productDetails.name" }
    }
  },
  
  // Stage 6: Sort
  {
    $sort: { "_id.year": 1, "_id.month": 1 }
  },
  
  // Stage 7: Project (reshape output)
  {
    $project: {
      _id: 0,
      period: {
        $concat: [
          { $toString: "$_id.year" },
          "-",
          { $toString: "$_id.month" }
        ]
      },
      totalRevenue: 1,
      totalOrders: 1,
      avgOrderValue: { $round: ["$avgOrderValue", 2] }
    }
  }
])
```

### Useful Aggregation Operators

```javascript
// Conditional expressions
db.products.aggregate([
  {
    $project: {
      name: 1,
      price: 1,
      priceCategory: {
        $switch: {
          branches: [
            { case: { $lt: ["$price", 20] }, then: "Budget" },
            { case: { $lt: ["$price", 50] }, then: "Mid-range" }
          ],
          default: "Premium"
        }
      }
    }
  }
])

// Array operations
db.orders.aggregate([
  {
    $project: {
      orderId: 1,
      itemCount: { $size: "$items" },
      firstItem: { $arrayElemAt: ["$items", 0] },
      lastItem: { $arrayElemAt: ["$items", -1] },
      itemNames: { $map: {
        input: "$items",
        as: "item",
        in: "$$item.name"
      }}
    }
  }
])

// Date operations
db.logs.aggregate([
  {
    $project: {
      timestamp: 1,
      dayOfWeek: { $dayOfWeek: "$timestamp" },
      hour: { $hour: "$timestamp" },
      dateString: { $dateToString: {
        format: "%Y-%m-%d %H:%M:%S",
        date: "$timestamp"
      }}
    }
  }
])
```

---

## 🏗️ Schema Design Patterns

### 1. Embedded Pattern (One-to-Few)

```javascript
// User with addresses
db.users.insertOne({
  _id: ObjectId("..."),
  name: "John Doe",
  email: "john@example.com",
  addresses: [
    {
      type: "home",
      street: "123 Main St",
      city: "New York",
      zip: "10001"
    },
    {
      type: "work",
      street: "456 Office Ave",
      city: "New York",
      zip: "10002"
    }
  ]
})
```

### 2. Reference Pattern (One-to-Many)

```javascript
// Blog posts (separate collections)
db.users.insertOne({
  _id: ObjectId("user1"),
  name: "John Doe",
  email: "john@example.com"
})

db.posts.insertMany([
  {
    title: "First Post",
    content: "...",
    authorId: ObjectId("user1"),
    createdAt: new Date()
  },
  {
    title: "Second Post",
    content: "...",
    authorId: ObjectId("user1"),
    createdAt: new Date()
  }
])

// Query with $lookup
db.posts.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "authorId",
      foreignField: "_id",
      as: "author"
    }
  },
  { $unwind: "$author" }
])
```

### 3. Bucket Pattern (Large datasets)

```javascript
// Time-series data bucketing
db.sensor_data_hourly.insertOne({
  sensorId: "sensor_001",
  date: ISODate("2024-01-01T10:00:00Z"),
  readings: [
    { time: ISODate("2024-01-01T10:00:00Z"), temp: 22.5 },
    { time: ISODate("2024-01-01T10:01:00Z"), temp: 22.6 },
    // ... up to 60 readings per hour
  ],
  count: 60,
  avgTemp: 22.5,
  minTemp: 21.8,
  maxTemp: 23.1
})
```

### 4. Extended Reference Pattern

```javascript
// Orders with denormalized product info
db.orders.insertOne({
  _id: ObjectId("order1"),
  customerId: ObjectId("customer1"),
  items: [
    {
      productId: ObjectId("product1"),
      // Denormalized for fast access
      productName: "Laptop",
      price: 999,
      quantity: 1
    }
  ],
  total: 999,
  orderDate: new Date()
})
```

---

## 💳 Transactions

### Multi-Document Transactions (MongoDB 4.0+)

```javascript
const session = db.getMongo().startSession()

session.startTransaction()

try {
  const accounts = session.getDatabase("bank").accounts
  
  // Debit from account A
  accounts.updateOne(
    { accountId: "A" },
    { $inc: { balance: -100 } },
    { session }
  )
  
  // Credit to account B
  accounts.updateOne(
    { accountId: "B" },
    { $inc: { balance: 100 } },
    { session }
  )
  
  session.commitTransaction()
  print("Transaction committed")
  
} catch (error) {
  session.abortTransaction()
  print("Transaction aborted: " + error)
} finally {
  session.endSession()
}
```

### Transaction with Error Handling

```javascript
async function transferMoney(fromAccount, toAccount, amount) {
  const session = client.startSession()
  
  try {
    await session.withTransaction(async () => {
      const accounts = client.db('bank').collection('accounts')
      
      // Check balance
      const from = await accounts.findOne(
        { accountId: fromAccount },
        { session }
      )
      
      if (from.balance < amount) {
        throw new Error('Insufficient funds')
      }
      
      // Perform transfer
      await accounts.updateOne(
        { accountId: fromAccount },
        { $inc: { balance: -amount } },
        { session }
      )
      
      await accounts.updateOne(
        { accountId: toAccount },
        { $inc: { balance: amount } },
        { session }
      )
    })
    
    console.log('Transfer successful')
  } finally {
    await session.endSession()
  }
}
```

---

## 🔄 Replication

### Replica Set Configuration

```javascript
// Initialize replica set
rs.initiate({
  _id: "myReplicaSet",
  members: [
    { _id: 0, host: "mongodb1:27017", priority: 2 },  // Primary
    { _id: 1, host: "mongodb2:27017", priority: 1 },  // Secondary
    { _id: 2, host: "mongodb3:27017", arbiterOnly: true }  // Arbiter
  ]
})

// Check replica set status
rs.status()

// Add member
rs.add("mongodb4:27017")

// Remove member
rs.remove("mongodb4:27017")

// Step down primary (for maintenance)
rs.stepDown(60)  // 60 seconds
```

### Read Preferences

```javascript
// Primary (default) - all reads from primary
db.users.find().readPref("primary")

// Primary Preferred - primary if available
db.users.find().readPref("primaryPreferred")

// Secondary - read from secondary only
db.users.find().readPref("secondary")

// Secondary Preferred
db.users.find().readPref("secondaryPreferred")

// Nearest - lowest latency
db.users.find().readPref("nearest")
```

---

## 🗂️ Sharding

### Shard Key Selection

```javascript
// Enable sharding on database
sh.enableSharding("myapp")

// Shard collection with hashed key
sh.shardCollection(
  "myapp.users",
  { userId: "hashed" }
)

// Shard with compound key
sh.shardCollection(
  "myapp.orders",
  { customerId: 1, orderDate: 1 }
)

// Check shard distribution
db.users.getShardDistribution()

// Shard status
sh.status()
```

---

## ⚡ Performance Optimization

### Explain Query Execution

```javascript
// Explain query plan
db.users.find({ email: "john@example.com" }).explain("executionStats")

// Output analysis:
// - executionTimeMillis: Query execution time
// - totalDocsExamined: Documents scanned
// - totalKeysExamined: Index keys scanned
// - executionStages: Query execution plan
```

### Index Strategies

```javascript
// Compound index for common queries
db.orders.createIndex({ customerId: 1, orderDate: -1 })

// Covered query (index-only)
db.users.find(
  { email: "john@example.com" },
  { email: 1, name: 1, _id: 0 }
)

// Index intersection
db.products.createIndex({ category: 1 })
db.products.createIndex({ price: 1 })
// MongoDB can use both indexes

// Sparse index (only indexed documents with field)
db.users.createIndex(
  { phoneNumber: 1 },
  { sparse: true }
)
```

### Query Optimization Tips

```javascript
// Use projection to limit fields
db.users.find({}, { name: 1, email: 1 })

// Limit results
db.users.find().limit(100)

// Use appropriate operators
db.users.find({ age: { $gte: 18 } })  // Better than $where

// Avoid $regex at start of string
db.users.find({ name: /^John/ })  // Use index
db.users.find({ name: /John/ })   // Cannot use index effectively

// Use $exists carefully
db.users.find({ optionalField: { $exists: true } })
```

---

## ✅ Data Validation

### Schema Validation

```javascript
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email", "age"],
      properties: {
        name: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        email: {
          bsonType: "string",
          pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
          description: "must be a valid email"
        },
        age: {
          bsonType: "int",
          minimum: 0,
          maximum: 120,
          description: "must be an integer between 0 and 120"
        },
        status: {
          enum: ["active", "inactive", "pending"],
          description: "can only be one of the enum values"
        }
      }
    }
  },
  validationLevel: "strict",
  validationAction: "error"
})

// Add validation to existing collection
db.runCommand({
  collMod: "users",
  validator: {
    $jsonSchema: { /* ... */ }
  }
})
```

---

## 🎯 Interview Questions

**Q: What is the difference between sharding and replication?**

**Answer:**
- **Replication:** Data redundancy for high availability (same data on multiple servers)
- **Sharding:** Data partitioning for horizontal scaling (different data on different servers)

**Q: How do you choose a shard key?**

**Answer:**
Good shard key characteristics:
- High cardinality (many unique values)
- Even distribution
- Query isolation (queries target specific shards)
- Avoid monotonically increasing keys

**Q: What is write concern?**

**Answer:**
Controls acknowledgment of write operations:
- `w: 1` - Acknowledged by primary (default)
- `w: "majority"` - Acknowledged by majority of replica set
- `w: 0` - No acknowledgment (fire and forget)

---

**Continue to Advanced MongoDB for production deployment!** 🚀

