# 📚 System Design Case Studies

## Overview
Real-world system design examples from top tech companies. Learn how they solved scalability, availability, and performance challenges.

---

## Case Study 1: Twitter

### System Overview
- **Users**: 330M+ monthly active users
- **Scale**: 6,000 tweets/sec average, 140,000+ tweets/sec peak
- **Challenge**: Real-time timeline generation

### Architecture

```
User tweets → Fanout Service → Redis Timeline Cache
                                      ↓
                               Followers' timelines
```

### Key Design Decisions

#### 1. **Timeline Generation (Fanout)**

**Approach 1: Fanout on Write** (Used for most users)
```
When @user tweets:
  For each follower:
    Add tweet to follower's timeline cache
```
**✅ Pros:** Fast reads (pre-computed)  
**❌ Cons:** Slow writes for celebrities (millions of followers)

**Approach 2: Fanout on Read** (Used for celebrities)
```
When user views timeline:
  Fetch followed users' tweets
  Merge and sort
```
**✅ Pros:** Fast writes  
**❌ Cons:** Slow reads

**Hybrid Solution:**
```
Regular users: Fanout on Write
Celebrities (>1M followers): Fanout on Read
User timeline: Merge both approaches
```

#### 2. **Technology Stack**
- **Timeline Storage**: Redis (in-memory cache)
- **Tweet Storage**: Manhattan (distributed database)
- **Search**: Elasticsearch
- **Social Graph**: FlockDB
- **Message Queue**: Kafka

#### 3. **Caching Strategy**
```
Timeline Cache (Redis):
  - Key: user_id
  - Value: List of tweet IDs (sorted by time)
  - TTL: Infinite for active users
  - Eviction: LRU for inactive users
```

---

## Case Study 2: Instagram

### System Overview
- **Users**: 2B+ monthly active users
- **Scale**: 95M photos/day
- **Challenge**: Photo storage and delivery

### Architecture

```
Upload → API Gateway → Web Servers → Cassandra (metadata)
                            ↓
                    AWS S3 (photo storage)
                            ↓
                    CloudFront CDN (delivery)
```

### Key Design Decisions

#### 1. **Photo Storage**
```
Original Photo → S3 (original size)
              → Lambda (resize)
              → S3 (multiple sizes: thumbnail, medium, large)
```

#### 2. **Photo ID Generation**
```
41 bits: Timestamp (milliseconds)
13 bits: Shard ID
10 bits: Sequence number

= 64-bit unique ID
```

#### 3. **Feed Generation**
```
Option 1: Pull Model (Used initially)
  User requests feed → Fetch recent posts from followed users → Rank → Display

Option 2: Push Model (Current)
  New post → Fanout to followers' feed cache → User fetches from cache
```

#### 4. **Database Sharding**
```
User data: Sharded by user_id
Photo data: Sharded by photo_id
Using consistent hashing
```

#### 5. **Technology Stack**
- **App Servers**: Django (Python)
- **Caching**: Memcached, Redis
- **Database**: PostgreSQL (users), Cassandra (photos/feeds)
- **Storage**: AWS S3
- **CDN**: CloudFront
- **Message Queue**: RabbitMQ

---

## Case Study 3: Netflix

### System Overview
- **Users**: 230M+ subscribers
- **Scale**: 1B+ hours watched/week
- **Challenge**: Video streaming at scale

### Architecture

```
User → API Gateway → Microservices → Cassandra/MySQL
                          ↓
                      Content CDN (AWS CloudFront + Open Connect)
```

### Key Design Decisions

#### 1. **Content Delivery**
```
Video Encoding:
  Original → Multiple formats (H.264, VP9, AV1)
          → Multiple qualities (4K, 1080p, 720p, 480p)
          → Multiple bitrates (adaptive streaming)

Result: 1,200+ versions per title!
```

#### 2. **Open Connect CDN**
```
Netflix's custom CDN:
  - Edge servers in ISP data centers
  - Pre-populates popular content during off-peak
  - Serves 95%+ of traffic from within ISP networks
```

#### 3. **Recommendation System**
```
User Activity → Kafka → Spark (real-time processing)
                             ↓
                     ML Models (collaborative filtering)
                             ↓
                     Personalized recommendations
```

#### 4. **Chaos Engineering**
```
Chaos Monkey: Randomly terminates instances
Chaos Kong: Simulates entire AWS region failure
Goal: Build resilient systems
```

#### 5. **Technology Stack**
- **Microservices**: 1000+ services
- **Database**: Cassandra (viewing history), MySQL (billing)
- **Caching**: EVCache (Memcached-based)
- **Stream Processing**: Kafka + Spark
- **Infrastructure**: AWS
- **API Gateway**: Zuul

---

## Case Study 4: Uber

### System Overview
- **Users**: 110M+ monthly active users
- **Scale**: 15M+ trips/day
- **Challenge**: Real-time matching and routing

### Architecture

```
Rider/Driver App → API Gateway → Microservices
                                      ↓
                              ┌───────┴────────┐
                              ↓                ↓
                         Dispatch         Routing
                        (Matching)       (Navigation)
```

### Key Design Decisions

#### 1. **Real-Time Location Tracking**
```
Driver Location Updates:
  Every 4 seconds → Kafka → Redis (geospatial index)
                            ↓
                     GEOADD drivers lat lng driver_id
                     GEORADIUS user_lat user_lng 5km
```

#### 2. **Dispatch System (Matching)**
```
Rider requests ride:
  1. Find nearby drivers (Redis GEORADIUS)
  2. Calculate ETA for each driver
  3. Match based on:
     - Distance
     - Destination
     - Driver rating
     - Rider rating
  4. Send request to best driver
  5. If declined, try next driver
```

#### 3. **Ringpop (Distributed Hash Ring)**
```
Consistent hashing for:
  - Request routing
  - Stateful services
  - Load balancing

Driver in region A → Always routes to Server A
(Maintains WebSocket connection)
```

#### 4. **Database Design**
```
Trips: Sharded by city (geographic partitioning)
  - Most queries are city-specific
  - Cross-city queries rare

Users: Sharded by user_id
Drivers: Sharded by driver_id
```

#### 5. **Technology Stack**
- **Backend**: Node.js, Go, Java
- **Databases**: PostgreSQL, MySQL, Cassandra
- **Caching**: Redis
- **Message Queue**: Kafka
- **Real-time**: WebSockets
- **Maps**: Google Maps API + custom routing

---

## Case Study 5: WhatsApp

### System Overview
- **Users**: 2B+ users
- **Scale**: 100B+ messages/day
- **Challenge**: Real-time messaging at scale

### Architecture

```
User → WhatsApp Server → Erlang (concurrent connections)
                              ↓
                        Message Queue (Mnesia)
                              ↓
                        Recipient's Device
```

### Key Design Decisions

#### 1. **Erlang for Concurrency**
```
Why Erlang?
  - Lightweight processes (2.6M connections per server!)
  - Built for telecom (high availability)
  - Hot code swapping (no downtime)
  - Actor model (message passing)
```

#### 2. **Message Delivery**
```
Online Recipient:
  Sender → Server → Recipient (immediate delivery)
  
Offline Recipient:
  Sender → Server → Queue (Mnesia database)
  When recipient online → Deliver queued messages
  After delivery → Delete from queue
```

#### 3. **End-to-End Encryption**
```
Message flow:
  1. Sender encrypts with recipient's public key
  2. Server routes encrypted message (can't read it)
  3. Recipient decrypts with private key
```

#### 4. **Minimal Data Storage**
```
WhatsApp stores:
  ✅ User phone numbers
  ✅ Queued messages (until delivered)
  ❌ Message history (deleted after delivery)
  ❌ User metadata
```

#### 5. **Technology Stack**
- **Backend**: Erlang
- **Database**: Mnesia (distributed Erlang DB)
- **Media Storage**: AWS S3
- **Infrastructure**: FreeBSD, custom hardware

---

## Case Study 6: YouTube

### System Overview
- **Users**: 2.5B+ users
- **Scale**: 720,000 hours uploaded/day, 1B hours watched/day
- **Challenge**: Video storage, processing, and delivery

### Architecture

```
Upload → Transcoding Service → Multiple formats/qualities
                                    ↓
                              Google CDN (Blob Storage)
                                    ↓
                              Adaptive Streaming
```

### Key Design Decisions

#### 1. **Video Processing Pipeline**
```
Raw Upload (1080p):
  ├─ 4K HDR
  ├─ 1080p
  ├─ 720p
  ├─ 480p
  ├─ 360p
  └─ 144p
  
Each in multiple codecs: H.264, VP9, AV1
Total: 20-30 versions per video!
```

#### 2. **Recommendation Algorithm**
```
Factors:
  1. Click-through rate (CTR)
  2. Watch time (more important than views)
  3. User engagement (likes, shares)
  4. Video freshness
  5. Upload frequency
  6. Viewer history
```

#### 3. **Live Streaming**
```
Streamer → RTMP → YouTube Servers → HLS/DASH → Viewers
                        ↓
                  (10-30 second delay)
```

#### 4. **Copyright Detection (Content ID)**
```
Uploaded Video → Audio/Video fingerprinting
                      ↓
              Compare with 100M+ reference files
                      ↓
              If match → Apply copyright policy
```

#### 5. **Technology Stack**
- **Backend**: Python, C++, Java
- **Database**: Vitess (MySQL sharding), Bigtable
- **CDN**: Google's global CDN
- **ML**: TensorFlow (recommendations)
- **Infrastructure**: Google Cloud Platform

---

## Case Study 7: Airbnb

### System Overview
- **Listings**: 7M+
- **Scale**: 900M+ bookings to date
- **Challenge**: Search, availability, and booking

### Key Design Decisions

#### 1. **Search System**
```
User Search → Elasticsearch
  Filters:
    - Location (geospatial query)
    - Price range
    - Dates (availability)
    - Amenities
    - Guest count
  
  Ranking:
    - Relevance score
    - Host quality
    - Guest reviews
    - Booking history
```

#### 2. **Availability Calendar**
```
Listing availability:
  - Redis: Fast lookups (cache)
  - MySQL: Source of truth
  - Pre-compute availability for next 365 days
  - Update on booking/cancellation
```

#### 3. **Booking Flow**
```
1. Check availability (Redis cache)
2. Reserve time slot (distributed lock)
3. Process payment (Stripe API)
4. Confirm booking (write to MySQL)
5. Send notifications (Kafka)
6. Update cache (Redis)
```

#### 4. **Pricing Algorithm**
```
Dynamic Pricing:
  - Base price (host sets)
  - Supply/demand in area
  - Seasonal trends
  - Local events
  - Competitor pricing
  - Length of stay discounts
```

---

## Common Patterns Across Companies

| Pattern | Used By | Purpose |
|---------|---------|---------|
| **Microservices** | Netflix, Uber, Airbnb | Scalability |
| **Sharding** | Instagram, Twitter, Uber | Database scaling |
| **Caching (Redis)** | All | Performance |
| **Message Queue (Kafka)** | Netflix, Uber, Airbnb | Async processing |
| **CDN** | Netflix, YouTube, Instagram | Content delivery |
| **Elasticsearch** | Airbnb, Uber | Search |
| **Load Balancing** | All | Traffic distribution |
| **Geo-distribution** | All | Low latency |

---

## Interview Tips

When asked "Design X":

1. **Clarify Requirements**
   - Users, scale, features
   - Read vs write heavy
   - Latency requirements

2. **High-Level Design**
   - Draw boxes (clients, servers, databases)
   - Show data flow

3. **Deep Dive Components**
   - API design
   - Database schema
   - Caching strategy

4. **Discuss Trade-offs**
   - Consistency vs availability
   - Cost vs performance

5. **Scalability**
   - How to handle 10x growth
   - Bottlenecks and solutions

---

## Next Steps

- **Interview Questions** → [interview-questions](../interview-questions/README.md)
- **Practice on**: LeetCode System Design, Pramp

---

**💡 Pro Tip**: Study how real companies solve problems. In interviews, reference these examples to show real-world knowledge!

