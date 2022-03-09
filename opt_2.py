import numpy as np
import cvxpy as cp
from expense_stream_data import *
b= cp.Variable((n,1))
w= cp.Variable((n,1))
x= cp.Variable((m,1))
constraints= [b[t+1]==((1+rho)*b[t])-w[t] for t in range(n-1)] 
constraints+= [x>=0, b>=0, w+(P@x)>=e] 
objective= cp.Minimize(b[0]+x.T@np.ones(m))
prob= cp.Problem(objective,constraints)
opt_investment=prob.solve()
print("The optimum investment:", opt_investment)
