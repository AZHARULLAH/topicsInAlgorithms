from cvxopt import matrix, solvers

# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# edges = [
#     (1,2), (1,3), (1,4), (1,5), (1,6), (4,5), (2,7), (3,7), (6,9), (3,9), (9,10), (7,8)  
# ]

def findLPSol(vertices, edges):

    n = len(vertices)
    e = len(edges)

    coEfficientsList = list()
    rawCoEfficientsList = list()
    criteriaList = [1.00 for col in range(n)]

    # Edge conditions -> x1 + x2 >= 1
    for edge in edges:
        tempList = [0 for col in range(n)]
        tempList[edge[0] - 1] = -1.00
        tempList[edge[1] - 1] = -1.00
        rawCoEfficientsList.append(tempList)

    # Lower bound conditions -> xn >= 0
    for i in range(n):
        tempList = [0 for col in range(n)]
        tempList[i] = -1.00
        rawCoEfficientsList.append(tempList)

    # Upper bound conditions -> xn <= 1
    for i in range(n):
        tempList = [0 for col in range(n)]
        tempList[i] = 1.00
        rawCoEfficientsList.append(tempList)

    # for i in rawCoEfficientsList:
    #     print (i)
    # print rawCoEfficientsList

    ctr = 0
    for vertex in vertices:
        tempList = list()
        for i in rawCoEfficientsList:
            tempList.append(i[ctr])
        coEfficientsList.append(tempList)
        ctr += 1

    # print ("\n---------------------\n")

    # for i in coEfficientsList:
    #     print (i)

    # print ("\n---------------------\n")

    # coEfficientsList is generated, now generate the constantsList,
    # first |E| conditions, then n conditions for ( xn >= 0 ) and n conditions for ( xn <= 1 )

    constantsList = [-1.00 for col in range(e)] + [0.00 for col in range(n)] + [1.00 for col in range(n)]

    # for i in constantsList:
    #     print (i)

    # print ("\n---------------------\n")

    A = matrix(coEfficientsList)
    B = matrix(constantsList)
    C = matrix(criteriaList)

    sol = solvers.lp(C, A, B)

    # print ("\n---------------------\n")

    # print(sol['x'])

    return sol['x']