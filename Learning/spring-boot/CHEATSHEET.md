# 🚀 Spring Boot Cheat Sheet

**Quick Reference for Developers**

---

## 📦 Dependencies

### Common Starters

```xml
<!-- Web & REST APIs -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<!-- Data JPA -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- Security -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<!-- Validation -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>

<!-- Actuator -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>

<!-- Test -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>

<!-- Lombok -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>

<!-- PostgreSQL -->
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <scope>runtime</scope>
</dependency>
```

---

## 🎯 Core Annotations

### Application

```java
@SpringBootApplication  // = @Configuration + @EnableAutoConfiguration + @ComponentScan
@EnableScheduling       // Enable scheduled tasks
@EnableAsync            // Enable async processing
@EnableCaching          // Enable caching
```

### Stereotypes

```java
@Component      // Generic component
@Service        // Business logic
@Repository     // Data access
@Controller     // MVC controller
@RestController // REST controller = @Controller + @ResponseBody
@Configuration  // Configuration class
```

### Dependency Injection

```java
@Autowired      // Inject dependency (prefer constructor injection)
@Qualifier      // Specify bean name
@Primary        // Preferred bean
@Lazy           // Lazy initialization
@Value          // Inject property value
```

### REST

```java
@RestController
@RequestMapping("/api/users")
@GetMapping("/{id}")
@PostMapping
@PutMapping("/{id}")
@PatchMapping("/{id}")
@DeleteMapping("/{id}")

@PathVariable   // Path variable
@RequestParam   // Query parameter
@RequestBody    // Request body
@RequestHeader  // Request header
@ResponseStatus // Response HTTP status
```

### JPA

```java
@Entity
@Table(name = "users")
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
@Column(name = "email", unique = true, nullable = false)

// Relationships
@OneToOne
@OneToMany(mappedBy = "user", cascade = CascadeType.ALL)
@ManyToOne(fetch = FetchType.LAZY)
@ManyToMany
@JoinColumn(name = "user_id")
@JoinTable(name = "user_roles")

// Auditing
@CreatedDate
@LastModifiedDate
@CreatedBy
@LastModifiedBy
@EntityListeners(AuditingEntityListener.class)
```

### Validation

```java
@Valid              // Trigger validation
@NotNull
@NotBlank
@NotEmpty
@Size(min = 2, max = 100)
@Min(18)
@Max(120)
@Email
@Pattern(regexp = "...")
@Past
@Future
@Positive
@Negative
```

### Transaction

```java
@Transactional
@Transactional(readOnly = true)
@Transactional(propagation = Propagation.REQUIRES_NEW)
@Transactional(isolation = Isolation.SERIALIZABLE)
@Transactional(rollbackFor = Exception.class)
```

### Configuration

```java
@Configuration
@ConfigurationProperties(prefix = "app")
@EnableConfigurationProperties
@PropertySource("classpath:custom.properties")
@Profile("dev")
@Conditional(MyCondition.class)
```

### Security

```java
@EnableWebSecurity
@EnableMethodSecurity
@PreAuthorize("hasRole('ADMIN')")
@PostAuthorize("returnObject.owner == authentication.name")
@Secured("ROLE_ADMIN")
@RolesAllowed("ADMIN")
```

### Testing

```java
@SpringBootTest
@WebMvcTest(UserController.class)
@DataJpaTest
@MockBean
@SpyBean
@TestConfiguration
@AutoConfigureMockMvc
```

---

## 🔧 Configuration

### application.yml

```yaml
# Server
server:
  port: 8080
  servlet:
    context-path: /api

# Application
spring:
  application:
    name: my-app
  
  # Profiles
  profiles:
    active: ${ENVIRONMENT:dev}
  
  # Database
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: ${DB_USER}
    password: ${DB_PASSWORD}
    driver-class-name: org.postgresql.Driver
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 30000
  
  # JPA
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: false
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
        format_sql: true
  
  # Flyway
  flyway:
    enabled: true
    locations: classpath:db/migration
    baseline-on-migrate: true
  
  # Redis
  redis:
    host: localhost
    port: 6379
    password: ${REDIS_PASSWORD}
  
  # Cache
  cache:
    type: redis
    redis:
      time-to-live: 3600000
  
  # Security
  security:
    oauth2:
      client:
        registration:
          google:
            client-id: ${GOOGLE_CLIENT_ID}
            client-secret: ${GOOGLE_CLIENT_SECRET}

# Actuator
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: always
  metrics:
    tags:
      application: ${spring.application.name}

# Logging
logging:
  level:
    root: INFO
    com.example: DEBUG
  pattern:
    console: "%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"
  file:
    name: logs/application.log
```

---

## 💻 Code Snippets

### REST Controller

```java
@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
@Slf4j
public class UserController {
    
    private final UserService userService;
    
    @GetMapping
    public ResponseEntity<List<UserDTO>> getAllUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUserById(@PathVariable Long id) {
        return userService.getUserById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @PostMapping
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody CreateUserRequest request) {
        UserDTO user = userService.createUser(request);
        URI location = ServletUriComponentsBuilder
            .fromCurrentRequest()
            .path("/{id}")
            .buildAndExpand(user.getId())
            .toUri();
        return ResponseEntity.created(location).body(user);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<UserDTO> updateUser(
            @PathVariable Long id,
            @Valid @RequestBody UpdateUserRequest request) {
        return userService.updateUser(id, request)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

### Service

```java
@Service
@Transactional
@RequiredArgsConstructor
@Slf4j
public class UserService {
    
    private final UserRepository userRepository;
    private final UserMapper userMapper;
    
    @Transactional(readOnly = true)
    public List<UserDTO> getAllUsers() {
        return userRepository.findAll()
            .stream()
            .map(userMapper::toDTO)
            .collect(Collectors.toList());
    }
    
    @Transactional(readOnly = true)
    public Optional<UserDTO> getUserById(Long id) {
        return userRepository.findById(id)
            .map(userMapper::toDTO);
    }
    
    public UserDTO createUser(CreateUserRequest request) {
        User user = userMapper.toEntity(request);
        User saved = userRepository.save(user);
        log.info("User created: {}", saved.getId());
        return userMapper.toDTO(saved);
    }
    
    public Optional<UserDTO> updateUser(Long id, UpdateUserRequest request) {
        return userRepository.findById(id)
            .map(user -> {
                userMapper.updateEntityFromDTO(request, user);
                return userMapper.toDTO(userRepository.save(user));
            });
    }
    
    public void deleteUser(Long id) {
        if (!userRepository.existsById(id)) {
            throw new ResourceNotFoundException("User not found");
        }
        userRepository.deleteById(id);
        log.info("User deleted: {}", id);
    }
}
```

### Repository

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    Optional<User> findByEmail(String email);
    
    List<User> findByStatus(UserStatus status);
    
    Page<User> findByNameContainingIgnoreCase(String name, Pageable pageable);
    
    boolean existsByEmail(String email);
    
    @Query("SELECT u FROM User u WHERE u.status = :status AND u.createdAt > :date")
    List<User> findActiveUsersAfterDate(
        @Param("status") UserStatus status,
        @Param("date") LocalDateTime date
    );
    
    @Query(value = "SELECT * FROM users WHERE status = ?1 LIMIT ?2", nativeQuery = true)
    List<User> findTopNByStatus(String status, int limit);
    
    @Modifying
    @Query("UPDATE User u SET u.status = :status WHERE u.id = :id")
    int updateUserStatus(@Param("id") Long id, @Param("status") UserStatus status);
}
```

### Entity

```java
@Entity
@Table(name = "users", indexes = {
    @Index(name = "idx_email", columnList = "email")
})
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@EntityListeners(AuditingEntityListener.class)
public class User {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, length = 100)
    private String name;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    @Column(nullable = false)
    private String password;
    
    @Enumerated(EnumType.STRING)
    private UserStatus status;
    
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Order> orders = new ArrayList<>();
    
    @CreatedDate
    @Column(nullable = false, updatable = false)
    private LocalDateTime createdAt;
    
    @LastModifiedDate
    private LocalDateTime updatedAt;
    
    @Version
    private Long version;
}
```

### Exception Handler

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

### Security Config

```java
@Configuration
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfig {
    
    private final JwtAuthenticationFilter jwtAuthFilter;
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .cors(Customizer.withDefaults())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/auth/**", "/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .addFilterBefore(jwtAuthFilter, UsernamePasswordAuthenticationFilter.class);
        
        return http.build();
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

### Caching

```java
@Service
@Slf4j
public class UserService {
    
    @Cacheable(value = "users", key = "#id")
    public User getUserById(Long id) {
        log.info("Fetching from database: {}", id);
        return userRepository.findById(id).orElseThrow();
    }
    
    @CachePut(value = "users", key = "#result.id")
    public User updateUser(Long id, UpdateUserRequest request) {
        // Update and return
    }
    
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
    
    @CacheEvict(value = "users", allEntries = true)
    public void clearAllCache() {
        log.info("Clearing all user cache");
    }
}
```

---

## 🗄️ Database

### Flyway Migration

```sql
-- V1__create_users_table.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    version BIGINT DEFAULT 0
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status);

-- V2__add_department.sql
ALTER TABLE users ADD COLUMN department_id BIGINT;
ALTER TABLE users ADD CONSTRAINT fk_users_department 
    FOREIGN KEY (department_id) REFERENCES departments(id);
```

---

## 🐳 Docker

### Dockerfile

```dockerfile
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
RUN addgroup -S spring && adduser -S spring -G spring
USER spring:spring
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
  
  app:
    build: .
    environment:
      SPRING_PROFILES_ACTIVE: prod
      SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/mydb
      SPRING_DATASOURCE_USERNAME: postgres
      SPRING_DATASOURCE_PASSWORD: secret
      SPRING_REDIS_HOST: redis
    ports:
      - "8080:8080"
    depends_on:
      - postgres
      - redis

volumes:
  postgres_data:
```

---

## 🧪 Testing

### Unit Test

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
    void getUserById_WhenExists_ReturnsUser() {
        // Given
        Long id = 1L;
        User user = User.builder().id(id).name("John").build();
        UserDTO dto = UserDTO.builder().id(id).name("John").build();
        
        when(userRepository.findById(id)).thenReturn(Optional.of(user));
        when(userMapper.toDTO(user)).thenReturn(dto);
        
        // When
        Optional<UserDTO> result = userService.getUserById(id);
        
        // Then
        assertThat(result).isPresent();
        assertThat(result.get().getName()).isEqualTo("John");
    }
}
```

### Integration Test

```java
@SpringBootTest
@AutoConfigureMockMvc
class UserControllerIntegrationTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @Test
    void createUser_WithValidData_ReturnsCreated() throws Exception {
        String requestBody = """
            {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "SecurePass123!",
                "age": 25
            }
            """;
        
        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(requestBody))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.name").value("John Doe"));
    }
}
```

---

## 📊 Common Commands

```bash
# Run application
./mvnw spring-boot:run

# Run with profile
./mvnw spring-boot:run -Dspring-boot.run.profiles=dev

# Build
./mvnw clean package

# Skip tests
./mvnw clean package -DskipTests

# Run tests
./mvnw test

# Create executable JAR
./mvnw clean package

# Run JAR
java -jar target/myapp-1.0.0.jar

# Run with profile
java -jar target/myapp.jar --spring.profiles.active=prod

# Docker build
docker build -t myapp:1.0 .

# Docker run
docker run -p 8080:8080 myapp:1.0

# Docker Compose
docker-compose up -d
docker-compose down
```

---

## 🔗 Quick Links

- **Fundamentals**: [01-fundamentals/README.md](01-fundamentals/README.md)
- **REST APIs**: [02-rest-apis/README.md](02-rest-apis/README.md)
- **Data & Databases**: [03-data-databases/README.md](03-data-databases/README.md)
- **Security**: [04-security-production/README.md](04-security-production/README.md)
- **Microservices**: [microservices/README.md](microservices/README.md)
- **Interview Questions**: [interview-questions/README.md](interview-questions/README.md)
- **Best Practices**: [best-practices/README.md](best-practices/README.md)

---

**Happy Coding! 🚀**



