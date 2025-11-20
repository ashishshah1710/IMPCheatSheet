# 🚀 Functional Programming in Java

Master functional programming concepts in Java 8+!

---

## 📚 Table of Contents

1. [Lambda Expressions](#lambda-expressions)
2. [Functional Interfaces](#functional-interfaces)
3. [Stream API](#stream-api)
4. [Method References](#method-references)
5. [Optional Class](#optional-class)
6. [Collectors](#collectors)
7. [Interview Questions](#interview-questions)

---

## λ Lambda Expressions

### Q1: Lambda Expression Syntax

**Answer:**

```java
import java.util.*;
import java.util.function.*;

public class LambdaBasics {
    public static void main(String[] args) {
        // No parameters
        Runnable r1 = () -> System.out.println("Hello Lambda");
        
        // Single parameter
        Consumer<String> print = str -> System.out.println(str);
        
        // Multiple parameters
        BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
        
        // Multi-line lambda
        BiFunction<Integer, Integer, Integer> multiply = (a, b) -> {
            System.out.println("Multiplying " + a + " and " + b);
            return a * b;
        };
        
        // Execute lambdas
        r1.run();
        print.accept("Lambda expression");
        System.out.println("Sum: " + add.apply(5, 3));
        System.out.println("Product: " + multiply.apply(4, 6));
    }
}
```

---

## 🎯 Functional Interfaces

### Q2: Built-in Functional Interfaces

**Answer:**

```java
import java.util.function.*;

public class FunctionalInterfacesDemo {
    public static void main(String[] args) {
        // 1. Predicate<T> - Takes T, returns boolean
        Predicate<Integer> isEven = num -> num % 2 == 0;
        System.out.println("Is 4 even? " + isEven.test(4));
        
        // 2. Function<T, R> - Takes T, returns R
        Function<String, Integer> length = str -> str.length();
        System.out.println("Length of 'Hello': " + length.apply("Hello"));
        
        // 3. Consumer<T> - Takes T, returns void
        Consumer<String> print = str -> System.out.println(str);
        print.accept("Hello Consumer");
        
        // 4. Supplier<T> - Takes nothing, returns T
        Supplier<Double> random = () -> Math.random();
        System.out.println("Random number: " + random.get());
        
        // 5. BiPredicate<T, U> - Takes T and U, returns boolean
        BiPredicate<String, Integer> isLengthEqual = (str, len) -> str.length() == len;
        System.out.println("Is length equal? " + isLengthEqual.test("Hello", 5));
        
        // 6. BiFunction<T, U, R> - Takes T and U, returns R
        BiFunction<Integer, Integer, Integer> multiply = (a, b) -> a * b;
        System.out.println("5 * 3 = " + multiply.apply(5, 3));
        
        // 7. UnaryOperator<T> - Takes T, returns T
        UnaryOperator<Integer> square = n -> n * n;
        System.out.println("Square of 5: " + square.apply(5));
        
        // 8. BinaryOperator<T> - Takes two T, returns T
        BinaryOperator<Integer> max = (a, b) -> a > b ? a : b;
        System.out.println("Max of 5 and 8: " + max.apply(5, 8));
    }
}
```

### Q3: Custom Functional Interface

**Answer:**

```java
@FunctionalInterface
interface Calculator {
    int calculate(int a, int b);
    
    // Default methods allowed
    default int add(int a, int b) {
        return a + b;
    }
    
    // Static methods allowed
    static int subtract(int a, int b) {
        return a - b;
    }
}

public class CustomFunctionalInterfaceDemo {
    public static void main(String[] args) {
        // Lambda implementation
        Calculator multiplication = (a, b) -> a * b;
        Calculator division = (a, b) -> a / b;
        
        System.out.println("Multiplication: " + multiplication.calculate(5, 3));
        System.out.println("Division: " + division.calculate(15, 3));
        System.out.println("Addition: " + multiplication.add(5, 3));
        System.out.println("Subtraction: " + Calculator.subtract(10, 4));
    }
}
```

---

## 🌊 Stream API

### Q4: Stream Operations

**Answer:**

```java
import java.util.*;
import java.util.stream.*;

public class StreamOperationsDemo {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // INTERMEDIATE OPERATIONS (return Stream)
        
        // 1. filter() - Filter elements
        List<Integer> evenNumbers = numbers.stream()
            .filter(n -> n % 2 == 0)
            .collect(Collectors.toList());
        System.out.println("Even numbers: " + evenNumbers);
        
        // 2. map() - Transform elements
        List<Integer> squares = numbers.stream()
            .map(n -> n * n)
            .collect(Collectors.toList());
        System.out.println("Squares: " + squares);
        
        // 3. flatMap() - Flatten nested structures
        List<List<Integer>> listOfLists = Arrays.asList(
            Arrays.asList(1, 2, 3),
            Arrays.asList(4, 5, 6),
            Arrays.asList(7, 8, 9)
        );
        List<Integer> flattened = listOfLists.stream()
            .flatMap(List::stream)
            .collect(Collectors.toList());
        System.out.println("Flattened: " + flattened);
        
        // 4. distinct() - Remove duplicates
        List<Integer> withDuplicates = Arrays.asList(1, 2, 2, 3, 3, 3, 4, 5, 5);
        List<Integer> unique = withDuplicates.stream()
            .distinct()
            .collect(Collectors.toList());
        System.out.println("Unique: " + unique);
        
        // 5. sorted() - Sort elements
        List<Integer> sorted = numbers.stream()
            .sorted(Comparator.reverseOrder())
            .collect(Collectors.toList());
        System.out.println("Sorted descending: " + sorted);
        
        // 6. peek() - Perform action without consuming
        List<Integer> peeked = numbers.stream()
            .peek(n -> System.out.println("Processing: " + n))
            .filter(n -> n > 5)
            .collect(Collectors.toList());
        
        // 7. limit() - Limit number of elements
        List<Integer> limited = numbers.stream()
            .limit(5)
            .collect(Collectors.toList());
        System.out.println("Limited to 5: " + limited);
        
        // 8. skip() - Skip first n elements
        List<Integer> skipped = numbers.stream()
            .skip(5)
            .collect(Collectors.toList());
        System.out.println("Skipped first 5: " + skipped);
        
        // TERMINAL OPERATIONS (produce result)
        
        // 1. forEach() - Perform action on each element
        System.out.print("ForEach: ");
        numbers.stream().forEach(n -> System.out.print(n + " "));
        System.out.println();
        
        // 2. collect() - Convert to collection
        Set<Integer> set = numbers.stream().collect(Collectors.toSet());
        
        // 3. reduce() - Reduce to single value
        int sum = numbers.stream()
            .reduce(0, (a, b) -> a + b);
        System.out.println("Sum: " + sum);
        
        // 4. count() - Count elements
        long count = numbers.stream()
            .filter(n -> n > 5)
            .count();
        System.out.println("Count > 5: " + count);
        
        // 5. anyMatch(), allMatch(), noneMatch()
        boolean hasEven = numbers.stream().anyMatch(n -> n % 2 == 0);
        boolean allPositive = numbers.stream().allMatch(n -> n > 0);
        boolean noneNegative = numbers.stream().noneMatch(n -> n < 0);
        System.out.println("Has even: " + hasEven);
        System.out.println("All positive: " + allPositive);
        System.out.println("None negative: " + noneNegative);
        
        // 6. findFirst(), findAny()
        Optional<Integer> first = numbers.stream()
            .filter(n -> n > 5)
            .findFirst();
        first.ifPresent(n -> System.out.println("First > 5: " + n));
        
        // 7. min(), max()
        Optional<Integer> min = numbers.stream().min(Integer::compareTo);
        Optional<Integer> max = numbers.stream().max(Integer::compareTo);
        System.out.println("Min: " + min.get());
        System.out.println("Max: " + max.get());
    }
}
```

### Q5: Complex Stream Examples

**Answer:**

```java
import java.util.*;
import java.util.stream.*;

class Employee {
    private String name;
    private String department;
    private double salary;
    private int age;
    
    public Employee(String name, String department, double salary, int age) {
        this.name = name;
        this.department = department;
        this.salary = salary;
        this.age = age;
    }
    
    // Getters
    public String getName() { return name; }
    public String getDepartment() { return department; }
    public double getSalary() { return salary; }
    public int getAge() { return age; }
    
    @Override
    public String toString() {
        return name + "(" + department + ", $" + salary + ", " + age + "y)";
    }
}

public class ComplexStreamExamples {
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("John", "IT", 75000, 30),
            new Employee("Jane", "HR", 65000, 28),
            new Employee("Bob", "IT", 85000, 35),
            new Employee("Alice", "Finance", 70000, 32),
            new Employee("Charlie", "IT", 95000, 40),
            new Employee("Diana", "HR", 60000, 26),
            new Employee("Eve", "Finance", 80000, 33)
        );
        
        // 1. Group by department
        Map<String, List<Employee>> byDepartment = employees.stream()
            .collect(Collectors.groupingBy(Employee::getDepartment));
        System.out.println("Grouped by department:");
        byDepartment.forEach((dept, emps) -> 
            System.out.println(dept + ": " + emps));
        
        // 2. Average salary by department
        Map<String, Double> avgSalaryByDept = employees.stream()
            .collect(Collectors.groupingBy(
                Employee::getDepartment,
                Collectors.averagingDouble(Employee::getSalary)
            ));
        System.out.println("\nAverage salary by department: " + avgSalaryByDept);
        
        // 3. Highest paid employee in each department
        Map<String, Optional<Employee>> highestPaidByDept = employees.stream()
            .collect(Collectors.groupingBy(
                Employee::getDepartment,
                Collectors.maxBy(Comparator.comparingDouble(Employee::getSalary))
            ));
        System.out.println("\nHighest paid by department:");
        highestPaidByDept.forEach((dept, emp) -> 
            System.out.println(dept + ": " + emp.get()));
        
        // 4. Partition by salary (above/below 70000)
        Map<Boolean, List<Employee>> partitioned = employees.stream()
            .collect(Collectors.partitioningBy(e -> e.getSalary() > 70000));
        System.out.println("\nHigh salary (>70k): " + partitioned.get(true));
        System.out.println("Low salary (<=70k): " + partitioned.get(false));
        
        // 5. Top 3 highest paid employees
        List<Employee> top3 = employees.stream()
            .sorted(Comparator.comparingDouble(Employee::getSalary).reversed())
            .limit(3)
            .collect(Collectors.toList());
        System.out.println("\nTop 3 highest paid: " + top3);
        
        // 6. Total salary by department
        Map<String, Double> totalSalaryByDept = employees.stream()
            .collect(Collectors.groupingBy(
                Employee::getDepartment,
                Collectors.summingDouble(Employee::getSalary)
            ));
        System.out.println("\nTotal salary by department: " + totalSalaryByDept);
        
        // 7. Count employees by department
        Map<String, Long> countByDept = employees.stream()
            .collect(Collectors.groupingBy(
                Employee::getDepartment,
                Collectors.counting()
            ));
        System.out.println("\nCount by department: " + countByDept);
        
        // 8. Names of IT employees sorted by salary
        String itNames = employees.stream()
            .filter(e -> e.getDepartment().equals("IT"))
            .sorted(Comparator.comparingDouble(Employee::getSalary))
            .map(Employee::getName)
            .collect(Collectors.joining(", ", "[", "]"));
        System.out.println("\nIT employees by salary: " + itNames);
        
        // 9. Statistics on salaries
        DoubleSummaryStatistics stats = employees.stream()
            .mapToDouble(Employee::getSalary)
            .summaryStatistics();
        System.out.println("\nSalary statistics:");
        System.out.println("Count: " + stats.getCount());
        System.out.println("Sum: $" + stats.getSum());
        System.out.println("Min: $" + stats.getMin());
        System.out.println("Max: $" + stats.getMax());
        System.out.println("Average: $" + stats.getAverage());
    }
}
```

---

## 🎯 Method References

### Q6: Types of Method References

**Answer:**

```java
import java.util.*;
import java.util.function.*;

public class MethodReferencesDemo {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("John", "Jane", "Bob", "Alice");
        
        // 1. STATIC METHOD REFERENCE
        // ClassName::staticMethod
        List<Integer> numbers = Arrays.asList(1, -2, 3, -4, 5);
        List<Integer> absolute = numbers.stream()
            .map(Math::abs)
            .collect(Collectors.toList());
        System.out.println("Absolute values: " + absolute);
        
        // 2. INSTANCE METHOD REFERENCE on particular object
        // object::instanceMethod
        String prefix = "Hello, ";
        Greeter greeter = new Greeter();
        names.forEach(greeter::greet);
        
        // 3. INSTANCE METHOD REFERENCE on arbitrary object
        // ClassName::instanceMethod
        List<String> uppercase = names.stream()
            .map(String::toUpperCase)
            .collect(Collectors.toList());
        System.out.println("Uppercase: " + uppercase);
        
        // Sorting example
        List<String> sorted = new ArrayList<>(names);
        sorted.sort(String::compareToIgnoreCase);
        System.out.println("Sorted: " + sorted);
        
        // 4. CONSTRUCTOR REFERENCE
        // ClassName::new
        
        // Array constructor
        Function<Integer, String[]> arrayCreator = String[]::new;
        String[] array = arrayCreator.apply(5);
        System.out.println("Array length: " + array.length);
        
        // Object constructor
        Supplier<ArrayList<String>> listSupplier = ArrayList::new;
        ArrayList<String> list = listSupplier.get();
        
        // Constructor with parameters
        BiFunction<String, Integer, Person> personCreator = Person::new;
        Person person = personCreator.apply("John", 30);
        System.out.println("Created: " + person);
        
        // Stream example with constructor reference
        List<Person> people = names.stream()
            .map(name -> new Person(name, 25))
            .collect(Collectors.toList());
        
        // More examples
        demonstrateMoreReferences();
    }
    
    static void demonstrateMoreReferences() {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        
        // Method reference vs Lambda
        numbers.forEach(System.out::println);  // Method reference
        // vs
        numbers.forEach(n -> System.out.println(n)); // Lambda
        
        // Predicate with method reference
        Predicate<String> isEmpty = String::isEmpty;
        System.out.println("Is empty: " + isEmpty.test(""));
        
        // BiPredicate with method reference
        BiPredicate<String, String> equals = String::equals;
        System.out.println("Equals: " + equals.test("hello", "hello"));
    }
}

class Greeter {
    public void greet(String name) {
        System.out.println("Hello, " + name);
    }
}

class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    @Override
    public String toString() {
        return name + " (" + age + ")";
    }
}
```

---

## 📦 Optional Class

### Q7: Optional Usage

**Answer:**

```java
import java.util.*;

public class OptionalDemo {
    public static void main(String[] args) {
        // CREATING OPTIONAL
        
        // 1. Optional.of() - value must not be null
        Optional<String> opt1 = Optional.of("Hello");
        
        // 2. Optional.ofNullable() - value can be null
        Optional<String> opt2 = Optional.ofNullable(null);
        
        // 3. Optional.empty() - empty optional
        Optional<String> opt3 = Optional.empty();
        
        // CHECKING PRESENCE
        
        // 1. isPresent() - returns boolean
        if (opt1.isPresent()) {
            System.out.println("Value present: " + opt1.get());
        }
        
        // 2. ifPresent() - execute if present
        opt1.ifPresent(val -> System.out.println("Value: " + val));
        
        // 3. ifPresentOrElse() (Java 9+)
        opt2.ifPresentOrElse(
            val -> System.out.println("Value: " + val),
            () -> System.out.println("No value present")
        );
        
        // RETRIEVING VALUES
        
        // 1. get() - throws exception if empty
        try {
            String value = opt1.get();
            System.out.println("Got value: " + value);
        } catch (NoSuchElementException e) {
            System.out.println("No value present");
        }
        
        // 2. orElse() - default value
        String value1 = opt2.orElse("Default");
        System.out.println("Value or default: " + value1);
        
        // 3. orElseGet() - default from supplier
        String value2 = opt2.orElseGet(() -> "Generated Default");
        System.out.println("Value or generated: " + value2);
        
        // 4. orElseThrow() - throw custom exception
        try {
            String value3 = opt2.orElseThrow(() -> 
                new RuntimeException("Value not present"));
        } catch (RuntimeException e) {
            System.out.println("Exception: " + e.getMessage());
        }
        
        // TRANSFORMING OPTIONAL
        
        // 1. map() - transform value
        Optional<Integer> length = opt1.map(String::length);
        System.out.println("Length: " + length.get());
        
        // 2. flatMap() - avoid nested Optional
        Optional<String> upper = opt1.flatMap(s -> Optional.of(s.toUpperCase()));
        System.out.println("Uppercase: " + upper.get());
        
        // 3. filter() - filter value
        Optional<String> filtered = opt1.filter(s -> s.length() > 3);
        System.out.println("Filtered: " + filtered.orElse("Too short"));
        
        // REAL-WORLD EXAMPLES
        realWorldExamples();
    }
    
    static void realWorldExamples() {
        System.out.println("\n=== Real World Examples ===");
        
        // Example 1: User lookup
        Optional<User> user = findUserById(1);
        String userName = user.map(User::getName)
                             .orElse("Guest");
        System.out.println("User name: " + userName);
        
        // Example 2: Nested optional handling
        Optional<User> user2 = findUserById(1);
        String email = user2.flatMap(User::getEmail)
                           .orElse("no-email@example.com");
        System.out.println("Email: " + email);
        
        // Example 3: Chaining
        Optional<User> user3 = findUserById(2);
        String message = user3.filter(u -> u.getAge() > 18)
                             .map(u -> "Adult user: " + u.getName())
                             .orElse("Minor or user not found");
        System.out.println(message);
    }
    
    static Optional<User> findUserById(int id) {
        if (id == 1) {
            return Optional.of(new User("John Doe", "john@example.com", 25));
        }
        return Optional.empty();
    }
}

class User {
    private String name;
    private String email;
    private int age;
    
    public User(String name, String email, int age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }
    
    public String getName() { return name; }
    public Optional<String> getEmail() { return Optional.ofNullable(email); }
    public int getAge() { return age; }
}
```

---

## 🎯 Interview Questions

**Q8: What is the difference between map() and flatMap()?**

**Answer:**
- `map()`: Transforms each element (1-to-1 mapping)
- `flatMap()`: Transforms and flattens (1-to-many mapping)

```java
List<String> words = Arrays.asList("Hello", "World");

// map() - returns Stream<String[]>
words.stream()
    .map(word -> word.split(""))
    .forEach(System.out::println); // Prints array objects

// flatMap() - returns Stream<String>
words.stream()
    .flatMap(word -> Arrays.stream(word.split("")))
    .forEach(System.out::println); // Prints individual characters
```

**Q9: Parallel Streams - When to use?**

**Answer:**

```java
List<Integer> numbers = IntStream.rangeClosed(1, 1000000)
    .boxed()
    .collect(Collectors.toList());

// Sequential stream
long start1 = System.currentTimeMillis();
long sum1 = numbers.stream()
    .mapToLong(Integer::longValue)
    .sum();
long end1 = System.currentTimeMillis();
System.out.println("Sequential time: " + (end1 - start1) + " ms");

// Parallel stream
long start2 = System.currentTimeMillis();
long sum2 = numbers.parallelStream()
    .mapToLong(Integer::longValue)
    .sum();
long end2 = System.currentTimeMillis();
System.out.println("Parallel time: " + (end2 - start2) + " ms");
```

**Use parallel streams when:**
- Large datasets (>10,000 elements)
- CPU-intensive operations
- No shared mutable state
- Order doesn't matter

---

**Master functional programming for modern Java!** 🎯

