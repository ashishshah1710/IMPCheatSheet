# 🔧 JVM Internals & Performance Tuning

Master the Java Virtual Machine and optimize performance like a pro!

---

## 📚 Table of Contents

1. [JVM Architecture](#jvm-architecture)
2. [Class Loading Mechanism](#class-loading)
3. [JIT Compiler](#jit-compiler)
4. [Memory Model](#memory-model)
5. [Performance Optimization](#performance-optimization)
6. [Interview Questions](#interview-questions)

---

## 🏗️ JVM Architecture

### Complete JVM Structure

```
┌────────────────────────────────────────────────────────┐
│                   JVM Architecture                      │
├────────────────────────────────────────────────────────┤
│  CLASS LOADER SUBSYSTEM                                │
│  ┌──────────────────────────────────────────────────┐ │
│  │ Loading → Linking → Initialization               │ │
│  │                                                   │ │
│  │ Bootstrap ClassLoader (rt.jar, core classes)     │ │
│  │         ↓                                         │ │
│  │ Extension ClassLoader (ext directory)            │ │
│  │         ↓                                         │ │
│  │ Application ClassLoader (classpath)              │ │
│  │         ↓                                         │ │
│  │ Custom ClassLoaders                              │ │
│  └──────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────┤
│  RUNTIME DATA AREAS                                    │
│  ┌──────────────────────────────────────────────────┐ │
│  │ METHOD AREA (Shared across threads)             │ │
│  │ - Class metadata                                 │ │
│  │ - Static variables                               │ │
│  │ - Constant pool                                  │ │
│  │ - Method bytecode                                │ │
│  └──────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────┐ │
│  │ HEAP (Shared across threads)                    │ │
│  │ ┌─────────────────────────────────────────────┐ │ │
│  │ │ YOUNG GENERATION                            │ │ │
│  │ │ ┌──────────┬──────────┬──────────┐         │ │ │
│  │ │ │  Eden    │ Survivor │ Survivor │         │ │ │
│  │ │ │  Space   │   S0     │   S1     │         │ │ │
│  │ │ └──────────┴──────────┴──────────┘         │ │ │
│  │ └─────────────────────────────────────────────┘ │ │
│  │ ┌─────────────────────────────────────────────┐ │ │
│  │ │ OLD GENERATION (Tenured)                    │ │ │
│  │ │ Long-lived objects                          │ │ │
│  │ └─────────────────────────────────────────────┘ │ │
│  │ ┌─────────────────────────────────────────────┐ │ │
│  │ │ METASPACE (Java 8+, replaces PermGen)      │ │ │
│  │ │ Class metadata (native memory)              │ │ │
│  │ └─────────────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────┐ │
│  │ STACK (Per thread)                              │ │
│  │ - Local variables                                │ │
│  │ - Partial results                                │ │
│  │ - Method invocation & return                     │ │
│  │ - Stack frames                                   │ │
│  └──────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────┐ │
│  │ PC REGISTERS (Per thread)                       │ │
│  │ - Current instruction address                    │ │
│  └──────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────┐ │
│  │ NATIVE METHOD STACK (Per thread)                │ │
│  │ - Native method information                      │ │
│  └──────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────┤
│  EXECUTION ENGINE                                      │
│  ┌──────────────────────────────────────────────────┐ │
│  │ INTERPRETER                                      │ │
│  │ - Reads bytecode line by line                    │ │
│  │ - Slower execution                               │ │
│  └──────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────┐ │
│  │ JIT COMPILER                                     │ │
│  │ - C1 Compiler (Client, fast)                     │ │
│  │ - C2 Compiler (Server, optimized)                │ │
│  │ - Tiered compilation                             │ │
│  └──────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────┐ │
│  │ GARBAGE COLLECTOR                                │ │
│  │ - Serial GC                                      │ │
│  │ - Parallel GC                                    │ │
│  │ - CMS, G1, ZGC, Shenandoah                       │ │
│  └──────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────┤
│  NATIVE METHOD INTERFACE (JNI)                         │
│  - Connects Java with native code (C/C++)             │
├────────────────────────────────────────────────────────┤
│  NATIVE METHOD LIBRARIES                               │
│  - C/C++ libraries for JVM functionality               │
└────────────────────────────────────────────────────────┘
```

---

## 📦 Class Loading Mechanism

### Q1: Explain the Class Loading Process

**Answer:**

The class loading process has three phases:

**1. Loading**
- Find and read .class file
- Create Class object in memory
- Done by ClassLoader

**2. Linking**
- **Verification:** Ensure bytecode is valid
- **Preparation:** Allocate memory for static variables, initialize with default values
- **Resolution:** Replace symbolic references with direct references

**3. Initialization**
- Execute static initializers
- Initialize static variables with actual values

```java
public class ClassLoadingDemo {
    // Static block - executed during initialization
    static {
        System.out.println("Class initialized");
    }
    
    // Static variable - prepared with 0, initialized with 100
    static int value = 100;
    
    public static void main(String[] args) {
        System.out.println("Main method");
        System.out.println("Value: " + value);
    }
}

// Output:
// Class initialized
// Main method
// Value: 100
```

### Q2: ClassLoader Hierarchy and Delegation Model

**Answer:**

```java
public class ClassLoaderHierarchy {
    public static void main(String[] args) {
        // Get classloader of current class
        ClassLoader appLoader = ClassLoaderHierarchy.class.getClassLoader();
        System.out.println("Application ClassLoader: " + appLoader);
        
        // Parent: Extension/Platform ClassLoader
        ClassLoader extLoader = appLoader.getParent();
        System.out.println("Extension ClassLoader: " + extLoader);
        
        // Grandparent: Bootstrap ClassLoader (null - native)
        ClassLoader bootstrapLoader = extLoader.getParent();
        System.out.println("Bootstrap ClassLoader: " + bootstrapLoader);
        
        // Core classes loaded by Bootstrap
        ClassLoader stringLoader = String.class.getClassLoader();
        System.out.println("String ClassLoader: " + stringLoader); // null
        
        // ArrayList loaded by Bootstrap
        ClassLoader arrayListLoader = java.util.ArrayList.class.getClassLoader();
        System.out.println("ArrayList ClassLoader: " + arrayListLoader); // null
    }
}

// Delegation Model:
// 1. Check if class already loaded
// 2. Delegate to parent classloader
// 3. If parent can't load, try to load yourself
// 4. If still can't load, throw ClassNotFoundException
```

### Q3: Custom ClassLoader Implementation

**Answer:**

```java
import java.io.*;

public class CustomClassLoader extends ClassLoader {
    private String classPath;
    
    public CustomClassLoader(String classPath) {
        this.classPath = classPath;
    }
    
    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        try {
            byte[] classData = loadClassData(name);
            return defineClass(name, classData, 0, classData.length);
        } catch (IOException e) {
            throw new ClassNotFoundException("Class not found: " + name, e);
        }
    }
    
    private byte[] loadClassData(String className) throws IOException {
        String fileName = classPath + File.separator + 
                         className.replace('.', File.separatorChar) + ".class";
        
        try (FileInputStream fis = new FileInputStream(fileName);
             ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
            
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                baos.write(buffer, 0, bytesRead);
            }
            return baos.toByteArray();
        }
    }
    
    public static void main(String[] args) throws Exception {
        CustomClassLoader loader = new CustomClassLoader("path/to/classes");
        
        // Load class using custom loader
        Class<?> clazz = loader.loadClass("com.example.MyClass");
        
        // Create instance
        Object instance = clazz.getDeclaredConstructor().newInstance();
        
        System.out.println("Loaded class: " + clazz.getName());
        System.out.println("ClassLoader: " + clazz.getClassLoader());
    }
}
```

---

## ⚡ JIT Compiler

### Q4: How does JIT Compiler work?

**Answer:**

**JIT (Just-In-Time) Compiler** converts bytecode to native machine code at runtime for better performance.

**Process:**
1. **Interpretation:** Initially, bytecode is interpreted
2. **Profiling:** JVM monitors method execution counts
3. **Compilation:** "Hot" methods (frequently called) are compiled to native code
4. **Optimization:** Apply aggressive optimizations
5. **Caching:** Cache compiled code for reuse

**Two JIT Compilers:**

```
┌──────────────────────────────────────────────┐
│  C1 COMPILER (Client Compiler)               │
│  - Fast compilation                          │
│  - Basic optimizations                       │
│  - Lower startup overhead                    │
│  - Used for less frequently executed code    │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│  C2 COMPILER (Server Compiler)               │
│  - Slower compilation                        │
│  - Aggressive optimizations                  │
│  - Better peak performance                   │
│  - Used for hot methods                      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│  TIERED COMPILATION (Default Java 8+)        │
│  - Level 0: Interpreter                      │
│  - Level 1: C1 with simple optimizations     │
│  - Level 2: C1 with invocation counters      │
│  - Level 3: C1 with full profiling           │
│  - Level 4: C2 with aggressive optimization  │
└──────────────────────────────────────────────┘
```

**Example:**

```java
public class JITDemo {
    // This method will be JIT compiled after ~10,000 invocations
    public static long calculateSum(int n) {
        long sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
    
    public static void main(String[] args) {
        // Warm-up phase - triggers JIT compilation
        for (int i = 0; i < 20000; i++) {
            calculateSum(1000);
        }
        
        // Now running with JIT compiled code - much faster
        long start = System.nanoTime();
        long result = calculateSum(1000000);
        long end = System.nanoTime();
        
        System.out.println("Result: " + result);
        System.out.println("Time: " + (end - start) / 1_000_000.0 + " ms");
    }
}

// JVM Flags to monitor JIT:
// -XX:+PrintCompilation          - Show what's being compiled
// -XX:+UnlockDiagnosticVMOptions - Unlock diagnostic options
// -XX:+PrintInlining             - Show method inlining
// -XX:+PrintCodeCache            - Show code cache statistics
// -XX:CompileThreshold=10000     - Set compilation threshold
```

### Q5: JIT Optimizations

**Answer:**

**Key JIT Optimizations:**

```java
public class JITOptimizations {
    
    // 1. METHOD INLINING
    // Small methods are inlined directly
    public static int add(int a, int b) {
        return a + b;
    }
    
    public static void demoInlining() {
        int result = add(5, 3); // JIT will inline add() here
        // Becomes: int result = 5 + 3;
    }
    
    // 2. DEAD CODE ELIMINATION
    public static void demoDeadCode() {
        int x = 10;
        int y = 20;
        int z = x + y; // Never used
        System.out.println(x); // Only x is used
        // JIT removes: int z = x + y;
    }
    
    // 3. LOOP OPTIMIZATION
    public static void demoLoopOptimization() {
        int[] arr = new int[1000];
        
        // Loop unrolling
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i * 2;
        }
        // JIT may unroll to process multiple iterations together
        
        // Loop invariant code motion
        int constant = 100;
        for (int i = 0; i < arr.length; i++) {
            arr[i] = arr[i] + constant;
        }
        // JIT moves 'constant' outside loop
    }
    
    // 4. ESCAPE ANALYSIS
    public static int demoEscapeAnalysis() {
        // Object doesn't escape - can be stack allocated
        Point p = new Point(10, 20);
        return p.x + p.y;
        // JIT may use scalar replacement: int x = 10, y = 20;
    }
    
    // 5. LOCK ELISION
    public static void demoLockElision() {
        // Local object, lock is unnecessary
        List<String> list = new ArrayList<>();
        synchronized(list) {
            list.add("item");
        }
        // JIT removes synchronization
    }
    
    // 6. NULL CHECK ELIMINATION
    public static void demoNullCheck(Object obj) {
        if (obj != null) {
            obj.toString(); // First call
            obj.hashCode(); // JIT knows obj is not null here
        }
    }
}

class Point {
    int x, y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

---

## 🧠 Memory Model

### Q6: Java Memory Model (JMM)

**Answer:**

```java
public class JavaMemoryModel {
    
    // HEAP MEMORY (Shared across threads)
    private static String staticVar = "Shared";  // Method Area
    private String instanceVar = "Instance";      // Heap
    
    public void demonstrateMemory() {
        // STACK MEMORY (Thread-local)
        int localVar = 10;              // Stack
        String localRef = "Local";       // Reference on Stack, Object in Heap
        
        Object obj = new Object();       // Reference on Stack, Object in Heap
        int[] array = new int[5];        // Reference on Stack, Array in Heap
    }
    
    // Memory allocation example
    public static void main(String[] args) {
        // Stack frame created for main()
        JavaMemoryModel obj1 = new JavaMemoryModel(); // Heap allocation
        JavaMemoryModel obj2 = new JavaMemoryModel(); // Heap allocation
        
        obj1.demonstrateMemory(); // New stack frame
        // Stack frame destroyed after method returns
    }
}

/*
MEMORY LAYOUT:

STACK (Thread-specific)          HEAP (Shared)
┌─────────────────────┐         ┌──────────────────────────┐
│ Thread 1            │         │ Young Generation         │
│ ┌─────────────────┐ │         │ ├─ Eden Space           │
│ │ main()          │ │    ───→ │ ├─ Survivor 0           │
│ │ - obj1 ref ─────┼─┼────┘    │ └─ Survivor 1           │
│ │ - obj2 ref ─────┼─┼────┐    │                         │
│ │ - localVar      │ │    │    │ Old Generation          │
│ └─────────────────┘ │    │    │ ├─ Long-lived objects   │
│ ┌─────────────────┐ │    └───→│ └─ Promoted objects     │
│ │ method()        │ │         │                         │
│ │ - params        │ │         │ Metaspace (Java 8+)     │
│ │ - local vars    │ │         │ ├─ Class metadata       │
│ └─────────────────┘ │         │ ├─ Static variables     │
└─────────────────────┘         │ └─ Constant pool        │
                                 └──────────────────────────┘
*/
```

### Q7: Stack vs Heap Memory

**Answer:**

```java
public class StackVsHeap {
    
    // Stored in Heap (Method Area)
    static int staticVar = 100;
    
    // Instance variables - Heap
    int instanceVar = 200;
    
    public void demoMemory() {
        // Primitives - Stack
        int a = 10;
        long b = 20L;
        boolean c = true;
        
        // Reference on Stack, Object in Heap
        String str = new String("Hello");
        Integer num = new Integer(100);
        
        // Array reference on Stack, Array object in Heap
        int[] arr = new int[5];
        
        // Method call - new stack frame
        calculate(a, b);
    }
    
    public long calculate(int x, long y) {
        // New stack frame created
        long result = x + y;  // Local variable on Stack
        return result;
        // Stack frame destroyed
    }
    
    public static void main(String[] args) {
        // main() stack frame
        StackVsHeap obj = new StackVsHeap();
        obj.demoMemory();
        // When main() ends, stack frames are removed
    }
}

/*
KEY DIFFERENCES:

STACK:
✅ Fast access
✅ Thread-local (thread-safe)
✅ Automatic memory management
✅ Smaller size
✅ Stores: primitives, references, method calls
❌ Limited size (StackOverflowError if exceeded)
❌ Can't store large objects

HEAP:
✅ Large size
✅ Stores objects and arrays
✅ Accessible by all threads
✅ Flexible size
❌ Slower access than stack
❌ Garbage collection overhead
❌ Thread-safety issues (need synchronization)
*/
```

---

## 🚀 Performance Optimization

### Q8: JVM Performance Tuning

**Answer:**

**Key JVM Flags:**

```bash
# HEAP SIZE
-Xms2g              # Initial heap size (2GB)
-Xmx4g              # Maximum heap size (4GB)
-Xmn1g              # Young generation size (1GB)

# GARBAGE COLLECTION
-XX:+UseG1GC                    # Use G1 Garbage Collector
-XX:+UseParallelGC              # Use Parallel GC
-XX:+UseConcMarkSweepGC         # Use CMS GC
-XX:+UseZGC                     # Use ZGC (Java 11+)

# GC TUNING
-XX:MaxGCPauseMillis=200        # Target max pause time
-XX:ParallelGCThreads=4         # Number of GC threads
-XX:ConcGCThreads=2             # Concurrent GC threads
-XX:NewRatio=2                  # Old/Young ratio

# METASPACE (Java 8+)
-XX:MetaspaceSize=128m          # Initial metaspace size
-XX:MaxMetaspaceSize=512m       # Max metaspace size

# JIT COMPILER
-XX:CompileThreshold=10000      # Compilation threshold
-XX:+TieredCompilation          # Enable tiered compilation
-XX:TieredStopAtLevel=1         # Stop at C1 compiler

# MONITORING & DEBUGGING
-XX:+PrintGCDetails             # Print GC details
-XX:+PrintGCTimeStamps          # Print GC timestamps
-XX:+PrintGCDateStamps          # Print GC dates
-Xlog:gc*                       # GC logging (Java 9+)
-XX:+HeapDumpOnOutOfMemoryError # Heap dump on OOM
-XX:HeapDumpPath=/path/to/dump  # Heap dump location

# PERFORMANCE
-server                         # Server mode (more optimizations)
-XX:+UseCompressedOops          # Compress object pointers
-XX:+UseStringDeduplication     # Deduplicate strings (G1 GC)
-XX:+AggressiveOpts             # Aggressive optimizations

# EXAMPLE PRODUCTION CONFIGURATION
java -server \
     -Xms4g -Xmx4g \
     -XX:+UseG1GC \
     -XX:MaxGCPauseMillis=200 \
     -XX:+UseStringDeduplication \
     -XX:+PrintGCDetails \
     -XX:+HeapDumpOnOutOfMemoryError \
     -XX:HeapDumpPath=/var/log/heapdump.hprof \
     -jar myapp.jar
```

### Q9: Performance Monitoring Code

**Answer:**

```java
import java.lang.management.*;
import java.util.*;

public class PerformanceMonitoring {
    
    public static void main(String[] args) {
        // 1. Memory Monitoring
        monitorMemory();
        
        // 2. Thread Monitoring
        monitorThreads();
        
        // 3. GC Monitoring
        monitorGC();
        
        // 4. CPU Monitoring
        monitorCPU();
        
        // 5. Class Loading
        monitorClassLoading();
    }
    
    public static void monitorMemory() {
        MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();
        
        MemoryUsage heapUsage = memoryBean.getHeapMemoryUsage();
        System.out.println("=== HEAP MEMORY ===");
        System.out.println("Init: " + heapUsage.getInit() / (1024 * 1024) + " MB");
        System.out.println("Used: " + heapUsage.getUsed() / (1024 * 1024) + " MB");
        System.out.println("Committed: " + heapUsage.getCommitted() / (1024 * 1024) + " MB");
        System.out.println("Max: " + heapUsage.getMax() / (1024 * 1024) + " MB");
        
        MemoryUsage nonHeapUsage = memoryBean.getNonHeapMemoryUsage();
        System.out.println("\n=== NON-HEAP MEMORY ===");
        System.out.println("Used: " + nonHeapUsage.getUsed() / (1024 * 1024) + " MB");
        
        // Memory pools
        List<MemoryPoolMXBean> pools = ManagementFactory.getMemoryPoolMXBeans();
        System.out.println("\n=== MEMORY POOLS ===");
        for (MemoryPoolMXBean pool : pools) {
            System.out.println(pool.getName() + ": " + 
                pool.getUsage().getUsed() / (1024 * 1024) + " MB");
        }
    }
    
    public static void monitorThreads() {
        ThreadMXBean threadBean = ManagementFactory.getThreadMXBean();
        
        System.out.println("\n=== THREADS ===");
        System.out.println("Thread Count: " + threadBean.getThreadCount());
        System.out.println("Peak Thread Count: " + threadBean.getPeakThreadCount());
        System.out.println("Daemon Thread Count: " + threadBean.getDaemonThreadCount());
        System.out.println("Total Started: " + threadBean.getTotalStartedThreadCount());
        
        // Detect deadlocks
        long[] deadlockedThreads = threadBean.findDeadlockedThreads();
        if (deadlockedThreads != null) {
            System.out.println("DEADLOCK DETECTED! Threads: " + 
                Arrays.toString(deadlockedThreads));
        }
    }
    
    public static void monitorGC() {
        List<GarbageCollectorMXBean> gcBeans = 
            ManagementFactory.getGarbageCollectorMXBeans();
        
        System.out.println("\n=== GARBAGE COLLECTION ===");
        for (GarbageCollectorMXBean gc : gcBeans) {
            System.out.println("Name: " + gc.getName());
            System.out.println("Collection Count: " + gc.getCollectionCount());
            System.out.println("Collection Time: " + gc.getCollectionTime() + " ms");
            System.out.println("Memory Pools: " + Arrays.toString(gc.getMemoryPoolNames()));
            System.out.println();
        }
    }
    
    public static void monitorCPU() {
        OperatingSystemMXBean osBean = ManagementFactory.getOperatingSystemMXBean();
        
        System.out.println("=== SYSTEM ===");
        System.out.println("OS: " + osBean.getName());
        System.out.println("Architecture: " + osBean.getArch());
        System.out.println("Available Processors: " + osBean.getAvailableProcessors());
        System.out.println("System Load Average: " + osBean.getSystemLoadAverage());
        
        // Extended info (if available)
        if (osBean instanceof com.sun.management.OperatingSystemMXBean) {
            com.sun.management.OperatingSystemMXBean sunOsBean = 
                (com.sun.management.OperatingSystemMXBean) osBean;
            
            System.out.println("Process CPU Load: " + 
                sunOsBean.getProcessCpuLoad() * 100 + "%");
            System.out.println("System CPU Load: " + 
                sunOsBean.getSystemCpuLoad() * 100 + "%");
            System.out.println("Free Physical Memory: " + 
                sunOsBean.getFreePhysicalMemorySize() / (1024 * 1024) + " MB");
            System.out.println("Total Physical Memory: " + 
                sunOsBean.getTotalPhysicalMemorySize() / (1024 * 1024) + " MB");
        }
    }
    
    public static void monitorClassLoading() {
        ClassLoadingMXBean classBean = ManagementFactory.getClassLoadingMXBean();
        
        System.out.println("\n=== CLASS LOADING ===");
        System.out.println("Loaded Classes: " + classBean.getLoadedClassCount());
        System.out.println("Total Loaded: " + classBean.getTotalLoadedClassCount());
        System.out.println("Unloaded Classes: " + classBean.getUnloadedClassCount());
    }
}
```

---

## 🎯 Interview Questions

### Q10: What happens when you run `java MyClass`?

**Answer:**

**Complete Flow:**

1. **ClassLoader** loads MyClass.class
2. **Bytecode Verification** ensures code is safe
3. **Memory Allocation** for static variables
4. **Static Initialization** executes static blocks
5. **JVM** creates main thread
6. **main()** method is invoked
7. **JIT Compiler** monitors hot methods
8. **Garbage Collector** runs in background
9. **Program Execution** continues
10. **JVM Shutdown** when main() completes

### Q11: OutOfMemoryError types

**Answer:**

```java
public class OutOfMemoryExamples {
    
    // 1. Java heap space
    public static void heapOOM() {
        List<byte[]> list = new ArrayList<>();
        while (true) {
            list.add(new byte[1024 * 1024]); // 1 MB
        }
        // Error: java.lang.OutOfMemoryError: Java heap space
    }
    
    // 2. GC Overhead limit exceeded
    public static void gcOverhead() {
        Map<Integer, String> map = new HashMap<>();
        for (int i = 0; i < Integer.MAX_VALUE; i++) {
            map.put(i, "Value" + i);
        }
        // Error: GC overhead limit exceeded
        // (GC taking >98% time, recovering <2% heap)
    }
    
    // 3. Metaspace (Java 8+)
    public static void metaspaceOOM() {
        // Dynamically create many classes
        while (true) {
            new CustomClassLoader().loadClass();
        }
        // Error: java.lang.OutOfMemoryError: Metaspace
    }
    
    // 4. StackOverflowError (not OOM, but related)
    public static void stackOverflow() {
        stackOverflow(); // Infinite recursion
        // Error: java.lang.StackOverflowError
    }
    
    // 5. Unable to create native thread
    public static void threadOOM() {
        while (true) {
            new Thread(() -> {
                try {
                    Thread.sleep(Long.MAX_VALUE);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }).start();
        }
        // Error: unable to create new native thread
    }
}
```

### Q12: How to troubleshoot performance issues?

**Answer:**

**Step-by-Step Approach:**

```bash
# 1. Take thread dump
jstack <pid> > thread_dump.txt
kill -3 <pid>  # On Unix/Linux

# 2. Take heap dump
jmap -dump:format=b,file=heap.bin <pid>
# Or use flag: -XX:+HeapDumpOnOutOfMemoryError

# 3. Analyze heap dump
# Use: Eclipse MAT, VisualVM, JProfiler

# 4. Monitor GC
jstat -gc <pid> 1000    # Every 1 second
jstat -gcutil <pid> 1000

# 5. JVM flags for analysis
java -XX:+PrintGCDetails \
     -XX:+PrintGCTimeStamps \
     -Xlog:gc*:file=gc.log \
     -jar app.jar

# 6. Profiling tools
# - JVisualVM (bundled with JDK)
# - Java Mission Control
# - YourKit
# - JProfiler
# - Async-profiler
```

---

## 📚 Key Takeaways

1. **Understand JVM architecture** - Critical for optimization
2. **Master class loading** - Custom loaders for advanced scenarios
3. **Learn JIT optimizations** - Write JIT-friendly code
4. **Monitor performance** - Use built-in tools
5. **Tune JVM flags** - For production environments
6. **Profile regularly** - Identify bottlenecks early

---

**Next: Advanced Concurrency** 🧵

