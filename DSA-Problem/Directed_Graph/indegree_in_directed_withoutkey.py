def indegree(graph, n):
    # Initialize indegree for each node to 0
    indegree = [0] * n
    
    # Iterate over each node in the graph
    for i in range(0,len(graph)):
        # Get the list of adjacent nodes for the current node
        neighbours = graph[i]
        
        # Iterate over the adjacent nodes and update their indegree
        for j in range(len(neighbours)):
            indegree[neighbours[j]] += 1


    print (indegree)

if __name__ == "__main__":
    # Example directed graph represented as an adjacency list
    graph = [
        [1,2],
        [3,4],
        [],
        [],
        [2,3]
    ]
    
    n = len(graph)
    
    # Calculate and print the indegree of each node
    indegree(graph, n)
