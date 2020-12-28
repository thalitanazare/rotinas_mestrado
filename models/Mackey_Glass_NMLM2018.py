#%% Artigo NMLM2018 Equação de Mackey-Glass

import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import math as mt

# Modelo Eq. 18 do artigo 

N=2500
x=np.random.rand(10)
x1=x
h=10
print(x)

for k in range(h,N):
    x = np.append(x, 0.24662*10*x[k-1] - 0.16423*10*x[k-2]\
                    + 0.60992*x[k-3] + 0.73012e-1*mt.pow(x[k-5],2)*mt.pow(x[k-10],2)\
                    + 0.38566*x[k-3]*x[k-10]\
                    + 0.66999*x[k-1]*mt.pow(x[k-10],2)\
                    + 0.88364*mt.pow(x[k-1],3)\
                    - 0.67300*x[k-4]*mt.pow(x[k-10],2)\
                    - 0.11929*10*mt.pow(x[k-1],2)\
                    - 0.50451e-1*x[k-4]*x[k-5] - 0.24765*mt.pow(x[k-1],4)\
                    + 0.42081*x[k-4]*x[k-9]*mt.pow(x[k-10],2)\
                    - 0.70406*x[k-1]*mt.pow(x[k-10],3)\
                    - 0.14089*x[k-5]*mt.pow(x[k-8],2)\
                    + 0.14807*x[k-1]*x[k-7]*x[k-10]   )



for i in range(h,N):
    x1 = np.append(x1, 0.24662*(10*x1[i-1]) - 0.16423*10*x1[i-2]\
                    + 0.60992*x1[i-3] + 0.73012e-1*mt.pow(x1[i-5],2)*mt.pow(x1[i-10],2)\
                    + 0.38566*x1[i-3]*x1[i-10]\
                    + 0.66999*x1[i-1]*mt.pow(x1[i-10],2)\
                    + 0.88364*mt.pow(x1[i-1],3)\
                    - 0.67300*x1[i-4]*mt.pow(x1[i-10],2)\
                    - 0.11929*10*mt.pow(x1[i-1],2)\
                    - 0.50451e-1*x1[i-4]*x1[i-5] - 0.24765*mt.pow(x1[i-1],4)\
                    + 0.42081*x1[i-4]*x1[i-9]*mt.pow(x1[i-10],2)\
                    - 0.70406*x1[i-1]*mt.pow(x1[i-10],3)\
                    - 0.14089*x1[i-5]*mt.pow(x1[i-8],2)\
                    + 0.14807*x1[i-1]*x1[i-7]*x1[i-10]   )

plt.figure(figsize=(16, 8))
plt.plot(x1[1500:2500])
plt.plot(x[1500:2500])
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('Número de Iterações (2500 pontos) - Intervalo de 1500 a 2500',fontsize=20)
plt.title('Equação de Mackey-Glass', fontsize=20)
plt.savefig('mackeyglass.png', format='png')
# %%
