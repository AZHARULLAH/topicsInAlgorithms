import sys
import numpy as np
import random

numOfvertices = random.randint(100, 200)
k = random.randint(100, numOfvertices)
# print numOfvertices, k
adjacencyMatrix = np.random.randint(0, 2, (numOfvertices, numOfvertices))
for i in range(numOfvertices):
	for j in range(numOfvertices-1, -1, -1):
		adjacencyMatrix[i][j] = adjacencyMatrix[j][i]
		if i == j:
			adjacencyMatrix[i][j] = 0
		# print "Copying " + str(j) + str(i) + " to " + str(i) + str(j)

print "Copying done"

fileName = str(sys.argv[1])
file = open(fileName, "w")

print >>file, str(k)
# print >>file, str(adjacencyMatrix)

edges = list()

for i in range(0, numOfvertices):
	for j in range(0, numOfvertices):
		if adjacencyMatrix[i][j] == 1:
			flag = 0
			for e in edges:
				if (e[0] == i and e[1] == j) or (e[0] == j and e[1] == i):
					flag = 1
					break
			if flag == 0:
				tempList = list()
				tempList.append(i)
				tempList.append(j)
				edges.append(tempList)

# print >>file, str(edges)

for i in edges:
	print >>file, str(i[0]) + " " + str(i[1])