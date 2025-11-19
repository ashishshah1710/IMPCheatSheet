# Auto-Configuration Deep Dive

## How Auto-Configuration Works

Spring Boot auto-configuration automatically configures your Spring application based on the dependencies present on the classpath.

### The Magic Behind Auto-Configuration

```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

This simple annotation does three things:

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@SpringBootConfiguration  // Same as @Configuration
@EnableAutoConfiguration  // THE MAGIC
@ComponentScan           // Scans current package
public @interface SpringBootApplication {
    // ...
}
```

### @EnableAutoConfiguration Mechanism

1. **Loads Configuration Classes**
   - Reads `META-INF/spring.factories`
   - Contains list of auto-configuration classes

2. **Applies Conditional Logic**
   - `@ConditionalOnClass` - Class must be present
   - `@ConditionalOnMissingBean` - Bean not already defined
   - `@ConditionalOnProperty` - Property must be set
   - `@ConditionalOnMissingClass` - Class must NOT be present

3. **Creates Beans**
   - Registers beans in Spring context
   - Uses sensible defaults

### Example: DataSource Auto-Configuration

```java
@Configuration
@ConditionalOnClass({ DataSource.class, EmbeddedDatabaseType.class })
@EnableConfigurationProperties(DataSourceProperties.class)
@Import({ DataSourcePoolMetadataProvidersConfiguration.class })
public class DataSourceAutoConfiguration {

    @Configuration
    @Conditional(EmbeddedDatabaseCondition.class)
    @ConditionalOnMissingBean({ DataSource.class, XADataSource.class })
    @Import(EmbeddedDataSourceConfiguration.class)
    protected static class EmbeddedDatabaseConfiguration {
    }

    @Configuration
    @ConditionalOnMissingBean(DataSource.class)
    @ConditionalOnProperty(name = "spring.datasource.type")
    static class Generic {
        @Bean
        public DataSource dataSource(DataSourceProperties properties) {
            return properties.initializeDataSourceBuilder().build();
        }
    }
}
```

### Viewing Auto-Configuration Report

```properties
# Enable debug mode
debug=true
```

Or run with:
```bash
java -jar myapp.jar --debug
```

**Report Sections:**
- **Positive matches** - Configurations that were applied
- **Negative matches** - Configurations that were NOT applied (and why)
- **Exclusions** - Explicitly excluded configurations
- **Unconditional classes** - Always applied

### Common Conditional Annotations

| Annotation | Description |
|------------|-------------|
| `@ConditionalOnClass` | Present if class is on classpath |
| `@ConditionalOnMissingClass` | Present if class is NOT on classpath |
| `@ConditionalOnBean` | Present if bean exists |
| `@ConditionalOnMissingBean` | Present if bean does NOT exist |
| `@ConditionalOnProperty` | Present if property has specific value |
| `@ConditionalOnResource` | Present if resource exists |
| `@ConditionalOnWebApplication` | Present if web application |
| `@ConditionalOnNotWebApplication` | Present if NOT web application |
| `@ConditionalOnExpression` | Present if SpEL expression is true |

### Custom Auto-Configuration

**Step 1: Create Configuration Class**

```java
@Configuration
@ConditionalOnClass(MyService.class)
@EnableConfigurationProperties(MyServiceProperties.class)
public class MyServiceAutoConfiguration {
    
    @Bean
    @ConditionalOnMissingBean
    public MyService myService(MyServiceProperties properties) {
        return new MyService(properties.getApiKey());
    }
    
    @Bean
    @ConditionalOnProperty(prefix = "myservice", name = "cache.enabled", havingValue = "true")
    public CacheManager cacheManager() {
        return new ConcurrentMapCacheManager();
    }
}
```

**Step 2: Create Properties Class**

```java
@ConfigurationProperties(prefix = "myservice")
@Data
public class MyServiceProperties {
    private String apiKey;
    private int timeout = 30;
    private Cache cache = new Cache();
    
    @Data
    public static class Cache {
        private boolean enabled = false;
        private int ttl = 3600;
    }
}
```

**Step 3: Register in spring.factories**

```properties
# src/main/resources/META-INF/spring.factories
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.example.autoconfigure.MyServiceAutoConfiguration
```

### Disabling Auto-Configuration

**Method 1: Using @SpringBootApplication**
```java
@SpringBootApplication(exclude = {
    DataSourceAutoConfiguration.class,
    SecurityAutoConfiguration.class
})
```

**Method 2: Using application.properties**
```properties
spring.autoconfigure.exclude=\
  org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration,\
  org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration
```

**Method 3: Using @EnableAutoConfiguration**
```java
@Configuration
@EnableAutoConfiguration(exclude = {DataSourceAutoConfiguration.class})
```

### Interview Questions

**Q: How does Spring Boot decide which auto-configurations to apply?**

A: Through conditional annotations and classpath scanning:
1. Checks if required classes are on classpath (`@ConditionalOnClass`)
2. Checks if beans are already defined (`@ConditionalOnMissingBean`)
3. Checks property values (`@ConditionalOnProperty`)
4. Evaluates all conditions; applies configuration only if all pass

**Q: What happens if you define the same bean that auto-configuration creates?**

A: Your bean takes precedence because of `@ConditionalOnMissingBean` in auto-configuration classes.

**Q: How do you debug auto-configuration issues?**

A: 
1. Enable debug mode (`--debug`)
2. Check auto-configuration report
3. Look at "Negative matches" section
4. Verify classpath dependencies
5. Check property configurations

### Best Practices

1. **Always use @ConditionalOnMissingBean** for default beans
2. **Order matters** - Use `@AutoConfigureAfter` and `@AutoConfigureBefore`
3. **Document your auto-configuration** - Add comments explaining conditions
4. **Test thoroughly** - Test with and without dependencies
5. **Provide properties** - Allow users to customize behavior

### Common Pitfalls

❌ **Forgetting to add spring.factories**
```
Auto-configuration won't be detected
```

❌ **Circular dependencies**
```
Be careful with @ConditionalOnBean and ordering
```

❌ **Not using @ConditionalOnMissingBean**
```
User can't override your defaults
```

❌ **Too aggressive auto-configuration**
```
Don't auto-configure everything; let users opt-in for some features
```

---

**[← Back to Fundamentals](./README.md)**

