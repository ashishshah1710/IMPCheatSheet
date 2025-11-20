# 🍃 MongoDB - Advanced Level

Master MongoDB for production environments and enterprise systems!

---

## 📚 Table of Contents

1. [Production Deployment](#production-deployment)
2. [Security & Authentication](#security-authentication)
3. [Backup & Recovery](#backup-recovery)
4. [Monitoring & Profiling](#monitoring-profiling)
5. [Change Streams](#change-streams)
6. [Time Series Collections](#time-series)
7. [Atlas & Cloud Deployment](#atlas-cloud)
8. [Interview Questions](#interview-questions)

---

## 🏭 Production Deployment

### Hardware Requirements

```yaml
Minimum Production Setup:
  CPU: 4+ cores
  RAM: 16GB+ (more for working set)
  Storage: SSD (NVMe preferred)
  Network: 10Gbps+

Replica Set (3 nodes):
  Primary: 8 cores, 32GB RAM
  Secondary: 8 cores, 32GB RAM
  Arbiter: 2 cores, 4GB RAM (optional)

Sharded Cluster:
  Config Servers: 3 nodes (4GB RAM each)
  Shard Servers: 3+ shards (scale based on data)
  mongos Routers: 2+ instances (4GB RAM each)
```

### mongod.conf Production Configuration

```yaml
# /etc/mongod.conf
storage:
  dbPath: /var/lib/mongodb
  journal:
    enabled: true
  engine: wiredTiger
  wiredTiger:
    engineConfig:
      cacheSizeGB: 24
      journalCompressor: snappy
    collectionConfig:
      blockCompressor: snappy
    indexConfig:
      prefixCompression: true

systemLog:
  destination: file
  path: /var/log/mongodb/mongod.log
  logAppend: true
  logRotate: reopen

net:
  port: 27017
  bindIp: 0.0.0.0
  maxIncomingConnections: 65536

security:
  authorization: enabled
  keyFile: /etc/mongodb-keyfile

replication:
  replSetName: rs0
  oplogSizeMB: 10240

operationProfiling:
  mode: slowOp
  slowOpThresholdMs: 100

setParameter:
  enableLocalhostAuthBypass: false
  cursorTimeoutMillis: 600000
```

---

## 🔐 Security & Authentication

### Role-Based Access Control

```javascript
// Create admin user
use admin
db.createUser({
  user: "admin",
  pwd: passwordPrompt(),
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" },
    { role: "dbAdminAnyDatabase", db: "admin" },
    { role: "clusterAdmin", db: "admin" }
  ]
})

// Create application user with limited permissions
use myapp
db.createUser({
  user: "appUser",
  pwd: passwordPrompt(),
  roles: [
    { role: "readWrite", db: "myapp" }
  ]
})

// Create read-only user
db.createUser({
  user: "readOnlyUser",
  pwd: passwordPrompt(),
  roles: [
    { role: "read", db: "myapp" }
  ]
})

// Custom role
use admin
db.createRole({
  role: "customRole",
  privileges: [
    {
      resource: { db: "myapp", collection: "" },
      actions: ["find", "insert", "update"]
    },
    {
      resource: { db: "myapp", collection: "sensitive" },
      actions: ["find"]
    }
  ],
  roles: []
})
```

### Encryption

```yaml
# Encryption at Rest (Enterprise)
security:
  enableEncryption: true
  encryptionKeyFile: /path/to/keyfile

# TLS/SSL Configuration
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/ca.pem
```

### Field-Level Encryption

```javascript
const { ClientEncryption } = require('mongodb-client-encryption')

const encryption = new ClientEncryption(client, {
  keyVaultNamespace: 'encryption.__keyVault',
  kmsProviders: {
    local: {
      key: Buffer.from(process.env.MASTER_KEY, 'base64')
    }
  }
})

// Encrypt sensitive field
const encrypted = await encryption.encrypt(
  'sensitive data',
  {
    algorithm: 'AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic',
    keyId: dataKeyId
  }
)

// Store encrypted data
await collection.insertOne({
  name: 'John',
  ssn: encrypted
})
```

---

## 💾 Backup & Recovery

### Backup Strategies

```bash
# 1. mongodump (logical backup)
mongodump \
  --host="replica-set/mongo1:27017,mongo2:27017" \
  --username=admin \
  --password=pass \
  --out=/backup/$(date +%Y%m%d) \
  --gzip \
  --oplog

# 2. mongorestore
mongorestore \
  --host="localhost:27017" \
  --username=admin \
  --password=pass \
  --gzip \
  --oplogReplay \
  /backup/20240101

# 3. File system snapshot (requires journaling)
# Stop writes
db.fsyncLock()
# Take snapshot
sudo lvcreate --size 10G --snapshot --name mongodb-snap /dev/vg0/mongodb
# Resume writes
db.fsyncUnlock()

# 4. Cloud Provider Snapshots (EBS, Azure Disk)
# Automated snapshots through cloud console
```

### Point-in-Time Recovery

```javascript
// Enable oplog
rs.conf()
// oplogSizeMB should be set appropriately

// Backup with oplog
mongodump --oplog --out=/backup

// Restore to specific point in time
mongorestore --oplogReplay --oplogLimit=1234567890:1 /backup
```

---

## 📊 Monitoring & Profiling

### Database Profiling

```javascript
// Enable profiling
db.setProfilingLevel(2)  // 0=off, 1=slow, 2=all

// Set slow threshold
db.setProfilingLevel(1, { slowms: 100 })

// View profile data
db.system.profile.find().limit(10).sort({ ts: -1 }).pretty()

// Analyze slow queries
db.system.profile.find({
  millis: { $gt: 100 }
}).sort({ millis: -1 })

// Disable profiling
db.setProfilingLevel(0)
```

### Server Status

```javascript
// Comprehensive server stats
db.serverStatus()

// Key metrics
const stats = db.serverStatus()
print("Connections:", stats.connections)
print("Network In:", stats.network.bytesIn)
print("Network Out:", stats.network.bytesOut)
print("Opcounters:", stats.opcounters)
print("Memory:", stats.mem)
print("WiredTiger Cache:", stats.wiredTiger.cache)

// Collection stats
db.users.stats()

// Index stats
db.users.aggregate([{ $indexStats: {} }])
```

### MongoDB Cloud Manager / Ops Manager

```javascript
// Metrics to monitor:
// - Query throughput (ops/sec)
// - Connection pool usage
// - Replication lag
// - Disk I/O
// - Cache hit ratio
// - Page faults
// - Lock percentage
// - Queue lengths

// Set up alerts
// - Replication lag > 10 seconds
// - Disk utilization > 80%
// - Connection count > 80% of max
// - Slow query threshold exceeded
```

---

## 🔄 Change Streams

### Real-Time Data Changes

```javascript
// Watch entire collection
const changeStream = db.orders.watch()

changeStream.on('change', (change) => {
  console.log('Change detected:', change)
  
  switch (change.operationType) {
    case 'insert':
      console.log('New order:', change.fullDocument)
      break
    case 'update':
      console.log('Order updated:', change.documentKey)
      break
    case 'delete':
      console.log('Order deleted:', change.documentKey)
      break
  }
})

// Watch with filter
const pipeline = [
  {
    $match: {
      'fullDocument.status': 'completed',
      'fullDocument.total': { $gt: 100 }
    }
  }
]

const filteredStream = db.orders.watch(pipeline)

// Watch entire database
const dbStream = db.watch()

// Resume from specific point
const resumeToken = changeStream.resumeToken
const resumedStream = db.orders.watch([], {
  resumeAfter: resumeToken
})
```

### Node.js Change Stream Example

```javascript
const { MongoClient } = require('mongodb')

async function watchOrders() {
  const client = new MongoClient('mongodb://localhost:27017')
  await client.connect()
  
  const db = client.db('myapp')
  const orders = db.collection('orders')
  
  const changeStream = orders.watch([
    {
      $match: {
        operationType: { $in: ['insert', 'update'] },
        'fullDocument.status': 'pending'
      }
    }
  ])
  
  console.log('Watching for order changes...')
  
  changeStream.on('change', async (change) => {
    console.log('Processing order:', change.fullDocument._id)
    
    // Process order
    await processOrder(change.fullDocument)
  })
  
  changeStream.on('error', (error) => {
    console.error('Change stream error:', error)
  })
}

watchOrders()
```

---

## ⏰ Time Series Collections

### Create Time Series Collection

```javascript
// MongoDB 5.0+
db.createCollection("weather", {
  timeseries: {
    timeField: "timestamp",
    metaField: "metadata",
    granularity: "seconds"  // seconds, minutes, hours
  }
})

// Insert time series data
db.weather.insertMany([
  {
    metadata: { sensorId: 5578, type: "temperature" },
    timestamp: ISODate("2024-01-01T00:00:00.000Z"),
    temp: 22.5
  },
  {
    metadata: { sensorId: 5578, type: "temperature" },
    timestamp: ISODate("2024-01-01T00:01:00.000Z"),
    temp: 22.6
  }
])

// Query time series
db.weather.find({
  "metadata.sensorId": 5578,
  timestamp: {
    $gte: ISODate("2024-01-01T00:00:00.000Z"),
    $lt: ISODate("2024-01-02T00:00:00.000Z")
  }
})

// Aggregate time series
db.weather.aggregate([
  {
    $match: {
      "metadata.sensorId": 5578,
      timestamp: {
        $gte: ISODate("2024-01-01"),
        $lt: ISODate("2024-02-01")
      }
    }
  },
  {
    $group: {
      _id: {
        $dateTrunc: {
          date: "$timestamp",
          unit: "hour"
        }
      },
      avgTemp: { $avg: "$temp" },
      minTemp: { $min: "$temp" },
      maxTemp: { $max: "$temp" }
    }
  },
  { $sort: { _id: 1 } }
])
```

---

## ☁️ Atlas & Cloud Deployment

### MongoDB Atlas Setup

```javascript
// Connection string
const uri = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/myapp?retryWrites=true&w=majority"

// Node.js connection with Atlas
const { MongoClient } = require('mongodb')

const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  maxPoolSize: 50,
  wtimeoutMS: 2500,
  retryWrites: true
})

async function connect() {
  try {
    await client.connect()
    console.log('Connected to MongoDB Atlas')
    
    const db = client.db('myapp')
    // Use database
    
  } catch (error) {
    console.error('Connection error:', error)
  }
}

// Atlas features:
// - Automated backups
// - Monitoring & alerts
// - Performance advisor
// - Index suggestions
// - Query profiler
// - Data migration
// - Serverless instances
```

### Production Connection Pool

```javascript
const options = {
  // Connection pool
  maxPoolSize: 50,
  minPoolSize: 10,
  
  // Timeouts
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 45000,
  connectTimeoutMS: 10000,
  
  // Retry writes
  retryWrites: true,
  
  // Write concern
  w: 'majority',
  wtimeoutMS: 2500,
  
  // Read preference
  readPreference: 'primaryPreferred',
  
  // Compression
  compressors: ['snappy', 'zlib']
}

const client = new MongoClient(uri, options)
```

---

## 🎯 Interview Questions

**Q: How do you handle a MongoDB outage in production?**

**Answer:**
1. Check replica set status (`rs.status()`)
2. Verify network connectivity
3. Check server resources (CPU, memory, disk)
4. Review logs for errors
5. Trigger failover if needed (`rs.stepDown()`)
6. Scale if necessary
7. Post-mortem analysis

**Q: What is the oplog and why is it important?**

**Answer:**
Oplog (operations log) is a special capped collection that records all write operations. Used for:
- Replication
- Change streams
- Point-in-time recovery
- Tailable cursors

**Q: How do you migrate data from SQL to MongoDB?**

**Answer:**
1. Analyze SQL schema and relationships
2. Design MongoDB schema (embedded vs referenced)
3. Export data (CSV, JSON)
4. Transform data
5. Use mongoimport or custom scripts
6. Validate data integrity
7. Update application code
8. Gradual cutover

---

**You're now a MongoDB expert ready for production!** 🚀

