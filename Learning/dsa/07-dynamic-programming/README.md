# 💎 Dynamic Programming

**Phase 7: Optimization Technique (2-3 Weeks)**

---

## 📖 Overview

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It's crucial for optimization problems and appears in 20% of technical interviews.

---

## 🎯 Core Concepts

### When to Use DP?

1. **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
2. **Overlapping Subproblems**: Same subproblems solved multiple times

### Two Approaches

1. **Memoization (Top-Down)**: Recursion + caching
2. **Tabulation (Bottom-Up)**: Iterative approach

---

## 📚 Classic DP Problems

### 1. Fibonacci

**Recursive (Exponential):**
```java
public int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
// Time: O(2^n), Space: O(n)
```

**Memoization (Top-Down):**
```java
public int fib(int n) {
    return fibHelper(n, new int[n + 1]);
}

private int fibHelper(int n, int[] memo) {
    if (n <= 1) return n;
    if (memo[n] != 0) return memo[n];
    
    memo[n] = fibHelper(n - 1, memo) + fibHelper(n - 2, memo);
    return memo[n];
}
// Time: O(n), Space: O(n)
```

**Tabulation (Bottom-Up):**
```java
public int fib(int n) {
    if (n <= 1) return n;
    
    int[] dp = new int[n + 1];
    dp[0] = 0;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    
    return dp[n];
}
// Time: O(n), Space: O(n)
```

**Space Optimized:**
```java
public int fib(int n) {
    if (n <= 1) return n;
    
    int prev = 0, curr = 1;
    
    for (int i = 2; i <= n; i++) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
    
    return curr;
}
// Time: O(n), Space: O(1)
```

---

### 2. Climbing Stairs

**Problem:** You can climb 1 or 2 steps. How many ways to reach top?

```java
public int climbStairs(int n) {
    if (n <= 2) return n;
    
    int prev = 1, curr = 2;
    
    for (int i = 3; i <= n; i++) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
    
    return curr;
}
```

---

### 3. Coin Change

**Problem:** Minimum coins to make amount

```java
public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    
    return dp[amount] > amount ? -1 : dp[amount];
}
```

---

### 4. Longest Common Subsequence (LCS)

```java
public int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length(), n = text2.length();
    int[][] dp = new int[m + 1][n + 1];
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    return dp[m][n];
}
```

---

### 5. 0/1 Knapsack

```java
public int knapsack(int[] weights, int[] values, int capacity) {
    int n = weights.length;
    int[][] dp = new int[n + 1][capacity + 1];
    
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = Math.max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    
    return dp[n][capacity];
}
```

---

### 6. Longest Increasing Subsequence (LIS)

```java
public int lengthOfLIS(int[] nums) {
    int[] dp = new int[nums.length];
    Arrays.fill(dp, 1);
    
    for (int i = 1; i < nums.length; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }
    
    return Arrays.stream(dp).max().getAsInt();
}
// Time: O(n²), Space: O(n)
```

---

## 🎯 DP Patterns

### Pattern 1: Fibonacci-Like
- Climbing Stairs
- House Robber
- Decode Ways

### Pattern 2: 0/1 Knapsack
- Subset Sum
- Partition Equal Subset Sum
- Target Sum

### Pattern 3: Unbounded Knapsack
- Coin Change
- Coin Change 2
- Minimum Cost for Tickets

### Pattern 4: LCS
- Longest Common Subsequence
- Edit Distance
- Minimum ASCII Delete Sum

### Pattern 5: LIS
- Longest Increasing Subsequence
- Russian Doll Envelopes
- Maximum Length of Pair Chain

### Pattern 6: Palindrome
- Longest Palindromic Substring
- Palindromic Substrings
- Longest Palindromic Subsequence

---

## 🎯 Top 30 DP Problems

### Easy
1. Climbing Stairs
2. House Robber
3. Maximum Subarray
4. Best Time to Buy and Sell Stock
5. Min Cost Climbing Stairs

### Medium
6. Coin Change
7. Longest Increasing Subsequence
8. Longest Common Subsequence
9. Word Break
10. Unique Paths
11. House Robber II
12. Decode Ways
13. Partition Equal Subset Sum
14. Target Sum
15. Perfect Squares
16. Combination Sum IV
17. Triangle
18. Maximum Product Subarray
19. Longest Palindromic Substring
20. Palindromic Substrings
21. Minimum Path Sum
22. Unique Binary Search Trees
23. Jump Game
24. Maximal Square

### Hard
25. Edit Distance
26. Regular Expression Matching
27. Wildcard Matching
28. Longest Valid Parentheses
29. Maximal Rectangle
30. Burst Balloons

---

## ✅ Practice Checklist

- [ ] Master Fibonacci pattern (5 problems)
- [ ] Solve 0/1 Knapsack problems (5 problems)
- [ ] Practice LCS problems (5 problems)
- [ ] Work on LIS problems (5 problems)
- [ ] Solve palindrome problems (5 problems)
- [ ] Practice state machine DP (5 problems)
- [ ] Solve at least 30 DP problems total

---

**👉 Next:** [Advanced Topics →](../08-advanced-topics/README.md)

---

**💡 Pro Tip:** DP is hard! Start with easy problems, identify patterns, and gradually progress. Don't get discouraged!

