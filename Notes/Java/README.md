# Java Full Notes

Source: [JAVAFullNOTES.pdf](./JAVAFullNOTES.pdf)

> Complete Java notes from basics to advanced — interview-ready, organized by topic.

## Table of Contents

1. [Introduction to Java](#introduction-to-java)
2. [Java Basics and Variables](#java-basics-and-variables)
3. [Operators](#operators)
4. [Control Statements](#control-statements)
5. [OOPs in Java](#oops-in-java)
6. [Classes and Objects](#classes-and-objects)
7. [Inheritance](#inheritance)
8. [Polymorphism](#polymorphism)
9. [Abstraction](#abstraction)
10. [Encapsulation](#encapsulation)
11. [Constructors](#constructors)
12. [This Keyword](#this-keyword)
13. [Static Keyword](#static-keyword)
14. [Exception Handling](#exception-handling)
15. [String Handling](#string-handling)
16. [Collections Framework](#collections-framework)
17. [Multithreading](#multithreading)
18. [File Handling](#file-handling)
19. [Java 8+ Features](#java-8-features)
20. [Interview Questions](#interview-questions)
21. [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
22. [Practice Questions](#practice-questions)
23. [Programs and Practice](#programs-and-practice)
24. [Tips and Best Practices](#tips-and-best-practices)

---

## Introduction to Java

**Java** is a high-level, class-based, object-oriented programming language developed by Sun Microsystems (now Oracle).

### History

| Year | Event |
|------|-------|
| 1991 | James Gosling, Patrick Naughton, Mike Sheridan start Green Project |
| 1995 | Java officially released |
| 2009 | Oracle acquires Sun Microsystems |
| Today | Used for web, mobile, enterprise, desktop, games |

### Key Features

| Feature | Description |
|---------|-------------|
| Platform Independent | Write Once, Run Anywhere (WORA) via JVM |
| Simple | Clean syntax, no pointers, no operator overloading |
| Object-Oriented | Classes, objects, inheritance, polymorphism, encapsulation, abstraction |
| Secure | Bytecode verifier, security manager, no explicit pointers |
| Robust | Strong memory management, exception handling, garbage collection |
| High Performance | JIT compiler |
| Multithreaded | Concurrent task execution |

### JVM — The Heart of Java

```
Source Code (.java) → Compiler → Bytecode (.class) → JVM → Machine Code
```

JVM (Java Virtual Machine) is an abstract machine enabling bytecode to run on any platform.

### Hello World

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

### Applications

Web, Mobile, Enterprise, Desktop, Games, Cloud, Big Data

> **Write Once, Run Anywhere** — that's the power of Java.

---

## Java Basics and Variables

### Structure of a Java Program

```java
// Comments
package mypack;           // optional
import java.util.*;       // optional

public class Hello {       // class definition
    public static void main(String[] args) {  // entry point
        System.out.println("Hello, Java!");
    }
}
```

### Tokens in Java

| Token | Examples |
|-------|----------|
| Keywords | `class`, `public`, `static`, `void`, `int`, `if`, `for` |
| Identifiers | `Hello`, `main`, `age` (user-defined names) |
| Literals | `10`, `3.14`, `'a'`, `"Hello"`, `true` |
| Operators | `+`, `-`, `*`, `/`, `=`, `>`, `&&` |
| Separators | `()`, `{}`, `[]`, `;`, `.` |

### Data Types

**Primitive Types**

| Type | Size | Default |
|------|------|---------|
| `byte` | 1 byte | 0 |
| `short` | 2 bytes | 0 |
| `int` | 4 bytes | 0 |
| `long` | 8 bytes | 0L |
| `float` | 4 bytes | 0.0f |
| `double` | 8 bytes | 0.0d |
| `char` | 2 bytes | `'\u0000'` |
| `boolean` | 1 bit | `false` |

**Non-Primitive:** `String`, `Array`, `Class`, `Interface`, `Enum`

### Variables

A variable is a container that stores data.

```java
int age = 20;
double salary = 55000.75;
char grade = 'A';
boolean isJavaFun = true;
String name = "Alice";
```

**Rules:** Start with letter/`$`/`_`, case-sensitive, cannot be keyword, no spaces.

### Type Conversion

| Type | Direction | Example |
|------|-----------|---------|
| Widening (Implicit) | smaller → larger | `int` → `long` → `float` → `double` |
| Narrowing (Explicit) | larger → smaller | `int a = 100; byte b = (byte) a;` |

### Comments

```java
// Single-line comment

/*
 * Multi-line comment
 */

/** Documentation comment (Javadoc) */
```

### Key Rules

- Java is **case-sensitive** (`class` ≠ `Class`)
- `main()` is the program entry point
- Every statement ends with `;`
- Code is compiled then executed by JVM

---

## Operators

Operators perform operations on operands.

### Arithmetic Operators

| Operator | Example (a=10, b=3) | Result |
|----------|---------------------|--------|
| `+` | `a + b` | 13 |
| `-` | `a - b` | 7 |
| `*` | `a * b` | 30 |
| `/` | `a / b` | 3 |
| `%` | `a % b` | 1 |
| `++` | `a++` / `++a` | 11 |
| `--` | `a--` / `--a` | 9 |

### Relational Operators

Return `boolean`: `==`, `!=`, `>`, `<`, `>=`, `<=`

### Logical Operators

| Operator | Description |
|----------|-------------|
| `&&` | AND — true if both true |
| `\|\|` | OR — true if any true |
| `!` | NOT — reverses boolean |

### Assignment Operators

`=`, `+=`, `-=`, `*=`, `/=`, `%=`

### Bitwise Operators

`&`, `|`, `^`, `~`, `<<`, `>>`, `>>>`

### Unary Operators

`+`, `-`, `++`, `--`, `!`, `~`

### Ternary Operator

```java
int max = (a > b) ? a : b;  // condition ? trueVal : falseVal
```

---

## Control Statements

Control the flow of program execution.

### Selection Statements

**if-else**

```java
if (marks >= 90)
    System.out.println("A Grade");
else if (marks >= 75)
    System.out.println("B Grade");
else
    System.out.println("C Grade");
```

**switch**

```java
switch (day) {
    case 1: System.out.println("Mon"); break;
    case 2: System.out.println("Tue"); break;
    default: System.out.println("Other");
}
```

### Iteration Statements (Loops)

| Loop | Use When |
|------|----------|
| `while` | Iterations unknown in advance |
| `do-while` | Execute at least once |
| `for` | Iterations known in advance |
| `for-each` | Traverse collections/arrays |

```java
for (int i = 1; i <= 5; i++)
    System.out.println(i);
```

### Jump Statements

| Statement | Purpose |
|-----------|---------|
| `break` | Exit loop/switch immediately |
| `continue` | Skip current iteration |
| `return` | Exit method, optionally return value |

---

## OOPs in Java

**OOP** (Object-Oriented Programming) models real-world entities as objects with data and behavior.

### Four Pillars

| Pillar | Description |
|--------|-------------|
| **Encapsulation** | Bind data + methods; hide internal details |
| **Abstraction** | Show only essential features; hide implementation |
| **Inheritance** | Child class acquires parent properties |
| **Polymorphism** | One interface, many forms |

### Class vs Object

| Class | Object |
|-------|--------|
| Blueprint / template | Real-world instance |
| Declared with `class` | Created with `new` |
| No memory allocated | Memory allocated at runtime |

### Advantages

- Reusable, modular code
- Easy debugging and maintenance
- Real-world modeling
- Secure programs

> Everything in Java is an object (except primitives).

---

## Classes and Objects

### Class Declaration

```java
class Student {
    int id;           // data member
    String name;

    void display() {  // method
        System.out.println(id + " " + name);
    }
}
```

### Creating Objects

```java
Student s1 = new Student();
s1.id = 101;
s1.name = "Alice";
s1.display();
```

### Key Points

- Class = blueprint, Object = instance
- Multiple objects from one class
- Each object has its own copy of data members

---

## Inheritance

**Inheritance** allows a child class to acquire fields and methods of a parent class (`is-a` relationship).

```java
class Animal {
    void eat() { System.out.println("Eating..."); }
}

class Dog extends Animal {
    void bark() { System.out.println("Barking..."); }
}
```

### Types of Inheritance

| Type | Description |
|------|-------------|
| Single | One parent, one child |
| Multilevel | Chain: A → B → C |
| Hierarchical | One parent, multiple children |
| Hybrid | Combination of above |

### Rules

- Use `extends` to inherit a class
- Java does **not** support multiple inheritance with classes
- Multiple inheritance achieved via **interfaces**
- `super` accesses parent class members
- Private members are not inherited

---

## Polymorphism

**Polymorphism** = "many forms" — same method behaves differently in different situations.

### Compile-Time (Method Overloading)

Same method name, different parameters (number, type, or order).

```java
int add(int a, int b) { return a + b; }
int add(int a, int b, int c) { return a + b + c; }
double add(double a, double b) { return a + b; }
```

### Runtime (Method Overriding)

Child class provides its own implementation of parent method.

```java
class Animal {
    void sound() { System.out.println("Animal sound"); }
}
class Dog extends Animal {
    @Override
    void sound() { System.out.println("Dog barks"); }
}

Animal a = new Dog();
a.sound();  // "Dog barks" — resolved at runtime
```

### Multiple Inheritance via Interface

```java
interface A { void showA(); }
interface B { void showB(); }

class C implements A, B {
    public void showA() { System.out.println("A"); }
    public void showB() { System.out.println("B"); }
}
```

---

## Abstraction

**Abstraction** hides implementation details and shows only essential functionality.

### Ways to Achieve

**1. Abstract Class**

```java
abstract class Shape {
    abstract void draw();          // no body
    void color() {                 // concrete method
        System.out.println("Colored");
    }
}

class Circle extends Shape {
    void draw() { System.out.println("Drawing circle"); }
}
```

**2. Interface**

```java
interface Vehicle {
    void start();
    void stop();
}

class Car implements Vehicle {
    public void start() { System.out.println("Car started"); }
    public void stop()  { System.out.println("Car stopped"); }
}
```

| Abstract Class | Interface |
|----------------|-----------|
| 0–100% abstraction | 100% abstraction (before Java 8) |
| Can have constructors | No constructors |
| Single inheritance | Multiple inheritance |
| `extends` | `implements` |

---

## Encapsulation

**Encapsulation** binds data and methods into a single unit, restricting direct data access.

### How to Achieve

1. Declare variables as **private**
2. Provide public **getter** methods
3. Provide public **setter** methods (with validation)

```java
class Student {
    private int rollNo;
    private String name;

    public int getRollNo() { return rollNo; }
    public void setRollNo(int rollNo) {
        if (rollNo > 0) this.rollNo = rollNo;
    }

    public String getName() { return name; }
    public void setName(String name) {
        if (!name.isEmpty()) this.name = name;
    }
}
```

> Never expose data directly — use getters/setters for control and security.

---

## Constructors

A **constructor** initializes objects when they are created. Called automatically — no return type.

### Types

**Default Constructor** — Provided by Java if none is written.

**Parameterized Constructor** — Accepts arguments.

**Constructor Overloading** — Multiple constructors with different parameters.

```java
class Student {
    int id;
    String name;

    Student() {                    // default
        id = 0;
        name = "Unknown";
    }

    Student(int id, String name) { // parameterized
        this.id = id;
        this.name = name;
    }
}
```

### Key Points

- Name = class name
- No return type (not even `void`)
- Called once at object creation
- Can be overloaded
- Not inherited
- If any constructor is written, default is not provided

---

## This Keyword

`this` refers to the **current object**.

### Uses

| Use | Example |
|-----|---------|
| Distinguish instance vs parameter | `this.id = id;` |
| Call current class constructor | `this(0, "Unknown");` |
| Pass current object as argument | `display(this);` |
| Return current object | `return this;` (method chaining) |

```java
class Student {
    int id;
    Student(int id) {
        this.id = id;  // this.id = instance variable
    }
    Student setId(int id) {
        this.id = id;
        return this;   // chaining: s.setId(101).show();
    }
}
```

---

## Static Keyword

`static` members belong to the **class**, not individual objects — shared by all instances.

### Static Variable

```java
class Counter {
    static int count = 0;
    Counter() { count++; }
}
// Counter.count shared by all objects
```

### Static Method

Called without creating an object. Can only access static members directly.

```java
class MathUtil {
    static int add(int a, int b) { return a + b; }
}
int sum = MathUtil.add(10, 20);
```

### Static Block

Runs once when class is loaded.

```java
class Demo {
    static { System.out.println("Static block executed"); }
}
```

### Rules

- `main()` is static — JVM calls it without creating an object
- Static methods cannot use `this` or `super`
- Static members loaded when class loads

---

## Exception Handling

An **exception** is an event that disrupts normal program flow. Handling it maintains program stability.

### Types

| Type | When Checked | Examples |
|------|--------------|----------|
| Checked | Compile time | `IOException`, `SQLException` |
| Unchecked | Runtime | `NullPointerException`, `ArithmeticException` |

### try-catch-finally

```java
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Divide by zero: " + e.getMessage());
} finally {
    System.out.println("Always executed");
}
```

### throw and throws

```java
void check(int age) throws IOException {
    if (age < 0) throw new IllegalArgumentException("Invalid age");
}
```

### Best Practices

- Handle specific exceptions first
- Never ignore exceptions
- Use meaningful error messages
- Use try-with-resources for I/O

---

## String Handling

### Key Points

- Strings are **immutable**
- Literals stored in **String Pool**
- Use `equals()` for content comparison (not `==`)
- `StringBuilder` for frequent modifications

### Common Methods

```java
String s = "Hello World";
s.length();                    // 11
s.charAt(1);                   // 'e'
s.substring(0, 5);             // "Hello"
s.equals("Hello World");       // true
s.contains("World");           // true
s.toUpperCase();               // "HELLO WORLD"
s.concat("!");                 // "Hello World!"
```

### String Comparison

```java
String a = "Hello";
String c = new String("Hello");
a == c;         // false (different references)
a.equals(c);  // true (same content)
```

---

## Collections Framework

Unified architecture in `java.util` for storing and manipulating groups of objects.

### Hierarchy

```
Collection
├── List (ordered, duplicates)     → ArrayList, LinkedList, Vector
├── Set (no duplicates)            → HashSet, LinkedHashSet, TreeSet
└── Queue (FIFO)                   → PriorityQueue, ArrayDeque

Map (key-value, separate)          → HashMap, LinkedHashMap, TreeMap, Hashtable
```

### When to Use

| Interface | Use When |
|-----------|----------|
| `ArrayList` | Fast random access, more reads |
| `LinkedList` | Frequent insertions/deletions |
| `HashSet` | Unique elements, no order needed |
| `TreeSet` | Sorted unique elements |
| `HashMap` | Fast key-value access |
| `TreeMap` | Sorted by keys |
| `PriorityQueue` | Priority-based processing |

### Example

```java
List<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");

Set<Integer> set = new HashSet<>();
set.add(10); set.add(20); set.add(10);  // {10, 20}

Map<String, Integer> map = new HashMap<>();
map.put("A", 1);
map.put("B", 2);
```

### Key Points

- Supports **Generics** for type safety
- **Fail-fast** iterators throw `ConcurrentModificationException`
- Use `Iterator` for traversal

---

## Multithreading

A **thread** is a lightweight sub-process enabling concurrent execution.

### Creating Threads

```java
// 1. Extend Thread
class MyThread extends Thread {
    public void run() { System.out.println("Running"); }
}
MyThread t = new MyThread();
t.start();

// 2. Implement Runnable
class MyTask implements Runnable {
    public void run() { System.out.println("Running"); }
}
Thread t = new Thread(new MyTask());
t.start();
```

### Important Methods

| Method | Description |
|--------|-------------|
| `start()` | Begin thread execution |
| `run()` | Defines task (don't call directly) |
| `sleep(ms)` | Pause thread |
| `join()` | Wait for thread to finish |

### Synchronization

Prevents race conditions when multiple threads access shared data.

```java
synchronized void increment() { count++; }
```

### Thread Types

| Type | Description |
|------|-------------|
| User Thread | Application waits for completion |
| Daemon Thread | JVM exits when only daemons remain (e.g., GC) |

### Problems

Race Condition, Deadlock, Starvation — use `ExecutorService` for thread pools.

---

## File Handling

Java treats files and directories through streams and the `File` class.

### File Class

```java
File f = new File("example.txt");
f.exists();
f.createNewFile();
f.delete();
f.isFile();
f.isDirectory();
f.list();  // files in directory
```

### Stream Types

| Type | Use For |
|------|---------|
| Byte Streams (`InputStream`/`OutputStream`) | Binary files (images, audio) |
| Character Streams (`Reader`/`Writer`) | Text files |

### Reading a Text File

```java
try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
}
```

### Writing a Text File

```java
try (BufferedWriter bw = new BufferedWriter(new FileWriter("out.txt"))) {
    bw.write("Hello Java");
}
```

### Best Practices

- Use **try-with-resources** (auto-close)
- Use **Buffered** streams for performance
- Handle `IOException` properly

---

## Java 8+ Features

### Lambda Expressions

```java
// Before
Runnable r = new Runnable() {
    public void run() { System.out.println("Hello"); }
};

// After
Runnable r = () -> System.out.println("Hello");
```

### Functional Interface

Interface with exactly one abstract method.

```java
@FunctionalInterface
interface MyFunc {
    void show(String msg);
}
```

### Stream API

```java
List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
int sum = list.stream()
    .filter(n -> n % 2 == 0)
    .mapToInt(n -> n)
    .sum();
```

### Optional

```java
Optional<String> name = Optional.ofNullable(getName());
name.ifPresent(n -> System.out.println(n));
```

### Other Features

| Feature | Description |
|---------|-------------|
| Default methods in interfaces | Method with body in interface |
| `java.time` API | Immutable, thread-safe date/time |
| `CompletableFuture` | Async programming |
| Method references | `list.forEach(System.out::println)` |

---

## Interview Questions

### Core Java

1. What is Java? Key features?
2. Difference between JDK, JRE, JVM?
3. What is OOP? Four pillars?
4. `==` vs `equals()`?
5. What is String Pool?
6. `final`, `finally`, `finalize`?
7. Access modifiers?
8. Abstract class vs Interface?

### Collections & Multithreading

1. Collection Framework hierarchy?
2. ArrayList vs LinkedList?
3. HashMap vs Hashtable?
4. What is a Thread? How to create?
5. `start()` vs `run()`?
6. What is synchronization? Deadlock?

### Java 8 & Advanced

1. Lambda expressions?
2. Functional Interface?
3. Stream API?
4. Optional class?
5. Garbage Collection?
6. Serialization?

### Tips

- Practice coding daily
- Be calm and confident
- Explain your approach out loud
- Start brute force, then optimize

---

## Frequently Asked Questions (FAQ)

**Q: What is Java?**
High-level, object-oriented programming language — platform independent via JVM.

**Q: JDK vs JRE vs JVM?**
- **JDK** — Development kit (compiler + tools)
- **JRE** — Runtime environment (libraries + JVM)
- **JVM** — Executes bytecode

**Q: What is OOP?**
Programming based on objects with 4 principles: Inheritance, Polymorphism, Encapsulation, Abstraction.

**Q: `==` vs `equals()`?**
`==` compares references; `equals()` compares content.

**Q: What is String Pool?**
Memory area storing string literals for reuse.

**Q: What is a Constructor?**
Special method to initialize objects — same name as class, no return type.

**Q: What is HashMap?**
Key-value store with O(1) average access — allows one null key.

**Q: What is Exception Handling?**
Mechanism using `try-catch-finally` to handle runtime errors gracefully.

---

## Practice Questions

### Theory

1. Explain four OOP concepts with examples
2. Difference between abstraction and encapsulation
3. Method overloading vs overriding
4. Checked vs unchecked exceptions
5. Interface vs abstract class
6. `HashMap` vs `HashTable`

### Coding

1. Reverse a String
2. Check if number is prime
3. Find Fibonacci series
4. Find largest element in array
5. Count vowels in a String
6. Implement Stack using array
7. Sort a list of integers

### Tips

- Solve daily — consistency is key
- Write code yourself (don't just read)
- Dry run with examples
- Handle edge cases

---

## Programs and Practice

### Hello World

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Add Two Numbers

```java
import java.util.Scanner;
public class AddNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int a = sc.nextInt();
        System.out.print("Enter second number: ");
        int b = sc.nextInt();
        System.out.println("Sum = " + (a + b));
    }
}
```

### Check Even or Odd

```java
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
if (n % 2 == 0)
    System.out.println("Even");
else
    System.out.println("Odd");
```

### Factorial

```java
int n = sc.nextInt();
long fact = 1;
for (int i = 1; i <= n; i++)
    fact *= i;
System.out.println("Factorial = " + fact);
```

### Prime Number Check

```java
int n = sc.nextInt();
boolean isPrime = n > 1;
for (int i = 2; i * i <= n; i++) {
    if (n % i == 0) { isPrime = false; break; }
}
System.out.println(isPrime ? "Prime" : "Not Prime");
```

### Fibonacci Series

```java
int n = sc.nextInt();
int a = 0, b = 1;
System.out.print(a + " " + b + " ");
for (int i = 3; i <= n; i++) {
    int c = a + b;
    System.out.print(c + " ");
    a = b; b = c;
}
```

> **Code. Compile. Run. Debug. Repeat.**

---

## Tips and Best Practices

### Learning Path

1. **Understand the basics** — strong foundation matters
2. **Solve problems actively** — start easy, go medium/hard
3. **Practice regularly** — consistency beats talent
4. **Write code daily** — builds confidence
5. **Review and revise** — spaced repetition works
6. **Discuss and learn** — ask doubts, share solutions

### Coding Best Practices

- Follow naming conventions (`camelCase` for variables/methods)
- Keep methods small and focused
- Handle exceptions properly
- Use meaningful variable names
- Comment only non-obvious logic
- Read error messages carefully

### Conclusion

You have taken a great step toward becoming a better Java programmer.

- Stay curious
- Keep practicing
- Learn from mistakes
- Be patient — every expert was once a beginner

> **Believe in yourself. Stay positive. Keep going. You've got this!**
