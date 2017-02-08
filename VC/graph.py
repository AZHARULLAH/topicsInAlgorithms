def checkNoEdges(graph):
    for i in graph:
        if len(graph[i]) > 0:
            return false
    return true

def numberOfEdges(graph):
    sum = 0
    for i in graph:
        sum = sum + len(graph[i])
    return sum/2

def vertexCover(graph, k):
    if checkNoEdges(graph):
        return true
    if numberOfEdges(graph) >= (k * len(graph)):
        return false

graph = dict()
edges = list()
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

# print len(edges)
# print vertexCover(graph, k)
# print numberOfEdges(graph)