## Problem
>Find the indegree of each node of the graph
Note: Indegree of ny node means no of upcoming edges towards that node

<img src='../img/indegree.png' width="500" height="300"/>

## List Representation of the above graph

"A":['B'],\
"B":['C'],\
"C":['E'],\
"D":['B']\
"E":['D','F'],\
"F":[],

## Code
###
```py
def indegree(graph):
    # Initialize indegree for each node to 0
    indegree = {node: 0 for node in graph}

    # Count the incoming edges for each node
    for key, val in graph.items():
        for node in val:
            indegree[node] += 1

    return indegree

def main():
    # Example directed graph represented as an adjacency list
    graph = {
       "A": ['B'],
       "B": ['C'],
       "C": ['E'],
       "D": ['B'],
       "E": ['D', 'F'],
       "F": [],
    }

    # Calculate indegree for each node in the graph
    indegree_result = indegree(graph)

    # Print the indegree for each node
    print(indegree_result)

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()

