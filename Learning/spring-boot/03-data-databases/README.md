# 🗄️ Data & Databases

**Phase 3: Master Data Persistence (1 Week)**

---

## 📖 Overview

Master data persistence with Spring Boot, covering JPA, repositories, transactions, caching, and database migrations. Learn how to build efficient, scalable data access layers.

---

## 🎯 Learning Objectives

✅ Spring Data JPA fundamentals  
✅ Repository patterns and query methods  
✅ Transaction management  
✅ Database connection pooling (HikariCP)  
✅ Flyway/Liquibase migrations  
✅ Query optimization and N+1 problem  
✅ Caching strategies (Redis, EhCache)  
✅ Multiple datasource configuration  

---

## 📚 Core Topics

### 1. Spring Data JPA

**Entity Example:**

```java
@Entity
@Table(name = "users", indexes = {
    @Index(name = "idx_email", columnList = "email"),
    @Index(name = "idx_status", columnList = "status")
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
    @Column(length = 20)
    private UserStatus status;
    
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Order> orders = new ArrayList<>();
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "department_id")
    private Department department;
    
    @ManyToMany
    @JoinTable(
        name = "user_roles",
        joinColumns = @JoinColumn(name = "user_id"),
        inverseJoinColumns = @JoinColumn(name = "role_id")
    )
    private Set<Role> roles = new HashSet<>();
    
    @CreatedDate
    @Column(nullable = false, updatable = false)
    private LocalDateTime createdAt;
    
    @LastModifiedDate
    private LocalDateTime updatedAt;
    
    @CreatedBy
    @Column(updatable = false)
    private String createdBy;
    
    @LastModifiedBy
    private String lastModifiedBy;
    
    @Version
    private Long version;
}
```

### 2. Repository Pattern

**Basic Repository:**

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    // Query methods
    Optional<User> findByEmail(String email);
    
    List<User> findByStatus(UserStatus status);
    
    List<User> findByNameContainingIgnoreCase(String name);
    
    List<User> findByCreatedAtBetween(LocalDateTime start, LocalDateTime end);
    
    // Count queries
    long countByStatus(UserStatus status);
    
    // Exists queries
    boolean existsByEmail(String email);
    
    // Delete queries
    void deleteByStatus(UserStatus status);
    
    // @Query with JPQL
    @Query("SELECT u FROM User u WHERE u.status = :status AND u.createdAt > :date")
    List<User> findActiveUsersAfterDate(
        @Param("status") UserStatus status,
        @Param("date") LocalDateTime date
    );
    
    // @Query with native SQL
    @Query(value = "SELECT * FROM users WHERE status = ?1 LIMIT ?2", nativeQuery = true)
    List<User> findTopNByStatus(String status, int limit);
    
    // Projections
    @Query("SELECT new com.example.dto.UserSummaryDTO(u.id, u.name, u.email) FROM User u")
    List<UserSummaryDTO> findAllSummaries();
    
    // Pagination and sorting
    Page<User> findByStatus(UserStatus status, Pageable pageable);
    
    Slice<User> findByNameStartingWith(String prefix, Pageable pageable);
    
    // Modifying queries
    @Modifying
    @Query("UPDATE User u SET u.status = :status WHERE u.id = :id")
    int updateUserStatus(@Param("id") Long id, @Param("status") UserStatus status);
}
```

### 3. Transaction Management

```java
@Service
@Transactional
@Slf4j
public class OrderService {
    
    private final OrderRepository orderRepository;
    private final UserRepository userRepository;
    private final PaymentService paymentService;
    
    // Read-only transaction (optimization)
    @Transactional(readOnly = true)
    public Optional<Order> getOrderById(Long id) {
        return orderRepository.findById(id);
    }
    
    // Default transaction (read-write)
    public Order createOrder(CreateOrderRequest request) {
        User user = userRepository.findById(request.getUserId())
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        
        Order order = Order.builder()
            .user(user)
            .items(request.getItems())
            .totalAmount(calculateTotal(request.getItems()))
            .status(OrderStatus.PENDING)
            .build();
        
        Order saved = orderRepository.save(order);
        
        // Process payment in same transaction
        paymentService.processPayment(saved.getId(), saved.getTotalAmount());
        
        return saved;
    }
    
    // Custom transaction settings
    @Transactional(
        propagation = Propagation.REQUIRES_NEW,
        isolation = Isolation.SERIALIZABLE,
        timeout = 30,
        rollbackFor = Exception.class
    )
    public void criticalOperation() {
        // This runs in a new transaction
    }
    
    // Programmatic transaction
    public void manualTransaction() {
        TransactionTemplate transactionTemplate = new TransactionTemplate(transactionManager);
        transactionTemplate.execute(status -> {
            try {
                // Your transactional code
                return null;
            } catch (Exception e) {
                status.setRollbackOnly();
                throw e;
            }
        });
    }
}
```

### 4. Database Migrations (Flyway)

**Configuration:**

```yaml
spring:
  flyway:
    enabled: true
    locations: classpath:db/migration
    baseline-on-migrate: true
    validate-on-migrate: true
```

**Migration Files:**

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

-- V2__create_orders_table.sql
CREATE TABLE orders (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    order_number VARCHAR(50) UNIQUE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- V3__add_department_to_users.sql
ALTER TABLE users ADD COLUMN department_id BIGINT;
ALTER TABLE users ADD CONSTRAINT fk_users_department 
    FOREIGN KEY (department_id) REFERENCES departments(id);
```

### 5. Connection Pooling (HikariCP)

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: ${DB_USER}
    password: ${DB_PASSWORD}
    driver-class-name: org.postgresql.Driver
    
    hikari:
      # Maximum number of connections in the pool
      maximum-pool-size: 20
      
      # Minimum number of idle connections
      minimum-idle: 5
      
      # Maximum lifetime of a connection (30 minutes)
      max-lifetime: 1800000
      
      # Connection timeout (30 seconds)
      connection-timeout: 30000
      
      # Idle timeout (10 minutes)
      idle-timeout: 600000
      
      # Pool name for logging
      pool-name: MyHikariPool
      
      # Connection test query
      connection-test-query: SELECT 1
      
      # Leak detection threshold (2 minutes)
      leak-detection-threshold: 120000
```

### 6. Caching

**Redis Configuration:**

```yaml
spring:
  redis:
    host: localhost
    port: 6379
    password: ${REDIS_PASSWORD}
    timeout: 2000
    lettuce:
      pool:
        max-active: 8
        max-idle: 8
        min-idle: 0
        max-wait: -1ms
  
  cache:
    type: redis
    redis:
      time-to-live: 3600000  # 1 hour
      cache-null-values: false
```

**Cache Configuration:**

```java
@Configuration
@EnableCaching
public class CacheConfig {
    
    @Bean
    public RedisCacheConfiguration cacheConfiguration() {
        return RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(60))
            .disableCachingNullValues()
            .serializeValuesWith(
                RedisSerializationContext.SerializationPair.fromSerializer(
                    new GenericJackson2JsonRedisSerializer()
                )
            );
    }
    
    @Bean
    public CacheManager cacheManager(RedisConnectionFactory connectionFactory) {
        RedisCacheManager cacheManager = RedisCacheManager.builder(connectionFactory)
            .cacheDefaults(cacheConfiguration())
            .withCacheConfiguration("users", 
                RedisCacheConfiguration.defaultCacheConfig()
                    .entryTtl(Duration.ofMinutes(30)))
            .withCacheConfiguration("products",
                RedisCacheConfiguration.defaultCacheConfig()
                    .entryTtl(Duration.ofHours(2)))
            .build();
        
        return cacheManager;
    }
}
```

**Using Cache:**

```java
@Service
@Slf4j
public class UserService {
    
    @Cacheable(value = "users", key = "#id")
    public User getUserById(Long id) {
        log.info("Fetching user from database: {}", id);
        return userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }
    
    @CachePut(value = "users", key = "#result.id")
    public User updateUser(Long id, UpdateUserRequest request) {
        log.info("Updating user and cache: {}", id);
        User user = getUserById(id);
        // Update user
        return userRepository.save(user);
    }
    
    @CacheEvict(value = "users", key = "#id")
    public void deleteUser(Long id) {
        log.info("Deleting user and evicting cache: {}", id);
        userRepository.deleteById(id);
    }
    
    @CacheEvict(value = "users", allEntries = true)
    public void clearAllUsersCache() {
        log.info("Clearing all users cache");
    }
    
    @Caching(
        cacheable = @Cacheable(value = "users", key = "#email"),
        put = @CachePut(value = "users", key = "#result.id")
    )
    public User getUserByEmail(String email) {
        return userRepository.findByEmail(email)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }
}
```

### 7. Query Optimization

**N+1 Problem Solution:**

```java
// ❌ Bad: N+1 problem
@Transactional(readOnly = true)
public List<Order> getAllOrders() {
    return orderRepository.findAll(); // 1 query
    // Each order.getUser() triggers another query - N queries
}

// ✅ Good: Fetch join
@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {
    
    @Query("SELECT o FROM Order o JOIN FETCH o.user")
    List<Order> findAllWithUser();
    
    @Query("SELECT o FROM Order o " +
           "LEFT JOIN FETCH o.user " +
           "LEFT JOIN FETCH o.items")
    List<Order> findAllWithUserAndItems();
    
    @EntityGraph(attributePaths = {"user", "items"})
    List<Order> findAll();
}

// ✅ Good: Batch fetching
@Entity
public class Order {
    @ManyToOne(fetch = FetchType.LAZY)
    @BatchSize(size = 10)
    private User user;
}
```

---

## 💻 Configuration Examples

### Multiple DataSources

```java
@Configuration
public class DatabaseConfig {
    
    // Primary DataSource
    @Primary
    @Bean(name = "primaryDataSource")
    @ConfigurationProperties(prefix = "spring.datasource.primary")
    public DataSource primaryDataSource() {
        return DataSourceBuilder.create().build();
    }
    
    @Primary
    @Bean(name = "primaryEntityManagerFactory")
    public LocalContainerEntityManagerFactoryBean primaryEntityManagerFactory(
            EntityManagerFactoryBuilder builder,
            @Qualifier("primaryDataSource") DataSource dataSource) {
        return builder
            .dataSource(dataSource)
            .packages("com.example.primary.model")
            .persistenceUnit("primary")
            .build();
    }
    
    @Primary
    @Bean(name = "primaryTransactionManager")
    public PlatformTransactionManager primaryTransactionManager(
            @Qualifier("primaryEntityManagerFactory") EntityManagerFactory entityManagerFactory) {
        return new JpaTransactionManager(entityManagerFactory);
    }
    
    // Secondary DataSource
    @Bean(name = "secondaryDataSource")
    @ConfigurationProperties(prefix = "spring.datasource.secondary")
    public DataSource secondaryDataSource() {
        return DataSourceBuilder.create().build();
    }
    
    @Bean(name = "secondaryEntityManagerFactory")
    public LocalContainerEntityManagerFactoryBean secondaryEntityManagerFactory(
            EntityManagerFactoryBuilder builder,
            @Qualifier("secondaryDataSource") DataSource dataSource) {
        return builder
            .dataSource(dataSource)
            .packages("com.example.secondary.model")
            .persistenceUnit("secondary")
            .build();
    }
    
    @Bean(name = "secondaryTransactionManager")
    public PlatformTransactionManager secondaryTransactionManager(
            @Qualifier("secondaryEntityManagerFactory") EntityManagerFactory entityManagerFactory) {
        return new JpaTransactionManager(entityManagerFactory);
    }
}
```

---

## 🎯 Interview Questions

**Q1: What is the N+1 problem and how do you solve it?**

A: N+1 happens when you fetch a list of entities (1 query), then for each entity, another query is triggered to fetch related data (N queries).

Solutions:
- Use JOIN FETCH in JPQL
- Use @EntityGraph
- Enable batch fetching with @BatchSize

**Q2: Difference between @OneToMany and @ManyToOne?**

A: 
- @OneToMany: One entity has many related entities (parent side)
- @ManyToOne: Many entities reference one entity (child side, owns the FK)

**Q3: What are transaction propagation types?**

A:
- REQUIRED (default): Use existing or create new
- REQUIRES_NEW: Always create new transaction
- SUPPORTS: Use existing, or non-transactional
- NOT_SUPPORTED: Run non-transactionally
- MANDATORY: Must have existing transaction
- NEVER: Must not run in transaction
- NESTED: Nested within existing transaction

---

## ✅ Practice Checklist

- [ ] Create entities with relationships
- [ ] Implement repository with query methods
- [ ] Configure HikariCP properly
- [ ] Set up Flyway migrations
- [ ] Implement caching with Redis
- [ ] Solve N+1 query problems
- [ ] Configure multiple datasources
- [ ] Implement auditing
- [ ] Handle optimistic locking
- [ ] Write efficient queries

---

**👉 [Phase 4: Security & Production →](../04-security-production/README.md)**

