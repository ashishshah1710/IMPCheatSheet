# ⭐ Spring Boot Best Practices

**Production-Ready Development Guidelines**

---

## 📖 Overview

Follow these best practices to write clean, maintainable, and production-ready Spring Boot applications.

---

## 🎯 Project Structure

### Recommended Package Structure

```
com.example.myapp/
├── MyAppApplication.java           # Main application class
├── config/                         # Configuration classes
│   ├── SecurityConfig.java
│   ├── DatabaseConfig.java
│   ├── CacheConfig.java
│   └── SwaggerConfig.java
├── controller/                     # REST controllers
│   ├── UserController.java
│   ├── OrderController.java
│   └── advice/                     # Exception handlers
│       └── GlobalExceptionHandler.java
├── service/                        # Business logic
│   ├── UserService.java
│   ├── impl/                       # Service implementations
│   │   └── UserServiceImpl.java
│   └── external/                   # External service clients
│       └── PaymentServiceClient.java
├── repository/                     # Data access
│   ├── UserRepository.java
│   └── OrderRepository.java
├── model/                          # Domain models
│   ├── entity/                     # JPA entities
│   │   ├── User.java
│   │   └── Order.java
│   ├── dto/                        # Data Transfer Objects
│   │   ├── UserDTO.java
│   │   ├── CreateUserRequest.java
│   │   └── UpdateUserRequest.java
│   └── enums/                      # Enumerations
│       └── UserStatus.java
├── mapper/                         # Object mapping
│   └── UserMapper.java
├── security/                       # Security components
│   ├── JwtService.java
│   ├── JwtAuthenticationFilter.java
│   └── CustomUserDetailsService.java
├── util/                           # Utility classes
│   └── DateUtils.java
└── exception/                      # Custom exceptions
    ├── ResourceNotFoundException.java
    └── BusinessException.java
```

---

## 🔧 Configuration Best Practices

### 1. Use Type-Safe Configuration

✅ **Good:**
```java
@Configuration
@ConfigurationProperties(prefix = "app")
@Validated
@Data
public class AppProperties {
    @NotBlank
    private String name;
    
    @Min(1)
    @Max(65535)
    private int port;
    
    private Security security = new Security();
    
    @Data
    public static class Security {
        private String jwtSecret;
        private long jwtExpiration;
    }
}
```

❌ **Avoid:**
```java
@Value("${app.name}")
private String appName;

@Value("${app.port}")
private int port;
```

---

### 2. Environment-Specific Configuration

```yaml
# application.yml (common)
spring:
  application:
    name: myapp

---
# application-dev.yml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb_dev
logging:
  level:
    com.example: DEBUG

---
# application-prod.yml
spring:
  datasource:
    url: ${DATABASE_URL}
logging:
  level:
    com.example: WARN
```

---

### 3. Externalize Secrets

❌ **Never do this:**
```yaml
spring:
  datasource:
    password: mySecretPassword123
```

✅ **Use environment variables:**
```yaml
spring:
  datasource:
    password: ${DB_PASSWORD}
app:
  jwt:
    secret: ${JWT_SECRET}
```

---

## 🏗️ Code Best Practices

### 1. Use DTOs, Never Expose Entities

✅ **Good:**
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUser(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getUserById(id));
    }
    
    @PostMapping
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody CreateUserRequest request) {
        UserDTO user = userService.createUser(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}
```

❌ **Avoid:**
```java
@GetMapping("/{id}")
public User getUser(@PathVariable Long id) {
    return userRepository.findById(id).orElse(null);
}
```

**Why?**
- Entities contain internal structure
- Risk of circular references (JSON serialization)
- Exposing sensitive data
- Breaking changes affect API

---

### 2. Use Constructor Injection

✅ **Good:**
```java
@Service
@RequiredArgsConstructor // Lombok
public class UserService {
    
    private final UserRepository userRepository;
    private final UserMapper userMapper;
    private final PasswordEncoder passwordEncoder;
    
    // Or manual constructor
    public UserService(UserRepository userRepository,
                      UserMapper userMapper,
                      PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.userMapper = userMapper;
        this.passwordEncoder = passwordEncoder;
    }
}
```

❌ **Avoid:**
```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private UserMapper userMapper;
}
```

**Benefits:**
- Immutability
- Easier testing
- Required dependencies clear
- No NullPointerException

---

### 3. Proper Exception Handling

✅ **Good:**
```java
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(
            ResourceNotFoundException ex, WebRequest request) {
        log.error("Resource not found: {}", ex.getMessage());
        
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
    public ResponseEntity<ErrorResponse> handleValidation(
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

### 4. Validate Input

✅ **Good:**
```java
@Data
public class CreateUserRequest {
    
    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100)
    private String name;
    
    @NotBlank
    @Email(message = "Email must be valid")
    private String email;
    
    @NotBlank
    @Size(min = 8)
    @Pattern(
        regexp = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
        message = "Password must contain uppercase, lowercase, number, and special character"
    )
    private String password;
    
    @Min(18)
    @Max(120)
    private Integer age;
}

@PostMapping
public ResponseEntity<UserDTO> createUser(@Valid @RequestBody CreateUserRequest request) {
    // Validation happens automatically
}
```

---

### 5. Use Transactions Properly

✅ **Good:**
```java
@Service
@Transactional
public class OrderService {
    
    // Read-only for queries
    @Transactional(readOnly = true)
    public List<OrderDTO> getAllOrders() {
        return orderRepository.findAll()
            .stream()
            .map(orderMapper::toDTO)
            .collect(Collectors.toList());
    }
    
    // Default for write operations
    public OrderDTO createOrder(CreateOrderRequest request) {
        // All operations in single transaction
        Order order = createOrderEntity(request);
        Order saved = orderRepository.save(order);
        paymentService.processPayment(saved.getId());
        return orderMapper.toDTO(saved);
    }
    
    // Custom settings for critical operations
    @Transactional(
        propagation = Propagation.REQUIRES_NEW,
        isolation = Isolation.SERIALIZABLE,
        timeout = 30
    )
    public void criticalOperation() {
        // Runs in new transaction
    }
}
```

---

### 6. Optimize Database Queries

✅ **Solve N+1 Problem:**
```java
// Bad: N+1 queries
List<Order> orders = orderRepository.findAll();
orders.forEach(order -> {
    order.getUser().getName(); // Triggers query for each order
});

// Good: Single query with JOIN FETCH
@Query("SELECT o FROM Order o JOIN FETCH o.user")
List<Order> findAllWithUser();

// Good: Entity Graph
@EntityGraph(attributePaths = {"user", "items"})
List<Order> findAll();
```

✅ **Use Projections:**
```java
// Don't fetch all fields if you need only few
public interface UserSummary {
    Long getId();
    String getName();
    String getEmail();
}

@Query("SELECT u.id as id, u.name as name, u.email as email FROM User u")
List<UserSummary> findAllSummaries();
```

---

### 7. Use Caching Wisely

✅ **Good:**
```java
@Service
@Slf4j
public class UserService {
    
    // Cache frequently accessed data
    @Cacheable(value = "users", key = "#id")
    public UserDTO getUserById(Long id) {
        log.info("Fetching from database: {}", id);
        return userRepository.findById(id)
            .map(userMapper::toDTO)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }
    
    // Update cache on modification
    @CachePut(value = "users", key = "#result.id")
    public UserDTO updateUser(Long id, UpdateUserRequest request) {
        // Update and return
    }
    
    // Remove from cache on deletion
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
    
    // Clear all cache periodically
    @CacheEvict(value = "users", allEntries = true)
    @Scheduled(fixedRate = 3600000) // Every hour
    public void clearCache() {
        log.info("Clearing user cache");
    }
}
```

---

### 8. Logging Best Practices

✅ **Good:**
```java
@Slf4j
@Service
public class OrderService {
    
    public OrderDTO createOrder(CreateOrderRequest request) {
        log.info("Creating order for user: {}", request.getUserId());
        
        try {
            Order order = processOrder(request);
            log.info("Order created successfully: {}", order.getId());
            return orderMapper.toDTO(order);
        } catch (PaymentException e) {
            log.error("Payment failed for order: userId={}, amount={}, error={}",
                request.getUserId(), request.getAmount(), e.getMessage());
            throw e;
        }
    }
    
    private void logSensitiveData(String data) {
        // Never log sensitive data
        log.debug("Processing data: {}", maskSensitiveData(data));
    }
}
```

**Logging Levels:**
- **ERROR**: Errors that need immediate attention
- **WARN**: Potential issues
- **INFO**: Important business events
- **DEBUG**: Detailed information for debugging
- **TRACE**: Very detailed information

---

### 9. API Documentation

✅ **Good:**
```java
@RestController
@RequestMapping("/api/users")
@Tag(name = "User Management", description = "APIs for managing users")
public class UserController {
    
    @Operation(
        summary = "Get user by ID",
        description = "Retrieves a user by their unique identifier"
    )
    @ApiResponses(value = {
        @ApiResponse(responseCode = "200", description = "User found"),
        @ApiResponse(responseCode = "404", description = "User not found"),
        @ApiResponse(responseCode = "500", description = "Internal server error")
    })
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUserById(
            @Parameter(description = "User ID", required = true)
            @PathVariable Long id) {
        return ResponseEntity.ok(userService.getUserById(id));
    }
}
```

---

### 10. Testing Best Practices

✅ **Unit Tests:**
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private UserMapper userMapper;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void getUserById_WhenUserExists_ReturnsUserDTO() {
        // Given
        Long userId = 1L;
        User user = User.builder().id(userId).name("John").build();
        UserDTO userDTO = UserDTO.builder().id(userId).name("John").build();
        
        when(userRepository.findById(userId)).thenReturn(Optional.of(user));
        when(userMapper.toDTO(user)).thenReturn(userDTO);
        
        // When
        UserDTO result = userService.getUserById(userId);
        
        // Then
        assertThat(result).isNotNull();
        assertThat(result.getName()).isEqualTo("John");
        verify(userRepository).findById(userId);
        verify(userMapper).toDTO(user);
    }
    
    @Test
    void getUserById_WhenUserNotExists_ThrowsException() {
        // Given
        Long userId = 999L;
        when(userRepository.findById(userId)).thenReturn(Optional.empty());
        
        // When/Then
        assertThatThrownBy(() -> userService.getUserById(userId))
            .isInstanceOf(ResourceNotFoundException.class)
            .hasMessageContaining("User not found");
    }
}
```

✅ **Integration Tests:**
```java
@SpringBootTest
@AutoConfigureMockMvc
@TestPropertySource(locations = "classpath:application-test.properties")
class UserControllerIntegrationTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @Autowired
    private ObjectMapper objectMapper;
    
    @Test
    void createUser_WithValidData_ReturnsCreated() throws Exception {
        // Given
        CreateUserRequest request = CreateUserRequest.builder()
            .name("John Doe")
            .email("john@example.com")
            .password("SecurePass123!")
            .age(25)
            .build();
        
        // When/Then
        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(request)))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.name").value("John Doe"))
            .andExpect(jsonPath("$.email").value("john@example.com"));
    }
}
```

---

## 🔒 Security Best Practices

### 1. Never Store Plain Text Passwords

✅ **Good:**
```java
@Service
public class UserService {
    
    private final PasswordEncoder passwordEncoder;
    
    public UserDTO createUser(CreateUserRequest request) {
        User user = userMapper.toEntity(request);
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        // Save user
    }
}
```

### 2. Implement Rate Limiting

```java
@Configuration
public class RateLimitConfig {
    
    @Bean
    public RateLimiter rateLimiter() {
        return RateLimiter.create(100.0); // 100 requests per second
    }
}
```

### 3. Use HTTPS in Production

```yaml
server:
  ssl:
    enabled: true
    key-store: classpath:keystore.p12
    key-store-password: ${SSL_PASSWORD}
    key-store-type: PKCS12
```

---

## 📊 Performance Best Practices

### 1. Connection Pooling

```yaml
spring:
  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 30000
      idle-timeout: 600000
      max-lifetime: 1800000
```

### 2. Enable HTTP Compression

```yaml
server:
  compression:
    enabled: true
    mime-types: application/json,application/xml,text/html,text/xml,text/plain
    min-response-size: 1024
```

### 3. Use Async Processing

```java
@Service
public class NotificationService {
    
    @Async
    public CompletableFuture<Void> sendEmailAsync(String email, String message) {
        // Send email
        return CompletableFuture.completedFuture(null);
    }
}
```

---

## 📝 Documentation Best Practices

1. **README.md**: Project overview, setup instructions
2. **API Documentation**: Swagger/OpenAPI
3. **Code Comments**: Why, not what
4. **Architecture Docs**: High-level design
5. **Runbooks**: Deployment, troubleshooting

---

## ✅ Checklist

### Before Committing
- [ ] Code compiles without warnings
- [ ] Tests pass
- [ ] No sensitive data in code
- [ ] Proper error handling
- [ ] Logging added for important events
- [ ] Code formatted and clean

### Before Deployment
- [ ] Environment variables configured
- [ ] Database migrations tested
- [ ] Health checks working
- [ ] Monitoring configured
- [ ] Security headers added
- [ ] Performance tested
- [ ] Rollback plan ready

---

## 🎯 Key Takeaways

1. **Use DTOs**: Never expose entities
2. **Constructor Injection**: Better than field injection
3. **Type-Safe Config**: Use @ConfigurationProperties
4. **Global Exception Handling**: Consistent error responses
5. **Validate Input**: Always validate user input
6. **Transaction Management**: Use @Transactional properly
7. **Optimize Queries**: Solve N+1 problem
8. **Cache Wisely**: Don't cache everything
9. **Test Thoroughly**: Unit + Integration tests
10. **Document Well**: Code, API, architecture

---

**💡 Remember**: Good code is:
- **Readable**: Easy to understand
- **Maintainable**: Easy to modify
- **Testable**: Easy to test
- **Performant**: Efficient
- **Secure**: Protected

---

**Follow these practices and your Spring Boot applications will be production-ready! 🚀**

