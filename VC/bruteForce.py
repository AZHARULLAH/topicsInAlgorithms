import sys
import itertools
import time

edges = list()
vertices = list()

def checkIfVertexCover(lst, edges):
    tempEdges = list()
    # print "Edges is " + str(edges)
    # print "List is " + str(lst)
    for i in edges:
        if (i[0] in lst) or (i[1] in lst):
            continue
        else:
            tempEdges.append(i)
    # print len(tempEdges)
    if len(tempEdges) == 0:
        return True
    else:
        return False

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

start_time = time.time()

allPossibleKCombinations = list(itertools.combinations(vertices, k))
flag = 0
for i in allPossibleKCombinations:
    if checkIfVertexCover(i, edges) == True:
        flag = 1
        print "True, Vertex cover of size " + str(k) + " is " + str(i)
        break
if flag == 0:
    print "False. vertex cover of size " + str(k) + " doesn't exist"

print("\nThe main program ran in %s seconds..." % (time.time() - start_time))

# print int(k[0])
# print graph
# print vertices
# print edges