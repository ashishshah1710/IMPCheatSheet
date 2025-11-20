# ☕ Core Java - Intermediate Level

Master advanced Java concepts and prepare for technical interviews!

---

## 📚 Table of Contents

1. [Object-Oriented Programming (OOP) Deep Dive](#oop-deep-dive)
2. [Collections Framework](#collections-framework)
3. [Exception Handling](#exception-handling)
4. [Multithreading & Concurrency](#multithreading-concurrency)
5. [Java 8+ Features](#java-8-features)
6. [Generics](#generics)
7. [File I/O & Serialization](#file-io-serialization)
8. [Interview Questions & Answers](#interview-questions)

---

## 🎯 OOP Deep Dive

### Q1: What is the difference between Abstract Class and Interface?

**Answer:**

| Feature | Abstract Class | Interface |
|---------|---------------|-----------|
| **Methods** | Can have abstract and concrete methods | Before Java 8: only abstract methods. After Java 8: can have default and static methods |
| **Variables** | Can have instance variables (any access modifier) | Only public static final constants |
| **Constructor** | Can have constructors | Cannot have constructors |
| **Multiple Inheritance** | Cannot extend multiple classes | Can implement multiple interfaces |
| **Access Modifiers** | Can have any access modifier | Methods are public by default |
| **When to Use** | When classes share common code | When defining a contract |

**Example:**

```java
// Abstract Class
abstract class Vehicle {
    protected String brand;
    
    public Vehicle(String brand) {
        this.brand = brand;
    }
    
    // Concrete method
    public void displayBrand() {
        System.out.println("Brand: " + brand);
    }
    
    // Abstract method
    abstract void start();
}

// Interface
interface Drivable {
    void drive();
    
    default void stop() {
        System.out.println("Vehicle stopped");
    }
}

class Car extends Vehicle implements Drivable {
    public Car(String brand) {
        super(brand);
    }
    
    @Override
    void start() {
        System.out.println("Car engine started");
    }
    
    @Override
    public void drive() {
        System.out.println("Driving the car");
    }
}
```

### Q2: Explain the concept of Method Overriding vs Method Overloading

**Answer:**

**Method Overloading (Compile-time Polymorphism)**
- Same method name, different parameters
- Occurs in the same class or inherited class
- Return type can be different

**Method Overriding (Runtime Polymorphism)**
- Same method name, same parameters
- Occurs in parent-child relationship
- Return type must be same or covariant

```java
class Calculator {
    // Method Overloading
    public int add(int a, int b) {
        return a + b;
    }
    
    public double add(double a, double b) {
        return a + b;
    }
    
    public int add(int a, int b, int c) {
        return a + b + c;
    }
}

class Parent {
    public void display() {
        System.out.println("Parent display");
    }
}

class Child extends Parent {
    // Method Overriding
    @Override
    public void display() {
        System.out.println("Child display");
    }
}
```

### Q3: What is the difference between == and equals() method?

**Answer:**

- **`==` operator:** Compares references (memory addresses) for objects, values for primitives
- **`equals()` method:** Compares the actual content of objects

```java
public class EqualsDemo {
    public static void main(String[] args) {
        String s1 = new String("Hello");
        String s2 = new String("Hello");
        String s3 = "Hello";
        String s4 = "Hello";
        
        System.out.println(s1 == s2);        // false (different objects)
        System.out.println(s1.equals(s2));   // true (same content)
        System.out.println(s3 == s4);        // true (string pool)
        
        Integer i1 = new Integer(100);
        Integer i2 = new Integer(100);
        System.out.println(i1 == i2);        // false
        System.out.println(i1.equals(i2));   // true
    }
}
```

---

## 📦 Collections Framework

### Q4: Explain the Java Collections Hierarchy

**Answer:**

```
                    Iterable
                       |
                  Collection
                       |
        ┌──────────────┼──────────────┐
        |              |              |
       List           Set           Queue
        |              |              |
    ArrayList      HashSet       PriorityQueue
    LinkedList     TreeSet       LinkedList
    Vector         LinkedHashSet  ArrayDeque
```

**Key Interfaces:**
- **List:** Ordered, allows duplicates (ArrayList, LinkedList)
- **Set:** Unordered, no duplicates (HashSet, TreeSet)
- **Queue:** FIFO structure (PriorityQueue, LinkedList)
- **Map:** Key-value pairs (HashMap, TreeMap, LinkedHashMap)

### Q5: ArrayList vs LinkedList - When to use which?

**Answer:**

| Operation | ArrayList | LinkedList |
|-----------|-----------|------------|
| **Random Access** | O(1) - Fast | O(n) - Slow |
| **Insert/Delete at beginning** | O(n) - Slow | O(1) - Fast |
| **Insert/Delete at end** | O(1) - Fast | O(1) - Fast |
| **Insert/Delete in middle** | O(n) - Slow | O(1) - Fast (if position known) |
| **Memory** | Less overhead | More overhead (node pointers) |
| **Use Case** | Frequent access by index | Frequent insertions/deletions |

```java
// ArrayList - Better for random access
List<String> arrayList = new ArrayList<>();
arrayList.add("A");
arrayList.add("B");
arrayList.add("C");
System.out.println(arrayList.get(1)); // Fast O(1)

// LinkedList - Better for frequent insertions
List<String> linkedList = new LinkedList<>();
linkedList.add(0, "First");  // Fast at beginning
linkedList.add("Last");
```

### Q6: HashMap vs TreeMap vs LinkedHashMap

**Answer:**

| Feature | HashMap | TreeMap | LinkedHashMap |
|---------|---------|---------|---------------|
| **Order** | No order | Sorted (natural/comparator) | Insertion order |
| **Time Complexity** | O(1) avg | O(log n) | O(1) avg |
| **Null Keys** | One null key allowed | No null keys | One null key allowed |
| **Use Case** | Fast lookup | Sorted keys needed | Maintain insertion order |

```java
// HashMap - No order
Map<String, Integer> hashMap = new HashMap<>();
hashMap.put("Banana", 2);
hashMap.put("Apple", 1);
hashMap.put("Cherry", 3);
// Output order: unpredictable

// TreeMap - Sorted order
Map<String, Integer> treeMap = new TreeMap<>();
treeMap.put("Banana", 2);
treeMap.put("Apple", 1);
treeMap.put("Cherry", 3);
// Output: Apple, Banana, Cherry

// LinkedHashMap - Insertion order
Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
linkedHashMap.put("Banana", 2);
linkedHashMap.put("Apple", 1);
linkedHashMap.put("Cherry", 3);
// Output: Banana, Apple, Cherry
```

### Q7: How does HashMap work internally?

**Answer:**

HashMap uses an array of buckets with linked lists/trees for collision handling.

**Key Concepts:**
- **Hash Function:** Converts key to bucket index
- **Collision:** When two keys hash to same bucket
- **Load Factor:** 0.75 (resize when 75% full)
- **Initial Capacity:** 16 buckets by default

**Process:**
1. Key's hashCode() is called
2. Hash is computed: `hash = (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16)`
3. Index calculated: `index = (n - 1) & hash`
4. If bucket empty, add entry
5. If collision, use equals() to check existing keys
6. Store in linked list or tree (if >8 elements)

```java
public class HashMapInternals {
    public static void main(String[] args) {
        Map<Employee, String> map = new HashMap<>();
        
        Employee e1 = new Employee(1, "John");
        Employee e2 = new Employee(1, "John");
        
        map.put(e1, "Developer");
        map.put(e2, "Manager"); // Overwrites if equals/hashCode properly implemented
        
        System.out.println(map.size()); // 1 if properly implemented
    }
}

class Employee {
    private int id;
    private String name;
    
    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Employee employee = (Employee) o;
        return id == employee.id && Objects.equals(name, employee.name);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(id, name);
    }
}
```

---

## ⚠️ Exception Handling

### Q8: Checked vs Unchecked Exceptions

**Answer:**

**Checked Exceptions (Compile-time)**
- Must be caught or declared
- Extends Exception (not RuntimeException)
- Examples: IOException, SQLException, ClassNotFoundException

**Unchecked Exceptions (Runtime)**
- Not required to catch/declare
- Extends RuntimeException
- Examples: NullPointerException, ArrayIndexOutOfBoundsException, ArithmeticException

```java
// Checked Exception - Must handle
public void readFile(String path) throws IOException {
    FileReader reader = new FileReader(path);
    // Must declare throws or use try-catch
}

// Unchecked Exception - Optional handling
public int divide(int a, int b) {
    return a / b; // Can throw ArithmeticException
}
```

### Q9: Exception Handling Best Practices

**Answer:**

```java
// ✅ GOOD - Specific exceptions
try {
    // code
} catch (FileNotFoundException e) {
    // handle file not found
} catch (IOException e) {
    // handle other IO issues
}

// ❌ BAD - Catching generic Exception
try {
    // code
} catch (Exception e) {
    // too broad
}

// ✅ GOOD - Custom exceptions
class InsufficientBalanceException extends Exception {
    public InsufficientBalanceException(String message) {
        super(message);
    }
}

// ✅ GOOD - Try-with-resources (Auto-close)
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line = br.readLine();
} catch (IOException e) {
    e.printStackTrace();
}

// ✅ GOOD - Finally for cleanup
Connection conn = null;
try {
    conn = DriverManager.getConnection(url);
    // database operations
} catch (SQLException e) {
    e.printStackTrace();
} finally {
    if (conn != null) {
        try {
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

---

## 🧵 Multithreading & Concurrency

### Q10: Different ways to create a Thread

**Answer:**

```java
// Method 1: Extend Thread class
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread using Thread class");
    }
}

// Method 2: Implement Runnable interface
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Thread using Runnable interface");
    }
}

// Method 3: Using Lambda (Java 8+)
public class ThreadDemo {
    public static void main(String[] args) {
        // Method 1
        MyThread t1 = new MyThread();
        t1.start();
        
        // Method 2
        Thread t2 = new Thread(new MyRunnable());
        t2.start();
        
        // Method 3 - Lambda
        Thread t3 = new Thread(() -> {
            System.out.println("Thread using Lambda");
        });
        t3.start();
        
        // Method 4 - Callable with ExecutorService
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Future<String> future = executor.submit(() -> {
            return "Result from Callable";
        });
        executor.shutdown();
    }
}
```

### Q11: Synchronized vs Volatile

**Answer:**

**Synchronized:**
- Ensures mutual exclusion (only one thread accesses at a time)
- Provides visibility and atomicity
- Can be applied to methods or blocks

**Volatile:**
- Ensures visibility only (changes visible to all threads)
- No mutual exclusion
- Applied only to variables
- Prevents instruction reordering

```java
class Counter {
    private int count = 0;
    
    // Synchronized method
    public synchronized void increment() {
        count++;
    }
    
    public int getCount() {
        return count;
    }
}

class Flag {
    // Volatile variable
    private volatile boolean running = true;
    
    public void stop() {
        running = false; // Immediately visible to all threads
    }
    
    public void run() {
        while (running) {
            // do work
        }
    }
}
```

### Q12: What is Deadlock? How to prevent it?

**Answer:**

**Deadlock** occurs when two or more threads are blocked forever, waiting for each other.

**Conditions for Deadlock:**
1. Mutual Exclusion
2. Hold and Wait
3. No Preemption
4. Circular Wait

```java
// DEADLOCK EXAMPLE ❌
class DeadlockDemo {
    private static Object lock1 = new Object();
    private static Object lock2 = new Object();
    
    public static void main(String[] args) {
        Thread t1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1: Holding lock1");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                synchronized (lock2) {
                    System.out.println("Thread 1: Holding lock1 & lock2");
                }
            }
        });
        
        Thread t2 = new Thread(() -> {
            synchronized (lock2) {
                System.out.println("Thread 2: Holding lock2");
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                synchronized (lock1) {
                    System.out.println("Thread 2: Holding lock2 & lock1");
                }
            }
        });
        
        t1.start();
        t2.start();
    }
}

// PREVENTION ✅ - Same order of lock acquisition
class DeadlockPrevention {
    private static Object lock1 = new Object();
    private static Object lock2 = new Object();
    
    public static void main(String[] args) {
        Thread t1 = new Thread(() -> {
            synchronized (lock1) {
                synchronized (lock2) {
                    System.out.println("Thread 1 completed");
                }
            }
        });
        
        Thread t2 = new Thread(() -> {
            synchronized (lock1) { // Same order as t1
                synchronized (lock2) {
                    System.out.println("Thread 2 completed");
                }
            }
        });
        
        t1.start();
        t2.start();
    }
}
```

---

## 🚀 Java 8+ Features

### Q13: What are Lambda Expressions and Functional Interfaces?

**Answer:**

**Lambda Expression:** Anonymous function with concise syntax

```java
// Before Java 8
Runnable r1 = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello");
    }
};

// After Java 8 - Lambda
Runnable r2 = () -> System.out.println("Hello");

// Functional Interface - Interface with single abstract method
@FunctionalInterface
interface Calculator {
    int calculate(int a, int b);
}

public class LambdaDemo {
    public static void main(String[] args) {
        // Lambda implementation
        Calculator add = (a, b) -> a + b;
        Calculator multiply = (a, b) -> a * b;
        
        System.out.println(add.calculate(5, 3));      // 8
        System.out.println(multiply.calculate(5, 3)); // 15
    }
}
```

### Q14: Explain Stream API

**Answer:**

Stream API provides functional-style operations on collections.

```java
import java.util.*;
import java.util.stream.*;

public class StreamDemo {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // Filter, Map, Reduce
        int sum = numbers.stream()
            .filter(n -> n % 2 == 0)        // Even numbers: 2,4,6,8,10
            .map(n -> n * n)                 // Square: 4,16,36,64,100
            .reduce(0, (a, b) -> a + b);    // Sum: 220
        
        System.out.println("Sum: " + sum);
        
        // Collect to List
        List<Integer> evenSquares = numbers.stream()
            .filter(n -> n % 2 == 0)
            .map(n -> n * n)
            .collect(Collectors.toList());
        
        System.out.println(evenSquares); // [4, 16, 36, 64, 100]
        
        // Finding max/min
        Optional<Integer> max = numbers.stream().max(Integer::compareTo);
        System.out.println("Max: " + max.get()); // 10
        
        // Grouping
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David", "Anna");
        Map<Character, List<String>> grouped = names.stream()
            .collect(Collectors.groupingBy(name -> name.charAt(0)));
        
        System.out.println(grouped); // {A=[Alice, Anna], B=[Bob], C=[Charlie], D=[David]}
    }
}
```

### Q15: Optional class - What and Why?

**Answer:**

Optional is a container to handle null values gracefully and avoid NullPointerException.

```java
import java.util.Optional;

public class OptionalDemo {
    public static void main(String[] args) {
        // Creating Optional
        Optional<String> optional1 = Optional.of("Hello");
        Optional<String> optional2 = Optional.ofNullable(null);
        Optional<String> optional3 = Optional.empty();
        
        // isPresent() and get()
        if (optional1.isPresent()) {
            System.out.println(optional1.get()); // Hello
        }
        
        // orElse() - default value
        String value1 = optional2.orElse("Default Value");
        System.out.println(value1); // Default Value
        
        // orElseThrow()
        try {
            String value2 = optional2.orElseThrow(() -> 
                new RuntimeException("Value not present"));
        } catch (RuntimeException e) {
            System.out.println(e.getMessage());
        }
        
        // ifPresent() - Consumer
        optional1.ifPresent(val -> System.out.println("Value: " + val));
        
        // map()
        Optional<Integer> length = optional1.map(String::length);
        System.out.println(length.get()); // 5
        
        // filter()
        Optional<String> filtered = optional1.filter(s -> s.length() > 3);
        System.out.println(filtered.get()); // Hello
    }
    
    // Example usage in method
    public static Optional<User> findUserById(int id) {
        // Simulating database lookup
        if (id == 1) {
            return Optional.of(new User("John"));
        }
        return Optional.empty();
    }
}

class User {
    private String name;
    
    public User(String name) {
        this.name = name;
    }
    
    public String getName() {
        return name;
    }
}
```

---

## 📐 Generics

### Q16: What are Generics and why are they used?

**Answer:**

Generics provide type safety and eliminate the need for type casting.

```java
// Without Generics ❌
List list = new ArrayList();
list.add("Hello");
list.add(123);
String s = (String) list.get(1); // ClassCastException at runtime

// With Generics ✅
List<String> stringList = new ArrayList<>();
stringList.add("Hello");
// stringList.add(123); // Compile-time error

// Generic Class
class Box<T> {
    private T value;
    
    public void set(T value) {
        this.value = value;
    }
    
    public T get() {
        return value;
    }
}

// Generic Method
public class GenericMethod {
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        Integer[] intArray = {1, 2, 3, 4, 5};
        String[] strArray = {"Hello", "World"};
        
        printArray(intArray); // 1 2 3 4 5
        printArray(strArray); // Hello World
        
        Box<Integer> intBox = new Box<>();
        intBox.set(100);
        System.out.println(intBox.get()); // 100
        
        Box<String> strBox = new Box<>();
        strBox.set("Generic");
        System.out.println(strBox.get()); // Generic
    }
}
```

### Q17: Bounded Type Parameters and Wildcards

**Answer:**

```java
// Upper Bounded Type Parameter <T extends Number>
class Calculator<T extends Number> {
    private T num;
    
    public Calculator(T num) {
        this.num = num;
    }
    
    public double getDoubleValue() {
        return num.doubleValue();
    }
}

// Wildcards
public class WildcardDemo {
    // Upper Bounded Wildcard <? extends Type>
    public static double sumOfList(List<? extends Number> list) {
        double sum = 0.0;
        for (Number num : list) {
            sum += num.doubleValue();
        }
        return sum;
    }
    
    // Lower Bounded Wildcard <? super Type>
    public static void addNumbers(List<? super Integer> list) {
        list.add(1);
        list.add(2);
        list.add(3);
    }
    
    // Unbounded Wildcard <?>
    public static void printList(List<?> list) {
        for (Object obj : list) {
            System.out.print(obj + " ");
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        List<Integer> intList = Arrays.asList(1, 2, 3);
        List<Double> doubleList = Arrays.asList(1.1, 2.2, 3.3);
        
        System.out.println(sumOfList(intList));    // 6.0
        System.out.println(sumOfList(doubleList)); // 6.6
        
        List<Number> numList = new ArrayList<>();
        addNumbers(numList);
        printList(numList); // 1 2 3
    }
}
```

---

## 💾 File I/O & Serialization

### Q18: Different ways to read a file in Java

**Answer:**

```java
import java.io.*;
import java.nio.file.*;
import java.util.stream.*;

public class FileReadingDemo {
    public static void main(String[] args) {
        String filePath = "example.txt";
        
        // Method 1: BufferedReader (traditional)
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // Method 2: Files.readAllLines() (Java 7+)
        try {
            List<String> lines = Files.readAllLines(Paths.get(filePath));
            lines.forEach(System.out::println);
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // Method 3: Files.lines() with Stream (Java 8+)
        try (Stream<String> stream = Files.lines(Paths.get(filePath))) {
            stream.forEach(System.out::println);
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // Method 4: Scanner
        try (Scanner scanner = new Scanner(new File(filePath))) {
            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

### Q19: What is Serialization? Explain with example

**Answer:**

**Serialization:** Converting object to byte stream (for storage/transmission)  
**Deserialization:** Converting byte stream back to object

```java
import java.io.*;

// Class must implement Serializable
class Employee implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private String name;
    private int age;
    private transient String password; // Won't be serialized
    
    public Employee(String name, int age, String password) {
        this.name = name;
        this.age = age;
        this.password = password;
    }
    
    @Override
    public String toString() {
        return "Employee{name='" + name + "', age=" + age + 
               ", password='" + password + "'}";
    }
}

public class SerializationDemo {
    public static void main(String[] args) {
        Employee emp = new Employee("John Doe", 30, "secret123");
        
        // Serialization
        try (ObjectOutputStream oos = new ObjectOutputStream(
                new FileOutputStream("employee.ser"))) {
            oos.writeObject(emp);
            System.out.println("Serialization complete");
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // Deserialization
        try (ObjectInputStream ois = new ObjectInputStream(
                new FileInputStream("employee.ser"))) {
            Employee deserializedEmp = (Employee) ois.readObject();
            System.out.println("Deserialized: " + deserializedEmp);
            // Note: password will be null (transient)
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

**Key Points:**
- Class must implement `Serializable`
- `serialVersionUID` ensures version compatibility
- `transient` keyword excludes fields from serialization
- Static fields are not serialized

---

## 🎯 Top 50 Interview Questions & Answers

### Memory Management

**Q20: Explain JVM memory structure**

**Answer:**
```
┌─────────────────────────────────────────┐
│           JVM Memory                     │
├─────────────────────────────────────────┤
│  Heap (Shared)                          │
│  - Young Generation                     │
│    - Eden Space                         │
│    - Survivor Space (S0, S1)            │
│  - Old Generation (Tenured)             │
│  - Metaspace (Java 8+)                  │
├─────────────────────────────────────────┤
│  Stack (Thread-specific)                │
│  - Local variables                      │
│  - Method call information              │
├─────────────────────────────────────────┤
│  PC Register (Thread-specific)          │
│  - Current instruction pointer          │
├─────────────────────────────────────────┤
│  Native Method Stack                    │
│  - Native method information            │
└─────────────────────────────────────────┘
```

**Q21: What is Garbage Collection?**

**Answer:** Automatic memory management that reclaims unused objects.

**GC Algorithms:**
- Serial GC
- Parallel GC
- CMS (Concurrent Mark Sweep)
- G1 GC (Garbage First)
- ZGC (Low latency)

---

### String Handling

**Q22: Why String is immutable in Java?**

**Answer:**

**Reasons:**
1. **Security:** Prevents modification of sensitive data
2. **Thread Safety:** No synchronization needed
3. **String Pool:** Enables string interning for memory efficiency
4. **Hashcode Caching:** Immutable hashcode for HashMap performance

```java
String s1 = "Hello";
String s2 = "Hello"; // Points to same object in string pool
String s3 = new String("Hello"); // Creates new object

System.out.println(s1 == s2);  // true (same reference)
System.out.println(s1 == s3);  // false (different reference)
System.out.println(s1.equals(s3)); // true (same content)
```

**Q23: String vs StringBuilder vs StringBuffer**

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|---------------|--------------|
| **Mutability** | Immutable | Mutable | Mutable |
| **Thread Safety** | Yes | No | Yes (synchronized) |
| **Performance** | Slower (concatenation) | Fast | Slower than StringBuilder |
| **Use Case** | Few modifications | Single thread | Multi-threaded |

---

### Design Patterns

**Q24: Implement Singleton Pattern**

**Answer:**

```java
// Thread-safe Singleton
public class Singleton {
    private static volatile Singleton instance;
    
    private Singleton() {
        // Private constructor
    }
    
    // Double-checked locking
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}

// Enum Singleton (Best approach)
public enum SingletonEnum {
    INSTANCE;
    
    public void doSomething() {
        System.out.println("Doing something");
    }
}
```

---

### Additional Quick Questions

**Q25: What is the difference between final, finally, and finalize?**

- **final:** Keyword for constants, prevent inheritance/override
- **finally:** Block that always executes after try-catch
- **finalize():** Method called by GC before object destruction (deprecated)

**Q26: Can we override static methods?**

No, static methods belong to class, not instance. We can hide them but not override.

**Q27: What is marker interface?**

Interface with no methods. Example: Serializable, Cloneable, Remote

**Q28: What is the purpose of default keyword in interface?**

Allows adding new methods to interfaces without breaking existing implementations.

---

## 🎓 Practice Tips

1. **Code Daily:** Practice at least one concept daily
2. **Build Projects:** Apply concepts in real applications
3. **Mock Interviews:** Practice explaining concepts verbally
4. **LeetCode/HackerRank:** Solve medium-level problems
5. **Review:** Revisit topics weekly

---

## 📚 Next Steps

- Move to **Advanced Java** for Spring, Hibernate, Microservices
- Practice **Design Patterns**
- Learn **JVM Internals** and **Performance Tuning**
- Master **Concurrency** utilities (ExecutorService, Fork/Join)

---

**Happy Learning! 🚀**

