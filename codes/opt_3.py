import cvxpy as cp
import numpy as np
wall_area_const = 200
floor_area_const = 60
a=0.8
b=1.2

#cvxpy variables declaration

h = cp.Variable(pos=True, name="h")
w = cp.Variable(pos=True, name="w")
d = cp.Variable(pos=True, name="d")


#from our knowledge
volume_box = h * w * d
wall_area = 2 * (h * w + h * d)
flr_area = w * d
hw_ratio = h/w
dw_ratio = d/w

#constraints declaration
constr = []
constr+=[wall_area <= wall_area_const]
constr+=[flr_area <= floor_area_const]
constr+=[hw_ratio >= a]
constr+=[hw_ratio <= b]
constr+=[dw_ratio >= a]
constr+=[dw_ratio <= b]


#objective declaration
objective=cp.Maximize(volume_box)
#objective=cp.Minimize(cp.exp(-(y1+y2+y3)))
prob = cp.Problem(objective,constr)
print("our convex optimized problem is")
print(prob)
try:
   prob.solve(gp=True)
except Exception as e:
  print(e)
print("optimal status:",prob.status)
print("our maximized volume is:",prob.solve(gp=True))
#printing h,d,w values that maximizes volume of the box
print("value of h(height) that maximizes volume of box is",h.value)
print("value of d(depth) that maximizes volume of box is",d.value)
print("value of w(width) that maximizes volume of box is",w.value)