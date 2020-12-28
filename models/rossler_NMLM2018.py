
#%% 
# Artigo 2: On the Use of Interval Extensions to Estimate the Largest Lyapunov Exponent from Chaotic Data
import numpy as np
from numpy import random
#import pandas as pd
import matplotlib.pyplot as plt
import math as mt

N=3000 #número de iterações
# maior que isso dá NaN

# Condições Iniciais: Não especifica no artigo
x = np.array([[0.1],[0.1],[0.1],[0.1],[0.1]])

# Primeira equação sem modificação
for i in range(5,N):
    x = np.append( x, 0.1972*10*x[i-1] - 0.104*10*x[i-2] \
                  + 0.7456e-4*x[i-4]*mt.pow(x[i-2],3)*x[i-1] \
                  - 0.2053e-4*x[i-5]*mt.pow(x[i-4],4)\
                  - 0.285e-4*x[i-5]*mt.pow(x[i-1],4)\
                  + 0.2484e-4*mt.pow(x[i-3],2)*mt.pow(x[i-2],3)\
                  + 0.1238e-2*x[i-2]*mt.pow(x[i-1],2)\
                  + 0.4353e-4*mt.pow(x[i-5],4)\
                  + 0.2258e-2*x[i-5]*x[i-2]*mt.pow(x[i-1],2)\
                  + 0.3123e-4*mt.pow(x[i-4],5)\
                  + 0.7531e-3*mt.pow(x[i-1],4)\
                  - 0.2703e-2*mt.pow(x[i-3],2)*mt.pow(x[i-1],2)\
                  - 0.7807e-3*mt.pow(x[i-1],3)\
                  - 0.7077e-4*mt.pow(x[i-3],2)*mt.pow(x[i-2],2)*x[i-1]\
                  - 0.3304e-3*x[i-3]*mt.pow(x[i-2],3)\
                  - 0.8847e-2*x[i-5]*x[i-1]\
                  + 0.7631e-2*x[i-4]*x[i-1]\
                  - 0.3870e-4*mt.pow(x[i-5],3)*mt.pow(x[i-1],2)\
                  + 0.4676e-3*mt.pow(x[i-3],3)*x[i-1] )
plt.figure()
plt.plot(x)

# Segunda equação alterando formulação matemática linha 2
x1 = np.array([[0.1],[0.1],[0.1],[0.1],[0.1]])
for i in range(5,N):
    x1 = np.append( x1, 0.1972*10*x1[i-1] - 0.104*10*x1[i-2] \
                  + 0.7456e-4*x1[i-4]*x1[i-2]*mt.pow(x1[i-2],2)*x1[i-1] \
                  - 0.2053e-4*x1[i-5]*mt.pow(x1[i-4],4)\
                  - 0.285e-4*x1[i-5]*mt.pow(x1[i-1],4)\
                  + 0.2484e-4*mt.pow(x1[i-3],2)*mt.pow(x1[i-2],3)\
                  + 0.1238e-2*x1[i-2]*mt.pow(x1[i-1],2)\
                  + 0.4353e-4*mt.pow(x1[i-5],4)\
                  + 0.2258e-2*x1[i-5]*x1[i-2]*mt.pow(x1[i-1],2)\
                  + 0.3123e-4*mt.pow(x1[i-4],5)\
                  + 0.7531e-3*mt.pow(x1[i-1],4)\
                  - 0.2703e-2*mt.pow(x1[i-3],2)*mt.pow(x1[i-1],2)\
                  - 0.7807e-3*mt.pow(x1[i-1],3)\
                  - 0.7077e-4*mt.pow(x1[i-3],2)*mt.pow(x1[i-2],2)*x1[i-1]\
                  - 0.3304e-3*x1[i-3]*mt.pow(x1[i-2],3)\
                  - 0.8847e-2*x1[i-5]*x1[i-1]\
                  + 0.7631e-2*x1[i-4]*x1[i-1]\
                  - 0.3870e-4*mt.pow(x1[i-5],3)*mt.pow(x1[i-1],2)\
                  + 0.4676e-3*mt.pow(x1[i-3],3)*x1[i-1] )
plt.figure()
plt.plot(x)

plt.figure()
plt.plot(x1)


plt.figure()
plt.plot(x[1800:2500])
plt.plot(x1[1800:2500])

# %%

# %%
