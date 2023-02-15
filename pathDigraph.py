'''
take argument in form of edges and then store them to undertsand the graph then determine 
the # of vertices and edges, if DAG, and the path
'''
import sys
from collections import defaultdict

edges = []
vertices = []
print("Enter edges in format 'a b': (type stop to exit)")
while True:
    try:
        edge = input()
        if edge == "stop" or edge == "STOP":
            break
        v1, v2 = edge.split()
        if (v1, v2) in edges or (v2, v1) in edges:
            print("Duplicate edge found, renter new edge.")
        else:
            edges.append((v1, v2))
            if v1 not in vertices:
                    vertices.append(v1)
            if v2 not in vertices:
                    vertices.append(v2)
    except EOFError:
         break

print("Edges Entered: ")
print(edges)

class DirectedGraph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            self.graph[u].append(v)
        self.visited = {}
    
    def find_path(self, start, end, path):
        path.append(start)
        if start == end:
            return True
        for node in self.graph[start]:
            if node not in path:
                if self.find_path(node, end, path):
                    return True
        path.pop()
        return False

    def is_DAG(self):
        for node in self.graph:
            if node not in self.visited:
                if self.is_cyclic(node, None):
                    return False
        return True

    def is_cyclic(self, node, parent):
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                if self.is_cyclic(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    def is_connected(self):
        start = next(iter(self.graph.keys()))
        self.dfs(start)
        return len(self.visited) == len(self.graph)

    def dfs(self, node):
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)

graph = DirectedGraph(edges)
print("Number of vertices:", len(vertices))
print("Number of edges:", sum([len(v) for v in graph.graph.values()]))
if graph.is_connected():
        print("The graph is connected: True")
else:
        print("The graph is connected: False")
if graph.is_DAG():
        print("The graph is a DAG: True")
else:
        print("The graph is a DAG: False")
if len(sys.argv) == 1:
    start, end = "null", "null"
elif len(sys.argv) < 3:
    print("Not enough arguments")
else:
    start = sys.argv[1]
    end = sys.argv[2]
path = []
if graph.find_path(start, end, path):
    print("Found path from", start, "to", end, ":", path)
else:
    print("No path found from", start, "to", end)