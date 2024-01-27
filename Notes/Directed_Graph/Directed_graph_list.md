## Problem
>Here we will create the graph via user input. we will not hardcode the nodes and edges and will give
flexibility to the user so that he can add the edges between two nodes

## Give Directed Graph
<img src='../img/directedgraph.png' width="500" height="300"/>

## Code
###
```py
# First define an empty dictionary
graph = dict()

# here we are defining a function that will add edges between two nodes.
def addEdge(node1, node2):
    # create an empty list of key nodes
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []

    # append the neighbor node to its corresponding key node
    graph[node1].append(node2)

# Now finally we will add the edges between 2 nodes
def main():
    addEdge('0', '1')
    addEdge('1', '2')
    addEdge('1', '3')
    addEdge('1', '4')
    addEdge('4', '5')
    addEdge('5', '2')

    for key, val in graph.items():
        print(f"{key} --> {val}")

if __name__ == "__main__":  # Add this line to execute main() only if the script is run directly
    main()
```

