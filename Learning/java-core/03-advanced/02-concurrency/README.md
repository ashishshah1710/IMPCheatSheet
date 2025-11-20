# 🧵 Advanced Concurrency & Multithreading

Master concurrent programming and build scalable, thread-safe applications!

---

## 📚 Table of Contents

1. [java.util.concurrent Package](#concurrent-package)
2. [Thread Pools & Executors](#thread-pools)
3. [Synchronization Utilities](#synchronization-utilities)
4. [Atomic Operations](#atomic-operations)
5. [Locks & Conditions](#locks-conditions)
6. [Concurrent Collections](#concurrent-collections)
7. [CompletableFuture](#completable-future)
8. [Interview Questions](#interview-questions)

---

## 📦 java.util.concurrent Package

### Overview of Concurrency Utilities

```
java.util.concurrent
├── Executor Framework
│   ├── Executor
│   ├── ExecutorService
│   ├── ThreadPoolExecutor
│   ├── ScheduledExecutorService
│   └── ForkJoinPool
├── Synchronizers
│   ├── CountDownLatch
│   ├── CyclicBarrier
│   ├── Semaphore
│   ├── Phaser
│   └── Exchanger
├── Locks
│   ├── ReentrantLock
│   ├── ReentrantReadWriteLock
│   ├── StampedLock
│   └── Condition
├── Atomic Variables
│   ├── AtomicInteger
│   ├── AtomicLong
│   ├── AtomicBoolean
│   ├── AtomicReference
│   └── LongAdder
├── Concurrent Collections
│   ├── ConcurrentHashMap
│   ├── CopyOnWriteArrayList
│   ├── BlockingQueue
│   └── ConcurrentSkipListMap
└── Async Programming
    ├── CompletableFuture
    ├── Future
    └── Callable
```

---

## 🏊 Thread Pools & Executors

### Q1: ExecutorService Types and Usage

**Answer:**

```java
import java.util.concurrent.*;
import java.util.*;

public class ExecutorServiceDemo {
    
    public static void main(String[] args) throws Exception {
        // 1. FIXED THREAD POOL - Fixed number of threads
        System.out.println("=== Fixed Thread Pool ===");
        ExecutorService fixedPool = Executors.newFixedThreadPool(3);
        
        for (int i = 0; i < 10; i++) {
            int taskId = i;
            fixedPool.submit(() -> {
                System.out.println("Task " + taskId + " by " + 
                    Thread.currentThread().getName());
                Thread.sleep(1000);
                return null;
            });
        }
        fixedPool.shutdown();
        
        // 2. CACHED THREAD POOL - Creates threads as needed
        System.out.println("\n=== Cached Thread Pool ===");
        ExecutorService cachedPool = Executors.newCachedThreadPool();
        
        for (int i = 0; i < 5; i++) {
            int taskId = i;
            cachedPool.submit(() -> {
                System.out.println("Task " + taskId + " by " + 
                    Thread.currentThread().getName());
                return null;
            });
        }
        cachedPool.shutdown();
        
        // 3. SINGLE THREAD EXECUTOR - Sequential execution
        System.out.println("\n=== Single Thread Executor ===");
        ExecutorService singleExecutor = Executors.newSingleThreadExecutor();
        
        for (int i = 0; i < 5; i++) {
            int taskId = i;
            singleExecutor.submit(() -> {
                System.out.println("Task " + taskId + " executed");
                return null;
            });
        }
        singleExecutor.shutdown();
        
        // 4. SCHEDULED EXECUTOR - Delayed/periodic execution
        System.out.println("\n=== Scheduled Executor ===");
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(2);
        
        // Execute after 2 seconds delay
        scheduler.schedule(() -> {
            System.out.println("Delayed task executed");
        }, 2, TimeUnit.SECONDS);
        
        // Execute periodically every 3 seconds
        scheduler.scheduleAtFixedRate(() -> {
            System.out.println("Periodic task: " + System.currentTimeMillis());
        }, 0, 3, TimeUnit.SECONDS);
        
        // Let it run for 10 seconds
        Thread.sleep(10000);
        scheduler.shutdown();
        
        // 5. WORK STEALING POOL - Fork/Join based
        System.out.println("\n=== Work Stealing Pool ===");
        ExecutorService workStealingPool = Executors.newWorkStealingPool();
        
        List<Callable<String>> tasks = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int taskId = i;
            tasks.add(() -> {
                Thread.sleep(100);
                return "Result " + taskId;
            });
        }
        
        List<Future<String>> results = workStealingPool.invokeAll(tasks);
        for (Future<String> result : results) {
            System.out.println(result.get());
        }
        workStealingPool.shutdown();
    }
}
```

### Q2: Custom ThreadPoolExecutor

**Answer:**

```java
import java.util.concurrent.*;

public class CustomThreadPoolDemo {
    
    public static void main(String[] args) throws Exception {
        // Custom thread pool with full control
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2,                              // corePoolSize
            4,                              // maximumPoolSize
            60L,                            // keepAliveTime
            TimeUnit.SECONDS,               // time unit
            new LinkedBlockingQueue<>(10),  // work queue
            new CustomThreadFactory(),      // thread factory
            new CustomRejectionHandler()    // rejection policy
        );
        
        // Monitor pool
        System.out.println("Core pool size: " + executor.getCorePoolSize());
        System.out.println("Max pool size: " + executor.getMaximumPoolSize());
        
        // Submit tasks
        for (int i = 0; i < 20; i++) {
            int taskId = i;
            try {
                executor.submit(() -> {
                    System.out.println("Executing task " + taskId + " by " + 
                        Thread.currentThread().getName());
                    Thread.sleep(2000);
                    return null;
                });
            } catch (RejectedExecutionException e) {
                System.out.println("Task " + taskId + " rejected!");
            }
        }
        
        // Monitor during execution
        while (executor.getActiveCount() > 0) {
            System.out.println("Active threads: " + executor.getActiveCount());
            System.out.println("Completed tasks: " + executor.getCompletedTaskCount());
            System.out.println("Queue size: " + executor.getQueue().size());
            Thread.sleep(1000);
        }
        
        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);
    }
    
    // Custom Thread Factory
    static class CustomThreadFactory implements ThreadFactory {
        private int counter = 0;
        
        @Override
        public Thread newThread(Runnable r) {
            Thread thread = new Thread(r);
            thread.setName("CustomThread-" + counter++);
            thread.setPriority(Thread.NORM_PRIORITY);
            thread.setDaemon(false);
            return thread;
        }
    }
    
    // Custom Rejection Handler
    static class CustomRejectionHandler implements RejectedExecutionHandler {
        @Override
        public void rejectedExecution(Runnable r, ThreadPoolExecutor executor) {
            System.out.println("Task rejected: " + r.toString());
            // Custom handling: log, retry, queue elsewhere, etc.
        }
    }
}

/*
BUILT-IN REJECTION POLICIES:

1. AbortPolicy (default) - Throws RejectedExecutionException
2. CallerRunsPolicy - Executes task in caller thread
3. DiscardPolicy - Silently discards task
4. DiscardOldestPolicy - Discards oldest task in queue
*/
```

---

## 🔄 Synchronization Utilities

### Q3: CountDownLatch

**Answer:**

```java
import java.util.concurrent.*;

public class CountDownLatchDemo {
    
    public static void main(String[] args) throws InterruptedException {
        int numWorkers = 5;
        CountDownLatch latch = new CountDownLatch(numWorkers);
        
        System.out.println("Master thread waiting for workers...");
        
        // Create worker threads
        for (int i = 0; i < numWorkers; i++) {
            new Thread(new Worker(i, latch)).start();
        }
        
        // Wait for all workers to complete
        latch.await();
        System.out.println("All workers completed. Master thread proceeding.");
        
        // Real-world example: Service startup
        serviceStartupExample();
    }
    
    static class Worker implements Runnable {
        private int id;
        private CountDownLatch latch;
        
        Worker(int id, CountDownLatch latch) {
            this.id = id;
            this.latch = latch;
        }
        
        @Override
        public void run() {
            try {
                System.out.println("Worker " + id + " started");
                Thread.sleep((long)(Math.random() * 3000));
                System.out.println("Worker " + id + " completed");
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                latch.countDown();
            }
        }
    }
    
    // Real-world example: Wait for multiple services to start
    static void serviceStartupExample() throws InterruptedException {
        CountDownLatch readyLatch = new CountDownLatch(3);
        
        // Start services
        new Thread(() -> {
            System.out.println("Database service starting...");
            sleep(2000);
            System.out.println("Database service ready");
            readyLatch.countDown();
        }).start();
        
        new Thread(() -> {
            System.out.println("Cache service starting...");
            sleep(1000);
            System.out.println("Cache service ready");
            readyLatch.countDown();
        }).start();
        
        new Thread(() -> {
            System.out.println("Message queue starting...");
            sleep(1500);
            System.out.println("Message queue ready");
            readyLatch.countDown();
        }).start();
        
        // Wait for all services
        readyLatch.await();
        System.out.println("All services ready. Application can start!");
    }
    
    static void sleep(long millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

### Q4: CyclicBarrier

**Answer:**

```java
import java.util.concurrent.*;

public class CyclicBarrierDemo {
    
    public static void main(String[] args) {
        int numThreads = 3;
        
        // Barrier with action to execute when all parties reach barrier
        CyclicBarrier barrier = new CyclicBarrier(numThreads, () -> {
            System.out.println("===== All threads reached barrier! =====\n");
        });
        
        // Create worker threads
        for (int i = 0; i < numThreads; i++) {
            new Thread(new Task(i, barrier)).start();
        }
        
        // Example: Parallel computation with phases
        parallelComputationExample();
    }
    
    static class Task implements Runnable {
        private int id;
        private CyclicBarrier barrier;
        
        Task(int id, CyclicBarrier barrier) {
            this.id = id;
            this.barrier = barrier;
        }
        
        @Override
        public void run() {
            try {
                for (int phase = 1; phase <= 3; phase++) {
                    System.out.println("Thread " + id + " - Phase " + phase + " started");
                    Thread.sleep((long)(Math.random() * 2000));
                    System.out.println("Thread " + id + " - Phase " + phase + " completed");
                    
                    // Wait for all threads to complete this phase
                    barrier.await();
                }
            } catch (InterruptedException | BrokenBarrierException e) {
                e.printStackTrace();
            }
        }
    }
    
    // Real-world example: Matrix multiplication in parallel
    static void parallelComputationExample() {
        int numWorkers = 4;
        CyclicBarrier barrier = new CyclicBarrier(numWorkers, () -> {
            System.out.println("Computation phase completed");
        });
        
        for (int i = 0; i < numWorkers; i++) {
            int workerId = i;
            new Thread(() -> {
                try {
                    // Phase 1: Load data
                    System.out.println("Worker " + workerId + ": Loading data");
                    Thread.sleep(1000);
                    barrier.await();
                    
                    // Phase 2: Process data
                    System.out.println("Worker " + workerId + ": Processing data");
                    Thread.sleep(1500);
                    barrier.await();
                    
                    // Phase 3: Save results
                    System.out.println("Worker " + workerId + ": Saving results");
                    Thread.sleep(500);
                    barrier.await();
                    
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }).start();
        }
    }
}

/*
COUNTDOWNLATCH vs CYCLICBARRIER:

CountDownLatch:
- One-time use
- Threads wait for countdown to reach zero
- Can't be reset
- Different threads can count down

CyclicBarrier:
- Reusable
- Threads wait for each other
- Can be reset
- Same threads participate in barrier
*/
```

### Q5: Semaphore

**Answer:**

```java
import java.util.concurrent.*;

public class SemaphoreDemo {
    
    public static void main(String[] args) {
        // Connection pool example
        connectionPoolExample();
        
        // Rate limiter example
        rateLimiterExample();
    }
    
    // Example: Database connection pool
    static void connectionPoolExample() {
        ConnectionPool pool = new ConnectionPool(3);
        
        for (int i = 0; i < 10; i++) {
            int userId = i;
            new Thread(() -> {
                try {
                    Connection conn = pool.getConnection();
                    System.out.println("User " + userId + " got connection: " + conn);
                    
                    // Use connection
                    Thread.sleep((long)(Math.random() * 3000));
                    
                    pool.releaseConnection(conn);
                    System.out.println("User " + userId + " released connection");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }).start();
        }
    }
    
    static class ConnectionPool {
        private Semaphore semaphore;
        private Connection[] connections;
        private boolean[] available;
        
        ConnectionPool(int size) {
            semaphore = new Semaphore(size, true); // fair mode
            connections = new Connection[size];
            available = new boolean[size];
            
            for (int i = 0; i < size; i++) {
                connections[i] = new Connection(i);
                available[i] = true;
            }
        }
        
        Connection getConnection() throws InterruptedException {
            semaphore.acquire();
            return getNextAvailableConnection();
        }
        
        void releaseConnection(Connection conn) {
            synchronized(this) {
                available[conn.getId()] = true;
            }
            semaphore.release();
        }
        
        private synchronized Connection getNextAvailableConnection() {
            for (int i = 0; i < connections.length; i++) {
                if (available[i]) {
                    available[i] = false;
                    return connections[i];
                }
            }
            return null;
        }
    }
    
    static class Connection {
        private int id;
        
        Connection(int id) {
            this.id = id;
        }
        
        int getId() {
            return id;
        }
        
        @Override
        public String toString() {
            return "Connection-" + id;
        }
    }
    
    // Example: Rate limiter
    static void rateLimiterExample() {
        RateLimiter limiter = new RateLimiter(3, 1); // 3 requests per second
        
        for (int i = 0; i < 10; i++) {
            int requestId = i;
            new Thread(() -> {
                try {
                    limiter.acquire();
                    System.out.println("Request " + requestId + " processed at " + 
                        System.currentTimeMillis());
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }).start();
        }
    }
    
    static class RateLimiter {
        private Semaphore semaphore;
        private int maxPermits;
        private long period;
        
        RateLimiter(int permits, long periodSeconds) {
            this.semaphore = new Semaphore(permits);
            this.maxPermits = permits;
            this.period = periodSeconds * 1000;
            startRefillThread();
        }
        
        void acquire() throws InterruptedException {
            semaphore.acquire();
        }
        
        private void startRefillThread() {
            new Thread(() -> {
                while (true) {
                    try {
                        Thread.sleep(period);
                        semaphore.release(maxPermits - semaphore.availablePermits());
                    } catch (InterruptedException e) {
                        break;
                    }
                }
            }).start();
        }
    }
}
```

---

## ⚛️ Atomic Operations

### Q6: Atomic Variables

**Answer:**

```java
import java.util.concurrent.atomic.*;
import java.util.concurrent.*;

public class AtomicDemo {
    
    public static void main(String[] args) throws Exception {
        // Compare: synchronized vs atomic
        comparePerformance();
        
        // Atomic operations demo
        atomicOperations();
    }
    
    static void comparePerformance() throws Exception {
        int numThreads = 10;
        int iterations = 100000;
        
        // 1. Synchronized counter
        SynchronizedCounter syncCounter = new SynchronizedCounter();
        long start1 = System.nanoTime();
        
        ExecutorService executor1 = Executors.newFixedThreadPool(numThreads);
        for (int i = 0; i < numThreads; i++) {
            executor1.submit(() -> {
                for (int j = 0; j < iterations; j++) {
                    syncCounter.increment();
                }
            });
        }
        executor1.shutdown();
        executor1.awaitTermination(1, TimeUnit.MINUTES);
        
        long end1 = System.nanoTime();
        System.out.println("Synchronized: " + syncCounter.get() + 
            " Time: " + (end1 - start1) / 1_000_000 + " ms");
        
        // 2. Atomic counter
        AtomicCounter atomicCounter = new AtomicCounter();
        long start2 = System.nanoTime();
        
        ExecutorService executor2 = Executors.newFixedThreadPool(numThreads);
        for (int i = 0; i < numThreads; i++) {
            executor2.submit(() -> {
                for (int j = 0; j < iterations; j++) {
                    atomicCounter.increment();
                }
            });
        }
        executor2.shutdown();
        executor2.awaitTermination(1, TimeUnit.MINUTES);
        
        long end2 = System.nanoTime();
        System.out.println("Atomic: " + atomicCounter.get() + 
            " Time: " + (end2 - start2) / 1_000_000 + " ms");
    }
    
    static class SynchronizedCounter {
        private int count = 0;
        
        public synchronized void increment() {
            count++;
        }
        
        public synchronized int get() {
            return count;
        }
    }
    
    static class AtomicCounter {
        private AtomicInteger count = new AtomicInteger(0);
        
        public void increment() {
            count.incrementAndGet();
        }
        
        public int get() {
            return count.get();
        }
    }
    
    static void atomicOperations() {
        System.out.println("\n=== Atomic Operations ===");
        
        // AtomicInteger
        AtomicInteger atomicInt = new AtomicInteger(10);
        System.out.println("Initial: " + atomicInt.get());
        System.out.println("Increment and get: " + atomicInt.incrementAndGet());
        System.out.println("Add and get (5): " + atomicInt.addAndGet(5));
        System.out.println("Compare and set (16, 100): " + 
            atomicInt.compareAndSet(16, 100));
        System.out.println("Current: " + atomicInt.get());
        
        // AtomicLong
        AtomicLong atomicLong = new AtomicLong(1000L);
        atomicLong.incrementAndGet();
        System.out.println("\nAtomicLong: " + atomicLong.get());
        
        // AtomicBoolean
        AtomicBoolean atomicBool = new AtomicBoolean(false);
        System.out.println("\nAtomicBoolean initial: " + atomicBool.get());
        atomicBool.set(true);
        System.out.println("After set: " + atomicBool.get());
        System.out.println("Compare and set: " + 
            atomicBool.compareAndSet(true, false));
        
        // AtomicReference
        AtomicReference<String> atomicRef = new AtomicReference<>("Initial");
        System.out.println("\nAtomicReference: " + atomicRef.get());
        atomicRef.set("Updated");
        System.out.println("After update: " + atomicRef.get());
        
        // LongAdder - Better for high contention
        LongAdder longAdder = new LongAdder();
        longAdder.increment();
        longAdder.add(10);
        System.out.println("\nLongAdder: " + longAdder.sum());
        
        // AtomicIntegerArray
        AtomicIntegerArray array = new AtomicIntegerArray(5);
        array.set(0, 10);
        array.set(1, 20);
        System.out.println("\nAtomicArray[0]: " + array.get(0));
        array.incrementAndGet(0);
        System.out.println("After increment: " + array.get(0));
    }
}
```

---

## 🔒 Locks & Conditions

### Q7: ReentrantLock vs Synchronized

**Answer:**

```java
import java.util.concurrent.locks.*;
import java.util.*;

public class LockDemo {
    
    public static void main(String[] args) throws Exception {
        // ReentrantLock features
        reentrantLockFeatures();
        
        // ReadWriteLock example
        readWriteLockExample();
        
        // Producer-Consumer with Condition
        producerConsumerExample();
    }
    
    static void reentrantLockFeatures() throws Exception {
        ReentrantLock lock = new ReentrantLock(true); // fair lock
        
        // Feature 1: Try lock with timeout
        new Thread(() -> {
            try {
                if (lock.tryLock(1, java.util.concurrent.TimeUnit.SECONDS)) {
                    try {
                        System.out.println("Thread 1 acquired lock");
                        Thread.sleep(2000);
                    } finally {
                        lock.unlock();
                    }
                } else {
                    System.out.println("Thread 1 couldn't acquire lock");
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        
        Thread.sleep(100);
        
        new Thread(() -> {
            try {
                if (lock.tryLock(1, java.util.concurrent.TimeUnit.SECONDS)) {
                    try {
                        System.out.println("Thread 2 acquired lock");
                    } finally {
                        lock.unlock();
                    }
                } else {
                    System.out.println("Thread 2 couldn't acquire lock");
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        
        Thread.sleep(3000);
        
        // Feature 2: Check lock status
        System.out.println("Is locked: " + lock.isLocked());
        System.out.println("Has queued threads: " + lock.hasQueuedThreads());
    }
    
    static void readWriteLockExample() throws Exception {
        ReadWriteLockDemo demo = new ReadWriteLockDemo();
        
        // Multiple readers
        for (int i = 0; i < 3; i++) {
            int readerId = i;
            new Thread(() -> {
                System.out.println("Reader " + readerId + ": " + demo.read());
            }).start();
        }
        
        Thread.sleep(1000);
        
        // Single writer
        new Thread(() -> {
            demo.write("Updated value");
            System.out.println("Writer updated value");
        }).start();
        
        Thread.sleep(2000);
    }
    
    static class ReadWriteLockDemo {
        private String data = "Initial value";
        private ReadWriteLock rwLock = new ReentrantReadWriteLock();
        private Lock readLock = rwLock.readLock();
        private Lock writeLock = rwLock.writeLock();
        
        String read() {
            readLock.lock();
            try {
                System.out.println(Thread.currentThread().getName() + " reading");
                Thread.sleep(1000);
                return data;
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            } finally {
                readLock.unlock();
            }
        }
        
        void write(String newData) {
            writeLock.lock();
            try {
                System.out.println(Thread.currentThread().getName() + " writing");
                Thread.sleep(1000);
                data = newData;
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            } finally {
                writeLock.unlock();
            }
        }
    }
    
    static void producerConsumerExample() throws Exception {
        BlockingQueueDemo queue = new BlockingQueueDemo(5);
        
        // Producer
        new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                try {
                    queue.put(i);
                    System.out.println("Produced: " + i);
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }).start();
        
        // Consumer
        new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                try {
                    int value = queue.take();
                    System.out.println("Consumed: " + value);
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
    
    static class BlockingQueueDemo {
        private Queue<Integer> queue = new LinkedList<>();
        private int capacity;
        private ReentrantLock lock = new ReentrantLock();
        private Condition notFull = lock.newCondition();
        private Condition notEmpty = lock.newCondition();
        
        BlockingQueueDemo(int capacity) {
            this.capacity = capacity;
        }
        
        void put(int value) throws InterruptedException {
            lock.lock();
            try {
                while (queue.size() == capacity) {
                    notFull.await();
                }
                queue.add(value);
                notEmpty.signalAll();
            } finally {
                lock.unlock();
            }
        }
        
        int take() throws InterruptedException {
            lock.lock();
            try {
                while (queue.isEmpty()) {
                    notEmpty.await();
                }
                int value = queue.poll();
                notFull.signalAll();
                return value;
            } finally {
                lock.unlock();
            }
        }
    }
}
```

---

**Continue to Part 2** for Concurrent Collections, CompletableFuture, and Interview Questions! 🚀

