import numpy as np
import cvxpy as cp
from pv_output_data import *
import matplotlib.pyplot as plt

p=np.reshape(p,[2016,1])

N=288 #number of samples in a dar
T=2016 #periods(one week)
### Defining cvxpy variables

c=cp.Variable((T,1)) #clear sky output
s=cp.Variable((T,1)) #shading loss component
r=cp.Variable((T,1)) #residual errors

### Defining Objective Function
c1=c[0:N]
I=np.identity(N)
A= np.roll(I, 1, axis=1)
obj=cp.sum_squares((I-A)@c1)
obj+=np.ones(T).T@s

#our objective
objective=cp.Minimize(obj)


### Constraints for Objective Function

constraints=[0<=s,s<=c,p==c-s+r]
constraints+=[(cp.norm(r,1)/T)<=4]
constraints+=[(c[i]==c[i-N]) for i in range(N,T)]

# Formulating convex problem

prob=cp.Problem(objective,constraints)
prob.solve()



#Printing required results
print('minimum value of loss function is',prob.solve())       
#print(c.value)
print('average value of clear sky output c:',np.mean(c.value))
print('average value of shading loss component s:',np.mean(s.value))
print('average value of PV array output time series p:',np.mean(p))
print('average of abosulte of residual errors r:',np.mean(r.value))
### Plots 
plt.figure()
plt.plot(c.value)
plt.title('plot for c')
plt.ylabel('clear sky output c')
 
plt.figure()
plt.plot(s.value)
plt.title('plot for s ')
plt.ylabel('shading loss component s')
 
plt.figure()
plt.plot(r.value)
plt.title('plot for  r ')
plt.ylabel('residual errors')
 
plt.figure()
plt.plot(p)
plt.title('plot for  p')
plt.ylabel('PV array output time series')