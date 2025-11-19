# 🍃 Spring Core Concepts

**Phase 1: IoC, DI, and Bean Lifecycle (1-2 Weeks)**

---

## 📖 Overview

Master the fundamental concepts of Spring Framework - Inversion of Control (IoC), Dependency Injection (DI), and Bean Management. These are the building blocks of all Spring applications.

---

## 🎯 Learning Objectives

✅ Understand IoC and DI principles  
✅ Master bean lifecycle and scopes  
✅ Learn configuration styles (XML, Java, Annotations)  
✅ Work with ApplicationContext  
✅ Handle circular dependencies  
✅ Use Spring Expression Language (SpEL)  

---

## 📚 Core Topics

### 1. Inversion of Control (IoC)

**What is IoC?**

Inversion of Control is a design principle where the control of object creation and lifecycle is transferred from the application code to the Spring container.

**Traditional Approach (Without IoC):**
```java
public class UserService {
    private UserRepository userRepository = new UserRepositoryImpl();
    
    public User getUser(Long id) {
        return userRepository.findById(id);
    }
}
```

**Spring IoC Approach:**
```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public User getUser(Long id) {
        return userRepository.findById(id);
    }
}
```

**Benefits:**
- Loose coupling
- Easy testing (can inject mocks)
- Flexible configuration
- Better maintainability

---

### 2. Dependency Injection (DI)

DI is the implementation of IoC where dependencies are "injected" into objects by the Spring container.

**Types of Dependency Injection:**

#### Constructor Injection (Recommended)

```java
@Service
public class OrderService {
    
    private final UserService userService;
    private final PaymentService paymentService;
    
    @Autowired // Optional in Spring 4.3+
    public OrderService(UserService userService, PaymentService paymentService) {
        this.userService = userService;
        this.paymentService = paymentService;
    }
}
```

**Advantages:**
- Immutable dependencies (final fields)
- Clear required dependencies
- Easy to test
- No NullPointerException

#### Setter Injection

```java
@Service
public class NotificationService {
    
    private EmailService emailService;
    
    @Autowired
    public void setEmailService(EmailService emailService) {
        this.emailService = emailService;
    }
}
```

**Use Case:** Optional dependencies

#### Field Injection (Not Recommended)

```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository; // Avoid this!
}
```

**Why Avoid?**
- Cannot create immutable objects
- Harder to test
- Hidden dependencies
- Can cause NullPointerException

---

### 3. Bean Lifecycle

**Bean Lifecycle Phases:**

1. **Instantiation**: Spring creates bean instance
2. **Populate Properties**: Spring injects dependencies
3. **setBeanName()**: If implements BeanNameAware
4. **setBeanFactory()**: If implements BeanFactoryAware
5. **setApplicationContext()**: If implements ApplicationContextAware
6. **preProcessBeforeInitialization()**: BeanPostProcessor
7. **afterPropertiesSet()**: If implements InitializingBean
8. **Custom init method**: @PostConstruct or init-method
9. **postProcessAfterInitialization()**: BeanPostProcessor
10. **Bean Ready**: Bean is ready to use
11. **destroy()**: If implements DisposableBean
12. **Custom destroy method**: @PreDestroy or destroy-method

**Example:**

```java
@Component
public class DatabaseConnection {
    
    private Connection connection;
    
    // 1. Constructor
    public DatabaseConnection() {
        System.out.println("1. Constructor called");
    }
    
    // 2. Dependency Injection
    @Autowired
    public void setDataSource(DataSource dataSource) {
        System.out.println("2. Dependencies injected");
    }
    
    // 3. @PostConstruct
    @PostConstruct
    public void init() {
        System.out.println("3. @PostConstruct - Opening connection");
        // Open database connection
    }
    
    // 4. InitializingBean interface
    @Override
    public void afterPropertiesSet() {
        System.out.println("4. afterPropertiesSet called");
    }
    
    // 5. Custom method (if configured)
    public void customInit() {
        System.out.println("5. Custom init method");
    }
    
    // Bean is ready to use
    
    // 6. @PreDestroy
    @PreDestroy
    public void cleanup() {
        System.out.println("6. @PreDestroy - Closing connection");
        // Close database connection
    }
    
    // 7. DisposableBean interface
    @Override
    public void destroy() {
        System.out.println("7. destroy() called");
    }
    
    // 8. Custom destroy method
    public void customDestroy() {
        System.out.println("8. Custom destroy method");
    }
}
```

---

### 4. Bean Scopes

**Available Scopes:**

| Scope | Description | Use Case |
|-------|-------------|----------|
| **singleton** (default) | One instance per container | Stateless beans, services |
| **prototype** | New instance each time | Stateful beans |
| **request** | One per HTTP request | Web applications |
| **session** | One per HTTP session | User session data |
| **application** | One per ServletContext | Shared application data |
| **websocket** | One per WebSocket | WebSocket handlers |

**Examples:**

```java
// Singleton (default)
@Component
public class UserService {
    // Single instance shared across application
}

// Prototype
@Component
@Scope("prototype")
public class ShoppingCart {
    // New instance for each request
}

// Request Scope
@Component
@Scope(value = WebApplicationContext.SCOPE_REQUEST, proxyMode = ScopedProxyMode.TARGET_CLASS)
public class LoginAction {
    // New instance per HTTP request
}

// Session Scope
@Component
@Scope(value = WebApplicationContext.SCOPE_SESSION, proxyMode = ScopedProxyMode.TARGET_CLASS)
public class UserPreferences {
    // One instance per user session
}
```

---

### 5. Configuration Styles

#### Java-Based Configuration (Recommended)

```java
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
    
    @Bean
    public UserService userService() {
        return new UserService(userRepository());
    }
    
    @Bean
    public UserRepository userRepository() {
        return new UserRepositoryImpl(dataSource());
    }
}
```

#### Annotation-Based Configuration

```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Value("${app.name}")
    private String appName;
    
    @Transactional
    public User createUser(User user) {
        return userRepository.save(user);
    }
}
```

#### XML Configuration (Legacy)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
                           http://www.springframework.org/schema/beans/spring-beans.xsd">
    
    <bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
        <property name="driverClassName" value="org.postgresql.Driver"/>
        <property name="url" value="jdbc:postgresql://localhost:5432/mydb"/>
        <property name="username" value="user"/>
        <property name="password" value="password"/>
    </bean>
    
    <bean id="userRepository" class="com.example.repository.UserRepositoryImpl">
        <constructor-arg ref="dataSource"/>
    </bean>
    
    <bean id="userService" class="com.example.service.UserService">
        <constructor-arg ref="userRepository"/>
    </bean>
</beans>
```

---

### 6. ApplicationContext vs BeanFactory

| Feature | BeanFactory | ApplicationContext |
|---------|-------------|-------------------|
| Bean instantiation | Lazy | Eager (default) |
| Internationalization | ❌ No | ✅ Yes |
| Event publishing | ❌ No | ✅ Yes |
| Annotation support | ❌ Limited | ✅ Full |
| Enterprise features | ❌ No | ✅ Yes |
| **Recommendation** | ❌ Don't use | ✅ Always use |

**Using ApplicationContext:**

```java
// Java-based configuration
ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
UserService userService = context.getBean(UserService.class);

// XML configuration
ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");
UserService userService = context.getBean("userService", UserService.class);

// Web application
// Automatically created by Spring Boot or DispatcherServlet
@Autowired
private ApplicationContext context;
```

---

### 7. Handling Circular Dependencies

**Problem:**

```java
@Service
public class ServiceA {
    @Autowired
    private ServiceB serviceB; // ServiceA depends on ServiceB
}

@Service
public class ServiceB {
    @Autowired
    private ServiceA serviceA; // ServiceB depends on ServiceA
}
// Result: BeanCurrentlyInCreationException
```

**Solutions:**

#### Solution 1: Redesign (Best)
```java
// Extract common functionality to a third service
@Service
public class CommonService {
    // Shared logic
}

@Service
public class ServiceA {
    @Autowired
    private CommonService commonService;
}

@Service
public class ServiceB {
    @Autowired
    private CommonService commonService;
}
```

#### Solution 2: Setter Injection
```java
@Service
public class ServiceA {
    private ServiceB serviceB;
    
    @Autowired
    public void setServiceB(ServiceB serviceB) {
        this.serviceB = serviceB;
    }
}
```

#### Solution 3: @Lazy
```java
@Service
public class ServiceA {
    private final ServiceB serviceB;
    
    @Autowired
    public ServiceA(@Lazy ServiceB serviceB) {
        this.serviceB = serviceB;
    }
}
```

#### Solution 4: @PostConstruct
```java
@Service
public class ServiceA {
    @Autowired
    private ApplicationContext context;
    
    private ServiceB serviceB;
    
    @PostConstruct
    public void init() {
        serviceB = context.getBean(ServiceB.class);
    }
}
```

---

### 8. Spring Expression Language (SpEL)

SpEL is a powerful expression language that supports querying and manipulating objects at runtime.

```java
@Component
public class SpELExamples {
    
    // Literal values
    @Value("#{100}")
    private int number;
    
    // Properties
    @Value("#{systemProperties['user.name']}")
    private String userName;
    
    // Bean references
    @Value("#{userService.getUserCount()}")
    private int userCount;
    
    // Operators
    @Value("#{10 * 2 + 5}")
    private int calculation;
    
    // Conditional
    @Value("#{userService.userCount > 100 ? 'Many' : 'Few'}")
    private String userStatus;
    
    // Collection selection
    @Value("#{users.?[age > 18]}")
    private List<User> adults;
    
    // Regular expressions
    @Value("#{user.email matches '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'}")
    private boolean validEmail;
    
    // Elvis operator (null-safe)
    @Value("#{user.name ?: 'Unknown'}")
    private String name;
    
    // Safe navigation
    @Value("#{user?.address?.city}")
    private String city;
}
```

---

## 💻 Complete Example

```java
// Configuration
@Configuration
@ComponentScan(basePackages = "com.example")
@PropertySource("classpath:application.properties")
public class AppConfig {
    
    @Value("${db.url}")
    private String dbUrl;
    
    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource ds = new DriverManagerDataSource();
        ds.setUrl(dbUrl);
        return ds;
    }
    
    @Bean(initMethod = "init", destroyMethod = "cleanup")
    @Scope("singleton")
    public ConnectionPool connectionPool() {
        return new ConnectionPool(dataSource());
    }
}

// Service with lifecycle callbacks
@Service
public class UserService {
    
    private final UserRepository userRepository;
    private final EmailService emailService;
    
    @Value("${app.name}")
    private String appName;
    
    // Constructor injection
    @Autowired
    public UserService(UserRepository userRepository, 
                      @Lazy EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }
    
    @PostConstruct
    public void init() {
        System.out.println("UserService initialized for: " + appName);
    }
    
    @Transactional
    public User createUser(User user) {
        User saved = userRepository.save(user);
        emailService.sendWelcomeEmail(saved);
        return saved;
    }
    
    @PreDestroy
    public void cleanup() {
        System.out.println("UserService shutting down");
    }
}

// Main application
public class Application {
    public static void main(String[] args) {
        ApplicationContext context = 
            new AnnotationConfigApplicationContext(AppConfig.class);
        
        UserService userService = context.getBean(UserService.class);
        
        User user = new User("John Doe", "john@example.com");
        userService.createUser(user);
        
        ((ConfigurableApplicationContext) context).close();
    }
}
```

---

## 🎯 Interview Questions

### Q1: What is the difference between IoC and DI?

**Answer:**
- **IoC (Inversion of Control)**: Design principle where control of object creation is inverted from application to container
- **DI (Dependency Injection)**: Implementation technique of IoC where dependencies are injected by the container

IoC is the concept, DI is how we achieve it.

---

### Q2: Constructor vs Setter injection - which is better?

**Answer:**

**Constructor Injection** (Recommended):
- ✅ Immutable objects (final fields)
- ✅ Required dependencies clear
- ✅ Easier to test
- ✅ No partial initialization

**Setter Injection**:
- ✅ Optional dependencies
- ✅ Allows re-configuration
- ❌ Mutable state
- ❌ Can forget to set dependencies

**Best Practice**: Use constructor injection for required dependencies, setter for optional.

---

### Q3: Explain bean scopes with examples

**Answer:**

- **Singleton** (default): One instance per container
  ```java
  @Component // Singleton by default
  public class UserService { }
  ```

- **Prototype**: New instance every time
  ```java
  @Component
  @Scope("prototype")
  public class ShoppingCart { }
  ```

- **Request**: One per HTTP request (web apps only)
- **Session**: One per HTTP session (web apps only)
- **Application**: One per ServletContext
- **WebSocket**: One per WebSocket session

---

### Q4: How does Spring resolve circular dependencies?

**Answer:**

Spring uses three-level cache to resolve circular dependencies:

1. **singletonObjects**: Fully initialized beans
2. **earlySingletonObjects**: Beans being initialized
3. **singletonFactories**: Bean factories

**Process:**
1. Create bean A
2. Put A in early cache
3. Inject dependency B into A
4. While creating B, it needs A
5. Spring returns early reference of A
6. Complete initialization of B
7. Complete initialization of A

**Note**: Only works with singleton beans and setter/field injection, NOT constructor injection.

---

### Q5: What is the use of @PostConstruct and @PreDestroy?

**Answer:**

```java
@Component
public class DatabaseService {
    
    @PostConstruct
    public void init() {
        // Called after dependency injection
        // Initialize resources: open connections, load config
        System.out.println("Opening database connection");
    }
    
    @PreDestroy
    public void cleanup() {
        // Called before bean destruction
        // Release resources: close connections, cleanup
        System.out.println("Closing database connection");
    }
}
```

**When to use:**
- @PostConstruct: Initialize resources, validate configuration
- @PreDestroy: Clean up resources, close connections

---

## ✅ Practice Checklist

- [ ] Create application using Java configuration
- [ ] Implement constructor and setter injection
- [ ] Create beans with different scopes
- [ ] Implement lifecycle callbacks
- [ ] Handle circular dependencies
- [ ] Use SpEL in @Value annotations
- [ ] Create custom BeanPostProcessor
- [ ] Implement conditional bean creation

---

**👉 Next:** [Spring MVC →](../02-spring-mvc/README.md)

---

**💡 Pro Tip:** Master these core concepts thoroughly. They are the foundation of all Spring applications and are heavily tested in interviews!

