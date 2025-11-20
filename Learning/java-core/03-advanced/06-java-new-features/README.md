# 🆕 Java New Features (Java 9 - 21)

Stay updated with the latest Java features!

---

## 📚 Table of Contents

1. [Java 9](#java-9)
2. [Java 10-11](#java-10-11)
3. [Java 12-14](#java-12-14)
4. [Java 15-17 LTS](#java-15-17)
5. [Java 18-21 LTS](#java-18-21)
6. [Interview Questions](#interview-questions)

---

## 🎯 Java 9 (September 2017)

### Q1: Module System (Project Jigsaw)

**Answer:**

```java
// module-info.java
module com.example.myapp {
    // Modules this module depends on
    requires java.sql;
    requires java.logging;
    requires com.example.utils;
    
    // Packages to export (make public)
    exports com.example.myapp.api;
    exports com.example.myapp.service to com.example.client;
    
    // Open packages for reflection
    opens com.example.myapp.model;
    
    // Provide service implementation
    provides com.example.service.MyService 
        with com.example.myapp.MyServiceImpl;
    
    // Use a service
    uses com.example.service.SomeService;
}
```

**Benefits:**
- Strong encapsulation
- Reliable configuration
- Improved performance
- Smaller runtime footprint

### Q2: JShell (Interactive REPL)

**Answer:**

```bash
# Start JShell
jshell

# Examples
jshell> int x = 10
x ==> 10

jshell> System.out.println("Hello JShell")
Hello JShell

jshell> IntStream.range(1, 10).sum()
$3 ==> 45

jshell> /help          # Get help
jshell> /list          # List all snippets
jshell> /exit          # Exit
```

### Q3: Collection Factory Methods

**Answer:**

```java
import java.util.*;

public class CollectionFactoryDemo {
    public static void main(String[] args) {
        // Immutable List
        List<String> list = List.of("A", "B", "C");
        // list.add("D"); // UnsupportedOperationException
        
        // Immutable Set
        Set<Integer> set = Set.of(1, 2, 3, 4, 5);
        // No duplicates allowed in Set.of()
        
        // Immutable Map
        Map<String, Integer> map = Map.of(
            "John", 30,
            "Jane", 25,
            "Bob", 35
        );
        
        // Map with more entries
        Map<String, Integer> largeMap = Map.ofEntries(
            Map.entry("One", 1),
            Map.entry("Two", 2),
            Map.entry("Three", 3),
            Map.entry("Four", 4)
        );
        
        System.out.println(list);
        System.out.println(set);
        System.out.println(map);
    }
}
```

### Q4: Stream API Enhancements

**Answer:**

```java
import java.util.stream.*;

public class StreamEnhancementsJava9 {
    public static void main(String[] args) {
        // 1. takeWhile() - take elements while condition is true
        Stream.of(1, 2, 3, 4, 5, 6)
            .takeWhile(n -> n < 4)
            .forEach(System.out::println); // 1, 2, 3
        
        // 2. dropWhile() - drop elements while condition is true
        Stream.of(1, 2, 3, 4, 5, 6)
            .dropWhile(n -> n < 4)
            .forEach(System.out::println); // 4, 5, 6
        
        // 3. ofNullable() - create stream from nullable value
        Stream<String> stream1 = Stream.ofNullable("Hello");
        Stream<String> stream2 = Stream.ofNullable(null); // Empty stream
        
        // 4. iterate() with predicate
        Stream.iterate(1, n -> n < 10, n -> n + 1)
            .forEach(System.out::println); // 1 to 9
    }
}
```

---

## 💎 Java 10-11 (March 2018 - September 2018)

### Q5: Local Variable Type Inference (var)

**Answer:**

```java
import java.util.*;

public class VarKeywordDemo {
    public static void main(String[] args) {
        // Instead of: String message = "Hello";
        var message = "Hello"; // Type inferred as String
        
        // Instead of: List<String> list = new ArrayList<>();
        var list = new ArrayList<String>();
        
        // Works with complex types
        var map = Map.of("key1", "value1", "key2", "value2");
        
        // In loops
        for (var item : list) {
            System.out.println(item);
        }
        
        // Lambda parameters (Java 11)
        list.forEach((var item) -> System.out.println(item));
        
        // ❌ NOT ALLOWED
        // var x; // Must initialize
        // var y = null; // Can't infer null
        // var z = {1, 2, 3}; // Can't infer array
        // var lambda = () -> "test"; // Can't infer lambda
    }
}
```

### Q6: String Methods (Java 11)

**Answer:**

```java
public class StringMethodsJava11 {
    public static void main(String[] args) {
        String str = "  Hello World  ";
        
        // 1. isBlank() - checks if string is empty or contains only whitespace
        System.out.println("   ".isBlank()); // true
        System.out.println("Hello".isBlank()); // false
        
        // 2. strip() - removes leading and trailing whitespace
        System.out.println(str.strip()); // "Hello World"
        System.out.println(str.stripLeading()); // "Hello World  "
        System.out.println(str.stripTrailing()); // "  Hello World"
        
        // 3. lines() - returns stream of lines
        String multiline = "Line1\nLine2\nLine3";
        multiline.lines().forEach(System.out::println);
        
        // 4. repeat() - repeats string n times
        System.out.println("Ha".repeat(3)); // "HaHaHa"
    }
}
```

### Q7: HttpClient API (Java 11)

**Answer:**

```java
import java.net.URI;
import java.net.http.*;
import java.net.http.HttpResponse.BodyHandlers;

public class HttpClientDemo {
    public static void main(String[] args) throws Exception {
        // Create client
        HttpClient client = HttpClient.newHttpClient();
        
        // Create request
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://api.github.com/users/github"))
            .GET()
            .build();
        
        // Send synchronously
        HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
        System.out.println("Status: " + response.statusCode());
        System.out.println("Body: " + response.body());
        
        // Send asynchronously
        client.sendAsync(request, BodyHandlers.ofString())
            .thenApply(HttpResponse::body)
            .thenAccept(System.out::println)
            .join();
        
        // POST request
        HttpRequest postRequest = HttpRequest.newBuilder()
            .uri(URI.create("https://httpbin.org/post"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString("{\"key\":\"value\"}"))
            .build();
        
        HttpResponse<String> postResponse = client.send(postRequest, BodyHandlers.ofString());
        System.out.println(postResponse.body());
    }
}
```

---

## 🎨 Java 12-14 (March 2019 - March 2020)

### Q8: Switch Expressions (Java 14)

**Answer:**

```java
public class SwitchExpressionsDemo {
    public static void main(String[] args) {
        // Old switch statement
        int day = 3;
        String dayType;
        switch (day) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                dayType = "Weekday";
                break;
            case 6:
            case 7:
                dayType = "Weekend";
                break;
            default:
                dayType = "Invalid";
        }
        
        // New switch expression
        String dayType2 = switch (day) {
            case 1, 2, 3, 4, 5 -> "Weekday";
            case 6, 7 -> "Weekend";
            default -> "Invalid";
        };
        
        // With yield
        String result = switch (day) {
            case 1, 2, 3, 4, 5 -> {
                System.out.println("It's a weekday");
                yield "Weekday";
            }
            case 6, 7 -> {
                System.out.println("It's weekend!");
                yield "Weekend";
            }
            default -> "Invalid";
        };
        
        System.out.println(result);
        
        // Pattern matching in switch (Java 17 preview, Java 21 final)
        Object obj = "Hello";
        String formatted = switch (obj) {
            case Integer i -> "Integer: " + i;
            case String s -> "String: " + s.toUpperCase();
            case null -> "null value";
            default -> "Unknown type";
        };
    }
}
```

### Q9: Text Blocks (Java 15)

**Answer:**

```java
public class TextBlocksDemo {
    public static void main(String[] args) {
        // Old way - ugly and error-prone
        String json1 = "{\n" +
                       "  \"name\": \"John\",\n" +
                       "  \"age\": 30,\n" +
                       "  \"city\": \"New York\"\n" +
                       "}";
        
        // New way - Text Blocks
        String json2 = """
            {
              "name": "John",
              "age": 30,
              "city": "New York"
            }
            """;
        
        // HTML example
        String html = """
            <html>
              <head>
                <title>My Page</title>
              </head>
              <body>
                <h1>Hello, World!</h1>
              </body>
            </html>
            """;
        
        // SQL example
        String sql = """
            SELECT users.name, orders.total
            FROM users
            JOIN orders ON users.id = orders.user_id
            WHERE orders.total > 100
            ORDER BY orders.total DESC
            """;
        
        // String interpolation with formatted()
        String name = "Alice";
        int age = 25;
        String message = """
            Hello, %s!
            You are %d years old.
            """.formatted(name, age);
        
        System.out.println(json2);
        System.out.println(html);
        System.out.println(sql);
        System.out.println(message);
    }
}
```

---

## 🚀 Java 15-17 LTS (September 2020 - September 2021)

### Q10: Records (Java 16)

**Answer:**

```java
// Old way - verbose
class PersonOld {
    private final String name;
    private final int age;
    
    public PersonOld(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() { return name; }
    public int getAge() { return age; }
    
    @Override
    public boolean equals(Object o) { /* ... */ }
    @Override
    public int hashCode() { /* ... */ }
    @Override
    public String toString() { /* ... */ }
}

// New way - Record (one line!)
record Person(String name, int age) {}

public class RecordsDemo {
    public static void main(String[] args) {
        // Create record
        Person person = new Person("John", 30);
        
        // Access fields (automatically generated accessors)
        System.out.println(person.name()); // John
        System.out.println(person.age());  // 30
        
        // toString() automatically generated
        System.out.println(person); // Person[name=John, age=30]
        
        // equals() automatically generated
        Person person2 = new Person("John", 30);
        System.out.println(person.equals(person2)); // true
        
        // hashCode() automatically generated
        System.out.println(person.hashCode());
        
        // Advanced record features
        demonstrateAdvancedRecords();
    }
    
    static void demonstrateAdvancedRecords() {
        // Record with validation
        record Employee(String name, double salary) {
            // Compact constructor
            public Employee {
                if (salary < 0) {
                    throw new IllegalArgumentException("Salary cannot be negative");
                }
                // Automatic field assignment
            }
            
            // Additional methods
            public double annualBonus() {
                return salary * 0.1;
            }
        }
        
        Employee emp = new Employee("Alice", 50000);
        System.out.println("Bonus: " + emp.annualBonus());
        
        // Record with static members
        record Point(int x, int y) {
            public static Point ORIGIN = new Point(0, 0);
            
            public double distanceFromOrigin() {
                return Math.sqrt(x * x + y * y);
            }
        }
        
        Point p1 = new Point(3, 4);
        System.out.println("Distance: " + p1.distanceFromOrigin()); // 5.0
    }
}
```

### Q11: Sealed Classes (Java 17)

**Answer:**

```java
// Sealed class restricts which classes can extend it
public sealed class Shape permits Circle, Rectangle, Triangle {
    public abstract double area();
}

// Subclasses must be final, sealed, or non-sealed
final class Circle extends Shape {
    private double radius;
    
    public Circle(double radius) {
        this.radius = radius;
    }
    
    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

final class Rectangle extends Shape {
    private double length, width;
    
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }
    
    @Override
    public double area() {
        return length * width;
    }
}

// non-sealed allows further extension
non-sealed class Triangle extends Shape {
    private double base, height;
    
    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }
    
    @Override
    public double area() {
        return 0.5 * base * height;
    }
}

// Now other classes can extend Triangle
class RightTriangle extends Triangle {
    public RightTriangle(double base, double height) {
        super(base, height);
    }
}

// Sealed interfaces
sealed interface Vehicle permits Car, Truck, Motorcycle {
    void start();
}

final class Car implements Vehicle {
    public void start() {
        System.out.println("Car started");
    }
}

final class Truck implements Vehicle {
    public void start() {
        System.out.println("Truck started");
    }
}

final class Motorcycle implements Vehicle {
    public void start() {
        System.out.println("Motorcycle started");
    }
}

public class SealedClassesDemo {
    public static void main(String[] args) {
        Shape circle = new Circle(5.0);
        System.out.println("Circle area: " + circle.area());
        
        // Pattern matching with sealed classes (exhaustive)
        Shape shape = new Rectangle(4, 5);
        String description = switch (shape) {
            case Circle c -> "Circle with radius " + c.radius;
            case Rectangle r -> "Rectangle " + r.length + "x" + r.width;
            case Triangle t -> "Triangle";
            // No default needed - compiler knows all possibilities!
        };
        System.out.println(description);
    }
}
```

### Q12: Pattern Matching for instanceof (Java 16)

**Answer:**

```java
public class PatternMatchingDemo {
    public static void main(String[] args) {
        Object obj = "Hello World";
        
        // Old way
        if (obj instanceof String) {
            String str = (String) obj;
            System.out.println(str.toUpperCase());
        }
        
        // New way - Pattern Matching
        if (obj instanceof String str) {
            System.out.println(str.toUpperCase());
            // str is available here
        }
        
        // More examples
        demonstratePatterns();
    }
    
    static void demonstratePatterns() {
        Object obj = 42;
        
        // Pattern with condition
        if (obj instanceof Integer num && num > 10) {
            System.out.println("Large number: " + num);
        }
        
        // In switch (Java 17+)
        String result = switch (obj) {
            case Integer i && i > 0 -> "Positive integer: " + i;
            case Integer i -> "Non-positive integer: " + i;
            case String s -> "String: " + s;
            case null -> "null value";
            default -> "Unknown type";
        };
        System.out.println(result);
    }
}
```

---

## 🎯 Java 18-21 LTS (March 2022 - September 2023)

### Q13: Virtual Threads (Java 21)

**Answer:**

```java
import java.time.Duration;
import java.util.concurrent.*;

public class VirtualThreadsDemo {
    public static void main(String[] args) throws Exception {
        // Create virtual thread
        Thread vThread = Thread.ofVirtual().start(() -> {
            System.out.println("Running in virtual thread");
        });
        vThread.join();
        
        // ExecutorService with virtual threads
        try (ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor()) {
            for (int i = 0; i < 10_000; i++) {
                int taskId = i;
                executor.submit(() -> {
                    System.out.println("Task " + taskId + 
                        " on " + Thread.currentThread());
                });
            }
        } // Auto-close waits for tasks
        
        // Compare performance
        compareThreadPerformance();
    }
    
    static void compareThreadPerformance() throws Exception {
        int numTasks = 10_000;
        
        // Platform threads
        long start1 = System.currentTimeMillis();
        try (ExecutorService executor = Executors.newFixedThreadPool(200)) {
            for (int i = 0; i < numTasks; i++) {
                executor.submit(() -> {
                    try {
                        Thread.sleep(Duration.ofMillis(100));
                    } catch (InterruptedException e) {}
                });
            }
        }
        long end1 = System.currentTimeMillis();
        System.out.println("Platform threads: " + (end1 - start1) + " ms");
        
        // Virtual threads
        long start2 = System.currentTimeMillis();
        try (ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor()) {
            for (int i = 0; i < numTasks; i++) {
                executor.submit(() -> {
                    try {
                        Thread.sleep(Duration.ofMillis(100));
                    } catch (InterruptedException e) {}
                });
            }
        }
        long end2 = System.currentTimeMillis();
        System.out.println("Virtual threads: " + (end2 - start2) + " ms");
    }
}
```

### Q14: Sequenced Collections (Java 21)

**Answer:**

```java
import java.util.*;

public class SequencedCollectionsDemo {
    public static void main(String[] args) {
        // List is a SequencedCollection
        List<String> list = new ArrayList<>(List.of("A", "B", "C", "D"));
        
        // New methods
        System.out.println("First: " + list.getFirst());  // A
        System.out.println("Last: " + list.getLast());    // D
        
        list.addFirst("Z");  // [Z, A, B, C, D]
        list.addLast("E");   // [Z, A, B, C, D, E]
        
        list.removeFirst();  // [A, B, C, D, E]
        list.removeLast();   // [A, B, C, D]
        
        // Reversed view
        List<String> reversed = list.reversed();
        System.out.println("Reversed: " + reversed); // [D, C, B, A]
        
        // LinkedHashSet is also a SequencedSet
        SequencedSet<Integer> set = new LinkedHashSet<>(List.of(1, 2, 3, 4, 5));
        System.out.println("First: " + set.getFirst());
        System.out.println("Last: " + set.getLast());
        
        // LinkedHashMap is a SequencedMap
        SequencedMap<String, Integer> map = new LinkedHashMap<>();
        map.put("one", 1);
        map.put("two", 2);
        map.put("three", 3);
        
        System.out.println("First entry: " + map.firstEntry());
        System.out.println("Last entry: " + map.lastEntry());
        
        SequencedMap<String, Integer> reversedMap = map.reversed();
        System.out.println("Reversed map: " + reversedMap);
    }
}
```

---

## 🎯 Interview Questions

**Q15: What are the benefits of virtual threads?**

**Answer:**
- Lightweight (millions can run concurrently)
- Simplified concurrency
- No need for complex async/await
- Better resource utilization
- Improved scalability

**Q16: When to use records vs classes?**

**Answer:**

**Use Records when:**
- Immutable data carriers
- Simple data transfer objects (DTOs)
- Configuration objects
- Return multiple values from methods

**Use Classes when:**
- Need mutability
- Complex business logic
- Need inheritance
- Require custom encapsulation

---

**Stay updated with the latest Java features!** 🚀

