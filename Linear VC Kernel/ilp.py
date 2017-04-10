from pulp import *

vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pulpVariables = list()

edges = [
    (1,2), (1,3), (1,4), (1,5), (1,6), (4,5), (2,7), (3,7), (6,9), (3,9), (9,10), (7,8)  
]

# edges = [
#     (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10)  
# ]

# declare your variables
# x1 = LpVariable("x1", 0, 40)   # 0<= x1 <= 40
# x2 = LpVariable("x2", 0, 1000) # 0<= x2 <= 1000

for i in vertices:
    temp = LpVariable("x" + str(i), 0.5, 1, LpContinuous)
    pulpVariables.append(temp)

for i in pulpVariables:
    print i

# defines the problem
prob = LpProblem("VCProblem", LpMaximize)

# defines the constraints
# prob += 2*x1+x2 <= 100

for edge in edges:
    var1 = pulpVariables[edge[0] - 1]
    var2 = pulpVariables[edge[1] - 1]
    print var1, var2
    prob += var1+var2 >= 1

# defines the objective function to maximize
# prob += 3*x1+2*x2

formula = ""
for i in pulpVariables:
    formula += i

prob += min(formula)

print prob

# solve the problem
status = prob.solve(GLPK(msg=0))
LpStatus[status]

# print the results x1 = 20, x2 = 60
# value(x1)
# value(x2)

for i in pulpVariables:
    print value(i)