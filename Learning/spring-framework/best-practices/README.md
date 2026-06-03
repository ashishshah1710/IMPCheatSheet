# ⭐ Spring Framework Best Practices

**Production-Ready Development Guidelines**

---

## 1. Dependency Injection

✅ **Use Constructor Injection**
```java
@Service
public class UserService {
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

❌ **Avoid Field Injection**
```java
@Autowired
private UserRepository userRepository; // Don't do this!
```

---

## 2. Bean Configuration

✅ **Prefer Java Config over XML**
```java
@Configuration
public class AppConfig {
    @Bean
    public DataSource dataSource() {
        // Configure datasource
    }
}
```

---

## 3. Transaction Management

✅ **Use @Transactional properly**
```java
@Service
@Transactional
public class OrderService {
    
    @Transactional(readOnly = true)
    public Order getOrder(Long id) { }
    
    public Order createOrder(Order order) { }
}
```

---

## 4. Exception Handling

✅ **Use @RestControllerAdvice**
```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        // Handle exception
    }
}
```

---

## 5. Validation

✅ **Always validate input**
```java
@PostMapping
public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
    // Validation happens automatically
}
```

---

## 6. Testing

✅ **Write comprehensive tests**
```java
@SpringBootTest
class UserServiceTest {
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void testCreateUser() {
        // Test logic
    }
}
```

---

## 7. Logging

✅ **Use proper logging levels**
```java
@Slf4j
@Service
public class UserService {
    public User createUser(User user) {
        log.info("Creating user: {}", user.getEmail());
        log.debug("User details: {}", user);
    }
}
```

---

## 8. Security

✅ **Never store plain passwords**
```java
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```

---

## Key Takeaways

1. **Constructor Injection** over field injection
2. **Java Config** over XML
3. **@Transactional** for transaction management
4. **Global Exception Handling** for consistency
5. **Input Validation** always
6. **Comprehensive Testing** is essential
7. **Proper Logging** for debugging
8. **Security First** mindset

---

**[← Back to Main](../README.md)**

---

## 💡 Simple Explanation (In Plain English)

- Good Spring code is testable: constructor injection and thin controllers make unit tests fast.
- Transactions belong on the service layer where business rules and boundaries are clear.
- Never leak JPA entities on REST APIs—DTOs protect your schema and versioning story.
- Global exception handlers and validation give APIs a professional, consistent contract.

## 🎯 Interview Quick Prep

### Q1: Why do teams ban field `@Autowired`?

**Simple Answer:** Hidden dependencies, harder unit tests, and no immutability. Constructor injection documents required collaborators and fails fast at startup if a bean is missing—interviewers expect you to defend this with testing examples.

### Q2: Where should `@Transactional` live?

**Simple Answer:** On service-layer methods that define business transactions, not controllers or repositories. Controllers should stay thin; multiple repository calls in one use case belong in one transactional service method.

### Q3: Why use DTOs in REST APIs?

**Simple Answer:** DTOs decouple persistence model from API contract, prevent over-fetching/lazy-load leaks, and let you evolve the database without breaking clients. Map with MapStruct or explicit mappers—mention performance and clarity.

### Q4: What makes exception handling “production ready”?

**Simple Answer:** One `@RestControllerAdvice`, mapped exception types, stable error JSON (code, message, trace id), correct HTTP status, and no stack traces to clients. Log full details server-side with correlation IDs.

### Q5: Security practices you should mention in interviews?

**Simple Answer:** BCrypt (or stronger) for passwords, never commit secrets, validate all input, least-privilege roles, HTTPS only, and secure headers/CORS. Tie to OWASP awareness and secrets managers in cloud deploys.

**Must-know for interviews:** Constructor injection, service-layer transactions, DTOs, and centralized exception handling.
