
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

def cost_array(u):
  uplus=cp.maximum(u,0)
  uminus=cp.maximum(-u,0)
  phi_fill=cp.square(uplus)*2+ uplus*30
  phi_cut=cp.square(uminus)*12+ uminus
  cost=phi_fill+phi_cut
  return cost

#Data given to us
n=100
x=np.linspace(1,101,100)
e=np.array([5*np.sin(i/(n*3*np.pi))+np.sin(i/(n*10*np.pi)) for i in x]) #1st expression as given in pdf is used
#e=np.array([5*np.sin((3*np.pi*i)/n)+np.sin((10*np.pi*i)/n) for i in x])
d=np.arange(1,101,1)

D=[0.08,0.025,0.005] #Constraints gradient vector

#Reshaping vectors
e=np.reshape(e,(n,1))
d=np.reshape(d,(n,1))

#CVXPY VARIABLE
h=cp.Variable((n,1))
u=h-e

#Constraints declaration
constraints=[]
#derivatives
G1=np.zeros((n,1))
G2=np.zeros((n,1))
G3=np.zeros((n,1))

for i in range(1,n):
  np.append(G1,(h[i]-h[i-1]))
for i in range(1,n-1):
  np.append(G2,(G1[i]-G1[i-1]))
for i in range(1,n-2):
  np.append(G3,(G2[i]-G2[i-1]))
for i in range(1,n-1):
  np.append(constraints,cp.abs(cp.max(G1[i]))<=D[0])
for i in range(1,n-2):
  np.append(constraints,cp.abs(cp.max(G2[i]))<=D[1])
for i in range(1,n-3):
  np.append(constraints,cp.abs(cp.max(G3[i]))<=D[2])


cost=cost_array(u)

obj=cp.Minimize(cp.sum(cost))

prob=cp.Problem(obj,constraints)
try:
   prob.solve()
except Exception as e:
  print(e)
print("optimal status:",prob.status)
print("our minimized cost:",prob.solve())
print("height values are",h.value)

plt.plot(h.value,d)
plt.xlabel("d")
plt.ylabel("height")
plt.title("height of Hill")

plt.plot((h.value-e),d) #u=h-e
plt.xlabel("d")
plt.ylabel("u")
plt.title("u plot")

#fill and cut function function plot
U=np.arange(1,11,0.1)
Uplus=np.array([max(u,0) for u in U])
  
phi_fill=np.array([np.square(uplus)*2+ uplus*30 for uplus in Uplus])
phi_fill=np.reshape(phi_fill,(100,-1))
plt.subplot(1,2,1)
plt.plot(U,phi_fill)
plt.title("fill function")
U=np.arange(1,11,0.1)
Uminus=np.array([max((u),0) for u in U])
phi_cut=np.array([np.square(uminus)*12+ uminus for uminus in Uminus])
plt.subplot(1,2,2)
plt.title("cut function")
plt.plot((-U),phi_cut)

#CONVEXITY CAN BE SEEN FROM GRAPGH

plt.plot(d,e)
plt.xlabel("d")
plt.ylabel("elevation")
plt.title("Elevation of Hill")

type(cost)

cost

print(type(e))