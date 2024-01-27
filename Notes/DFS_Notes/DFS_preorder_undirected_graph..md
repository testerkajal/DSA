## Problem Statement: 
> Given an undirected graph, return a vector of all nodes by traversing the graph using depth-first search (DFS).

# Pre-req:
>Recursion, Graph Representation
## Graph
```mermaid
graph TD;
  A --> B;
  A --> C;
  B --> A;
  B --> D;
  C --> A;
  C --> D;
  C --> E;
  D --> B;
  D --> C;
  D --> E;
  E --> C;
  E --> D;
  ```
# Solution Approach
### 1 Implement a Depth-First Search (DFS) function to traverse the graph/
### 2 Maintain a visited array to keep track of visited nodes./
### 3 Start DFS from each unvisited node in the graph.
### 4 Print the nodes in pre-order during traversal.

## Code
###
```py
def dfs(graph, node, visited):
    # Mark the current node as visited
    visited[node] = True

    # Process the current node (pre-order)
    print(node, end=' ')

    # Recur for all the adjacent nodes
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def dfs_preorder(graph):
    # Get the number of nodes in the graph
    num_nodes = len(graph)

    # Initialize the visited array
    visited = {node: False for node in graph}

    # Perform DFS traversal for each unvisited node
    for node in graph:
        if not visited[node]:
            dfs(graph, node, visited)

# Example usage:
undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

print("DFS Pre-order Traversal:")
dfs_preorder(undirected_graph)

```
## Result:
> DFS Pre-order Traversal:
A B D C E
