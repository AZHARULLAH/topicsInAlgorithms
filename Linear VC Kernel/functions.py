solutionSet = list()

# Checks if there are any edges in the graph
def checkNoEdges(graph):
    for i in graph:
        if len(graph[i]) > 0:
            return False
    return True

# Counts the number of edges in the graph
def numberOfEdges(graph):
    sum = 0
    for i in graph:
        sum = sum + len(graph[i])
    return sum/2

# Function to pick a random edge from a graph
def pickRandomEdge(graph):
    if checkNoEdges(graph):
        return False
    else:
        selectedEdge = list()
        for i in graph:
            if len(graph[i])!=0:
                selectedEdge.append(i)
                selectedEdge.append(graph[i][0])
                # print "Selected " + str(selectedEdge)
                return selectedEdge

# Function to remove a vertex from a graph
def removeVertex(graph, vertex):
    for i in graph:
        if vertex in graph[i]:
            graph[i].remove(vertex)
    if vertex in graph:
        del graph[vertex]
    return graph

def VCDbst(graph, k, originalK):
    # print "Called DBST with graph = " + str(graph) + " and k = " + str(k)
    if checkNoEdges(graph):
        return True
    if k <= 0:
        if checkNoEdges(graph):
            # print "Graph has a VC of size " + str(originalK)
            return True
        else:
            # print "Graph has no VC of size " + str(originalK)
            return False
    else:
        randomEgde = pickRandomEdge(graph)
        # print randomEgde
        graph1 = dict(graph)
        graph2 = dict(graph)
        result = (VCDbst(removeVertex(graph1, randomEgde[0]), k-1, originalK) or VCDbst(removeVertex(graph, randomEgde[1]), k-1, originalK))
        # print VCDbst(removeVertex(graph2, randomEgde[1]), k-1, originalK)
        # print result
        return result

# This function will reduce the graph and produce a f(k) kernel for the graph
def kernelize(graph, k):
    originalK = k
    while(1):
        if k<=0:
            if checkNoEdges(graph):
                # print "Graph has a VC of size " + str(originalK)
                # print graph, k
                return True
            else:
                # print "Graph has no VC of size " + str(originalK)
                # print graph, k
                return False
        didSomething = False
        # Check for single vertices
        for i in graph.keys():
            if len(graph[i]) == 0:
                # print "deleting " + str(i) + " (single vertex)" 
                del graph[i]
                didSomething = True
                break
        # Check for self loops
        for i in graph.keys():
            if i in graph[i]:
                # print "deleting " + str(graph[i]) + " (self loop)" 
                for j in graph.keys():
                    if i in graph[j]:
                        # print "deleting " + str(graph[j]) + " from " + str(i) + " (self loop edges)" 
                        graph[j].remove(i)
                del graph[i]
                k -= 1
                solutionSet.append(i)
                didSomething = True
                break
        # Check for vertices with degree > k
        for i in graph.keys():
            if len(graph[i]) > k:
                # print "deleting " + str(i) + " = " + str(graph[i]) + " (>" + str(k) + " neighbours)" 
                for j in graph.keys():
                    if i in graph[j]:
                        # print "deleting " + str(i) + " = " + str(graph[i]) + " (>" + str(k) + " neighbours)"
                        graph[j].remove(i)
                del graph[i]
                k -= 1
                solutionSet.append(i)
                didSomething = True
                break
        if didSomething == False:
            break
    
    # print (solutionSet, "@@@@@")
    return graph, k, solutionSet