# Spring Boot Starters

## What are Starters?

Starters are a set of convenient dependency descriptors that you can include in your application. They provide a one-stop shop for all the Spring and related technologies you need, without having to hunt through sample code and copy-paste loads of dependency descriptors.

## Core Starters

### spring-boot-starter-web

For building web applications and REST APIs.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

**Includes:**
- Spring MVC
- Embedded Tomcat
- Jackson (JSON processing)
- Validation
- Logging (Logback)

**Use Cases:**
- REST APIs
- MVC web applications
- WebSocket applications

---

### spring-boot-starter-data-jpa

For working with databases using JPA.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

**Includes:**
- Spring Data JPA
- Hibernate
- Transaction management
- JDBC
- Entity management

**Use Cases:**
- Database operations
- ORM mapping
- Repository pattern

---

### spring-boot-starter-security

For adding security features.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

**Includes:**
- Spring Security
- Authentication
- Authorization
- CSRF protection

---

### spring-boot-starter-test

For testing applications.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

**Includes:**
- JUnit 5
- Mockito
- AssertJ
- Hamcrest
- Spring Test
- JSONassert

---

### spring-boot-starter-actuator

For production monitoring.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

**Includes:**
- Health checks
- Metrics
- Application info
- Environment details

---

## Database Starters

### JDBC Starter

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
```

### MongoDB Starter

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```

### Redis Starter

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

---

## Messaging Starters

### Kafka Starter

```xml
<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
</dependency>
```

### RabbitMQ Starter

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

---

## Complete Starter List

| Starter | Purpose |
|---------|---------|
| `spring-boot-starter` | Core starter (logging, auto-config) |
| `spring-boot-starter-web` | Web apps, REST APIs |
| `spring-boot-starter-data-jpa` | JPA with Hibernate |
| `spring-boot-starter-data-jdbc` | JDBC access |
| `spring-boot-starter-data-mongodb` | MongoDB |
| `spring-boot-starter-data-redis` | Redis |
| `spring-boot-starter-security` | Security |
| `spring-boot-starter-oauth2-client` | OAuth2 client |
| `spring-boot-starter-oauth2-resource-server` | OAuth2 resource server |
| `spring-boot-starter-validation` | Bean validation |
| `spring-boot-starter-cache` | Caching |
| `spring-boot-starter-mail` | Email |
| `spring-boot-starter-quartz` | Quartz scheduler |
| `spring-boot-starter-batch` | Batch processing |
| `spring-boot-starter-actuator` | Production monitoring |
| `spring-boot-starter-test` | Testing |
| `spring-boot-starter-webflux` | Reactive web |
| `spring-boot-starter-amqp` | RabbitMQ |
| `spring-boot-starter-thymeleaf` | Thymeleaf templates |

---

## Creating Custom Starter

### Project Structure

```
myservice-spring-boot-starter/
├── myservice-spring-boot-autoconfigure/
│   ├── src/main/java/
│   │   └── com/example/
│   │       ├── MyServiceAutoConfiguration.java
│   │       └── MyServiceProperties.java
│   └── src/main/resources/
│       └── META-INF/
│           └── spring.factories
└── myservice-spring-boot-starter/
    └── pom.xml (depends on autoconfigure)
```

### Step 1: Auto-Configuration Module

```java
@Configuration
@ConditionalOnClass(MyService.class)
@EnableConfigurationProperties(MyServiceProperties.class)
public class MyServiceAutoConfiguration {
    
    @Bean
    @ConditionalOnMissingBean
    public MyService myService(MyServiceProperties properties) {
        return new MyServiceImpl(properties);
    }
}
```

### Step 2: Properties Class

```java
@ConfigurationProperties(prefix = "myservice")
@Data
public class MyServiceProperties {
    private String apiKey;
    private String baseUrl = "https://api.example.com";
    private int timeout = 30;
    private boolean enabled = true;
}
```

### Step 3: spring.factories

```properties
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.example.MyServiceAutoConfiguration
```

### Step 4: Starter POM

```xml
<project>
    <groupId>com.example</groupId>
    <artifactId>myservice-spring-boot-starter</artifactId>
    <version>1.0.0</version>
    
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>myservice-spring-boot-autoconfigure</artifactId>
            <version>1.0.0</version>
        </dependency>
    </dependencies>
</project>
```

### Usage

```xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>myservice-spring-boot-starter</artifactId>
    <version>1.0.0</version>
</dependency>
```

```properties
myservice.api-key=secret123
myservice.timeout=60
myservice.enabled=true
```

---

## Dependency Management

Spring Boot manages versions through `spring-boot-dependencies` BOM.

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.0</version>
</parent>
```

**Benefits:**
- No need to specify versions for managed dependencies
- Compatible versions guaranteed
- Easy upgrades

**Override Versions:**
```xml
<properties>
    <postgresql.version>42.6.0</postgresql.version>
</properties>
```

---

## Interview Questions

**Q: What problem do starters solve?**

A: Starters solve dependency management complexity:
- No need to find compatible versions
- Reduce dependency declarations
- Include transitive dependencies
- Provide sensible defaults

**Q: Difference between starter and auto-configuration?**

A:
- **Starter**: Maven/Gradle dependency descriptor (POM file)
- **Auto-Configuration**: Java configuration classes that create beans

**Q: Can you use Spring Boot without starters?**

A: Yes, but you'll need to:
- Manually add all dependencies
- Configure everything yourself
- Manage version compatibility
- No auto-configuration benefits

---

**[← Back to Fundamentals](./README.md)**

