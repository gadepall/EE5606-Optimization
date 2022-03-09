

import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
N=30
n_list=[5,10,20]
m=2*N+1
#L2 norm
x=np.linspace(-1,1,m)
costValue=np.array([])
c=1
for n in n_list:
  X=np.array([])
  f=x**n
  for i in range(n):
      X=np.append(X,[x**i])
  X=X.reshape(n,m)
  f=f.reshape(1,m)

  a=cp.Variable((n,1))
  cost=cp.sum_squares(f-a.T@X)
  prob = cp.Problem(cp.Minimize(cost))
  prob.solve()
  costValue=np.append(costValue,prob.value)
  print("The coefficients (ai) for n =",n,"are",a.value.T,)
  print("The value of cost function is",prob.value,"\n")
  
  #Plot of actual values and predicted values 
  plt.subplot(1,3,c)
  plt.scatter(x.reshape(1,m),f,s=20,label='actual values')
  plt.scatter(x.reshape(1,m),a.value.T@X,s=5,label='predicted values')
  plt.xlabel("x")
  plt.legend()
  
  c+=1

#Plot of n values and cost
plt.figure(2)
plt.scatter(n_list,costValue)
plt.title("Plot showing cost as a function of n")
plt.xlabel("n")
plt.ylabel("cost")

#L1 norm
x=np.linspace(-1,1,m)
costValue=np.array([])
c=1
for n in n_list:
  X=np.array([])
  f=x**n
  for i in range(n):
      X=np.append(X,[x**i])
  X=X.reshape(n,m)
  f=f.reshape(1,m)

  a=cp.Variable((n,1))
  cost=cp.sum(cp.abs( f-a.T@X))
  #cost=cp.sum_squares(f-a.T@X)
  prob = cp.Problem(cp.Minimize(cost))
  prob.solve()
  costValue=np.append(costValue,prob.value)
  print("The coefficients (ai) for n =",n,"are",a.value.T,)
  print("The value of cost function is",prob.value,"\n")
  
  #Plot of actual values and predicted values 
  plt.subplot(1,3,c)
  plt.scatter(x.reshape(1,m),f,s=20,label='actual values')
  plt.scatter(x.reshape(1,m),a.value.T@X,s=5,label='predicted values')
  plt.xlabel("x")
  plt.legend()
  
  c+=1

#Plot of n values and cost
plt.figure(2)
plt.scatter(n_list,costValue)
plt.title("Plot showing cost as a function of n")
plt.xlabel("n")
plt.ylabel("cost")