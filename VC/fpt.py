import sys
import itertools
import time

edges = list()
vertices = list()

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

def removeVertex(graph, verticeslist):
	# print vertices
	removedVertices = list()
	for vertex in verticeslist:
		# print vertex
		# removing vertices in graph list
		for i in graph:
			if i == vertex:
				# print "removed " + str(i) + " from graph"
				removedVertices.append(i)
				del graph[i]
				break
		for i in graph:
			toBeRemoved = -1
			for j in graph[i]:
				if j == vertex:
					graph[i].remove(j)
		global edges
		tempEdges = list()
		for i in range(len(edges)):
			if (edges[i][0] == vertex) or (edges[i][1] == vertex):
				# print "Removing " + str(edges[i][0]) + ", " + str(edges[i][1]) + " from the edges list"
				continue
			else:
				tempEdges.append([edges[i][0], edges[i][1]]) 
		edges = tempEdges
	global vertices
	# removing vertice in list
	tempVertices = list(set(vertices) - set(removedVertices)) 
	# print vertices
	# print removedVertices
	# print "&&&"
	# print tempVertices
	vertices = tempVertices
	# print vertices
	return graph

def checkIfVertexCover(lst, edges):
    tempEdges = list()
    for i in edges:
        if (i[0] in lst) or (i[1] in lst):
            continue
        else:
            tempEdges.append(i)
    if len(tempEdges) == 0:
        return True
    else:
        return False

def reduceGraph(graph, k):
	# print graph, k
	duplicateGraph = graph
	# print duplicateGraph
	if k == 0:
		print "False, vertex cover does not exists"
	if checkNoEdges(graph):
		print "True, vertex cover exists"
	if numberOfEdges(graph) >= (k * len(graph)):
		print "False, vertex cover does not exists"
	verticesToBeRemoved = list()
	for i in duplicateGraph:
		if len(duplicateGraph[i]) == 0:
			# print "case 1"
			verticesToBeRemoved.append(i)
			# return reduceGraph(removeVertex(graph, tempList), k)
		elif len(duplicateGraph[i]) > k:
			# print "case 2"
			verticesToBeRemoved.append(i)
			# return reduceGraph(removeVertex(graph, tempList), k-1)
		elif len(duplicateGraph[i]) == 1:
			# print "case 3"
			verticesToBeRemoved.append(i)
			verticesToBeRemoved.append(graph[i][0])
			# return reduceGraph(removeVertex(graph, tempList), k-1)
	# return graph
	vertexCover(removeVertex(graph, verticesToBeRemoved), k)

def vertexCover(graph, k):
	start_time = time.time()
	allPossibleKCombinations = list(itertools.combinations(vertices, k))
	flag = 0
	for i in allPossibleKCombinations:
	    if checkIfVertexCover(i, edges) == True:
	        flag = 1
	        print "True, Vertex cover of size " + str(k) + " is " + str(i)
	if flag == 0:
	    print "False. vertex cover of size " + str(k) + " doesn't exist"
	print("\nThe main program ran in %s seconds..." % (time.time() - start_time))

fileName = str(sys.argv[1])

with open(fileName) as file:
	lines = file.readlines()

graph = dict()
lineNum = 1
for line in lines:
	finalLine = line.rstrip('\n').split(" ")
	if lineNum == 1:
		k = int(finalLine[0])
	else:
		if len(finalLine) == 1:
			a = int(finalLine[0])
			if a not in graph:
				graph[a] = list()
			vertices.append(a)
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

reduceGraph(graph, k)

# print removeVertex(graph, [1, 2])