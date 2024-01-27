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
