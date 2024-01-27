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
