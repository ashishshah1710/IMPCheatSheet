# 🌐 REST APIs & Microservices

**Phase 2: Build Production-Grade REST APIs (2 Weeks)**

---

## 📖 Overview

Master the art of building production-ready REST APIs with Spring Boot. This section covers everything from basic CRUD operations to advanced topics like versioning, HATEOAS, and API documentation.

---

## 🎯 Learning Objectives

By the end of this section, you should master:

✅ RESTful API design principles  
✅ Request/Response handling  
✅ Global exception handling  
✅ Input validation  
✅ API versioning strategies  
✅ HATEOAS  
✅ API documentation (Swagger/OpenAPI)  
✅ Content negotiation  

---

## 📚 Core Topics

### 1. RESTful Principles

**REST (Representational State Transfer) Principles:**
- Client-Server architecture
- Stateless communication
- Cacheable responses
- Uniform interface
- Layered system
- Code on demand (optional)

**HTTP Methods:**
| Method | Purpose | Idempotent | Safe |
|--------|---------|------------|------|
| GET | Retrieve resource | Yes | Yes |
| POST | Create resource | No | No |
| PUT | Update/Replace resource | Yes | No |
| PATCH | Partial update | No | No |
| DELETE | Delete resource | Yes | No |
| HEAD | Get headers only | Yes | Yes |
| OPTIONS | Get allowed methods | Yes | Yes |

**HTTP Status Codes:**
| Code | Meaning | Use Case |
|------|---------|----------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Not authenticated |
| 403 | Forbidden | Not authorized |
| 404 | Not Found | Resource not found |
| 409 | Conflict | Duplicate resource |
| 500 | Internal Server Error | Server error |

---

### 2. REST Controllers

**Basic Controller:**

```java
@RestController
@RequestMapping("/api/users")
@Slf4j
public class UserController {
    
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping
    public ResponseEntity<List<UserDTO>> getAllUsers() {
        log.info("Fetching all users");
        List<UserDTO> users = userService.getAllUsers();
        return ResponseEntity.ok(users);
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUserById(@PathVariable Long id) {
        log.info("Fetching user with id: {}", id);
        return userService.getUserById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @PostMapping
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody CreateUserRequest request) {
        log.info("Creating user: {}", request.getEmail());
        UserDTO created = userService.createUser(request);
        
        URI location = ServletUriComponentsBuilder
            .fromCurrentRequest()
            .path("/{id}")
            .buildAndExpand(created.getId())
            .toUri();
        
        return ResponseEntity.created(location).body(created);
    }
    
    @PutMapping("/{id}")
    public ResponseEntity<UserDTO> updateUser(
            @PathVariable Long id,
            @Valid @RequestBody UpdateUserRequest request) {
        log.info("Updating user: {}", id);
        return userService.updateUser(id, request)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @PatchMapping("/{id}")
    public ResponseEntity<UserDTO> partialUpdateUser(
            @PathVariable Long id,
            @RequestBody Map<String, Object> updates) {
        log.info("Partially updating user: {}", id);
        return userService.partialUpdate(id, updates)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteUser(@PathVariable Long id) {
        log.info("Deleting user: {}", id);
        userService.deleteUser(id);
    }
}
```

**📄 Deep Dive:** [controllers.md](./controllers.md)

---

### 3. Exception Handling

**Global Exception Handler:**

```java
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleResourceNotFound(
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
    public ResponseEntity<ErrorResponse> handleValidationException(
            MethodArgumentNotValidException ex, WebRequest request) {
        log.error("Validation failed");
        
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(
                FieldError::getField,
                FieldError::getDefaultMessage,
                (existing, replacement) -> existing
            ));
        
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.BAD_REQUEST.value())
            .error("Validation Failed")
            .message("Invalid input")
            .errors(errors)
            .path(request.getDescription(false))
            .build();
        
        return ResponseEntity.badRequest().body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGlobalException(
            Exception ex, WebRequest request) {
        log.error("Internal server error", ex);
        
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.INTERNAL_SERVER_ERROR.value())
            .error("Internal Server Error")
            .message("An unexpected error occurred")
            .path(request.getDescription(false))
            .build();
        
        return ResponseEntity
            .status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(error);
    }
}
```

**📄 Deep Dive:** [exception-handling.md](./exception-handling.md)

---

### 4. Validation

**Entity Validation:**

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
public class CreateUserRequest {
    
    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100, message = "Name must be between 2 and 100 characters")
    private String name;
    
    @NotBlank(message = "Email is required")
    @Email(message = "Email must be valid")
    private String email;
    
    @NotBlank(message = "Password is required")
    @Size(min = 8, message = "Password must be at least 8 characters")
    @Pattern(
        regexp = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
        message = "Password must contain uppercase, lowercase, number, and special character"
    )
    private String password;
    
    @NotNull(message = "Age is required")
    @Min(value = 18, message = "Age must be at least 18")
    @Max(value = 120, message = "Age must be less than 120")
    private Integer age;
    
    @Past(message = "Date of birth must be in the past")
    private LocalDate dateOfBirth;
    
    @Valid
    private Address address;
}

@Data
public class Address {
    @NotBlank
    private String street;
    
    @NotBlank
    private String city;
    
    @NotBlank
    @Pattern(regexp = "^[0-9]{5}$", message = "Zip code must be 5 digits")
    private String zipCode;
}
```

**Custom Validation:**

```java
@Target({ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = UniqueEmailValidator.class)
public @interface UniqueEmail {
    String message() default "Email already exists";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

@Component
public class UniqueEmailValidator implements ConstraintValidator<UniqueEmail, String> {
    
    @Autowired
    private UserRepository userRepository;
    
    @Override
    public boolean isValid(String email, ConstraintValidatorContext context) {
        if (email == null) {
            return true;
        }
        return !userRepository.existsByEmail(email);
    }
}
```

**📄 Deep Dive:** [validation.md](./validation.md)

---

### 5. API Versioning

**Three Main Strategies:**

**1. URI Versioning:**
```java
@RestController
@RequestMapping("/api/v1/users")
public class UserControllerV1 {
    @GetMapping("/{id}")
    public UserDTOV1 getUser(@PathVariable Long id) {
        // V1 implementation
    }
}

@RestController
@RequestMapping("/api/v2/users")
public class UserControllerV2 {
    @GetMapping("/{id}")
    public UserDTOV2 getUser(@PathVariable Long id) {
        // V2 implementation with additional fields
    }
}
```

**2. Header Versioning:**
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping(value = "/{id}", headers = "X-API-VERSION=1")
    public UserDTOV1 getUserV1(@PathVariable Long id) {
        // V1 implementation
    }
    
    @GetMapping(value = "/{id}", headers = "X-API-VERSION=2")
    public UserDTOV2 getUserV2(@PathVariable Long id) {
        // V2 implementation
    }
}
```

**3. Content Negotiation (Media Type):**
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping(value = "/{id}", produces = "application/vnd.company.v1+json")
    public UserDTOV1 getUserV1(@PathVariable Long id) {
        // V1 implementation
    }
    
    @GetMapping(value = "/{id}", produces = "application/vnd.company.v2+json")
    public UserDTOV2 getUserV2(@PathVariable Long id) {
        // V2 implementation
    }
}
```

**📄 Deep Dive:** [versioning.md](./versioning.md)

---

### 6. API Documentation (Swagger/OpenAPI)

**Setup:**

```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.2.0</version>
</dependency>
```

**Configuration:**

```java
@Configuration
public class OpenAPIConfig {
    
    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
            .info(new Info()
                .title("User Management API")
                .version("1.0")
                .description("API for managing users")
                .contact(new Contact()
                    .name("API Support")
                    .email("support@example.com")
                    .url("https://example.com/support"))
                .license(new License()
                    .name("Apache 2.0")
                    .url("https://www.apache.org/licenses/LICENSE-2.0")))
            .servers(Arrays.asList(
                new Server().url("http://localhost:8080").description("Development"),
                new Server().url("https://api.example.com").description("Production")
            ))
            .addSecurityItem(new SecurityRequirement().addList("bearerAuth"))
            .components(new Components()
                .addSecuritySchemes("bearerAuth", new SecurityScheme()
                    .type(SecurityScheme.Type.HTTP)
                    .scheme("bearer")
                    .bearerFormat("JWT")));
    }
}
```

**Annotations:**

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
        @ApiResponse(responseCode = "200", description = "User found",
            content = @Content(schema = @Schema(implementation = UserDTO.class))),
        @ApiResponse(responseCode = "404", description = "User not found",
            content = @Content(schema = @Schema(implementation = ErrorResponse.class))),
        @ApiResponse(responseCode = "500", description = "Internal server error")
    })
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUserById(
            @Parameter(description = "User ID", required = true)
            @PathVariable Long id) {
        return userService.getUserById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
}
```

**Access Swagger UI:**
- UI: `http://localhost:8080/swagger-ui.html`
- JSON: `http://localhost:8080/v3/api-docs`

**📄 Deep Dive:** [documentation.md](./documentation.md)

---

### 7. DTOs and Mapping

**Using ModelMapper:**

```java
@Configuration
public class MapperConfig {
    @Bean
    public ModelMapper modelMapper() {
        return new ModelMapper();
    }
}

@Service
public class UserService {
    
    private final UserRepository userRepository;
    private final ModelMapper modelMapper;
    
    public UserService(UserRepository userRepository, ModelMapper modelMapper) {
        this.userRepository = userRepository;
        this.modelMapper = modelMapper;
    }
    
    public UserDTO getUserById(Long id) {
        User user = userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        return modelMapper.map(user, UserDTO.class);
    }
    
    public UserDTO createUser(CreateUserRequest request) {
        User user = modelMapper.map(request, User.class);
        User saved = userRepository.save(user);
        return modelMapper.map(saved, UserDTO.class);
    }
}
```

**Using MapStruct (Better Performance):**

```java
@Mapper(componentModel = "spring")
public interface UserMapper {
    
    UserDTO toDTO(User user);
    
    User toEntity(CreateUserRequest request);
    
    @Mapping(target = "id", ignore = true)
    @Mapping(target = "createdAt", ignore = true)
    void updateEntityFromDTO(UpdateUserRequest request, @MappingTarget User user);
}
```

---

## 💻 Complete Example

### Entity

```java
@Entity
@Table(name = "users")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String name;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    @Column(nullable = false)
    private String password;
    
    private Integer age;
    
    @Enumerated(EnumType.STRING)
    private UserStatus status;
    
    @CreatedDate
    @Column(nullable = false, updatable = false)
    private LocalDateTime createdAt;
    
    @LastModifiedDate
    private LocalDateTime updatedAt;
}
```

### DTOs

```java
@Data
@Builder
public class UserDTO {
    private Long id;
    private String name;
    private String email;
    private Integer age;
    private String status;
    private LocalDateTime createdAt;
}

@Data
public class CreateUserRequest {
    @NotBlank
    @Size(min = 2, max = 100)
    private String name;
    
    @NotBlank
    @Email
    @UniqueEmail
    private String email;
    
    @NotBlank
    @Size(min = 8)
    private String password;
    
    @Min(18)
    private Integer age;
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
}
```

### Service

```java
@Service
@Transactional
@Slf4j
public class UserService {
    
    private final UserRepository userRepository;
    private final UserMapper userMapper;
    private final PasswordEncoder passwordEncoder;
    
    public UserService(UserRepository userRepository, 
                      UserMapper userMapper,
                      PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.userMapper = userMapper;
        this.passwordEncoder = passwordEncoder;
    }
    
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
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setStatus(UserStatus.ACTIVE);
        
        User saved = userRepository.save(user);
        log.info("User created: {}", saved.getEmail());
        
        return userMapper.toDTO(saved);
    }
    
    public Optional<UserDTO> updateUser(Long id, UpdateUserRequest request) {
        return userRepository.findById(id)
            .map(user -> {
                userMapper.updateEntityFromDTO(request, user);
                User updated = userRepository.save(user);
                return userMapper.toDTO(updated);
            });
    }
    
    public void deleteUser(Long id) {
        if (!userRepository.existsById(id)) {
            throw new ResourceNotFoundException("User not found with id: " + id);
        }
        userRepository.deleteById(id);
        log.info("User deleted: {}", id);
    }
}
```

---

## 🎯 Interview Questions

### Basic Level

**Q1: What is REST and its principles?**

A: REST (Representational State Transfer) is an architectural style with these principles:
- Client-Server separation
- Stateless communication
- Cacheable responses
- Uniform interface (URIs, HTTP methods)
- Layered system
- Resource-based

**Q2: Difference between @Controller and @RestController?**

A:
- `@Controller`: Returns views (HTML)
- `@RestController`: Returns data (JSON/XML), combines `@Controller` + `@ResponseBody`

**Q3: What HTTP status codes do you use for REST APIs?**

A:
- 200: Success (GET, PUT, PATCH)
- 201: Created (POST)
- 204: No Content (DELETE)
- 400: Bad Request (validation error)
- 404: Not Found
- 500: Server error

---

## ✅ Practice Checklist

- [ ] Create CRUD REST API
- [ ] Implement global exception handling
- [ ] Add validation with custom validators
- [ ] Implement API versioning
- [ ] Add Swagger documentation
- [ ] Use DTOs and mapping
- [ ] Implement pagination and sorting
- [ ] Add filtering and search
- [ ] Handle content negotiation
- [ ] Write integration tests

---

## 🎯 Next Steps

**👉 [Phase 3: Data & Databases →](../03-data-databases/README.md)**

---

**💡 Pro Tip:** Always use DTOs! Never expose entities directly. This gives you flexibility to change internal structure without affecting API contracts.



