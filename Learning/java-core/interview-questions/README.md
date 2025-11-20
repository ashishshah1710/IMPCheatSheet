# 💼 Java Core - Interview Questions & Answers

**Comprehensive interview preparation with simple explanations!**

---

## 📚 Table of Contents

1. [Object-Oriented Programming (OOP)](#oop-questions)
2. [String & String Pool](#string-questions)
3. [Collections Framework](#collections-questions)
4. [Exception Handling](#exception-questions)
5. [Multithreading & Concurrency](#multithreading-questions)
6. [Java 8+ Features](#java8-questions)
7. [Memory Management](#memory-questions)
8. [Generics](#generics-questions)
9. [Tricky Questions](#tricky-questions)

---

## 🎯 OOP Questions

### Q1: What is Object-Oriented Programming?

**Simple Explanation:**
OOP is a programming style where we organize code around "objects" rather than "actions". Think of objects as real-world things (like a Car, Person, or BankAccount) that have:
- **Properties** (what they have) - like color, name, balance
- **Behaviors** (what they can do) - like drive(), eat(), withdraw()

**4 Main Principles:**
1. **Encapsulation** - Hide internal details, show only what's needed
2. **Inheritance** - Child gets features from parent
3. **Polymorphism** - Same thing behaves differently in different situations
4. **Abstraction** - Show only essential features, hide complexity

**Example:**
```java
// Real-world object as Java class
class BankAccount {
    // Properties (Encapsulation - private data)
    private String accountNumber;
    private double balance;
    
    // Behaviors (Methods)
    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }
    
    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        }
    }
    
    public double getBalance() {
        return balance;
    }
}
```

---

### Q2: What is the difference between Abstract Class and Interface?

**Simple Explanation:**

**Abstract Class = Partial Blueprint**
- Can have both complete methods (with code) and incomplete methods (without code)
- Can have variables
- Child can extend only ONE abstract class
- Use when: Classes share common code

**Interface = Pure Contract**
- Originally only method names (contract), but Java 8+ allows some code
- Can only have constants (final variables)
- Child can implement MULTIPLE interfaces
- Use when: Defining what a class should do, not how

**Real-Life Analogy:**
- **Abstract Class:** Like a "Vehicle" blueprint - has common features (engine, wheels) that all vehicles share
- **Interface:** Like a "Flyable" contract - anything can fly (bird, plane, drone) but each flies differently

**Example:**
```java
// Abstract Class - Partial code sharing
abstract class Animal {
    String name; // Can have variables
    
    // Complete method - all animals share this
    public void sleep() {
        System.out.println(name + " is sleeping");
    }
    
    // Incomplete method - each animal sounds different
    abstract void makeSound();
}

// Interface - Pure contract
interface Swimmable {
    void swim(); // Just method signature
}

// Child class
class Dog extends Animal implements Swimmable {
    @Override
    void makeSound() {
        System.out.println("Woof! Woof!");
    }
    
    @Override
    public void swim() {
        System.out.println("Dog is swimming");
    }
}
```

---

### Q3: What is Polymorphism? Explain with example.

**Simple Explanation:**
Polymorphism = "Many Forms"

One thing can behave in different ways depending on the situation.

**Types:**
1. **Compile-time (Method Overloading)** - Same name, different parameters
2. **Runtime (Method Overriding)** - Same signature, different behavior in child

**Real-Life Analogy:**
You are a "person" but:
- At home: You're a son/daughter
- At work: You're an employee
- At gym: You're a member

Same person, different roles (forms)!

**Example:**
```java
// Method Overloading (Compile-time Polymorphism)
class Calculator {
    // Same method name, different parameters
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

// Method Overriding (Runtime Polymorphism)
class Shape {
    public void draw() {
        System.out.println("Drawing shape");
    }
}

class Circle extends Shape {
    @Override
    public void draw() {
        System.out.println("Drawing circle ⭕");
    }
}

class Square extends Shape {
    @Override
    public void draw() {
        System.out.println("Drawing square ⬜");
    }
}

// Usage - One reference, many forms
public class Test {
    public static void main(String[] args) {
        Shape shape1 = new Circle(); // Parent reference, Child object
        Shape shape2 = new Square();
        
        shape1.draw(); // Calls Circle's draw()
        shape2.draw(); // Calls Square's draw()
    }
}
```

---

### Q4: What is Encapsulation and why is it important?

**Simple Explanation:**
Encapsulation = Wrapping data and code together + Hiding internal details

Like a capsule medicine 💊 - you don't see what's inside, you just use it.

**Why Important?**
1. **Security** - Protect data from unauthorized access
2. **Control** - Validate data before setting
3. **Flexibility** - Change internal code without affecting others
4. **Maintainability** - Easy to update and maintain

**How to Achieve:**
- Make variables `private`
- Provide public `getter` and `setter` methods

**Example:**
```java
// ❌ BAD - No Encapsulation
class Employee {
    public String name;
    public int salary;
    
    // Anyone can do this:
    // emp.salary = -5000; (Invalid!)
}

// ✅ GOOD - With Encapsulation
class Employee {
    private String name;
    private int salary;
    
    // Getter - Read access
    public int getSalary() {
        return salary;
    }
    
    // Setter - Controlled write access
    public void setSalary(int salary) {
        // Validation before setting
        if (salary > 0) {
            this.salary = salary;
        } else {
            System.out.println("Invalid salary!");
        }
    }
}

// Usage
Employee emp = new Employee();
emp.setSalary(50000);    // ✅ Valid
emp.setSalary(-5000);    // ❌ Rejected by validation
```

---

### Q5: What is the difference between Composition and Inheritance?

**Simple Explanation:**

**Inheritance = "IS-A" Relationship**
- Child IS-A type of Parent
- Example: Dog IS-A Animal

**Composition = "HAS-A" Relationship**
- Class HAS-A another class as member
- Example: Car HAS-A Engine

**Which is Better?**
**Composition is generally preferred** because:
- More flexible
- Avoids tight coupling
- Can change behavior at runtime

**Real-Life Analogy:**
- **Inheritance:** You inherit features from your parents (eyes, height) - you can't change them
- **Composition:** Your car has an engine - you can replace the engine anytime

**Example:**
```java
// Inheritance - IS-A
class Animal {
    public void eat() {
        System.out.println("Eating...");
    }
}

class Dog extends Animal { // Dog IS-A Animal
    public void bark() {
        System.out.println("Barking...");
    }
}

// Composition - HAS-A (Better approach)
class Engine {
    public void start() {
        System.out.println("Engine started");
    }
}

class Car {
    private Engine engine; // Car HAS-A Engine
    
    public Car() {
        engine = new Engine(); // Can use any Engine type
    }
    
    public void startCar() {
        engine.start();
        System.out.println("Car is ready to drive");
    }
}

// Why Composition is better:
class ElectricCar {
    private Engine engine;
    
    public ElectricCar() {
        engine = new ElectricEngine(); // Easily switch engine type!
    }
}
```

---

## 📝 String Questions

### Q6: Why are Strings immutable in Java?

**Simple Explanation:**
Immutable = Once created, cannot be changed

**Why Immutable?**

1. **String Pool Efficiency**
   - Multiple variables can share same String object
   - Saves memory

2. **Security**
   - Strings used in file paths, URLs, passwords
   - If mutable, someone could change them

3. **Thread Safety**
   - Multiple threads can share String without synchronization

4. **Hashcode Caching**
   - Hashcode calculated once and reused
   - Important for HashMap, HashSet

**Example:**
```java
String s1 = "Hello";
s1.concat(" World"); // Doesn't change s1
System.out.println(s1); // Still prints: Hello

// What actually happens:
String s2 = s1.concat(" World"); // Creates NEW object
System.out.println(s2); // Prints: Hello World
```

**Visual Explanation:**
```
String Pool:
┌─────────┐
│ "Hello" │ ← s1 points here
└─────────┘

After concat:
┌─────────┐
│ "Hello" │ ← s1 still points here (unchanged)
└─────────┘
┌──────────────┐
│ "Hello World"│ ← New object created in heap
└──────────────┘
```

---

### Q7: What is the difference between String, StringBuilder, and StringBuffer?

**Simple Explanation:**

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|---------------|--------------|
| **Mutable?** | ❌ No (Immutable) | ✅ Yes | ✅ Yes |
| **Thread-Safe?** | ✅ Yes | ❌ No | ✅ Yes (Synchronized) |
| **Performance** | Slow (creates new objects) | ⚡ Fast | Moderate |
| **Use When** | Few modifications | Single thread, many changes | Multiple threads, many changes |

**When to Use:**
- **String:** Fixed text like "Hello", email addresses
- **StringBuilder:** Building dynamic strings in loops (most common)
- **StringBuffer:** Multi-threaded environments

**Example:**
```java
// String - Inefficient for loops
String str = "";
for (int i = 0; i < 1000; i++) {
    str += i; // Creates 1000 new objects! ❌ BAD
}

// StringBuilder - Efficient (Single thread)
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i); // Modifies same object ✅ GOOD
}
String result = sb.toString();

// StringBuffer - Thread-safe (Multi-thread)
StringBuffer sbf = new StringBuffer();
sbf.append("Thread-safe");
```

---

### Q8: What is String Pool?

**Simple Explanation:**
String Pool is a special memory area where Java stores unique string literals to save memory.

**How It Works:**
When you create a string literal, Java:
1. Checks if it already exists in pool
2. If yes, reuse it
3. If no, create new one

**Example:**
```java
// String literals - stored in String Pool
String s1 = "Hello";
String s2 = "Hello";
String s3 = "Hello";

// All three point to SAME object in pool!
System.out.println(s1 == s2); // true
System.out.println(s1 == s3); // true

// new String() - creates object in Heap, NOT pool
String s4 = new String("Hello");
System.out.println(s1 == s4); // false (different objects)

// intern() - force add to pool
String s5 = new String("Hello").intern();
System.out.println(s1 == s5); // true (now in pool)
```

**Visual Memory:**
```
String Pool (Special Memory Area):
┌─────────┐
│ "Hello" │ ← s1, s2, s3 all point here
└─────────┘

Heap (Regular Memory):
┌─────────┐
│ "Hello" │ ← s4 points here (separate object)
└─────────┘
```

---

## 📦 Collections Questions

### Q9: Explain ArrayList vs LinkedList

**Simple Explanation:**

**ArrayList = Dynamic Array**
- Stores elements in continuous memory (like an array)
- Fast to read (by index)
- Slow to insert/delete in middle

**LinkedList = Chain of Nodes**
- Each element (node) points to next element
- Slow to read (must traverse)
- Fast to insert/delete anywhere

**Real-Life Analogy:**
- **ArrayList:** Books on a shelf - easy to grab book #5, hard to insert book in middle
- **LinkedList:** Chain link - easy to break and add link, hard to count to link #5

**Performance Comparison:**
```java
// ArrayList
List<String> arrayList = new ArrayList<>();
arrayList.add("A");           // O(1) - Fast
arrayList.get(5);             // O(1) - Very Fast ✅
arrayList.add(0, "First");    // O(n) - Slow ❌
arrayList.remove(0);          // O(n) - Slow ❌

// LinkedList
List<String> linkedList = new LinkedList<>();
linkedList.add("A");          // O(1) - Fast
linkedList.get(5);            // O(n) - Slow ❌
linkedList.add(0, "First");   // O(1) - Fast ✅
linkedList.remove(0);         // O(1) - Fast ✅
```

**When to Use:**
- **ArrayList:** You need to access elements by index frequently
- **LinkedList:** You need to add/remove elements frequently

---

### Q10: How does HashMap work internally?

**Simple Explanation:**
HashMap uses a technique called "Hashing" to store and retrieve data super fast (almost instant).

**Simple Process:**

1. **Put Operation:**
   ```
   map.put("John", 25)
   
   Step 1: Calculate hash of key "John" → 12345
   Step 2: Find bucket: 12345 % 16 = 5 (bucket number)
   Step 3: Store in bucket 5
   ```

2. **Get Operation:**
   ```
   map.get("John")
   
   Step 1: Calculate hash of "John" → 12345
   Step 2: Find bucket: 12345 % 16 = 5
   Step 3: Get value from bucket 5 → 25
   ```

**Key Concepts:**

**1. Buckets (Array):**
```
HashMap has 16 buckets initially (0 to 15)

Bucket Array:
[0] → null
[1] → null
[2] → ["Alice", 30]
[3] → null
[4] → null
[5] → ["John", 25]
...
```

**2. Collision:**
When two keys hash to same bucket:
```
"John" → bucket 5
"Emma" → bucket 5 (collision!)

Bucket 5 becomes a linked list:
["John", 25] → ["Emma", 28] → null
```

**3. Load Factor (0.75):**
When 75% full, double the size (16 → 32 → 64...)

**Example:**
```java
Map<String, Integer> map = new HashMap<>();

// Internal process
map.put("John", 25);
// 1. hash("John") → calculates number
// 2. bucket = hash % 16 → finds bucket
// 3. Stores in that bucket

map.get("John");
// 1. hash("John") → same hash as before
// 2. bucket = hash % 16 → goes to same bucket
// 3. Returns 25
```

---

### Q11: Why do we need to override equals() and hashCode() together?

**Simple Explanation:**
If you override one without the other, HashMap and HashSet won't work correctly!

**The Rule:**
**If two objects are equal (equals = true), they MUST have same hashCode**

**Why?**
HashMap uses hashCode to find the bucket, then uses equals to check equality.

**Example of Problem:**
```java
class Person {
    String name;
    int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // Only override equals (WRONG!)
    @Override
    public boolean equals(Object obj) {
        Person p = (Person) obj;
        return this.name.equals(p.name) && this.age == p.age;
    }
    
    // Didn't override hashCode - PROBLEM!
}

// Problem in action:
Person p1 = new Person("John", 25);
Person p2 = new Person("John", 25);

// equals says they're equal
System.out.println(p1.equals(p2)); // true ✅

// But HashMap treats them as different!
Map<Person, String> map = new HashMap<>();
map.put(p1, "Developer");
map.put(p2, "Manager"); // Should replace, but creates new entry!

System.out.println(map.size()); // 2 (WRONG! Should be 1) ❌
```

**Correct Implementation:**
```java
class Person {
    String name;
    int age;
    
    // Both equals AND hashCode
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return age == person.age && Objects.equals(name, person.name);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }
}

// Now it works correctly!
Person p1 = new Person("John", 25);
Person p2 = new Person("John", 25);

Map<Person, String> map = new HashMap<>();
map.put(p1, "Developer");
map.put(p2, "Manager"); // Correctly replaces!

System.out.println(map.size()); // 1 ✅ Correct!
```

---

### Q12: What is the difference between HashMap and ConcurrentHashMap?

**Simple Explanation:**

**HashMap = Single Thread Only**
- Not thread-safe
- If multiple threads modify together → Data corruption ❌
- Faster (no locking overhead)

**ConcurrentHashMap = Multi-Thread Safe**
- Thread-safe
- Multiple threads can modify safely ✅
- Uses segment locking (only locks part of map)
- Slightly slower but safe

**Real-Life Analogy:**
- **HashMap:** Single-person bathroom - fast but only one can use
- **ConcurrentHashMap:** Multi-stall bathroom - multiple people can use simultaneously

**Example:**
```java
// HashMap - Single thread
Map<String, Integer> hashMap = new HashMap<>();
hashMap.put("A", 1); // Safe in single thread

// ConcurrentHashMap - Multi thread
Map<String, Integer> concurrentMap = new ConcurrentHashMap<>();

// Multiple threads can safely do this:
Thread t1 = new Thread(() -> concurrentMap.put("A", 1));
Thread t2 = new Thread(() -> concurrentMap.put("B", 2));
Thread t3 = new Thread(() -> concurrentMap.put("C", 3));

t1.start();
t2.start();
t3.start();

// All threads work safely without corruption ✅
```

**When to Use:**
- **HashMap:** Single-threaded applications, local variables
- **ConcurrentHashMap:** Multi-threaded applications, shared data

---

### Q13: Explain Comparable vs Comparator

**Simple Explanation:**

**Comparable = Natural Ordering (Inside the class)**
- Define default sorting logic inside the class itself
- Implement `compareTo()` method
- Only ONE way to sort

**Comparator = Custom Ordering (Outside the class)**
- Define sorting logic outside the class
- Can have MULTIPLE different sorting ways
- More flexible

**Real-Life Analogy:**
- **Comparable:** Students naturally sorted by roll number (built-in)
- **Comparator:** You can sort students by name, age, marks (your choice)

**Example:**
```java
// Comparable - Natural ordering
class Student implements Comparable<Student> {
    String name;
    int age;
    int marks;
    
    public Student(String name, int age, int marks) {
        this.name = name;
        this.age = age;
        this.marks = marks;
    }
    
    // Natural ordering by age
    @Override
    public int compareTo(Student other) {
        return this.age - other.age;
    }
}

// Usage
List<Student> students = new ArrayList<>();
students.add(new Student("John", 25, 85));
students.add(new Student("Alice", 22, 90));
students.add(new Student("Bob", 28, 75));

Collections.sort(students); // Sorts by age (natural ordering)

// Comparator - Custom ordering
// Sort by name
Comparator<Student> nameComparator = new Comparator<Student>() {
    @Override
    public int compare(Student s1, Student s2) {
        return s1.name.compareTo(s2.name);
    }
};

// Sort by marks
Comparator<Student> marksComparator = new Comparator<Student>() {
    @Override
    public int compare(Student s1, Student s2) {
        return s2.marks - s1.marks; // Descending order
    }
};

// Usage
Collections.sort(students, nameComparator);  // Sort by name
Collections.sort(students, marksComparator); // Sort by marks

// Java 8 way (cleaner)
students.sort(Comparator.comparing(s -> s.name));
students.sort(Comparator.comparingInt(s -> s.marks).reversed());
```

---

## ⚠️ Exception Questions

### Q14: What is the difference between Checked and Unchecked Exceptions?

**Simple Explanation:**

**Checked Exceptions = Compiler Forces You to Handle**
- Must handle with try-catch OR declare with throws
- Compiler checks at compile-time
- Usually recoverable errors
- Examples: IOException, SQLException, FileNotFoundException

**Unchecked Exceptions = Your Choice to Handle**
- Not forced to handle
- Happens at runtime
- Usually programming errors
- Examples: NullPointerException, ArrayIndexOutOfBoundsException

**Real-Life Analogy:**
- **Checked:** Before boarding flight, you MUST show ticket (forced)
- **Unchecked:** Eating food is your choice, nobody forces you

**Example:**
```java
// Checked Exception - MUST handle
public void readFile() {
    // ❌ Compiler error if not handled
    FileReader reader = new FileReader("file.txt");
    
    // ✅ Must use try-catch
    try {
        FileReader reader = new FileReader("file.txt");
    } catch (FileNotFoundException e) {
        System.out.println("File not found");
    }
    
    // ✅ OR declare throws
    public void readFile() throws FileNotFoundException {
        FileReader reader = new FileReader("file.txt");
    }
}

// Unchecked Exception - Optional to handle
public int divide(int a, int b) {
    return a / b; // Can throw ArithmeticException
    // No need to handle, but good practice to check
}

// Better approach:
public int divide(int a, int b) {
    if (b == 0) {
        throw new IllegalArgumentException("Cannot divide by zero");
    }
    return a / b;
}
```

---

### Q15: What is try-with-resources?

**Simple Explanation:**
Try-with-resources automatically closes resources (files, connections) even if error occurs. No need to write finally block!

**Before Java 7 (Old Way):**
```java
// ❌ OLD - Manual closing with finally
BufferedReader reader = null;
try {
    reader = new BufferedReader(new FileReader("file.txt"));
    String line = reader.readLine();
} catch (IOException e) {
    e.printStackTrace();
} finally {
    // Must manually close
    if (reader != null) {
        try {
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**After Java 7 (New Way):**
```java
// ✅ NEW - Auto-closing
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line = reader.readLine();
} catch (IOException e) {
    e.printStackTrace();
}
// reader automatically closed! No finally needed

// Multiple resources
try (FileReader fr = new FileReader("input.txt");
     BufferedReader br = new BufferedReader(fr);
     FileWriter fw = new FileWriter("output.txt")) {
    
    String line = br.readLine();
    fw.write(line);
    
} catch (IOException e) {
    e.printStackTrace();
}
// All resources automatically closed!
```

**Benefits:**
- Cleaner code
- No resource leaks
- Automatic closing even if exception occurs
- Less boilerplate code

---

## 🧵 Multithreading Questions

### Q16: What is the difference between Process and Thread?

**Simple Explanation:**

**Process = Running Program**
- Independent execution unit
- Has its own memory space
- Heavy (takes more resources)
- Example: Chrome browser, Word document

**Thread = Lightweight Process**
- Part of a process
- Shares memory with other threads
- Light (takes fewer resources)
- Example: Multiple tabs in Chrome

**Real-Life Analogy:**
- **Process:** Separate houses - each has its own kitchen, bedroom
- **Thread:** Roommates in same house - share kitchen, bedroom

**Visual:**
```
Process (Chrome Browser)
├── Thread 1 (Tab 1 - Gmail)
├── Thread 2 (Tab 2 - YouTube)
├── Thread 3 (Tab 3 - Facebook)
└── Thread 4 (Download Manager)

All threads share Chrome's memory!
```

**Comparison:**
```java
| Feature | Process | Thread |
|---------|---------|--------|
| **Memory** | Separate | Shared |
| **Communication** | Difficult (IPC needed) | Easy (shared memory) |
| **Creation Time** | Slow | Fast |
| **Context Switching** | Expensive | Cheap |
| **Example** | Multiple Java programs | Multiple threads in one program |
```

---

### Q17: How to create a Thread in Java?

**Simple Explanation:**
There are 3 main ways to create threads in Java.

**Method 1: Extend Thread Class**
```java
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread running: " + Thread.currentThread().getName());
    }
}

// Usage
MyThread thread = new MyThread();
thread.start(); // Don't call run() directly!
```

**Method 2: Implement Runnable Interface (Better!)**
```java
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Runnable running: " + Thread.currentThread().getName());
    }
}

// Usage
Thread thread = new Thread(new MyRunnable());
thread.start();
```

**Method 3: Lambda Expression (Java 8+, Best for simple tasks)**
```java
// Super simple!
Thread thread = new Thread(() -> {
    System.out.println("Lambda thread: " + Thread.currentThread().getName());
});
thread.start();

// One-liner
new Thread(() -> System.out.println("Quick task")).start();
```

**Why Runnable is Better than Thread?**
1. Can implement multiple interfaces
2. Separation of task from thread
3. Can reuse Runnable with different threads
4. More flexible

**Complete Example:**
```java
public class ThreadDemo {
    public static void main(String[] args) {
        // Method 1: Thread class
        Thread t1 = new MyThread();
        
        // Method 2: Runnable
        Thread t2 = new Thread(new MyRunnable());
        
        // Method 3: Lambda
        Thread t3 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Count: " + i);
            }
        });
        
        t1.start();
        t2.start();
        t3.start();
    }
}
```

---

### Q18: Explain synchronized keyword

**Simple Explanation:**
`synchronized` prevents multiple threads from accessing the same resource simultaneously. It's like a lock on a door - only one person can enter at a time.

**Problem Without Synchronized:**
```java
class Counter {
    private int count = 0;
    
    public void increment() {
        count++; // Not thread-safe!
    }
    
    public int getCount() {
        return count;
    }
}

// Problem:
Counter counter = new Counter();

Thread t1 = new Thread(() -> {
    for (int i = 0; i < 1000; i++) {
        counter.increment();
    }
});

Thread t2 = new Thread(() -> {
    for (int i = 0; i < 1000; i++) {
        counter.increment();
    }
});

t1.start();
t2.start();
t1.join();
t2.join();

System.out.println(counter.getCount()); // Should be 2000, but might be 1850! ❌
```

**Solution With Synchronized:**
```java
class Counter {
    private int count = 0;
    
    // Method-level synchronization
    public synchronized void increment() {
        count++; // Now thread-safe! ✅
    }
    
    public synchronized int getCount() {
        return count;
    }
}

// Now it works correctly!
System.out.println(counter.getCount()); // Always 2000 ✅

// Block-level synchronization (more efficient)
class Counter {
    private int count = 0;
    private Object lock = new Object();
    
    public void increment() {
        synchronized(lock) {
            count++; // Only this part is locked
        }
    }
}
```

**Real-Life Analogy:**
Bathroom with a lock:
- Without synchronized: Multiple people try to use bathroom together (chaos!)
- With synchronized: Lock ensures only one person at a time (orderly)

---

### Q19: What is deadlock? How to prevent it?

**Simple Explanation:**
Deadlock = Two or more threads waiting for each other forever, none can proceed.

**Real-Life Analogy:**
Two people at a narrow bridge:
- Person A waits for Person B to move
- Person B waits for Person A to move
- Nobody moves! (Deadlock)

**Code Example of Deadlock:**
```java
class DeadlockExample {
    private final Object lock1 = new Object();
    private final Object lock2 = new Object();
    
    public void method1() {
        synchronized (lock1) { // Thread 1 gets lock1
            System.out.println("Thread 1: Holding lock1...");
            
            try { Thread.sleep(10); } catch (Exception e) {}
            
            synchronized (lock2) { // Thread 1 waits for lock2 (held by Thread 2)
                System.out.println("Thread 1: Got lock2!");
            }
        }
    }
    
    public void method2() {
        synchronized (lock2) { // Thread 2 gets lock2
            System.out.println("Thread 2: Holding lock2...");
            
            try { Thread.sleep(10); } catch (Exception e) {}
            
            synchronized (lock1) { // Thread 2 waits for lock1 (held by Thread 1)
                System.out.println("Thread 2: Got lock1!");
            }
        }
    }
}

// Deadlock occurs:
// Thread 1: Has lock1, waiting for lock2
// Thread 2: Has lock2, waiting for lock1
// Both wait forever! ☠️
```

**How to Prevent Deadlock:**

**1. Lock Ordering (Best Solution)**
```java
// Always acquire locks in same order
public void method1() {
    synchronized (lock1) {
        synchronized (lock2) {
            // Work
        }
    }
}

public void method2() {
    synchronized (lock1) { // Same order!
        synchronized (lock2) {
            // Work
        }
    }
}
```

**2. Trylock with Timeout**
```java
Lock lock1 = new ReentrantLock();
Lock lock2 = new ReentrantLock();

public void method1() {
    try {
        if (lock1.tryLock(50, TimeUnit.MILLISECONDS)) {
            try {
                if (lock2.tryLock(50, TimeUnit.MILLISECONDS)) {
                    try {
                        // Work
                    } finally {
                        lock2.unlock();
                    }
                }
            } finally {
                lock1.unlock();
            }
        }
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}
```

**3. Avoid Nested Locks**
```java
// Don't do this:
synchronized(lock1) {
    synchronized(lock2) {
        // Risky!
    }
}

// Do this instead:
synchronized(lock1) {
    // Work
}
// Then separately:
synchronized(lock2) {
    // Work
}
```

---

## ☕ Java 8+ Questions

### Q20: What is a Lambda Expression?

**Simple Explanation:**
Lambda = Short way to write a function (method) without a name.

**Before Lambda (Verbose):**
```java
// Old way - Too much code for simple task!
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello");
    }
};
```

**With Lambda (Concise):**
```java
// New way - Clean and simple!
Runnable r = () -> System.out.println("Hello");
```

**Syntax:**
```
(parameters) -> expression or { statements }
```

**Examples:**
```java
// No parameters
() -> System.out.println("Hello");

// One parameter (parentheses optional)
x -> x * x
(x) -> x * x // Same thing

// Multiple parameters
(a, b) -> a + b

// Multiple statements (need braces)
(a, b) -> {
    int sum = a + b;
    System.out.println("Sum: " + sum);
    return sum;
}

// Real usage
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

// Without lambda
numbers.forEach(new Consumer<Integer>() {
    @Override
    public void accept(Integer n) {
        System.out.println(n);
    }
});

// With lambda
numbers.forEach(n -> System.out.println(n));

// Even shorter
numbers.forEach(System.out::println);
```

---

### Q21: Explain Stream API with examples

**Simple Explanation:**
Stream = Pipeline to process collections (list, set) in a declarative way.

Like an assembly line: data goes through multiple operations.

**Benefits:**
- Clean, readable code
- Lazy evaluation (efficient)
- Easy parallelization
- No loops needed!

**Common Operations:**

**1. Filter - Select elements**
```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Get even numbers
List<Integer> evenNumbers = numbers.stream()
    .filter(n -> n % 2 == 0) // Keep only even
    .collect(Collectors.toList());

System.out.println(evenNumbers); // [2, 4, 6, 8, 10]
```

**2. Map - Transform elements**
```java
// Square each number
List<Integer> squares = numbers.stream()
    .map(n -> n * n) // Transform
    .collect(Collectors.toList());

System.out.println(squares); // [1, 4, 9, 16, 25...]
```

**3. Reduce - Combine to single result**
```java
// Sum all numbers
int sum = numbers.stream()
    .reduce(0, (a, b) -> a + b);

System.out.println(sum); // 55

// Or simpler:
int sum = numbers.stream().sum();
```

**4. Chaining Operations**
```java
// Complex example: Get sum of squares of even numbers
int result = numbers.stream()
    .filter(n -> n % 2 == 0)  // Step 1: Keep even
    .map(n -> n * n)           // Step 2: Square them
    .reduce(0, (a, b) -> a + b); // Step 3: Sum

System.out.println(result); // 220 (4+16+36+64+100)
```

**Real-World Example:**
```java
class Employee {
    String name;
    int salary;
    String department;
    
    // Constructor, getters...
}

List<Employee> employees = Arrays.asList(
    new Employee("John", 50000, "IT"),
    new Employee("Alice", 60000, "HR"),
    new Employee("Bob", 45000, "IT"),
    new Employee("Charlie", 70000, "Finance")
);

// Find average salary of IT department
double avgSalary = employees.stream()
    .filter(e -> e.department.equals("IT"))
    .mapToInt(e -> e.salary)
    .average()
    .orElse(0);

System.out.println("Average IT Salary: " + avgSalary); // 47500

// Get names of employees earning > 50000
List<String> highEarners = employees.stream()
    .filter(e -> e.salary > 50000)
    .map(e -> e.name)
    .collect(Collectors.toList());

System.out.println(highEarners); // [Alice, Charlie]
```

---

### Q22: What is Optional class? Why do we need it?

**Simple Explanation:**
Optional is a container that may or may not contain a value. It helps avoid NullPointerException!

**Problem Without Optional:**
```java
// Old way - Risky!
public String getUserEmail(int userId) {
    User user = findUser(userId);
    return user.getEmail(); // ❌ NullPointerException if user is null!
}

// Have to do null checks everywhere
if (user != null) {
    String email = user.getEmail();
    if (email != null) {
        System.out.println(email.toUpperCase());
    }
}
```

**With Optional:**
```java
// New way - Safe!
public Optional<String> getUserEmail(int userId) {
    User user = findUser(userId);
    return Optional.ofNullable(user)
        .map(User::getEmail);
}

// Usage - No null checks needed!
getUserEmail(123)
    .map(String::toUpperCase)
    .ifPresent(System.out::println);
```

**Common Methods:**

**1. Creating Optional**
```java
// Empty optional
Optional<String> empty = Optional.empty();

// With value
Optional<String> optional = Optional.of("Hello"); // Throws exception if null

// Nullable value (safer)
Optional<String> optional = Optional.ofNullable(getValue()); // Can be null
```

**2. Checking Value**
```java
Optional<String> optional = Optional.of("Hello");

// Check if present
if (optional.isPresent()) {
    System.out.println(optional.get());
}

// Better way
optional.ifPresent(value -> System.out.println(value));

// Even better
optional.ifPresent(System.out::println);
```

**3. Default Values**
```java
Optional<String> optional = Optional.empty();

// Get value or default
String value = optional.orElse("Default"); // Returns "Default"

// Get value or throw exception
String value = optional.orElseThrow(() -> new RuntimeException("Not found"));

// Get value or compute default
String value = optional.orElseGet(() -> computeDefaultValue());
```

**4. Transformation**
```java
Optional<String> optional = Optional.of("hello");

// Transform value
Optional<String> upper = optional.map(String::toUpperCase);
System.out.println(upper.get()); // HELLO

// Flatmap for nested optionals
Optional<String> email = Optional.ofNullable(user)
    .flatMap(User::getEmail); // getEmail() returns Optional<String>
```

**Real Example:**
```java
class User {
    private String name;
    private Optional<String> email; // Email might not exist
    
    public Optional<String> getEmail() {
        return email;
    }
}

// Usage
User user = findUser(123);

// Old way (ugly)
if (user != null) {
    Optional<String> email = user.getEmail();
    if (email.isPresent()) {
        System.out.println(email.get());
    } else {
        System.out.println("No email");
    }
}

// New way (clean)
Optional.ofNullable(user)
    .flatMap(User::getEmail)
    .ifPresentOrElse(
        email -> System.out.println("Email: " + email),
        () -> System.out.println("No email")
    );
```

---

## 💾 Memory Questions

### Q23: Explain Java Memory Model (Heap vs Stack)

**Simple Explanation:**

**Stack Memory:**
- Stores local variables and method calls
- Fast access (LIFO - Last In First Out)
- Small in size
- Automatic cleanup when method ends
- Each thread has its own stack

**Heap Memory:**
- Stores objects and arrays
- Slower access than stack
- Large in size
- Garbage collector cleans it
- Shared by all threads

**Visual Example:**
```java
public class MemoryDemo {
    public static void main(String[] args) {
        int number = 10;        // Stack
        String name = "John";   // "John" in heap, reference in stack
        
        Person person = new Person("Alice"); // Object in heap, reference in stack
    }
}

/*
Stack:
┌─────────────────┐
│ main() frame    │
│ number = 10     │ ← Primitive in stack
│ name → [ref]    │ ← Reference in stack
│ person → [ref]  │ ← Reference in stack
└─────────────────┘

Heap:
┌──────────────────────┐
│ "John" object        │ ← String object
│ "Alice" object       │ ← String object
│ Person object        │ ← Person object
│ { name: "Alice" }    │
└──────────────────────┘
*/
```

**Key Differences:**
```java
public void example() {
    // Stack variables
    int age = 25;           // Stack
    double salary = 50000;   // Stack
    
    // Heap objects
    Employee emp = new Employee(); // Object in heap
    List<String> names = new ArrayList<>(); // Object in heap
    
    // When method ends:
    // - Stack variables (age, salary, emp reference) removed
    // - Heap objects (Employee, ArrayList) remain until GC
}
```

---

### Q24: What is Garbage Collection?

**Simple Explanation:**
Garbage Collection (GC) = Automatic memory cleanup. Java automatically removes unused objects from memory.

**How It Works:**

**1. Object Becomes Garbage When:**
- No reference pointing to it
- Reference becomes null
- Reference goes out of scope

**Example:**
```java
public void createObjects() {
    // Object 1
    Employee emp1 = new Employee("John");
    
    // Object 2
    Employee emp2 = new Employee("Alice");
    
    // emp1 becomes garbage (no reference anymore)
    emp1 = null;
    
    // emp2 becomes garbage when method ends
} // Method ends, emp2 out of scope

// Both objects eligible for garbage collection
```

**Ways Object Becomes Garbage:**

**1. Nullifying Reference**
```java
Employee emp = new Employee();
emp = null; // Object eligible for GC
```

**2. Reassigning Reference**
```java
Employee emp = new Employee("John");
emp = new Employee("Alice"); // "John" object eligible for GC
```

**3. Island of Isolation**
```java
class Node {
    Node next;
}

Node n1 = new Node();
Node n2 = new Node();
n1.next = n2;
n2.next = n1;

n1 = null;
n2 = null;
// Both objects unreachable → both eligible for GC
```

**How to Request GC:**
```java
// Suggest GC (not guaranteed to run immediately)
System.gc();

// Or
Runtime.getRuntime().gc();

// Note: GC runs automatically, don't call manually in production!
```

**finalize() Method:**
```java
class MyClass {
    @Override
    protected void finalize() throws Throwable {
        // Called before GC destroys object
        System.out.println("Cleaning up...");
    }
}
```

---

## 🎯 Tricky Questions

### Q25: Why is main() method static?

**Simple Explanation:**
`main()` is static because Java needs to call it **without creating an object**.

**Reason:**
- When program starts, no objects exist yet
- `static` methods can be called directly with class name
- JVM calls: `ClassName.main()` without creating object

**Example:**
```java
public class Test {
    // If main was not static (hypothetical):
    public void main(String[] args) {
        // JVM would need to do:
        // Test obj = new Test(); // Can't create object automatically!
        // obj.main(args);
    }
    
    // Correct way - static main:
    public static void main(String[] args) {
        // JVM can call directly:
        // Test.main(args); ✅
        System.out.println("Program started");
    }
}
```

---

### Q26: Can we overload main() method?

**Simple Explanation:**
Yes! We can overload `main()` but JVM only calls the standard signature.

**Example:**
```java
public class MainOverload {
    // Standard main - JVM calls this
    public static void main(String[] args) {
        System.out.println("Standard main");
        
        // We can call overloaded versions
        main(10);
        main("Hello");
    }
    
    // Overloaded main - int parameter
    public static void main(int x) {
        System.out.println("Main with int: " + x);
    }
    
    // Overloaded main - String parameter
    public static void main(String x) {
        System.out.println("Main with String: " + x);
    }
}

// Output:
// Standard main
// Main with int: 10
// Main with String: Hello
```

---

### Q27: What happens if we don't provide main() method?

**Simple Explanation:**
Program compiles but gives runtime error when you try to run it.

**Example:**
```java
public class NoMain {
    public void display() {
        System.out.println("Hello");
    }
}

// Compile: ✅ javac NoMain.java (Success)
// Run: ❌ java NoMain
// Error: Main method not found in class NoMain
```

---

### Q28: Can we have multiple public classes in single file?

**Simple Explanation:**
**No!** Only ONE public class per file, and file name must match that class.

**Example:**
```java
// ❌ WRONG - Compilation error
public class Class1 {
}

public class Class2 {
}

// ✅ CORRECT - Only one public class
public class MyClass {
}

class Helper1 {
}

class Helper2 {
}

// File name must be: MyClass.java
```

---

### Q29: What is the output?

```java
String s1 = "Hello";
String s2 = "Hello";
String s3 = new String("Hello");

System.out.println(s1 == s2);        // ?
System.out.println(s1 == s3);        // ?
System.out.println(s1.equals(s3));   // ?
```

**Answer:**
```java
System.out.println(s1 == s2);        // true  (same object in pool)
System.out.println(s1 == s3);        // false (different objects)
System.out.println(s1.equals(s3));   // true  (same content)
```

**Explanation:**
- `s1` and `s2` point to same object in String Pool
- `s3` is a new object in Heap (not pool)
- `==` compares references (memory addresses)
- `equals()` compares content

---

### Q30: What will be printed?

```java
Integer i1 = 127;
Integer i2 = 127;
System.out.println(i1 == i2); // ?

Integer i3 = 128;
Integer i4 = 128;
System.out.println(i3 == i4); // ?
```

**Answer:**
```java
System.out.println(i1 == i2); // true
System.out.println(i3 == i4); // false
```

**Explanation:**
- Java caches Integer objects from -128 to 127
- Values in this range reuse same object (like String pool)
- Outside this range, new objects are created

**Lesson:** Always use `.equals()` for Integer comparison!

---

## 🎓 Final Tips for Interviews

### 1. **Think Out Loud**
- Explain your thinking process
- Don't just give answers, explain why

### 2. **Use Real Examples**
- Relate concepts to real-world scenarios
- Makes you sound experienced

### 3. **Ask Clarifying Questions**
- Shows you think before coding
- "Should I handle null values?"
- "What should happen if input is invalid?"

### 4. **Know Trade-offs**
- ArrayList vs LinkedList
- HashMap vs TreeMap
- When to use what and why

### 5. **Be Honest**
- If you don't know, say "I don't know, but I can learn"
- Don't make up answers

---

## 🚀 Practice Makes Perfect!

✅ Understand concepts, don't memorize  
✅ Write code, don't just read  
✅ Solve coding problems daily  
✅ Review these questions regularly  
✅ Build real projects  

**Good Luck! 🎯**

