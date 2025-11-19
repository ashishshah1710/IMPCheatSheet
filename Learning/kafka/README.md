# 📨 Apache Kafka - Complete Guide

**For 3.5+ Years Experienced Developers | Interview Preparation**

Master Apache Kafka for distributed event streaming and ace your technical interviews!

---

## 📖 Overview

Apache Kafka is a distributed event streaming platform capable of handling trillions of events a day. It's designed for high-throughput, fault-tolerant, publish-subscribe messaging.

### Why Kafka?

✅ **High Throughput** - Millions of messages per second  
✅ **Scalable** - Horizontal scaling with partitions  
✅ **Durable** - Persistent message storage  
✅ **Real-Time** - Low latency message delivery  
✅ **Fault-Tolerant** - Replication and high availability  
✅ **Industry Standard** - LinkedIn, Netflix, Uber, Airbnb  

---

## 🎯 Learning Path for Experienced Developers

### Phase 1: Kafka Fundamentals (1 week)
**Master core concepts**

- Architecture overview
- Topics, Partitions, Offsets
- Producers and Consumers
- Consumer Groups
- Brokers and Clusters
- Zookeeper/KRaft

**👉 Start:** [`01-fundamentals/README.md`](01-fundamentals/README.md)

---

### Phase 2: Producers & Consumers (1 week)
**Deep dive into clients**

- Producer configuration
- Serialization
- Partitioning strategies
- Consumer configuration
- Offset management
- Consumer rebalancing

**👉 Continue:** [`02-producers-consumers/README.md`](02-producers-consumers/README.md)

---

### Phase 3: Advanced Kafka (1 week)
**Production-ready knowledge**

- Kafka Streams API
- Kafka Connect
- Schema Registry (Avro)
- Transactions
- Exactly-once semantics
- Performance tuning

**👉 Master:** [`03-advanced/README.md`](03-advanced/README.md)

---

### Phase 4: Spring Boot Integration (1 week)
**Build event-driven applications**

- Spring Kafka basics
- KafkaTemplate
- @KafkaListener
- Error handling
- Dead Letter Topics
- Testing Kafka applications

**👉 Advanced:** [`04-spring-boot-integration/README.md`](04-spring-boot-integration/README.md)

---

## 💼 Interview Preparation

### Top Interview Questions

**Fundamentals:**
- What is Apache Kafka?
- Kafka vs traditional message queues?
- Explain Topics and Partitions
- What is a Consumer Group?
- Offset management explained

**Producers:**
- How does producer work?
- Partitioning strategies
- Acks configuration
- Idempotent producer
- Retry mechanism

**Consumers:**
- Consumer group rebalancing
- Offset commit strategies
- At-least-once vs exactly-once
- Consumer lag handling
- Kafka performance

**Advanced:**
- Kafka Streams vs KSQL?
- Schema evolution with Avro
- Exactly-once semantics
- Kafka Connect use cases
- Monitoring Kafka cluster

**👉 See:** [`interview-questions/README.md`](interview-questions/README.md)

---

## 🎯 Quick Start

### Installation & Setup

```bash
# Download Kafka
wget https://downloads.apache.org/kafka/3.6.0/kafka_2.13-3.6.0.tgz
tar -xzf kafka_2.13-3.6.0.tgz
cd kafka_2.13-3.6.0

# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Server
bin/kafka-server-start.sh config/server.properties

# Or using Docker
docker run -d --name kafka \
  -p 9092:9092 \
  apache/kafka:latest
```

### Basic Commands

```bash
# Create Topic
kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --partitions 3 \
  --replication-factor 1

# List Topics
kafka-topics.sh --list --bootstrap-server localhost:9092

# Describe Topic
kafka-topics.sh --describe \
  --bootstrap-server localhost:9092 \
  --topic my-topic

# Produce Messages
kafka-console-producer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic

# Consume Messages
kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --from-beginning

# Consumer Groups
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --list

# Describe Consumer Group
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --group my-group \
  --describe
```

### Java Producer

```java
import org.apache.kafka.clients.producer.*;
import java.util.Properties;

public class SimpleProducer {
    
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", 
            "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", 
            "org.apache.kafka.common.serialization.StringSerializer");
        props.put("acks", "all");
        props.put("retries", 3);
        
        Producer<String, String> producer = new KafkaProducer<>(props);
        
        try {
            for (int i = 0; i < 100; i++) {
                ProducerRecord<String, String> record = 
                    new ProducerRecord<>("my-topic", 
                        Integer.toString(i), 
                        "Message " + i);
                
                // Synchronous send
                RecordMetadata metadata = producer.send(record).get();
                System.out.printf("Sent record to partition %d with offset %d%n",
                    metadata.partition(), metadata.offset());
                
                // Asynchronous send with callback
                producer.send(record, (metadata, exception) -> {
                    if (exception != null) {
                        exception.printStackTrace();
                    } else {
                        System.out.printf("Sent to partition %d offset %d%n",
                            metadata.partition(), metadata.offset());
                    }
                });
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            producer.close();
        }
    }
}
```

### Java Consumer

```java
import org.apache.kafka.clients.consumer.*;
import java.util.*;
import java.time.Duration;

public class SimpleConsumer {
    
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "my-consumer-group");
        props.put("key.deserializer", 
            "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", 
            "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("enable.auto.commit", "false");
        props.put("auto.offset.reset", "earliest");
        
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Arrays.asList("my-topic"));
        
        try {
            while (true) {
                ConsumerRecords<String, String> records = 
                    consumer.poll(Duration.ofMillis(100));
                
                for (ConsumerRecord<String, String> record : records) {
                    System.out.printf("Received: key=%s, value=%s, " +
                        "partition=%d, offset=%d%n",
                        record.key(), record.value(), 
                        record.partition(), record.offset());
                    
                    // Process the message
                    processMessage(record);
                }
                
                // Manual commit
                consumer.commitSync();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            consumer.close();
        }
    }
    
    private static void processMessage(ConsumerRecord<String, String> record) {
        // Your business logic here
    }
}
```

---

## 🍃 Spring Boot Integration

### Dependencies

```xml
<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
</dependency>
```

### Configuration

```yaml
spring:
  kafka:
    bootstrap-servers: localhost:9092
    consumer:
      group-id: my-group
      auto-offset-reset: earliest
      key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value-deserializer: org.springframework.kafka.support.serializer.JsonDeserializer
      properties:
        spring.json.trusted.packages: "*"
    producer:
      key-serializer: org.apache.kafka.common.serialization.StringSerializer
      value-serializer: org.springframework.kafka.support.serializer.JsonSerializer
      acks: all
      retries: 3
```

### Producer (Spring Boot)

```java
@Service
@Slf4j
public class KafkaProducerService {
    
    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;
    
    private static final String TOPIC = "user-events";
    
    public void sendMessage(String key, Object message) {
        log.info("Sending message: {}", message);
        
        CompletableFuture<SendResult<String, Object>> future = 
            kafkaTemplate.send(TOPIC, key, message);
        
        future.whenComplete((result, ex) -> {
            if (ex == null) {
                log.info("Message sent successfully: partition={}, offset={}",
                    result.getRecordMetadata().partition(),
                    result.getRecordMetadata().offset());
            } else {
                log.error("Failed to send message", ex);
            }
        });
    }
    
    public void sendMessageSync(String key, Object message) throws Exception {
        SendResult<String, Object> result = 
            kafkaTemplate.send(TOPIC, key, message).get();
        log.info("Message sent: offset={}", result.getRecordMetadata().offset());
    }
}
```

### Consumer (Spring Boot)

```java
@Service
@Slf4j
public class KafkaConsumerService {
    
    @KafkaListener(
        topics = "user-events",
        groupId = "my-group",
        containerFactory = "kafkaListenerContainerFactory"
    )
    public void listen(ConsumerRecord<String, UserEvent> record) {
        log.info("Received message: key={}, value={}, partition={}, offset={}",
            record.key(), record.value(), 
            record.partition(), record.offset());
        
        try {
            processEvent(record.value());
        } catch (Exception e) {
            log.error("Error processing message", e);
            // Message will be sent to DLT if configured
        }
    }
    
    @KafkaListener(topics = "batch-topic", groupId = "batch-group")
    public void listenBatch(List<ConsumerRecord<String, String>> records) {
        log.info("Received batch of {} messages", records.size());
        records.forEach(this::processRecord);
    }
    
    private void processEvent(UserEvent event) {
        // Your business logic
    }
    
    private void processRecord(ConsumerRecord<String, String> record) {
        // Process each record
    }
}
```

### Configuration Class

```java
@Configuration
@EnableKafka
public class KafkaConfig {
    
    @Bean
    public ProducerFactory<String, Object> producerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        config.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, 
            StringSerializer.class);
        config.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, 
            JsonSerializer.class);
        config.put(ProducerConfig.ACKS_CONFIG, "all");
        return new DefaultKafkaProducerFactory<>(config);
    }
    
    @Bean
    public KafkaTemplate<String, Object> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
    
    @Bean
    public ConsumerFactory<String, Object> consumerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        config.put(ConsumerConfig.GROUP_ID_CONFIG, "my-group");
        config.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, 
            StringDeserializer.class);
        config.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, 
            JsonDeserializer.class);
        config.put(JsonDeserializer.TRUSTED_PACKAGES, "*");
        return new DefaultKafkaConsumerFactory<>(config);
    }
    
    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, Object> 
        kafkaListenerContainerFactory() {
        
        ConcurrentKafkaListenerContainerFactory<String, Object> factory = 
            new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        factory.setConcurrency(3); // 3 consumer threads
        factory.getContainerProperties()
            .setAckMode(ContainerProperties.AckMode.MANUAL);
        return factory;
    }
    
    // Error handling
    @Bean
    public DefaultErrorHandler errorHandler() {
        BackOff fixedBackOff = new FixedBackOff(1000L, 3L);
        return new DefaultErrorHandler((record, exception) -> {
            // Send to DLT or log
            log.error("Failed to process record: {}", record, exception);
        }, fixedBackOff);
    }
}
```

---

## 🏆 For 3.5+ Years Experience

### What Interviewers Expect

**Technical Mastery:**
- Kafka architecture
- Partition and replication
- Consumer groups
- Exactly-once semantics
- Performance tuning

**Real-World Experience:**
- Production deployment
- Monitoring Kafka cluster
- Handling consumer lag
- Schema management
- Disaster recovery

**Problem-Solving:**
- Design event-driven systems
- Optimize throughput
- Handle failures
- Implement patterns
- Troubleshoot issues

---

## 📊 Interview Success Metrics

| Topic | Importance | Interview Frequency |
|-------|------------|-------------------|
| Architecture | 🔴 Critical | 95% |
| Topics & Partitions | 🔴 Critical | 90% |
| Consumer Groups | 🔴 Critical | 85% |
| Producers | 🟡 Important | 80% |
| Replication | 🟡 Important | 70% |
| Kafka Streams | 🟢 Good to Know | 60% |
| Schema Registry | 🟢 Good to Know | 50% |

---

## ✅ Preparation Checklist

### Fundamentals
- [ ] Kafka architecture
- [ ] Topics and partitions
- [ ] Brokers and clusters
- [ ] Replication factor
- [ ] Leader election

### Producers & Consumers
- [ ] Producer configuration
- [ ] Serialization
- [ ] Consumer groups
- [ ] Offset management
- [ ] Rebalancing

### Advanced
- [ ] Kafka Streams
- [ ] Kafka Connect
- [ ] Schema Registry
- [ ] Transactions
- [ ] Exactly-once semantics

### Spring Boot
- [ ] Spring Kafka integration
- [ ] KafkaTemplate
- [ ] @KafkaListener
- [ ] Error handling
- [ ] Testing

---

## 🚀 Career Impact

**Salary with Kafka Expertise:**
- **3-5 Years:** $100K-$150K
- **5-7 Years:** $140K-$190K
- **7+ Years:** $170K-$220K+

---

## 🔗 Quick Links

| Topic | Link |
|-------|------|
| Fundamentals | [01-fundamentals/README.md](01-fundamentals/README.md) |
| Producers & Consumers | [02-producers-consumers/README.md](02-producers-consumers/README.md) |
| Advanced Kafka | [03-advanced/README.md](03-advanced/README.md) |
| Spring Boot Integration | [04-spring-boot-integration/README.md](04-spring-boot-integration/README.md) |
| Interview Questions | [interview-questions/README.md](interview-questions/README.md) |
| Cheat Sheet | [CHEATSHEET.md](CHEATSHEET.md) |

---

**Ready to master Kafka?** 📨

👉 **[Start with Fundamentals →](01-fundamentals/README.md)**

