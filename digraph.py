import random

class DiGraph:
    def __init__(self, num_vertices, is_connected):
        self.num_vertices = num_vertices
        self.graph = {i: [] for i in range(num_vertices)}
        self.is_connected = is_connected

        if is_connected:
            for i in range(num_vertices - 1):
                j = i + 1
                self.graph[i].append(j)
                self.graph[j].append(i)

        else:
            for i in range(num_vertices):
                for j in range(i + 1, num_vertices):
                    if random.random() > 0.5:
                        self.graph[i].append(j)

    def display(self):
        print("Graph:")
        for i in range(self.num_vertices):
            print(i, "->", self.graph[i])

num_vertices = int(input("Enter the number of vertices: "))
is_connected = input("Is the graph connected (yes/no)? ") == "yes"
graph = DiGraph(num_vertices, is_connected)
graph.display()