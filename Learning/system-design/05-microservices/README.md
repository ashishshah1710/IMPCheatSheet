# 🔧 Microservices Architecture

## Overview
Microservices is an architectural style where applications are built as a collection of small, independent services that communicate over well-defined APIs.

---

## Monolith vs Microservices

### Monolithic Architecture
```
┌─────────────────────────────────┐
│      Single Application         │
│  ┌───────────────────────────┐  │
│  │  User Module              │  │
│  │  Order Module             │  │
│  │  Payment Module           │  │
│  │  Inventory Module         │  │
│  │  Notification Module      │  │
│  └───────────────────────────┘  │
│                                  │
│      Single Database             │
└─────────────────────────────────┘
```

**✅ Advantages:**
- Simple to develop initially
- Easy to test
- Simple deployment
- No network latency between modules

**❌ Disadvantages:**
- Scaling limitations (must scale entire app)
- Single point of failure
- Slow development at scale
- Technology lock-in
- Hard to understand large codebase

---

### Microservices Architecture
```
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│   User   │  │  Order   │  │ Payment  │  │Inventory │
│ Service  │  │ Service  │  │ Service  │  │ Service  │
└────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │             │
  UserDB        OrderDB      PaymentDB      InvDB
```

**✅ Advantages:**
- Independent scaling
- Technology flexibility
- Fault isolation
- Easier to understand (smaller codebases)
- Parallel development
- Independent deployment

**❌ Disadvantages:**
- Distributed system complexity
- Network latency
- Data consistency challenges
- Testing complexity
- Operational overhead
- More moving parts

---

## Microservices Characteristics

### 1. **Single Responsibility**
Each service does one thing well

```
❌ UserOrderPaymentService
✅ UserService
✅ OrderService
✅ PaymentService
```

### 2. **Independently Deployable**
Deploy without affecting other services

```bash
# Deploy only order service
kubectl apply -f order-service-v2.yaml
# Other services unaffected
```

### 3. **Decentralized Data**
Each service owns its database

```
UserService → UserDB
OrderService → OrderDB (can't directly query UserDB)
```

### 4. **Inter-Service Communication**
Services communicate via APIs (REST, gRPC, messaging)

---

## Communication Patterns

### 1. **Synchronous Communication (REST)**

```java
// User Service calls Order Service via REST
@RestController
public class UserController {
    @Autowired
    private RestTemplate restTemplate;
    
    @GetMapping("/users/{id}/orders")
    public List<Order> getUserOrders(@PathVariable Long id) {
        String url = "http://order-service/api/orders?userId=" + id;
        return restTemplate.getForObject(url, List.class);
    }
}
```

**✅ Pros:**
- Simple
- Immediate response
- Easy to understand

**❌ Cons:**
- Tight coupling
- Cascading failures
- Latency accumulation

---

### 2. **Synchronous Communication (gRPC)**

```protobuf
// order.proto
service OrderService {
  rpc GetUserOrders(UserRequest) returns (OrderList);
}

message UserRequest {
  int64 user_id = 1;
}

message OrderList {
  repeated Order orders = 1;
}
```

```java
// Client code
OrderServiceBlockingStub stub = OrderServiceGrpc.newBlockingStub(channel);
OrderList orders = stub.getUserOrders(
    UserRequest.newBuilder().setUserId(123).build()
);
```

**Benefits over REST:**
- Faster (binary protocol)
- Strongly typed (protobuf)
- Bi-directional streaming
- Better for internal services

---

### 3. **Asynchronous Communication (Message Queue)**

```java
// Order Service publishes event
@Service
public class OrderService {
    @Autowired
    private KafkaTemplate<String, OrderEvent> kafka;
    
    public Order createOrder(Order order) {
        Order saved = repository.save(order);
        
        // Publish event (fire and forget)
        OrderEvent event = new OrderEvent(saved.getId(), saved.getUserId());
        kafka.send("order-created", event);
        
        return saved;
    }
}

// Email Service subscribes to event
@Service
public class EmailService {
    @KafkaListener(topics = "order-created")
    public void handleOrderCreated(OrderEvent event) {
        // Send confirmation email
        sendEmail(event.getUserId(), "Order confirmed!");
    }
}
```

**✅ Pros:**
- Loose coupling
- Fault tolerance (retry, dead letter queue)
- Async processing
- Event-driven

**❌ Cons:**
- Eventual consistency
- More complex
- Harder to debug

---

## Service Discovery

### Problem
Services need to find each other dynamically

```
How does User Service know Order Service address?
- Static config: http://192.168.1.10:8080 ❌
- DNS: order-service.company.com ❌ (manual updates)
- Service Discovery: ✅
```

### Solution: Service Registry

```
┌──────────────────┐
│ Service Registry │  (Eureka, Consul, etcd)
│   User: 10.0.1.5 │
│   Order: 10.0.2.3│
└────────┬─────────┘
         │
    ┌────┴────┐
    ↓         ↓
UserService OrderService
(Register)  (Register & Discover)
```

### Example: Spring Cloud Eureka

```java
// Service Registration
@SpringBootApplication
@EnableEurekaClient
public class OrderServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(OrderServiceApplication.class, args);
    }
}

// Service Discovery
@Autowired
private DiscoveryClient discoveryClient;

public String getOrderServiceUrl() {
    List<ServiceInstance> instances = 
        discoveryClient.getInstances("order-service");
    return instances.get(0).getUri().toString();
}
```

---

## API Gateway Pattern

### Without API Gateway
```
Mobile App → User Service
          → Order Service
          → Payment Service
          → Inventory Service
(Client knows all services)
```

### With API Gateway
```
Mobile App → API Gateway → User Service
                         → Order Service
                         → Payment Service
                         → Inventory Service
(Single entry point)
```

### API Gateway Responsibilities

1. **Routing**: Forward requests to appropriate service
2. **Authentication/Authorization**: Centralized security
3. **Rate Limiting**: Prevent abuse
4. **Load Balancing**: Distribute load
5. **Caching**: Cache responses
6. **Logging/Monitoring**: Centralized logging
7. **Protocol Translation**: REST to gRPC

### Example: Spring Cloud Gateway

```java
@Configuration
public class GatewayConfig {
    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
            .route("user-service", r -> r
                .path("/api/users/**")
                .filters(f -> f
                    .stripPrefix(1)
                    .addRequestHeader("X-Gateway", "true"))
                .uri("lb://user-service"))
            
            .route("order-service", r -> r
                .path("/api/orders/**")
                .filters(f -> f.circuitBreaker(c -> c
                    .setName("orderCircuitBreaker")
                    .setFallbackUri("/fallback/orders")))
                .uri("lb://order-service"))
            
            .build();
    }
}
```

---

## Circuit Breaker Pattern

### Problem
When a service fails, cascading failures can bring down entire system

### Solution
```
Normal State:          Circuit Open:         Circuit Half-Open:
Request → Service      Request → Fallback    Request → Service (test)
  ✓                      ❌                     ? (if success, close)
```

### Example: Resilience4j

```java
@Service
public class OrderService {
    @CircuitBreaker(name = "paymentService", fallbackMethod = "paymentFallback")
    public PaymentResponse processPayment(Payment payment) {
        return paymentClient.charge(payment);
    }
    
    // Fallback method
    private PaymentResponse paymentFallback(Payment payment, Exception ex) {
        log.error("Payment service down, using fallback", ex);
        return new PaymentResponse("PENDING", "Will retry later");
    }
}
```

**Configuration:**
```yaml
resilience4j.circuitbreaker:
  instances:
    paymentService:
      slidingWindowSize: 10
      failureRateThreshold: 50
      waitDurationInOpenState: 10s
      permittedNumberOfCallsInHalfOpenState: 3
```

---

## Data Management Patterns

### 1. **Database per Service** ⭐

```
UserService → UserDB
OrderService → OrderDB
PaymentService → PaymentDB
```

**✅ Pros:**
- Service independence
- Technology choice per service
- Loose coupling

**❌ Cons:**
- No joins across services
- Distributed transactions
- Data duplication

---

### 2. **Saga Pattern** (Distributed Transactions)

#### Problem
```
CreateOrder → ChargePayment → UpdateInventory
What if Payment succeeds but Inventory fails? ❌
```

#### Solution 1: Choreography (Event-Based)

```
OrderService:
  ① Create Order (PENDING)
  ② Publish OrderCreated event

PaymentService:
  ③ Listen OrderCreated
  ④ Charge payment
  ⑤ Publish PaymentCompleted event

InventoryService:
  ⑥ Listen PaymentCompleted
  ⑦ Update inventory
  ⑧ Publish InventoryUpdated event

OrderService:
  ⑨ Listen InventoryUpdated
  ⑩ Update Order (CONFIRMED)
```

**Compensating Transaction (Rollback):**
```
If Inventory fails:
  InventoryService → Publish InventoryFailed
  PaymentService → Listen InventoryFailed → Refund
  OrderService → Listen PaymentRefunded → Cancel Order
```

#### Solution 2: Orchestration

```java
@Service
public class OrderSaga {
    public void executeOrderSaga(Order order) {
        try {
            // Step 1: Create order
            orderService.createOrder(order);
            
            // Step 2: Charge payment
            paymentService.charge(order.getPayment());
            
            // Step 3: Update inventory
            inventoryService.reserve(order.getItems());
            
            // Success - confirm order
            orderService.confirmOrder(order.getId());
            
        } catch (PaymentException e) {
            // Compensate: Cancel order
            orderService.cancelOrder(order.getId());
            throw e;
            
        } catch (InventoryException e) {
            // Compensate: Refund + Cancel
            paymentService.refund(order.getPayment());
            orderService.cancelOrder(order.getId());
            throw e;
        }
    }
}
```

---

### 3. **CQRS (Command Query Responsibility Segregation)**

```
          Commands (Write)
               ↓
          Write Service
               ↓
          Event Stream (Kafka)
               ↓
        ┌──────┴──────┐
        ↓             ↓
   Read Service1  Read Service2
   (User View)    (Analytics View)
        ↓             ↓
      ReadDB1      ReadDB2
```

**Benefits:**
- Optimized read/write models
- Independent scaling
- Multiple read views

---

### 4. **Event Sourcing**

Instead of storing current state, store all events:

```java
// Traditional
UserTable: { id: 1, name: "John", balance: 100 }

// Event Sourcing
Events:
  1. UserCreated(id=1, name="John")
  2. BalanceAdded(id=1, amount=100)
  3. BalanceDeducted(id=1, amount=20)
  4. BalanceAdded(id=1, amount=20)

Current State: Replay all events → balance=100
```

**Benefits:**
- Complete audit trail
- Time travel (rebuild any past state)
- Event-driven architecture

**Challenges:**
- Complexity
- Storage overhead
- Schema evolution

---

## Security in Microservices

### 1. **API Gateway Authentication**
```
Client → API Gateway (JWT validation) → Services
```

### 2. **Service-to-Service Authentication**

```java
// Option 1: JWT passed from Gateway
@GetMapping("/orders")
public List<Order> getOrders(@RequestHeader("Authorization") String jwt) {
    // Validate JWT
}

// Option 2: mTLS (Mutual TLS)
// Services authenticate each other with certificates
```

### 3. **OAuth 2.0 / OpenID Connect**

```
User → Login → Auth Server → JWT Token
       ↓
   API Gateway (validate token)
       ↓
   Microservices (validate token)
```

---

## Observability (Monitoring & Logging)

### 1. **Distributed Tracing**

```
Request ID: abc-123
┌─────────────────────────────────────────┐
│ API Gateway (100ms)                     │
│   ├─ User Service (30ms)                │
│   └─ Order Service (50ms)               │
│       └─ Payment Service (40ms) ← Slow! │
└─────────────────────────────────────────┘
```

**Tools:**
- **Jaeger**
- **Zipkin**
- **AWS X-Ray**

**Example:**
```java
@Autowired
private Tracer tracer;

public Order createOrder(Order order) {
    Span span = tracer.buildSpan("createOrder").start();
    try {
        // Business logic
        return orderRepository.save(order);
    } finally {
        span.finish();
    }
}
```

### 2. **Centralized Logging**

```
All Services → Log Aggregator (ELK/Splunk) → Dashboard
```

**Structured Logging:**
```java
log.info("Order created", 
    kv("orderId", order.getId()),
    kv("userId", order.getUserId()),
    kv("amount", order.getTotal()));
```

### 3. **Metrics & Alerting**

```java
@Timed(value = "order.creation.time")
@Counted(value = "order.creation.count")
public Order createOrder(Order order) {
    // Business logic
}
```

**Tools:**
- **Prometheus + Grafana**
- **Datadog**
- **New Relic**

---

## Common Microservices Patterns

| Pattern | Purpose |
|---------|---------|
| **API Gateway** | Single entry point |
| **Service Discovery** | Dynamic service location |
| **Circuit Breaker** | Fault tolerance |
| **Saga** | Distributed transactions |
| **CQRS** | Separate read/write models |
| **Event Sourcing** | Store all events |
| **Sidecar** | Auxiliary process (logging, monitoring) |
| **Strangler Fig** | Gradual migration from monolith |
| **Bulkhead** | Isolate failures |
| **Rate Limiting** | Prevent abuse |

---

## Interview Questions

1. **Monolith vs Microservices: When to use each?**
2. **How do microservices communicate?**
3. **What is the API Gateway pattern?**
4. **How do you handle distributed transactions?**
5. **Explain the Circuit Breaker pattern**
6. **How do you maintain data consistency across services?**
7. **How do you handle service discovery?**
8. **What are the challenges of microservices?**

---

## Best Practices

✅ Start with a monolith, migrate to microservices when needed  
✅ Define clear service boundaries  
✅ Use API Gateway for client-facing APIs  
✅ Implement circuit breakers for resilience  
✅ Use async communication where possible  
✅ Implement distributed tracing  
✅ Automate deployment (CI/CD)  
✅ Monitor everything  
✅ Design for failure  

---

## Next Steps

- **Real-World Systems** → [06-real-world-systems](../06-real-world-systems/README.md)
- **Case Studies** → [case-studies](../case-studies/README.md)
- **Interview Questions** → [interview-questions](../interview-questions/README.md)

---

**💡 Pro Tip**: Don't start with microservices! Build a monolith first, identify boundaries, then extract services when you have a clear reason to do so.

