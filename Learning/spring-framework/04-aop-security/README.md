# 🔒 AOP & Security

**Phase 4: Advanced Enterprise Features (1 Week)**

---

## 📖 Overview

Master Aspect-Oriented Programming (AOP) for cross-cutting concerns and Spring Security for application security.

---

## 🎯 Learning Objectives

✅ AOP concepts and terminology  
✅ Create custom aspects  
✅ Spring Security architecture  
✅ Authentication & Authorization  
✅ Method security  
✅ OAuth2 & JWT  

---

## 📚 Core Topics

### 1. Aspect-Oriented Programming (AOP)

**Key Concepts:**
- **Aspect**: Modularization of cross-cutting concern
- **Join Point**: Point in execution (method call)
- **Advice**: Action taken at join point
- **Pointcut**: Expression matching join points
- **Weaving**: Linking aspects with objects

**Advice Types:**

```java
@Aspect
@Component
@Slf4j
public class LoggingAspect {
    
    // Before advice
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        log.info("Executing: {}", joinPoint.getSignature().getName());
    }
    
    // After returning advice
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", 
                    returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        log.info("Method {} returned: {}", joinPoint.getSignature().getName(), result);
    }
    
    // After throwing advice
    @AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", 
                   throwing = "error")
    public void logAfterThrowing(JoinPoint joinPoint, Throwable error) {
        log.error("Method {} threw exception: {}", 
            joinPoint.getSignature().getName(), error.getMessage());
    }
    
    // After (finally) advice
    @After("execution(* com.example.service.*.*(..))")
    public void logAfter(JoinPoint joinPoint) {
        log.info("Method {} completed", joinPoint.getSignature().getName());
    }
    
    // Around advice
    @Around("execution(* com.example.service.*.*(..))")
    public Object logAround(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        
        log.info("Starting: {}", joinPoint.getSignature().getName());
        
        try {
            Object result = joinPoint.proceed();
            long duration = System.currentTimeMillis() - start;
            log.info("Completed: {} in {}ms", joinPoint.getSignature().getName(), duration);
            return result;
        } catch (Exception e) {
            log.error("Error in {}: {}", joinPoint.getSignature().getName(), e.getMessage());
            throw e;
        }
    }
}
```

**Pointcut Expressions:**

```java
@Aspect
@Component
public class PointcutExamples {
    
    // Specific method
    @Pointcut("execution(public String com.example.service.UserService.getName())")
    public void specificMethod() {}
    
    // All methods in class
    @Pointcut("execution(* com.example.service.UserService.*(..))")
    public void allMethodsInClass() {}
    
    // All methods in package
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void allMethodsInPackage() {}
    
    // All methods with @Transactional
    @Pointcut("@annotation(org.springframework.transaction.annotation.Transactional)")
    public void transactionalMethods() {}
    
    // All methods in classes with @Service
    @Pointcut("within(@org.springframework.stereotype.Service *)")
    public void serviceMethods() {}
    
    // Combine pointcuts
    @Pointcut("allMethodsInPackage() && !specificMethod()")
    public void combined() {}
}
```

---

### 2. Spring Security Basics

**Security Configuration:**

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .requestMatchers("/api/user/**").hasAnyRole("USER", "ADMIN")
                .anyRequest().authenticated()
            )
            .httpBasic(Customizer.withDefaults())
            .formLogin(form -> form
                .loginPage("/login")
                .defaultSuccessUrl("/dashboard")
                .permitAll()
            )
            .logout(logout -> logout
                .logoutUrl("/logout")
                .logoutSuccessUrl("/login?logout")
                .permitAll()
            );
        
        return http.build();
    }
    
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

**UserDetailsService:**

```java
@Service
public class CustomUserDetailsService implements UserDetailsService {
    
    @Autowired
    private UserRepository userRepository;
    
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByEmail(username)
            .orElseThrow(() -> new UsernameNotFoundException("User not found"));
        
        return org.springframework.security.core.userdetails.User.builder()
            .username(user.getEmail())
            .password(user.getPassword())
            .roles(user.getRoles().stream()
                .map(Role::getName)
                .toArray(String[]::new))
            .build();
    }
}
```

---

### 3. Method Security

```java
@Configuration
@EnableMethodSecurity
public class MethodSecurityConfig {
}

@Service
public class UserService {
    
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
    
    @PreAuthorize("hasRole('ADMIN') or #id == authentication.principal.id")
    public User updateUser(Long id, User user) {
        // Update logic
    }
    
    @PostAuthorize("returnObject.owner == authentication.name")
    public Document getDocument(Long id) {
        return documentRepository.findById(id).orElseThrow();
    }
    
    @Secured({"ROLE_ADMIN", "ROLE_MANAGER"})
    public void approveOrder(Long orderId) {
        // Approve logic
    }
}
```

---

### 4. JWT Authentication

**JWT Service:**

```java
@Service
public class JwtService {
    
    @Value("${jwt.secret}")
    private String secret;
    
    @Value("${jwt.expiration}")
    private Long expiration;
    
    public String generateToken(UserDetails userDetails) {
        return Jwts.builder()
            .setSubject(userDetails.getUsername())
            .setIssuedAt(new Date())
            .setExpiration(new Date(System.currentTimeMillis() + expiration))
            .signWith(getSigningKey(), SignatureAlgorithm.HS256)
            .compact();
    }
    
    public String extractUsername(String token) {
        return extractClaim(token, Claims::getSubject);
    }
    
    public boolean isTokenValid(String token, UserDetails userDetails) {
        final String username = extractUsername(token);
        return (username.equals(userDetails.getUsername()) && !isTokenExpired(token));
    }
    
    private boolean isTokenExpired(String token) {
        return extractExpiration(token).before(new Date());
    }
    
    private Date extractExpiration(String token) {
        return extractClaim(token, Claims::getExpiration);
    }
    
    private <T> T extractClaim(String token, Function<Claims, T> claimsResolver) {
        final Claims claims = extractAllClaims(token);
        return claimsResolver.apply(claims);
    }
    
    private Claims extractAllClaims(String token) {
        return Jwts.parserBuilder()
            .setSigningKey(getSigningKey())
            .build()
            .parseClaimsJws(token)
            .getBody();
    }
    
    private Key getSigningKey() {
        byte[] keyBytes = Decoders.BASE64.decode(secret);
        return Keys.hmacShaKeyFor(keyBytes);
    }
}
```

---

## 🎯 Interview Questions

**Q1: What is AOP and when to use it?**

**Answer:**
AOP separates cross-cutting concerns (logging, security, transactions) from business logic.

Use cases:
- Logging
- Transaction management
- Security checks
- Performance monitoring
- Caching

**Q2: Difference between @PreAuthorize and @Secured?**

**Answer:**
- `@PreAuthorize`: Supports SpEL expressions, more flexible
- `@Secured`: Only role-based, simpler

Example:
```java
@PreAuthorize("hasRole('ADMIN') or #id == principal.id")
vs
@Secured("ROLE_ADMIN")
```

---

**👉 Next:** [Interview Questions →](../interview-questions/README.md)

---

## 💡 Simple Explanation (In Plain English)

- AOP lets you add logging, metrics, or security around many methods without copying the same code everywhere.
- An aspect = pointcut (where) + advice (when: before/after/around) applied by Spring proxies.
- Spring Security is a filter chain: authenticate first (who you are), then authorize (what you can do).
- JWT/OAuth2 are common in APIs; session cookies still matter in traditional web apps.

## 🎯 Interview Quick Prep

### Q1: What is AOP and when should you use it?

**Simple Answer:** AOP applies cross-cutting behavior (logging, tracing, retries) across many join points via aspects. Use when the concern is not core business logic but must run consistently; avoid overusing AOP where a simple service wrapper is clearer.

### Q2: What advice types exist and which is most powerful?

**Simple Answer:** Before, after returning, after throwing, after (finally), and around. `@Around` can proceed or skip the method and measure time—most flexible but easiest to misuse; keep aspects thin.

### Q3: How does Spring Security protect an HTTP request?

**Simple Answer:** A chain of servlet filters checks authentication (credentials/token), builds `SecurityContext`, then authorization rules (`authorizeHttpRequests`, method security). Unauthenticated/unauthorized requests are rejected before controllers run.

### Q4: Authentication vs authorization?

**Simple Answer:** Authentication verifies identity (login, JWT validation). Authorization checks permissions/roles for a resource (`hasRole`, `@PreAuthorize`). You can be authenticated but still forbidden—that is 401 vs 403 in APIs.

### Q5: JWT basics for REST interviews?

**Simple Answer:** Server signs a token with claims; clients send `Authorization: Bearer`. Validate signature, expiry, and issuer; store secrets safely. Mention refresh tokens, stateless scaling, and that revocation needs extra design (blocklist, short TTL).

**Must-know for interviews:** AOP terminology, filter-chain security model, and auth vs authorization with JWT tradeoffs.

