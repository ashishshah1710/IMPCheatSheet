# 🌍 Real-World System Designs

**Phase 6: Practice with Popular Systems (2-3 Weeks)**

---

## 📖 Overview

Learn how to design real-world systems from scratch. Practice with systems asked in actual interviews.

---

## 🎯 System Design Template

### 1. Requirements Clarification (5 min)

**Functional Requirements:**
- What features are needed?
- What are the core use cases?
- What is out of scope?

**Non-Functional Requirements:**
- Scale (users, requests, storage)
- Performance (latency, throughput)
- Availability requirements
- Consistency requirements

### 2. Capacity Estimation (5 min)

**Calculate:**
- Total users
- Daily active users (DAU)
- Requests per second (RPS)
- Storage requirements
- Bandwidth requirements

### 3. API Design (5 min)

**Define Core APIs:**
```
POST /users
GET /users/{userId}
POST /posts
GET /feed
```

### 4. High-Level Design (10 min)

**Draw Components:**
- Clients
- Load Balancer
- Application Servers
- Cache
- Database
- Message Queue
- Storage

### 5. Database Schema (10 min)

**Design Tables:**
```sql
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP
);
```

### 6. Deep Dive (15 min)

**Discuss:**
- Specific components
- Algorithms
- Data flow
- Edge cases

### 7. Trade-offs (5 min)

**Consider:**
- Alternative approaches
- Pros and cons
- Why chose this solution

---

## 🚀 Design: URL Shortener (bit.ly)

### Requirements

**Functional:**
- Shorten long URL to short URL
- Redirect short URL to original URL
- Custom short URLs (optional)
- Analytics (optional)

**Non-Functional:**
- 100M URLs per month
- Low latency (<100ms)
- High availability (99.99%)
- URL lifetime: 5 years

### Capacity Estimation

```
Write (Shorten URL):
- 100M URLs/month
- 100M / (30 days × 24 hours × 3600s) ≈ 40 URLs/second

Read (Redirect):
- Read:Write ratio = 100:1
- 40 × 100 = 4000 reads/second

Storage:
- 100M URLs/month × 12 months × 5 years = 6B URLs
- Each URL: 500 bytes (URL + metadata)
- 6B × 500 bytes = 3 TB

Bandwidth:
- Write: 40 URLs/s × 500 bytes = 20 KB/s
- Read: 4000 URLs/s × 500 bytes = 2 MB/s
```

### API Design

```
POST /shorten
Request: { "longUrl": "https://example.com/very/long/url" }
Response: { "shortUrl": "https://short.ly/abc123" }

GET /{shortCode}
Response: 302 Redirect to original URL
```

### High-Level Design

```
┌──────────┐
│  Client  │
└────┬─────┘
     │
┌────▼───────────┐
│ Load Balancer  │
└────┬───────────┘
     │
┌────▼───────────┐
│  Web Servers   │
└────┬───────────┘
     │
┌────▼──────┬────▼────────┐
│   Cache   │  Database   │
└───────────┴─────────────┘
```

### Database Schema

```sql
CREATE TABLE urls (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    long_url TEXT NOT NULL,
    user_id BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    INDEX idx_short_code (short_code)
);

CREATE TABLE analytics (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    short_code VARCHAR(10),
    accessed_at TIMESTAMP,
    ip_address VARCHAR(45),
    user_agent TEXT,
    INDEX idx_short_code (short_code)
);
```

### URL Encoding Algorithm

**Base62 Encoding:**
```
Characters: [a-z, A-Z, 0-9] = 62 characters

Length 7: 62^7 = 3.5 trillion URLs
```

**Approaches:**

**1. Hash-based:**
```java
public String encodeUrl(String longUrl) {
    String hash = MD5(longUrl);
    String shortCode = base62Encode(hash.substring(0, 7));
    // Handle collisions
    return shortCode;
}
```

**2. Counter-based:**
```java
public String encodeUrl(long id) {
    return base62Encode(id);
}

private String base62Encode(long id) {
    String chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    StringBuilder sb = new StringBuilder();
    
    while (id > 0) {
        sb.append(chars.charAt((int)(id % 62)));
        id /= 62;
    }
    
    return sb.reverse().toString();
}
```

### Caching Strategy

```
Cache: Redis
- Cache short_code → long_url mapping
- LRU eviction policy
- TTL: 24 hours
- Cache hit rate: 80%+
```

### Scaling

**Database Sharding:**
```
Shard key: hash(short_code) % number_of_shards
Shard 1: short_codes 0-25%
Shard 2: short_codes 26-50%
Shard 3: short_codes 51-75%
Shard 4: short_codes 76-100%
```

---

## 🐦 Design: Twitter

### Requirements

**Functional:**
- Post tweets (280 characters)
- Follow users
- View timeline (tweets from followed users)
- Like, retweet

**Non-Functional:**
- 200M daily active users
- 400M tweets per day
- Timeline latency < 200ms
- Highly available

### Capacity Estimation

```
Users:
- 200M DAU
- Each user: 5 tweets/day average
- Write: 400M tweets/day ≈ 4600 tweets/second

Timeline:
- 200M users × 20 timeline views/day = 4B views/day
- Read: ≈ 46,000 requests/second

Storage:
- Tweet: 280 chars + metadata ≈ 500 bytes
- 400M tweets/day × 500 bytes ≈ 200 GB/day
- Annual: 200 GB × 365 ≈ 73 TB/year
```

### High-Level Design

```
┌──────────┐
│  Client  │
└────┬─────┘
     │
┌────▼──────────┐
│  API Gateway  │
└────┬──────────┘
     │
┌────▼───────┬─────────┬──────────┐
│Tweet Service│Timeline │ User     │
│             │Service  │ Service  │
└──┬──────────┴────┬────┴─────┬────┘
   │               │          │
┌──▼────┐    ┌────▼───┐  ┌───▼────┐
│ Tweet │    │Timeline│  │ User   │
│  DB   │    │ Cache  │  │   DB   │
└───────┘    └────────┘  └────────┘
```

### Database Schema

```sql
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100),
    bio TEXT,
    created_at TIMESTAMP
);

CREATE TABLE tweets (
    tweet_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    content TEXT,
    created_at TIMESTAMP,
    likes_count INT DEFAULT 0,
    retweets_count INT DEFAULT 0,
    INDEX idx_user_created (user_id, created_at)
);

CREATE TABLE follows (
    follower_id BIGINT,
    followee_id BIGINT,
    created_at TIMESTAMP,
    PRIMARY KEY (follower_id, followee_id)
);

CREATE TABLE timeline (
    user_id BIGINT,
    tweet_id BIGINT,
    created_at TIMESTAMP,
    PRIMARY KEY (user_id, tweet_id)
);
```

### Timeline Generation

**Approach 1: Fan-out on Write (Push)**
```
When user tweets:
1. Get all followers
2. Insert tweet into each follower's timeline cache
3. Expensive for celebrities (millions of followers)

Pros: Fast reads
Cons: Slow writes for popular users
```

**Approach 2: Fan-out on Read (Pull)**
```
When user requests timeline:
1. Get all users they follow
2. Fetch recent tweets from each
3. Merge and sort

Pros: Fast writes
Cons: Slow reads
```

**Hybrid Approach (Twitter's Solution):**
```
Regular users: Fan-out on write
Celebrities: Fan-out on read
At read time: Merge both timelines
```

### Scaling Strategies

**Database Sharding:**
```
Tweets: Shard by tweet_id
Users: Shard by user_id
Timeline: Shard by user_id
```

**Caching:**
```
User Cache: Profile data
Timeline Cache: Pre-computed timelines
Tweet Cache: Recent tweets
```

---

## 🎯 More System Designs

### Design WhatsApp/Chat System
- Real-time messaging
- WebSocket connections
- Message delivery
- Read receipts
- Group chat

### Design YouTube
- Video upload and processing
- Video streaming
- CDN delivery
- Recommendations
- View analytics

### Design Uber
- Real-time location tracking
- Driver matching
- ETA calculation
- Pricing
- Payment processing

### Design Instagram
- Photo upload
- Image processing
- Feed generation
- Stories
- Direct messaging

---

## ✅ Practice Checklist

- [ ] Design 3 easy systems
- [ ] Design 5 medium systems
- [ ] Design 2 hard systems
- [ ] Practice timing (45 min each)
- [ ] Draw diagrams
- [ ] Calculate capacity
- [ ] Discuss trade-offs
- [ ] Mock interviews

---

**👉 Next:** [Interview Questions →](../interview-questions/README.md)

---

**💡 Pro Tip:** Practice drawing architectures by hand. In interviews, you'll be whiteboarding!

