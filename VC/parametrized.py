import sys
import time

edges = list()
vertices = list()

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
                didSomething = True
                break
        if didSomething == False:
            break
    # print graph, k
    # print "Calling DBST now"
    if numberOfEdges(graph) <= (3 * (k ^ 2)):
        return VCDbst(graph,k,originalK)
    else:
        return False

# Open file given for input and read from that file
fileName = str(sys.argv[1])
with open(fileName) as file:
	lines = file.readlines()

graph = dict()
lineNum = 1
for line in lines:
	finalLine = line.rstrip('\n').split(" ")
    # line number 1 is the paramter
	if lineNum == 1:
		k = int(finalLine[0])
	else:
        # Single vertices
		if len(finalLine) == 1:
			a = int(finalLine[0])
			if a not in graph:
				graph[a] = list()
			vertices.append(a)
        # Two vertices => an edge
		else:
			a,b = int(finalLine[0]), int(finalLine[1])
			edges.append([a,b])
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
			if a not in vertices:
				vertices.append(a)
			if b not in vertices:
				vertices.append(b)
	lineNum = lineNum + 1

# print int(k[0])
# print graph
# print vertices
# print edges

start_time = time.time()

# reduceGraph(graph, k)
if kernelize(graph, k):
    print "Graph has a VC of size " + str(k)
else:
    print "No VC of size " + str(k) + " exists on the graph."
# print removeVertex(graph, 3)
print("\nThe main program ran in %s seconds..." % (time.time() - start_time))