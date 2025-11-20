# 🌸 Couchbase - Spring Boot Integration

Build production Spring Boot applications with Couchbase!

---

## 📚 Table of Contents

1. [Setup & Configuration](#setup-configuration)
2. [Repository Pattern](#repository-pattern)
3. [Service Layer](#service-layer)
4. [REST API](#rest-api)
5. [Advanced Features](#advanced-features)
6. [Testing](#testing)
7. [Production Deployment](#production-deployment)
8. [Interview Questions](#interview-questions)

---

## 🛠️ Setup & Configuration

### Dependencies

```xml
<!-- pom.xml -->
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-couchbase</artifactId>
    </dependency>
    
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
</dependencies>
```

### Application Properties

```yaml
# application.yml
spring:
  couchbase:
    connection-string: couchbase://localhost
    username: Administrator
    password: password
  data:
    couchbase:
      bucket-name: my-app
      scope-name: _default
      auto-index: true
      
server:
  port: 8080

logging:
  level:
    com.couchbase: DEBUG
```

### Configuration Class

```java
@Configuration
@EnableCouchbaseRepositories(basePackages = "com.example.repository")
public class CouchbaseConfig extends AbstractCouchbaseConfiguration {
    
    @Value("${spring.couchbase.connection-string}")
    private String connectionString;
    
    @Value("${spring.couchbase.username}")
    private String username;
    
    @Value("${spring.couchbase.password}")
    private String password;
    
    @Value("${spring.data.couchbase.bucket-name}")
    private String bucketName;
    
    @Override
    public String getConnectionString() {
        return connectionString;
    }
    
    @Override
    public String getUserName() {
        return username;
    }
    
    @Override
    public String getPassword() {
        return password;
    }
    
    @Override
    public String getBucketName() {
        return bucketName;
    }
    
    @Bean
    public ClusterEnvironment couchbaseClusterEnvironment() {
        return ClusterEnvironment.builder()
            .timeoutConfig(TimeoutConfig.builder()
                .kvTimeout(Duration.ofSeconds(10))
                .queryTimeout(Duration.ofSeconds(75))
                .build())
            .build();
    }
}
```

---

## 📦 Repository Pattern

### Entity Model

```java
@Document
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    
    @Id
    private String id;
    
    @Field
    private String email;
    
    @Field
    private String firstName;
    
    @Field
    private String lastName;
    
    @Field
    private Integer age;
    
    @Field
    private Address address;
    
    @Field
    private List<String> roles;
    
    @Field
    @CreatedDate
    private Instant createdAt;
    
    @Field
    @LastModifiedDate
    private Instant updatedAt;
    
    @Version
    private long version;
}

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Address {
    private String street;
    private String city;
    private String state;
    private String zipCode;
    private String country;
}
```

### Repository Interface

```java
@Repository
public interface UserRepository extends CouchbaseRepository<User, String> {
    
    // Derived query methods
    List<User> findByEmail(String email);
    
    List<User> findByFirstName(String firstName);
    
    List<User> findByAgeGreaterThan(Integer age);
    
    List<User> findByRolesContaining(String role);
    
    @Query("#{#n1ql.selectEntity} WHERE #{#n1ql.filter} AND email = $1")
    Optional<User> findByEmailCustom(String email);
    
    @Query("SELECT COUNT(*) FROM #{#n1ql.bucket} WHERE type = 'user' AND age > $1")
    Long countUsersOlderThan(Integer age);
    
    // N1QL query
    @Query("SELECT u.* FROM #{#n1ql.bucket} u WHERE u.address.city = $1")
    List<User> findByCity(String city);
}
```

---

## 🔧 Service Layer

### User Service

```java
@Service
@Slf4j
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private Cluster cluster;
    
    public User createUser(User user) {
        user.setId("user::" + UUID.randomUUID().toString());
        user.setCreatedAt(Instant.now());
        return userRepository.save(user);
    }
    
    public Optional<User> getUserById(String id) {
        return userRepository.findById(id);
    }
    
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
    
    public User updateUser(String id, User user) {
        return userRepository.findById(id)
            .map(existing -> {
                existing.setEmail(user.getEmail());
                existing.setFirstName(user.getFirstName());
                existing.setLastName(user.getLastName());
                existing.setAge(user.getAge());
                existing.setAddress(user.getAddress());
                existing.setUpdatedAt(Instant.now());
                return userRepository.save(existing);
            })
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }
    
    public void deleteUser(String id) {
        userRepository.deleteById(id);
    }
    
    // Custom N1QL query
    public List<User> searchUsers(String searchTerm) {
        Scope scope = cluster.bucket("my-app").defaultScope();
        QueryResult result = scope.query(
            "SELECT u.* FROM `my-app` u " +
            "WHERE LOWER(u.firstName) LIKE $1 OR LOWER(u.lastName) LIKE $1",
            QueryOptions.queryOptions()
                .parameters(JsonArray.from("%" + searchTerm.toLowerCase() + "%"))
        );
        
        return result.rowsAs(User.class);
    }
}
```

---

## 🌐 REST API

### User Controller

```java
@RestController
@RequestMapping("/api/users")
@Slf4j
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
        User created = userService.createUser(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable String id) {
        return userService.getUserById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        List<User> users = userService.getAllUsers();
        return ResponseEntity.ok(users);
    }
    
    @GetMapping("/search")
    public ResponseEntity<List<User>> searchUsers(@RequestParam String q) {
        List<User> users = userService.searchUsers(q);
        return ResponseEntity.ok(users);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(
            @PathVariable String id,
            @Valid @RequestBody User user) {
        User updated = userService.updateUser(id, user);
        return ResponseEntity.ok(updated);
    }
    
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable String id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}
```

### Exception Handling

```java
@ControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleResourceNotFound(
            ResourceNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            Instant.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(DocumentNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleDocumentNotFound(
            DocumentNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            "Document not found",
            Instant.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericException(Exception ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            "Internal server error",
            Instant.now()
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}

@Data
@AllArgsConstructor
class ErrorResponse {
    private int status;
    private String message;
    private Instant timestamp;
}
```

---

## 🚀 Advanced Features

### Caching with @Cacheable

```java
@Service
public class CachedUserService {
    
    @Cacheable(value = "users", key = "#id")
    public User getUserById(String id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }
    
    @CachePut(value = "users", key = "#user.id")
    public User updateUser(User user) {
        return userRepository.save(user);
    }
    
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(String id) {
        userRepository.deleteById(id);
    }
}
```

### Reactive Programming

```java
@Service
public class ReactiveUserService {
    
    @Autowired
    private ReactiveUserRepository reactiveUserRepository;
    
    public Mono<User> createUser(User user) {
        user.setId("user::" + UUID.randomUUID().toString());
        return reactiveUserRepository.save(user);
    }
    
    public Flux<User> getAllUsers() {
        return reactiveUserRepository.findAll();
    }
    
    public Mono<User> getUserById(String id) {
        return reactiveUserRepository.findById(id);
    }
}

@Repository
public interface ReactiveUserRepository 
        extends ReactiveCouchbaseRepository<User, String> {
    
    Flux<User> findByAgeGreaterThan(Integer age);
    
    Mono<User> findByEmail(String email);
}
```

---

## 🧪 Testing

### Integration Tests

```java
@SpringBootTest
@TestPropertySource(locations = "classpath:application-test.yml")
class UserServiceIntegrationTest {
    
    @Autowired
    private UserService userService;
    
    @Autowired
    private UserRepository userRepository;
    
    @BeforeEach
    void setUp() {
        userRepository.deleteAll();
    }
    
    @Test
    void testCreateUser() {
        User user = new User();
        user.setEmail("test@example.com");
        user.setFirstName("John");
        user.setLastName("Doe");
        user.setAge(30);
        
        User created = userService.createUser(user);
        
        assertNotNull(created.getId());
        assertEquals("test@example.com", created.getEmail());
    }
    
    @Test
    void testGetUserById() {
        User user = createTestUser();
        
        Optional<User> found = userService.getUserById(user.getId());
        
        assertTrue(found.isPresent());
        assertEquals(user.getEmail(), found.get().getEmail());
    }
    
    private User createTestUser() {
        User user = new User();
        user.setEmail("test@example.com");
        user.setFirstName("John");
        user.setLastName("Doe");
        user.setAge(30);
        return userService.createUser(user);
    }
}
```

---

## 🏭 Production Deployment

### Docker Compose

```yaml
version: '3.8'

services:
  couchbase:
    image: couchbase:latest
    ports:
      - "8091-8096:8091-8096"
      - "11210:11210"
    environment:
      - CLUSTER_NAME=my-cluster
    volumes:
      - couchbase-data:/opt/couchbase/var
  
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_COUCHBASE_CONNECTION_STRING=couchbase://couchbase
      - SPRING_COUCHBASE_USERNAME=Administrator
      - SPRING_COUCHBASE_PASSWORD=password
    depends_on:
      - couchbase

volumes:
  couchbase-data:
```

---

## 🎯 Interview Questions

**Q: How do you handle transactions in Couchbase with Spring Boot?**

**Answer:**
Use `@Transactional` annotation with Spring Data Couchbase 4.x+:

```java
@Transactional
public void transferFunds(String fromId, String toId, Double amount) {
    // Operations within transaction
}
```

**Q: What are the benefits of using Spring Data Couchbase?**

**Answer:**
- Repository pattern abstraction
- Automatic query generation
- Integration with Spring ecosystem
- Support for reactive programming
- Built-in caching support

---

**Master Couchbase with Spring Boot for production applications!** 🚀

