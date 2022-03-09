import numpy as np
import cvxpy as cp
n=3
m=5
s= [40,50,45]
d= [45,20,30,30,10]
c= np.array([[8,6,10,9,8],[9,12,13,7,5],[14,9,16,5,2]])
# defining the variable
x= cp.Variable((n,m))
# assigning constraints
constraints = [x@np.ones(m)<=s, x.T@np.ones(n)>=d, x>=0] 

# defining ojective
objective= cp.Minimize(cp.trace(c.T@x))
#defining the problem
prob= cp.Problem(objective,constraints)
# solving the problem
optimal_cost= prob.solve()
#printing the optimum value
print("The optimum no. of servings :", x.value)
print("The optimum cost:",optimal_cost)
