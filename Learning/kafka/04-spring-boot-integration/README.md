# 🌸 Kafka - Spring Boot Integration

Build production-ready event-driven applications with Spring Kafka!

---

## 📚 Table of Contents

1. [Setup & Configuration](#setup-configuration)
2. [Producer Implementation](#producer-implementation)
3. [Consumer Implementation](#consumer-implementation)
4. [Error Handling](#error-handling)
5. [Testing](#testing)
6. [Production Patterns](#production-patterns)
7. [Monitoring](#monitoring)
8. [Interview Questions](#interview-questions)

---

## 🛠️ Setup & Configuration

### Dependencies

```xml
<!-- pom.xml -->
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <dependency>
        <groupId>org.springframework.kafka</groupId>
        <artifactId>spring-kafka</artifactId>
    </dependency>
    
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    
    <dependency>
        <groupId>org.springframework.kafka</groupId>
        <artifactId>spring-kafka-test</artifactId>
        <scope>test</scope>
    </dependency>
    
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
</dependencies>
```

### Application Configuration

```yaml
# application.yml
spring:
  kafka:
    bootstrap-servers: localhost:9092
    
    producer:
      key-serializer: org.apache.kafka.common.serialization.StringSerializer
      value-serializer: org.springframework.kafka.support.serializer.JsonSerializer
      acks: all
      retries: 3
      properties:
        enable.idempotence: true
        max.in.flight.requests.per.connection: 5
        compression.type: snappy
    
    consumer:
      group-id: my-consumer-group
      auto-offset-reset: earliest
      key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
      value-deserializer: org.springframework.kafka.support.serializer.JsonDeserializer
      properties:
        spring.json.trusted.packages: "*"
        max.poll.records: 500
        session.timeout.ms: 10000
    
    listener:
      ack-mode: manual
      concurrency: 3

logging:
  level:
    org.apache.kafka: INFO
    org.springframework.kafka: DEBUG
```

### Kafka Configuration Class

```java
@Configuration
@EnableKafka
public class KafkaConfig {
    
    @Value("${spring.kafka.bootstrap-servers}")
    private String bootstrapServers;
    
    // Producer Factory
    @Bean
    public ProducerFactory<String, Object> producerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        config.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        config.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
        config.put(ProducerConfig.ACKS_CONFIG, "all");
        config.put(ProducerConfig.RETRIES_CONFIG, 3);
        config.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true);
        
        return new DefaultKafkaProducerFactory<>(config);
    }
    
    @Bean
    public KafkaTemplate<String, Object> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
    
    // Consumer Factory
    @Bean
    public ConsumerFactory<String, Object> consumerFactory() {
        Map<String, Object> config = new HashMap<>();
        config.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        config.put(ConsumerConfig.GROUP_ID_CONFIG, "my-consumer-group");
        config.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        config.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, JsonDeserializer.class);
        config.put(JsonDeserializer.TRUSTED_PACKAGES, "*");
        config.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        
        return new DefaultKafkaConsumerFactory<>(config);
    }
    
    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, Object> kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, Object> factory =
            new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        factory.setConcurrency(3);
        factory.getContainerProperties().setAckMode(ContainerProperties.AckMode.MANUAL);
        return factory;
    }
}
```

---

## 📤 Producer Implementation

### Domain Model

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
public class OrderEvent {
    private String orderId;
    private String customerId;
    private Double amount;
    private String status;
    private LocalDateTime createdAt;
}
```

### Kafka Producer Service

```java
@Service
@Slf4j
public class KafkaProducerService {
    
    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;
    
    private static final String TOPIC = "orders";
    
    // Simple send
    public void sendMessage(OrderEvent order) {
        kafkaTemplate.send(TOPIC, order);
        log.info("Order sent: {}", order);
    }
    
    // Send with key
    public void sendMessageWithKey(String key, OrderEvent order) {
        kafkaTemplate.send(TOPIC, key, order);
        log.info("Order sent with key {}: {}", key, order);
    }
    
    // Send with callback
    public void sendMessageAsync(OrderEvent order) {
        ListenableFuture<SendResult<String, Object>> future = 
            kafkaTemplate.send(TOPIC, order);
        
        future.addCallback(new ListenableFutureCallback<>() {
            @Override
            public void onSuccess(SendResult<String, Object> result) {
                log.info("Sent message=[{}] with offset=[{}]",
                    order,
                    result.getRecordMetadata().offset());
            }
            
            @Override
            public void onFailure(Throwable ex) {
                log.error("Unable to send message=[{}] due to : {}", 
                    order, ex.getMessage());
            }
        });
    }
    
    // Send with CompletableFuture (Spring 2.7+)
    public CompletableFuture<SendResult<String, Object>> sendMessageReactive(OrderEvent order) {
        return kafkaTemplate.send(TOPIC, order)
            .completable()
            .whenComplete((result, ex) -> {
                if (ex == null) {
                    log.info("Sent message=[{}] with offset=[{}]",
                        order,
                        result.getRecordMetadata().offset());
                } else {
                    log.error("Unable to send message=[{}] due to : {}", 
                        order, ex.getMessage());
                }
            });
    }
    
    // Send to specific partition
    public void sendToPartition(int partition, OrderEvent order) {
        kafkaTemplate.send(TOPIC, partition, null, order);
        log.info("Order sent to partition {}: {}", partition, order);
    }
}
```

### REST Controller

```java
@RestController
@RequestMapping("/api/orders")
@Slf4j
public class OrderController {
    
    @Autowired
    private KafkaProducerService producerService;
    
    @PostMapping
    public ResponseEntity<String> createOrder(@RequestBody OrderEvent order) {
        order.setCreatedAt(LocalDateTime.now());
        producerService.sendMessage(order);
        return ResponseEntity.ok("Order published successfully");
    }
    
    @PostMapping("/async")
    public ResponseEntity<String> createOrderAsync(@RequestBody OrderEvent order) {
        order.setCreatedAt(LocalDateTime.now());
        producerService.sendMessageAsync(order);
        return ResponseEntity.accepted().body("Order submitted for publishing");
    }
}
```

---

## 📥 Consumer Implementation

### Basic Consumer

```java
@Service
@Slf4j
public class KafkaConsumerService {
    
    @KafkaListener(topics = "orders", groupId = "order-consumers")
    public void consumeOrder(OrderEvent order) {
        log.info("Received order: {}", order);
        processOrder(order);
    }
    
    private void processOrder(OrderEvent order) {
        // Business logic here
        log.info("Processing order: {}", order.getOrderId());
    }
}
```

### Consumer with Manual Acknowledgment

```java
@Service
@Slf4j
public class ManualAckConsumer {
    
    @KafkaListener(
        topics = "orders",
        groupId = "manual-ack-group",
        containerFactory = "kafkaListenerContainerFactory"
    )
    public void consume(
            ConsumerRecord<String, OrderEvent> record,
            Acknowledgment acknowledgment) {
        
        try {
            log.info("Received: partition={}, offset={}, key={}, value={}",
                record.partition(),
                record.offset(),
                record.key(),
                record.value());
            
            processOrder(record.value());
            
            // Manual acknowledgment
            acknowledgment.acknowledge();
            
        } catch (Exception e) {
            log.error("Error processing message", e);
            // Don't acknowledge - message will be reprocessed
        }
    }
    
    private void processOrder(OrderEvent order) {
        // Process order
        log.info("Order processed: {}", order.getOrderId());
    }
}
```

### Batch Consumer

```java
@Service
@Slf4j
public class BatchConsumer {
    
    @KafkaListener(
        topics = "orders",
        groupId = "batch-consumers",
        containerFactory = "batchFactory"
    )
    public void consumeBatch(
            List<ConsumerRecord<String, OrderEvent>> records,
            Acknowledgment acknowledgment) {
        
        log.info("Received batch of {} messages", records.size());
        
        try {
            for (ConsumerRecord<String, OrderEvent> record : records) {
                processOrder(record.value());
            }
            
            acknowledgment.acknowledge();
            log.info("Batch processed successfully");
            
        } catch (Exception e) {
            log.error("Error processing batch", e);
        }
    }
}
```

### Multi-Topic Consumer

```java
@Service
@Slf4j
public class MultiTopicConsumer {
    
    @KafkaListener(
        topics = {"orders", "payments", "shipments"},
        groupId = "multi-topic-group"
    )
    public void consumeMultipleTopics(ConsumerRecord<String, Object> record) {
        log.info("Received from topic: {}, message: {}", 
            record.topic(), record.value());
        
        switch (record.topic()) {
            case "orders":
                handleOrder((OrderEvent) record.value());
                break;
            case "payments":
                handlePayment((PaymentEvent) record.value());
                break;
            case "shipments":
                handleShipment((ShipmentEvent) record.value());
                break;
        }
    }
}
```

---

## ⚠️ Error Handling

### Dead Letter Topic (DLT)

```java
@Configuration
public class ErrorHandlingConfig {
    
    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, Object> 
            kafkaListenerContainerFactory(
                ConsumerFactory<String, Object> consumerFactory) {
        
        ConcurrentKafkaListenerContainerFactory<String, Object> factory =
            new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        
        // Error handling
        factory.setCommonErrorHandler(
            new DefaultErrorHandler(
                new DeadLetterPublishingRecoverer(kafkaTemplate(),
                    (record, ex) -> {
                        return new TopicPartition(
                            record.topic() + ".DLT",
                            record.partition()
                        );
                    }),
                new FixedBackOff(1000L, 3)  // 3 retries with 1s delay
            )
        );
        
        return factory;
    }
}

// DLT Consumer
@Service
@Slf4j
public class DeadLetterTopicConsumer {
    
    @KafkaListener(topics = "orders.DLT", groupId = "dlt-group")
    public void consumeDLT(ConsumerRecord<String, OrderEvent> record) {
        log.error("Message in DLT: partition={}, offset={}, value={}",
            record.partition(),
            record.offset(),
            record.value());
        
        // Handle failed messages (alert, manual review, etc.)
        alertOps(record);
    }
    
    private void alertOps(ConsumerRecord<String, OrderEvent> record) {
        // Send alert to operations team
    }
}
```

### Custom Error Handler

```java
@Service
@Slf4j
public class CustomErrorHandlingConsumer {
    
    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;
    
    @KafkaListener(topics = "orders", groupId = "error-handling-group")
    public void consume(ConsumerRecord<String, OrderEvent> record) {
        try {
            processOrder(record.value());
        } catch (RetryableException e) {
            log.warn("Retryable error, sending to retry topic", e);
            sendToRetryTopic(record);
        } catch (NonRetryableException e) {
            log.error("Non-retryable error, sending to DLT", e);
            sendToDLT(record);
        }
    }
    
    private void sendToRetryTopic(ConsumerRecord<String, OrderEvent> record) {
        kafkaTemplate.send("orders.retry", record.value());
    }
    
    private void sendToDLT(ConsumerRecord<String, OrderEvent> record) {
        kafkaTemplate.send("orders.DLT", record.value());
    }
}
```

---

## 🧪 Testing

### Integration Test

```java
@SpringBootTest
@TestPropertySource(properties = {
    "spring.kafka.bootstrap-servers=${spring.embedded.kafka.brokers}"
})
@EmbeddedKafka(
    partitions = 1,
    topics = {"orders", "orders.DLT"}
)
class KafkaIntegrationTest {
    
    @Autowired
    private KafkaProducerService producerService;
    
    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;
    
    @Autowired
    private EmbeddedKafkaBroker embeddedKafkaBroker;
    
    private Consumer<String, OrderEvent> consumer;
    
    @BeforeEach
    void setUp() {
        Map<String, Object> consumerProps = KafkaTestUtils.consumerProps(
            "test-group",
            "true",
            embeddedKafkaBroker
        );
        consumerProps.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        
        DefaultKafkaConsumerFactory<String, OrderEvent> cf =
            new DefaultKafkaConsumerFactory<>(consumerProps);
        consumer = cf.createConsumer();
        consumer.subscribe(Collections.singleton("orders"));
    }
    
    @Test
    void testSendAndReceive() throws Exception {
        // Given
        OrderEvent order = new OrderEvent(
            "order-123",
            "customer-456",
            99.99,
            "PENDING",
            LocalDateTime.now()
        );
        
        // When
        producerService.sendMessage(order);
        
        // Then
        ConsumerRecord<String, OrderEvent> record = 
            KafkaTestUtils.getSingleRecord(consumer, "orders");
        
        assertThat(record).isNotNull();
        assertThat(record.value().getOrderId()).isEqualTo("order-123");
    }
    
    @AfterEach
    void tearDown() {
        consumer.close();
    }
}
```

### Unit Test with MockBean

```java
@ExtendWith(MockitoExtension.class)
class OrderControllerTest {
    
    @Mock
    private KafkaProducerService producerService;
    
    @InjectMocks
    private OrderController orderController;
    
    @Test
    void testCreateOrder() {
        // Given
        OrderEvent order = new OrderEvent(
            "order-123",
            "customer-456",
            99.99,
            "PENDING",
            LocalDateTime.now()
        );
        
        // When
        ResponseEntity<String> response = orderController.createOrder(order);
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        verify(producerService, times(1)).sendMessage(any(OrderEvent.class));
    }
}
```

---

## 🏭 Production Patterns

### Idempotent Consumer

```java
@Service
@Slf4j
public class IdempotentConsumer {
    
    @Autowired
    private ProcessedMessageRepository repository;
    
    @KafkaListener(topics = "orders", groupId = "idempotent-group")
    @Transactional
    public void consume(ConsumerRecord<String, OrderEvent> record) {
        String messageId = record.key();
        
        // Check if already processed
        if (repository.existsById(messageId)) {
            log.info("Message already processed: {}", messageId);
            return;
        }
        
        // Process message
        processOrder(record.value());
        
        // Mark as processed
        repository.save(new ProcessedMessage(messageId, Instant.now()));
    }
}
```

### Request-Reply Pattern

```java
@Service
@Slf4j
public class RequestReplyService {
    
    @Autowired
    private ReplyingKafkaTemplate<String, OrderEvent, String> replyingTemplate;
    
    public String processOrderSync(OrderEvent order) throws Exception {
        ProducerRecord<String, OrderEvent> record = 
            new ProducerRecord<>("order-requests", order);
        
        RequestReplyFuture<String, OrderEvent, String> future = 
            replyingTemplate.sendAndReceive(record);
        
        ConsumerRecord<String, String> response = 
            future.get(10, TimeUnit.SECONDS);
        
        return response.value();
    }
}

// Reply consumer
@Service
@Slf4j
public class ReplyingConsumer {
    
    @KafkaListener(topics = "order-requests")
    @SendTo
    public String handleRequest(OrderEvent order) {
        log.info("Processing order: {}", order);
        // Process order
        return "Order " + order.getOrderId() + " processed successfully";
    }
}
```

---

## 📊 Monitoring

### Actuator Metrics

```yaml
# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,metrics,prometheus
  metrics:
    export:
      prometheus:
        enabled: true
```

### Custom Metrics

```java
@Service
@Slf4j
public class MetricsCollectorService {
    
    private final Counter messagesProducedCounter;
    private final Counter messagesConsumedCounter;
    private final Timer processingTimer;
    
    public MetricsCollectorService(MeterRegistry meterRegistry) {
        this.messagesProducedCounter = Counter.builder("kafka.messages.produced")
            .description("Number of messages produced")
            .register(meterRegistry);
        
        this.messagesConsumedCounter = Counter.builder("kafka.messages.consumed")
            .description("Number of messages consumed")
            .register(meterRegistry);
        
        this.processingTimer = Timer.builder("kafka.message.processing.time")
            .description("Time taken to process messages")
            .register(meterRegistry);
    }
    
    public void recordProduced() {
        messagesProducedCounter.increment();
    }
    
    public void recordConsumed() {
        messagesConsumedCounter.increment();
    }
    
    public void recordProcessingTime(Runnable task) {
        processingTimer.record(task);
    }
}
```

---

## 🎯 Interview Questions

**Q: How do you handle duplicate messages in Spring Kafka?**

**Answer:**
1. Use idempotent producer (`enable.idempotence=true`)
2. Implement idempotent consumer (check processed message IDs)
3. Use database constraints (unique keys)
4. Store offsets with processed data atomically

**Q: What is the difference between @KafkaListener and KafkaTemplate?**

**Answer:**
- **@KafkaListener:** Consumer annotation for receiving messages
- **KafkaTemplate:** Producer class for sending messages

**Q: How do you achieve exactly-once processing in Spring Kafka?**

**Answer:**
1. Enable transactions on producer
2. Use @Transactional on consumer
3. Commit offsets within same transaction
4. Handle failures with rollback

---

**Master Spring Kafka for production-grade event-driven systems!** 🚀

