# 📝 Linked Lists

## Overview
Linked Lists are fundamental data structures where elements are stored in nodes, with each node containing data and a reference (pointer) to the next node.

## Topics Covered

### 1. **Singly Linked List**
- Node structure: data + next pointer
- Operations: insert, delete, search, traverse
- Time Complexity: O(1) insert at head, O(n) search

### 2. **Doubly Linked List**
- Node structure: data + next + previous pointers
- Bidirectional traversal
- Operations: insert at both ends O(1)

### 3. **Circular Linked List**
- Last node points back to first node
- Useful for round-robin scheduling
- No null terminator

## Key Operations

### Insertion
```java
// Insert at beginning
void insertAtHead(int data) {
    Node newNode = new Node(data);
    newNode.next = head;
    head = newNode;
}

// Insert at end
void insertAtEnd(int data) {
    Node newNode = new Node(data);
    if (head == null) {
        head = newNode;
        return;
    }
    Node current = head;
    while (current.next != null) {
        current = current.next;
    }
    current.next = newNode;
}

// Insert at position
void insertAtPosition(int data, int position) {
    if (position == 0) {
        insertAtHead(data);
        return;
    }
    Node newNode = new Node(data);
    Node current = head;
    for (int i = 0; i < position - 1 && current != null; i++) {
        current = current.next;
    }
    if (current == null) return;
    newNode.next = current.next;
    current.next = newNode;
}
```

### Deletion
```java
// Delete first node
void deleteHead() {
    if (head != null) {
        head = head.next;
    }
}

// Delete by value
void deleteByValue(int data) {
    if (head == null) return;
    if (head.data == data) {
        head = head.next;
        return;
    }
    Node current = head;
    while (current.next != null && current.next.data != data) {
        current = current.next;
    }
    if (current.next != null) {
        current.next = current.next.next;
    }
}
```

### Search
```java
// Search for a value
boolean search(int data) {
    Node current = head;
    while (current != null) {
        if (current.data == data) return true;
        current = current.next;
    }
    return false;
}
```

## Common Patterns & Problems

### 1. **Two Pointer Technique**
- **Fast & Slow Pointers** (Floyd's Cycle Detection)
  - Detect cycle in linked list
  - Find middle element
  - Find kth element from end

```java
// Detect cycle
boolean hasCycle(Node head) {
    Node slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}

// Find middle element
Node findMiddle(Node head) {
    Node slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}
```

### 2. **Reversal**
```java
// Reverse linked list iteratively
Node reverse(Node head) {
    Node prev = null, current = head;
    while (current != null) {
        Node next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

// Reverse recursively
Node reverseRecursive(Node head) {
    if (head == null || head.next == null) return head;
    Node newHead = reverseRecursive(head.next);
    head.next.next = head;
    head.next = null;
    return newHead;
}
```

### 3. **Merge Operations**
```java
// Merge two sorted lists
Node mergeSorted(Node l1, Node l2) {
    Node dummy = new Node(0);
    Node current = dummy;
    while (l1 != null && l2 != null) {
        if (l1.data <= l2.data) {
            current.next = l1;
            l1 = l1.next;
        } else {
            current.next = l2;
            l2 = l2.next;
        }
        current = current.next;
    }
    current.next = (l1 != null) ? l1 : l2;
    return dummy.next;
}
```

## Practice Problems

### Easy
1. ✅ Reverse a linked list
2. ✅ Detect cycle in linked list
3. ✅ Find middle element
4. ✅ Remove duplicates from sorted list
5. ✅ Merge two sorted lists

### Medium
6. 🔥 Remove Nth node from end
7. 🔥 Intersection of two linked lists
8. 🔥 Add two numbers represented as linked lists
9. 🔥 Palindrome linked list
10. 🔥 Reorder list (L0→Ln→L1→Ln-1→...)

### Hard
11. 💪 Reverse nodes in k-group
12. 💪 Merge k sorted lists
13. 💪 Copy list with random pointer
14. 💪 LRU Cache implementation

## Complexity Analysis

| Operation | Singly | Doubly | Array |
|-----------|--------|--------|-------|
| Access | O(n) | O(n) | O(1) |
| Search | O(n) | O(n) | O(n) |
| Insert at head | O(1) | O(1) | O(n) |
| Insert at tail | O(n) | O(1)* | O(1)* |
| Delete at head | O(1) | O(1) | O(n) |
| Delete at tail | O(n) | O(1) | O(1) |

*with tail pointer

## Advantages & Disadvantages

### ✅ Advantages
- Dynamic size (no fixed capacity)
- Efficient insertion/deletion at beginning
- No memory waste
- Easy to implement complex structures (stacks, queues)

### ❌ Disadvantages
- No random access (must traverse)
- Extra memory for pointers
- Not cache-friendly
- Reverse traversal difficult (singly)

## Interview Tips

1. **Always check for null**: Handle edge cases (empty list, single node)
2. **Use dummy nodes**: Simplifies insertion/deletion logic
3. **Draw diagrams**: Visualize pointer changes
4. **Two-pointer technique**: Master this pattern
5. **Practice reversal**: Very common in interviews

## Common Mistakes

❌ Forgetting to update head pointer  
❌ Not handling null cases  
❌ Losing reference to nodes during deletion  
❌ Not updating tail pointer in doubly linked lists  
❌ Infinite loops in circular lists  

## Real-World Applications

- **Music Playlists**: Next/previous song navigation
- **Browser History**: Forward/back navigation
- **Undo/Redo**: Editor operations
- **Image Viewer**: Next/previous image
- **File Systems**: Directory structures
- **Memory Management**: Free memory blocks

## Resources

### Practice Platforms
- LeetCode: Linked List problems
- HackerRank: Data Structures
- GeeksforGeeks: Linked List practice

### Videos
- Abdul Bari: Linked List algorithms
- mycodeschool: Linked List series

## Next Steps

After mastering linked lists, move to:
- **Stacks & Queues** → [03-stacks-queues](../03-stacks-queues/README.md)
- **Trees** → [04-trees](../04-trees/README.md)
- **Practice Problems** → [problem-patterns](../problem-patterns/README.md)

---

**💡 Pro Tip**: Draw the pointers on paper before coding. Understanding pointer manipulation is key to mastering linked lists!

