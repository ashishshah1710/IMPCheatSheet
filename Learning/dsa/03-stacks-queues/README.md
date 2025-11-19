# 📚 Stacks & Queues

## Overview
Stacks and Queues are linear data structures that restrict access to their elements in specific ways.

---

## 🔹 STACKS (LIFO - Last In First Out)

### Basic Concept
A stack is like a stack of plates - you can only add or remove from the top.

### Core Operations
```java
class Stack {
    private int[] arr;
    private int top;
    private int capacity;
    
    public Stack(int size) {
        arr = new int[size];
        capacity = size;
        top = -1;
    }
    
    // Push element
    public void push(int x) {
        if (isFull()) {
            throw new StackOverflowError("Stack is full");
        }
        arr[++top] = x;
    }
    
    // Pop element
    public int pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return arr[top--];
    }
    
    // Peek top element
    public int peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return arr[top];
    }
    
    public boolean isEmpty() {
        return top == -1;
    }
    
    public boolean isFull() {
        return top == capacity - 1;
    }
}
```

### Stack Using Linked List
```java
class StackNode {
    int data;
    StackNode next;
    StackNode(int data) {
        this.data = data;
    }
}

class LinkedStack {
    StackNode top;
    
    public void push(int data) {
        StackNode newNode = new StackNode(data);
        newNode.next = top;
        top = newNode;
    }
    
    public int pop() {
        if (top == null) throw new EmptyStackException();
        int data = top.data;
        top = top.next;
        return data;
    }
    
    public int peek() {
        if (top == null) throw new EmptyStackException();
        return top.data;
    }
}
```

### Common Stack Problems

#### 1. **Balanced Parentheses**
```java
boolean isBalanced(String s) {
    Stack<Character> stack = new Stack<>();
    Map<Character, Character> map = new HashMap<>();
    map.put(')', '(');
    map.put('}', '{');
    map.put(']', '[');
    
    for (char c : s.toCharArray()) {
        if (map.containsValue(c)) {
            stack.push(c);
        } else if (map.containsKey(c)) {
            if (stack.isEmpty() || stack.pop() != map.get(c)) {
                return false;
            }
        }
    }
    return stack.isEmpty();
}
```

#### 2. **Next Greater Element**
```java
int[] nextGreaterElement(int[] arr) {
    int n = arr.length;
    int[] result = new int[n];
    Stack<Integer> stack = new Stack<>();
    
    for (int i = n - 1; i >= 0; i--) {
        while (!stack.isEmpty() && stack.peek() <= arr[i]) {
            stack.pop();
        }
        result[i] = stack.isEmpty() ? -1 : stack.peek();
        stack.push(arr[i]);
    }
    return result;
}
```

#### 3. **Evaluate Postfix Expression**
```java
int evaluatePostfix(String exp) {
    Stack<Integer> stack = new Stack<>();
    
    for (char c : exp.toCharArray()) {
        if (Character.isDigit(c)) {
            stack.push(c - '0');
        } else {
            int val2 = stack.pop();
            int val1 = stack.pop();
            switch (c) {
                case '+': stack.push(val1 + val2); break;
                case '-': stack.push(val1 - val2); break;
                case '*': stack.push(val1 * val2); break;
                case '/': stack.push(val1 / val2); break;
            }
        }
    }
    return stack.pop();
}
```

---

## 🔹 QUEUES (FIFO - First In First Out)

### Basic Concept
A queue is like a line at a store - first person in line gets served first.

### Core Operations (Array Implementation)
```java
class Queue {
    private int[] arr;
    private int front, rear, size, capacity;
    
    public Queue(int capacity) {
        this.capacity = capacity;
        arr = new int[capacity];
        front = 0;
        rear = -1;
        size = 0;
    }
    
    // Enqueue (add to rear)
    public void enqueue(int x) {
        if (isFull()) {
            throw new IllegalStateException("Queue is full");
        }
        rear = (rear + 1) % capacity;
        arr[rear] = x;
        size++;
    }
    
    // Dequeue (remove from front)
    public int dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }
        int data = arr[front];
        front = (front + 1) % capacity;
        size--;
        return data;
    }
    
    public int peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }
        return arr[front];
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    public boolean isFull() {
        return size == capacity;
    }
}
```

### Queue Using Linked List
```java
class QueueNode {
    int data;
    QueueNode next;
    QueueNode(int data) {
        this.data = data;
    }
}

class LinkedQueue {
    QueueNode front, rear;
    
    public void enqueue(int data) {
        QueueNode newNode = new QueueNode(data);
        if (rear == null) {
            front = rear = newNode;
            return;
        }
        rear.next = newNode;
        rear = newNode;
    }
    
    public int dequeue() {
        if (front == null) {
            throw new NoSuchElementException("Queue is empty");
        }
        int data = front.data;
        front = front.next;
        if (front == null) rear = null;
        return data;
    }
}
```

### Circular Queue
```java
class CircularQueue {
    private int[] arr;
    private int front, rear, size, capacity;
    
    public CircularQueue(int k) {
        capacity = k;
        arr = new int[k];
        front = -1;
        rear = -1;
        size = 0;
    }
    
    public boolean enQueue(int value) {
        if (isFull()) return false;
        if (isEmpty()) front = 0;
        rear = (rear + 1) % capacity;
        arr[rear] = value;
        size++;
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()) return false;
        if (front == rear) {
            front = rear = -1;
        } else {
            front = (front + 1) % capacity;
        }
        size--;
        return true;
    }
}
```

### Priority Queue (Min Heap)
```java
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
minHeap.offer(5);
minHeap.offer(2);
minHeap.offer(8);
int min = minHeap.poll(); // Returns 2
```

### Common Queue Problems

#### 1. **Implement Stack Using Queues**
```java
class MyStack {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();
    
    public void push(int x) {
        q2.offer(x);
        while (!q1.isEmpty()) {
            q2.offer(q1.poll());
        }
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }
    
    public int pop() {
        return q1.poll();
    }
}
```

#### 2. **Sliding Window Maximum**
```java
int[] maxSlidingWindow(int[] nums, int k) {
    Deque<Integer> deque = new LinkedList<>();
    int[] result = new int[nums.length - k + 1];
    
    for (int i = 0; i < nums.length; i++) {
        // Remove elements outside window
        if (!deque.isEmpty() && deque.peek() < i - k + 1) {
            deque.poll();
        }
        // Remove smaller elements
        while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
            deque.pollLast();
        }
        deque.offer(i);
        if (i >= k - 1) {
            result[i - k + 1] = nums[deque.peek()];
        }
    }
    return result;
}
```

## Practice Problems

### Stack Problems
#### Easy
1. ✅ Valid Parentheses
2. ✅ Min Stack
3. ✅ Implement Stack using Queues

#### Medium
4. 🔥 Next Greater Element
5. 🔥 Daily Temperatures
6. 🔥 Evaluate Reverse Polish Notation
7. 🔥 Asteroid Collision
8. 🔥 Decode String

#### Hard
9. 💪 Largest Rectangle in Histogram
10. 💪 Trapping Rain Water
11. 💪 Basic Calculator

### Queue Problems
#### Easy
12. ✅ Implement Queue using Stacks
13. ✅ Circular Queue

#### Medium
14. 🔥 Sliding Window Maximum
15. 🔥 Design Circular Deque
16. 🔥 Time Needed to Buy Tickets

#### Hard
17. 💪 Shortest Subarray with Sum at Least K
18. 💪 Maximum Frequency Stack

## Complexity Analysis

| Operation | Array Stack | Linked Stack | Array Queue | Linked Queue |
|-----------|-------------|--------------|-------------|--------------|
| Push/Enqueue | O(1) | O(1) | O(1) | O(1) |
| Pop/Dequeue | O(1) | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) | O(1) |
| Space | O(n) | O(n) | O(n) | O(n) |

## Real-World Applications

### Stacks
- **Browser History**: Back button
- **Undo/Redo**: Text editors
- **Function Calls**: Call stack
- **Expression Evaluation**: Calculators
- **Syntax Parsing**: Compilers

### Queues
- **Task Scheduling**: OS process scheduling
- **Printer Queue**: Print jobs
- **BFS**: Graph traversal
- **Message Queues**: Kafka, RabbitMQ
- **Request Handling**: Web servers

## Interview Tips

1. **Know when to use what**: Stack for LIFO, Queue for FIFO
2. **Master monotonic stack/queue**: Very common pattern
3. **Practice two-stack/queue problems**: Implement one using other
4. **Understand deque**: Double-ended queue (both ends access)
5. **Priority queue mastery**: Heap-based operations

## Next Steps

- **Trees** → [04-trees](../04-trees/README.md)
- **Graphs** → [05-graphs](../05-graphs/README.md)
- **Practice** → [problem-patterns](../problem-patterns/README.md)

---

**💡 Pro Tip**: Monotonic stack is one of the most powerful patterns in competitive programming. Master it!

