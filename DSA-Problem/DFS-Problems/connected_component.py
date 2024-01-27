def dfs(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def connected_components(graph):
    num_nodes = len(graph)
    visited = {node: False for node in graph}
    components = []

    for node in graph:
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)

    return components

# Example usage:
undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D'],
    'F': ['G'],
    'G': ['F']
}

connected_components_list = connected_components(undirected_graph)

# Print the connected components and their nodes
for i, component in enumerate(connected_components_list):
    print(f"Connected Component {i + 1}: {component}")

print(f"Total number of connected components: {len(connected_components_list)}")
