# 🕸️ Graphs

## Overview
Graphs are non-linear data structures consisting of vertices (nodes) and edges connecting them. They model relationships and networks.

## Graph Representations

### 1. **Adjacency Matrix**
```java
// Good for dense graphs
int[][] adjMatrix = new int[V][V];
// adjMatrix[i][j] = 1 means edge from i to j
// Space: O(V²), Edge lookup: O(1)
```

### 2. **Adjacency List**
```java
// Good for sparse graphs
List<List<Integer>> adjList = new ArrayList<>();
for (int i = 0; i < V; i++) {
    adjList.add(new ArrayList<>());
}
// Space: O(V + E), Edge lookup: O(degree)
```

### 3. **Edge List**
```java
class Edge {
    int src, dest, weight;
    Edge(int s, int d, int w) {
        src = s; dest = d; weight = w;
    }
}
List<Edge> edges = new ArrayList<>();
```

## Graph Types

### 1. **Directed Graph (Digraph)**
- Edges have direction (A → B)
- Used in: Task scheduling, web links

### 2. **Undirected Graph**
- Edges have no direction (A ↔ B)
- Used in: Social networks, road maps

### 3. **Weighted Graph**
- Edges have weights/costs
- Used in: Shortest path, MST

### 4. **Unweighted Graph**
- All edges have equal weight (1)

### 5. **Cyclic vs Acyclic**
- **Cyclic**: Contains cycles
- **Acyclic**: No cycles (DAG - Directed Acyclic Graph)

## Core Traversal Algorithms

### 1. **Depth-First Search (DFS)**
```java
// Recursive DFS
void dfs(int node, boolean[] visited, List<List<Integer>> graph) {
    visited[node] = true;
    System.out.print(node + " ");
    
    for (int neighbor : graph.get(node)) {
        if (!visited[neighbor]) {
            dfs(neighbor, visited, graph);
        }
    }
}

// Iterative DFS using Stack
void dfsIterative(int start, List<List<Integer>> graph) {
    boolean[] visited = new boolean[graph.size()];
    Stack<Integer> stack = new Stack<>();
    stack.push(start);
    
    while (!stack.isEmpty()) {
        int node = stack.pop();
        if (!visited[node]) {
            visited[node] = true;
            System.out.print(node + " ");
            
            for (int neighbor : graph.get(node)) {
                if (!visited[neighbor]) {
                    stack.push(neighbor);
                }
            }
        }
    }
}
```

### 2. **Breadth-First Search (BFS)**
```java
void bfs(int start, List<List<Integer>> graph) {
    boolean[] visited = new boolean[graph.size()];
    Queue<Integer> queue = new LinkedList<>();
    
    visited[start] = true;
    queue.offer(start);
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.print(node + " ");
        
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.offer(neighbor);
            }
        }
    }
}
```

**When to use:**
- **DFS**: Cycle detection, topological sort, path finding
- **BFS**: Shortest path (unweighted), level-order traversal

## Classic Graph Algorithms

### 3. **Dijkstra's Algorithm** (Shortest Path)
```java
int[] dijkstra(List<List<int[]>> graph, int start) {
    int n = graph.size();
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[start] = 0;
    
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
    pq.offer(new int[]{start, 0});
    
    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int node = curr[0];
        int distance = curr[1];
        
        if (distance > dist[node]) continue;
        
        for (int[] edge : graph.get(node)) {
            int neighbor = edge[0];
            int weight = edge[1];
            int newDist = dist[node] + weight;
            
            if (newDist < dist[neighbor]) {
                dist[neighbor] = newDist;
                pq.offer(new int[]{neighbor, newDist});
            }
        }
    }
    return dist;
}
```
**Time**: O((V + E) log V), **Space**: O(V)

### 4. **Bellman-Ford Algorithm** (Handles Negative Weights)
```java
int[] bellmanFord(int V, List<Edge> edges, int start) {
    int[] dist = new int[V];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[start] = 0;
    
    // Relax all edges V-1 times
    for (int i = 0; i < V - 1; i++) {
        for (Edge edge : edges) {
            if (dist[edge.src] != Integer.MAX_VALUE &&
                dist[edge.src] + edge.weight < dist[edge.dest]) {
                dist[edge.dest] = dist[edge.src] + edge.weight;
            }
        }
    }
    
    // Check for negative cycles
    for (Edge edge : edges) {
        if (dist[edge.src] != Integer.MAX_VALUE &&
            dist[edge.src] + edge.weight < dist[edge.dest]) {
            System.out.println("Negative cycle detected");
        }
    }
    return dist;
}
```
**Time**: O(VE), **Space**: O(V)

### 5. **Floyd-Warshall Algorithm** (All Pairs Shortest Path)
```java
void floydWarshall(int[][] graph) {
    int V = graph.length;
    int[][] dist = new int[V][V];
    
    // Initialize
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            dist[i][j] = graph[i][j];
        }
    }
    
    // Try all intermediate vertices
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] != Integer.MAX_VALUE &&
                    dist[k][j] != Integer.MAX_VALUE &&
                    dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}
```
**Time**: O(V³), **Space**: O(V²)

### 6. **Topological Sort** (DAG Only)
```java
// Using DFS
void topologicalSort(int V, List<List<Integer>> graph) {
    boolean[] visited = new boolean[V];
    Stack<Integer> stack = new Stack<>();
    
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            topologicalDFS(i, visited, graph, stack);
        }
    }
    
    while (!stack.isEmpty()) {
        System.out.print(stack.pop() + " ");
    }
}

void topologicalDFS(int node, boolean[] visited, 
                    List<List<Integer>> graph, Stack<Integer> stack) {
    visited[node] = true;
    for (int neighbor : graph.get(node)) {
        if (!visited[neighbor]) {
            topologicalDFS(neighbor, visited, graph, stack);
        }
    }
    stack.push(node);
}

// Using Kahn's Algorithm (BFS)
void topologicalSortKahn(int V, List<List<Integer>> graph) {
    int[] indegree = new int[V];
    for (int i = 0; i < V; i++) {
        for (int neighbor : graph.get(i)) {
            indegree[neighbor]++;
        }
    }
    
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < V; i++) {
        if (indegree[i] == 0) queue.offer(i);
    }
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.print(node + " ");
        
        for (int neighbor : graph.get(node)) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                queue.offer(neighbor);
            }
        }
    }
}
```

### 7. **Cycle Detection**
```java
// Undirected Graph
boolean hasCycleUndirected(int node, int parent, boolean[] visited, 
                           List<List<Integer>> graph) {
    visited[node] = true;
    for (int neighbor : graph.get(node)) {
        if (!visited[neighbor]) {
            if (hasCycleUndirected(neighbor, node, visited, graph)) {
                return true;
            }
        } else if (neighbor != parent) {
            return true;
        }
    }
    return false;
}

// Directed Graph (using colors: white=0, gray=1, black=2)
boolean hasCycleDirected(int node, int[] color, List<List<Integer>> graph) {
    color[node] = 1; // Mark as visiting
    
    for (int neighbor : graph.get(node)) {
        if (color[neighbor] == 1) return true; // Back edge found
        if (color[neighbor] == 0 && hasCycleDirected(neighbor, color, graph)) {
            return true;
        }
    }
    
    color[node] = 2; // Mark as visited
    return false;
}
```

### 8. **Minimum Spanning Tree (MST)**

#### Prim's Algorithm
```java
int primMST(int V, List<List<int[]>> graph) {
    boolean[] inMST = new boolean[V];
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
    pq.offer(new int[]{0, 0}); // {node, weight}
    
    int mstCost = 0;
    
    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int node = curr[0];
        int weight = curr[1];
        
        if (inMST[node]) continue;
        
        inMST[node] = true;
        mstCost += weight;
        
        for (int[] edge : graph.get(node)) {
            int neighbor = edge[0];
            int edgeWeight = edge[1];
            if (!inMST[neighbor]) {
                pq.offer(new int[]{neighbor, edgeWeight});
            }
        }
    }
    return mstCost;
}
```

#### Kruskal's Algorithm (using Union-Find)
```java
class UnionFind {
    int[] parent, rank;
    
    UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        
        if (rank[px] < rank[py]) parent[px] = py;
        else if (rank[px] > rank[py]) parent[py] = px;
        else {
            parent[py] = px;
            rank[px]++;
        }
        return true;
    }
}

int kruskalMST(int V, List<Edge> edges) {
    Collections.sort(edges, (a, b) -> a.weight - b.weight);
    UnionFind uf = new UnionFind(V);
    int mstCost = 0;
    
    for (Edge edge : edges) {
        if (uf.union(edge.src, edge.dest)) {
            mstCost += edge.weight;
        }
    }
    return mstCost;
}
```

## Common Graph Patterns

### 1. **Connected Components**
```java
int countComponents(int n, int[][] edges) {
    List<List<Integer>> graph = new ArrayList<>();
    for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
    for (int[] edge : edges) {
        graph.get(edge[0]).add(edge[1]);
        graph.get(edge[1]).add(edge[0]);
    }
    
    boolean[] visited = new boolean[n];
    int count = 0;
    
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, visited, graph);
            count++;
        }
    }
    return count;
}
```

### 2. **Bipartite Check**
```java
boolean isBipartite(List<List<Integer>> graph) {
    int n = graph.size();
    int[] color = new int[n];
    Arrays.fill(color, -1);
    
    for (int i = 0; i < n; i++) {
        if (color[i] == -1) {
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            color[i] = 0;
            
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : graph.get(node)) {
                    if (color[neighbor] == -1) {
                        color[neighbor] = 1 - color[node];
                        queue.offer(neighbor);
                    } else if (color[neighbor] == color[node]) {
                        return false;
                    }
                }
            }
        }
    }
    return true;
}
```

## Practice Problems

### Easy
1. ✅ Find if Path Exists in Graph
2. ✅ Number of Connected Components
3. ✅ Clone Graph

### Medium
4. 🔥 Course Schedule (Topological Sort)
5. 🔥 Number of Islands
6. 🔥 Pacific Atlantic Water Flow
7. 🔥 Network Delay Time (Dijkstra)
8. 🔥 Is Graph Bipartite
9. 🔥 All Paths From Source to Target

### Hard
10. 💪 Word Ladder
11. 💪 Alien Dictionary
12. 💪 Minimum Cost to Connect All Cities
13. 💪 Critical Connections in a Network
14. 💪 Reconstruct Itinerary

## Algorithm Comparison

| Algorithm | Problem | Time | Space |
|-----------|---------|------|-------|
| **BFS** | Shortest path (unweighted) | O(V+E) | O(V) |
| **DFS** | Cycle detection, Traversal | O(V+E) | O(V) |
| **Dijkstra** | Shortest path (non-negative) | O((V+E)logV) | O(V) |
| **Bellman-Ford** | Shortest path (with negative) | O(VE) | O(V) |
| **Floyd-Warshall** | All pairs shortest path | O(V³) | O(V²) |
| **Prim** | MST | O(ElogV) | O(V) |
| **Kruskal** | MST | O(ElogE) | O(V) |
| **Topological Sort** | DAG ordering | O(V+E) | O(V) |

## Real-World Applications

- **Social Networks**: Friend recommendations (BFS)
- **Maps/Navigation**: GPS routing (Dijkstra)
- **Compilers**: Dependency resolution (Topological Sort)
- **Network Design**: Minimum spanning tree
- **Web Crawlers**: Page traversal (DFS/BFS)
- **Recommendation Systems**: Graph-based filtering

## Interview Tips

1. **Always clarify**: Directed or undirected? Weighted or unweighted?
2. **Choose right representation**: Adjacency list for sparse, matrix for dense
3. **Master traversals**: DFS and BFS are building blocks
4. **Union-Find**: Essential for connectivity problems
5. **Practice visualization**: Draw graphs for complex problems

## Next Steps

- **Dynamic Programming** → [07-dynamic-programming](../07-dynamic-programming/README.md)
- **Advanced Topics** → [08-advanced-topics](../08-advanced-topics/README.md)
- **Practice** → [interview-questions](../interview-questions/README.md)

---

**💡 Pro Tip**: Most graph problems can be solved with DFS/BFS variations. Master these first before learning specialized algorithms!

