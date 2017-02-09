edges = list()

def checkNoEdges(graph):
    for i in graph:
        if len(graph[i]) > 0:
            return False
    return True

def numberOfEdges(graph):
    sum = 0
    for i in graph:
        sum = sum + len(graph[i])
    return sum/2

def removeVertex(graph, vertex):
    for i in graph:
        if i == vertex:
            toBeremoved = i
        else:
            for j in graph[i]:
                if j == vertex:
                    graph[i].remove(j)
    del graph[toBeremoved]
    for i in edges:
        if (i[0] == vertex) or (i[1] == vertex):
            edges.remove[i]
    print edges
    return graph

def vertexCover(graph, k):
    if checkNoEdges(graph):
        return true
    if numberOfEdges(graph) >= (k * len(graph)):
        return false

graph = dict()
e = int(raw_input())
for i in range(e):
    a, b = map(int, raw_input().split(" "))
    edges.append([a,b])
    # edges.append([b,a])
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = list()
        graph[a].append(b)
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = list()
        graph[b].append(a)
        
k = int(raw_input())

# print checkNoEdges(graph)
# print numberOfEdges(graph)
print graph
print edges
print removeVertex(graph, 3)
print edges
# print vertexCover(removeVertex(graph, 3), k)
# print numberOfEdges(graph)