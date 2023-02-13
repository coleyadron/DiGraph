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
if graph.is_connected():
        print("The graph is a connected.")
else:
        print("The graph is not a connected.")
start, end = "a", "q3"
path = []
if graph.find_path(start, end, path):
    print("Found path from", start, "to", end, ":", path)
else:
    print("No path found from", start, "to", end)