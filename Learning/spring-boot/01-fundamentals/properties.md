# Configuration Properties & Management

## Externalized Configuration

Spring Boot allows you to externalize configuration so you can work with the same application code in different environments.

## Property Sources (Priority Order)

1. **Command line arguments**
2. **SPRING_APPLICATION_JSON**
3. **ServletConfig init parameters**
4. **ServletContext init parameters**
5. **JNDI attributes** from `java:comp/env`
6. **Java System properties** (`System.getProperties()`)
7. **OS environment variables**
8. **RandomValuePropertySource**
9. **Profile-specific properties outside jar** (`application-{profile}.properties`)
10. **Profile-specific properties inside jar**
11. **Application properties outside jar** (`application.properties`)
12. **Application properties inside jar**
13. **@PropertySource annotations**
14. **Default properties** (`SpringApplication.setDefaultProperties`)

## Configuration Files

### application.properties

```properties
# Server Configuration
server.port=8080
server.servlet.context-path=/api

# Database Configuration
spring.datasource.url=jdbc:postgresql://localhost:5432/mydb
spring.datasource.username=postgres
spring.datasource.password=secret

# JPA Configuration
spring.jpa.hibernate.ddl-auto=validate
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect

# Logging
logging.level.root=INFO
logging.level.com.example=DEBUG
logging.file.name=logs/application.log
```

### application.yml

```yaml
server:
  port: 8080
  servlet:
    context-path: /api

spring:
  application:
    name: my-app
  
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: postgres
    password: secret
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
  
  jpa:
    hibernate:
      ddl-auto: validate
    show-sql: true
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
        format_sql: true

logging:
  level:
    root: INFO
    com.example: DEBUG
  file:
    name: logs/application.log
```

## Profile-Specific Configuration

### application-dev.yml

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb_dev
  
logging:
  level:
    com.example: DEBUG
```

### application-prod.yml

```yaml
spring:
  datasource:
    url: jdbc:postgresql://prod-db:5432/mydb
  
logging:
  level:
    com.example: WARN
    
management:
  endpoints:
    web:
      exposure:
        include: health,metrics
```

### Activating Profiles

```bash
# Command line
java -jar myapp.jar --spring.profiles.active=prod

# Environment variable
export SPRING_PROFILES_ACTIVE=prod

# application.properties
spring.profiles.active=dev

# Multiple profiles
spring.profiles.active=dev,mysql,debug
```

## @ConfigurationProperties

### Type-Safe Configuration

```java
@Configuration
@ConfigurationProperties(prefix = "app")
@Data
public class AppProperties {
    
    private String name;
    private String version;
    private Security security = new Security();
    private Database database = new Database();
    
    @Data
    public static class Security {
        private String jwtSecret;
        private long jwtExpiration;
        private List<String> allowedOrigins;
    }
    
    @Data
    public static class Database {
        private int maxConnections;
        private int timeout;
        private boolean enableCaching;
    }
}
```

### application.yml

```yaml
app:
  name: My Application
  version: 1.0.0
  security:
    jwt-secret: ${JWT_SECRET}
    jwt-expiration: 86400000
    allowed-origins:
      - http://localhost:3000
      - https://example.com
  database:
    max-connections: 20
    timeout: 30
    enable-caching: true
```

### Using Configuration

```java
@Service
public class MyService {
    
    private final AppProperties appProperties;
    
    public MyService(AppProperties appProperties) {
        this.appProperties = appProperties;
    }
    
    public void doSomething() {
        String secret = appProperties.getSecurity().getJwtSecret();
        int maxConn = appProperties.getDatabase().getMaxConnections();
    }
}
```

## @Value Annotation

```java
@Component
public class MyComponent {
    
    @Value("${app.name}")
    private String appName;
    
    @Value("${app.timeout:30}")  // Default value: 30
    private int timeout;
    
    @Value("${app.enabled:true}")
    private boolean enabled;
    
    @Value("#{'${app.allowed-ips}'.split(',')}")
    private List<String> allowedIps;
    
    @Value("#{systemProperties['user.home']}")
    private String userHome;
}
```

## Environment Variables

### Relaxed Binding

Spring Boot uses relaxed binding rules:

```yaml
# All these are equivalent:
app.my-property=value
app.myProperty=value
app.my_property=value
APP_MY_PROPERTY=value  # Environment variable
```

### Common Patterns

```bash
# Database
export DATABASE_URL=jdbc:postgresql://localhost:5432/mydb
export DATABASE_USERNAME=postgres
export DATABASE_PASSWORD=secret

# Application
export SPRING_PROFILES_ACTIVE=prod
export SERVER_PORT=8080

# Custom properties
export APP_JWT_SECRET=mysecret
export APP_FEATURE_FLAG_ENABLED=true
```

## Configuration Validation

### Using Validation Annotations

```java
@Configuration
@ConfigurationProperties(prefix = "app")
@Validated
@Data
public class AppProperties {
    
    @NotBlank(message = "Application name is required")
    private String name;
    
    @Email(message = "Invalid email format")
    private String adminEmail;
    
    @Min(value = 1, message = "Port must be positive")
    @Max(value = 65535, message = "Port must be <= 65535")
    private int port;
    
    @Pattern(regexp = "^[A-Z]{2,4}$", message = "Invalid region code")
    private String regionCode;
    
    @Valid
    private Database database;
    
    @Data
    public static class Database {
        @NotBlank
        private String url;
        
        @Min(1)
        @Max(100)
        private int maxConnections = 10;
    }
}
```

## Configuration Processor

### Enable Metadata Generation

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
```

**Benefits:**
- IDE autocomplete for custom properties
- Property documentation
- Validation in IDE

## Multi-Document Files

### YAML

```yaml
# Default profile
spring:
  application:
    name: myapp

---
# Dev profile
spring:
  config:
    activate:
      on-profile: dev
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb_dev

---
# Prod profile
spring:
  config:
    activate:
      on-profile: prod
  datasource:
    url: jdbc:postgresql://prod-db:5432/mydb
```

## External Configuration Files

### Custom Locations

```bash
# Command line
java -jar myapp.jar --spring.config.location=file:./config/

# Multiple locations
java -jar myapp.jar --spring.config.location=\
  classpath:/default.properties,\
  file:./config/application.properties

# Additional locations (keeps defaults)
java -jar myapp.jar --spring.config.additional-location=\
  file:/etc/myapp/
```

## Encrypting Properties

### Using Jasypt

```xml
<dependency>
    <groupId>com.github.ulisesbocchio</groupId>
    <artifactId>jasypt-spring-boot-starter</artifactId>
    <version>3.0.5</version>
</dependency>
```

```properties
# Encrypted properties
spring.datasource.password=ENC(encrypted_password_here)
jasypt.encryptor.password=${JASYPT_PASSWORD}
```

## Best Practices

### 1. Use Type-Safe Configuration

✅ **Good:**
```java
@ConfigurationProperties(prefix = "app")
public class AppProperties {
    private String apiKey;
    // getters/setters
}
```

❌ **Avoid:**
```java
@Value("${app.api-key}")
private String apiKey;
```

### 2. Provide Defaults

```java
@ConfigurationProperties(prefix = "app")
@Data
public class AppProperties {
    private int timeout = 30;  // Default value
    private boolean enabled = true;
}
```

### 3. Group Related Properties

```yaml
app:
  security:
    jwt-secret: secret
    jwt-expiration: 86400000
  database:
    max-connections: 20
    timeout: 30
```

### 4. Use Environment Variables for Secrets

```yaml
spring:
  datasource:
    password: ${DB_PASSWORD}
    
app:
  jwt:
    secret: ${JWT_SECRET}
```

### 5. Document Custom Properties

```java
/**
 * Application configuration properties.
 */
@ConfigurationProperties(prefix = "app")
@Data
public class AppProperties {
    
    /**
     * JWT secret key for token signing.
     */
    private String jwtSecret;
    
    /**
     * JWT expiration time in milliseconds.
     * Default: 24 hours (86400000 ms)
     */
    private long jwtExpiration = 86400000;
}
```

## Interview Questions

**Q: What is the order of property source precedence in Spring Boot?**

A: Command line args → Environment variables → application.properties (external) → application.properties (internal) → @PropertySource → defaults

**Q: How do you handle sensitive data in properties?**

A:
1. Use environment variables
2. Encrypt with Jasypt
3. Use cloud secret managers (AWS Secrets Manager, Azure Key Vault)
4. Never commit secrets to Git

**Q: Difference between @Value and @ConfigurationProperties?**

A:
- `@Value`: Simple properties, SpEL support, scattered across code
- `@ConfigurationProperties`: Type-safe, grouped, validation support, preferred for complex configs

**Q: How do you validate configuration properties?**

A:
```java
@ConfigurationProperties(prefix = "app")
@Validated  // Enable validation
@Data
public class AppProperties {
    @NotBlank
    private String name;
    
    @Min(1)
    @Max(65535)
    private int port;
}
```

---

**[← Back to Fundamentals](./README.md)**

