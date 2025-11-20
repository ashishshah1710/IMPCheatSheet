# ☁️ Microservices Architecture

**Advanced: Building Microservices with Spring Boot**

---

## 📖 Overview

Learn how to build production-ready microservices using Spring Cloud. Master service discovery, API Gateway, configuration management, circuit breakers, and distributed tracing.

---

## 🎯 Learning Objectives

✅ Microservices architecture principles  
✅ Service discovery (Eureka, Consul)  
✅ API Gateway (Spring Cloud Gateway)  
✅ Centralized configuration (Config Server)  
✅ Circuit breaker pattern (Resilience4j)  
✅ Distributed tracing (Sleuth, Zipkin)  
✅ Load balancing  
✅ Service-to-service communication  

---

## 📚 Core Topics

### 1. Service Discovery (Eureka)

**Eureka Server:**

```java
@SpringBootApplication
@EnableEurekaServer
public class EurekaServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(EurekaServerApplication.class, args);
    }
}
```

```yaml
# Eureka Server Configuration
server:
  port: 8761

eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
  server:
    enable-self-preservation: false
```

**Eureka Client:**

```java
@SpringBootApplication
@EnableDiscoveryClient
public class UserServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserServiceApplication.class, args);
    }
}
```

```yaml
# Eureka Client Configuration
spring:
  application:
    name: user-service

eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
    fetch-registry: true
    register-with-eureka: true
  instance:
    prefer-ip-address: true
    instance-id: ${spring.application.name}:${random.value}
```

---

### 2. API Gateway (Spring Cloud Gateway)

**Configuration:**

```java
@SpringBootApplication
public class ApiGatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(ApiGatewayApplication.class, args);
    }
}
```

```yaml
spring:
  application:
    name: api-gateway
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/api/users/**
          filters:
            - RewritePath=/api/users/(?<segment>.*), /${segment}
            - name: CircuitBreaker
              args:
                name: userServiceCircuitBreaker
                fallbackUri: forward:/fallback/users
        
        - id: order-service
          uri: lb://order-service
          predicates:
            - Path=/api/orders/**
          filters:
            - RewritePath=/api/orders/(?<segment>.*), /${segment}
            - name: RateLimiter
              args:
                redis-rate-limiter.replenishRate: 10
                redis-rate-limiter.burstCapacity: 20
      
      default-filters:
        - name: GlobalFilter
        - AddResponseHeader=X-Response-Time, #{T(System).currentTimeMillis()}

eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
```

**Custom Filters:**

```java
@Component
public class AuthenticationFilter extends AbstractGatewayFilterFactory<AuthenticationFilter.Config> {
    
    @Autowired
    private JwtService jwtService;
    
    public AuthenticationFilter() {
        super(Config.class);
    }
    
    @Override
    public GatewayFilter apply(Config config) {
        return (exchange, chain) -> {
            ServerHttpRequest request = exchange.getRequest();
            
            if (!request.getHeaders().containsKey(HttpHeaders.AUTHORIZATION)) {
                throw new RuntimeException("Missing authorization header");
            }
            
            String authHeader = request.getHeaders().get(HttpHeaders.AUTHORIZATION).get(0);
            String token = authHeader.substring(7);
            
            try {
                jwtService.validateToken(token);
            } catch (Exception e) {
                throw new RuntimeException("Invalid token");
            }
            
            return chain.filter(exchange);
        };
    }
    
    public static class Config {
    }
}
```

---

### 3. Config Server

**Config Server:**

```java
@SpringBootApplication
@EnableConfigServer
public class ConfigServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(ConfigServerApplication.class, args);
    }
}
```

```yaml
server:
  port: 8888

spring:
  application:
    name: config-server
  cloud:
    config:
      server:
        git:
          uri: https://github.com/yourorg/config-repo
          default-label: main
          search-paths:
            - '{application}'
          clone-on-start: true
        # Or use native file system
        native:
          search-locations: classpath:/config
```

**Config Client:**

```yaml
spring:
  application:
    name: user-service
  config:
    import: configserver:http://localhost:8888
  cloud:
    config:
      fail-fast: true
      retry:
        max-attempts: 6
        initial-interval: 1000
        multiplier: 1.1
```

**Refresh Configuration:**

```java
@RestController
@RefreshScope
public class UserController {
    
    @Value("${user.service.message}")
    private String message;
    
    @GetMapping("/message")
    public String getMessage() {
        return message;
    }
}
```

```bash
# Refresh configuration without restart
curl -X POST http://localhost:8080/actuator/refresh
```

---

### 4. Circuit Breaker (Resilience4j)

**Configuration:**

```yaml
resilience4j:
  circuitbreaker:
    instances:
      userService:
        register-health-indicator: true
        sliding-window-size: 10
        minimum-number-of-calls: 5
        permitted-number-of-calls-in-half-open-state: 3
        automatic-transition-from-open-to-half-open-enabled: true
        wait-duration-in-open-state: 10s
        failure-rate-threshold: 50
        slow-call-rate-threshold: 100
        slow-call-duration-threshold: 2s
  
  retry:
    instances:
      userService:
        max-attempts: 3
        wait-duration: 1s
        enable-exponential-backoff: true
        exponential-backoff-multiplier: 2
  
  bulkhead:
    instances:
      userService:
        max-concurrent-calls: 10
        max-wait-duration: 1s
  
  timelimiter:
    instances:
      userService:
        timeout-duration: 3s
```

**Usage:**

```java
@Service
@Slf4j
public class OrderService {
    
    private final WebClient webClient;
    
    @CircuitBreaker(name = "userService", fallbackMethod = "getUserFallback")
    @Retry(name = "userService")
    @Bulkhead(name = "userService")
    @TimeLimiter(name = "userService")
    public Mono<UserDTO> getUserById(Long userId) {
        log.info("Calling user-service for userId: {}", userId);
        
        return webClient
            .get()
            .uri("http://user-service/api/users/{id}", userId)
            .retrieve()
            .bodyToMono(UserDTO.class);
    }
    
    private Mono<UserDTO> getUserFallback(Long userId, Exception ex) {
        log.error("Fallback method called for userId: {}, error: {}", userId, ex.getMessage());
        
        return Mono.just(UserDTO.builder()
            .id(userId)
            .name("Unknown User")
            .email("unknown@example.com")
            .build());
    }
}
```

---

### 5. Distributed Tracing (Sleuth & Zipkin)

**Configuration:**

```yaml
spring:
  sleuth:
    sampler:
      probability: 1.0
  zipkin:
    base-url: http://localhost:9411
    sender:
      type: web
```

**Custom Span:**

```java
@Service
@Slf4j
public class OrderService {
    
    private final Tracer tracer;
    
    public Order createOrder(CreateOrderRequest request) {
        Span span = tracer.nextSpan().name("createOrder").start();
        
        try (Tracer.SpanInScope ws = tracer.withSpan(span)) {
            span.tag("order.type", request.getType());
            span.tag("order.items", String.valueOf(request.getItems().size()));
            
            log.info("Creating order with traceId: {}", span.context().traceId());
            
            // Process order
            Order order = processOrder(request);
            
            span.tag("order.id", order.getId().toString());
            span.annotate("order.created");
            
            return order;
        } finally {
            span.end();
        }
    }
}
```

---

### 6. Service Communication

**Using WebClient:**

```java
@Configuration
public class WebClientConfig {
    
    @Bean
    @LoadBalanced
    public WebClient.Builder webClientBuilder() {
        return WebClient.builder()
            .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
            .filter(logRequest())
            .filter(logResponse());
    }
    
    private ExchangeFilterFunction logRequest() {
        return ExchangeFilterFunction.ofRequestProcessor(clientRequest -> {
            log.info("Request: {} {}", clientRequest.method(), clientRequest.url());
            return Mono.just(clientRequest);
        });
    }
    
    private ExchangeFilterFunction logResponse() {
        return ExchangeFilterFunction.ofResponseProcessor(clientResponse -> {
            log.info("Response status: {}", clientResponse.statusCode());
            return Mono.just(clientResponse);
        });
    }
}

@Service
public class OrderService {
    
    private final WebClient.Builder webClientBuilder;
    
    public Mono<UserDTO> getUserById(Long userId) {
        return webClientBuilder.build()
            .get()
            .uri("http://user-service/api/users/{id}", userId)
            .retrieve()
            .onStatus(HttpStatus::is4xxClientError, response -> 
                Mono.error(new ResourceNotFoundException("User not found")))
            .onStatus(HttpStatus::is5xxServerError, response ->
                Mono.error(new ServiceUnavailableException("User service unavailable")))
            .bodyToMono(UserDTO.class);
    }
}
```

**Using Feign Client:**

```java
@FeignClient(name = "user-service", fallback = UserServiceFallback.class)
public interface UserServiceClient {
    
    @GetMapping("/api/users/{id}")
    UserDTO getUserById(@PathVariable Long id);
    
    @PostMapping("/api/users")
    UserDTO createUser(@RequestBody CreateUserRequest request);
    
    @GetMapping("/api/users")
    List<UserDTO> getAllUsers(@RequestParam(required = false) String name);
}

@Component
public class UserServiceFallback implements UserServiceClient {
    
    @Override
    public UserDTO getUserById(Long id) {
        return UserDTO.builder()
            .id(id)
            .name("Unknown User")
            .build();
    }
    
    @Override
    public UserDTO createUser(CreateUserRequest request) {
        throw new ServiceUnavailableException("User service is unavailable");
    }
    
    @Override
    public List<UserDTO> getAllUsers(String name) {
        return Collections.emptyList();
    }
}
```

---

### 7. Saga Pattern

**Choreography-Based Saga:**

```java
@Service
@Slf4j
public class OrderService {
    
    @Autowired
    private KafkaTemplate<String, OrderEvent> kafkaTemplate;
    
    @Transactional
    public Order createOrder(CreateOrderRequest request) {
        // Create order
        Order order = orderRepository.save(createOrderEntity(request));
        
        // Publish OrderCreated event
        OrderEvent event = OrderEvent.builder()
            .orderId(order.getId())
            .userId(order.getUserId())
            .amount(order.getTotalAmount())
            .type(EventType.ORDER_CREATED)
            .build();
        
        kafkaTemplate.send("order-events", event);
        log.info("Published OrderCreated event for orderId: {}", order.getId());
        
        return order;
    }
    
    @KafkaListener(topics = "payment-events", groupId = "order-service")
    public void handlePaymentEvent(PaymentEvent event) {
        if (event.getType() == EventType.PAYMENT_SUCCESS) {
            Order order = orderRepository.findById(event.getOrderId())
                .orElseThrow(() -> new ResourceNotFoundException("Order not found"));
            
            order.setStatus(OrderStatus.CONFIRMED);
            orderRepository.save(order);
            
            log.info("Order confirmed: {}", order.getId());
        } else if (event.getType() == EventType.PAYMENT_FAILED) {
            // Compensating transaction
            Order order = orderRepository.findById(event.getOrderId())
                .orElseThrow(() -> new ResourceNotFoundException("Order not found"));
            
            order.setStatus(OrderStatus.CANCELLED);
            orderRepository.save(order);
            
            log.warn("Order cancelled due to payment failure: {}", order.getId());
        }
    }
}
```

---

## 🎯 Interview Questions

**Q1: What is service discovery and why is it needed?**

A: Service discovery allows services to find and communicate with each other without hard-coding hostname/port. It's needed because:
- Dynamic IP addresses in cloud
- Auto-scaling adds/removes instances
- Service instances can fail

**Q2: Explain Circuit Breaker pattern**

A: Circuit breaker prevents cascading failures:
- **Closed**: Normal operation
- **Open**: Fast fail without calling service (after threshold)
- **Half-Open**: Test if service recovered

**Q3: Saga pattern vs Distributed transactions?**

A:
- **Distributed transactions**: 2PC protocol, requires locks, not scalable
- **Saga**: Sequence of local transactions, eventual consistency, compensating transactions

**Q4: How do you handle configuration in microservices?**

A:
- Centralized config server
- Environment-specific configs
- Refresh without restart using @RefreshScope
- Secrets in vault/secret managers

---

## ✅ Practice Checklist

- [ ] Set up Eureka Server and clients
- [ ] Configure API Gateway with routing
- [ ] Implement Config Server
- [ ] Add Circuit Breaker with fallbacks
- [ ] Set up distributed tracing
- [ ] Implement service communication
- [ ] Create Saga pattern example
- [ ] Set up message broker (Kafka/RabbitMQ)
- [ ] Implement load balancing
- [ ] Deploy microservices with Docker Compose

---

**👉 [Interview Questions →](../interview-questions/README.md)**



