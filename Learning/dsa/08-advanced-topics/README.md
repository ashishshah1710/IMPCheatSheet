# 🚀 Advanced Topics in DSA

## Overview
This section covers advanced data structures and algorithms frequently asked in senior-level interviews at top tech companies (FAANG).

---

## 🔹 ADVANCED DATA STRUCTURES

### 1. **Trie (Prefix Tree)**
```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEndOfWord;
}

class Trie {
    TrieNode root = new TrieNode();
    
    // Insert word
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEndOfWord = true;
    }
    
    // Search word
    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEndOfWord;
    }
    
    // Check if prefix exists
    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }
    
    private TrieNode searchPrefix(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) return null;
            node = node.children[idx];
        }
        return node;
    }
}
```
**Time**: O(m) for all operations (m = word length)  
**Space**: O(ALPHABET_SIZE × N × M)  
**Use Cases**: Autocomplete, spell checker, IP routing

### 2. **Segment Tree**
```java
class SegmentTree {
    int[] tree;
    int n;
    
    public SegmentTree(int[] arr) {
        n = arr.length;
        tree = new int[4 * n];
        build(arr, 0, 0, n - 1);
    }
    
    private void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return;
        }
        int mid = start + (end - start) / 2;
        build(arr, 2 * node + 1, start, mid);
        build(arr, 2 * node + 2, mid + 1, end);
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }
    
    // Range sum query
    public int query(int l, int r) {
        return query(0, 0, n - 1, l, r);
    }
    
    private int query(int node, int start, int end, int l, int r) {
        if (r < start || l > end) return 0;
        if (l <= start && end <= r) return tree[node];
        
        int mid = start + (end - start) / 2;
        int leftSum = query(2 * node + 1, start, mid, l, r);
        int rightSum = query(2 * node + 2, mid + 1, end, l, r);
        return leftSum + rightSum;
    }
    
    // Point update
    public void update(int idx, int val) {
        update(0, 0, n - 1, idx, val);
    }
    
    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            update(2 * node + 1, start, mid, idx, val);
        } else {
            update(2 * node + 2, mid + 1, end, idx, val);
        }
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }
}
```
**Time**: Build O(n), Query/Update O(log n)  
**Use Cases**: Range queries, dynamic programming optimization

### 3. **Fenwick Tree (Binary Indexed Tree)**
```java
class FenwickTree {
    int[] tree;
    int n;
    
    public FenwickTree(int n) {
        this.n = n;
        tree = new int[n + 1];
    }
    
    // Add value at index
    public void update(int idx, int delta) {
        idx++; // 1-indexed
        while (idx <= n) {
            tree[idx] += delta;
            idx += idx & (-idx);
        }
    }
    
    // Prefix sum [1...idx]
    public int query(int idx) {
        idx++; // 1-indexed
        int sum = 0;
        while (idx > 0) {
            sum += tree[idx];
            idx -= idx & (-idx);
        }
        return sum;
    }
    
    // Range sum [l...r]
    public int rangeQuery(int l, int r) {
        return query(r) - (l > 0 ? query(l - 1) : 0);
    }
}
```
**Time**: Update/Query O(log n)  
**Space**: O(n)  
**Use Cases**: Cumulative frequency, range sum queries

### 4. **Disjoint Set Union (Union-Find)**
```java
class DSU {
    int[] parent, rank;
    int components;
    
    public DSU(int n) {
        parent = new int[n];
        rank = new int[n];
        components = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    // Find with path compression
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    // Union by rank
    public boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        
        if (rank[px] < rank[py]) {
            parent[px] = py;
        } else if (rank[px] > rank[py]) {
            parent[py] = px;
        } else {
            parent[py] = px;
            rank[px]++;
        }
        components--;
        return true;
    }
    
    public boolean connected(int x, int y) {
        return find(x) == find(y);
    }
}
```
**Time**: Almost O(1) with path compression (α(n) - inverse Ackermann)  
**Use Cases**: Cycle detection, Kruskal's MST, network connectivity

### 5. **Suffix Array & LCP**
```java
class SuffixArray {
    String s;
    int n;
    int[] sa, lcp;
    
    public SuffixArray(String s) {
        this.s = s + "$"; // Add sentinel
        this.n = this.s.length();
        buildSuffixArray();
        buildLCP();
    }
    
    private void buildSuffixArray() {
        Integer[] suffixes = new Integer[n];
        for (int i = 0; i < n; i++) suffixes[i] = i;
        
        Arrays.sort(suffixes, (a, b) -> s.substring(a).compareTo(s.substring(b)));
        
        sa = new int[n];
        for (int i = 0; i < n; i++) sa[i] = suffixes[i];
    }
    
    private void buildLCP() {
        lcp = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) rank[sa[i]] = i;
        
        int h = 0;
        for (int i = 0; i < n; i++) {
            if (rank[i] > 0) {
                int j = sa[rank[i] - 1];
                while (i + h < n && j + h < n && s.charAt(i + h) == s.charAt(j + h)) {
                    h++;
                }
                lcp[rank[i]] = h;
                if (h > 0) h--;
            }
        }
    }
}
```
**Use Cases**: Pattern matching, longest repeated substring

---

## 🔹 ADVANCED ALGORITHMS

### 6. **KMP (Knuth-Morris-Pratt) Pattern Matching**
```java
class KMP {
    public int[] computeLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        
        for (int i = 1; i < m; ) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                lps[i++] = ++len;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i++] = 0;
                }
            }
        }
        return lps;
    }
    
    public List<Integer> search(String text, String pattern) {
        List<Integer> result = new ArrayList<>();
        int n = text.length(), m = pattern.length();
        int[] lps = computeLPS(pattern);
        
        int i = 0, j = 0;
        while (i < n) {
            if (text.charAt(i) == pattern.charAt(j)) {
                i++; j++;
            }
            if (j == m) {
                result.add(i - j);
                j = lps[j - 1];
            } else if (i < n && text.charAt(i) != pattern.charAt(j)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return result;
    }
}
```
**Time**: O(n + m)  
**Use Cases**: String matching, text search

### 7. **Rabin-Karp Algorithm**
```java
class RabinKarp {
    private static final int D = 256; // Number of characters
    private static final int Q = 101; // Prime number
    
    public List<Integer> search(String text, String pattern) {
        List<Integer> result = new ArrayList<>();
        int n = text.length(), m = pattern.length();
        int h = 1;
        
        // Calculate h = D^(m-1) % Q
        for (int i = 0; i < m - 1; i++) {
            h = (h * D) % Q;
        }
        
        // Calculate hash for pattern and first window
        int patHash = 0, txtHash = 0;
        for (int i = 0; i < m; i++) {
            patHash = (D * patHash + pattern.charAt(i)) % Q;
            txtHash = (D * txtHash + text.charAt(i)) % Q;
        }
        
        // Slide pattern over text
        for (int i = 0; i <= n - m; i++) {
            if (patHash == txtHash) {
                // Check character by character
                if (text.substring(i, i + m).equals(pattern)) {
                    result.add(i);
                }
            }
            
            if (i < n - m) {
                txtHash = (D * (txtHash - text.charAt(i) * h) + text.charAt(i + m)) % Q;
                if (txtHash < 0) txtHash += Q;
            }
        }
        return result;
    }
}
```
**Time**: O(n + m) average, O(nm) worst  
**Use Cases**: Multiple pattern search, plagiarism detection

### 8. **Manacher's Algorithm** (Longest Palindromic Substring)
```java
String longestPalindrome(String s) {
    if (s == null || s.length() == 0) return "";
    
    // Preprocess: "abc" -> "#a#b#c#"
    StringBuilder sb = new StringBuilder();
    sb.append('#');
    for (char c : s.toCharArray()) {
        sb.append(c).append('#');
    }
    String t = sb.toString();
    
    int n = t.length();
    int[] p = new int[n]; // p[i] = radius of palindrome centered at i
    int center = 0, right = 0;
    
    for (int i = 0; i < n; i++) {
        int mirror = 2 * center - i;
        
        if (i < right) {
            p[i] = Math.min(right - i, p[mirror]);
        }
        
        // Expand around i
        while (i - p[i] - 1 >= 0 && i + p[i] + 1 < n &&
               t.charAt(i - p[i] - 1) == t.charAt(i + p[i] + 1)) {
            p[i]++;
        }
        
        // Update center and right
        if (i + p[i] > right) {
            center = i;
            right = i + p[i];
        }
    }
    
    // Find longest palindrome
    int maxLen = 0, centerIdx = 0;
    for (int i = 0; i < n; i++) {
        if (p[i] > maxLen) {
            maxLen = p[i];
            centerIdx = i;
        }
    }
    
    int start = (centerIdx - maxLen) / 2;
    return s.substring(start, start + maxLen);
}
```
**Time**: O(n)

### 9. **A* Search Algorithm**
```java
class AStarNode implements Comparable<AStarNode> {
    int x, y;
    int g, h; // g = cost from start, h = heuristic to goal
    
    public int compareTo(AStarNode other) {
        return (this.g + this.h) - (other.g + other.h);
    }
}

List<int[]> aStar(int[][] grid, int[] start, int[] goal) {
    PriorityQueue<AStarNode> pq = new PriorityQueue<>();
    // Implementation similar to Dijkstra with heuristic
    // Common heuristics: Manhattan, Euclidean distance
    return new ArrayList<>(); // Path from start to goal
}
```
**Use Cases**: Pathfinding in games, GPS navigation

### 10. **Heavy-Light Decomposition**
Advanced tree technique for efficient path queries

### 11. **Convex Hull (Graham Scan)**
```java
class Point {
    int x, y;
    Point(int x, int y) { this.x = x; this.y = y; }
}

List<Point> convexHull(Point[] points) {
    Arrays.sort(points, (a, b) -> a.x != b.x ? a.x - b.x : a.y - b.y);
    
    List<Point> hull = new ArrayList<>();
    
    // Build lower hull
    for (Point p : points) {
        while (hull.size() >= 2 && ccw(hull.get(hull.size()-2), 
                                       hull.get(hull.size()-1), p) <= 0) {
            hull.remove(hull.size() - 1);
        }
        hull.add(p);
    }
    
    // Build upper hull
    int lowerSize = hull.size();
    for (int i = points.length - 2; i >= 0; i--) {
        Point p = points[i];
        while (hull.size() > lowerSize && ccw(hull.get(hull.size()-2),
                                               hull.get(hull.size()-1), p) <= 0) {
            hull.remove(hull.size() - 1);
        }
        hull.add(p);
    }
    
    hull.remove(hull.size() - 1);
    return hull;
}

int ccw(Point a, Point b, Point c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}
```

---

## Practice Problems

### Trie
1. 🔥 Implement Trie
2. 🔥 Word Search II
3. 💪 Design Add and Search Words Data Structure

### Segment Tree / BIT
4. 🔥 Range Sum Query - Mutable
5. 💪 Count of Smaller Numbers After Self
6. 💪 Reverse Pairs

### Union-Find
7. 🔥 Number of Islands II
8. 🔥 Accounts Merge
9. 💪 Swim in Rising Water

### String Algorithms
10. 🔥 Implement strStr() (KMP)
11. 💪 Shortest Palindrome (KMP/Manacher)
12. 💪 Repeated DNA Sequences (Rabin-Karp)

### Geometry
13. 🔥 Convex Hull
14. 💪 Line Reflection

## Complexity Cheat Sheet

| Data Structure | Operation | Time |
|----------------|-----------|------|
| **Trie** | Insert/Search | O(m) |
| **Segment Tree** | Build | O(n) |
| **Segment Tree** | Query/Update | O(log n) |
| **Fenwick Tree** | Query/Update | O(log n) |
| **Union-Find** | Find/Union | O(α(n)) ≈ O(1) |
| **KMP** | Pattern search | O(n+m) |
| **Rabin-Karp** | Pattern search | O(n+m) avg |

## Interview Tips

1. **Know when to use advanced DS**: Don't over-engineer
2. **Trie for strings**: Prefix matching, autocomplete
3. **Segment Tree**: Range queries with updates
4. **Union-Find**: Connectivity, grouping
5. **String algorithms**: Pattern matching optimization

## Real-World Applications

- **Trie**: Autocomplete, IP routing, spell check
- **Segment Tree**: Database range queries, computational geometry
- **Union-Find**: Network connectivity, image processing (connected components)
- **KMP**: Text editors, virus scanning
- **A***: GPS navigation, game AI

## Next Steps

- **Practice on**: LeetCode Hard, Codeforces
- **System Design** → [system-design](../../system-design/README.md)
- **Interview Prep** → [interview-questions](../interview-questions/README.md)

---

**💡 Pro Tip**: These topics separate mid-level from senior engineers in interviews. Master at least 3-4 of these for FAANG!

