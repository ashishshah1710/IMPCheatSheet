# 🍃 MongoDB - Beginner Level

Learn NoSQL database fundamentals with MongoDB!

---

## 📚 Table of Contents

1. [What is MongoDB?](#what-is-mongodb)
2. [Installation & Setup](#installation-setup)
3. [CRUD Operations](#crud-operations)
4. [Data Modeling](#data-modeling)
5. [Queries & Filtering](#queries-filtering)
6. [Indexes](#indexes)
7. [Aggregation Basics](#aggregation-basics)
8. [Interview Questions](#interview-questions)

---

## 🎯 What is MongoDB?

MongoDB is a **NoSQL document database** that stores data in flexible, JSON-like documents.

### Key Features:
- **Document-Oriented:** Store data as BSON (Binary JSON)
- **Schema-less:** No fixed schema required
- **Scalable:** Horizontal scaling with sharding
- **High Performance:** Fast read/write operations
- **Flexible:** Easy to evolve data model

### MongoDB vs SQL

| Feature | MongoDB | SQL Database |
|---------|---------|--------------|
| **Data Model** | Documents (JSON-like) | Tables with rows |
| **Schema** | Dynamic | Fixed schema |
| **Relationships** | Embedded or referenced | Foreign keys |
| **Scaling** | Horizontal (sharding) | Vertical (bigger server) |
| **Transactions** | Multi-document (v4.0+) | ACID transactions |
| **Query Language** | MongoDB Query Language | SQL |

---

## 🛠️ Installation & Setup

### Install MongoDB

```bash
# Windows (using Chocolatey)
choco install mongodb

# macOS
brew tap mongodb/brew
brew install mongodb-community

# Linux (Ubuntu)
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org

# Start MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod
```

### MongoDB Shell (mongosh)

```bash
# Install mongosh
npm install -g mongosh

# Connect to MongoDB
mongosh

# Or connect to specific host
mongosh "mongodb://localhost:27017"
```

### Basic Commands

```javascript
// Show databases
show dbs

// Create/Switch to database
use myapp

// Show collections
show collections

// Get current database
db

// Drop database
db.dropDatabase()
```

---

## ✍️ CRUD Operations

### Create (Insert)

```javascript
// Insert one document
db.users.insertOne({
  name: "John Doe",
  email: "john@example.com",
  age: 30,
  city: "New York"
})

// Insert multiple documents
db.users.insertMany([
  { name: "Jane Smith", email: "jane@example.com", age: 25 },
  { name: "Bob Wilson", email: "bob@example.com", age: 35 }
])

// Result includes _id (auto-generated)
// {
//   acknowledged: true,
//   insertedId: ObjectId("...")
// }
```

### Read (Find)

```javascript
// Find all documents
db.users.find()

// Find with pretty print
db.users.find().pretty()

// Find one document
db.users.findOne({ name: "John Doe" })

// Find with filter
db.users.find({ age: 30 })

// Find with multiple conditions (AND)
db.users.find({ age: 30, city: "New York" })

// Find with OR
db.users.find({
  $or: [
    { age: 30 },
    { city: "Los Angeles" }
  ]
})

// Count documents
db.users.countDocuments({ age: { $gte: 25 } })

// Limit results
db.users.find().limit(5)

// Skip results (pagination)
db.users.find().skip(10).limit(5)

// Sort results
db.users.find().sort({ age: 1 })   // 1 = ascending
db.users.find().sort({ age: -1 })  // -1 = descending
```

### Update

```javascript
// Update one document
db.users.updateOne(
  { name: "John Doe" },           // Filter
  { $set: { age: 31 } }           // Update
)

// Update multiple documents
db.users.updateMany(
  { city: "New York" },
  { $set: { country: "USA" } }
)

// Increment value
db.users.updateOne(
  { name: "John Doe" },
  { $inc: { age: 1 } }            // Increment age by 1
)

// Add to array
db.users.updateOne(
  { name: "John Doe" },
  { $push: { hobbies: "reading" } }
)

// Remove field
db.users.updateOne(
  { name: "John Doe" },
  { $unset: { city: "" } }
)

// Replace entire document
db.users.replaceOne(
  { name: "John Doe" },
  { name: "John Doe", email: "newemail@example.com", age: 32 }
)

// Upsert (insert if not exists)
db.users.updateOne(
  { email: "new@example.com" },
  { $set: { name: "New User", age: 25 } },
  { upsert: true }
)
```

### Delete

```javascript
// Delete one document
db.users.deleteOne({ name: "John Doe" })

// Delete multiple documents
db.users.deleteMany({ age: { $lt: 25 } })

// Delete all documents in collection
db.users.deleteMany({})

// Drop collection
db.users.drop()
```

---

## 📊 Data Modeling

### Embedded Documents

```javascript
// User with embedded address
db.users.insertOne({
  name: "John Doe",
  email: "john@example.com",
  address: {
    street: "123 Main St",
    city: "New York",
    state: "NY",
    zip: "10001"
  },
  phones: [
    { type: "home", number: "555-1234" },
    { type: "work", number: "555-5678" }
  ]
})

// Query embedded documents
db.users.find({ "address.city": "New York" })
db.users.find({ "phones.type": "home" })
```

### Referenced Documents

```javascript
// Posts collection
db.posts.insertOne({
  title: "My First Post",
  content: "This is my first blog post",
  authorId: ObjectId("649abc123..."),  // Reference to user
  createdAt: new Date()
})

// Query with reference
const user = db.users.findOne({ name: "John Doe" })
const userPosts = db.posts.find({ authorId: user._id })
```

---

## 🔍 Queries & Filtering

### Comparison Operators

```javascript
// Equal
db.users.find({ age: 30 })

// Greater than
db.users.find({ age: { $gt: 30 } })

// Greater than or equal
db.users.find({ age: { $gte: 30 } })

// Less than
db.users.find({ age: { $lt: 30 } })

// Less than or equal
db.users.find({ age: { $lte: 30 } })

// Not equal
db.users.find({ age: { $ne: 30 } })

// In array
db.users.find({ city: { $in: ["New York", "Los Angeles"] } })

// Not in array
db.users.find({ city: { $nin: ["Chicago", "Boston"] } })
```

### Logical Operators

```javascript
// AND (implicit)
db.users.find({ age: 30, city: "New York" })

// OR
db.users.find({
  $or: [
    { age: 30 },
    { city: "Los Angeles" }
  ]
})

// AND + OR
db.users.find({
  age: { $gte: 25 },
  $or: [
    { city: "New York" },
    { city: "Los Angeles" }
  ]
})

// NOT
db.users.find({ age: { $not: { $gt: 30 } } })

// NOR
db.users.find({
  $nor: [
    { age: { $lt: 25 } },
    { city: "Chicago" }
  ]
})
```

### Array Queries

```javascript
// Match array element
db.users.find({ hobbies: "reading" })

// Match all elements
db.users.find({ hobbies: { $all: ["reading", "gaming"] } })

// Array size
db.users.find({ hobbies: { $size: 3 } })

// Element match
db.users.find({
  phones: {
    $elemMatch: { type: "home", number: { $exists: true } }
  }
})
```

### Text Search

```javascript
// Create text index
db.posts.createIndex({ title: "text", content: "text" })

// Text search
db.posts.find({ $text: { $search: "mongodb tutorial" } })

// Text search with score
db.posts.find(
  { $text: { $search: "mongodb" } },
  { score: { $meta: "textScore" } }
).sort({ score: { $meta: "textScore" } })
```

---

## 🚀 Indexes

### Creating Indexes

```javascript
// Single field index
db.users.createIndex({ email: 1 })  // 1 = ascending

// Compound index
db.users.createIndex({ city: 1, age: -1 })

// Unique index
db.users.createIndex({ email: 1 }, { unique: true })

// Partial index
db.users.createIndex(
  { age: 1 },
  { partialFilterExpression: { age: { $gte: 18 } } }
)

// TTL index (auto-delete after time)
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 3600 }  // Delete after 1 hour
)
```

### Managing Indexes

```javascript
// List indexes
db.users.getIndexes()

// Drop index
db.users.dropIndex("email_1")

// Drop all indexes
db.users.dropIndexes()

// Index stats
db.users.stats()
```

---

## 📈 Aggregation Basics

### Aggregation Pipeline

```javascript
// Match -> Group -> Sort
db.orders.aggregate([
  // Stage 1: Filter
  { $match: { status: "completed" } },
  
  // Stage 2: Group and sum
  { $group: {
    _id: "$customerId",
    totalSpent: { $sum: "$amount" },
    orderCount: { $sum: 1 }
  }},
  
  // Stage 3: Sort
  { $sort: { totalSpent: -1 } },
  
  // Stage 4: Limit
  { $limit: 10 }
])

// Count by category
db.products.aggregate([
  { $group: {
    _id: "$category",
    count: { $sum: 1 },
    avgPrice: { $avg: "$price" }
  }}
])

// Lookup (join)
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "user"
    }
  }
])
```

---

## 🎯 Interview Questions

**Q1: What is MongoDB and when should you use it?**

**Answer:**
MongoDB is a NoSQL document database. Use it when:
- Schema flexibility is needed
- Rapid development and iteration
- Scaling horizontally
- Handling large volumes of unstructured data
- Real-time analytics

**Q2: What is the difference between find() and findOne()?**

**Answer:**
- `find()`: Returns a cursor to all matching documents
- `findOne()`: Returns the first matching document

**Q3: What are ObjectIds?**

**Answer:**
12-byte unique identifier automatically generated for `_id` field:
- 4 bytes: timestamp
- 5 bytes: random value
- 3 bytes: counter

**Q4: Embedded vs Referenced documents?**

**Answer:**
- **Embedded:** Store related data together (1-to-1, 1-to-few)
- **Referenced:** Store references to other documents (1-to-many, many-to-many)

---

## 💡 Practice Exercises

```javascript
// Exercise 1: Create a blog database
use blog
db.posts.insertMany([
  { title: "Post 1", author: "John", views: 100, tags: ["mongodb", "nosql"] },
  { title: "Post 2", author: "Jane", views: 250, tags: ["javascript"] },
  { title: "Post 3", author: "John", views: 180, tags: ["mongodb", "database"] }
])

// Exercise 2: Find posts by John with > 150 views
// Exercise 3: Update all posts to add a "published" field
// Exercise 4: Count posts by author
// Exercise 5: Find posts tagged with "mongodb"
```

---

**Continue to Intermediate MongoDB for advanced queries and performance!** 🚀

