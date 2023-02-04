import random
import sys

def genDigraph(num_vertices, is_connected):
    G = {}
    for i in range(num_vertices):
        G[i] = []
    if is_connected:
        for i in range(num_vertices - 1):
            for j in range(i+1, num_vertices):
                G[i].append(j)
    else:
        for i in range(num_vertices):
            for j in range(num_vertices):
                if i != j and random.random() < 0.5:
                    G[i].append(j)
    
    return G

def main():
    if len(sys.argv) == 1:
        num_vertices = random.randint(1,20)
        connect = random.randint(1,2)
        if connect == 1:
            is_connected = True
        else:
            is_connected = False
        digraph = genDigraph(num_vertices, is_connected)
    elif len(sys.argv) < 3:
        print("Not enough arguments")
        return
    else: 
        num_vertices = int(sys.argv[1])
        is_connected = (sys.argv[2] == "connected")
        digraph = genDigraph(num_vertices, is_connected)
    for i in digraph:
     for j in digraph[i]:
        print(f"{i} {j}")


main()