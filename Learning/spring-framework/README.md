# 🍃 Spring Framework - Complete Guide

**For 3.5+ Years Experienced Developers | Interview Preparation**

Master Spring Framework for enterprise Java development and ace your technical interviews!

---

## 📖 Overview

Spring Framework is the most popular Java framework for building enterprise applications. It provides comprehensive infrastructure support for developing Java applications.

### Why Spring?

✅ **Dependency Injection** - Loose coupling and testability  
✅ **AOP Support** - Cross-cutting concerns made easy  
✅ **Transaction Management** - Declarative transaction support  
✅ **Enterprise Integration** - Easy integration with Java EE  
✅ **Testing Support** - Built-in testing capabilities  
✅ **Industry Standard** - Used by 70%+ Java enterprise applications  

---

## 🎯 Learning Path for Experienced Developers

### Phase 1: Core Concepts (1-2 weeks)
**Refresh and deepen your understanding**

- Dependency Injection (DI) & Inversion of Control (IoC)
- Bean lifecycle and scopes
- Configuration styles (XML, Java, Annotations)
- Spring Expression Language (SpEL)
- ApplicationContext vs BeanFactory

**👉 Start:** [`01-core-concepts/README.md`](01-core-concepts/README.md)

---

### Phase 2: Spring MVC & Web (1-2 weeks)
**Build production-ready web applications**

- Spring MVC architecture
- Controllers, RequestMapping, RestController
- Request/Response handling
- Exception handling
- Validation and data binding
- Interceptors and filters

**👉 Continue:** [`02-spring-mvc/README.md`](02-spring-mvc/README.md)

---

### Phase 3: Data Access & Transactions (1 week)
**Master data persistence**

- Spring Data JPA
- JDBC Template
- Transaction management (@Transactional)
- Transaction propagation and isolation
- Repository pattern
- Query methods

**👉 Master:** [`03-data-access/README.md`](03-data-access/README.md)

---

### Phase 4: AOP & Security (1 week)
**Advanced enterprise features**

- Aspect-Oriented Programming
- Spring Security basics
- Authentication vs Authorization
- Method security
- OAuth2 and JWT
- CORS configuration

**👉 Advanced:** [`04-aop-security/README.md`](04-aop-security/README.md)

---

## 💼 Interview Preparation

### Common Interview Topics

**Core Spring:**
- What is Dependency Injection? Types of DI?
- Bean scopes and lifecycle
- Difference between @Component, @Service, @Repository
- Constructor vs Setter injection
- Circular dependency resolution

**Spring MVC:**
- Request processing flow
- @RestController vs @Controller
- Exception handling strategies
- Content negotiation
- Async request processing

**Data & Transactions:**
- @Transactional working
- Transaction propagation levels
- Optimistic vs Pessimistic locking
- N+1 query problem
- Connection pooling

**👉 See:** [`interview-questions/README.md`](interview-questions/README.md)

---

## 📚 Content Structure

```
spring-framework/
├── 01-core-concepts/
│   ├── README.md                     # IoC, DI, Bean lifecycle
│   ├── dependency-injection.md       # DI patterns
│   ├── bean-scopes.md               # Singleton, Prototype, etc.
│   └── configuration.md              # XML, Java, Annotations
│
├── 02-spring-mvc/
│   ├── README.md                     # MVC architecture
│   ├── controllers.md               # Request handling
│   ├── rest-api.md                  # RESTful services
│   └── exception-handling.md        # Global exception handling
│
├── 03-data-access/
│   ├── README.md                     # Data access overview
│   ├── spring-data-jpa.md           # JPA integration
│   ├── transactions.md              # Transaction management
│   └── jdbc-template.md             # JDBC operations
│
├── 04-aop-security/
│   ├── README.md                     # AOP & Security
│   ├── aspect-oriented.md           # AOP concepts
│   ├── spring-security.md           # Security basics
│   └── oauth2-jwt.md                # Modern auth
│
├── interview-questions/
│   ├── README.md                     # All interview Q&A
│   ├── core-spring.md               # Core concepts
│   ├── spring-mvc.md                # MVC questions
│   ├── data-access.md               # Data questions
│   └── scenario-based.md            # Real-world scenarios
│
├── best-practices/
│   ├── README.md                     # Spring best practices
│   ├── design-patterns.md           # Common patterns
│   ├── performance.md               # Optimization tips
│   └── testing.md                   # Unit & integration tests
│
├── real-world-examples/
│   ├── microservice-example/        # Complete microservice
│   ├── rest-api-example/            # Production API
│   └── security-example/            # Secured application
│
└── CHEATSHEET.md                     # Quick reference
```

---

## 🎯 Quick Reference

### Core Annotations

```java
// Component Scanning
@Component          // Generic component
@Service            // Service layer
@Repository         // Data access layer
@Controller         // Web MVC controller
@RestController     // REST API controller
@Configuration      // Java config class

// Dependency Injection
@Autowired          // Auto-wire dependency
@Qualifier          // Specify which bean to inject
@Value              // Inject property values
@Primary            // Mark as primary candidate

// Bean Management
@Bean               // Define a bean
@Scope              // Define bean scope
@Lazy               // Lazy initialization
@DependsOn          // Define dependency order

// Web Layer
@RequestMapping     // Map HTTP requests
@GetMapping         // HTTP GET
@PostMapping        // HTTP POST
@PutMapping         // HTTP PUT
@DeleteMapping      // HTTP DELETE
@PathVariable       // Extract path variable
@RequestParam       // Extract query param
@RequestBody        // Bind request body
@ResponseBody       // Write to response body

// Data Access
@Transactional      // Transaction management
@Entity             // JPA entity
@Repository         // Data repository
@Query              // Custom query
```

---

## 💡 Quick Start Example

### Simple Spring Application

```java
// Configuration
@Configuration
@ComponentScan(basePackages = "com.example")
@EnableTransactionManagement
public class AppConfig {
    
    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource ds = new DriverManagerDataSource();
        ds.setDriverClassName("org.postgresql.Driver");
        ds.setUrl("jdbc:postgresql://localhost:5432/mydb");
        ds.setUsername("user");
        ds.setPassword("password");
        return ds;
    }
}

// Service
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Transactional
    public User createUser(User user) {
        return userRepository.save(user);
    }
    
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
}

// REST Controller
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping
    public ResponseEntity<List<User>> getUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }
    
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody User user) {
        User created = userService.createUser(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }
}
```

---

## 🏆 For 3.5+ Years Experience

### What Interviewers Expect

**Technical Depth:**
- Deep understanding of IoC and DI
- Transaction management expertise
- Security implementation
- Performance optimization
- Testing strategies

**Real-World Experience:**
- Microservices architecture
- REST API best practices
- Error handling strategies
- Caching implementation
- Async processing

**Problem-Solving:**
- Debug production issues
- Optimize application performance
- Design scalable solutions
- Handle edge cases
- Security vulnerabilities

---

## 📊 Interview Success Metrics

### Topics You Must Know

| Topic | Importance | Interview Frequency |
|-------|------------|-------------------|
| Dependency Injection | 🔴 Critical | 95% |
| Bean Lifecycle | 🔴 Critical | 85% |
| Transaction Management | 🔴 Critical | 80% |
| Spring MVC Flow | 🟡 Important | 75% |
| Exception Handling | 🟡 Important | 70% |
| AOP Concepts | 🟡 Important | 60% |
| Spring Security | 🟡 Important | 65% |
| Spring Data JPA | 🟢 Good to Know | 55% |

---

## 🎓 Learning Resources

### Official Documentation
- [Spring Framework Docs](https://docs.spring.io/spring-framework/docs/current/reference/html/)
- [Spring Guides](https://spring.io/guides)
- [Spring Blog](https://spring.io/blog)

### Recommended Books
- "Spring in Action" by Craig Walls
- "Pro Spring 5" by Iuliana Cosmina
- "Spring Framework Essentials" by Shameer Kunjumohamed

### Online Courses
- Udemy: Spring Framework Master Class
- Pluralsight: Spring Framework courses
- Baeldung: Spring tutorials

---

## ✅ Preparation Checklist

### Core Concepts
- [ ] Understand IoC and DI thoroughly
- [ ] Know all bean scopes
- [ ] Bean lifecycle and callbacks
- [ ] Configuration methods (XML, Java, Annotations)
- [ ] Circular dependency handling

### Spring MVC
- [ ] Request processing flow
- [ ] Controller types and annotations
- [ ] Exception handling
- [ ] Data validation
- [ ] Content negotiation

### Data Access
- [ ] @Transactional internals
- [ ] Transaction propagation
- [ ] Repository pattern
- [ ] Query optimization
- [ ] Connection pooling

### Advanced Topics
- [ ] AOP concepts and use cases
- [ ] Spring Security architecture
- [ ] Caching strategies
- [ ] Async processing
- [ ] WebSocket support

---

## 🚀 Career Impact

### Salary Ranges (with Spring expertise)

**3-5 Years Experience:**
- **Java Developer** - $85K-$120K
- **Spring Developer** - $90K-$130K
- **Backend Engineer** - $95K-$135K

**5-7 Years Experience:**
- **Senior Spring Developer** - $120K-$160K
- **Tech Lead** - $130K-$170K
- **Architect** - $140K-$180K

---

## 🔗 Quick Links

| Topic | Link |
|-------|------|
| Core Concepts | [01-core-concepts/README.md](01-core-concepts/README.md) |
| Spring MVC | [02-spring-mvc/README.md](02-spring-mvc/README.md) |
| Data Access | [03-data-access/README.md](03-data-access/README.md) |
| AOP & Security | [04-aop-security/README.md](04-aop-security/README.md) |
| Interview Questions | [interview-questions/README.md](interview-questions/README.md) |
| Cheat Sheet | [CHEATSHEET.md](CHEATSHEET.md) |

---

## 🎯 Next Steps

1. **Review Core Concepts** - Start with [`01-core-concepts/README.md`](01-core-concepts/README.md)
2. **Practice Coding** - Build sample applications
3. **Study Interview Questions** - [`interview-questions/README.md`](interview-questions/README.md)
4. **Build Projects** - Create portfolio pieces
5. **Mock Interviews** - Practice with peers

---

**Ready to master Spring Framework?** 🍃

👉 **[Start with Core Concepts →](01-core-concepts/README.md)**

---

## 💡 Simple Explanation (In Plain English)

- Spring is a container that creates and wires your objects so you focus on business logic, not `new` everywhere.
- IoC means Spring controls object lifecycle; DI means dependencies are passed in (usually via constructors).
- MVC, data access, transactions, AOP, and security are layered modules you combine in real apps.
- At 3–5 years experience, interviews expect you to explain *why* Spring solves coupling, testing, and cross-cutting concerns—not just annotation names.

## 🎯 Interview Quick Prep

### Q1: What problem does Spring Framework solve?

**Simple Answer:** It centralizes object creation and wiring (IoC/DI), so classes depend on interfaces instead of concrete implementations. That makes code easier to test, swap implementations, and configure per environment without rewriting business logic.

### Q2: IoC vs DI—what is the difference?

**Simple Answer:** IoC is the principle: something else (the container) controls how objects are built and connected. DI is how Spring implements IoC—by injecting dependencies through constructors, setters, or fields. In interviews, say “IoC is the idea; DI is the mechanism.”

### Q3: What should a mid-level developer know about the Spring container?

**Simple Answer:** `ApplicationContext` loads beans, applies configuration, and manages scopes (mostly singleton). You should explain bean lifecycle, `@Component` scanning, and why constructor injection is preferred for required dependencies and testability.

### Q4: How does Spring MVC fit into the bigger picture?

**Simple Answer:** `DispatcherServlet` routes HTTP requests to controllers, which call services backed by repositories. You are not memorizing every class—show the request flow and where validation, exceptions, and transactions sit in the stack.

### Q5: What production topics come up most for Spring interviews?

**Simple Answer:** `@Transactional` behavior (propagation, rollback rules), exception handling strategy, N+1 queries with JPA, and basic security (auth vs authorization). Tie answers to incidents you debugged: slow APIs, wrong transaction boundaries, or leaked sessions.

**Must-know for interviews:** Explain IoC/DI, bean scopes, MVC request flow, and `@Transactional` propagation with a real example from your projects.
