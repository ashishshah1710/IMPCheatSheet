# 📊 Arrays & Strings

**Phase 1: Foundation (1-2 Weeks)**

---

## 📖 Overview

Arrays and Strings are the most fundamental data structures. Mastering them is crucial as they appear in 30-40% of coding interviews.

---

## 🎯 Learning Objectives

✅ Array operations and manipulations  
✅ Two pointers technique  
✅ Sliding window pattern  
✅ String algorithms  
✅ Pattern matching  
✅ Common problem patterns  

---

## 📚 Core Topics

### 1. Array Basics

**Time Complexities:**
- Access: O(1)
- Search: O(n)
- Insert: O(n)
- Delete: O(n)

**Common Operations:**

```java
// Initialize array
int[] arr = new int[5];
int[] arr = {1, 2, 3, 4, 5};

// Access
int element = arr[0];

// Modify
arr[0] = 10;

// Iterate
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}

// For-each
for (int num : arr) {
    System.out.println(num);
}
```

---

### 2. Two Pointers Technique

**When to Use:**
- Searching pairs in sorted array
- Reversing array/string
- Removing duplicates
- Merging arrays

**Pattern:**

```java
// Opposite direction pointers
int left = 0, right = arr.length - 1;
while (left < right) {
    // Process
    if (condition) {
        left++;
    } else {
        right--;
    }
}

// Same direction pointers
int slow = 0, fast = 0;
while (fast < arr.length) {
    // Process
    if (condition) {
        // Move slow
        slow++;
    }
    fast++;
}
```

**Example Problems:**

**1. Two Sum (Sorted Array)**
```java
public int[] twoSum(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    
    while (left < right) {
        int sum = arr[left] + arr[right];
        
        if (sum == target) {
            return new int[]{left, right};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    return new int[]{-1, -1};
}
```

**2. Remove Duplicates**
```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    
    int slow = 0;
    for (int fast = 1; fast < nums.length; fast++) {
        if (nums[fast] != nums[slow]) {
            slow++;
            nums[slow] = nums[fast];
        }
    }
    
    return slow + 1;
}
```

**3. Reverse String**
```java
public void reverseString(char[] s) {
    int left = 0, right = s.length - 1;
    
    while (left < right) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
}
```

---

### 3. Sliding Window

**When to Use:**
- Subarray/substring problems
- Maximum/minimum in window
- Fixed or variable window size

**Fixed Window Pattern:**

```java
public int maxSumSubarray(int[] arr, int k) {
    int windowSum = 0;
    
    // Calculate first window
    for (int i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    
    int maxSum = windowSum;
    
    // Slide the window
    for (int i = k; i < arr.length; i++) {
        windowSum = windowSum - arr[i - k] + arr[i];
        maxSum = Math.max(maxSum, windowSum);
    }
    
    return maxSum;
}
```

**Variable Window Pattern:**

```java
public int lengthOfLongestSubstring(String s) {
    Set<Character> set = new HashSet<>();
    int left = 0, maxLen = 0;
    
    for (int right = 0; right < s.length(); right++) {
        // Shrink window if duplicate
        while (set.contains(s.charAt(right))) {
            set.remove(s.charAt(left));
            left++;
        }
        
        set.add(s.charAt(right));
        maxLen = Math.max(maxLen, right - left + 1);
    }
    
    return maxLen;
}
```

**Example Problems:**

**1. Maximum Sum Subarray of Size K**
```java
public int maxSumSubarray(int[] arr, int k) {
    int windowSum = 0, maxSum = Integer.MIN_VALUE;
    
    for (int i = 0; i < arr.length; i++) {
        windowSum += arr[i];
        
        if (i >= k - 1) {
            maxSum = Math.max(maxSum, windowSum);
            windowSum -= arr[i - k + 1];
        }
    }
    
    return maxSum;
}
```

**2. Minimum Window Substring**
```java
public String minWindow(String s, String t) {
    if (s.length() < t.length()) return "";
    
    Map<Character, Integer> map = new HashMap<>();
    for (char c : t.toCharArray()) {
        map.put(c, map.getOrDefault(c, 0) + 1);
    }
    
    int left = 0, minLen = Integer.MAX_VALUE;
    int minStart = 0, count = t.length();
    
    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        
        if (map.containsKey(c)) {
            if (map.get(c) > 0) count--;
            map.put(c, map.get(c) - 1);
        }
        
        while (count == 0) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }
            
            char leftChar = s.charAt(left);
            if (map.containsKey(leftChar)) {
                map.put(leftChar, map.get(leftChar) + 1);
                if (map.get(leftChar) > 0) count++;
            }
            left++;
        }
    }
    
    return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
}
```

---

### 4. Common Array Problems

**1. Rotate Array**
```java
public void rotate(int[] nums, int k) {
    k = k % nums.length;
    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);
}

private void reverse(int[] nums, int start, int end) {
    while (start < end) {
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}
```

**2. Maximum Subarray (Kadane's Algorithm)**
```java
public int maxSubArray(int[] nums) {
    int maxSum = nums[0];
    int currentSum = nums[0];
    
    for (int i = 1; i < nums.length; i++) {
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(maxSum, currentSum);
    }
    
    return maxSum;
}
```

**3. Product of Array Except Self**
```java
public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    
    // Left products
    result[0] = 1;
    for (int i = 1; i < n; i++) {
        result[i] = result[i - 1] * nums[i - 1];
    }
    
    // Right products
    int right = 1;
    for (int i = n - 1; i >= 0; i--) {
        result[i] = result[i] * right;
        right *= nums[i];
    }
    
    return result;
}
```

**4. Container With Most Water**
```java
public int maxArea(int[] height) {
    int left = 0, right = height.length - 1;
    int maxArea = 0;
    
    while (left < right) {
        int area = Math.min(height[left], height[right]) * (right - left);
        maxArea = Math.max(maxArea, area);
        
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxArea;
}
```

---

### 5. String Problems

**1. Valid Palindrome**
```java
public boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;
    
    while (left < right) {
        while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
            left++;
        }
        while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
            right--;
        }
        
        if (Character.toLowerCase(s.charAt(left)) != 
            Character.toLowerCase(s.charAt(right))) {
            return false;
        }
        
        left++;
        right--;
    }
    
    return true;
}
```

**2. Longest Palindromic Substring**
```java
public String longestPalindrome(String s) {
    if (s == null || s.length() < 1) return "";
    
    int start = 0, end = 0;
    
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandFromCenter(s, i, i);      // Odd length
        int len2 = expandFromCenter(s, i, i + 1);  // Even length
        int len = Math.max(len1, len2);
        
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    
    return s.substring(start, end + 1);
}

private int expandFromCenter(String s, int left, int right) {
    while (left >= 0 && right < s.length() && 
           s.charAt(left) == s.charAt(right)) {
        left--;
        right++;
    }
    return right - left - 1;
}
```

**3. Group Anagrams**
```java
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> map = new HashMap<>();
    
    for (String str : strs) {
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        String key = new String(chars);
        
        map.putIfAbsent(key, new ArrayList<>());
        map.get(key).add(str);
    }
    
    return new ArrayList<>(map.values());
}
```

---

## 🎯 Top 30 Must-Do Problems

### Easy
1. Two Sum
2. Best Time to Buy and Sell Stock
3. Contains Duplicate
4. Valid Anagram
5. Valid Palindrome
6. Reverse String
7. First Unique Character
8. Implement strStr()
9. Merge Sorted Array
10. Pascal's Triangle

### Medium
11. 3Sum
12. Container With Most Water
13. Longest Substring Without Repeating Characters
14. Longest Palindromic Substring
15. Group Anagrams
16. Maximum Subarray
17. Rotate Array
18. Product of Array Except Self
19. Find All Anagrams in String
20. Subarray Sum Equals K
21. Spiral Matrix
22. Set Matrix Zeroes
23. String to Integer (atoi)
24. Zigzag Conversion
25. Minimum Window Substring

### Hard
26. Trapping Rain Water
27. Sliding Window Maximum
28. Median of Two Sorted Arrays
29. First Missing Positive
30. Minimum Window Substring

---

## ✅ Practice Checklist

- [ ] Implement array operations
- [ ] Master two pointers technique (10 problems)
- [ ] Master sliding window (10 problems)
- [ ] Solve string manipulation problems (10 problems)
- [ ] Practice Kadane's algorithm
- [ ] Solve anagram problems
- [ ] Practice palindrome problems
- [ ] Solve at least 30 problems total

---

**👉 Next:** [Linked Lists →](../02-linked-lists/README.md)

---

**💡 Pro Tip:** For interviews, always consider:
1. **Time Complexity**: Can you do better than O(n²)?
2. **Space Complexity**: Can you solve in O(1) space?
3. **Edge Cases**: Empty array, single element, all same elements
4. **Clarifying Questions**: Are there duplicates? Is array sorted?

