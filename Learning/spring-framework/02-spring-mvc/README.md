# 🌐 Spring MVC & Web

**Phase 2: Build Production-Ready Web Applications (1-2 Weeks)**

---

## 📖 Overview

Master Spring MVC architecture, request handling, REST APIs, exception handling, and validation. Learn to build robust web applications.

---

## 🎯 Learning Objectives

✅ Understand Spring MVC architecture  
✅ Master request/response handling  
✅ Build RESTful APIs  
✅ Implement global exception handling  
✅ Validate input data  
✅ Configure interceptors and filters  
✅ Handle content negotiation  

---

## 📚 Core Topics

### 1. Spring MVC Architecture

**Request Processing Flow:**

```
Client Request
     ↓
DispatcherServlet (Front Controller)
     ↓
HandlerMapping (Find Controller)
     ↓
Controller (Process Request)
     ↓
ModelAndView (Return Data + View)
     ↓
ViewResolver (Resolve View)
     ↓
View (Render Response)
     ↓
Client Response
```

**Key Components:**

- **DispatcherServlet**: Front controller that handles all requests
- **HandlerMapping**: Maps requests to controllers
- **Controller**: Handles business logic
- **ModelAndView**: Contains model data and view name
- **ViewResolver**: Resolves view names to actual views
- **View**: Renders the response

---

### 2. Controllers

#### Traditional MVC Controller

```java
@Controller
@RequestMapping("/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping
    public String listUsers(Model model) {
        List<User> users = userService.getAllUsers();
        model.addAttribute("users", users);
        return "user-list"; // Returns view name
    }
    
    @GetMapping("/{id}")
    public String getUser(@PathVariable Long id, Model model) {
        User user = userService.getUserById(id);
        model.addAttribute("user", user);
        return "user-detail";
    }
    
    @GetMapping("/new")
    public String showCreateForm(Model model) {
        model.addAttribute("user", new User());
        return "user-form";
    }
    
    @PostMapping
    public String createUser(@ModelAttribute @Valid User user, 
                            BindingResult result,
                            RedirectAttributes redirectAttributes) {
        if (result.hasErrors()) {
            return "user-form";
        }
        
        userService.createUser(user);
        redirectAttributes.addFlashAttribute("message", "User created successfully");
        return "redirect:/users";
    }
}
```

#### REST Controller

```java
@RestController
@RequestMapping("/api/users")
@Slf4j
public class UserRestController {
    
    private final UserService userService;
    
    @Autowired
    public UserRestController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping
    public ResponseEntity<List<UserDTO>> getAllUsers(
            @RequestParam(required = false) String name,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size) {
        
        Pageable pageable = PageRequest.of(page, size);
        Page<UserDTO> users = userService.findUsers(name, pageable);
        
        return ResponseEntity.ok()
            .header("X-Total-Count", String.valueOf(users.getTotalElements()))
            .body(users.getContent());
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUserById(@PathVariable Long id) {
        return userService.getUserById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ResponseEntity<UserDTO> createUser(
            @Valid @RequestBody CreateUserRequest request,
            UriComponentsBuilder uriBuilder) {
        
        UserDTO created = userService.createUser(request);
        
        URI location = uriBuilder
            .path("/api/users/{id}")
            .buildAndExpand(created.getId())
            .toUri();
        
        return ResponseEntity.created(location).body(created);
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

---

### 3. Request Mapping

**HTTP Method Annotations:**

```java
@RestController
@RequestMapping("/api/products")
public class ProductController {
    
    // GET /api/products
    @GetMapping
    public List<Product> getAllProducts() { }
    
    // GET /api/products/123
    @GetMapping("/{id}")
    public Product getProduct(@PathVariable Long id) { }
    
    // GET /api/products/search?name=laptop
    @GetMapping("/search")
    public List<Product> search(@RequestParam String name) { }
    
    // POST /api/products
    @PostMapping
    public Product createProduct(@RequestBody Product product) { }
    
    // PUT /api/products/123
    @PutMapping("/{id}")
    public Product updateProduct(@PathVariable Long id, @RequestBody Product product) { }
    
    // PATCH /api/products/123
    @PatchMapping("/{id}")
    public Product partialUpdate(@PathVariable Long id, @RequestBody Map<String, Object> updates) { }
    
    // DELETE /api/products/123
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteProduct(@PathVariable Long id) { }
}
```

**Request Parameters:**

```java
@RestController
public class SearchController {
    
    // Path variable
    @GetMapping("/users/{id}")
    public User getUser(@PathVariable Long id) { }
    
    // Query parameter
    @GetMapping("/users")
    public List<User> searchUsers(@RequestParam String name) { }
    
    // Optional parameter with default
    @GetMapping("/products")
    public List<Product> getProducts(
        @RequestParam(required = false, defaultValue = "0") int page,
        @RequestParam(required = false, defaultValue = "10") int size
    ) { }
    
    // Request header
    @GetMapping("/data")
    public Data getData(@RequestHeader("Authorization") String token) { }
    
    // Multiple path variables
    @GetMapping("/orders/{orderId}/items/{itemId}")
    public OrderItem getItem(
        @PathVariable Long orderId,
        @PathVariable Long itemId
    ) { }
    
    // Request body
    @PostMapping("/users")
    public User createUser(@RequestBody User user) { }
    
    // Matrix variables
    @GetMapping("/users/{id}")
    public User getUser(
        @PathVariable Long id,
        @MatrixVariable String lang
    ) { }
}
```

---

### 4. Exception Handling

**Global Exception Handler:**

```java
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(
            ResourceNotFoundException ex,
            WebRequest request) {
        
        log.error("Resource not found: {}", ex.getMessage());
        
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.NOT_FOUND.value())
            .error("Not Found")
            .message(ex.getMessage())
            .path(extractPath(request))
            .build();
        
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(
            MethodArgumentNotValidException ex) {
        
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error -> 
            errors.put(error.getField(), error.getDefaultMessage())
        );
        
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.BAD_REQUEST.value())
            .error("Validation Failed")
            .message("Invalid input data")
            .fieldErrors(errors)
            .build();
        
        return ResponseEntity.badRequest().body(error);
    }
    
    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<ErrorResponse> handleAccessDenied(
            AccessDeniedException ex) {
        
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.FORBIDDEN.value())
            .error("Forbidden")
            .message("You don't have permission to access this resource")
            .build();
        
        return ResponseEntity.status(HttpStatus.FORBIDDEN).body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGlobalException(
            Exception ex,
            WebRequest request) {
        
        log.error("Internal server error", ex);
        
        ErrorResponse error = ErrorResponse.builder()
            .timestamp(LocalDateTime.now())
            .status(HttpStatus.INTERNAL_SERVER_ERROR.value())
            .error("Internal Server Error")
            .message("An unexpected error occurred")
            .build();
        
        return ResponseEntity
            .status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(error);
    }
}
```

**Controller-Specific Exception Handler:**

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.getUserById(id);
    }
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<String> handleUserNotFound(UserNotFoundException ex) {
        return ResponseEntity
            .status(HttpStatus.NOT_FOUND)
            .body(ex.getMessage());
    }
}
```

---

### 5. Validation

**Entity Validation:**

```java
@Data
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
    @NotBlank(message = "Street is required")
    private String street;
    
    @NotBlank(message = "City is required")
    private String city;
    
    @Pattern(regexp = "^[0-9]{5}$", message = "Zip code must be 5 digits")
    private String zipCode;
}
```

**Controller with Validation:**

```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @PostMapping
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody CreateUserRequest request) {
        UserDTO user = userService.createUser(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }
}
```

---

### 6. Interceptors

**Custom Interceptor:**

```java
@Component
@Slf4j
public class LoggingInterceptor implements HandlerInterceptor {
    
    @Override
    public boolean preHandle(
            HttpServletRequest request,
            HttpServletResponse response,
            Object handler) {
        
        log.info("Request: {} {}", request.getMethod(), request.getRequestURI());
        request.setAttribute("startTime", System.currentTimeMillis());
        return true;
    }
    
    @Override
    public void postHandle(
            HttpServletRequest request,
            HttpServletResponse response,
            Object handler,
            ModelAndView modelAndView) {
        
        log.info("Response status: {}", response.getStatus());
    }
    
    @Override
    public void afterCompletion(
            HttpServletRequest request,
            HttpServletResponse response,
            Object handler,
            Exception ex) {
        
        long startTime = (Long) request.getAttribute("startTime");
        long duration = System.currentTimeMillis() - startTime;
        log.info("Request completed in {}ms", duration);
    }
}

@Configuration
public class WebMvcConfig implements WebMvcConfigurer {
    
    @Autowired
    private LoggingInterceptor loggingInterceptor;
    
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(loggingInterceptor)
            .addPathPatterns("/api/**")
            .excludePathPatterns("/api/public/**");
    }
}
```

---

## 🎯 Interview Questions

**Q1: Explain Spring MVC request processing flow**

**Answer:**
1. Client sends request to DispatcherServlet
2. DispatcherServlet consults HandlerMapping to find controller
3. HandlerMapping returns handler
4. DispatcherServlet calls controller method
5. Controller processes request and returns ModelAndView
6. DispatcherServlet consults ViewResolver
7. ViewResolver returns View
8. View renders response
9. Response sent to client

**Q2: Difference between @Controller and @RestController?**

**Answer:**
- `@Controller`: Returns view name (HTML pages)
- `@RestController`: Returns data (JSON/XML), equivalent to `@Controller + @ResponseBody`

Use @Controller for MVC apps, @RestController for REST APIs.

**Q3: How do you handle exceptions globally in Spring MVC?**

**Answer:**
Use `@RestControllerAdvice` or `@ControllerAdvice`:

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

## ✅ Practice Checklist

- [ ] Create MVC application with controllers
- [ ] Build REST API with CRUD operations
- [ ] Implement global exception handling
- [ ] Add validation with custom validators
- [ ] Create interceptors for logging
- [ ] Handle different content types
- [ ] Implement pagination and sorting
- [ ] Add async request processing

---

**👉 Next:** [Data Access & Transactions →](../03-data-access/README.md)

---

## 💡 Simple Explanation (In Plain English)

- `DispatcherServlet` is the front door: every HTTP request goes through it before your controller runs.
- `@RestController` returns JSON/XML directly; `@Controller` often returns a view name for server-rendered pages.
- Validation and exception handlers keep APIs consistent so clients always get predictable error shapes.
- Filters run before the servlet chain; interceptors run around controller execution—know both for security and logging.

## 🎯 Interview Quick Prep

### Q1: Walk through the Spring MVC request lifecycle.

**Simple Answer:** Client hits `DispatcherServlet` → `HandlerMapping` picks the controller method → controller calls services → result goes through `HttpMessageConverter` (REST) or `ViewResolver` (MVC). Mention where filters, interceptors, and `@ExceptionHandler` fit.

### Q2: `@Controller` vs `@RestController`?

**Simple Answer:** `@Controller` is for traditional MVC that returns view names. `@RestController` is `@Controller` + `@ResponseBody`, so return values serialize to the HTTP body (typical REST APIs). Use REST controllers for microservices and JSON APIs.

### Q3: How do you handle exceptions globally?

**Simple Answer:** Use `@ControllerAdvice` or `@RestControllerAdvice` with `@ExceptionHandler` methods mapped to exception types. Return consistent status codes and error DTOs; log server-side details, expose safe messages to clients.

### Q4: How does validation work in Spring MVC?

**Simple Answer:** Annotate request DTOs with Bean Validation (`@NotNull`, `@Email`, etc.) and add `@Valid` or `@Validated` on controller parameters. Spring returns 400 with binding errors; customize via exception handler for your API contract.

### Q5: What async or performance topics might interviewers ask?

**Simple Answer:** `Callable`/`DeferredResult` for async MVC, content negotiation with `produces`/`consumes`, and pagination with `Pageable`. For 3–5 years, also mention avoiding blocking calls on reactive stacks if the team uses WebFlux.

**Must-know for interviews:** DispatcherServlet flow, `@RestController` vs `@Controller`, and global exception handling with `@RestControllerAdvice`.

