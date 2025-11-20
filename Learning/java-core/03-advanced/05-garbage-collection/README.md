# 🗑️ Garbage Collection & Memory Management

Master Java memory management and optimize GC performance!

---

## 📚 Table of Contents

1. [Memory Structure](#memory-structure)
2. [GC Algorithms](#gc-algorithms)
3. [GC Tuning](#gc-tuning)
4. [Memory Leaks](#memory-leaks)
5. [Monitoring & Tools](#monitoring-tools)
6. [Interview Questions](#interview-questions)

---

## 🧠 Memory Structure

### Heap Memory Organization

```
┌────────────────────────────────────────────────────┐
│                  JAVA HEAP                          │
├────────────────────────────────────────────────────┤
│  YOUNG GENERATION (1/3 of heap)                    │
│  ┌──────────────────────────────────────────────┐ │
│  │  Eden Space (80%)                            │ │
│  │  - New objects allocated here                │ │
│  │  - Minor GC happens here                     │ │
│  └──────────────────────────────────────────────┘ │
│  ┌────────────────────┬────────────────────────┐ │
│  │  Survivor 0 (10%)  │  Survivor 1 (10%)     │ │
│  │  - Objects that    │  - Alternates with S0  │ │
│  │    survived 1 GC   │    during Minor GC     │ │
│  └────────────────────┴────────────────────────┘ │
├────────────────────────────────────────────────────┤
│  OLD GENERATION / TENURED (2/3 of heap)            │
│  - Long-lived objects                              │
│  - Objects promoted from Young Gen                 │
│  - Major GC happens here (slower)                  │
├────────────────────────────────────────────────────┤
│  METASPACE (Java 8+) - Native Memory               │
│  - Class metadata                                  │
│  - Static variables                                │
│  - Constant pool                                   │
│  - Can grow dynamically                            │
└────────────────────────────────────────────────────┘
```

### Object Lifecycle

```java
public class ObjectLifecycleDemo {
    public static void main(String[] args) {
        // 1. Object created in Eden space
        MyObject obj1 = new MyObject("Object1");
        
        // 2. More objects created
        for (int i = 0; i < 1000; i++) {
            MyObject temp = new MyObject("Temp" + i);
            // temp becomes eligible for GC after loop iteration
        }
        
        // 3. obj1 survives Minor GC, moves to Survivor space
        System.gc(); // Suggest GC (not guaranteed)
        
        // 4. After multiple survivals (age threshold), promoted to Old Gen
        // Default age threshold: 15 (can be changed with -XX:MaxTenuringThreshold)
        
        // 5. Object no longer referenced, eligible for GC
        obj1 = null;
        
        // 6. Eventually garbage collected
        System.gc();
    }
}

class MyObject {
    private String name;
    private byte[] data = new byte[1024]; // 1KB
    
    public MyObject(String name) {
        this.name = name;
    }
    
    @Override
    protected void finalize() throws Throwable {
        System.out.println(name + " being garbage collected");
        super.finalize();
    }
}
```

---

## 🔄 GC Algorithms

### Q1: Serial GC

**Answer:**

```bash
# Single-threaded GC
# Best for: Single-CPU machines, small heaps (<100MB), client applications

java -XX:+UseSerialGC \
     -Xms512m -Xmx512m \
     -XX:+PrintGCDetails \
     MyApp
```

**Characteristics:**
- Single GC thread
- Stops all application threads (Stop-The-World)
- Simple and low overhead
- Predictable but slow for large heaps

### Q2: Parallel GC (Throughput Collector)

**Answer:**

```bash
# Multi-threaded GC for Young and Old generations
# Best for: Batch processing, throughput-focused applications

java -XX:+UseParallelGC \
     -XX:ParallelGCThreads=4 \
     -Xms2g -Xmx2g \
     -XX:+PrintGCDetails \
     MyApp
```

**Characteristics:**
- Multiple GC threads
- Focus on maximum throughput
- Longer pause times acceptable
- Good for multi-core servers

### Q3: CMS (Concurrent Mark Sweep)

**Answer:**

```bash
# Low-latency GC (deprecated in Java 14)
# Best for: Web applications, low-latency requirements

java -XX:+UseConcMarkSweepGC \
     -XX:+UseCMSInitiatingOccupancyOnly \
     -XX:CMSInitiatingOccupancyFraction=70 \
     -Xms4g -Xmx4g \
     -XX:+PrintGCDetails \
     MyApp
```

**Phases:**
1. Initial Mark (STW) - Mark root objects
2. Concurrent Mark - Mark reachable objects
3. Concurrent Preclean - Prepare for final mark
4. Final Remark (STW) - Complete marking
5. Concurrent Sweep - Sweep dead objects
6. Concurrent Reset - Reset for next cycle

**Characteristics:**
- Most work concurrent with application
- Lower pause times
- More CPU overhead
- Can cause fragmentation

### Q4: G1 GC (Garbage First) - Default since Java 9

**Answer:**

```bash
# Region-based, low-latency GC
# Best for: Large heaps (>4GB), balanced performance

java -XX:+UseG1GC \
     -XX:MaxGCPauseMillis=200 \
     -XX:G1HeapRegionSize=4m \
     -Xms8g -Xmx8g \
     -XX:+PrintGC \
     MyApp
```

**How G1 Works:**

```
┌────────────────────────────────────────┐
│  G1 divides heap into regions (1-32MB) │
├────────────────────────────────────────┤
│  [E][E][S][O][O][H][E][O][F][E]...    │
│                                        │
│  E = Eden                              │
│  S = Survivor                          │
│  O = Old                               │
│  H = Humongous (large objects)         │
│  F = Free                              │
└────────────────────────────────────────┘
```

**Phases:**
1. Young GC - Evacuate young regions
2. Concurrent Marking
3. Mixed GC - Collect young + old regions

**Characteristics:**
- Predictable pause times
- No fragmentation (compacting)
- Good for large heaps (up to tens of GB)
- Excellent balance of throughput and latency

### Q5: ZGC (Z Garbage Collector) - Java 11+

**Answer:**

```bash
# Ultra-low latency GC (<10ms pauses)
# Best for: Real-time applications, very large heaps (multi-TB)

java -XX:+UseZGC \
     -Xms16g -Xmx16g \
     -XX:+PrintGC \
     MyApp
```

**Characteristics:**
- Pause times <10ms
- Scales to multi-TB heaps
- Concurrent compaction
- Requires more memory overhead
- Linux only (initially)

### Q6: Shenandoah GC - Java 12+

**Answer:**

```bash
# Low-pause concurrent GC
# Best for: Low-latency requirements, large heaps

java -XX:+UseShenandoahGC \
     -Xms8g -Xmx8g \
     -XX:+PrintGC \
     MyApp
```

**Characteristics:**
- Pause times independent of heap size
- Concurrent compaction
- Similar to ZGC but different algorithm
- Available on more platforms

---

## ⚙️ GC Tuning

### Q7: JVM Memory Flags

**Answer:**

```java
public class GCTuningDemo {
    public static void main(String[] args) {
        // Monitor memory
        Runtime runtime = Runtime.getRuntime();
        
        System.out.println("=== JVM Memory Info ===");
        System.out.println("Max Memory: " + 
            runtime.maxMemory() / (1024 * 1024) + " MB");
        System.out.println("Total Memory: " + 
            runtime.totalMemory() / (1024 * 1024) + " MB");
        System.out.println("Free Memory: " + 
            runtime.freeMemory() / (1024 * 1024) + " MB");
        System.out.println("Used Memory: " + 
            (runtime.totalMemory() - runtime.freeMemory()) / (1024 * 1024) + " MB");
        
        // Available processors
        System.out.println("Available Processors: " + 
            runtime.availableProcessors());
    }
}
```

**Common Tuning Flags:**

```bash
# HEAP SIZE
-Xms4g                  # Initial heap size
-Xmx8g                  # Maximum heap size
-Xmn2g                  # Young generation size
-XX:NewRatio=2          # Old/Young ratio (default: 2)
-XX:SurvivorRatio=8     # Eden/Survivor ratio (default: 8)

# GARBAGE COLLECTION
-XX:+UseG1GC                    # Use G1 GC
-XX:MaxGCPauseMillis=200        # Target pause time (ms)
-XX:ParallelGCThreads=8         # Parallel GC threads
-XX:ConcGCThreads=2             # Concurrent GC threads
-XX:G1HeapRegionSize=16m        # G1 region size

# METASPACE
-XX:MetaspaceSize=256m          # Initial metaspace
-XX:MaxMetaspaceSize=512m       # Max metaspace

# GC LOGGING (Java 8)
-XX:+PrintGCDetails
-XX:+PrintGCTimeStamps
-XX:+PrintGCDateStamps
-Xloggc:gc.log

# GC LOGGING (Java 9+)
-Xlog:gc*:file=gc.log:time,level,tags

# DEBUGGING
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=/path/to/dumps
-XX:+PrintFlagsFinal              # Print all JVM flags

# PERFORMANCE
-XX:+UseCompressedOops            # Compress object pointers (<32GB heap)
-XX:+UseStringDeduplication       # Deduplicate strings (G1 only)
-XX:+AggressiveOpts               # Aggressive optimizations
```

### Q8: GC Tuning Strategy

**Answer:**

```
1. UNDERSTAND REQUIREMENTS
   - Throughput vs Latency?
   - Heap size?
   - Response time requirements?

2. CHOOSE GC ALGORITHM
   - Small heap (<2GB): Serial or Parallel
   - Medium heap (2-8GB): G1 GC
   - Large heap (>8GB): G1 GC or ZGC
   - Ultra-low latency: ZGC or Shenandoah

3. SET INITIAL FLAGS
   - Start with defaults
   - Set heap size (-Xms, -Xmx to same value)
   - Set GC algorithm

4. MEASURE & ANALYZE
   - Enable GC logging
   - Monitor pause times
   - Track throughput
   - Check heap usage

5. TUNE ITERATIVELY
   - Adjust pause time target
   - Tune generation sizes
   - Adjust GC threads
   - Test with production load

6. VALIDATE
   - Load testing
   - Stress testing
   - Monitor in production
```

---

## 🚨 Memory Leaks

### Q9: Common Memory Leak Patterns

**Answer:**

```java
import java.util.*;

public class MemoryLeakExamples {
    
    // 1. STATIC COLLECTION THAT KEEPS GROWING
    private static List<Object> leakyList = new ArrayList<>();
    
    public void leakPattern1() {
        Object obj = new Object();
        leakyList.add(obj); // Never removed!
        // Fix: Remove when no longer needed or use WeakHashMap
    }
    
    // 2. UNCLOSED RESOURCES
    public void leakPattern2(String filename) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            String line = reader.readLine();
            // reader never closed! ❌
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    // FIX: Use try-with-resources ✅
    public void fixPattern2(String filename) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line = reader.readLine();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    // 3. THREADLOCAL NOT CLEANED UP
    private static ThreadLocal<List<String>> threadLocal = new ThreadLocal<>();
    
    public void leakPattern3() {
        threadLocal.set(new ArrayList<>());
        // Do work...
        // threadLocal.remove(); // MUST call this! ✅
    }
    
    // 4. LISTENERS NOT UNREGISTERED
    public class EventSource {
        private List<EventListener> listeners = new ArrayList<>();
        
        public void addEventListener(EventListener listener) {
            listeners.add(listener);
            // If listener is never removed, objects can't be GC'd
        }
        
        public void removeEventListener(EventListener listener) {
            listeners.remove(listener); // Important!
        }
    }
    
    // 5. HASH KEY WITHOUT PROPER EQUALS/HASHCODE
    class BadKey {
        private String key;
        
        public BadKey(String key) {
            this.key = key;
        }
        // No equals/hashCode implementation ❌
    }
    
    public void leakPattern5() {
        Map<BadKey, String> map = new HashMap<>();
        BadKey key1 = new BadKey("key");
        map.put(key1, "value");
        
        key1 = null; // Key can't be retrieved, but stays in map
        
        BadKey key2 = new BadKey("key");
        map.get(key2); // Returns null, even though logically same key
    }
    
    // 6. INNER CLASS HOLDING OUTER CLASS REFERENCE
    public class OuterClass {
        private byte[] data = new byte[1024 * 1024]; // 1MB
        
        public class InnerClass {
            // Implicitly holds reference to OuterClass
            public void method() {
                // Even if we only need InnerClass,
                // OuterClass and its data can't be GC'd
            }
        }
        
        // FIX: Use static inner class ✅
        public static class StaticInnerClass {
            // No implicit reference to OuterClass
        }
    }
}

interface EventListener {
    void onEvent();
}
```

### Q10: Detecting Memory Leaks

**Answer:**

```java
import java.lang.management.*;

public class MemoryLeakDetection {
    
    public static void main(String[] args) {
        // Monitor memory continuously
        new Thread(() -> {
            while (true) {
                printMemoryStats();
                try {
                    Thread.sleep(5000); // Every 5 seconds
                } catch (InterruptedException e) {
                    break;
                }
            }
        }).start();
        
        // Simulate application
        simulateMemoryLeak();
    }
    
    public static void printMemoryStats() {
        MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();
        MemoryUsage heapUsage = memoryBean.getHeapMemoryUsage();
        
        System.out.println("=== Memory Stats ===");
        System.out.println("Used: " + heapUsage.getUsed() / (1024 * 1024) + " MB");
        System.out.println("Committed: " + heapUsage.getCommitted() / (1024 * 1024) + " MB");
        System.out.println("Max: " + heapUsage.getMax() / (1024 * 1024) + " MB");
        
        double usedPercentage = (double) heapUsage.getUsed() / heapUsage.getMax() * 100;
        System.out.println("Usage: " + String.format("%.2f", usedPercentage) + "%");
        
        if (usedPercentage > 80) {
            System.out.println("⚠️ WARNING: High memory usage!");
        }
        System.out.println();
    }
    
    private static List<byte[]> leakyList = new ArrayList<>();
    
    public static void simulateMemoryLeak() {
        for (int i = 0; i < 1000; i++) {
            leakyList.add(new byte[1024 * 1024]); // Add 1MB each iteration
            
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                break;
            }
        }
    }
}
```

---

## 🛠️ Monitoring & Tools

### Q11: GC Monitoring Tools

**Answer:**

**1. Command Line Tools:**

```bash
# jps - List Java processes
jps -l

# jstat - GC statistics
jstat -gc <pid> 1000        # Every 1 second
jstat -gcutil <pid> 1000    # GC utilization

# jmap - Heap dump
jmap -dump:format=b,file=heap.bin <pid>
jmap -heap <pid>            # Heap configuration

# jstack - Thread dump
jstack <pid> > thread_dump.txt

# jcmd - All-purpose tool
jcmd <pid> GC.heap_info
jcmd <pid> GC.class_histogram
jcmd <pid> VM.flags
```

**2. Visual Tools:**

- **VisualVM** (bundled with JDK 8, separate download for JDK 9+)
  - Real-time monitoring
  - Heap dump analysis
  - Thread profiling
  - CPU profiling

- **Java Mission Control (JMC)**
  - Flight recorder
  - Advanced profiling
  - Low overhead

- **Eclipse Memory Analyzer (MAT)**
  - Heap dump analysis
  - Leak detection
  - Memory usage reports

**3. GC Log Analysis:**

```bash
# Generate GC logs
java -XX:+UseG1GC \
     -Xlog:gc*:file=gc.log:time,level,tags \
     -XX:+HeapDumpOnOutOfMemoryError \
     -XX:HeapDumpPath=heapdump.hprof \
     MyApp

# Analyze with GCEasy (online tool)
# Upload gc.log to https://gceasy.io
```

---

## 🎯 Interview Questions

**Q12: What causes OutOfMemoryError?**

**Answer:**

1. **Java heap space** - Heap full
2. **GC Overhead limit exceeded** - GC taking too much time
3. **Metaspace** - Too many classes loaded
4. **Unable to create new native thread** - Too many threads
5. **Direct buffer memory** - NIO buffer issue

**Q13: How to prevent memory leaks?**

**Answer:**

✅ Always close resources (use try-with-resources)  
✅ Clean up ThreadLocal variables  
✅ Unregister listeners  
✅ Implement equals/hashCode properly  
✅ Use weak references when appropriate  
✅ Avoid static collections that grow indefinitely  
✅ Profile regularly  
✅ Monitor production

---

**Master GC for optimal performance!** 🚀

