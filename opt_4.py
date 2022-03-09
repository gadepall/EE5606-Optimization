import numpy as np
import cvxpy as cp

c= np.array([120000,150000,150000]).reshape(1,3)
P= np.array([[1,1,1],[1200,1125,3150],[-30000,0,0],[0,0,-15000],[30000,0,0],[0,25000,0],[0,0,15000],[-1,0,0],[0,-1,0],[0,0,-1]]).reshape(10,3)
q= np.array([1,6000,-5000,-4000,10000,15000,8000,0,0,0]).reshape(10,1)
A1=np.array([[40,0,0],[0,40,0],[40,40,40]]).reshape(3,3)
A2=np.array([[1/30000,0,0],[0,1/25000,0],[0,0,1/15000]]).reshape(3,3)
# defining the variable
x= cp.Variable((3,1))
# assigning constraints
constraints = [P@x<=q] 
# defining ojective
objective= cp.Minimize(-(c@x))
#defining the problem
prob= cp.Problem(objective,constraints)
# solving the problem
opt_profit= -prob.solve()
z=A1@x.value
y=A2@x.value
#printing the optimum value
print("The optimum no. of  :", x.value)
print("Maximum profit:", opt_profit)
print("value of y:",y)
print("value of z:",z)