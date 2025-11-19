# 🔍 Sorting & Searching

## Overview
Sorting and searching are fundamental operations in computer science. Mastering these algorithms is crucial for technical interviews.

---

## 🔸 SORTING ALGORITHMS

### 1. **Bubble Sort**
```java
void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        boolean swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr, j, j + 1);
                swapped = true;
            }
        }
        if (!swapped) break; // Optimization
    }
}
```
**Time**: O(n²) worst/avg, O(n) best | **Space**: O(1) | **Stable**: Yes

### 2. **Selection Sort**
```java
void selectionSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        swap(arr, i, minIdx);
    }
}
```
**Time**: O(n²) all cases | **Space**: O(1) | **Stable**: No

### 3. **Insertion Sort**
```java
void insertionSort(int[] arr) {
    int n = arr.length;
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```
**Time**: O(n²) worst/avg, O(n) best | **Space**: O(1) | **Stable**: Yes  
**Best for**: Small arrays, nearly sorted data

### 4. **Merge Sort** ⭐
```java
void mergeSort(int[] arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

void merge(int[] arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    int[] L = new int[n1];
    int[] R = new int[n2];
    
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}
```
**Time**: O(n log n) all cases | **Space**: O(n) | **Stable**: Yes  
**Best for**: External sorting, stable sort needed

### 5. **Quick Sort** ⭐
```java
void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, high);
    return i + 1;
}
```
**Time**: O(n log n) avg, O(n²) worst | **Space**: O(log n) | **Stable**: No  
**Best for**: In-memory sorting, average case performance

### 6. **Heap Sort**
```java
void heapSort(int[] arr) {
    int n = arr.length;
    
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    
    // Extract elements from heap
    for (int i = n - 1; i > 0; i--) {
        swap(arr, 0, i);
        heapify(arr, i, 0);
    }
}

void heapify(int[] arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    
    if (largest != i) {
        swap(arr, i, largest);
        heapify(arr, n, largest);
    }
}
```
**Time**: O(n log n) all cases | **Space**: O(1) | **Stable**: No  
**Best for**: Priority queue, guaranteed O(n log n)

### 7. **Counting Sort** (Non-comparison based)
```java
void countingSort(int[] arr) {
    int max = Arrays.stream(arr).max().getAsInt();
    int min = Arrays.stream(arr).min().getAsInt();
    int range = max - min + 1;
    
    int[] count = new int[range];
    int[] output = new int[arr.length];
    
    // Store count
    for (int num : arr) {
        count[num - min]++;
    }
    
    // Cumulative count
    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output
    for (int i = arr.length - 1; i >= 0; i--) {
        output[count[arr[i] - min] - 1] = arr[i];
        count[arr[i] - min]--;
    }
    
    System.arraycopy(output, 0, arr, 0, arr.length);
}
```
**Time**: O(n + k) | **Space**: O(n + k) | **Stable**: Yes  
**Best for**: Small range of integers

### 8. **Radix Sort**
```java
void radixSort(int[] arr) {
    int max = Arrays.stream(arr).max().getAsInt();
    
    for (int exp = 1; max / exp > 0; exp *= 10) {
        countingSortByDigit(arr, exp);
    }
}

void countingSortByDigit(int[] arr, int exp) {
    int n = arr.length;
    int[] output = new int[n];
    int[] count = new int[10];
    
    for (int num : arr) {
        count[(num / exp) % 10]++;
    }
    
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }
    
    for (int i = n - 1; i >= 0; i--) {
        int digit = (arr[i] / exp) % 10;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }
    
    System.arraycopy(output, 0, arr, 0, n);
}
```
**Time**: O(d × (n + k)) | **Space**: O(n + k) | **Stable**: Yes  
**Best for**: Large numbers, fixed digit length

---

## 🔸 SEARCHING ALGORITHMS

### 1. **Linear Search**
```java
int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
```
**Time**: O(n) | **Space**: O(1)  
**Best for**: Unsorted arrays, small datasets

### 2. **Binary Search** ⭐
```java
// Iterative
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

// Recursive
int binarySearchRecursive(int[] arr, int target, int left, int right) {
    if (left > right) return -1;
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) {
        return binarySearchRecursive(arr, target, mid + 1, right);
    }
    return binarySearchRecursive(arr, target, left, mid - 1);
}
```
**Time**: O(log n) | **Space**: O(1) iterative, O(log n) recursive  
**Requirement**: Array must be sorted

### 3. **Binary Search Variations**

#### Find First Occurrence
```java
int findFirst(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            result = mid;
            right = mid - 1; // Continue searching left
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
}
```

#### Find Last Occurrence
```java
int findLast(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            result = mid;
            left = mid + 1; // Continue searching right
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
}
```

#### Search in Rotated Sorted Array
```java
int searchRotated(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] == target) return mid;
        
        // Left half is sorted
        if (nums[left] <= nums[mid]) {
            if (target >= nums[left] && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        // Right half is sorted
        else {
            if (target > nums[mid] && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return -1;
}
```

#### Find Peak Element
```java
int findPeakElement(int[] nums) {
    int left = 0, right = nums.length - 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[mid + 1]) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

### 4. **Ternary Search**
```java
// Find maximum in unimodal function
int ternarySearch(int[] arr, int left, int right) {
    while (right - left > 2) {
        int mid1 = left + (right - left) / 3;
        int mid2 = right - (right - left) / 3;
        
        if (arr[mid1] < arr[mid2]) {
            left = mid1;
        } else {
            right = mid2;
        }
    }
    
    int maxIdx = left;
    for (int i = left + 1; i <= right; i++) {
        if (arr[i] > arr[maxIdx]) maxIdx = i;
    }
    return maxIdx;
}
```
**Time**: O(log₃ n) | **Best for**: Finding maximum/minimum in unimodal functions

### 5. **Exponential Search**
```java
int exponentialSearch(int[] arr, int target) {
    if (arr[0] == target) return 0;
    
    int i = 1;
    while (i < arr.length && arr[i] <= target) {
        i *= 2;
    }
    
    return binarySearch(arr, target, i / 2, Math.min(i, arr.length - 1));
}
```
**Time**: O(log n) | **Best for**: Unbounded/infinite arrays

## Sorting Comparison

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| **Bubble** | O(n) | O(n²) | O(n²) | O(1) | Yes | Simple, rarely used |
| **Selection** | O(n²) | O(n²) | O(n²) | O(1) | No | Minimum swaps |
| **Insertion** | O(n) | O(n²) | O(n²) | O(1) | Yes | Good for small/sorted |
| **Merge** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Guaranteed performance |
| **Quick** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Fast in practice |
| **Heap** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | In-place |
| **Counting** | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | Integer range |
| **Radix** | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Yes | Fixed digits |

## Practice Problems

### Sorting
#### Easy
1. ✅ Sort Array
2. ✅ Merge Two Sorted Arrays
3. ✅ Sort Colors (Dutch National Flag)

#### Medium
4. 🔥 Kth Largest Element
5. 🔥 Sort List (Linked List)
6. 🔥 Meeting Rooms II
7. 🔥 Custom Sort String

#### Hard
8. 💪 Count of Smaller Numbers After Self
9. 💪 Reverse Pairs

### Binary Search
#### Easy
10. ✅ Binary Search
11. ✅ Search Insert Position
12. ✅ First Bad Version

#### Medium
13. 🔥 Search in Rotated Sorted Array
14. 🔥 Find Peak Element
15. 🔥 Search a 2D Matrix
16. 🔥 Find First and Last Position
17. 🔥 Koko Eating Bananas

#### Hard
18. 💪 Median of Two Sorted Arrays
19. 💪 Find Minimum in Rotated Sorted Array II
20. 💪 Split Array Largest Sum

## Binary Search Patterns

### 1. **Find Exact Value**
Standard binary search

### 2. **Find Boundary** (First/Last occurrence)
Continue searching after finding target

### 3. **Minimize/Maximize**
Binary search on answer space

### 4. **Matrix Search**
Treat 2D as 1D array

## Interview Tips

1. **Always clarify**: Array sorted? Duplicates allowed?
2. **Quick Sort in interviews**: Most commonly asked
3. **Binary Search mastery**: Know all variations
4. **Time vs Space tradeoff**: Merge (O(n) space) vs Quick (O(1) avg)
5. **Edge cases**: Empty array, single element, all duplicates

## Real-World Applications

### Sorting
- **Databases**: Query result ordering
- **E-commerce**: Product listings
- **Analytics**: Data analysis
- **File Systems**: Directory listings

### Binary Search
- **Autocomplete**: Search suggestions
- **Databases**: Index lookups
- **Version Control**: Finding bugs (git bisect)
- **Libraries**: Efficient lookups

## Next Steps

- **Dynamic Programming** → [07-dynamic-programming](../07-dynamic-programming/README.md)
- **Advanced Topics** → [08-advanced-topics](../08-advanced-topics/README.md)
- **Problem Patterns** → [problem-patterns](../problem-patterns/README.md)

---

**💡 Pro Tip**: Master binary search variations - they appear in 30%+ of coding interviews!

