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
    # removing vertices in graph list
    toBeremoved = -1
    for i in graph:
        if i == vertex:
            toBeremoved = i
        else:
            for j in graph[i]:
                if j == vertex:
                    graph[i].remove(j)
    if toBeremoved != -1:
        print "Removing " + str(toBeremoved) + " from the graph"
        del graph[toBeremoved]
    # removing edges in edges list
    global edges
    tempEdges = list()
    for i in range(len(edges)):
        # print "checking (" + str(edges[i][0]) + ", " + str(edges[i][1]) + ")"
        if (edges[i][0] == vertex) or (edges[i][1] == vertex):
            print "Removing " + str(edges[i][0]) + ", " + str(edges[i][1]) + " from the edges list"
            continue
        else:
            tempEdges.append([edges[i][0], edges[i][1]]) 
    edges = tempEdges
    return graph

def vertexCover(graph, k):
    if checkNoEdges(graph):
        print "There are no edges in the graph, returning true!"
        return True
    if numberOfEdges(graph) >= (k * len(graph)):
        print "There are more than 0 edges in the graph"
        print "Number of edges = " + str(numberOfEdges(graph)) + " more than k*len(graph) = " + str(k * len(graph)) + " in the graph, returning false!"
        return False
    else:
        print "There are more than 0 edges in the graph and Number of edges = " + str(numberOfEdges(graph)) + " not more than k*len(graph) = " + str(k * len(graph)) + " in the graph"
        randomEdge = edges[0]
        print "selected " + str(randomEdge) + " randomly for proceeding!"
        print "calling graph - " + str(randomEdge[0]) + " and k = " + str(k-1)  
        subGraph1 = vertexCover(removeVertex(graph, randomEdge[0]), k-1)
        print "calling graph - " + str(randomEdge[0]) + " and k = " + str(k-1) 
        subGraph2 = vertexCover(removeVertex(graph, randomEdge[1]), k-1)
        return subGraph1 or subGraph2

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
# print graph
# print edges
# print removeVertex(graph, 3)
# print edges
print vertexCover(graph, k)
# print numberOfEdges(graph)