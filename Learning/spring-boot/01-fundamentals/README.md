# 🚀 Spring Boot Fundamentals

**Phase 1: Master Spring Boot Core Concepts (1 Week)**

---

## 📖 Overview

Spring Boot revolutionizes Java development by eliminating boilerplate configuration and providing production-ready features out of the box. Understanding how Boot works "under the hood" is crucial for interviews at the 3.5+ years experience level.

---

## 🎯 Learning Objectives

By the end of this section, you should master:

✅ Auto-configuration mechanism  
✅ Starter dependencies and their purpose  
✅ Configuration management (properties/YAML)  
✅ Embedded servers and deployment  
✅ Spring Boot DevTools  
✅ Actuator for production monitoring  

---

## 📚 Core Topics

### 1. What is Spring Boot?

Spring Boot is an extension of the Spring framework that simplifies the setup and development of Spring applications.

**Key Features:**
- **Auto-Configuration**: Automatically configures your application based on classpath dependencies
- **Standalone**: Creates standalone applications with embedded servers
- **Opinionated Defaults**: Provides sensible defaults to get started quickly
- **Production-Ready**: Includes metrics, health checks, and externalized configuration

**📄 Deep Dive:** [What is Spring Boot](./what-is-spring-boot.md)

---

### 2. Auto-Configuration Magic

Auto-configuration is the heart of Spring Boot. It automatically configures beans based on:
- Classpath dependencies
- Existing beans
- Property settings

**Key Concepts:**
- `@EnableAutoConfiguration`
- `@SpringBootApplication` (combines `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan`)
- Conditional annotations (`@ConditionalOnClass`, `@ConditionalOnMissingBean`, etc.)
- `spring.factories` file
- Auto-configuration report

**📄 Deep Dive:** [auto-configuration.md](./auto-configuration.md)

---

### 3. Starter Dependencies

Starters are dependency descriptors that bring everything you need for a particular feature.

**Popular Starters:**
```xml
<!-- Web Applications -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<!-- Data JPA -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- Security -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<!-- Test -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

**📄 Deep Dive:** [starters.md](./starters.md)

---

### 4. Configuration Management

Spring Boot supports multiple ways to externalize configuration.

**Configuration Sources (Priority Order):**
1. Command line arguments
2. SPRING_APPLICATION_JSON
3. ServletConfig init parameters
4. ServletContext init parameters
5. Java System properties
6. OS environment variables
7. Profile-specific properties
8. Application properties (application.yml/application.properties)
9. `@PropertySource` annotations
10. Default properties

**Example Configuration:**

```yaml
# application.yml
spring:
  application:
    name: my-app
  
  profiles:
    active: ${ENVIRONMENT:dev}
  
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: ${DB_USER}
    password: ${DB_PASSWORD}

server:
  port: ${PORT:8080}
  
logging:
  level:
    root: INFO
    com.example: DEBUG
```

**📄 Deep Dive:** [properties.md](./properties.md)

---

### 5. Embedded Servers

Spring Boot embeds Tomcat, Jetty, or Undertow directly in your application.

**Benefits:**
- No need for WAR files
- Simplified deployment
- Consistent environment
- Easy containerization

**Default Servers:**
- **Tomcat** (default)
- **Jetty** (alternative)
- **Undertow** (alternative)

**Switching Servers:**
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jetty</artifactId>
</dependency>
```

**📄 Deep Dive:** [embedded-servers.md](./embedded-servers.md)

---

### 6. Spring Boot DevTools

DevTools enhance development experience with:
- Automatic restarts
- LiveReload
- Remote debugging support
- Property defaults for development

**Usage:**
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <scope>runtime</scope>
    <optional>true</optional>
</dependency>
```

**📄 Deep Dive:** [devtools.md](./devtools.md)

---

### 7. Spring Boot Actuator

Actuator provides production-ready features to monitor and manage your application.

**Key Endpoints:**
- `/actuator/health` - Application health
- `/actuator/info` - Application info
- `/actuator/metrics` - Application metrics
- `/actuator/env` - Environment properties
- `/actuator/loggers` - Logger configuration
- `/actuator/threaddump` - Thread dump
- `/actuator/heapdump` - Heap dump

**Configuration:**
```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: always
  metrics:
    tags:
      application: ${spring.application.name}
```

**📄 Deep Dive:** [actuator.md](./actuator.md)

---

## 💻 Hands-On Practice

### Quick Start Application

```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

@RestController
@RequestMapping("/api")
class HelloController {
    
    @Value("${app.message:Hello World}")
    private String message;
    
    @GetMapping("/hello")
    public Map<String, String> hello() {
        return Map.of(
            "message", message,
            "timestamp", LocalDateTime.now().toString()
        );
    }
    
    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "UP");
    }
}
```

### Custom Auto-Configuration

```java
@Configuration
@ConditionalOnClass(DataSource.class)
@EnableConfigurationProperties(MyProperties.class)
public class MyAutoConfiguration {
    
    @Bean
    @ConditionalOnMissingBean
    public MyService myService(MyProperties properties) {
        return new MyServiceImpl(properties);
    }
}

@ConfigurationProperties(prefix = "myapp")
@Data
public class MyProperties {
    private String apiKey;
    private int timeout = 30;
    private boolean enabled = true;
}
```

---

## 🎯 Interview Questions

### Basic Level

**Q1: What is Spring Boot and how is it different from Spring Framework?**

**Answer:**
Spring Boot is an extension of Spring Framework that simplifies configuration and deployment. Key differences:

| Aspect | Spring Framework | Spring Boot |
|--------|-----------------|-------------|
| Configuration | XML or Java config | Auto-configuration |
| Dependency Management | Manual | Starter dependencies |
| Embedded Server | External server needed | Embedded Tomcat/Jetty |
| Production Features | Manual setup | Actuator built-in |
| Setup Time | Hours/Days | Minutes |

---

**Q2: Explain @SpringBootApplication annotation.**

**Answer:**
`@SpringBootApplication` is a convenience annotation that combines three annotations:

```java
@SpringBootApplication
// Equivalent to:
@Configuration      // Marks class as configuration
@EnableAutoConfiguration  // Enables auto-configuration
@ComponentScan     // Scans for components in package and sub-packages
```

---

**Q3: How does Spring Boot auto-configuration work?**

**Answer:**
Auto-configuration works through:

1. **@EnableAutoConfiguration** triggers the process
2. **spring.factories** file lists all auto-configuration classes
3. **@Conditional** annotations determine which configs apply
4. **Classpath scanning** detects available dependencies
5. **Beans are created** based on conditions

Example:
```java
@Configuration
@ConditionalOnClass(DataSource.class)
@ConditionalOnMissingBean(DataSource.class)
public class DataSourceAutoConfiguration {
    @Bean
    public DataSource dataSource() {
        // Create DataSource
    }
}
```

---

**Q4: What are Spring Boot Starters?**

**Answer:**
Starters are dependency descriptors that provide:
- All necessary dependencies for a feature
- Compatible versions
- Transitive dependencies
- Sensible defaults

Example: `spring-boot-starter-web` includes:
- Spring MVC
- Embedded Tomcat
- Jackson for JSON
- Validation
- Logging

---

**Q5: How do you disable specific auto-configuration?**

**Answer:**
Three ways:

```java
// Method 1: Using annotation
@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})

// Method 2: Using properties
spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration

// Method 3: Using @EnableAutoConfiguration
@EnableAutoConfiguration(exclude = {DataSourceAutoConfiguration.class})
```

---

### Advanced Level

**Q6: Explain the order of property sources in Spring Boot.**

**Answer:**
Properties are resolved in this order (higher priority first):

1. Command line arguments
2. SPRING_APPLICATION_JSON
3. ServletConfig/ServletContext init parameters
4. JNDI attributes
5. Java System properties (`System.getProperties()`)
6. OS environment variables
7. RandomValuePropertySource
8. Profile-specific properties outside jar
9. Profile-specific properties inside jar
10. Application properties outside jar
11. Application properties inside jar
12. @PropertySource annotations
13. Default properties

---

**Q7: How would you create a custom Spring Boot starter?**

**Answer:**

```java
// 1. Create auto-configuration class
@Configuration
@ConditionalOnClass(MyService.class)
@EnableConfigurationProperties(MyServiceProperties.class)
public class MyServiceAutoConfiguration {
    
    @Bean
    @ConditionalOnMissingBean
    public MyService myService(MyServiceProperties props) {
        return new MyService(props);
    }
}

// 2. Create properties class
@ConfigurationProperties(prefix = "myservice")
public class MyServiceProperties {
    private String apiKey;
    private int timeout = 30;
    // getters/setters
}

// 3. Create spring.factories file
// src/main/resources/META-INF/spring.factories
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.example.MyServiceAutoConfiguration

// 4. Create starter POM
<artifactId>myservice-spring-boot-starter</artifactId>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>myservice-spring-boot-autoconfigure</artifactId>
    </dependency>
</dependencies>
```

---

**Q8: How do you customize Actuator endpoints?**

**Answer:**

```java
// Custom health indicator
@Component
public class CustomHealthIndicator implements HealthIndicator {
    
    @Override
    public Health health() {
        boolean serviceUp = checkService();
        if (serviceUp) {
            return Health.up()
                .withDetail("service", "available")
                .build();
        }
        return Health.down()
            .withDetail("service", "unavailable")
            .build();
    }
}

// Custom endpoint
@Endpoint(id = "custom")
@Component
public class CustomEndpoint {
    
    @ReadOperation
    public Map<String, Object> customInfo() {
        return Map.of(
            "version", "1.0",
            "status", "active"
        );
    }
}

// Secure endpoints
@Configuration
public class ActuatorSecurity extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .requestMatcher(EndpointRequest.toAnyEndpoint())
            .authorizeRequests()
            .anyRequest().hasRole("ADMIN");
    }
}
```

---

### Scenario-Based Questions

**Q9: Your application is slow to start. How would you diagnose and fix it?**

**Answer:**

**Diagnosis:**
```bash
# Enable debug logging
java -jar app.jar --debug

# Check auto-configuration report
java -jar app.jar --debug 2>&1 | grep "CONDITIONS EVALUATION REPORT"

# Use Spring Boot Actuator
curl http://localhost:8080/actuator/startup
```

**Solutions:**
1. **Lazy initialization:**
```properties
spring.main.lazy-initialization=true
```

2. **Exclude unnecessary auto-configurations:**
```java
@SpringBootApplication(exclude = {
    DataSourceAutoConfiguration.class,
    HibernateJpaAutoConfiguration.class
})
```

3. **Profile-specific beans:**
```java
@Bean
@Profile("!test")
public ExpensiveService expensiveService() {
    return new ExpensiveService();
}
```

---

**Q10: How do you handle different configurations for dev, staging, and production?**

**Answer:**

```yaml
# application.yml (common)
spring:
  application:
    name: myapp
logging:
  level:
    root: INFO

---
# application-dev.yml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb_dev
logging:
  level:
    com.example: DEBUG

---
# application-staging.yml
spring:
  datasource:
    url: jdbc:postgresql://staging-db:5432/mydb
  
---
# application-prod.yml
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

**Activation:**
```bash
# Dev
java -jar app.jar --spring.profiles.active=dev

# Prod
java -jar app.jar --spring.profiles.active=prod

# Multiple profiles
java -jar app.jar --spring.profiles.active=prod,monitoring
```

---

## ✅ Practice Checklist

- [ ] Create a basic Spring Boot application
- [ ] Understand @SpringBootApplication components
- [ ] Disable specific auto-configurations
- [ ] Create custom auto-configuration
- [ ] Use different property sources
- [ ] Configure profile-specific properties
- [ ] Add and configure Actuator endpoints
- [ ] Create custom health indicators
- [ ] Use DevTools for development
- [ ] Create a custom starter

---

## 📖 Additional Resources

### Official Documentation
- [Spring Boot Reference Documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [Spring Boot Auto-configuration](https://docs.spring.io/spring-boot/docs/current/reference/html/using.html#using.auto-configuration)
- [Spring Boot Actuator](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html)

### Recommended Reading
- [Baeldung Spring Boot Tutorials](https://www.baeldung.com/spring-boot)
- [Spring Boot in Action](https://www.manning.com/books/spring-boot-in-action)

---

## 🎯 Next Steps

Once you've mastered fundamentals, move to:

**👉 [Phase 2: REST APIs & Microservices →](../02-rest-apis/README.md)**

---

**💡 Pro Tip for Interviews:**
Be ready to explain how auto-configuration works under the hood. Draw the flow diagram if needed. Interviewers at 3.5+ years level expect deep understanding, not just surface knowledge!



