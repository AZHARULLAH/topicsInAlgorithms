def vertexCover(graph, k):
    if checkNoEdges(graph):
        return true
    if numberOfEdges(graph) >= (k * len(graph)):
        return false

graph = dict()

e = int(raw_input())
for i in range(e):
    a, b = map(int, raw_input().split(" "))
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

print vertexCover(graph, k)
