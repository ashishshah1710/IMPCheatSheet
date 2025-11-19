# 🎯 Problem-Solving Patterns

## Overview
Master these 15 coding patterns to solve 90% of interview questions. Each pattern is a template you can apply to multiple problems.

---

## Pattern 1: Sliding Window

### When to Use
- Contiguous subarrays or sublists
- Finding longest/shortest substring
- Maximum/minimum sum of subarray
- **Keywords**: contiguous, substring, subarray, window

### Template
```java
int slidingWindow(int[] arr, int k) {
    int windowSum = 0, maxSum = 0;
    int windowStart = 0;
    
    for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        windowSum += arr[windowEnd]; // Add to window
        
        // Slide the window if size > k
        if (windowEnd >= k - 1) {
            maxSum = Math.max(maxSum, windowSum);
            windowSum -= arr[windowStart]; // Remove from window
            windowStart++; // Slide window ahead
        }
    }
    return maxSum;
}
```

### Problems
1. Maximum Sum Subarray of Size K
2. Longest Substring Without Repeating Characters
3. Fruits Into Baskets
4. Minimum Window Substring
5. Longest Substring with K Distinct Characters

---

## Pattern 2: Two Pointers

### When to Use
- Sorted arrays or linked lists
- Finding pairs with target sum
- Reversing or comparing sequences
- **Keywords**: sorted, pairs, opposite ends

### Template
```java
int[] twoPointers(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    
    while (left < right) {
        int sum = arr[left] + arr[right];
        
        if (sum == target) {
            return new int[]{left, right};
        } else if (sum < target) {
            left++; // Need larger sum
        } else {
            right--; // Need smaller sum
        }
    }
    return new int[]{-1, -1};
}
```

### Problems
1. Two Sum II (Sorted)
2. Remove Duplicates from Sorted Array
3. Squaring a Sorted Array
4. 3Sum
5. Container With Most Water

---

## Pattern 3: Fast & Slow Pointers

### When to Use
- Linked list cycle detection
- Finding middle element
- Palindrome checking
- **Keywords**: cycle, middle, linked list

### Template
```java
boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    
    while (fast != null && fast.next != null) {
        slow = slow.next;          // Move 1 step
        fast = fast.next.next;     // Move 2 steps
        
        if (slow == fast) {
            return true; // Cycle detected
        }
    }
    return false;
}

ListNode findMiddle(ListNode head) {
    ListNode slow = head, fast = head;
    
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow; // Middle element
}
```

### Problems
1. Linked List Cycle
2. Start of Linked List Cycle
3. Happy Number
4. Middle of the Linked List
5. Palindrome Linked List

---

## Pattern 4: Merge Intervals

### When to Use
- Overlapping intervals
- Scheduling problems
- **Keywords**: intervals, overlapping, merge, ranges

### Template
```java
List<int[]> mergeIntervals(int[][] intervals) {
    if (intervals.length == 0) return new ArrayList<>();
    
    // Sort by start time
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    
    List<int[]> merged = new ArrayList<>();
    int[] current = intervals[0];
    
    for (int i = 1; i < intervals.length; i++) {
        if (current[1] >= intervals[i][0]) {
            // Overlapping - merge
            current[1] = Math.max(current[1], intervals[i][1]);
        } else {
            // Non-overlapping - add current
            merged.add(current);
            current = intervals[i];
        }
    }
    merged.add(current);
    return merged;
}
```

### Problems
1. Merge Intervals
2. Insert Interval
3. Interval List Intersections
4. Meeting Rooms II
5. Employee Free Time

---

## Pattern 5: Cyclic Sort

### When to Use
- Array contains numbers from 1 to n
- Finding missing/duplicate numbers
- **Keywords**: 1 to n, missing, duplicate, in-place

### Template
```java
void cyclicSort(int[] nums) {
    int i = 0;
    while (i < nums.length) {
        int correctIdx = nums[i] - 1;
        
        if (nums[i] != nums[correctIdx]) {
            // Swap to correct position
            swap(nums, i, correctIdx);
        } else {
            i++;
        }
    }
}
```

### Problems
1. Find the Missing Number
2. Find All Missing Numbers
3. Find the Duplicate Number
4. Find All Duplicates
5. First Missing Positive

---

## Pattern 6: In-place Reversal of Linked List

### When to Use
- Reversing linked list or part of it
- **Keywords**: reverse, linked list, in-place

### Template
```java
ListNode reverse(ListNode head) {
    ListNode prev = null, current = head;
    
    while (current != null) {
        ListNode next = current.next;
        current.next = prev; // Reverse link
        prev = current;
        current = next;
    }
    return prev;
}

ListNode reverseBetween(ListNode head, int left, int right) {
    if (head == null || left == right) return head;
    
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode prev = dummy;
    
    // Move to position
    for (int i = 0; i < left - 1; i++) {
        prev = prev.next;
    }
    
    // Reverse sublist
    ListNode current = prev.next;
    for (int i = 0; i < right - left; i++) {
        ListNode next = current.next;
        current.next = next.next;
        next.next = prev.next;
        prev.next = next;
    }
    
    return dummy.next;
}
```

### Problems
1. Reverse Linked List
2. Reverse Linked List II
3. Reverse Nodes in k-Group
4. Rotate List

---

## Pattern 7: Tree BFS (Level Order Traversal)

### When to Use
- Level-by-level tree traversal
- Finding depth/width of tree
- **Keywords**: level, breadth-first, layer

### Template
```java
List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    while (!queue.isEmpty()) {
        int levelSize = queue.size();
        List<Integer> currentLevel = new ArrayList<>();
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode node = queue.poll();
            currentLevel.add(node.val);
            
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        
        result.add(currentLevel);
    }
    return result;
}
```

### Problems
1. Binary Tree Level Order Traversal
2. Zigzag Traversal
3. Level Averages in Binary Tree
4. Minimum Depth of Binary Tree
5. Right View of Binary Tree

---

## Pattern 8: Tree DFS (Depth First Search)

### When to Use
- Path-related problems in trees
- Finding depth/height
- **Keywords**: path, root to leaf, depth

### Template
```java
// Preorder: Root → Left → Right
void preorder(TreeNode root) {
    if (root == null) return;
    visit(root);
    preorder(root.left);
    preorder(root.right);
}

// Inorder: Left → Root → Right
void inorder(TreeNode root) {
    if (root == null) return;
    inorder(root.left);
    visit(root);
    inorder(root.right);
}

// Postorder: Left → Right → Root
void postorder(TreeNode root) {
    if (root == null) return;
    postorder(root.left);
    postorder(root.right);
    visit(root);
}

// Path sum
boolean hasPathSum(TreeNode root, int targetSum) {
    if (root == null) return false;
    if (root.left == null && root.right == null) {
        return targetSum == root.val;
    }
    return hasPathSum(root.left, targetSum - root.val) ||
           hasPathSum(root.right, targetSum - root.val);
}
```

### Problems
1. Path Sum
2. All Paths for a Sum
3. Sum of Path Numbers
4. Path With Given Sequence
5. Binary Tree Maximum Path Sum

---

## Pattern 9: Two Heaps

### When to Use
- Finding median of stream
- Balancing two parts of dataset
- **Keywords**: median, middle value, streaming data

### Template
```java
class MedianFinder {
    PriorityQueue<Integer> maxHeap; // Left half
    PriorityQueue<Integer> minHeap; // Right half
    
    public MedianFinder() {
        maxHeap = new PriorityQueue<>((a, b) -> b - a); // Max heap
        minHeap = new PriorityQueue<>(); // Min heap
    }
    
    public void addNum(int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.offer(num);
        } else {
            minHeap.offer(num);
        }
        
        // Balance heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }
    
    public double findMedian() {
        if (maxHeap.size() == minHeap.size()) {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
        return maxHeap.peek();
    }
}
```

### Problems
1. Find Median from Data Stream
2. Sliding Window Median
3. IPO
4. Next Interval

---

## Pattern 10: Subsets

### When to Use
- Finding all combinations/permutations
- Backtracking problems
- **Keywords**: combinations, permutations, subsets

### Template
```java
// Subsets
List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(result, new ArrayList<>(), nums, 0);
    return result;
}

void backtrack(List<List<Integer>> result, List<Integer> temp, 
               int[] nums, int start) {
    result.add(new ArrayList<>(temp));
    
    for (int i = start; i < nums.length; i++) {
        temp.add(nums[i]);
        backtrack(result, temp, nums, i + 1);
        temp.remove(temp.size() - 1); // Backtrack
    }
}

// Permutations
List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    backtrackPerm(result, new ArrayList<>(), nums);
    return result;
}

void backtrackPerm(List<List<Integer>> result, List<Integer> temp, int[] nums) {
    if (temp.size() == nums.length) {
        result.add(new ArrayList<>(temp));
        return;
    }
    
    for (int num : nums) {
        if (temp.contains(num)) continue; // Skip used
        temp.add(num);
        backtrackPerm(result, temp, nums);
        temp.remove(temp.size() - 1); // Backtrack
    }
}
```

### Problems
1. Subsets
2. Subsets II (with duplicates)
3. Permutations
4. Combinations
5. Generate Parentheses

---

## Pattern 11: Modified Binary Search

### When to Use
- Sorted or rotated arrays
- Finding peak/valley
- **Keywords**: sorted, rotated, binary search

### Template
```java
int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
```

### Problems
1. Binary Search
2. Search in Rotated Sorted Array
3. Find Peak Element
4. Search in 2D Matrix
5. Time Based Key-Value Store

---

## Pattern 12: Top K Elements

### When to Use
- Finding K largest/smallest elements
- Frequency-based problems
- **Keywords**: top K, Kth largest, most frequent

### Template
```java
int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    
    for (int num : nums) {
        minHeap.offer(num);
        if (minHeap.size() > k) {
            minHeap.poll(); // Remove smallest
        }
    }
    
    return minHeap.peek();
}
```

### Problems
1. Kth Largest Element
2. Top K Frequent Elements
3. K Closest Points to Origin
4. Kth Smallest Element in Sorted Matrix

---

## Pattern 13: K-way Merge

### When to Use
- Merging K sorted arrays/lists
- **Keywords**: K sorted, merge

### Template
```java
ListNode mergeKLists(ListNode[] lists) {
    PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
    
    // Add first node of each list
    for (ListNode list : lists) {
        if (list != null) pq.offer(list);
    }
    
    ListNode dummy = new ListNode(0);
    ListNode tail = dummy;
    
    while (!pq.isEmpty()) {
        ListNode node = pq.poll();
        tail.next = node;
        tail = tail.next;
        
        if (node.next != null) {
            pq.offer(node.next);
        }
    }
    
    return dummy.next;
}
```

### Problems
1. Merge K Sorted Lists
2. Kth Smallest Number in M Sorted Lists
3. Smallest Range Covering Elements from K Lists

---

## Pattern 14: 0/1 Knapsack (Dynamic Programming)

### When to Use
- Subset sum problems
- Partition problems
- **Keywords**: subset, partition, capacity, optimize

### Template
```java
int knapsack(int[] weights, int[] values, int capacity) {
    int n = weights.length;
    int[][] dp = new int[n + 1][capacity + 1];
    
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i-1] <= w) {
                // Include or exclude
                dp[i][w] = Math.max(
                    values[i-1] + dp[i-1][w - weights[i-1]], // Include
                    dp[i-1][w] // Exclude
                );
            } else {
                dp[i][w] = dp[i-1][w]; // Can't include
            }
        }
    }
    
    return dp[n][capacity];
}
```

### Problems
1. 0/1 Knapsack
2. Equal Subset Sum Partition
3. Subset Sum
4. Target Sum
5. Minimum Subset Sum Difference

---

## Pattern 15: Topological Sort (Graph)

### When to Use
- Dependency resolution
- Task scheduling with prerequisites
- **Keywords**: dependencies, order, prerequisites, DAG

### Template
```java
List<Integer> topologicalSort(int n, int[][] edges) {
    List<Integer> result = new ArrayList<>();
    Map<Integer, List<Integer>> graph = new HashMap<>();
    int[] indegree = new int[n];
    
    // Build graph
    for (int[] edge : edges) {
        graph.putIfAbsent(edge[0], new ArrayList<>());
        graph.get(edge[0]).add(edge[1]);
        indegree[edge[1]]++;
    }
    
    // Add nodes with 0 indegree
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) queue.offer(i);
    }
    
    // Process nodes
    while (!queue.isEmpty()) {
        int node = queue.poll();
        result.add(node);
        
        if (graph.containsKey(node)) {
            for (int neighbor : graph.get(node)) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
    }
    
    return result.size() == n ? result : new ArrayList<>();
}
```

### Problems
1. Course Schedule
2. Course Schedule II
3. Alien Dictionary
4. Minimum Height Trees
5. Sequence Reconstruction

---

## 🎯 Pattern Selection Guide

| Problem Type | Use Pattern |
|--------------|-------------|
| Contiguous subarray | Sliding Window |
| Sorted array, pairs | Two Pointers |
| Linked list cycle | Fast & Slow Pointers |
| Intervals | Merge Intervals |
| Array 1 to n | Cyclic Sort |
| Reverse linked list | In-place Reversal |
| Tree levels | Tree BFS |
| Tree paths | Tree DFS |
| Median/balancing | Two Heaps |
| All combinations | Subsets/Backtracking |
| Modified search | Binary Search |
| K largest/smallest | Top K / Heap |
| Merge sorted | K-way Merge |
| Subset sum | 0/1 Knapsack |
| Dependencies | Topological Sort |

---

## 💡 How to Practice

1. **Master one pattern at a time**
2. **Solve 5-10 problems per pattern**
3. **Recognize patterns in new problems**
4. **Mix patterns in later stages**
5. **Time yourself (30-45 min per problem)**

---

**💡 Pro Tip**: Once you master these 15 patterns, you'll be able to solve most interview questions by pattern recognition!

