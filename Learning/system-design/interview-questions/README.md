# 💼 System Design Interview Questions

## Overview
Comprehensive collection of system design interview questions with structured approaches and key concepts to discuss.

---

## How to Approach System Design Interviews

### 1. **Clarify Requirements (5 min)**
Ask questions to understand the scope:

```
❓ Who are the users? (general public, internal, B2B)
❓ How many users? (100s, millions, billions)
❓ What are the main features?
❓ What's the expected traffic? (requests/sec)
❓ What's the expected data size? (GB, TB, PB)
❓ What's the read:write ratio?
❓ What are the latency requirements?
❓ What are the availability requirements? (99.9%, 99.99%)
```

### 2. **High-Level Design (10 min)**
```
┌─────────┐
│ Client  │
└────┬────┘
     ↓
┌────┴─────────┐
│Load Balancer │
└────┬─────────┘
     ↓
┌────┴────┐  ┌──────────┐
│App Server│  │  Cache   │
└────┬────┘  └──────────┘
     ↓
┌────┴────┐
│Database │
└─────────┘
```

### 3. **Deep Dive (15-20 min)**
- API design
- Database schema
- Scaling strategies
- Trade-offs

### 4. **Wrap Up (5 min)**
- Bottlenecks
- Monitoring
- Future improvements

---

## Question Categories

---

## 🔵 Social Media & Content

### 1. Design Twitter

**Requirements:**
- Post tweets (280 chars)
- Follow/unfollow users
- View timeline (feed)
- Search tweets

**Key Components:**
```
User → API Gateway → Tweet Service → Cassandra
                   → Timeline Service → Redis (cache)
                   → Search Service → Elasticsearch
```

**Database Schema:**
```sql
users: user_id, username, email, created_at
tweets: tweet_id, user_id, content, created_at
follows: follower_id, followee_id
```

**Key Discussions:**
- **Fanout on Write** vs **Fanout on Read**
- Timeline generation for celebrities
- Caching strategy
- Sharding by user_id
- Real-time vs eventual consistency

**Capacity Estimation:**
```
300M users, 50M DAU
100M tweets/day = 1,157 tweets/sec
Each tweet ~1KB → 100GB/day storage
```

---

### 2. Design Instagram

**Requirements:**
- Upload photos
- Follow users
- View feed (photos from followed users)
- Like/comment

**Key Components:**
```
Upload → API → AWS S3 (storage)
              → Resize Service → Multiple sizes
              → CDN (CloudFront)
              
Feed → Redis cache → Pre-computed timelines
```

**Database Design:**
```sql
users: user_id, username, profile_pic
photos: photo_id, user_id, caption, s3_url, created_at
likes: user_id, photo_id
follows: follower_id, followee_id
```

**Key Discussions:**
- Photo storage (S3 vs CDN)
- Feed generation algorithm
- Ranking (chronological vs ML-based)
- Image CDN and optimization
- Database sharding strategy

---

### 3. Design Facebook Messenger / WhatsApp

**Requirements:**
- 1-on-1 messaging
- Group chats
- Online status
- Message history
- Read receipts

**Key Components:**
```
User → WebSocket Server → Message Queue → Recipient
                        → Cassandra (history)
                        → Redis (online status)
```

**Message Flow:**
```
1. Sender connects via WebSocket
2. Send message to server
3. Server stores in Cassandra
4. If recipient online: deliver immediately
5. If recipient offline: queue message
6. Send read receipt back
```

**Key Discussions:**
- WebSocket vs Long Polling vs SSE
- Message ordering and delivery guarantees
- Offline message storage
- Group chat scalability
- End-to-end encryption
- Presence (online status)

---

### 4. Design YouTube / Netflix

**Requirements:**
- Upload videos
- Watch videos
- Search videos
- Recommendations

**Key Components:**
```
Upload → Transcoding Service → Multiple formats
                            → Blob Storage (S3)
                            → CDN
                            
Watch → CDN → Adaptive Bitrate Streaming (HLS/DASH)
```

**Video Processing:**
```
Raw Upload:
  ├─ 4K (H.264, VP9, AV1)
  ├─ 1080p
  ├─ 720p
  ├─ 480p
  └─ 360p
  
= 15-20 versions per video
```

**Key Discussions:**
- Video transcoding pipeline
- Adaptive bitrate streaming
- CDN strategy (edge caching)
- Recommendation algorithm
- Copyright detection
- Live streaming vs VOD

---

## 🔵 E-Commerce & Marketplace

### 5. Design Amazon / E-Commerce Platform

**Requirements:**
- Product catalog
- Search products
- Shopping cart
- Checkout and payment
- Order tracking

**Microservices:**
```
┌────────────┐  ┌────────────┐  ┌────────────┐
│  Product   │  │    Cart    │  │   Order    │
│  Service   │  │  Service   │  │  Service   │
└────────────┘  └────────────┘  └────────────┘
     ↓               ↓               ↓
  PostgreSQL      Redis         PostgreSQL
```

**Key Discussions:**
- Product catalog (Elasticsearch for search)
- Inventory management (race conditions)
- Payment processing (Stripe, idempotency)
- Order fulfillment workflow
- Distributed transactions (Saga pattern)
- Flash sales (high concurrency)

---

### 6. Design Uber / Ride-Sharing

**Requirements:**
- Match riders with drivers
- Real-time tracking
- ETA calculation
- Pricing

**Key Components:**
```
Location Updates → Redis (GEOADD)
Dispatch → Matching Algorithm
         → WebSocket (real-time updates)
```

**Geospatial Indexing:**
```redis
GEOADD drivers longitude latitude driver_id
GEORADIUS rider_lat rider_lng 5 km
```

**Key Discussions:**
- Real-time location tracking (WebSocket)
- Geospatial indexing (Redis, PostGIS)
- Dispatch algorithm (matching)
- ETA calculation (routing API)
- Surge pricing
- Driver-rider communication

---

### 7. Design Airbnb / Hotel Booking

**Requirements:**
- Search listings (location, dates, price)
- View availability
- Book property
- Reviews and ratings

**Search Architecture:**
```
User Search → Elasticsearch
  Filters: location, dates, price, amenities
  
  Query:
    - Geospatial (within 10km)
    - Date range (check availability)
    - Price range
    - Guest count
```

**Booking Flow:**
```
1. Check availability (Redis cache)
2. Distributed lock (prevent double booking)
3. Create reservation (PostgreSQL)
4. Process payment (Stripe)
5. Send confirmation (Email service)
```

**Key Discussions:**
- Geospatial search (Elasticsearch, PostGIS)
- Availability calendar (precomputed, Redis cache)
- Preventing double bookings (distributed locks)
- Payment processing
- Dynamic pricing
- Reviews and ranking algorithm

---

## 🔵 Productivity & Collaboration

### 8. Design Google Docs / Collaborative Editor

**Requirements:**
- Real-time editing
- Multiple users editing simultaneously
- Version history
- Offline support

**Key Components:**
```
WebSocket → Operational Transform (OT) / CRDT
         → Conflict resolution
         → Save to database
```

**Conflict Resolution:**
```
User A: "Hello" → "Hello World" (adds " World")
User B: "Hello" → "Hi" (replaces with "Hi")

Server merges:
  Option 1 (OT): Transform operations
  Option 2 (CRDT): Conflict-free replicated data type
  
Result: "Hi World"
```

**Key Discussions:**
- Operational Transform vs CRDT
- WebSocket for real-time sync
- Conflict resolution
- Version history (Git-like)
- Offline editing (sync on reconnect)

---

### 9. Design Dropbox / Google Drive

**Requirements:**
- Upload/download files
- Sync across devices
- Share files
- Version control

**Architecture:**
```
Client → Upload → Chunking (4MB blocks)
                → Deduplication (hash-based)
                → S3 Storage
                → Metadata DB (PostgreSQL)
```

**Sync Algorithm:**
```
1. Client watches file changes
2. Calculate file hash (SHA-256)
3. Check if hash exists (deduplication)
4. Upload only changed blocks
5. Update metadata
6. Notify other clients (WebSocket/Long Polling)
7. Other clients download changes
```

**Key Discussions:**
- File chunking and deduplication
- Delta sync (only upload changes)
- Conflict resolution (last-write-wins vs merge)
- Storage optimization
- Sharing and permissions

---

### 10. Design Slack / Chat Application

**Requirements:**
- Channels (group chats)
- Direct messages
- File sharing
- Search messages

**Architecture:**
```
WebSocket Server → Message Queue (Kafka)
                → Elasticsearch (search)
                → Cassandra (history)
                → Redis (online status, typing indicators)
```

**Key Discussions:**
- WebSocket for real-time
- Message ordering in channels
- Presence (online status)
- Typing indicators
- Search (Elasticsearch)
- Notifications

---

## 🔵 Infrastructure & Utilities

### 11. Design URL Shortener (bit.ly)

**Requirements:**
- Shorten long URLs
- Redirect to original URL
- Analytics (click count)

**Key Design:**
```
Long URL → Hash (MD5/SHA-256) → Take first 7 chars → Short URL
Or: Auto-increment counter → Base62 encode → Short URL

Example:
  Counter: 12345
  Base62: "dnh"
  Short URL: "bit.ly/dnh"
```

**Database Schema:**
```sql
urls: short_code, long_url, created_at, user_id
clicks: short_code, timestamp, user_agent, ip
```

**Key Discussions:**
- URL generation (hash vs counter)
- Collision handling
- Redirection (302 vs 301)
- Analytics and tracking
- Rate limiting
- Custom short URLs

---

### 12. Design Rate Limiter

**Requirements:**
- Limit requests per user/IP
- Different limits for different endpoints
- Distributed system

**Algorithms:**

**1. Token Bucket**
```python
class TokenBucket:
    def allow_request(self, user_id):
        tokens = redis.get(f"tokens:{user_id}")
        if tokens >= 1:
            redis.decr(f"tokens:{user_id}")
            return True
        return False
    
    def refill():
        # Add tokens every second
        redis.incr(f"tokens:{user_id}", rate)
```

**2. Sliding Window Log**
```python
def allow_request(user_id):
    now = time.time()
    key = f"requests:{user_id}"
    
    # Remove old requests
    redis.zremrangebyscore(key, 0, now - window)
    
    # Count recent requests
    count = redis.zcard(key)
    
    if count < limit:
        redis.zadd(key, {now: now})
        return True
    return False
```

**Key Discussions:**
- Token bucket vs Fixed window vs Sliding window
- Redis vs in-memory
- Distributed rate limiting
- Different limits per user tier
- Response headers (X-Rate-Limit-Remaining)

---

### 13. Design Web Crawler

**Requirements:**
- Crawl billions of web pages
- Handle robots.txt
- Avoid duplicates
- Distributed system

**Architecture:**
```
URL Frontier (Queue) → Crawler Workers → HTML Parser
                                      → Link Extractor
                                      → Deduplication (Bloom Filter)
                                      → Storage (S3 + Metadata DB)
```

**Components:**
```
1. URL Frontier: Priority queue (important sites first)
2. DNS Resolver: Cache DNS lookups
3. Fetcher: Download HTML (HTTP client pool)
4. Parser: Extract text, links
5. Deduplicator: Check URL hash (Bloom filter)
6. Storage: S3 for HTML, DB for metadata
```

**Key Discussions:**
- Politeness (respect robots.txt, rate limit per domain)
- URL deduplication (Bloom filter)
- Priority crawling (PageRank)
- Distributed crawling (partition by domain)
- Handling failures and retries

---

### 14. Design Notification System

**Requirements:**
- Send email, SMS, push notifications
- Handle millions of notifications
- Retry failed notifications
- Priority notifications

**Architecture:**
```
Service → API Gateway → Notification Service → Message Queue (Kafka)
                                                      ↓
                                          ┌───────────┴───────────┐
                                          ↓           ↓           ↓
                                      Email       SMS         Push
                                    (SendGrid) (Twilio)   (Firebase)
```

**Key Discussions:**
- Multiple channels (email, SMS, push)
- Template management
- User preferences (opt-out)
- Rate limiting (avoid spam)
- Retry logic (exponential backoff)
- Priority queue (urgent vs normal)
- Analytics (delivery rates)

---

## 🔵 Search & Discovery

### 15. Design Search Autocomplete / Typeahead

**Requirements:**
- Suggest completions as user types
- Fast (<100ms)
- Relevant suggestions
- Scale to millions of queries

**Architecture:**
```
User types → API Gateway → Autocomplete Service → Trie data structure
                                                → Redis cache
```

**Trie Structure:**
```
       root
      /  |  \
     c   d   e
    /    |    \
   a     o     m
  /      |      \
 t       g      a
                 \
                  i
                   \
                    l
```

**Key Discussions:**
- Trie data structure
- Caching popular queries (Redis)
- Ranking (popularity, recency, personalization)
- Prefix matching
- Fuzzy matching (typos)
- Scale (sharding by first letter)

---

## 🔵 Analytics & Monitoring

### 16. Design Analytics System (Google Analytics)

**Requirements:**
- Track page views, clicks, events
- Real-time and batch analytics
- Dashboards and reports

**Architecture:**
```
Website → Tracking Pixel/JS → API Gateway → Kafka
                                                ↓
                                    ┌───────────┴───────────┐
                                    ↓                       ↓
                            Real-time Processing      Batch Processing
                            (Spark Streaming)         (Hadoop/Spark)
                                    ↓                       ↓
                                ElasticSearch           Data Warehouse
                                                        (Redshift)
```

**Key Discussions:**
- Data ingestion (Kafka)
- Stream processing (Spark) vs Batch (Hadoop)
- Data warehousing (Redshift, BigQuery)
- Hot vs cold data
- Aggregation and rollups
- Visualization (Grafana)

---

## 🔵 Infrastructure

### 17. Design Distributed Cache

**Requirements:**
- Store key-value pairs
- Fast reads/writes (<1ms)
- Distributed across servers
- Handle failures

**Architecture:**
```
┌────────┐  ┌────────┐  ┌────────┐
│Cache   │  │Cache   │  │Cache   │
│Node 1  │  │Node 2  │  │Node 3  │
└────────┘  └────────┘  └────────┘
     ↑           ↑           ↑
     └───────────┴───────────┘
        Consistent Hashing
```

**Consistent Hashing:**
```
hash(key) % num_servers → Server ID
Problem: Adding/removing servers rehashes all keys

Solution: Consistent hashing ring
- Keys and servers on ring
- Key → clockwise to next server
- Adding server: only nearby keys affected
```

**Key Discussions:**
- Consistent hashing (minimize rehashing)
- Replication (for fault tolerance)
- Eviction policies (LRU, LFU)
- Cache invalidation
- Monitoring (hit rate, latency)

---

## Interview Template

Use this template for any system design question:

```markdown
## 1. Requirements (Functional & Non-Functional)
Functional: What features?
Non-Functional: Scale, latency, availability

## 2. Capacity Estimation
Users, Traffic, Storage, Bandwidth

## 3. API Design
POST /api/resource
GET /api/resource/{id}

## 4. Database Design
Schema, Indexes, Sharding

## 5. High-Level Design
Draw components and data flow

## 6. Deep Dive
- Scaling strategies
- Caching
- Bottlenecks
- Trade-offs

## 7. Additional Considerations
- Monitoring
- Security
- Future improvements
```

---

## Common Pitfalls to Avoid

❌ Jumping into details without clarifying requirements  
❌ Not discussing trade-offs  
❌ Over-engineering (YAGNI - You Aren't Gonna Need It)  
❌ Not considering failures and edge cases  
❌ Ignoring non-functional requirements  
❌ Not doing capacity estimation  
❌ Being too generic (use specific technologies)  

---

## Resources

### Books
- **"Designing Data-Intensive Applications"** by Martin Kleppmann
- **"System Design Interview"** by Alex Xu

### Websites
- **ByteByteGo**: System design explanations
- **Educative.io**: Grokking the System Design Interview
- **LeetCode Premium**: System design questions

### YouTube Channels
- **Gaurav Sen**
- **Tech Dummies**
- **System Design Interview**

---

## Next Steps

- Practice with mock interviews (Pramp, Interviewing.io)
- Study real system architectures (company engineering blogs)
- Build projects to apply concepts

---

**💡 Pro Tip**: There's no single "correct" answer in system design. Show your thought process, discuss trade-offs, and be ready to adapt based on requirements!

