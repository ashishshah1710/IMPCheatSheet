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
- `public class HelloWorld` - Class definition (must match filename)
- `public static void main(String[] args)` - Entry point of program
- `System.out.println()` - Print to console
- `;` - Statement terminator
- `{}` - Code blocks

**Compile and Run:**
```bash
javac HelloWorld.java  # Compile
java HelloWorld        # Run
```

---

## 🔤 Variables and Data Types

### Primitive Data Types

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

### Reference Types

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

### Type Casting

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

