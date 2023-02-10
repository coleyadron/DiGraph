'''
take argument in form of edges and then store them to undertsand the graph then determine 
the # of vertices and edges, if DAG, and the path
'''
edges = {}

print("Enter edges in format 'a b': (ctrl + d to stop)")
while True:
    try:
        edge = input()
        if edge == "stop":
            break
        v1, v2 = edge.split()
        if (v1, v2) in edges.keys() or (v2, v1) in edges.keys():
            print("Duplicate edge found, renter new edge.")
        else:
            edges[(v1, v2)] = True
    except EOFError:
        break

print("Edges:")
for edge in edges:
    print(edge)
