# 🚀 Caching in System Design

## Overview
Caching is storing frequently accessed data in fast storage to reduce latency and database load. Essential for scalable systems.

---

## Why Caching?

### Problems Solved
- **Reduce Latency**: ms vs μs response times
- **Reduce Database Load**: 80/20 rule - 20% data = 80% requests
- **Cost Savings**: Fewer database instances needed
- **Better UX**: Faster page loads

### Example Impact
```
Without Cache:
- Database query: 50ms
- 1000 req/s = 50,000ms CPU time

With Cache (90% hit rate):
- 900 cached: 900 × 1ms = 900ms
- 100 from DB: 100 × 50ms = 5,000ms
- Total: 5,900ms (88% reduction!)
```

---

## Cache Hierarchy

```
Client (Browser) → CDN → Server Cache → Database Cache → Database
    ↓                ↓           ↓              ↓
 Fastest         Fast        Faster        Slowest
```

### 1. **Client-Side Caching (Browser)**
```html
<!-- HTTP Headers -->
Cache-Control: max-age=3600, public
ETag: "686897696a7c876b7e"
Last-Modified: Mon, 15 Jan 2024 12:00:00 GMT
```

### 2. **CDN Caching**
- Static assets (images, CSS, JS)
- Geographically distributed
- Edge locations

### 3. **Application Cache (Redis/Memcached)**
- Database query results
- Session data
- API responses

### 4. **Database Cache**
- Query cache
- Buffer pool
- Internal optimization

---

## Caching Strategies

### 1. **Cache-Aside (Lazy Loading)** ⭐ Most Common

```java
public User getUser(int userId) {
    String key = "user:" + userId;
    
    // 1. Try cache first
    User user = cache.get(key);
    
    if (user != null) {
        return user; // Cache hit!
    }
    
    // 2. Cache miss - load from database
    user = database.getUserById(userId);
    
    // 3. Store in cache for next time
    cache.set(key, user, TTL_SECONDS);
    
    return user;
}
```

**✅ Pros:**
- Only cache what's needed
- Resilient to cache failures
- Simple to implement

**❌ Cons:**
- Initial cache miss penalty
- Stale data possible
- Cache warming needed

**Best for:** Read-heavy applications

---

### 2. **Read-Through**

```java
// Cache sits between app and DB
// Cache automatically loads from DB on miss
public User getUser(int userId) {
    return cache.get(userId); // Cache handles DB if miss
}
```

**✅ Pros:**
- Transparent to application
- Automatic cache population

**❌ Cons:**
- Tight coupling
- Cache failure = system failure

---

### 3. **Write-Through**

```java
public void updateUser(User user) {
    // 1. Write to cache
    cache.set("user:" + user.id, user);
    
    // 2. Immediately write to database
    database.update(user);
}
```

**✅ Pros:**
- Cache always consistent
- No data loss
- Reliable

**❌ Cons:**
- Write latency (two writes)
- Unused data cached
- Not suitable for high write loads

**Best for:** Applications needing consistency

---

### 4. **Write-Behind (Write-Back)**

```java
public void updateUser(User user) {
    // 1. Write to cache immediately
    cache.set("user:" + user.id, user);
    
    // 2. Queue for async DB write
    writeQueue.add(() -> database.update(user));
    
    // Returns fast!
}
```

**✅ Pros:**
- Fast writes
- Batch writes possible
- Reduced DB load

**❌ Cons:**
- Data loss risk (if cache crashes)
- Complex implementation
- Eventual consistency

**Best for:** High-write applications (analytics, metrics)

---

### 5. **Write-Around**

```java
public void updateUser(User user) {
    // Write directly to database, bypass cache
    database.update(user);
    
    // Cache will be updated on next read
}
```

**✅ Pros:**
- Avoid cache pollution
- Simple

**❌ Cons:**
- Cache miss on next read
- Stale data temporarily

**Best for:** Infrequently read data

---

### 6. **Refresh-Ahead**

```java
// Proactively refresh hot data before expiry
if (cache.getTTL(key) < REFRESH_THRESHOLD) {
    asyncRefresh(key); // Background refresh
}
```

**✅ Pros:**
- No cache miss for hot data
- Better latency

**❌ Cons:**
- Complexity
- Wasted resources for cold data

**Best for:** Predictable access patterns

---

## Cache Eviction Policies

### 1. **LRU (Least Recently Used)** ⭐ Most Popular

```java
class LRUCache {
    LinkedHashMap<Integer, Integer> cache;
    int capacity;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new LinkedHashMap<>(capacity, 0.75f, true) {
            protected boolean removeEldestEntry(Map.Entry eldest) {
                return size() > capacity;
            }
        };
    }
    
    public int get(int key) {
        return cache.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        cache.put(key, value);
    }
}
```

**Best for:** General-purpose caching

### 2. **LFU (Least Frequently Used)**
- Track access count
- Remove least frequently accessed

**Best for:** Long-term popular content

### 3. **FIFO (First In First Out)**
- Remove oldest entry
- Simple but less effective

### 4. **Random**
- Random eviction
- Simple, unpredictable

### 5. **TTL (Time To Live)**
```java
cache.set("key", value, 3600); // Expire in 1 hour
```

**Best for:** Time-sensitive data

---

## Popular Caching Technologies

### 1. **Redis** ⭐

#### Features
- In-memory key-value store
- Data structures: Strings, Lists, Sets, Hashes, Sorted Sets
- Persistence options (RDB, AOF)
- Pub/Sub messaging
- Lua scripting
- Clustering support

#### Use Cases
- Session storage
- Real-time leaderboards
- Rate limiting
- Job queues
- Geospatial data

#### Example
```java
// Spring Boot + Redis
@Cacheable(value = "users", key = "#userId")
public User getUserById(Long userId) {
    return userRepository.findById(userId);
}

@CacheEvict(value = "users", key = "#user.id")
public void updateUser(User user) {
    userRepository.save(user);
}

@CachePut(value = "users", key = "#result.id")
public User createUser(User user) {
    return userRepository.save(user);
}
```

#### Redis Data Structures
```redis
# String
SET user:1001 "John Doe"
GET user:1001

# Hash (good for objects)
HSET user:1001 name "John" age 30
HGETALL user:1001

# List (queue)
LPUSH queue:jobs "job1"
RPOP queue:jobs

# Set (unique items)
SADD tags:post:1 "java" "spring" "redis"
SMEMBERS tags:post:1

# Sorted Set (leaderboard)
ZADD leaderboard 9500 "player1"
ZREVRANGE leaderboard 0 9 WITHSCORES
```

---

### 2. **Memcached**

#### Features
- Simple key-value store
- Distributed caching
- Multi-threaded
- No persistence
- LRU eviction

#### When to Use
✅ Simple caching needs  
✅ High-throughput  
✅ Multiple servers  
❌ Need persistence  
❌ Complex data structures  

#### Example
```java
MemcachedClient client = new MemcachedClient(
    new InetSocketAddress("localhost", 11211)
);

client.set("user:1001", 3600, userObject);
User user = (User) client.get("user:1001");
```

---

### 3. **CDN (Content Delivery Network)**

#### How It Works
```
User (Tokyo) → CDN Edge (Tokyo) → Origin Server (US)
                    ↓
              Cached content
             (Served instantly!)
```

#### What to Cache
- Images, videos
- CSS, JavaScript files
- Static HTML pages
- Downloadable files

#### Popular CDNs
- **Cloudflare**
- **AWS CloudFront**
- **Akamai**
- **Fastly**

#### Configuration Example
```javascript
// CloudFront cache behavior
{
  "ViewerProtocolPolicy": "redirect-to-https",
  "AllowedMethods": ["GET", "HEAD"],
  "CachedMethods": ["GET", "HEAD"],
  "DefaultTTL": 86400,
  "MaxTTL": 31536000,
  "Compress": true
}
```

---

## Cache Invalidation Strategies

> "There are only two hard things in Computer Science: cache invalidation and naming things." - Phil Karlton

### 1. **TTL-Based (Time To Live)**
```java
cache.set("key", value, 300); // Expires in 5 minutes
```
**✅ Pros:** Simple, automatic  
**❌ Cons:** Might serve stale data

### 2. **Event-Based Invalidation**
```java
public void updateUser(User user) {
    database.update(user);
    cache.delete("user:" + user.id); // Invalidate immediately
}
```
**✅ Pros:** Always fresh  
**❌ Cons:** More complex, cache miss

### 3. **Write-Through**
Update cache and DB together

### 4. **Tag-Based Invalidation**
```java
cache.set("user:1001", user, tags=["users", "premium"]);
cache.invalidateTag("users"); // Invalidate all user caches
```

### 5. **Version-Based**
```java
String key = "user:" + userId + ":v" + version;
// New version = new key, old cache naturally expires
```

---

## Cache Patterns

### 1. **Cache Stampede Prevention**

**Problem:** Cache expires, 1000 requests hit DB simultaneously

**Solution 1: Lock**
```java
public User getUser(int userId) {
    String key = "user:" + userId;
    User user = cache.get(key);
    
    if (user == null) {
        Lock lock = acquireLock("lock:" + key);
        try {
            user = cache.get(key); // Double-check
            if (user == null) {
                user = database.get(userId);
                cache.set(key, user, TTL);
            }
        } finally {
            lock.release();
        }
    }
    return user;
}
```

**Solution 2: Probabilistic Early Expiration**
```java
double delta = randomSeconds();
double expiry = currentTime + TTL - delta;
// Refresh before actual expiry
```

---

### 2. **Distributed Caching**

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│  Cache   │    │  Cache   │    │  Cache   │
│  Node 1  │    │  Node 2  │    │  Node 3  │
└──────────┘    └──────────┘    └──────────┘
      ↑              ↑                ↑
      └──────────────┴────────────────┘
               Consistent Hashing
```

**Benefits:**
- Horizontal scaling
- Fault tolerance
- Larger total memory

---

### 3. **Multi-Level Caching**

```java
public User getUser(int userId) {
    // L1: In-memory cache (fastest)
    User user = localCache.get(userId);
    if (user != null) return user;
    
    // L2: Redis (fast)
    user = redis.get("user:" + userId);
    if (user != null) {
        localCache.set(userId, user);
        return user;
    }
    
    // L3: Database (slowest)
    user = database.get(userId);
    redis.set("user:" + userId, user, TTL);
    localCache.set(userId, user);
    return user;
}
```

---

## Cache Metrics

### Key Metrics to Monitor

1. **Hit Rate**
   ```
   Hit Rate = Cache Hits / Total Requests
   Target: > 80-90%
   ```

2. **Miss Rate**
   ```
   Miss Rate = Cache Misses / Total Requests
   ```

3. **Eviction Rate**
   ```
   How often cache entries are evicted
   High rate = cache too small
   ```

4. **Latency**
   ```
   p50, p95, p99 response times
   ```

5. **Memory Usage**
   ```
   Current usage / Total capacity
   Alert if > 80%
   ```

### Monitoring Example
```java
@Aspect
public class CacheMetrics {
    private final MeterRegistry registry;
    
    @Around("@annotation(Cacheable)")
    public Object measureCache(ProceedingJoinPoint pjp) {
        Timer.Sample sample = Timer.start(registry);
        try {
            Object result = pjp.proceed();
            sample.stop(Timer.builder("cache.get")
                .tag("result", "hit")
                .register(registry));
            return result;
        } catch (Throwable ex) {
            sample.stop(Timer.builder("cache.get")
                .tag("result", "miss")
                .register(registry));
            throw ex;
        }
    }
}
```

---

## Common Caching Pitfalls

### 1. **Cache Stampede**
Multiple requests overwhelm DB when cache expires

**Solution:** Locking, probabilistic expiration

### 2. **Stale Data**
Serving outdated information

**Solution:** Proper TTL, event-based invalidation

### 3. **Cache Penetration**
Queries for non-existent keys bypass cache

**Solution:** Cache null results, bloom filter

### 4. **Cache Avalanche**
Many keys expire simultaneously

**Solution:** Randomized TTL, gradual expiration

### 5. **Hot Key Problem**
Single key gets too many requests

**Solution:** Replication, local caching

---

## Interview Questions

1. **What is caching and why is it important?**
2. **Explain cache-aside vs write-through strategies**
3. **How would you handle cache invalidation?**
4. **What is cache stampede and how to prevent it?**
5. **Redis vs Memcached: when to use each?**
6. **How do you measure cache effectiveness?**
7. **Design a caching strategy for read-heavy vs write-heavy systems**

---

## Best Practices

✅ Set appropriate TTL based on data freshness requirements  
✅ Monitor cache hit rate (target 80-90%)  
✅ Use consistent key naming conventions  
✅ Implement cache warming for critical data  
✅ Handle cache failures gracefully (fallback to DB)  
✅ Use tags for batch invalidation  
✅ Compress large cached objects  
✅ Consider security (don't cache sensitive data)  

---

## Real-World Examples

### Facebook
- **TAO (The Associations and Objects)**: Distributed cache for social graph
- Caches friendships, likes, comments

### Netflix
- **EVCache**: Distributed caching (Memcached + custom layer)
- Caches user preferences, viewing history, metadata

### Twitter
- **Manhattan**: Distributed key-value store
- Caches timelines, tweets, user data

---

## Next Steps

- **Microservices** → [05-microservices](../05-microservices/README.md)
- **Real-World Systems** → [06-real-world-systems](../06-real-world-systems/README.md)
- **Case Studies** → [case-studies](../case-studies/README.md)

---

**💡 Pro Tip**: Start with simple cache-aside pattern. Optimize only when needed based on actual metrics!

