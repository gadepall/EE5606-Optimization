import numpy as np
import cvxpy as cp
cost= [0.18,0.23,0.05]
A= [107,500,0]
cal= [72,121,65]
P= np.array([[107,500,0],[-107,-500,0],[72,121,65],[-72,-121,-65],[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]])
Q= np.array([50000,-5000,2250,-2000,10,10,10,0,0,0])
def optimum_cost(s):
  return cost@s # defining the optimization function
# defining the variable
s= cp.Variable(3, integer=True)
# assigning constraints
constraints = [P@s<=Q] 
#constraints = [s>=0 , s<=10 , A@s>= 5000 , A@s<=50000 , cal@s>=2000 , cal@s<=2250]
# defining ojective
objective= cp.Minimize(cost@s)
#defining the problem
prob= cp.Problem(objective,constraints)
# solving the problem
prob.solve()
#printing the optimum value
print("The optimum no. of servings :", s.value)
print("The optimum cost :", optimum_cost(s.value))
