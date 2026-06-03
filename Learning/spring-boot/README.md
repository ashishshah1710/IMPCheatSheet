# 🚀 Spring Boot - Complete Guide

**For 3.5+ Years Experienced Developers | Interview Preparation**

Master Spring Boot for building production-ready microservices and ace your interviews!

---

## 📖 Overview

Spring Boot makes it easy to create stand-alone, production-grade Spring applications. It takes an opinionated view of the Spring platform to get you started quickly.

### Why Spring Boot?

✅ **Auto-Configuration** - Intelligent defaults  
✅ **Standalone** - Embedded servers (Tomcat, Jetty)  
✅ **Production-Ready** - Metrics, health checks, monitoring  
✅ **Microservices** - Perfect for cloud-native apps  
✅ **Rapid Development** - Start coding in minutes  
✅ **Industry Standard** - 80%+ new Spring projects use Boot  

---

## 🎯 Learning Path for Experienced Developers

### Phase 1: Spring Boot Fundamentals (1 week)
**Master the Boot way of development**

- Auto-configuration magic
- Starter dependencies
- Application properties & YAML
- Embedded servers
- Spring Boot DevTools
- Actuator endpoints

**👉 Start:** [`01-fundamentals/README.md`](01-fundamentals/README.md)

---

### Phase 2: REST APIs & Microservices (2 weeks)
**Build production-grade APIs**

- RESTful API design
- Request/Response handling
- Exception handling
- Validation
- API versioning
- HATEOAS
- API documentation (Swagger/OpenAPI)

**👉 Continue:** [`02-rest-apis/README.md`](02-rest-apis/README.md)

---

### Phase 3: Data & Databases (1 week)
**Master data persistence**

- Spring Data JPA
- Multiple database support
- Connection pooling (HikariCP)
- Flyway/Liquibase migrations
- Repository patterns
- Query optimization
- Caching (Redis, EhCache)

**👉 Master:** [`03-data-databases/README.md`](03-data-databases/README.md)

---

### Phase 4: Security & Production (1 week)
**Deploy with confidence**

- Spring Security integration
- JWT authentication
- OAuth2 & OpenID Connect
- Method security
- CORS configuration
- Docker deployment
- Cloud deployment (AWS, Azure, GCP)
- Monitoring & logging

**👉 Advanced:** [`04-security-production/README.md`](04-security-production/README.md)

---

## 💼 Interview Preparation

### Top Interview Questions

**Spring Boot Basics:**
- Difference between Spring and Spring Boot?
- How does auto-configuration work?
- What are starter dependencies?
- Explain @SpringBootApplication annotation
- How to disable specific auto-configuration?

**REST APIs:**
- Design principles for REST APIs
- Exception handling strategies
- API versioning approaches
- Best practices for DTOs
- Idempotency in REST

**Microservices:**
- Service discovery patterns
- Circuit breaker pattern
- Distributed tracing
- API Gateway pattern
- Configuration management

**Production:**
- Actuator endpoints and uses
- Health check implementation
- Metrics and monitoring
- Logging strategies
- Performance optimization

**👉 See:** [`interview-questions/README.md`](interview-questions/README.md)

---

## 📚 Content Structure

```
spring-boot/
├── 01-fundamentals/
│   ├── README.md                      # Spring Boot basics
│   ├── auto-configuration.md          # How it works
│   ├── starters.md                    # Starter dependencies
│   ├── properties.md                  # Configuration
│   └── actuator.md                    # Production features
│
├── 02-rest-apis/
│   ├── README.md                      # REST API guide
│   ├── controllers.md                 # Request handling
│   ├── exception-handling.md          # Error responses
│   ├── validation.md                  # Input validation
│   ├── documentation.md               # Swagger/OpenAPI
│   └── versioning.md                  # API versions
│
├── 03-data-databases/
│   ├── README.md                      # Data access
│   ├── spring-data-jpa.md            # JPA integration
│   ├── repositories.md                # Repository pattern
│   ├── migrations.md                  # DB migrations
│   └── caching.md                     # Caching strategies
│
├── 04-security-production/
│   ├── README.md                      # Security & deployment
│   ├── jwt-auth.md                    # JWT implementation
│   ├── oauth2.md                      # OAuth2 flow
│   ├── docker.md                      # Containerization
│   ├── monitoring.md                  # APM tools
│   └── cloud-deployment.md            # Cloud platforms
│
├── microservices/
│   ├── README.md                      # Microservices guide
│   ├── service-discovery.md           # Eureka, Consul
│   ├── api-gateway.md                 # Spring Cloud Gateway
│   ├── config-server.md               # Centralized config
│   ├── circuit-breaker.md             # Resilience4j
│   └── distributed-tracing.md         # Sleuth, Zipkin
│
├── interview-questions/
│   ├── README.md                      # All questions
│   ├── fundamentals.md                # Basic questions
│   ├── rest-apis.md                   # API questions
│   ├── microservices.md               # Microservices Q&A
│   ├── scenario-based.md              # Real scenarios
│   └── system-design.md               # Design questions
│
├── best-practices/
│   ├── README.md                      # Best practices
│   ├── project-structure.md           # Code organization
│   ├── error-handling.md              # Exception strategies
│   ├── testing.md                     # Testing approaches
│   └── performance.md                 # Optimization
│
├── real-world-projects/
│   ├── e-commerce-api/                # Complete API
│   ├── blog-microservice/             # Microservice example
│   └── todo-app/                      # Full CRUD
│
└── CHEATSHEET.md                       # Quick reference
```

---

## 🎯 Quick Start

### Create Spring Boot App

```bash
# Using Spring Initializr (start.spring.io)
curl https://start.spring.io/starter.zip \
  -d dependencies=web,data-jpa,postgresql,lombok,actuator \
  -d type=maven-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -d baseDir=my-app \
  -o my-app.zip

unzip my-app.zip
cd my-app
./mvnw spring-boot:run
```

### Simple REST API

```java
// Application Entry Point
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

// Entity
@Entity
@Table(name = "users")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String name;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    private LocalDateTime createdAt = LocalDateTime.now();
}

// Repository
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    List<User> findByNameContainingIgnoreCase(String name);
}

// Service
@Service
@Transactional
@Slf4j
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    public User createUser(User user) {
        log.info("Creating user: {}", user.getEmail());
        return userRepository.save(user);
    }
    
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
    
    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }
    
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}

// REST Controller
@RestController
@RequestMapping("/api/users")
@Slf4j
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        return userService.getUserById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
        User created = userService.createUser(user);
        return ResponseEntity
            .status(HttpStatus.CREATED)
            .body(created);
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}

// Global Exception Handler
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(
        ResourceNotFoundException ex) {
        log.error("Resource not found", ex);
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGlobalException(Exception ex) {
        log.error("Internal server error", ex);
        ErrorResponse error = new ErrorResponse(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            "An error occurred",
            LocalDateTime.now()
        );
        return ResponseEntity
            .status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(error);
    }
}
```

### Configuration (application.yml)

```yaml
spring:
  application:
    name: user-service
  
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: ${DB_USER:postgres}
    password: ${DB_PASSWORD:password}
    driver-class-name: org.postgresql.Driver
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
  
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
        format_sql: true
  
  flyway:
    enabled: true
    locations: classpath:db/migration

server:
  port: 8080
  servlet:
    context-path: /
  
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: always

logging:
  level:
    root: INFO
    com.example: DEBUG
  pattern:
    console: "%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"
```

---

## 🏆 For 3.5+ Years Experience

### What Interviewers Expect

**Technical Mastery:**
- Deep Spring Boot understanding
- Microservices architecture
- Production deployment experience
- Performance tuning
- Security implementation

**System Design:**
- Design scalable APIs
- Database design decisions
- Caching strategies
- Message queues integration
- Cloud architecture

**Problem-Solving:**
- Debug production issues
- Optimize slow APIs
- Handle high traffic
- Implement resilience patterns
- Secure applications

---

## 📊 Interview Success Metrics

| Topic | Importance | Interview Frequency |
|-------|------------|-------------------|
| Auto-Configuration | 🔴 Critical | 90% |
| REST API Design | 🔴 Critical | 95% |
| Exception Handling | 🔴 Critical | 85% |
| Spring Data JPA | 🔴 Critical | 80% |
| Security (JWT/OAuth2) | 🟡 Important | 75% |
| Microservices Patterns | 🟡 Important | 70% |
| Actuator & Monitoring | 🟡 Important | 65% |
| Docker & Deployment | 🟢 Good to Know | 60% |

---

## 🎓 Learning Resources

### Official Documentation
- [Spring Boot Docs](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [Spring Guides](https://spring.io/guides)
- [Baeldung Spring Boot](https://www.baeldung.com/spring-boot)

### Recommended Books
- "Spring Boot in Action" by Craig Walls
- "Cloud Native Java" by Josh Long
- "Mastering Spring Boot 2.0" by Dinesh Rajput

---

## ✅ Preparation Checklist

### Fundamentals
- [ ] Auto-configuration mechanism
- [ ] Starter dependencies
- [ ] Application properties
- [ ] Embedded servers
- [ ] Actuator endpoints

### REST APIs
- [ ] RESTful principles
- [ ] HTTP methods and status codes
- [ ] Exception handling
- [ ] Validation
- [ ] API documentation

### Data Access
- [ ] Spring Data JPA
- [ ] Repository patterns
- [ ] Query methods
- [ ] Transaction management
- [ ] Database migrations

### Microservices
- [ ] Service discovery
- [ ] API Gateway
- [ ] Config Server
- [ ] Circuit Breaker
- [ ] Distributed tracing

### Production
- [ ] Security implementation
- [ ] Monitoring and logging
- [ ] Docker containerization
- [ ] Cloud deployment
- [ ] Performance optimization

---

## 🚀 Career Impact

### Salary Ranges (with Spring Boot expertise)

**3-5 Years:**
- **Spring Boot Developer** - $95K-$135K
- **Backend Engineer** - $100K-$140K
- **Microservices Developer** - $105K-$145K

**5-7 Years:**
- **Senior Backend Engineer** - $130K-$170K
- **Tech Lead** - $140K-$180K
- **Solutions Architect** - $150K-$200K

---

## 🔗 Quick Links

| Topic | Link |
|-------|------|
| Fundamentals | [01-fundamentals/README.md](01-fundamentals/README.md) |
| REST APIs | [02-rest-apis/README.md](02-rest-apis/README.md) |
| Data & Databases | [03-data-databases/README.md](03-data-databases/README.md) |
| Security & Production | [04-security-production/README.md](04-security-production/README.md) |
| Microservices | [microservices/README.md](microservices/README.md) |
| Interview Questions | [interview-questions/README.md](interview-questions/README.md) |
| Cheat Sheet | [CHEATSHEET.md](CHEATSHEET.md) |

---

## 🎯 Next Steps

1. **Review Fundamentals** - [`01-fundamentals/README.md`](01-fundamentals/README.md)
2. **Build REST APIs** - [`02-rest-apis/README.md`](02-rest-apis/README.md)
3. **Study Interview Questions** - [`interview-questions/README.md`](interview-questions/README.md)
4. **Build Microservices** - Practice with real projects
5. **Mock Interviews** - Prepare for technical rounds

---

**Ready to master Spring Boot?** 🚀

👉 **[Start with Fundamentals →](01-fundamentals/README.md)**

---

## 💡 Simple Explanation (In Plain English)

- Spring Boot is Spring with batteries included: starters, auto-config, and an embedded server so you run `main()` and ship fast.
- You configure behavior with `application.yml` and `@ConfigurationProperties`, not huge XML files.
- Actuator and health checks are how ops knows your app is alive in Kubernetes or the cloud.
- At 3–5 years, interviews focus on *how* auto-config chooses beans and how you override it safely.

## 🎯 Interview Quick Prep

### Q1: Spring Framework vs Spring Boot?

**Simple Answer:** Framework gives core IoC, MVC, data, security. Boot adds opinionated auto-configuration, starters, embedded Tomcat, and production features (Actuator). Boot is not a replacement—it builds on Framework with faster bootstrap.

### Q2: What is Spring Boot auto-configuration?

**Simple Answer:** `@EnableAutoConfiguration` loads conditional `@Configuration` classes based on classpath and properties (e.g., DataSource if JDBC on classpath). You override with your own `@Bean` or `application.properties`. Explain `@ConditionalOn*` mentally.

### Q3: Why use starter dependencies?

**Simple Answer:** Starters bundle compatible libraries (e.g., `spring-boot-starter-web`) so you avoid version conflicts and missing transitive deps. Interview tip: mention BOM/import for dependency management in Maven/Gradle.

### Q4: How do you make a Boot app production-ready?

**Simple Answer:** Externalized config, health/metrics via Actuator, proper logging, connection pooling, security, tests, and container-friendly settings (graceful shutdown, probes). Reference profiles (`dev`, `prod`) and secrets from env/vault.

### Q5: Common Boot pitfalls senior interviewers mention?

**Simple Answer:** Over-broad component scan, fighting auto-config without understanding conditions, giant `application.yml`, missing `readOnly` transactions, and exposing Actuator without security. Show you profile and secure endpoints.

**Must-know for interviews:** Auto-configuration conditions, starters/BOM, profiles, and Actuator health for production.
