# 💼 Spring Boot Interview Questions

**Comprehensive Interview Preparation for 3.5+ Years Experience**

---

## 📖 Overview

This section contains real interview questions asked at top companies, organized by difficulty and topic. Practice these to ace your Spring Boot interviews!

---

## 🎯 Question Categories

1. [Fundamentals](#fundamentals)
2. [REST APIs](#rest-apis)
3. [Data & JPA](#data--jpa)
4. [Security](#security)
5. [Microservices](#microservices)
6. [Production & DevOps](#production--devops)
7. [Scenario-Based](#scenario-based)
8. [System Design](#system-design)

---

## Fundamentals

### Basic Level

**Q1: What is Spring Boot? How is it different from Spring Framework?**

**Answer:**
Spring Boot is an extension of Spring Framework that simplifies application setup and development.

| Aspect | Spring Framework | Spring Boot |
|--------|-----------------|-------------|
| Configuration | XML or extensive Java config | Auto-configuration |
| Dependency Management | Manual version management | Starter dependencies with BOM |
| Embedded Server | Requires external server | Embedded Tomcat/Jetty/Undertow |
| Production Features | Manual setup | Actuator built-in |
| Development Time | Hours/Days | Minutes |

---

**Q2: Explain @SpringBootApplication annotation**

**Answer:**
```java
@SpringBootApplication is a combination of three annotations:

@SpringBootApplication
// Equivalent to:
@Configuration          // Marks class as configuration source
@EnableAutoConfiguration // Enables auto-configuration
@ComponentScan          // Scans for components in package and sub-packages
```

---

**Q3: How does Spring Boot auto-configuration work?**

**Answer:**
Auto-configuration works through:

1. `@EnableAutoConfiguration` triggers the process
2. Reads `META-INF/spring.factories` to find auto-configuration classes
3. Uses `@Conditional` annotations to determine applicability
4. Checks classpath for required classes
5. Creates beans if conditions are met

Example:
```java
@Configuration
@ConditionalOnClass(DataSource.class)
@ConditionalOnMissingBean(DataSource.class)
public class DataSourceAutoConfiguration {
    @Bean
    public DataSource dataSource() {
        // Create DataSource
    }
}
```

---

**Q4: What are Spring Boot Starters?**

**Answer:**
Starters are dependency descriptors that:
- Provide all necessary dependencies for a feature
- Include compatible versions
- Bring transitive dependencies
- Provide sensible defaults

Example: `spring-boot-starter-web` includes:
- Spring MVC
- Embedded Tomcat
- Jackson for JSON
- Validation
- Logging

---

**Q5: How do you disable specific auto-configuration?**

**Answer:**
Three methods:

```java
// Method 1: Using @SpringBootApplication
@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})

// Method 2: Using application.properties
spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration

// Method 3: Using @EnableAutoConfiguration
@EnableAutoConfiguration(exclude = {DataSourceAutoConfiguration.class})
```

---

### Advanced Level

**Q6: Explain the property source precedence in Spring Boot**

**Answer:**
Properties are resolved in this order (highest priority first):

1. Command line arguments
2. SPRING_APPLICATION_JSON
3. ServletConfig/ServletContext init parameters
4. JNDI attributes
5. Java System properties
6. OS environment variables
7. Profile-specific properties outside jar
8. Profile-specific properties inside jar
9. Application properties outside jar
10. Application properties inside jar
11. @PropertySource
12. Default properties

---

**Q7: How would you create a custom Spring Boot starter?**

**Answer:**

```java
// 1. Create auto-configuration
@Configuration
@ConditionalOnClass(MyService.class)
@EnableConfigurationProperties(MyServiceProperties.class)
public class MyServiceAutoConfiguration {
    @Bean
    @ConditionalOnMissingBean
    public MyService myService(MyServiceProperties props) {
        return new MyService(props);
    }
}

// 2. Create properties
@ConfigurationProperties(prefix = "myservice")
public class MyServiceProperties {
    private String apiKey;
    private int timeout = 30;
}

// 3. Create spring.factories
// META-INF/spring.factories
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.example.MyServiceAutoConfiguration

// 4. Create starter POM
<artifactId>myservice-spring-boot-starter</artifactId>
```

---

**Q8: What is Spring Boot DevTools and how does it work?**

**Answer:**
DevTools enhances development experience with:
- **Automatic restart**: Monitors classpath changes
- **LiveReload**: Refreshes browser automatically
- **Property defaults**: Dev-friendly configurations
- **Remote debugging**: Debug applications remotely

How it works:
- Uses two classloaders: base (dependencies) and restart (application code)
- Only restart classloader reloads on changes
- Much faster than full restart

---

## REST APIs

**Q9: What are REST principles?**

**Answer:**
REST (Representational State Transfer) principles:

1. **Client-Server**: Separation of concerns
2. **Stateless**: Each request contains all needed information
3. **Cacheable**: Responses marked as cacheable or not
4. **Uniform Interface**: Standardized communication (URIs, HTTP methods)
5. **Layered System**: Client can't tell if connected directly
6. **Code on Demand** (optional): Server can send executable code

---

**Q10: Explain idempotency in REST APIs**

**Answer:**
Idempotent operations produce same result when called multiple times.

| Method | Idempotent | Example |
|--------|------------|---------|
| GET | Yes | Always returns same data |
| PUT | Yes | Replace resource (same result) |
| DELETE | Yes | Already deleted = same state |
| POST | No | Creates new resource each time |
| PATCH | No | Can produce different results |

---

**Q11: How do you version REST APIs?**

**Answer:**
Three main strategies:

```java
// 1. URI Versioning (most common)
@GetMapping("/api/v1/users/{id}")
@GetMapping("/api/v2/users/{id}")

// 2. Header Versioning
@GetMapping(value = "/api/users/{id}", headers = "X-API-VERSION=1")
@GetMapping(value = "/api/users/{id}", headers = "X-API-VERSION=2")

// 3. Media Type Versioning
@GetMapping(value = "/api/users/{id}", produces = "application/vnd.company.v1+json")
@GetMapping(value = "/api/users/{id}", produces = "application/vnd.company.v2+json")
```

**Best Practice**: URI versioning for simplicity and visibility

---

**Q12: How do you handle exceptions globally in Spring Boot?**

**Answer:**

```java
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(
            ResourceNotFoundException ex, WebRequest request) {
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.NOT_FOUND.value())
            .error("Not Found")
            .message(ex.getMessage())
            .path(request.getDescription(false))
            .build();
        
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationException(
            MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(
                FieldError::getField,
                FieldError::getDefaultMessage
            ));
        
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.BAD_REQUEST.value())
            .error("Validation Failed")
            .errors(errors)
            .build();
        
        return ResponseEntity.badRequest().body(error);
    }
}
```

---

## Data & JPA

**Q13: What is the N+1 query problem? How do you solve it?**

**Answer:**
N+1 happens when:
- 1 query fetches parent entities
- N additional queries fetch related entities (one per parent)

**Problem:**
```java
List<Order> orders = orderRepository.findAll(); // 1 query
for (Order order : orders) {
    order.getUser().getName(); // N queries
}
```

**Solutions:**

```java
// Solution 1: JOIN FETCH
@Query("SELECT o FROM Order o JOIN FETCH o.user")
List<Order> findAllWithUser();

// Solution 2: @EntityGraph
@EntityGraph(attributePaths = {"user", "items"})
List<Order> findAll();

// Solution 3: @BatchSize
@Entity
public class Order {
    @ManyToOne(fetch = FetchType.LAZY)
    @BatchSize(size = 10)
    private User user;
}
```

---

**Q14: Explain transaction propagation types**

**Answer:**

| Propagation | Behavior |
|------------|----------|
| **REQUIRED** (default) | Use existing transaction, create if none |
| **REQUIRES_NEW** | Always create new transaction, suspend existing |
| **SUPPORTS** | Use existing if available, non-transactional otherwise |
| **NOT_SUPPORTED** | Execute non-transactionally, suspend existing |
| **MANDATORY** | Must have existing transaction, throw exception if none |
| **NEVER** | Must not run in transaction, throw exception if exists |
| **NESTED** | Execute in nested transaction if one exists |

---

**Q15: Difference between @OneToMany and @ManyToOne?**

**Answer:**

```java
// @OneToMany: Parent side (does NOT own FK)
@Entity
public class User {
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL)
    private List<Order> orders;
}

// @ManyToOne: Child side (OWNS the FK)
@Entity
public class Order {
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id") // FK column
    private User user;
}
```

**Best Practice**: Always define relationship on both sides with `mappedBy` on parent.

---

**Q16: How do you implement soft delete in JPA?**

**Answer:**

```java
@Entity
@SQLDelete(sql = "UPDATE users SET deleted_at = NOW() WHERE id = ?")
@Where(clause = "deleted_at IS NULL")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "deleted_at")
    private LocalDateTime deletedAt;
}

// Repository
public interface UserRepository extends JpaRepository<User, Long> {
    // Only finds non-deleted users
    List<User> findAll();
    
    // Find including deleted
    @Query("SELECT u FROM User u")
    List<User> findAllIncludingDeleted();
}
```

---

## Security

**Q17: How does JWT authentication work?**

**Answer:**

1. **User Login**:
   - User sends credentials
   - Server validates
   - Server creates JWT token
   - Token returned to client

2. **Subsequent Requests**:
   - Client includes token in Authorization header
   - Server validates token (signature, expiration)
   - Extracts user info from token
   - Processes request

3. **JWT Structure**:
   - Header: Algorithm and token type
   - Payload: Claims (user data)
   - Signature: Verification

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.  <- Header
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.  <- Payload
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c  <- Signature
```

---

**Q18: Difference between @PreAuthorize and @Secured?**

**Answer:**

| Aspect | @PreAuthorize | @Secured |
|--------|---------------|----------|
| SpEL Support | Yes | No |
| Flexibility | High | Low |
| Expression | Complex expressions | Role names only |
| Example | `@PreAuthorize("hasRole('ADMIN') or #id == authentication.principal.id")` | `@Secured("ROLE_ADMIN")` |

**Recommendation**: Use @PreAuthorize for flexibility

---

**Q19: How do you implement OAuth2 in Spring Boot?**

**Answer:**

```yaml
# Configuration
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            client-id: ${GOOGLE_CLIENT_ID}
            client-secret: ${GOOGLE_CLIENT_SECRET}
            scope: profile, email
          github:
            client-id: ${GITHUB_CLIENT_ID}
            client-secret: ${GITHUB_CLIENT_SECRET}
            scope: read:user, user:email
```

```java
@Configuration
@EnableWebSecurity
public class OAuth2SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/", "/login/**").permitAll()
                .anyRequest().authenticated()
            )
            .oauth2Login(oauth2 -> oauth2
                .loginPage("/login")
                .defaultSuccessUrl("/dashboard")
                .failureUrl("/login?error=true")
                .userInfoEndpoint(userInfo -> userInfo
                    .userService(customOAuth2UserService())
                )
            );
        
        return http.build();
    }
}
```

---

## Microservices

**Q20: Explain Service Discovery**

**Answer:**
Service discovery allows services to find each other without hardcoded addresses.

**Types:**
1. **Client-Side** (Eureka, Consul):
   - Client queries registry
   - Client chooses instance
   - Direct communication

2. **Server-Side** (Kubernetes, AWS ELB):
   - Load balancer queries registry
   - LB routes request
   - Transparent to client

**Example with Eureka:**
```yaml
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
    fetch-registry: true
    register-with-eureka: true
```

---

**Q21: What is Circuit Breaker pattern?**

**Answer:**
Circuit breaker prevents cascading failures by monitoring service calls.

**States:**
1. **CLOSED**: Normal operation
   - Calls go through
   - Counts failures

2. **OPEN**: Service unavailable
   - Fast fail without calling service
   - After threshold reached

3. **HALF_OPEN**: Testing recovery
   - Allow limited calls
   - Close if successful, Open if failed

```java
@CircuitBreaker(name = "userService", fallbackMethod = "getUserFallback")
public User getUserById(Long id) {
    return restTemplate.getForObject("/users/" + id, User.class);
}

public User getUserFallback(Long id, Exception ex) {
    return User.builder().id(id).name("Unknown").build();
}
```

---

**Q22: Saga Pattern: Choreography vs Orchestration?**

**Answer:**

**Choreography** (Event-Based):
- Services publish/subscribe to events
- No central coordinator
- Decoupled
- Complex to track

```java
// Order Service
orderCreated -> publish OrderCreatedEvent
listen PaymentSuccessEvent -> confirm order

// Payment Service  
listen OrderCreatedEvent -> process payment
paymentSuccess -> publish PaymentSuccessEvent
```

**Orchestration** (Coordinator):
- Central coordinator manages flow
- Easy to track
- Single point of failure

```java
// Saga Orchestrator
1. Create order
2. Process payment
3. Update inventory
4. Send notification
// If any fails, trigger compensating transactions
```

---

## Production & DevOps

**Q23: How do you monitor Spring Boot applications?**

**Answer:**

1. **Spring Boot Actuator**: Health, metrics, info endpoints

2. **Prometheus + Grafana**:
```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  metrics:
    export:
      prometheus:
        enabled: true
```

3. **ELK Stack**: Centralized logging

4. **APM Tools**: New Relic, Datadog, Dynatrace

5. **Distributed Tracing**: Sleuth + Zipkin

---

**Q24: How do you optimize Spring Boot application performance?**

**Answer:**

1. **Lazy Initialization**:
```properties
spring.main.lazy-initialization=true
```

2. **Connection Pooling**:
```yaml
spring:
  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
```

3. **Caching**:
```java
@Cacheable(value = "users", key = "#id")
public User getUserById(Long id)
```

4. **Async Processing**:
```java
@Async
public CompletableFuture<Result> processAsync()
```

5. **Query Optimization**: Solve N+1, use projections

6. **JVM Tuning**: Heap size, GC settings

---

## Scenario-Based

**Q25: Application is slow to start. How do you diagnose and fix?**

**Answer:**

**Diagnosis:**
```bash
# Enable debug logging
java -jar app.jar --debug

# Check auto-configuration report
java -jar app.jar --debug 2>&1 | grep "CONDITIONS EVALUATION REPORT"

# Profile startup
-Dspring.jmx.enabled=true
```

**Solutions:**
1. Lazy initialization
2. Exclude unnecessary auto-configurations
3. Profile-specific beans
4. Optimize bean creation

---

**Q26: How do you handle database migrations in production?**

**Answer:**

Using Flyway:

1. **Never modify existing migrations**
2. **Always create new migration files**
3. **Test on staging first**
4. **Have rollback plan**

```sql
-- V1__create_users.sql
CREATE TABLE users (...);

-- V2__add_email_to_users.sql (NEW FILE)
ALTER TABLE users ADD COLUMN email VARCHAR(255);

-- Never modify V1 after deployment!
```

**Best Practices:**
- Version control migrations
- Baseline on existing DB
- Keep migrations small
- Document complex migrations

---

**Q27: API is getting too many requests. How do you handle it?**

**Answer:**

1. **Rate Limiting**:
```java
@Bean
public RateLimiter rateLimiter() {
    return RateLimiter.create(100); // 100 requests/second
}
```

2. **Caching**: Cache frequent requests

3. **Async Processing**: Queue requests

4. **Load Balancing**: Scale horizontally

5. **API Gateway**: Throttling at gateway level

6. **Database**: Read replicas, connection pooling

---

## System Design

**Q28: Design a URL Shortener Service**

**Answer:**

**Requirements:**
- Shorten long URLs
- Redirect to original URL
- Track analytics
- Handle high traffic

**Architecture:**
```
API Gateway
↓
URL Service (Spring Boot)
↓
Redis (Cache) + PostgreSQL (Storage)
↓
Analytics Service (Kafka)
```

**Key Design Decisions:**
- Base62 encoding for short URLs
- Distributed cache for hot URLs
- Async analytics processing
- Database sharding by URL hash

---

## ✅ Preparation Tips

1. **Understand Concepts Deeply**: Don't memorize, understand why
2. **Practice Coding**: Implement examples yourself
3. **System Design**: Practice designing complete systems
4. **Real Experience**: Work on projects, contribute to open source
5. **Stay Updated**: Follow Spring Boot releases and features

---

**💡 Remember**: Interviewers at 3.5+ years level expect:
- Deep technical knowledge
- Production experience
- Problem-solving ability
- System design skills
- Best practices awareness

---

**Good Luck with Your Interviews! 🚀**



