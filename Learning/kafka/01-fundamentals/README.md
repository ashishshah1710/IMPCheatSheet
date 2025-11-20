# 📨 Kafka - Fundamentals

Master Apache Kafka core concepts and architecture!

---

## 📚 Table of Contents

1. [What is Kafka?](#what-is-kafka)
2. [Kafka Architecture](#kafka-architecture)
3. [Topics & Partitions](#topics-partitions)
4. [Producers & Consumers](#producers-consumers)
5. [Consumer Groups](#consumer-groups)
6. [Zookeeper vs KRaft](#zookeeper-kraft)
7. [Installation & Setup](#installation-setup)
8. [Interview Questions](#interview-questions)

---

## 🎯 What is Kafka?

Apache Kafka is a **distributed event streaming platform** used for:
- Real-time data pipelines
- Streaming applications
- Event-driven architectures
- Microservices communication

### Key Features:
- **High Throughput:** Millions of messages/second
- **Scalability:** Horizontal scaling with partitions
- **Durability:** Persistent storage on disk
- **Fault Tolerance:** Replication across brokers
- **Low Latency:** Sub-10ms latency
- **Distributed:** Runs as a cluster

### Use Cases:
- Real-time analytics
- Log aggregation
- Event sourcing
- Stream processing
- Metrics collection
- CDC (Change Data Capture)

---

## 🏗️ Kafka Architecture

### Core Components

```
┌─────────────────────────────────────────────────────────┐
│                 KAFKA CLUSTER                            │
├─────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Broker 1 │  │ Broker 2 │  │ Broker 3 │              │
│  │          │  │          │  │          │              │
│  │ Topic A  │  │ Topic A  │  │ Topic A  │              │
│  │ Part 0   │  │ Part 1   │  │ Part 2   │              │
│  │ (Leader) │  │ (Replica)│  │ (Replica)│              │
│  └──────────┘  └──────────┘  └──────────┘              │
├─────────────────────────────────────────────────────────┤
│              Zookeeper / KRaft                           │
│         (Metadata & Leader Election)                     │
└─────────────────────────────────────────────────────────┘
         ↑                              ↓
    ┌─────────┐                    ┌─────────┐
    │Producer │                    │Consumer │
    └─────────┘                    └─────────┘
```

### Broker
- Kafka server that stores and serves data
- Multiple brokers form a cluster
- Each broker identified by unique ID
- Handles read/write requests

### Zookeeper/KRaft
- **Zookeeper (legacy):** Manages cluster metadata
- **KRaft (Kafka 3.x+):** Built-in consensus, no Zookeeper needed
- Leader election
- Topic configuration
- Broker registry

---

## 📋 Topics & Partitions

### Topics

A **Topic** is a category/feed name to which records are published.

```
Topic: user-events
├── Partition 0: [msg1][msg2][msg3]...
├── Partition 1: [msg4][msg5][msg6]...
└── Partition 2: [msg7][msg8][msg9]...
```

**Characteristics:**
- Logical grouping of messages
- Split into partitions for parallelism
- Configurable retention period
- Immutable (append-only log)

### Partitions

**Partition** is an ordered, immutable sequence of records.

```
Partition 0:
┌────────────────────────────────────────────┐
│ Offset: 0    1    2    3    4    5    6    │
│ Data:  [A]  [B]  [C]  [D]  [E]  [F]  [G]   │
└────────────────────────────────────────────┘
         ↑                             ↑
    Old messages              New messages
```

**Key Concepts:**
- Each message gets sequential ID (offset)
- Messages are ordered within partition
- Partitions enable parallelism
- More partitions = higher throughput

### Offsets

**Offset** is a unique ID for each message in a partition.

- Sequential integer (0, 1, 2, ...)
- Immutable once assigned
- Consumers track their position via offset
- Stored in special Kafka topic `__consumer_offsets`

---

## 📤 Producers & Consumers

### Producer

**Producer** publishes messages to Kafka topics.

```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

KafkaProducer<String, String> producer = new KafkaProducer<>(props);

ProducerRecord<String, String> record = 
    new ProducerRecord<>("my-topic", "key", "value");

producer.send(record);
producer.close();
```

**Producer Flow:**
1. Create record
2. Serialize key/value
3. Determine partition
4. Send to broker
5. Receive acknowledgment

### Consumer

**Consumer** reads messages from Kafka topics.

```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "my-group");
props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
consumer.subscribe(Arrays.asList("my-topic"));

while (true) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
    for (ConsumerRecord<String, String> record : records) {
        System.out.printf("offset=%d, key=%s, value=%s%n",
            record.offset(), record.key(), record.value());
    }
}
```

---

## 👥 Consumer Groups

### What is a Consumer Group?

A **Consumer Group** is a set of consumers that cooperatively consume a topic.

```
Topic: orders (3 partitions)

Consumer Group: order-processors
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Consumer A  │  │ Consumer B  │  │ Consumer C  │
│ Partition 0 │  │ Partition 1 │  │ Partition 2 │
└─────────────┘  └─────────────┘  └─────────────┘
```

**Benefits:**
- Load balancing across consumers
- Fault tolerance (rebalancing)
- Scalability (add more consumers)
- Each partition assigned to only one consumer in group

### Consumer Rebalancing

**Rebalancing** redistributes partitions when:
- Consumer joins group
- Consumer leaves group
- Partition count changes

```
Before Rebalance:
Consumer A: [P0, P1]
Consumer B: [P2, P3]

After Consumer C joins:
Consumer A: [P0]
Consumer B: [P1]
Consumer C: [P2, P3]
```

---

## 🔧 Zookeeper vs KRaft

### Zookeeper (Legacy)

```
┌────────────────────────────────────┐
│     Zookeeper Ensemble              │
│  (Separate cluster management)      │
└────────────────────────────────────┘
              ↕
┌────────────────────────────────────┐
│       Kafka Brokers                 │
└────────────────────────────────────┘
```

**Issues:**
- Extra dependency
- Complex deployment
- Scaling limitations
- Operational overhead

### KRaft (Kafka 3.x+)

```
┌────────────────────────────────────┐
│    Kafka Cluster (Self-managed)     │
│  Built-in consensus (Raft protocol) │
└────────────────────────────────────┘
```

**Benefits:**
- No external dependency
- Simpler architecture
- Better scalability
- Faster metadata operations
- Production-ready since Kafka 3.3

---

## 🛠️ Installation & Setup

### Docker Compose (Recommended)

```yaml
version: '3.8'

services:
  kafka:
    image: confluentinc/cp-kafka:7.5.0
    hostname: kafka
    container_name: kafka
    ports:
      - "9092:9092"
      - "9101:9101"
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: 'CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT'
      KAFKA_ADVERTISED_LISTENERS: 'PLAINTEXT://localhost:9092'
      KAFKA_PROCESS_ROLES: 'broker,controller'
      KAFKA_CONTROLLER_QUORUM_VOTERS: '1@kafka:29093'
      KAFKA_LISTENERS: 'PLAINTEXT://kafka:29092,CONTROLLER://kafka:29093,PLAINTEXT_HOST://0.0.0.0:9092'
      KAFKA_INTER_BROKER_LISTENER_NAME: 'PLAINTEXT'
      KAFKA_CONTROLLER_LISTENER_NAMES: 'CONTROLLER'
      KAFKA_LOG_DIRS: '/tmp/kraft-combined-logs'
      CLUSTER_ID: 'MkU3OEVBNTcwNTJENDM2Qk'

  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    container_name: kafka-ui
    depends_on:
      - kafka
    ports:
      - "8080:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:29092
```

```bash
# Start Kafka
docker-compose up -d

# Access Kafka UI
http://localhost:8080
```

### Command Line Tools

```bash
# Create topic
kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --partitions 3 \
  --replication-factor 1

# List topics
kafka-topics.sh --list \
  --bootstrap-server localhost:9092

# Describe topic
kafka-topics.sh --describe \
  --bootstrap-server localhost:9092 \
  --topic my-topic

# Produce messages
kafka-console-producer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic

# Consume messages
kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --from-beginning

# List consumer groups
kafka-consumer-groups.sh --list \
  --bootstrap-server localhost:9092

# Describe consumer group
kafka-consumer-groups.sh --describe \
  --bootstrap-server localhost:9092 \
  --group my-group
```

---

## 🎯 Interview Questions

**Q1: What is Apache Kafka?**

**Answer:**
Kafka is a distributed event streaming platform for:
- Publishing and subscribing to streams of records
- Storing streams durably and reliably
- Processing streams in real-time

**Q2: Kafka vs Traditional Message Queue?**

**Answer:**

| Feature | Kafka | Traditional MQ |
|---------|-------|----------------|
| **Model** | Pub-Sub + Queue | Typically Queue |
| **Persistence** | Durable (disk) | Often in-memory |
| **Replay** | Yes (offset) | No |
| **Throughput** | Very high | Moderate |
| **Ordering** | Per partition | Per queue |
| **Retention** | Configurable | Deleted after consumption |

**Q3: What are partitions and why are they important?**

**Answer:**
Partitions are:
- Ordered, immutable sequence of records
- Enable parallelism (multiple consumers)
- Provide scalability (distributed across brokers)
- Ensure ordering within partition
- Allow horizontal scaling

**Q4: What is a consumer group?**

**Answer:**
Group of consumers that:
- Cooperatively consume a topic
- Each partition consumed by only one consumer in group
- Enable load balancing
- Provide fault tolerance via rebalancing

**Q5: What is an offset?**

**Answer:**
Offset is:
- Unique sequential ID for each message in partition
- Consumer's position in partition
- Committed to Kafka (`__consumer_offsets` topic)
- Enables replay, fault tolerance, and exactly-once processing

---

## 💡 Key Takeaways

✅ Kafka is a distributed event streaming platform  
✅ Topics are divided into partitions for parallelism  
✅ Offsets uniquely identify messages in partitions  
✅ Consumer groups enable load balancing  
✅ Replication provides fault tolerance  
✅ KRaft removes Zookeeper dependency  

---

**Continue to Producers & Consumers for deep dive!** 🚀

