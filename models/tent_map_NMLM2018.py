#%% 
# Artigo 2: On the Use of Interval Extensions to Estimate the Largest Lyapunov Exponent from Chaotic Data
# Mapa Tenda

import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import math as mt

N=200

x1=[0.4]
print(x1)
h=1
for k in range(h,N):
    x1 = np.append(x1, 1 - 1.999*abs(x1[k-1]-0.5))

plt.scatter(x1[:-1],x1[1:])

#%%

x=np.array([x1[0], x1[1], x1[2]])
h=3

print(x)

for i in range(h, N):
    x = np.append(x, 0.1133*x[i-1] + 14.0488*mt.pow(x[i-1],4) + 0.5214\
                    - 28.3140*mt.pow(x[i-1],3) + 14.2003*mt.pow(x[i-1],2)\
                    - 1.9861*x[i-2] + 1.9682*mt.pow(x[i-2],2))

plt.scatter(x[:-1],x[1:])

# %%
