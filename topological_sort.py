def topological_sort(graph):
    inDeg ={}
    visit = []
    for v in graph:
        inDeg[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1
    for v in graph:
         if inDeg[v] == 0:
            visit.append(v)

    while visit:
        v = visit.pop()
        print(v,end='')

        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u]==0:
                visit.append(u)

my_graph = { "A":{"C","D"},
             "B":{"D","E"},
             "C":{"D","F"},
             "D":{"F"},
             "E":{"F"},
             "F":{}
    }
print(my_graph)
topological_sort(my_graph)


    
       
