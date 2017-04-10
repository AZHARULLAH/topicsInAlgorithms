import sys
import time
import itertools
from functions import *
from cvxoptsol import *

edges = list()
vertices = list()

solutionSet = list()

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

print ("\n------------ Solution ------------------\n")

start_time = time.time()

graph, k, solSubSet = kernelize(graph, k)

solutionSet += solSubSet

vertices = list()
edges = list()

for i in graph:
    for j in graph[i]:
        temp = list()
        temp.append(i)
        temp.append(j)
        edges.append(temp)
        if i in graph[j]:
            graph[j].remove(i)
    vertices.append(i)

# print ("\n----- After Kernelization ---------\n")
# print (k)
# print (vertices)
# print (edges)
# print ("\n----- /After Kernelization ---------\n")

# Mapping the vertices to 1,2,3...

mappedVertices = dict()

k = 1
for i in vertices:
    mappedVertices[k] = i
    k += 1

mappedEdges = edges
for i in range(len(mappedEdges)):
    mappedEdges[i][0] = mappedVertices[mappedEdges[i][0]]  
    mappedEdges[i][1] = mappedVertices[mappedEdges[i][1]]

# print ("Mapped Vertices", mappedVertices)

# print ("\n----- After Mapping ---------\n")
# print (k)
# print (mappedVertices)
# print (mappedEdges)
# print ("\n----- /After Mapping ---------\n\n")

LPResult = findLPSol(mappedVertices, mappedEdges)

# print ("LP Solved", LPResult)

V_05 = list()
V_1 = list() 
V_0 = list()

for i in range(len(LPResult)):
    if (round(LPResult[i], 2)) == 0:
        tempVertex = i + 1
        V_0.append(tempVertex)
    elif (round(LPResult[i], 2)) == 1:
        tempVertex = i + 1
        V_1.append(tempVertex)
    else: #(round(LPResult[i], 2)) == 1:
        tempVertex = i + 1
        V_05.append(tempVertex)

# print (V_0, V_05, V_1)

for i in range(len(V_0)):
    for searchKey in mappedVertices:
        if searchKey == V_0[i]:
            V_0[i] = mappedVertices[searchKey]

for i in range(len(V_1)):
    for searchKey in mappedVertices:
        if searchKey == V_1[i]:
            V_1[i] = mappedVertices[searchKey]

for i in range(len(V_05)):
    for searchKey in mappedVertices:
        if searchKey == V_05[i]:
            V_05[i] = mappedVertices[searchKey]

# print ("LP Result is")

print ("\n------ Final Solution --------\n")
print ("Vertices that cannot be in VC", V_0)
print ("Vertices that are for sure in VC", V_1 + solutionSet)
print ("Vertices that are in VC with a choice", V_05)
print ("\n------ /Final Solution --------\n")
print ("\n------------ /Solution ------------------\n")