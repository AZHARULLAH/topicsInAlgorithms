import itertools

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

graph = dict()
k = int(raw_input())
for i in range(e):
    inputLst = map(int, raw_input().split(" "))
    if len(inputLst) == 1:
        print "len 1"
        a = inputLst[0]
        if a in graph:
            graph[a] = list()
    else:
        a,b = inputLst[0], inputLst[1]
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

allPossibleKCombinations = list(itertools.combinations(vertices, k))
print graph
# print edges
# print allPossibleKCombinations
# print "\n********\n"

flag = 0

for i in allPossibleKCombinations:
    if checkIfVertexCover(i, edges) == True:
        flag = 1
        print "True, Vertex cover of size " + str(k) + " is " + str(i)
if flag == 0:
    print "False. vertex cover of size " + str(k) + " doesn't exist"


# print vertices
# print len(allPossibleKCombinations)