# ⚡ Redis (In-Memory Data Store)

## Overview
Redis is an in-memory key-value store known for speed and versatility. Used for caching, sessions, real-time analytics, and more.

---

## Why Redis?

### ✅ Benefits
- **Blazing Fast**: Sub-millisecond latency (in-memory)
- **Versatile**: Multiple data structures
- **Persistence Options**: RDB snapshots, AOF logs
- **Pub/Sub**: Real-time messaging
- **Distributed**: Built-in clustering
- **Simple**: Easy to learn and use

### Use Cases
- **Caching**: Database query results, API responses
- **Session Storage**: User sessions
- **Real-Time Analytics**: Leaderboards, counters
- **Message Broker**: Pub/Sub, queues
- **Rate Limiting**: API throttling
- **Geospatial**: Location-based queries

---

## Installation

```bash
# Ubuntu
sudo apt update
sudo apt install redis-server

# Mac
brew install redis

# Start Redis
redis-server

# Start with config
redis-server /path/to/redis.conf

# CLI client
redis-cli
```

---

## Basic Commands

### Strings (Simple Key-Value)
```redis
# Set key
SET user:1001 "John Doe"

# Get key
GET user:1001
# Output: "John Doe"

# Set with expiration (seconds)
SETEX session:abc123 3600 "user_data"

# Set if not exists
SETNX lock:resource "locked"

# Multiple set/get
MSET key1 "value1" key2 "value2"
MGET key1 key2

# Increment/Decrement
SET counter 0
INCR counter  # 1
INCRBY counter 5  # 6
DECR counter  # 5

# Append
APPEND message "Hello"
APPEND message " World"
GET message  # "Hello World"

# Get length
STRLEN message  # 11

# Delete key
DEL user:1001

# Check if key exists
EXISTS user:1001  # 0 (false) or 1 (true)

# Get TTL (time to live)
TTL session:abc123  # Seconds remaining

# Rename key
RENAME old_key new_key
```

---

## Data Structures

### 1. Lists (Ordered Collections)
```redis
# Push to list (left/right)
LPUSH tasks "Task 1"
RPUSH tasks "Task 3"

# Pop from list
LPOP tasks  # Remove and return first
RPOP tasks  # Remove and return last

# Get range
LRANGE tasks 0 -1  # All elements
LRANGE tasks 0 4   # First 5 elements

# Get length
LLEN tasks

# Insert before/after
LINSERT tasks BEFORE "Task 2" "Task 1.5"

# Trim (keep only specified range)
LTRIM tasks 0 99  # Keep first 100 items

# Use Case: Job Queue
LPUSH queue:emails "email1"
LPUSH queue:emails "email2"
BRPOP queue:emails 0  # Blocking pop (wait for item)
```

### 2. Sets (Unique Unordered Collections)
```redis
# Add members
SADD tags:post:1 "python" "redis" "tutorial"

# Get all members
SMEMBERS tags:post:1

# Check membership
SISMEMBER tags:post:1 "python"  # 1 (true)

# Remove member
SREM tags:post:1 "tutorial"

# Get count
SCARD tags:post:1

# Set operations
SADD set1 "a" "b" "c"
SADD set2 "b" "c" "d"

SINTER set1 set2  # Intersection: b, c
SUNION set1 set2  # Union: a, b, c, d
SDIFF set1 set2   # Difference: a

# Random member
SRANDMEMBER tags:post:1

# Use Case: Unique visitors
SADD visitors:2024-01-15 "user1" "user2" "user3"
SCARD visitors:2024-01-15  # Count unique visitors
```

### 3. Sorted Sets (Ordered by Score)
```redis
# Add with score
ZADD leaderboard 9500 "player1"
ZADD leaderboard 8700 "player2"
ZADD leaderboard 10200 "player3"

# Get top 10
ZREVRANGE leaderboard 0 9 WITHSCORES

# Get rank
ZREVRANK leaderboard "player1"  # 1 (2nd place)

# Get score
ZSCORE leaderboard "player1"  # 9500

# Increment score
ZINCRBY leaderboard 100 "player1"

# Get by score range
ZRANGEBYSCORE leaderboard 9000 10000

# Remove
ZREM leaderboard "player2"

# Count
ZCARD leaderboard

# Use Case: Real-time Leaderboard
ZADD game:scores 1500 "alice"
ZADD game:scores 2300 "bob"
ZADD game:scores 1800 "charlie"

# Top 3 players
ZREVRANGE game:scores 0 2 WITHSCORES
```

### 4. Hashes (Field-Value Pairs)
```redis
# Set hash fields
HSET user:1001 name "John Doe"
HSET user:1001 email "john@example.com"
HSET user:1001 age 30

# Set multiple fields
HMSET user:1002 name "Jane" email "jane@example.com" age 25

# Get field
HGET user:1001 name  # "John Doe"

# Get multiple fields
HMGET user:1001 name email

# Get all fields and values
HGETALL user:1001

# Check if field exists
HEXISTS user:1001 email  # 1

# Delete field
HDEL user:1001 age

# Increment field
HINCRBY user:1001 age 1

# Get all keys
HKEYS user:1001

# Get all values
HVALS user:1001

# Use Case: Object Storage
HMSET product:101 name "Laptop" price 999.99 stock 50
HGETALL product:101
```

---

## Advanced Features

### TTL (Time To Live)
```redis
# Set expiration on key
EXPIRE user:session:abc 3600  # Expire in 1 hour

# Set expiration at specific time
EXPIREAT key 1704067200  # Unix timestamp

# Set with expiration
SETEX cache:data 300 "value"  # Expire in 5 minutes

# Remove expiration
PERSIST key

# Check TTL
TTL key  # Seconds remaining
PTTL key  # Milliseconds remaining
```

### Transactions
```redis
MULTI
SET key1 "value1"
SET key2 "value2"
INCR counter
EXEC

# Discard transaction
MULTI
SET key1 "value1"
DISCARD
```

### Pipelining (Batch Commands)
```python
# Python example
import redis

r = redis.Redis()
pipe = r.pipeline()

pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
pipe.get('key1')
pipe.execute()  # Send all at once
```

### Pub/Sub (Messaging)
```redis
# Publisher
PUBLISH news:tech "New iPhone released"

# Subscriber (in another client)
SUBSCRIBE news:tech
# Waits for messages...

# Pattern subscription
PSUBSCRIBE news:*
# Receives from news:tech, news:sports, etc.
```

---

## Caching Patterns

### 1. Cache-Aside
```python
def get_user(user_id):
    # Try cache first
    user = redis.get(f"user:{user_id}")
    
    if user:
        return json.loads(user)
    
    # Cache miss - load from DB
    user = db.get_user(user_id)
    
    # Store in cache
    redis.setex(
        f"user:{user_id}",
        3600,  # 1 hour TTL
        json.dumps(user)
    )
    
    return user
```

### 2. Write-Through
```python
def update_user(user_id, data):
    # Update database
    db.update_user(user_id, data)
    
    # Update cache
    redis.setex(
        f"user:{user_id}",
        3600,
        json.dumps(data)
    )
```

### 3. Cache Invalidation
```python
def delete_user(user_id):
    # Delete from database
    db.delete_user(user_id)
    
    # Invalidate cache
    redis.delete(f"user:{user_id}")
```

---

## Use Case Examples

### Session Storage
```python
# Store session
redis.setex(
    f"session:{session_id}",
    1800,  # 30 minutes
    json.dumps({"user_id": 123, "role": "admin"})
)

# Get session
session_data = redis.get(f"session:{session_id}")
```

### Rate Limiting
```python
def is_rate_limited(user_id, max_requests=100, window=60):
    """Allow max_requests per window (seconds)"""
    key = f"rate_limit:{user_id}"
    
    # Increment counter
    count = redis.incr(key)
    
    # Set expiration on first request
    if count == 1:
        redis.expire(key, window)
    
    return count > max_requests

# Usage
if is_rate_limited(user_id):
    return "Too many requests"
```

### Leaderboard
```python
# Add score
redis.zadd("game:leaderboard", {player_id: score})

# Increment score
redis.zincrby("game:leaderboard", 10, player_id)

# Get top 10
top_players = redis.zrevrange(
    "game:leaderboard",
    0, 9,
    withscores=True
)

# Get player rank
rank = redis.zrevrank("game:leaderboard", player_id)
```

### Distributed Lock
```python
def acquire_lock(lock_key, timeout=10):
    """Acquire distributed lock"""
    lock_id = str(uuid.uuid4())
    
    # SETNX with expiration
    acquired = redis.set(
        lock_key,
        lock_id,
        nx=True,  # Only if not exists
        ex=timeout  # Expiration
    )
    
    return lock_id if acquired else None

def release_lock(lock_key, lock_id):
    """Release lock"""
    # Ensure we own the lock
    if redis.get(lock_key) == lock_id:
        redis.delete(lock_key)
```

### Geospatial Queries
```redis
# Add locations
GEOADD stores -122.4194 37.7749 "store1"
GEOADD stores -118.2437 34.0522 "store2"

# Find nearby (within 10km)
GEORADIUS stores -122.4194 37.7749 10 km WITHDIST

# Distance between two points
GEODIST stores "store1" "store2" km
```

---

## Persistence

### RDB (Snapshots)
```conf
# redis.conf
save 900 1      # Save if 1 key changed in 900 seconds
save 300 10     # Save if 10 keys changed in 300 seconds
save 60 10000   # Save if 10000 keys changed in 60 seconds
```

### AOF (Append-Only File)
```conf
# redis.conf
appendonly yes
appendfsync everysec  # Options: always, everysec, no
```

---

## Redis with Programming Languages

### Python (redis-py)
```python
import redis

# Connect
r = redis.Redis(host='localhost', port=6379, db=0)

# Or with connection pool
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

# Operations
r.set('key', 'value')
value = r.get('key')

# Decode responses automatically
r = redis.Redis(host='localhost', decode_responses=True)
```

### Node.js (ioredis)
```javascript
const Redis = require('ioredis');
const redis = new Redis();

// Set
await redis.set('key', 'value');

// Get
const value = await redis.get('key');

// Pipeline
const pipeline = redis.pipeline();
pipeline.set('key1', 'value1');
pipeline.set('key2', 'value2');
await pipeline.exec();
```

### Java (Jedis)
```java
import redis.clients.jedis.Jedis;

Jedis jedis = new Jedis("localhost", 6379);

// Set
jedis.set("key", "value");

// Get
String value = jedis.get("key");

// Close
jedis.close();
```

---

## Best Practices

✅ Use appropriate data structures (don't store JSON in strings)  
✅ Set TTL on all keys (avoid memory bloat)  
✅ Use pipelining for batch operations  
✅ Monitor memory usage  
✅ Use connection pooling  
✅ Enable persistence for important data  
✅ Use Redis Cluster for high availability  
✅ Avoid large keys (split into smaller ones)  

---

## Monitoring

```redis
# Info
INFO
INFO memory
INFO stats

# Monitor (watch commands in real-time)
MONITOR

# Slow log
SLOWLOG GET 10

# Key scan (don't use KEYS in production!)
SCAN 0 MATCH user:* COUNT 100
```

---

## Resources

### Official
- **redis.io**: Official documentation
- **Redis University**: Free courses

### Tools
- **RedisInsight**: GUI client
- **redis-cli**: Command-line client

---

**💡 Pro Tip**: Use Redis for speed, not as primary database. Always have data backed up in a persistent database!

