#importing libraries
import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

#data according to our problem
#gain matrix G is given
Gain_mat = np.array([[1.0,0.1,0.2,0.1,0.0],
                [0.1,1.0,0.1,0.1,0.0],
                [0.2,0.1,2.0,0.2,0.2],
                [0.1,0.1,0.2,1.0,0.1],
                [0.0,0.0,0.2,0.1,1.0]])

# n transmitters and n recievers we have

n,_ = np.shape(Gain_mat)

# set maximum power of each transmitter and receiver saturation level
P_sat = np.array([3.]*n)
P_sat = P_sat.reshape((n,1))

# normalised received power, total possible would be all power from all transmitters so 1/n
P_received = (np.array([5.,5.,5.,5.,5.]))
P_received = P_received.reshape((n,1))
P_received_norm=P_received/n #for the sake of normalising


# set noise level according to our problem
sigma = np.array([0.5,0.5,0.5,0.5,0.5])
sigma = sigma.reshape((n,1))

# group matrix: number of groups by number of transmitters
#Group 1- 1 and 2 
#Group 2- 3,4 and 5
Groups2 = np.array([[1.,1.,0,0,0],[0,0,1.,1.,1.]])


# max normalised power for groups, 4/2 and 6/3
Group_max = np.array([[2.0],[2.0]])


identity_matrix = np.identity(n)

SignalPower = Gain_mat*identity_matrix # signal power matrix

Interference = Gain_mat-SignalPower # interference power matrix



#number of groups calculated from Groups2
number_groups = int(np.size(Groups2,0))


# normalising the max power of a group so it is in the range [0,1]
Group_normalisation = Groups2/np.sum(Groups2,axis=1).reshape((number_groups,1))

# create scalar optimisation variable p: the power of the n transmitters
powers = cp.Variable((n,1),name="powers")

#linear fractional problem

# alpha defines the sub-level sets of the generalised linear fractional problem

# in this case α is the reciprocal of the minimum SINR
#cvxpy variable declaration
alpha = cp.Parameter(shape=1,name="alpha value")

# set up the constraints for the bisection feasibility algo test
constraints=[]
constraints = [Interference*powers + sigma <= alpha*SignalPower*powers]
constraints+=[Group_normalisation*powers <= Group_max]
constraints+=[Gain_mat*powers <= P_received_norm]
constraints+=[powers >= 0]
constraints+=[powers <= P_sat]

# define objective function, in our case it's constant as only want to test the solution's feasibility

#we need to maximize minimum required sinr and alpha is reciprocal of sinr ,so objective will be minimize alpha

#objective is
objective = cp.Minimize(alpha)

#convex problem is

prob = cp.Problem(objective, constraints)

print("Convex optimization problem is:",prob)

#Bisection algorithm 

accuracy_order=0.05 #accuracy order given in question

#initialize to 0 to bisection algo solution'

best_powers = np.zeros((n))

# set upper and lower bounds for sub-level set
upper = 1e4
lower = 0

# Bisection algortithm procedure

max_iterations = int(1e7) #maximum iterations taken

for i in range(1,max_iterations):
# First check that upper is in the feasible domain and lower is not, loop finishes here if this is not the case

# set α as the midpoint of the interval
   alpha.value = np.atleast_1d((upper + lower)/2.0)

# test the size of the interval against the specified tolerance
   if upper-lower <= accuracy_order:
         break

   #solve problem
   #solving the problem
   try:
      prob.solve()
   except Exception as e:
      print(e)
   #print("optimal status:",prob.status)
   #print("our minimised  objective is:",prob.solve())

   # If the problem is feasible upper will be alpha, if not lower will be alpha , best takes the last feasible value as the optimal one as
   # when the tolerance is reached, the new alpha could be out of bounds
   if prob.status == 'optimal':
         upper = alpha.value
         best_powers = powers.value
   else:
         lower = alpha.value

   # final condition to check that the interval has converged to order ε, i.e. the range of the optimal sublevel set is <=ε
   if i == (max_iterations-1) and  upper - lower > accuracy_order :
          print("Solution not converged to given accuracy order ")

#sinr value is
#allocating sinr value

sinr=1/alpha.value  
sinr

# feasibility of convex problem check
prob.status=='optimal'

#displaying all required results

print("optimized problem status:",prob.status)
print('Maximized Minimum SINR required at reciever is =%0.4g'%(sinr))
print("powers that maximize minimum sinr required is given by:")
print('Power=%s'%(best_powers))