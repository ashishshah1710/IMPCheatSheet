# 🎯 DSA Cheat Sheet

**Quick Reference Guide**

---

## Time Complexities

| Data Structure | Access | Search | Insert | Delete |
|----------------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| Singly Linked List | O(n) | O(n) | O(1) | O(1) |
| Doubly Linked List | O(n) | O(n) | O(1) | O(1) |
| Hash Table | - | O(1) | O(1) | O(1) |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| Binary Tree | O(n) | O(n) | O(n) | O(n) |

---

## Sorting Algorithms

| Algorithm | Time (Avg) | Time (Worst) | Space | Stable |
|-----------|------------|--------------|-------|--------|
| Bubble Sort | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(1) | No |

---

## Common Patterns

### Two Pointers
```java
int left = 0, right = arr.length - 1;
while (left < right) {
    // Process
    if (condition) left++;
    else right--;
}
```

### Sliding Window
```java
int left = 0;
for (int right = 0; right < arr.length; right++) {
    // Expand window
    while (condition) {
        // Shrink window
        left++;
    }
}
```

### Binary Search
```java
int left = 0, right = arr.length - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
}
```

### DFS (Tree)
```java
void dfs(TreeNode root) {
    if (root == null) return;
    // Process root
    dfs(root.left);
    dfs(root.right);
}
```

### BFS (Tree)
```java
Queue<TreeNode> queue = new LinkedList<>();
queue.offer(root);
while (!queue.isEmpty()) {
    TreeNode node = queue.poll();
    // Process node
    if (node.left != null) queue.offer(node.left);
    if (node.right != null) queue.offer(node.right);
}
```

### DP Pattern
```java
// Tabulation
int[] dp = new int[n + 1];
dp[0] = base_case;
for (int i = 1; i <= n; i++) {
    dp[i] = // compute from previous states
}
```

---

## Must-Know Algorithms

### Binary Search
```java
public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

### Merge Sort
```java
public void mergeSort(int[] arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
```

### Quick Sort
```java
public void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

---

## Interview Checklist

### Before Interview
- [ ] Practice 2-3 problems daily
- [ ] Review time complexities
- [ ] Know all patterns
- [ ] Practice on whiteboard
- [ ] Mock interviews

### During Interview
- [ ] Ask clarifying questions
- [ ] Discuss approach before coding
- [ ] Think out loud
- [ ] Test with examples
- [ ] Optimize if asked

### After Coding
- [ ] Test with edge cases
- [ ] Analyze time/space complexity
- [ ] Discuss trade-offs
- [ ] Suggest optimizations

---

**Happy Coding! 🎯**

