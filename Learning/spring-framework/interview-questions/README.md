# 💼 Spring Framework Interview Questions

**Comprehensive Interview Preparation**

---

## Core Spring Questions

### Q1: What is Dependency Injection?

**Answer:** DI is a design pattern where objects receive their dependencies from external sources rather than creating them. Spring IoC container injects dependencies into beans.

**Types:**
- Constructor Injection (recommended)
- Setter Injection
- Field Injection (avoid)

---

### Q2: Explain bean scopes

**Answer:**

| Scope | Description |
|-------|-------------|
| singleton | One instance per container (default) |
| prototype | New instance each time |
| request | One per HTTP request |
| session | One per HTTP session |
| application | One per ServletContext |

---

### Q3: How does Spring resolve circular dependencies?

**Answer:** Spring uses three-level cache:
1. Fully initialized beans
2. Beans being initialized
3. Bean factories

Works with singleton + setter injection, NOT constructor injection.

---

### Q4: @Component vs @Service vs @Repository?

**Answer:**
- `@Component`: Generic stereotype
- `@Service`: Business logic layer
- `@Repository`: Data access layer (adds exception translation)

All are specialized `@Component` annotations for semantic clarity.

---

## Spring MVC Questions

### Q5: Explain Spring MVC request flow

**Answer:**
1. DispatcherServlet receives request
2. HandlerMapping finds controller
3. Controller processes request
4. Returns ModelAndView
5. ViewResolver resolves view
6. View renders response

---

### Q6: Difference between @Controller and @RestController?

**Answer:**
- `@Controller`: Returns view names (MVC)
- `@RestController`: Returns data (`@Controller + @ResponseBody`)

---

## Transaction Questions

### Q7: Explain @Transactional

**Answer:** Declarative transaction management. Wraps method in transaction.

**Attributes:**
- `propagation`: How transactions propagate
- `isolation`: Transaction isolation level
- `readOnly`: Optimization for read operations
- `rollbackFor`: Which exceptions trigger rollback

---

### Q8: Transaction propagation types?

**Answer:**
- **REQUIRED**: Use existing or create new (default)
- **REQUIRES_NEW**: Always create new
- **SUPPORTS**: Use if available, else non-transactional
- **MANDATORY**: Must have transaction
- **NEVER**: Must not have transaction

---

## AOP Questions

### Q9: What is AOP?

**Answer:** Aspect-Oriented Programming modularizes cross-cutting concerns.

**Terms:**
- **Aspect**: Cross-cutting concern module
- **Join Point**: Point in execution
- **Advice**: Action at join point
- **Pointcut**: Expression matching join points

**Advice Types:**
- @Before
- @After
- @AfterReturning
- @AfterThrowing
- @Around

---

### Q10: When to use AOP?

**Answer:**
- Logging
- Security
- Transaction management
- Performance monitoring
- Caching
- Error handling

---

## Security Questions

### Q11: How does Spring Security work?

**Answer:** Filter chain intercepts requests:
1. Authentication Filter
2. AuthenticationManager authenticates
3. SecurityContext stores authentication
4. Authorization checks
5. Access granted/denied

---

### Q12: JWT vs Session authentication?

**Answer:**

| JWT | Session |
|-----|---------|
| Stateless | Stateful |
| Scalable | Less scalable |
| No server storage | Server storage |
| Cross-domain friendly | Same domain |

---

## Scenario-Based Questions

### Q13: Application slow to start. How to fix?

**Answer:**
1. Enable lazy initialization
2. Profile unused beans
3. Optimize auto-configuration
4. Use `@Lazy` annotation
5. Check circular dependencies

---

### Q14: How to handle high traffic?

**Answer:**
1. Caching (Redis)
2. Connection pooling
3. Async processing
4. Load balancing
5. Database optimization
6. CDN for static content

---

### Q15: N+1 query problem solution?

**Answer:**
- Use JOIN FETCH in JPQL
- @EntityGraph
- @BatchSize annotation
- Query optimization

---

**[← Back to Main](../README.md)**

---

## 💡 Simple Explanation (In Plain English)

- This folder is your rapid-review bank: core Spring, MVC, data, and scenario questions together.
- Interviewers at 3–5 years want reasoning and tradeoffs, not definitions copied from docs.
- Practice explaining one real bug you fixed (transactions, security, performance) per topic area.
- Link answers to layers: controller → service → repository → database.

## 🎯 Interview Quick Prep

### Q1: How do you structure a strong answer to “What is Dependency Injection?”

**Simple Answer:** Define IoC/DI in one sentence, name constructor injection as default, and give a testability example (mock repository in a unit test). End with a benefit you saw in production—faster feature swaps or cleaner modules.

### Q2: What is a good bean-scope answer in under 30 seconds?

**Simple Answer:** Default singleton for stateless beans; prototype when each consumer needs its own instance; web scopes for per-request/session state. Add when you chose prototype to avoid shared mutable state bugs.

### Q3: How do you explain `@Transactional` without sounding vague?

**Simple Answer:** Proxy + transaction manager, default rollback on runtime exceptions, propagation/isolation knobs, and the self-invocation pitfall. Mention one incident: partial commit, long lock, or read-only optimization with `readOnly = true`.

### Q4: Typical Spring MVC whiteboard question?

**Simple Answer:** Draw DispatcherServlet → controller → service → repo, note filters and `@RestControllerAdvice`. Contrast `@Controller` (views) vs `@RestController` (JSON body).

### Q5: Scenario: “API is slow under load”—where do you start?

**Simple Answer:** Metrics and traces, DB query plan/N+1, pool exhaustion, missing indexes, synchronous external calls, and cache misuse. Show structured debugging—not random tuning.

**Must-know for interviews:** Short, layered answers with one real production example per major Spring topic.


