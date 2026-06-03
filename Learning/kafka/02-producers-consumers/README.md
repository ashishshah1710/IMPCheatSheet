# 📨 Kafka - Producers & Consumers

Deep dive into Kafka producers and consumers!

---

## 📚 Table of Contents

1. [Producer Deep Dive](#producer-deep-dive)
2. [Producer Configuration](#producer-configuration)
3. [Partitioning Strategies](#partitioning-strategies)
4. [Consumer Deep Dive](#consumer-deep-dive)
5. [Consumer Configuration](#consumer-configuration)
6. [Offset Management](#offset-management)
7. [Rebalancing](#rebalancing)
8. [Interview Questions](#interview-questions)

---

## 📤 Producer Deep Dive

### Producer Architecture

```
Application
     ↓
KafkaProducer
     ↓
Serializer (Key + Value)
     ↓
Partitioner
     ↓
Record Accumulator (Buffer)
     ↓
Sender Thread → Kafka Broker
```

### Basic Producer Example

```java
import org.apache.kafka.clients.producer.*;
import java.util.Properties;

public class SimpleProducer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, 
            "org.apache.kafka.common.serialization.StringSerializer");
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, 
            "org.apache.kafka.common.serialization.StringSerializer");
        
        KafkaProducer<String, String> producer = new KafkaProducer<>(props);
        
        for (int i = 0; i < 100; i++) {
            ProducerRecord<String, String> record = 
                new ProducerRecord<>("my-topic", 
                    "key-" + i, 
                    "value-" + i);
            
            producer.send(record);
        }
        
        producer.close();
    }
}
```

### Asynchronous Send with Callback

```java
public class AsyncProducer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        
        KafkaProducer<String, String> producer = new KafkaProducer<>(props);
        
        ProducerRecord<String, String> record = 
            new ProducerRecord<>("my-topic", "key", "value");
        
        producer.send(record, new Callback() {
            @Override
            public void onCompletion(RecordMetadata metadata, Exception exception) {
                if (exception != null) {
                    System.err.println("Error: " + exception.getMessage());
                } else {
                    System.out.printf("Sent to partition %d at offset %d%n",
                        metadata.partition(), metadata.offset());
                }
            }
        });
        
        producer.flush();
        producer.close();
    }
}
```

---

## ⚙️ Producer Configuration

### Critical Settings

```java
Properties props = new Properties();

// Basic configuration
props.put("bootstrap.servers", "broker1:9092,broker2:9092");
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

// Acknowledgments (0, 1, all/-1)
props.put("acks", "all");  // Wait for all replicas

// Retries
props.put("retries", 3);
props.put("retry.backoff.ms", 100);

// Idempotence (exactly-once)
props.put("enable.idempotence", true);

// Compression
props.put("compression.type", "snappy");  // none, gzip, snappy, lz4, zstd

// Batch configuration
props.put("batch.size", 16384);  // 16KB
props.put("linger.ms", 10);      // Wait 10ms to batch

// Buffer memory
props.put("buffer.memory", 33554432);  // 32MB

// Request timeout
props.put("request.timeout.ms", 30000);
props.put("delivery.timeout.ms", 120000);
```

### Acks Configuration

```yaml
acks=0:
  - No acknowledgment from broker
  - Highest throughput
  - Lowest durability
  - Use: Metrics, logs (loss acceptable)

acks=1:
  - Leader acknowledges
  - Balanced performance/durability
  - Data loss if leader fails before replication

acks=all/-1:
  - All in-sync replicas acknowledge
  - Highest durability
  - Lower throughput
  - Use: Financial transactions, critical data
```

### Idempotent Producer

```java
// Enable idempotence (Kafka 0.11+)
props.put("enable.idempotence", true);

// Automatically sets:
// acks = all
// retries = Integer.MAX_VALUE
// max.in.flight.requests.per.connection = 5

// Prevents duplicates due to:
// - Network retries
// - Broker failures
// - Client retries
```

---

## 🎯 Partitioning Strategies

### Default Partitioner

```java
// With key - hash-based partitioning
ProducerRecord<String, String> record = 
    new ProducerRecord<>("topic", "key123", "value");
// partition = hash(key) % num_partitions

// Without key - round-robin
ProducerRecord<String, String> record = 
    new ProducerRecord<>("topic", "value");
```

### Custom Partitioner

```java
public class CustomPartitioner implements Partitioner {
    
    @Override
    public int partition(String topic, Object key, byte[] keyBytes,
                        Object value, byte[] valueBytes, Cluster cluster) {
        
        List<PartitionInfo> partitions = cluster.partitionsForTopic(topic);
        int numPartitions = partitions.size();
        
        if (key == null) {
            return ThreadLocalRandom.current().nextInt(numPartitions);
        }
        
        String keyString = (String) key;
        
        // Custom logic: Premium users to partition 0
        if (keyString.startsWith("premium_")) {
            return 0;
        }
        
        // Others distributed evenly
        return Math.abs(keyString.hashCode()) % numPartitions;
    }
    
    @Override
    public void close() {}
    
    @Override
    public void configure(Map<String, ?> configs) {}
}

// Use custom partitioner
props.put("partitioner.class", "com.example.CustomPartitioner");
```

### Specifying Partition Explicitly

```java
// Send to specific partition
ProducerRecord<String, String> record = 
    new ProducerRecord<>(
        "my-topic",   // topic
        2,            // partition
        "key",        // key
        "value"       // value
    );
```

---

## 📥 Consumer Deep Dive

### Consumer Architecture

```
KafkaConsumer
     ↓
subscribe(topics)
     ↓
poll() - Fetch records
     ↓
Deserializer
     ↓
Process records
     ↓
Commit offsets
```

### Basic Consumer

```java
import org.apache.kafka.clients.consumer.*;
import java.time.Duration;
import java.util.*;

public class SimpleConsumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "my-consumer-group");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("auto.offset.reset", "earliest");
        
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Arrays.asList("my-topic"));
        
        try {
            while (true) {
                ConsumerRecords<String, String> records = 
                    consumer.poll(Duration.ofMillis(100));
                
                for (ConsumerRecord<String, String> record : records) {
                    System.out.printf("partition=%d, offset=%d, key=%s, value=%s%n",
                        record.partition(), record.offset(), 
                        record.key(), record.value());
                }
            }
        } finally {
            consumer.close();
        }
    }
}
```

### Manual Offset Commit

```java
public class ManualCommitConsumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "my-group");
        props.put("enable.auto.commit", "false");  // Manual commit
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Arrays.asList("my-topic"));
        
        try {
            while (true) {
                ConsumerRecords<String, String> records = 
                    consumer.poll(Duration.ofMillis(100));
                
                for (ConsumerRecord<String, String> record : records) {
                    // Process record
                    processRecord(record);
                }
                
                // Commit after processing all records
                consumer.commitSync();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            consumer.close();
        }
    }
    
    private static void processRecord(ConsumerRecord<String, String> record) {
        System.out.println("Processing: " + record.value());
    }
}
```

---

## 🔧 Consumer Configuration

### Important Settings

```java
Properties props = new Properties();

// Basic
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "my-consumer-group");

// Deserializers
props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

// Auto offset reset (earliest, latest, none)
props.put("auto.offset.reset", "earliest");

// Offset commit
props.put("enable.auto.commit", "true");
props.put("auto.commit.interval.ms", "5000");

// Fetch configuration
props.put("fetch.min.bytes", 1024);       // Min 1KB
props.put("fetch.max.wait.ms", 500);      // Max wait 500ms
props.put("max.partition.fetch.bytes", 1048576);  // 1MB per partition

// Session timeout
props.put("session.timeout.ms", 10000);   // 10 seconds
props.put("heartbeat.interval.ms", 3000); // 3 seconds

// Max poll
props.put("max.poll.records", 500);
props.put("max.poll.interval.ms", 300000);  // 5 minutes
```

---

## 📌 Offset Management

### Commit Strategies

```java
// 1. Auto Commit (Default)
props.put("enable.auto.commit", "true");
props.put("auto.commit.interval.ms", "5000");

// 2. Sync Commit
consumer.commitSync();

// 3. Async Commit
consumer.commitAsync((offsets, exception) -> {
    if (exception != null) {
        System.err.println("Commit failed: " + exception.getMessage());
    }
});

// 4. Commit Specific Offsets
Map<TopicPartition, OffsetAndMetadata> offsets = new HashMap<>();
offsets.put(
    new TopicPartition("my-topic", 0),
    new OffsetAndMetadata(100)
);
consumer.commitSync(offsets);
```

### Seek to Specific Offset

```java
// Seek to beginning
consumer.seekToBeginning(consumer.assignment());

// Seek to end
consumer.seekToEnd(consumer.assignment());

// Seek to specific offset
TopicPartition partition = new TopicPartition("my-topic", 0);
consumer.seek(partition, 100);

// Seek to timestamp
Map<TopicPartition, Long> timestampsToSearch = new HashMap<>();
timestampsToSearch.put(partition, System.currentTimeMillis() - 3600000);  // 1 hour ago
Map<TopicPartition, OffsetAndTimestamp> offsets = 
    consumer.offsetsForTimes(timestampsToSearch);
```

---

## 🔄 Rebalancing

### Rebalance Triggers

```yaml
Consumer Joins:
  - New consumer added to group
  - Partitions redistributed

Consumer Leaves:
  - Consumer crashes
  - Consumer shuts down
  - Heartbeat timeout

Partition Changes:
  - New partitions added
  - Topic deleted
```

### Rebalance Listener

```java
public class RebalanceListenerConsumer {
    
    private Map<TopicPartition, OffsetAndMetadata> currentOffsets = new HashMap<>();
    
    class HandleRebalance implements ConsumerRebalanceListener {
        
        @Override
        public void onPartitionsRevoked(Collection<TopicPartition> partitions) {
            System.out.println("Partitions revoked: " + partitions);
            // Commit current offsets
            consumer.commitSync(currentOffsets);
        }
        
        @Override
        public void onPartitionsAssigned(Collection<TopicPartition> partitions) {
            System.out.println("Partitions assigned: " + partitions);
            // Initialize from database or external store
        }
    }
    
    public void consume() {
        consumer.subscribe(
            Arrays.asList("my-topic"),
            new HandleRebalance()
        );
        
        while (true) {
            ConsumerRecords<String, String> records = 
                consumer.poll(Duration.ofMillis(100));
            
            for (ConsumerRecord<String, String> record : records) {
                processRecord(record);
                
                currentOffsets.put(
                    new TopicPartition(record.topic(), record.partition()),
                    new OffsetAndMetadata(record.offset() + 1)
                );
            }
            
            consumer.commitAsync(currentOffsets, null);
        }
    }
}
```

---

## 🎯 Interview Questions

**Q1: What is the difference between commitSync() and commitAsync()?**

**Answer:**
- **commitSync():** Blocks until commit completes, retries on failure
- **commitAsync():** Non-blocking, doesn't retry, callback on completion

**Q2: What happens if max.poll.interval.ms is exceeded?**

**Answer:**
Consumer is considered dead and removed from group, triggering rebalance. Partition reassigned to another consumer.

**Q3: How do you ensure exactly-once delivery?**

**Answer:**
1. Enable idempotent producer
2. Use transactions
3. Store offsets with processed data atomically
4. Implement idempotent consumer logic

**Q4: What is auto.offset.reset?**

**Answer:**
Controls behavior when no offset exists:
- `earliest`: Start from beginning
- `latest`: Start from end (default)
- `none`: Throw exception

**Q5: How does Kafka achieve high throughput?**

**Answer:**
- Sequential disk I/O
- Batch processing
- Zero-copy transfers
- Compression
- Partitioning for parallelism

---

**Continue to Advanced Topics for Streams, Connect, and more!** 🚀

---

## 📖 Simple Explanation

This module deep-dives producer batching, acks, retries, partitioning strategies, consumer polling, offset commits, and rebalance behavior. These settings decide whether your pipeline is fast, safe, or stuck in duplicate processing.

Enterprise backends must explain acks=all, idempotent producer, and manual commits when side effects must not double-apply.

---

## 🎯 Interview Quick Prep

*Backend and enterprise interview focus — plain-English answers.*

### Q1: What does acks=all mean for producers?

**Simple Answer:**
The leader waits for all in-sync replicas to acknowledge before confirming success. It is safer for durability but slower than acks=1.

### Q2: How do you choose a partition key?

**Simple Answer:**
Use a business key that keeps related events ordered—orderId, customerId—so all events for that entity land in one partition and keep order.

### Q3: What causes consumer lag?

**Simple Answer:**
Consumers process slower than producers, too few consumers, slow handlers, or rebalance storms. Fix by scaling consumers, optimizing code, or increasing partitions with a planned migration.

### Q4: Manual vs auto offset commit?

**Simple Answer:**
Auto commit is simple but can acknowledge messages before processing finishes, risking loss on crash. Manual commit after successful processing gives stronger control for side effects.

### Q5: What is a consumer rebalance?

**Simple Answer:**
When members join or leave a group, partitions are reassigned. Frequent rebalances pause consumption; stable session timeouts and cooperative protocols reduce impact.

