# 🍃 Spring Framework Cheat Sheet

**Quick Reference Guide**

---

## Core Annotations

```java
// Component Stereotypes
@Component       // Generic component
@Service         // Business logic
@Repository      // Data access
@Controller      // Web MVC
@RestController  // REST API
@Configuration   // Java config

// Dependency Injection
@Autowired       // Auto-wire dependency
@Qualifier       // Specify bean
@Value           // Inject property
@Primary         // Primary candidate

// Bean Management
@Bean            // Define bean
@Scope           // Bean scope
@Lazy            // Lazy initialization
@PostConstruct   // After creation
@PreDestroy      // Before destruction

// Web Layer
@RequestMapping  // Map requests
@GetMapping      // HTTP GET
@PostMapping     // HTTP POST
@PutMapping      // HTTP PUT
@DeleteMapping   // HTTP DELETE
@PathVariable    // Path variable
@RequestParam    // Query parameter
@RequestBody     // Request body

// Validation
@Valid           // Trigger validation
@NotNull         // Not null
@NotBlank        // Not blank
@Email           // Email format
@Size            // Size range
@Min/@Max        // Number range

// Transaction
@Transactional   // Transaction management

// AOP
@Aspect          // Aspect
@Before          // Before advice
@After           // After advice
@Around          // Around advice
@Pointcut        // Pointcut

// Security
@EnableWebSecurity
@PreAuthorize
@Secured
```

---

## Configuration

```java
@Configuration
@ComponentScan(basePackages = "com.example")
@EnableTransactionManagement
public class AppConfig {
    
    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource ds = new DriverManagerDataSource();
        ds.setUrl("jdbc:postgresql://localhost:5432/mydb");
        return ds;
    }
}
```

---

## REST Controller

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        return userService.getUserById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {
        User created = userService.createUser(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }
}
```

---

## Service Layer

```java
@Service
@Transactional
public class UserService {
    
    private final UserRepository userRepository;
    
    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    @Transactional(readOnly = true)
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
    
    public User createUser(User user) {
        return userRepository.save(user);
    }
}
```

---

## Repository

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    List<User> findByStatus(String status);
    
    @Query("SELECT u FROM User u WHERE u.age > :age")
    List<User> findUsersOlderThan(@Param("age") int age);
}
```

---

## Exception Handling

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(
            ResourceNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
}
```

---

## AOP

```java
@Aspect
@Component
public class LoggingAspect {
    
    @Around("execution(* com.example.service.*.*(..))")
    public Object logAround(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object result = joinPoint.proceed();
        long duration = System.currentTimeMillis() - start;
        System.out.println("Method " + joinPoint.getSignature().getName() + 
                          " took " + duration + "ms");
        return result;
    }
}
```

---

## Security

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .httpBasic(Customizer.withDefaults());
        
        return http.build();
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

---

## Transaction Propagation

| Type | Behavior |
|------|----------|
| REQUIRED | Use existing or create new |
| REQUIRES_NEW | Always create new |
| SUPPORTS | Use if available |
| MANDATORY | Must have transaction |
| NEVER | Must not have transaction |

---

## Bean Scopes

| Scope | Description |
|-------|-------------|
| singleton | One instance (default) |
| prototype | New instance each time |
| request | One per HTTP request |
| session | One per HTTP session |

---

## Common Commands

```bash
# Maven
mvn clean install
mvn spring-boot:run
mvn test

# Run with profile
mvn spring-boot:run -Dspring-boot.run.profiles=dev
```

---

**Happy Coding! 🍃**

