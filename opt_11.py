import cvxpy as cp
import numpy as np
A= np.array([[1,-0.5],[-0.5,2]]).reshape(2,2)
b=np.array([-1,0]).reshape(2,1)
P = np.array([[1,-2],[1,4],[5,-76]]).reshape(3,2)
q=np.array([-2,-3,1]).reshape(3,1)
x=cp.Variable((2,1))
const= [P@x<=q]
obj= cp.Minimize(cp.quad_form(x,A)+b.T@x)
prob= cp.Problem(obj,const)
opt=prob.solve()
print("optimum value",opt)
print ("Optimum variables", x.value)