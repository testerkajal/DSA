#here we are going to implement the graph using adjecency list representation 
# so we are using disctionary for implementing graph (adjecency list representation)

graph ={
    'A':["B","C"],
    'B':["A","D"],
    'C':["A","D","E"],
    'D':["B","C","E"],
    'E':["C","D"]
}

#To verify or get the adjecent of any node 
print(graph['B'])

#-------Problem1----------
'''add a new edge or adjecent of A to/as D. For this we have to add adjecent of D as A.
 since our graph is undirected. '''
graph['A'].append("D")
graph['D'].append("A")
print(graph['A']) # A : ['B', 'C', 'D']
print(graph['D']) # D: ['B', 'C', 'E', 'A']

#After the above operation our graph will changed to 
print(graph) # {'A': ['B', 'C', 'D'], 'B': ['A', 'D'], 'C': ['A', 'D', 'E'], 'D': ['B', 'C', 'E', 'A'], 'E': ['C', 'D']}
''' i.e 
graph ={
    'A':["B","C","D"],
    'B':["A","D"],
    'C':["A","D","E"],
    'D':["B","C","E","A"],
    'E':["C","D"]
}'''
#------Done--------------

#-------Problem2----------
""" Now we have to print the graph in below format
A-->B,C,D
B-->A,D
C-->A,D,E
D-->B,C,E,A
E-->C,D
"""
for key, val in graph.items():
    print(f"{key}-->{','.join(val)}")
#--------------Done---------
    

    





