import numpy as np
import matplotlib.pyplot as plt

# Reference trajectory 
global xref 
xref = [(k-5)**2 for k in range(0,11)]
x0 = range(0,11)
optimal_cost_table = np.zeros([10,10])
print(optimal_cost_table)

# Dynamics
def fk(xk, uk, wk):
    return xk + uk*wk

# Get all possible control actions for a given state 
def get_u(xk):
    return range(0, 10-xk)

# Stage costs
def gk(k, xk, uk):
    if k == 10:
        cost = xk**2
    else:
        cost = (xk - xref[k])**2 + uk**2
    return cost

for x in x0:







