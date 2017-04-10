import numpy as np
# from scipy import optimize
# from scipy import optimize
from scipy import *
from numpy.linalg import solve

vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

edges = [
    (1,2), (1,3), (1,4), (1,5), (1,6), (4,5), (2,7), (3,7), (6,9), (3,9), (9,10), (7,8)  
]

n = len(vertices)
e = len(edges)

constraintList = list()
constraintValues = [1 for col in range(e)]

for edge in edges:
    tempList = [0 for col in range(n)]
    tempList[edge[0] - 1] = 1
    tempList[edge[1] - 1] = 1
    constraintList.append(tempList)

A_lb = np.array(constraintList)
b_lb = np.array(constraintValues)

c = np.array(constraintValues)

print A_lb, b_lb, c

res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=(0, 1))

print('Optimal value:', res.fun, '\nX:', res.x)

# for i in constraintList:
#     print i

# print lp
