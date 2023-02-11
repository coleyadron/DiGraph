'''
take argument in form of edges and then store them to undertsand the graph then determine 
the # of vertices and edges, if DAG, and the path
'''
from collections import defaultdict
edges = []
print("Enter edges in format 'a b': (ctrl + d to stop)")
while True:
    try:
        edge = input()
        if edge == "stop":
             break
        v1, v2 = edge.split()
        if (v1, v2) in edges or (v2, v1) in edges:
            print("Duplicate edge found, renter new edge.")
        else:
             edges.append((v1, v2))
    except EOFError:
         break

print(edges)

class DirectedGraph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            self.graph[u].append(v)
        self.visited = {}