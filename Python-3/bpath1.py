#BPATH1 Brownian path simulation
#
# Adapted from 
# Desmond J. Higham "An Algorithmic Introduction to Numerical Simulation of 
#                    Stochastic Differential Equations"
#
# http://www.caam.rice.edu/~cox/stoch/dhigham.pdf

import numpy as np
import matplotlib.pyplot as plt


np.random.seed(100) # set the random seed
T=1; N=500; dt=float(T)/N
dW = np.zeros(N) # preallocate arrays ...
W = np.zeros(N) # for efficiency

dW[1] = np.sqrt(dt)*np.random.randn(1) # first approximation outside the loop ...
W[1] = dW[1] 

for j in range(2,N):
    dW[j] = np.sqrt(dt) * np.random.randn(1) #  general increment
    W[j] = W[j-1] + dW[j]


plt.plot(W,'r-') # plot W against t
plt.xlabel('t',fontsize=16)
plt.ylabel('W(t)',fontsize=16, rotation=90)

plt.show()