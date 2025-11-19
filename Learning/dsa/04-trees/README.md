# 🌳 Trees

**Phase 4: Hierarchical Data Structures (2 Weeks)**

---

## 📖 Overview

Trees are fundamental hierarchical data structures crucial for technical interviews. They appear in 20-25% of coding interviews.

---

## 🎯 Core Concepts

### Tree Terminology

- **Root**: Top node
- **Parent**: Node with children
- **Child**: Node descended from parent
- **Leaf**: Node with no children
- **Height**: Longest path from root to leaf
- **Depth**: Distance from root to node
- **Level**: Depth + 1

---

## 📚 Binary Tree Basics

**Node Structure:**

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int val) {
        this.val = val;
    }
}
```

---

### 1. Tree Traversals

**Inorder (Left → Root → Right)**
```java
public void inorder(TreeNode root) {
    if (root == null) return;
    
    inorder(root.left);
    System.out.print(root.val + " ");
    inorder(root.right);
}

// Iterative
public List<Integer> inorderIterative(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode curr = root;
    
    while (curr != null || !stack.isEmpty()) {
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        result.add(curr.val);
        curr = curr.right;
    }
    
    return result;
}
```

**Preorder (Root → Left → Right)**
```java
public void preorder(TreeNode root) {
    if (root == null) return;
    
    System.out.print(root.val + " ");
    preorder(root.left);
    preorder(root.right);
}
```

**Postorder (Left → Right → Root)**
```java
public void postorder(TreeNode root) {
    if (root == null) return;
    
    postorder(root.left);
    postorder(root.right);
    System.out.print(root.val + " ");
}
```

**Level Order (BFS)**
```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    while (!queue.isEmpty()) {
        int size = queue.size();
        List<Integer> level = new ArrayList<>();
        
        for (int i = 0; i < size; i++) {
            TreeNode node = queue.poll();
            level.add(node.val);
            
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        
        result.add(level);
    }
    
    return result;
}
```

---

### 2. Binary Search Tree (BST)

**Properties:**
- Left subtree values < root
- Right subtree values > root
- Both subtrees are BSTs

**Search in BST:**
```java
public TreeNode searchBST(TreeNode root, int val) {
    if (root == null || root.val == val) {
        return root;
    }
    
    if (val < root.val) {
        return searchBST(root.left, val);
    } else {
        return searchBST(root.right, val);
    }
}
```

**Insert in BST:**
```java
public TreeNode insertIntoBST(TreeNode root, int val) {
    if (root == null) {
        return new TreeNode(val);
    }
    
    if (val < root.val) {
        root.left = insertIntoBST(root.left, val);
    } else {
        root.right = insertIntoBST(root.right, val);
    }
    
    return root;
}
```

**Validate BST:**
```java
public boolean isValidBST(TreeNode root) {
    return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
}

private boolean validate(TreeNode node, long min, long max) {
    if (node == null) return true;
    
    if (node.val <= min || node.val >= max) return false;
    
    return validate(node.left, min, node.val) &&
           validate(node.right, node.val, max);
}
```

---

### 3. Common Tree Problems

**1. Maximum Depth**
```java
public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    
    int leftDepth = maxDepth(root.left);
    int rightDepth = maxDepth(root.right);
    
    return Math.max(leftDepth, rightDepth) + 1;
}
```

**2. Symmetric Tree**
```java
public boolean isSymmetric(TreeNode root) {
    return isMirror(root, root);
}

private boolean isMirror(TreeNode t1, TreeNode t2) {
    if (t1 == null && t2 == null) return true;
    if (t1 == null || t2 == null) return false;
    
    return (t1.val == t2.val) &&
           isMirror(t1.left, t2.right) &&
           isMirror(t1.right, t2.left);
}
```

**3. Lowest Common Ancestor**
```java
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null || root == p || root == q) {
        return root;
    }
    
    TreeNode left = lowestCommonAncestor(root.left, p, q);
    TreeNode right = lowestCommonAncestor(root.right, p, q);
    
    if (left != null && right != null) return root;
    return left != null ? left : right;
}
```

**4. Path Sum**
```java
public boolean hasPathSum(TreeNode root, int targetSum) {
    if (root == null) return false;
    
    if (root.left == null && root.right == null) {
        return root.val == targetSum;
    }
    
    return hasPathSum(root.left, targetSum - root.val) ||
           hasPathSum(root.right, targetSum - root.val);
}
```

---

## 🎯 Top 25 Tree Problems

### Easy
1. Maximum Depth of Binary Tree
2. Same Tree
3. Invert Binary Tree
4. Symmetric Tree
5. Path Sum
6. Diameter of Binary Tree
7. Merge Two Binary Trees
8. Average of Levels

### Medium
9. Binary Tree Level Order Traversal
10. Validate Binary Search Tree
11. Kth Smallest Element in BST
12. Binary Tree Right Side View
13. Lowest Common Ancestor
14. Construct Binary Tree from Preorder and Inorder
15. Populating Next Right Pointers
16. Flatten Binary Tree to Linked List
17. Binary Tree Zigzag Level Order Traversal
18. All Nodes Distance K
19. Count Good Nodes in Binary Tree

### Hard
20. Binary Tree Maximum Path Sum
21. Serialize and Deserialize Binary Tree
22. Vertical Order Traversal
23. Binary Tree Cameras
24. Distribute Coins in Binary Tree
25. Count Complete Tree Nodes

---

**👉 Next:** [Graphs →](../05-graphs/README.md)

