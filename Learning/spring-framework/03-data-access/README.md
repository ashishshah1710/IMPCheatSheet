# 🗄️ Data Access & Transactions

**Phase 3: Master Data Persistence (1 Week)**

---

## 📖 Overview

Master Spring's data access capabilities including JPA, JDBC Template, transactions, and repository patterns.

---

## 🎯 Learning Objectives

✅ Spring Data JPA  
✅ JDBC Template  
✅ Transaction management  
✅ Transaction propagation & isolation  
✅ Repository pattern  
✅ Query optimization  

---

## 📚 Core Topics

### 1. Spring Data JPA

**Repository Interface:**

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    // Query methods
    Optional<User> findByEmail(String email);
    List<User> findByStatus(UserStatus status);
    Page<User> findByNameContaining(String name, Pageable pageable);
    
    // @Query annotation
    @Query("SELECT u FROM User u WHERE u.age > :age")
    List<User> findUsersOlderThan(@Param("age") int age);
    
    // Native query
    @Query(value = "SELECT * FROM users WHERE status = ?1", nativeQuery = true)
    List<User> findByStatusNative(String status);
    
    // Modifying query
    @Modifying
    @Query("UPDATE User u SET u.status = :status WHERE u.id = :id")
    int updateUserStatus(@Param("id") Long id, @Param("status") UserStatus status);
}
```

---

### 2. Transaction Management

**@Transactional:**

```java
@Service
@Transactional
public class UserService {
    
    @Transactional(readOnly = true)
    public User getUserById(Long id) {
        return userRepository.findById(id).orElseThrow();
    }
    
    public User createUser(User user) {
        return userRepository.save(user);
    }
    
    @Transactional(
        propagation = Propagation.REQUIRES_NEW,
        isolation = Isolation.SERIALIZABLE,
        timeout = 30,
        rollbackFor = Exception.class
    )
    public void criticalOperation() {
        // Runs in new transaction
    }
}
```

**Transaction Propagation:**

| Propagation | Behavior |
|------------|----------|
| REQUIRED | Use existing or create new |
| REQUIRES_NEW | Always create new |
| SUPPORTS | Use existing if available |
| NOT_SUPPORTED | Run non-transactionally |
| MANDATORY | Must have transaction |
| NEVER | Must not have transaction |
| NESTED | Nested transaction |

---

### 3. JDBC Template

```java
@Repository
public class UserJdbcRepository {
    
    @Autowired
    private JdbcTemplate jdbcTemplate;
    
    public User findById(Long id) {
        String sql = "SELECT * FROM users WHERE id = ?";
        return jdbcTemplate.queryForObject(sql, new UserRowMapper(), id);
    }
    
    public List<User> findAll() {
        String sql = "SELECT * FROM users";
        return jdbcTemplate.query(sql, new UserRowMapper());
    }
    
    public int create(User user) {
        String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
        return jdbcTemplate.update(sql, user.getName(), user.getEmail());
    }
    
    private static class UserRowMapper implements RowMapper<User> {
        @Override
        public User mapRow(ResultSet rs, int rowNum) throws SQLException {
            User user = new User();
            user.setId(rs.getLong("id"));
            user.setName(rs.getString("name"));
            user.setEmail(rs.getString("email"));
            return user;
        }
    }
}
```

---

## 🎯 Interview Questions

**Q: Explain transaction propagation types**

**A:** See table above. Most common: REQUIRED (default) and REQUIRES_NEW (for independent transactions).

---

**👉 Next:** [AOP & Security →](../04-aop-security/README.md)

---

## 💡 Simple Explanation (In Plain English)

- Spring Data JPA hides boilerplate CRUD; you still own query design and transaction boundaries.
- `@Transactional` wraps methods in a database transaction—rollback on runtime exceptions by default.
- Propagation decides whether a method joins an existing transaction or starts a new one.
- N+1 queries and wrong isolation levels are classic production bugs interviewers love to discuss.

## 🎯 Interview Quick Prep

### Q1: How does `@Transactional` work under the hood?

**Simple Answer:** Spring creates a proxy around your bean. When a `@Transactional` method is called, the proxy starts/commits/rolls back a transaction via `PlatformTransactionManager`. Self-invocation (calling `@Transactional` from same class) bypasses the proxy—common interview trap.

### Q2: Explain transaction propagation `REQUIRED` vs `REQUIRES_NEW`.

**Simple Answer:** `REQUIRED` (default) joins the caller’s transaction or creates one if none exists. `REQUIRES_NEW` always suspends the current transaction and opens a new one—use for audit/logging that must commit even if the outer transaction rolls back.

### Q3: What is the N+1 problem and how do you fix it?

**Simple Answer:** Loading N parent rows triggers N extra queries for children (lazy loading). Fix with `JOIN FETCH`, `@EntityGraph`, batch fetching, or DTO projections. Show you profile SQL/logs, not only know the term.

### Q4: When use JDBC Template vs JPA?

**Simple Answer:** JPA fits domain models and standard CRUD with relationships. JDBC Template fits bulk operations, complex reporting SQL, or legacy schemas where ORM overhead hurts. Many teams use both in the same app.

### Q5: Optimistic vs pessimistic locking?

**Simple Answer:** Optimistic uses a version column—conflicts fail on update (good for read-heavy). Pessimistic locks rows in the DB during the transaction (good for scarce resources). Pick based on contention and UX for retries.

**Must-know for interviews:** `@Transactional` proxy/self-invocation, propagation types, and N+1 causes plus fixes.

