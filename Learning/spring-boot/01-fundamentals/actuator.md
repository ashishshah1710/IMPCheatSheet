# Spring Boot Actuator

## Overview

Spring Boot Actuator provides production-ready features to help you monitor and manage your application. It includes built-in endpoints for health checks, metrics, application info, and more.

## Setup

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

## Built-in Endpoints

| Endpoint | Description |
|----------|-------------|
| `/actuator/health` | Application health information |
| `/actuator/info` | Application information |
| `/actuator/metrics` | Application metrics |
| `/actuator/metrics/{name}` | Specific metric details |
| `/actuator/env` | Environment properties |
| `/actuator/loggers` | Logger configuration |
| `/actuator/loggers/{name}` | Specific logger level |
| `/actuator/httptrace` | HTTP request trace |
| `/actuator/threaddump` | Thread dump |
| `/actuator/heapdump` | Heap dump (downloads file) |
| `/actuator/beans` | All Spring beans |
| `/actuator/mappings` | All @RequestMapping paths |
| `/actuator/configprops` | @ConfigurationProperties |
| `/actuator/conditions` | Auto-configuration report |
| `/actuator/scheduledtasks` | Scheduled tasks |
| `/actuator/shutdown` | Graceful shutdown (disabled by default) |

## Configuration

### Expose Endpoints

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
        # Or expose all (not recommended for production)
        # include: '*'
  
  endpoint:
    health:
      show-details: always
      show-components: always
    shutdown:
      enabled: true  # Enable shutdown endpoint
```

### Base Path

```yaml
management:
  endpoints:
    web:
      base-path: /manage  # Default is /actuator
```

## Health Checks

### Default Health

```bash
curl http://localhost:8080/actuator/health
```

```json
{
  "status": "UP",
  "components": {
    "diskSpace": {
      "status": "UP",
      "details": {
        "total": 499963174912,
        "free": 180024532992,
        "threshold": 10485760,
        "exists": true
      }
    },
    "db": {
      "status": "UP",
      "details": {
        "database": "PostgreSQL",
        "validationQuery": "isValid()"
      }
    },
    "ping": {
      "status": "UP"
    }
  }
}
```

### Custom Health Indicator

```java
@Component
public class CustomHealthIndicator implements HealthIndicator {
    
    @Autowired
    private ExternalService externalService;
    
    @Override
    public Health health() {
        try {
            externalService.check();
            return Health.up()
                .withDetail("service", "External Service")
                .withDetail("status", "Available")
                .withDetail("responseTime", "120ms")
                .build();
        } catch (Exception e) {
            return Health.down()
                .withDetail("service", "External Service")
                .withDetail("status", "Unavailable")
                .withDetail("error", e.getMessage())
                .build();
        }
    }
}
```

### Health Groups

```yaml
management:
  endpoint:
    health:
      group:
        liveness:
          include: livenessProbe
        readiness:
          include: readinessProbe,db,redis
```

Access:
- `/actuator/health/liveness`
- `/actuator/health/readiness`

## Metrics

### Common Metrics

```bash
# All metrics
curl http://localhost:8080/actuator/metrics

# Specific metric
curl http://localhost:8080/actuator/metrics/jvm.memory.used
curl http://localhost:8080/actuator/metrics/http.server.requests
```

### Built-in Metrics

**JVM Metrics:**
- `jvm.memory.used`
- `jvm.memory.max`
- `jvm.threads.live`
- `jvm.gc.pause`

**System Metrics:**
- `system.cpu.usage`
- `system.cpu.count`
- `process.uptime`

**Application Metrics:**
- `http.server.requests`
- `tomcat.sessions.active.current`
- `hikaricp.connections.active`
- `logback.events`

### Custom Metrics

```java
@Service
public class MyService {
    
    private final MeterRegistry meterRegistry;
    private final Counter orderCounter;
    private final Timer orderTimer;
    
    public MyService(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
        
        // Counter
        this.orderCounter = Counter.builder("orders.placed")
            .description("Total orders placed")
            .tag("type", "online")
            .register(meterRegistry);
        
        // Timer
        this.orderTimer = Timer.builder("order.processing.time")
            .description("Order processing time")
            .register(meterRegistry);
    }
    
    public void placeOrder(Order order) {
        orderTimer.record(() -> {
            // Process order
            processOrder(order);
            orderCounter.increment();
        });
    }
    
    // Gauge
    @Scheduled(fixedRate = 60000)
    public void updatePendingOrders() {
        Gauge.builder("orders.pending", this, MyService::getPendingOrderCount)
            .description("Pending orders count")
            .register(meterRegistry);
    }
    
    private int getPendingOrderCount() {
        // Return pending order count
        return 0;
    }
}
```

### Using @Timed

```java
@RestController
@RequestMapping("/api")
@Timed  // Metrics for all endpoints
public class UserController {
    
    @GetMapping("/users")
    @Timed(value = "users.get.all", description = "Get all users")
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }
    
    @PostMapping("/users")
    @Timed(value = "users.create", percentiles = {0.5, 0.95, 0.99})
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }
}
```

## Application Info

### Configuration

```yaml
info:
  app:
    name: My Application
    description: Spring Boot application
    version: @project.version@
    encoding: @project.build.sourceEncoding@
    java:
      version: @java.version@

management:
  info:
    env:
      enabled: true
    git:
      mode: full
    build:
      enabled: true
```

### Custom Info Contributor

```java
@Component
public class CustomInfoContributor implements InfoContributor {
    
    @Override
    public void contribute(Info.Builder builder) {
        Map<String, Object> details = new HashMap<>();
        details.put("activeUsers", 1523);
        details.put("lastDeployment", LocalDateTime.now());
        details.put("features", Arrays.asList("feature1", "feature2"));
        
        builder.withDetail("app", details);
    }
}
```

## Custom Endpoints

### Read-Only Endpoint

```java
@Endpoint(id = "custom")
@Component
public class CustomEndpoint {
    
    @ReadOperation
    public Map<String, Object> customInfo() {
        Map<String, Object> info = new HashMap<>();
        info.put("version", "1.0.0");
        info.put("status", "active");
        info.put("timestamp", System.currentTimeMillis());
        return info;
    }
}
```

### Read/Write Endpoint

```java
@Endpoint(id = "feature")
@Component
public class FeatureEndpoint {
    
    private Map<String, Boolean> features = new HashMap<>();
    
    @ReadOperation
    public Map<String, Boolean> getFeatures() {
        return features;
    }
    
    @ReadOperation
    public Boolean getFeature(@Selector String name) {
        return features.getOrDefault(name, false);
    }
    
    @WriteOperation
    public void updateFeature(@Selector String name, Boolean enabled) {
        features.put(name, enabled);
    }
    
    @DeleteOperation
    public void deleteFeature(@Selector String name) {
        features.remove(name);
    }
}
```

## Prometheus Integration

### Setup

```xml
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
```

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  metrics:
    export:
      prometheus:
        enabled: true
    tags:
      application: ${spring.application.name}
```

### Scrape Configuration

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'spring-boot-app'
    metrics_path: '/actuator/prometheus'
    static_configs:
      - targets: ['localhost:8080']
```

## Security

### Secure Endpoints

```java
@Configuration
public class ActuatorSecurity {
    
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .requestMatcher(EndpointRequest.toAnyEndpoint())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers(EndpointRequest.to("health", "info"))
                    .permitAll()
                .requestMatchers(EndpointRequest.toAnyEndpoint())
                    .hasRole("ADMIN")
            )
            .httpBasic(Customizer.withDefaults());
        
        return http.build();
    }
}
```

### Using Properties

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info
      
spring:
  security:
    user:
      name: admin
      password: secret
```

## Monitoring with Micrometer

### Application Tags

```yaml
management:
  metrics:
    tags:
      application: ${spring.application.name}
      environment: ${spring.profiles.active}
      region: us-east-1
```

### Timer Example

```java
@Service
public class OrderService {
    
    private final MeterRegistry meterRegistry;
    
    public OrderService(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
    }
    
    public Order processOrder(Order order) {
        return Timer
            .builder("order.processing")
            .tag("type", order.getType())
            .register(meterRegistry)
            .record(() -> {
                // Process order
                return performProcessing(order);
            });
    }
}
```

## Best Practices

### 1. Limit Exposed Endpoints in Production

```yaml
# Production
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
```

### 2. Secure Sensitive Endpoints

```java
.requestMatchers(EndpointRequest.to("heapdump", "threaddump", "env"))
    .hasRole("ADMIN")
```

### 3. Use Health Groups

```yaml
management:
  endpoint:
    health:
      group:
        liveness:
          include: ping
        readiness:
          include: db,redis,customService
```

### 4. Add Custom Metrics

```java
// Business metrics
Counter.builder("orders.completed")
Timer.builder("payment.processing.time")
Gauge.builder("inventory.stock.level")
```

### 5. Configure Appropriate Detail Levels

```yaml
# Development
management:
  endpoint:
    health:
      show-details: always

# Production
management:
  endpoint:
    health:
      show-details: when-authorized
```

## Interview Questions

**Q: What is Spring Boot Actuator?**

A: Production-ready features for monitoring and managing applications. Includes endpoints for health checks, metrics, environment info, etc.

**Q: How do you secure Actuator endpoints?**

A:
1. Use Spring Security
2. Limit exposed endpoints
3. Use `EndpointRequest` matcher
4. Require authentication/authorization

**Q: Difference between health and liveness/readiness probes?**

A:
- **Health**: Overall application status
- **Liveness**: Application is running (restart if DOWN)
- **Readiness**: Application can accept traffic (remove from load balancer if DOWN)

**Q: How do you add custom metrics?**

A: Use Micrometer:
```java
Counter.builder("custom.metric").register(meterRegistry);
Timer.builder("custom.timer").register(meterRegistry);
Gauge.builder("custom.gauge", this, MyService::getValue).register(meterRegistry);
```

---

**[← Back to Fundamentals](./README.md)**

