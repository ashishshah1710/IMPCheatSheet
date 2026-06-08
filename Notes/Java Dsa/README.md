# Java DSA Full Notes

Source: [JAVADSAFullNotes.pdf](./JAVADSAFullNotes.pdf)

> Comprehensive Data Structures & Algorithms notes for Java developers — interview-ready, organized by topic.

## Table of Contents

1. [Introduction to DSA](#introduction-to-dsa)
2. [Time and Space Complexity](#time-and-space-complexity)
3. [Arrays](#arrays)
4. [Strings](#strings)
5. [Recursion](#recursion)
6. [Sorting](#sorting)
7. [Searching](#searching)
8. [Hashing](#hashing)
9. [Bit Manipulation](#bit-manipulation)
10. [Sliding Window Technique](#sliding-window-technique)
11. [Two Pointers Technique](#two-pointers-technique)
12. [Prefix Sum](#prefix-sum)
13. [Stack](#stack)
14. [Queue](#queue)
15. [Linked List](#linked-list)
16. [Trees](#trees)
17. [Binary Search Tree (BST)](#binary-search-tree-bst)
18. [Heap and Priority Queue](#heap-and-priority-queue)
19. [Graphs](#graphs)
20. [Greedy Algorithms](#greedy-algorithms)
21. [Dynamic Programming](#dynamic-programming)
22. [Backtracking](#backtracking)
23. [Interview Patterns and Tricks](#interview-patterns-and-tricks)
24. [Frequently Asked DSA Questions](#frequently-asked-dsa-questions)
25. [Tips and Conclusion](#tips-and-conclusion)

---

## Introduction to DSA

**DSA** stands for **Data Structures and Algorithms** — a way to organize data and solve problems efficiently.

### Data Structures

A data structure stores and organizes data for efficient use.

| Type | Examples |
|------|----------|
| Linear | Array, Linked List, Stack, Queue |
| Non-Linear | Tree, Graph, Heap |

### Algorithms

An algorithm is a step-by-step procedure to solve a problem.

**Examples:** Searching, Sorting, Shortest path in a graph, Mathematical computations.

### Why DSA Matters

- Write efficient and optimized code
- Improve problem-solving and logical thinking
- Essential for coding interviews
- Used in real-world systems (OS, DBMS, AI, apps)

> **In short:** DSA helps solve problems in the best possible way.

---

## Time and Space Complexity

### Time Complexity

Amount of time an algorithm takes as a function of input size `n`.

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Accessing array element |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Linear Search |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Bubble Sort |
| O(2ⁿ) | Exponential | Naive Fibonacci |

**Use it to:** Compare algorithms, find efficient solutions, predict performance at scale.

### Space Complexity

Amount of memory an algorithm uses as a function of input size `n`.

- **Auxiliary Space** — Extra space (variables, temp structures)
- **Total Space** — Auxiliary + Input space
- **In-Place** — O(1) extra space (e.g., Bubble Sort on same array)

> Always analyze time and space before coding. For large inputs, small improvements matter.

---

## Arrays

An **array** is a linear data structure storing elements of the same type in **contiguous memory**. Elements are accessed by **index**.

### Key Points

- All elements are the same type
- Contiguous memory locations
- Direct access via index — O(1)
- First index = `0`, last index = `n - 1`
- **Fixed size** — cannot grow or shrink

### Declaration & Initialization

```java
int[] arr = new int[5];           // size 5, default 0
int[] arr = {10, 20, 30, 40, 50}; // direct init

arr[0] = 10;  // 1st element
arr[2] = 30;  // 3rd element
```

### Common Operations

| Operation | Time | Description |
|-----------|------|-------------|
| Traversal | O(n) | Visit all elements |
| Access | O(1) | `arr[i]` |
| Insert at end | O(1)* | If space available |
| Insert at start/middle | O(n) | Shift elements |
| Delete | O(n) | Shift elements |

```java
int[] arr = {10, 20, 30, 40, 50};
for (int i = 0; i < arr.length; i++) {
    System.out.print(arr[i] + " ");
}
```

---

## Strings

A **String** is a sequence of characters. In Java, `String` is an immutable object of class `String`.

### Key Points

- **Immutable** — cannot change after creation; operations create new strings
- Stored in **String Pool** (for literals)
- Index starts at `0`
- Length = number of characters
- Supports Unicode

### Creation

```java
String s1 = "Hello";                    // literal (String Pool)
String s2 = new String("Hello");        // heap object
String s3 = "";                         // empty string
```

### Common Methods

| Method | Description |
|--------|-------------|
| `length()` | Returns length |
| `charAt(i)` | Character at index |
| `substring(i, j)` | Substring [i, j) |
| `equals()` | Content comparison |
| `equalsIgnoreCase()` | Case-insensitive |
| `toUpperCase()` / `toLowerCase()` | Case conversion |
| `contains()` | Substring check |
| `startsWith()` / `endsWith()` | Prefix/suffix check |
| `concat()` | Join strings |

### String vs StringBuilder

| | String | StringBuilder |
|---|--------|---------------|
| Mutability | Immutable | Mutable |
| Storage | String Pool / Heap | Heap |
| Use case | Few changes | Frequent modifications |

---

## Recursion

**Recursion** is when a function calls itself to solve a smaller instance of the same problem until a **base case** is reached.

### Two Parts

1. **Base Case** — Stops recursion (e.g., `n == 0`, `n == 1`)
2. **Recursive Case** — Calls itself with smaller input

### How It Works

1. Function called → pushed to call stack
2. Checks base case
3. If not base case → recursive call
4. Results returned step by step

### Examples

Factorial, Fibonacci, GCD, String Reversal, Tower of Hanoi, Subset Generation, Tree Traversals, Permutations, Power (aⁿ)

```java
int fact(int n) {
    if (n <= 1) return 1;        // base case
    return n * fact(n - 1);      // recursive case
}
```

### Trade-offs

| Pros | Cons |
|------|------|
| Short, elegant code | Extra memory (call stack) |
| Good for repetitive structure | May be slower (repeated calls) |

> Always define the base case carefully to avoid infinite recursion.

---

## Sorting

**Sorting** arranges elements in ascending or descending order.

### Why Sort?

- Organizes data systematically
- Enables Binary Search
- Improves efficiency of other algorithms
- Used in databases, leaderboards, reports

### Common Algorithms

| Algorithm | Idea | Best Use |
|-----------|------|----------|
| Bubble Sort | Swap adjacent wrong-order elements | Learning / small data |
| Selection Sort | Place minimum at correct position | When swaps are costly |
| Insertion Sort | Insert into sorted portion | Nearly sorted / small data |
| Merge Sort | Divide, sort halves, merge | Large data, stable sort |
| Quick Sort | Pivot partition | General purpose |
| Heap Sort | Use heap property | Limited extra space |

### Time Complexity

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

---

## Searching

**Searching** finds a target element in a collection and returns its index (or -1 if not found).

### Linear Search

- Works on sorted and unsorted arrays
- Check each element sequentially
- **Time:** Best O(1), Worst O(n)

```java
for (int i = 0; i < arr.length; i++) {
    if (arr[i] == target) return i;
}
return -1;
```

### Binary Search

- Requires **sorted** array
- Repeatedly divide search space in half
- **Time:** Best O(1), Average/Worst O(log n)

```java
int low = 0, high = n - 1;
while (low <= high) {
    int mid = (low + high) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) low = mid + 1;
    else high = mid - 1;
}
return -1;
```

### Tips

- Linear Search → small or unsorted data
- Binary Search → large sorted data
- Handle boundary conditions carefully in Binary Search

---

## Hashing

**Hashing** maps a key to an index in a table using a **hash function**, enabling average O(1) insert, search, and delete.

### Hash Function

`h(key) → index` — should distribute keys uniformly.

**Example:** `h(key) = key % tableSize`

### Collision Handling

| Technique | Description |
|-----------|-------------|
| Separate Chaining | Each index stores a linked list of colliding keys |
| Open Addressing | Probe for next empty slot (linear/quadratic probing) |

### Operations

- `insert(key)` — Add to table
- `search(key)` — Find key
- `delete(key)` — Remove key

### Trade-offs

| Pros | Cons |
|------|------|
| Average O(1) operations | Worst case O(n) with many collisions |
| Efficient for large datasets | Depends on hash function quality |
| Used in caching, indexing | Requires extra table space |

---

## Bit Manipulation

Operating on individual bits using **bitwise operators**.

All numbers are stored in binary (0s and 1s).

### Bitwise Operators

| Operator | Name | Description |
|----------|------|-------------|
| `&` | AND | 1 if both bits are 1 |
| `\|` | OR | 1 if any bit is 1 |
| `^` | XOR | 1 if bits differ |
| `~` | NOT | Inverts all bits |
| `<<` | Left Shift | Shifts bits left |
| `>>` | Right Shift | Shifts bits right |

### Common Tricks

```java
// Check even/odd
(n & 1) == 0  // even

// Check power of 2
(n & (n - 1)) == 0

// Set ith bit
n | (1 << i)

// Clear ith bit
n & ~(1 << i)

// Toggle ith bit
n ^ (1 << i)

// Swap without temp
a = a ^ b; b = a ^ b; a = a ^ b;
```

> Left shift ≈ multiply by 2. Right shift ≈ divide by 2.

---

## Sliding Window Technique

Maintain a **window** (subarray/substring) and slide it to solve problems in O(n) instead of O(n²).

### Types

| Type | Description | Examples |
|------|-------------|----------|
| Fixed Size | Window size k is constant | Max sum subarray of size k |
| Variable Size | Expand/shrink based on condition | Longest substring without repeats |

### Template

```java
int left = 0;
for (int right = 0; right < n; right++) {
    // add arr[right] to window
    while (windowInvalid) {
        // remove arr[left] from window
        left++;
    }
    // update answer
}
```

**Complexity:** O(n) time — each element visited at most twice.

---

## Two Pointers Technique

Use two pointers moving through data to solve problems in O(n) with O(1) extra space.

### Patterns

| Pattern | Movement | Use Cases |
|---------|----------|-----------|
| Opposite Direction | Start & end → center | Pair sum, palindrome, container with most water |
| Same Direction | Both move forward | Remove duplicates, merge sorted arrays |
| Different Speeds | Fast & slow | Linked list cycle, middle of list |

### Example — Pair Sum in Sorted Array

```java
int left = 0, right = n - 1;
while (left < right) {
    int sum = arr[left] + arr[right];
    if (sum == target) return true;
    else if (sum < target) left++;
    else right--;
}
```

---

## Prefix Sum

**Prefix Sum** stores cumulative sums for O(1) range sum queries on static arrays.

```java
prefix[0] = arr[0];
for (int i = 1; i < n; i++)
    prefix[i] = prefix[i-1] + arr[i];

// Sum from L to R
sum(L, R) = prefix[R] - prefix[L-1];  // L > 0
sum(0, R) = prefix[R];                 // L == 0
```

### Difference Array

Efficiently perform **range updates** in O(1), then rebuild array with prefix sum.

```java
diff[L] += val;
diff[R+1] -= val;
```

| Technique | Use Case | Update | Query |
|-----------|----------|--------|-------|
| Prefix Sum | Range sum queries | O(n) | O(1) |
| Difference Array | Range updates | O(1) | O(n) rebuild |

---

## Stack

A **stack** follows **LIFO** (Last In, First Out) — like a stack of plates.

### Operations (all O(1))

| Operation | Description |
|-----------|-------------|
| `push(x)` | Add to top |
| `pop()` | Remove and return top |
| `peek()` | View top without removing |
| `isEmpty()` | Check if empty |

### Applications

- Parentheses matching
- Undo operations
- Expression evaluation
- Function call stack (recursion)
- DFS traversal

```java
Stack<Integer> st = new Stack<>();
st.push(10);
st.push(20);
st.pop();   // 20
st.peek();  // 10
```

---

## Queue

A **queue** follows **FIFO** (First In, First Out) — like a line of people.

### Operations

| Operation | Description |
|-----------|-------------|
| `enqueue(x)` | Add at rear |
| `dequeue()` | Remove from front |
| `front()` | View front element |
| `isEmpty()` | Check if empty |

### Types

- **Linear Queue** — Simple FIFO
- **Circular Queue** — Reuses space efficiently

### Applications

- BFS traversal
- CPU scheduling
- Print queue
- Buffer for data streams

---

## Linked List

A **linked list** stores nodes in **non-contiguous** memory. Each node has **data** and a **pointer** to the next node.

### Types

| Type | Description |
|------|-------------|
| Singly Linked List | One pointer per node |
| Doubly Linked List | Next + previous pointers |
| Circular Linked List | Last node points to head |

### Operations

`create()`, `traverse()`, `insert_at_end(x)`, `insert_at_beg(x)`, `delete_at_beg()`, `delete_at_end()`, `search(key)`

### vs Array

| Linked List | Array |
|-------------|-------|
| Dynamic size | Fixed size |
| O(1) insert/delete at known position | O(1) random access |
| Extra pointer memory | Contiguous memory |
| No random access | Cache-friendly |

---

## Trees

A **tree** is a non-linear hierarchical structure with a **root** and parent-child relationships.

### Terminology

| Term | Definition |
|------|------------|
| Root | Topmost node |
| Parent / Child | Direct ancestor / descendant |
| Leaf | Node with no children |
| Degree | Number of children |
| Height | Max levels from root |
| Level | Distance from root (root = 0) |

### Binary Tree Types

- **Full** — 0 or 2 children per node
- **Complete** — All levels filled left-to-right except possibly last
- **Binary Search Tree** — Left < Node < Right

### Traversals

| Order | Sequence | Mnemonic |
|-------|----------|----------|
| Inorder | Left → Root → Right | LNR |
| Preorder | Root → Left → Right | NLR |
| Postorder | Left → Right → Root | LRN |

> A tree with n nodes has n - 1 edges.

---

## Binary Search Tree (BST)

A **BST** is a binary tree where for every node: **left subtree < node < right subtree**.

### Properties

- Inorder traversal gives **sorted** order
- No duplicate keys (typically)
- Search, Insert, Delete: **O(h)** where h = height

### Operations

```java
// Search
if (key == node.key) found;
else if (key < node.key) go left;
else go right;

// Delete cases: leaf, one child, two children
```

### Complexity

| Case | Time |
|------|------|
| Balanced BST | O(log n) |
| Skewed BST | O(n) |

> For guaranteed O(log n), use AVL or Red-Black trees.

---

## Heap and Priority Queue

A **heap** is a **complete binary tree** satisfying the heap property, used to implement **Priority Queue**.

### Types

| Type | Property | Root |
|------|----------|------|
| Max Heap | Parent ≥ children | Maximum |
| Min Heap | Parent ≤ children | Minimum |

### Array Representation

For index `i`: Left = `2i+1`, Right = `2i+2`, Parent = `(i-1)/2`

### Operations

| Operation | Time |
|-----------|------|
| Insert (heapify up) | O(log n) |
| Delete top (heapify down) | O(log n) |
| Peek top | O(1) |
| Build heap | O(n) |

### Applications

- Heap Sort, Dijkstra's algorithm, Huffman coding, Top-K elements, Task scheduling

---

## Graphs

A **graph** consists of **vertices** (nodes) connected by **edges**.

### Types

| Type | Description |
|------|-------------|
| Undirected | Edges have no direction |
| Directed (Digraph) | Edges have direction |
| Weighted | Edges have weights |

### Representations

| Method | Space | Best For |
|--------|-------|----------|
| Adjacency Matrix | O(V²) | Dense graphs |
| Adjacency List | O(V + E) | Sparse graphs |

### Traversals

| Algorithm | Strategy | Use |
|-----------|----------|-----|
| BFS | Level by level | Shortest path (unweighted), connected components |
| DFS | Go deep first | Cycle detection, topological sort, path finding |

### Key Algorithms

- **Dijkstra** — Shortest path (non-negative weights)
- **Kruskal / Prim** — Minimum Spanning Tree
- **Topological Sort** — DAG ordering

---

## Greedy Algorithms

At each step, choose the **locally optimal** choice hoping for a **global optimum**.

### When Greedy Works

- **Greedy Choice Property** — Local optimum leads to global optimum
- **Optimal Substructure** — Optimal solution contains optimal sub-solutions

### Classic Problems

| Problem | Greedy Strategy |
|---------|-----------------|
| Activity Selection | Pick earliest finishing activity |
| Fractional Knapsack | Take highest value/weight ratio |
| Huffman Coding | Merge lowest frequency nodes |
| Dijkstra | Pick closest unvisited vertex |
| Job Sequencing | Sort by profit/deadline |

### Trade-offs

| Pros | Cons |
|------|------|
| Simple, fast | Not always optimal |
| Low complexity | Needs correctness proof |

---

## Dynamic Programming

**DP** solves problems by breaking into overlapping subproblems, solving each once, and storing results.

### When to Use

- Overlapping subproblems
- Optimal substructure

### Approaches

| Approach | Method | Example |
|----------|--------|---------|
| Memoization (Top-Down) | Recursion + cache | Fibonacci with map |
| Tabulation (Bottom-Up) | Iterative table fill | Fibonacci with array |

```java
// Tabulation — Fibonacci O(n)
int[] dp = new int[n+1];
dp[0] = 0; dp[1] = 1;
for (int i = 2; i <= n; i++)
    dp[i] = dp[i-1] + dp[i-2];
```

### Classic Problems

Fibonacci, Climbing Stairs, Coin Change, 0/1 Knapsack, LCS, LIS, Matrix Chain Multiplication, Edit Distance

> Store once, use many times — turns exponential into polynomial.

---

## Backtracking

Explore all possibilities; **undo** (backtrack) when a path leads to a dead end.

### When to Use

- Need all possible solutions
- Constraint satisfaction problems
- When greedy fails

### Template

```java
void backtrack(state) {
    if (isComplete(state)) { record(state); return; }
    for (choice : choices(state)) {
        if (isValid(choice)) {
            make(choice);
            backtrack(newState);
            undo(choice);  // backtrack
        }
    }
}
```

### Examples

N-Queens, Sudoku, Rat in Maze, Subset Sum, Permutations, Combination Sum

---

## Interview Patterns and Tricks

### Problem-Solving Approach

1. Understand the problem thoroughly
2. Ask clarifying questions and examples
3. Think brute force first
4. Optimize — discuss trade-offs
5. Dry run with edge cases
6. State time and space complexity

### Common Patterns

| # | Pattern | Use When |
|---|---------|----------|
| 1 | Two Pointers | Sorted arrays, pairs |
| 2 | Sliding Window | Subarrays/substrings |
| 3 | Fast & Slow Pointers | Cycle detection, middle node |
| 4 | Binary Search | Sorted data, search space |
| 5 | DFS / BFS | Trees, graphs |
| 6 | Dynamic Programming | Overlapping subproblems |
| 7 | Backtracking | All combinations/permutations |
| 8 | Greedy | Local optimal → global |
| 9 | Heap | Top-K, priority processing |
| 10 | Prefix Sum | Range queries |

### Study Plan

1. Learn 1–2 patterns at a time
2. Solve easy → medium → hard
3. Revise and build templates
4. Quality over quantity

---

## Frequently Asked DSA Questions

### Arrays & Strings

| # | Problem |
|---|---------|
| 1 | Two Sum |
| 2 | Best Time to Buy & Sell Stock |
| 3 | Maximum Subarray (Kadane's) |
| 4 | Product of Array Except Self |
| 5 | Merge Intervals |
| 6 | Valid Anagram |
| 7 | Longest Substring Without Repeating Characters |
| 8 | Longest Palindromic Substring |

### Linked List, Stack, Queue

| # | Problem |
|---|---------|
| 1 | Reverse Linked List |
| 2 | Detect Cycle |
| 3 | Merge Two Sorted Lists |
| 4 | Valid Parentheses |
| 5 | Min Stack |
| 6 | Implement Queue using Stacks |

### Trees, Graphs, Heap

| # | Problem |
|---|---------|
| 1 | Inorder Traversal |
| 2 | Maximum Depth of Binary Tree |
| 3 | Validate BST |
| 4 | Number of Islands |
| 5 | Course Schedule (Topological Sort) |
| 6 | Kth Largest Element |
| 7 | Merge K Sorted Lists |

### DP, Greedy, Backtracking, Bit Manipulation

| # | Problem |
|---|---------|
| 1 | Climbing Stairs |
| 2 | Coin Change |
| 3 | House Robber |
| 4 | Activity Selection |
| 5 | Subsets / Permutations |
| 6 | N-Queens |
| 7 | Single Number |
| 8 | Missing Number |

---

## Tips and Conclusion

### Key Takeaways

- **Consistency beats talent** — practice daily
- **Understand > Memorize** — learn why, not just how
- DSA builds real problem-solving skills for interviews and production systems

### Mindset

- Break problems into smaller parts
- Analyze multiple solutions
- Discuss and learn with others
- Stay patient — every expert was once a beginner

> **Practice Today. Solve Tomorrow. Succeed Forever!**
