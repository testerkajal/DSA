## Definition
>Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u-v, vertex u comes before v in the ordering.

## Graph:
```mermaid
graph TD;
  A --> B;
  A --> C;
  B --> D;
  B --> E;
  C --> D;
  D;
  E;
  ```

## Solution Approach

>In topological sorting:

1) We use a temporary stack. 
2) We don’t print the vertex immediately, 
3) We first recursively call topological sorting for all its adjacent vertices, then push it to a stack. 
4) Finally, print the contents of the stack. 

## Code

```py
def dfs_topological(graph, node, visited, stack):
    visited[node] = True

    # Recur for all the adjacent vertices
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_topological(graph, neighbor, visited, stack)

    # After exploring all adjacent vertices, push the current node to the stack
    stack.append(node)

def topological_sort(graph):
    num_nodes = len(graph)
    visited = {node: False for node in graph}
    stack = []

    # Perform DFS for each unvisited node
    for node in graph:
        if not visited[node]:
            dfs_topological(graph, node, visited, stack)

    # The stack now contains the topological ordering
    topological_ordering = stack[::-1]
    return topological_ordering

# Example usage:
dag = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': [],
    'E': [],
}

result = topological_sort(dag)
print("Topological Sorting Order:", result)

```
## Result: 
Topological Sorting Order: ['A', 'C', 'B', 'E', 'D']
