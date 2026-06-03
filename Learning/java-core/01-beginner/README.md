# ☕ Core Java - Beginner Guide

Master Java programming fundamentals from scratch!

---

## 📖 What is Java?

Java is a high-level, object-oriented programming language that follows the principle **"Write Once, Run Anywhere" (WORA)**.

### Why Java?

✅ **Platform Independent** - Runs on any device with JVM  
✅ **Object-Oriented** - Clean, modular code  
✅ **Robust & Secure** - Strong memory management  
✅ **Rich Ecosystem** - Vast libraries and frameworks  
✅ **High Demand** - Popular in enterprise applications  
✅ **Great Community** - Extensive support and resources  

---

## 🏗️ Java Architecture

```
┌─────────────────────────────────────┐
│      Java Source Code (.java)      │
└──────────────┬──────────────────────┘
               │
               ▼
         [javac compiler]
               │
               ▼
┌─────────────────────────────────────┐
│     Bytecode (.class files)         │
└──────────────┬──────────────────────┘
               │
               ▼
         [Java Virtual Machine]
               │
      ┌────────┼────────┐
      ▼        ▼        ▼
   Windows   Mac     Linux
```

**Explanation:**
- **In Simple Words:** You write Java once, compile to bytecode, and the JVM runs it on any computer — like a universal translator for your code.
- **Source code (`.java`)** — The Java files you write in an editor
- **`javac` compiler** — Turns your code into bytecode (`.class` files)
- **Bytecode** — Middle format that any JVM can run (not Windows/Mac-specific machine code)
- **JVM** — The program that actually runs your bytecode on your OS
- **WORA** — Write once, run on Windows, Mac, or Linux without recompiling per OS

---

## 📝 Your First Java Program

### Hello World

```java
// HelloWorld.java

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**Explanation:**
- **In Simple Words:** A Java program is a class with a `main` method — that's where execution starts when you run it.
- `public class HelloWorld` — Class name must match the filename (`HelloWorld.java`)
- `public static void main(String[] args)` — Program entry point; JVM calls this first
- `System.out.println()` — Prints a line to the console
- `;` — Ends each statement
- `{}` — Groups code into blocks (class body, method body)

**Compile and Run:**
```bash
javac HelloWorld.java  # Compile
java HelloWorld        # Run
```

---

## 🔤 Variables and Data Types

### Primitive Data Types

**Definition:** Primitive types are Java's built-in data types that store **simple values directly** in memory. They are not objects — each variable holds the actual value (e.g., `25`, `true`, `'A'`), not a reference to something else.

Java has **8 primitive types**:

| Type | Size | Description | Example |
|------|------|-------------|---------|
| `byte` | 8-bit | Small whole numbers | `byte age = 25;` |
| `short` | 16-bit | Medium whole numbers | `short year = 2024;` |
| `int` | 32-bit | Default for integers | `int count = 100;` |
| `long` | 64-bit | Large whole numbers | `long id = 9876543210L;` |
| `float` | 32-bit | Single-precision decimal | `float price = 19.99f;` |
| `double` | 64-bit | Default for decimals | `double pi = 3.14;` |
| `char` | 16-bit | Single Unicode character | `char grade = 'A';` |
| `boolean` | 1-bit | `true` or `false` | `boolean active = true;` |

**Key points:**
- Primitives have **default values** when declared as fields (`0`, `false`, `'\u0000'`) — local variables must be assigned before use
- Use `L` suffix for `long` and `f` suffix for `float` when assigning literals
- Choose the smallest type that fits your data to save memory (though `int` and `double` are most common)

```java
public class DataTypes {
    public static void main(String[] args) {
        // Integer types
        byte age = 25;           // 8-bit: -128 to 127
        short year = 2024;       // 16-bit: -32,768 to 32,767
        int population = 1000000; // 32-bit: -2^31 to 2^31-1
        long distance = 9876543210L; // 64-bit: -2^63 to 2^63-1
        
        // Floating-point types
        float price = 19.99f;    // 32-bit floating point
        double pi = 3.14159265;  // 64-bit floating point
        
        // Character and Boolean
        char grade = 'A';        // 16-bit Unicode character
        boolean isActive = true; // true or false
        
        // Printing variables
        System.out.println("Age: " + age);
        System.out.println("Price: $" + price);
        System.out.println("Is Active: " + isActive);
    }
}
```

**Explanation:**
- **In Simple Words:** Primitives are simple boxes that hold one value directly — numbers, one character, or true/false.
- Integer types (`byte`, `short`, `int`, `long`) — whole numbers; use `int` unless you need a smaller or bigger type
- Floating types (`float`, `double`) — decimal numbers; use `double` by default
- `char` — one character in single quotes (`'A'`)
- `boolean` — only `true` or `false` (for `if` and loops)
- `+` in `println` — joins text; numbers are converted to strings automatically

### Reference Types

**Definition:** Reference types store a **reference (memory address)** to an object on the heap, not the object itself. Think of the variable as a pointer or label that points to the actual data elsewhere in memory.

Unlike primitives, reference types:
- Are **objects** (or arrays) created with `new` or literals (e.g., `"Hello"`)
- Default to `null` when not initialized
- Can be `null` (no object pointed to)
- Are passed **by reference value** — a copy of the address is passed, so both variables can refer to the same object

**Common reference types:**

| Category | Examples | Purpose |
|----------|----------|---------|
| **String** | `String name = "John";` | Text data (immutable) |
| **Arrays** | `int[] nums = {1, 2, 3};` | Fixed-size collections |
| **Classes** | `Scanner sc = new Scanner(System.in);` | Custom or library objects |
| **Wrappers** | `Integer`, `Double`, `Boolean` | Object versions of primitives (for collections, nullability) |

```java
public class ReferenceTypes {
    public static void main(String[] args) {
        // Strings
        String name = "John Doe";
        String greeting = "Hello";
        String message = greeting + ", " + name + "!";
        
        System.out.println(message); // Hello, John Doe!
        
        // Arrays
        int[] numbers = {1, 2, 3, 4, 5};
        String[] names = new String[3];
        names[0] = "Alice";
        names[1] = "Bob";
        names[2] = "Charlie";
    }
}
```

**Explanation:**
- **In Simple Words:** Reference types don't hold the data itself — they point to an object (like a label on a box elsewhere in memory).
- `String` — text object; use `+` to join strings
- `int[] numbers` — array with preset values
- `new String[3]` — empty array of size 3; each slot starts as `null`
- Two reference variables can point to the same object (same array in memory)

### Type Casting

**Definition:** Type casting is **converting a value from one data type to another**. Java supports two kinds:

| Type | Also called | Direction | Syntax | Risk |
|------|-------------|-----------|--------|------|
| **Widening** | Implicit casting | Smaller → larger type | Automatic (no cast) | Safe — no data loss |
| **Narrowing** | Explicit casting | Larger → smaller type | `(targetType) value` | May lose precision |

**Widening order (safe, automatic):**
```
byte → short → int → long → float → double
                char → int
```

**When casting is needed:**
- **Numeric:** Assigning `double` to `int` requires `(int)` — decimal part is truncated
- **String ↔ number:** Use `Integer.parseInt()`, `Double.parseDouble()`, or `String.valueOf()`
- **Objects:** Upcasting is implicit; downcasting requires `(SubClass) obj` and can throw `ClassCastException`

```java
public class TypeCasting {
    public static void main(String[] args) {
        // Implicit casting (widening)
        int num = 100;
        long bigNum = num;      // int to long
        double decimal = bigNum; // long to double
        
        // Explicit casting (narrowing)
        double pi = 3.14159;
        int roundedPi = (int) pi;  // 3 (loses decimal part)
        
        // String conversion
        String ageStr = "25";
        int age = Integer.parseInt(ageStr);
        
        String priceStr = String.valueOf(19.99);
    }
}
```

**Explanation:**
- **In Simple Words:** Casting is changing a value from one type to another — sometimes automatic (safe), sometimes you must ask explicitly (may lose data).
- `long bigNum = num` — automatic widening: small type fits into bigger type safely
- `(int) pi` — manual narrowing: decimal part is cut off (`3`)
- `Integer.parseInt(ageStr)` — text to number (fails if text is not a valid integer)
- `String.valueOf(19.99)` — number to text

---

## ➕ Operators

### Arithmetic Operators

```java
public class ArithmeticOps {
    public static void main(String[] args) {
        int a = 10, b = 3;
        
        System.out.println("Addition: " + (a + b));       // 13
        System.out.println("Subtraction: " + (a - b));    // 7
        System.out.println("Multiplication: " + (a * b)); // 30
        System.out.println("Division: " + (a / b));       // 3
        System.out.println("Modulus: " + (a % b));        // 1
        
        // Increment/Decrement
        int x = 5;
        System.out.println("x++: " + (x++)); // 5 (post-increment)
        System.out.println("x: " + x);       // 6
        System.out.println("++x: " + (++x)); // 7 (pre-increment)
    }
}
```

**Explanation:**
- **In Simple Words:** Arithmetic operators do math; `%` gives the leftover after division; watch out for integer division dropping decimals.
- `+`, `-`, `*`, `/`, `%` — add, subtract, multiply, divide, remainder
- `10 / 3` with integers — result is `3`, not `3.33` (use `double` for decimals)
- `x++` — use `x`, then add 1
- `++x` — add 1 first, then use `x`

### Comparison Operators

```java
public class ComparisonOps {
    public static void main(String[] args) {
        int a = 10, b = 20;
        
        System.out.println("a == b: " + (a == b)); // false
        System.out.println("a != b: " + (a != b)); // true
        System.out.println("a > b: " + (a > b));   // false
        System.out.println("a < b: " + (a < b));   // true
        System.out.println("a >= b: " + (a >= b)); // false
        System.out.println("a <= b: " + (a <= b)); // true
    }
}
```

**Explanation:**
- **In Simple Words:** Comparison operators answer yes/no questions — they always give you `true` or `false`.
- `==` and `!=` — same or different
- `>`, `<`, `>=`, `<=` — greater, less, or equal
- Result is always `boolean` — used in `if`, `while`, `for`

### Logical Operators

```java
public class LogicalOps {
    public static void main(String[] args) {
        boolean x = true, y = false;
        
        System.out.println("x && y: " + (x && y)); // AND: false
        System.out.println("x || y: " + (x || y)); // OR: true
        System.out.println("!x: " + (!x));         // NOT: false
        
        // Short-circuit evaluation
        int a = 10, b = 0;
        boolean result = (b != 0) && (a / b > 0); // Doesn't evaluate second part
    }
}
```

**Explanation:**
- **In Simple Words:** Logical operators combine true/false conditions — AND needs both true, OR needs at least one true.
- `&&` — both must be true
- `||` — at least one must be true
- `!` — flips true to false and vice versa
- Short-circuit — Java may skip the second part if the answer is already known (helps avoid crashes like dividing by zero)

---

## 🔀 Control Flow Statements

### If-Else

```java
public class IfElseDemo {
    public static void main(String[] args) {
        int age = 18;
        
        if (age >= 18) {
            System.out.println("You are an adult");
        } else {
            System.out.println("You are a minor");
        }
        
        // If-else-if ladder
        int score = 85;
        
        if (score >= 90) {
            System.out.println("Grade: A");
        } else if (score >= 80) {
            System.out.println("Grade: B");
        } else if (score >= 70) {
            System.out.println("Grade: C");
        } else if (score >= 60) {
            System.out.println("Grade: D");
        } else {
            System.out.println("Grade: F");
        }
        
        // Ternary operator
        String result = (score >= 60) ? "Pass" : "Fail";
    }
}
```

**Explanation:**
- **In Simple Words:** `if` lets your program choose different paths based on whether a condition is true or false.
- `if` / `else` — do one thing or the other
- `else if` — try the next condition if the previous ones failed
- Ternary `? :` — short if-else in one line
- Condition must be `true` or `false`

### Switch Statement

```java
public class SwitchDemo {
    public static void main(String[] args) {
        int day = 3;
        String dayName;
        
        switch (day) {
            case 1:
                dayName = "Monday";
                break;
            case 2:
                dayName = "Tuesday";
                break;
            case 3:
                dayName = "Wednesday";
                break;
            case 4:
                dayName = "Thursday";
                break;
            case 5:
                dayName = "Friday";
                break;
            case 6:
            case 7:
                dayName = "Weekend";
                break;
            default:
                dayName = "Invalid day";
        }
        
        System.out.println(dayName);
        
        // Java 14+ Switch expression
        String dayType = switch (day) {
            case 1, 2, 3, 4, 5 -> "Weekday";
            case 6, 7 -> "Weekend";
            default -> "Invalid";
        };
    }
}
```

**Explanation:**
- **In Simple Words:** `switch` picks one action from many options based on a single value — like a menu with numbered choices.
- `switch (day)` — compare `day` to each `case`
- `break` — stop after a match; without it, code "falls through" to the next case
- Multiple `case` labels — same code for several values (e.g. weekend)
- `default` — runs when nothing else matches
- Switch expression (`->`) — cleaner syntax that returns a value without `break`

---

## 🔁 Loops

### For Loop

```java
public class ForLoopDemo {
    public static void main(String[] args) {
        // Basic for loop
        for (int i = 1; i <= 5; i++) {
            System.out.println("Count: " + i);
        }
        
        // For loop with array
        int[] numbers = {1, 2, 3, 4, 5};
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("numbers[" + i + "] = " + numbers[i]);
        }
        
        // Enhanced for loop (for-each)
        for (int num : numbers) {
            System.out.println("Number: " + num);
        }
        
        // Nested loops
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                System.out.print(i + "," + j + " ");
            }
            System.out.println();
        }
    }
}
```

**Explanation:**
- **In Simple Words:** Loops repeat code — `for` is best when you know how many times, for-each is easiest for reading every item in a list or array.
- Classic `for` — `start; keep going while; step` — count 1 to 5, loop an array by index
- `numbers[i]` — get element at position `i` (starts at 0)
- For-each `for (int num : numbers)` — visit each value without managing index
- Nested loops — one loop inside another (grids, patterns)

### While Loop

```java
public class WhileLoopDemo {
    public static void main(String[] args) {
        // While loop
        int count = 1;
        while (count <= 5) {
            System.out.println("Count: " + count);
            count++;
        }
        
        // Do-while loop (executes at least once)
        int num = 1;
        do {
            System.out.println("Number: " + num);
            num++;
        } while (num <= 5);
        
        // Infinite loop (use with break)
        int i = 0;
        while (true) {
            if (i >= 5) break;
            System.out.println(i);
            i++;
        }
    }
}
```

**Explanation:**
- **In Simple Words:** `while` repeats until the condition becomes false; `do-while` always runs at least once before checking.
- `while` — check first, then run (may never run)
- `do-while` — run once, then check
- `while (true)` with `break` — loop until you explicitly stop
- Change your counter inside the loop so it eventually ends

### Loop Control

```java
public class LoopControl {
    public static void main(String[] args) {
        // Break statement
        for (int i = 1; i <= 10; i++) {
            if (i == 5) break;  // Exit loop when i is 5
            System.out.println(i);
        }
        
        // Continue statement
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) continue;  // Skip even numbers
            System.out.println(i);
        }
        
        // Labeled break (for nested loops)
        outer:
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i * j > 4) break outer;
                System.out.println(i + " * " + j + " = " + (i * j));
            }
        }
    }
}
```

**Explanation:**
- **In Simple Words:** `break` jumps out of a loop early; `continue` skips to the next round without finishing the rest of this round.
- `break` — exit the loop now
- `continue` — skip the rest of this iteration, go to next
- Labeled `break outer` — escape a nested loop from deep inside

---

## 📦 Arrays

### One-Dimensional Arrays

```java
public class ArraysDemo {
    public static void main(String[] args) {
        // Declaration and initialization
        int[] numbers = new int[5];  // Array of size 5
        int[] values = {1, 2, 3, 4, 5};  // Array with values
        
        // Accessing elements
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        
        System.out.println("First element: " + numbers[0]);
        System.out.println("Array length: " + numbers.length);
        
        // Iterating through array
        for (int i = 0; i < values.length; i++) {
            System.out.println("values[" + i + "] = " + values[i]);
        }
        
        // Enhanced for loop
        for (int value : values) {
            System.out.println("Value: " + value);
        }
    }
}
```

**Explanation:**
- **In Simple Words:** An array is a fixed-size list of slots — same type, numbered from 0, great for storing many values in order.
- `new int[5]` — five slots, all start at `0` for numbers
- `{1, 2, 3}` — create and fill in one line
- First index is `0`; last is `length - 1`
- `.length` — how many slots (no `()`)

### Multi-Dimensional Arrays

```java
public class MultiDimensionalArrays {
    public static void main(String[] args) {
        // 2D array
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        
        // Accessing elements
        System.out.println("Element at [1][2]: " + matrix[1][2]); // 6
        
        // Iterating through 2D array
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        
        // Jagged array (different row sizes)
        int[][] jaggedArray = new int[3][];
        jaggedArray[0] = new int[2];
        jaggedArray[1] = new int[3];
        jaggedArray[2] = new int[4];
    }
}
```

**Explanation:**
- **In Simple Words:** A 2D array is like a table — rows and columns — each cell is `matrix[row][col]`.
- `int[][]` — grid of numbers
- `matrix[1][2]` — row 1, column 2 (both start at 0)
- Nested loops — outer = rows, inner = columns
- Jagged array — rows can have different lengths

---

## 🔧 Methods (Functions)

### Method Basics

```java
public class MethodsDemo {
    // Method without return value
    public static void greet() {
        System.out.println("Hello, World!");
    }
    
    // Method with parameters
    public static void greetPerson(String name) {
        System.out.println("Hello, " + name + "!");
    }
    
    // Method with return value
    public static int add(int a, int b) {
        return a + b;
    }
    
    // Method with multiple parameters
    public static double calculateAverage(int a, int b, int c) {
        return (a + b + c) / 3.0;
    }
    
    public static void main(String[] args) {
        greet();
        greetPerson("John");
        
        int sum = add(10, 20);
        System.out.println("Sum: " + sum);
        
        double avg = calculateAverage(80, 90, 85);
        System.out.println("Average: " + avg);
    }
}
```

**Explanation:**
- **In Simple Words:** Methods are reusable chunks of code — you pass inputs, they can send a result back.
- `void` — no return value
- Parameters — values you pass in, like `(String name)`
- `return` — give back a result to whoever called the method
- `static` — call without creating an object (common in `main`)
- `3.0` — makes division keep decimals

### Method Overloading

```java
public class MethodOverloading {
    // Same method name, different parameters
    public static int add(int a, int b) {
        return a + b;
    }
    
    public static double add(double a, double b) {
        return a + b;
    }
    
    public static int add(int a, int b, int c) {
        return a + b + c;
    }
    
    public static void main(String[] args) {
        System.out.println(add(5, 10));           // 15
        System.out.println(add(5.5, 10.5));       // 16.0
        System.out.println(add(5, 10, 15));       // 30
    }
}
```

**Explanation:**
- **In Simple Words:** Overloading is using the same method name with different inputs — Java picks the right version based on what you pass.
- Same name, different parameters (count, types, or order)
- Compiler chooses at compile time from your arguments
- Return type alone is not enough to overload
- One name `add` for many similar operations

### Varargs (Variable Arguments)

```java
public class VarargsDemo {
    public static int sum(int... numbers) {
        int total = 0;
        for (int num : numbers) {
            total += num;
        }
        return total;
    }
    
    public static void main(String[] args) {
        System.out.println(sum(1, 2, 3));           // 6
        System.out.println(sum(1, 2, 3, 4, 5));     // 15
        System.out.println(sum());                   // 0
    }
}
```

**Explanation:**
- **In Simple Words:** Varargs let you pass any number of arguments of one type — handy when you don't know how many values you'll get.
- `int... numbers` — acts like an array inside the method
- `sum(1, 2, 3)` — Java bundles them into an array for you
- `sum()` — zero arguments is allowed
- Varargs must be the last parameter in the list

---

## 🎯 Hands-On Exercises

### Exercise 1: Temperature Converter

```java
public class TemperatureConverter {
    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9/5) + 32;
    }
    
    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5/9;
    }
    
    public static void main(String[] args) {
        double tempC = 25.0;
        double tempF = celsiusToFahrenheit(tempC);
        System.out.println(tempC + "°C = " + tempF + "°F");
        
        tempF = 77.0;
        tempC = fahrenheitToCelsius(tempF);
        System.out.println(tempF + "°F = " + tempC + "°C");
    }
}
```

**Explanation:**
- **In Simple Words:** Put each formula in its own method so you can reuse it anywhere — use `double` so temperatures keep decimals.
- Celsius to Fahrenheit: `(C × 9/5) + 32`
- Fahrenheit to Celsius: `(F − 32) × 5/9`
- One method per conversion keeps code clear
- `double` avoids chopping off decimal temperatures

### Exercise 2: Prime Number Checker

```java
public class PrimeChecker {
    public static boolean isPrime(int number) {
        if (number <= 1) return false;
        if (number == 2) return true;
        if (number % 2 == 0) return false;
        
        for (int i = 3; i <= Math.sqrt(number); i += 2) {
            if (number % i == 0) return false;
        }
        return true;
    }
    
    public static void main(String[] args) {
        System.out.println("Prime numbers from 1 to 50:");
        for (int i = 1; i <= 50; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
    }
}
```

**Explanation:**
- **In Simple Words:** A prime has no divisors except 1 and itself — check only up to √n and skip even numbers after 2 to go faster.
- 0 and 1 are not prime; 2 is prime
- Test odd divisors from 3 upward
- Stop at `√number` — if something divides it, one factor is already smaller than √n
- Return `true`/`false` so callers can use it in `if`

### Exercise 3: Array Operations

```java
public class ArrayOperations {
    public static int findMax(int[] arr) {
        int max = arr[0];
        for (int num : arr) {
            if (num > max) max = num;
        }
        return max;
    }
    
    public static int findMin(int[] arr) {
        int min = arr[0];
        for (int num : arr) {
            if (num < min) min = num;
        }
        return min;
    }
    
    public static double findAverage(int[] arr) {
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return (double) sum / arr.length;
    }
    
    public static void main(String[] args) {
        int[] numbers = {45, 23, 67, 12, 89, 34, 56};
        
        System.out.println("Max: " + findMax(numbers));
        System.out.println("Min: " + findMin(numbers));
        System.out.println("Average: " + findAverage(numbers));
    }
}
```

**Explanation:**
- **In Simple Words:** Pass the array once and loop through it — track max/min as you go, and cast to `double` before dividing for a correct average.
- One parameter `int[] arr` works for any array of ints
- Start with `arr[0]` and update when you see a bigger/smaller value
- `(double) sum / arr.length` — avoids integer division chopping the average
- Real apps should check the array is not empty first

---

## 🎓 Practice Problems

### Problem 1: Factorial Calculator
Write a program to calculate the factorial of a number using both iterative and recursive approaches.

### Problem 2: Fibonacci Series
Generate the first N numbers of the Fibonacci series.

### Problem 3: Palindrome Checker
Check if a given string is a palindrome.

### Problem 4: Pattern Printing
Print various patterns (pyramid, diamond, etc.) using loops.

### Problem 5: Array Reversal
Reverse an array without using extra space.

---

## ✅ Beginner Checklist

- [ ] Understand Java syntax and structure
- [ ] Can declare and use variables
- [ ] Know all primitive data types
- [ ] Understand operators
- [ ] Can use if-else and switch
- [ ] Comfortable with loops
- [ ] Can work with arrays
- [ ] Can create and call methods
- [ ] Understand method overloading
- [ ] Completed all exercises

---

## 🚀 Next Steps

Once you've mastered these basics:

1. **Move to:** `02-core-java/02-intermediate/` for OOP concepts
2. **Practice:** Solve 10-20 basic problems on LeetCode/HackerRank
3. **Build:** Simple console applications
4. **Learn:** Object-Oriented Programming fundamentals

---

**Remember:** Programming is learned by doing. Write code every day! 💪

---

## 💡 Simple Explanation (In Plain English)

- This section is your first steps in Java: how programs run, variables, loops, arrays, and methods.
- You learn the building blocks every interview and real project still uses — even advanced topics build on these.
- Think of it as learning the alphabet before writing sentences: syntax, types, and control flow come first.
- Practice the small exercises so `if`, `for`, and methods feel natural before moving to OOP.

## 🎯 Interview Quick Prep

### Q1: What is the JVM, and why does Java need it?
**Simple Answer:** The JVM (Java Virtual Machine) runs compiled bytecode on any operating system. You compile `.java` to `.class` once; the JVM on each machine executes it. That is how Java achieves "Write Once, Run Anywhere."

### Q2: What is the difference between primitive and reference types?
**Simple Answer:** Primitives (`int`, `boolean`, etc.) store the actual value directly. Reference types (`String`, arrays, objects) store an address pointing to data on the heap. Primitives cannot be `null`; references can.

### Q3: What is the difference between `==` and `.equals()` for objects?
**Simple Answer:** `==` checks whether two references point to the same object in memory. `.equals()` checks whether the content is the same (when properly overridden). For strings, always prefer `.equals()` for comparing text.

### Q4: Explain method overloading vs overriding (beginner view).
**Simple Answer:** Overloading is same method name, different parameters in one class — the compiler picks the match at compile time. Overriding is a child class replacing a parent's method with the same signature — the JVM picks the child's version at runtime.

### Q5: Why does `main` have the signature `public static void main(String[] args)`?
**Simple Answer:** `public` lets the JVM call it from outside the class. `static` means no object is needed — the JVM can start the program immediately. `String[] args` holds command-line arguments passed when you run the program.

**Must-know for interviews:** Know the 8 primitives, stack vs heap basics, and be able to write a simple loop/array/method solution on a whiteboard.

