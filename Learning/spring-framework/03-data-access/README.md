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

