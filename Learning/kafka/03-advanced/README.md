# 📨 Kafka - Advanced Topics

Master advanced Kafka concepts for production systems!

---

## 📚 Table of Contents

1. [Kafka Streams](#kafka-streams)
2. [Kafka Connect](#kafka-connect)
3. [Schema Registry](#schema-registry)
4. [Transactions](#transactions)
5. [Exactly-Once Semantics](#exactly-once-semantics)
6. [Performance Tuning](#performance-tuning)
7. [Production Deployment](#production-deployment)
8. [Interview Questions](#interview-questions)

---

## 🌊 Kafka Streams

### What is Kafka Streams?

**Kafka Streams** is a client library for building stream processing applications.

**Features:**
- Lightweight (no separate cluster needed)
- Fault-tolerant
- Scalable
- Exactly-once processing
- Stateful and stateless operations

### Simple Streams Application

```java
import org.apache.kafka.streams.*;
import org.apache.kafka.streams.kstream.*;

public class WordCountApp {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "wordcount-app");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        
        StreamsBuilder builder = new StreamsBuilder();
        
        // Input stream
        KStream<String, String> textLines = 
            builder.stream("input-topic");
        
        // Processing
        KTable<String, Long> wordCounts = textLines
            .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\\W+")))
            .groupBy((key, word) -> word)
            .count();
        
        // Output
        wordCounts.toStream()
            .to("output-topic", Produced.with(Serdes.String(), Serdes.Long()));
        
        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
        
        Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
    }
}
```

### Stateful Operations

```java
public class StatefulStreamsApp {
    public static void main(String[] args) {
        StreamsBuilder builder = new StreamsBuilder();
        
        KStream<String, Long> transactions = 
            builder.stream("transactions");
        
        // Aggregation
        KTable<String, Long> totalByUser = transactions
            .groupByKey()
            .aggregate(
                () -> 0L,  // Initializer
                (key, value, aggregate) -> aggregate + value,  // Aggregator
                Materialized.as("user-totals-store")
            );
        
        // Windowing - Tumbling Window (5 minutes)
        KTable<Windowed<String>, Long> windowedTotals = transactions
            .groupByKey()
            .windowedBy(TimeWindows.ofSizeWithNoGrace(Duration.ofMinutes(5)))
            .aggregate(
                () -> 0L,
                (key, value, aggregate) -> aggregate + value
            );
        
        // Join streams
        KStream<String, String> orders = builder.stream("orders");
        KStream<String, String> payments = builder.stream("payments");
        
        KStream<String, String> ordersWithPayments = orders.join(
            payments,
            (orderValue, paymentValue) -> orderValue + " : " + paymentValue,
            JoinWindows.ofTimeDifferenceWithNoGrace(Duration.ofMinutes(5))
        );
    }
}
```

---

## 🔌 Kafka Connect

### What is Kafka Connect?

**Kafka Connect** is a framework for streaming data between Kafka and external systems.

**Components:**
- **Source Connectors:** Import data to Kafka
- **Sink Connectors:** Export data from Kafka

### Common Connectors

```yaml
Source Connectors:
  - JDBC Source (databases)
  - File Source
  - MongoDB Source
  - S3 Source
  - HTTP Source

Sink Connectors:
  - JDBC Sink
  - Elasticsearch Sink
  - S3 Sink
  - HDFS Sink
  - MongoDB Sink
```

### JDBC Source Connector Example

```json
{
  "name": "jdbc-source-connector",
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
    "tasks.max": "1",
    "connection.url": "jdbc:mysql://localhost:3306/mydb",
    "connection.user": "user",
    "connection.password": "password",
    "table.whitelist": "users,orders",
    "mode": "incrementing",
    "incrementing.column.name": "id",
    "topic.prefix": "mysql-",
    "poll.interval.ms": "1000"
  }
}
```

### Starting Kafka Connect

```bash
# Standalone mode
connect-standalone.sh \
  config/connect-standalone.properties \
  config/jdbc-source-connector.properties

# Distributed mode (production)
connect-distributed.sh config/connect-distributed.properties

# REST API to manage connectors
curl -X POST http://localhost:8083/connectors \
  -H "Content-Type: application/json" \
  -d @jdbc-source-connector.json
```

### Custom Connector

```java
public class CustomSourceConnector extends SourceConnector {
    
    @Override
    public void start(Map<String, String> props) {
        // Initialize connector
    }
    
    @Override
    public Class<? extends Task> taskClass() {
        return CustomSourceTask.class;
    }
    
    @Override
    public List<Map<String, String>> taskConfigs(int maxTasks) {
        // Return task configurations
    }
    
    @Override
    public void stop() {
        // Cleanup
    }
    
    @Override
    public ConfigDef config() {
        return new ConfigDef()
            .define("source.url", ConfigDef.Type.STRING, 
                    ConfigDef.Importance.HIGH, "Source URL");
    }
    
    @Override
    public String version() {
        return "1.0.0";
    }
}
```

---

## 📋 Schema Registry

### What is Schema Registry?

**Schema Registry** stores and manages Avro schemas for Kafka messages.

**Benefits:**
- Schema evolution
- Backward/forward compatibility
- Centralized schema management
- Automatic serialization/deserialization

### Avro Schema Example

```json
{
  "namespace": "com.example.kafka",
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "id", "type": "long"},
    {"name": "username", "type": "string"},
    {"name": "email", "type": "string"},
    {"name": "created_at", "type": "long", "logicalType": "timestamp-millis"}
  ]
}
```

### Producer with Avro

```java
import io.confluent.kafka.serializers.KafkaAvroSerializer;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.generic.GenericData;

public class AvroProducer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", KafkaAvroSerializer.class.getName());
        props.put("value.serializer", KafkaAvroSerializer.class.getName());
        props.put("schema.registry.url", "http://localhost:8081");
        
        KafkaProducer<String, GenericRecord> producer = new KafkaProducer<>(props);
        
        String userSchema = "{ \"type\": \"record\", \"name\": \"User\"," +
            "\"fields\": [" +
            "{\"name\": \"id\", \"type\": \"long\"}," +
            "{\"name\": \"username\", \"type\": \"string\"}" +
            "]}";
        
        Schema.Parser parser = new Schema.Parser();
        Schema schema = parser.parse(userSchema);
        
        GenericRecord user = new GenericData.Record(schema);
        user.put("id", 1L);
        user.put("username", "john_doe");
        
        ProducerRecord<String, GenericRecord> record = 
            new ProducerRecord<>("users-avro", user);
        
        producer.send(record);
        producer.close();
    }
}
```

---

## 💼 Transactions

### What are Kafka Transactions?

**Transactions** enable atomic writes across multiple partitions.

**Use Cases:**
- Exactly-once processing
- Atomicity across topics
- Read-process-write patterns

### Transactional Producer

```java
public class TransactionalProducer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        
        // Enable transactions
        props.put("enable.idempotence", "true");
        props.put("transactional.id", "my-transactional-id");
        
        KafkaProducer<String, String> producer = new KafkaProducer<>(props);
        
        // Initialize transactions
        producer.initTransactions();
        
        try {
            // Begin transaction
            producer.beginTransaction();
            
            // Send multiple records atomically
            producer.send(new ProducerRecord<>("topic1", "key1", "value1"));
            producer.send(new ProducerRecord<>("topic2", "key2", "value2"));
            producer.send(new ProducerRecord<>("topic3", "key3", "value3"));
            
            // Commit transaction
            producer.commitTransaction();
            
        } catch (Exception e) {
            // Abort on error
            producer.abortTransaction();
        } finally {
            producer.close();
        }
    }
}
```

### Transactional Consumer-Producer

```java
public class TransactionalProcessor {
    public static void main(String[] args) {
        // Consumer config
        Properties consumerProps = new Properties();
        consumerProps.put("bootstrap.servers", "localhost:9092");
        consumerProps.put("group.id", "txn-processor");
        consumerProps.put("enable.auto.commit", "false");
        consumerProps.put("isolation.level", "read_committed");
        
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(consumerProps);
        consumer.subscribe(Arrays.asList("input-topic"));
        
        // Producer config
        Properties producerProps = new Properties();
        producerProps.put("bootstrap.servers", "localhost:9092");
        producerProps.put("transactional.id", "processor-txn-id");
        producerProps.put("enable.idempotence", "true");
        
        KafkaProducer<String, String> producer = new KafkaProducer<>(producerProps);
        producer.initTransactions();
        
        while (true) {
            ConsumerRecords<String, String> records = 
                consumer.poll(Duration.ofMillis(100));
            
            if (!records.isEmpty()) {
                producer.beginTransaction();
                
                try {
                    for (ConsumerRecord<String, String> record : records) {
                        // Process and send
                        String processed = process(record.value());
                        producer.send(new ProducerRecord<>("output-topic", processed));
                    }
                    
                    // Commit offsets as part of transaction
                    producer.sendOffsetsToTransaction(
                        getOffsets(records),
                        consumer.groupMetadata()
                    );
                    
                    producer.commitTransaction();
                    
                } catch (Exception e) {
                    producer.abortTransaction();
                }
            }
        }
    }
    
    private static String process(String value) {
        return value.toUpperCase();
    }
    
    private static Map<TopicPartition, OffsetAndMetadata> getOffsets(
            ConsumerRecords<String, String> records) {
        Map<TopicPartition, OffsetAndMetadata> offsets = new HashMap<>();
        for (TopicPartition partition : records.partitions()) {
            List<ConsumerRecord<String, String>> partitionRecords = records.records(partition);
            long offset = partitionRecords.get(partitionRecords.size() - 1).offset();
            offsets.put(partition, new OffsetAndMetadata(offset + 1));
        }
        return offsets;
    }
}
```

---

## 🎯 Exactly-Once Semantics

### Delivery Guarantees

```yaml
At-Most-Once (acks=0):
  - No retries
  - Messages may be lost
  - Highest throughput

At-Least-Once (acks=1/all, retries):
  - Messages never lost
  - May have duplicates
  - Default behavior

Exactly-Once (idempotence + transactions):
  - No loss, no duplicates
  - Highest overhead
  - Production use case
```

### Achieving Exactly-Once

```java
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");

// Producer side
props.put("enable.idempotence", "true");
props.put("transactional.id", "unique-txn-id");
props.put("acks", "all");
props.put("retries", Integer.MAX_VALUE);

// Consumer side
props.put("isolation.level", "read_committed");
props.put("enable.auto.commit", "false");
```

---

## ⚡ Performance Tuning

### Producer Tuning

```java
Properties props = new Properties();

// Compression (snappy recommended)
props.put("compression.type", "snappy");

// Batching
props.put("batch.size", 32768);     // 32KB
props.put("linger.ms", 20);          // Wait 20ms

// Buffer
props.put("buffer.memory", 67108864);  // 64MB

// Parallelism
props.put("max.in.flight.requests.per.connection", 5);

// Throughput vs Latency
// High throughput: larger batch.size, higher linger.ms
// Low latency: smaller batch.size, lower linger.ms
```

### Consumer Tuning

```java
Properties props = new Properties();

// Fetch configuration
props.put("fetch.min.bytes", 50000);      // 50KB
props.put("fetch.max.wait.ms", 500);

// Max records per poll
props.put("max.poll.records", 1000);

// Partition fetch
props.put("max.partition.fetch.bytes", 2097152);  // 2MB
```

### Broker Tuning

```properties
# server.properties

# Network threads
num.network.threads=8

# I/O threads
num.io.threads=16

# Socket buffers
socket.send.buffer.bytes=102400
socket.receive.buffer.bytes=102400
socket.request.max.bytes=104857600

# Log configuration
log.segment.bytes=1073741824
log.retention.hours=168
log.retention.check.interval.ms=300000

# Replication
replica.lag.time.max.ms=10000
num.replica.fetchers=4

# Compression
compression.type=producer
```

---

## 🏭 Production Deployment

### High-Availability Setup

```yaml
Minimum Production Cluster:
  Brokers: 3 (for replication)
  Replication Factor: 3
  Min In-Sync Replicas: 2
  Partitions: 3x number of consumers

Hardware:
  CPU: 8+ cores
  RAM: 32GB+
  Disk: SSD (RAID 10)
  Network: 10Gbps+
```

### Monitoring Metrics

```yaml
Producer Metrics:
  - record-send-rate
  - request-latency-avg
  - buffer-available-bytes
  - batch-size-avg

Consumer Metrics:
  - records-consumed-rate
  - fetch-latency-avg
  - commit-latency-avg
  - records-lag-max

Broker Metrics:
  - UnderReplicatedPartitions
  - OfflinePartitionsCount
  - ActiveControllerCount
  - NetworkProcessorAvgIdlePercent
```

---

## 🎯 Interview Questions

**Q: What is Kafka Streams vs Kafka Connect?**

**Answer:**
- **Kafka Streams:** Library for stream processing (transformations, aggregations)
- **Kafka Connect:** Framework for data integration (import/export to external systems)

**Q: How do you achieve exactly-once semantics?**

**Answer:**
1. Enable idempotent producer
2. Use transactional API
3. Set isolation.level=read_committed on consumer
4. Commit offsets within transaction

**Q: What is Schema Registry used for?**

**Answer:**
- Store and manage Avro/JSON/Protobuf schemas
- Schema evolution and compatibility checking
- Automatic serialization/deserialization
- Centralized schema management

---

**Continue to Spring Boot Integration for application development!** 🚀

