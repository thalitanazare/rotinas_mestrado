#%%
# Artigo 1(NMB2013): Improved Structure Detection For Polynomial NARX Models Using a Multiobjective Error Reduction Ratio
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import math 


N=500 #número de iterações
var=0.05 #variância do ruído branco da entrada

mu=0 #média zero
sigma=0.001 #desvio padrão
v=math.sqrt(var)*np.random.normal(mu,sigma,N) #ruído branco entrada

u=np.zeros((1, 1))
lag=1
for k in range(lag, len(v)):
       u = np.append( u,0.5*u[k-1] + v[k])

plt.plot(u)
#%% Sistema Original
theta = np.array([[0.5], [0.8], [1], [-0.05], [0.5]])

e = np.random.normal(mu,sigma, N) #ruído branco saída
y = np.zeros((1, 1))# condições iniciais

for k in range(lag, len(e)):
        y =  np.append( y, theta[0]*y[k-1] + theta[1]*u[k-2] \
            + theta[2]*u[k-1]**2 + theta[3]*y[k-2]**2 + e[k])

plt.plot(y)
# %% MERR 1
theta1 = np.array([[0.479], [0.8936], [0.2121], [0], [1.3504]])

y1 = np.zeros((1, 1))# condições iniciais

for k in range(lag, len(e)):
        y1 =  np.append( y1, theta1[0]*y1[k-1] + theta1[1]*u[k-2] \
            + theta1[2]*u[k-1]**2 + theta1[3]*y1[k-2]**2 + e[k])

plt.plot(y1)
plt.plot(y)
# %% MERR 2
theta2 = np.array([[0.4962], [0.7904], [0.9962], [0], [0.5446]])

y2 = np.zeros((1, 1))# condições iniciais

for k in range(lag, len(e)):
        y2 =  np.append( y2, theta2[0]*y2[k-1] + theta2[1]*u[k-2] \
            + theta2[2]*u[k-1]**2 + theta2[3]*y2[k-2]**2 + e[k])

plt.plot(y2)
plt.plot(y)

# %% MERR 3 e 4
theta3 = np.array([[0.4932], [0.8007], [0.996], [-0.0491], [0.5355]])

y3 = np.zeros((1, 1))# condições iniciais

for k in range(lag, len(e)):
        y3 =  np.append( y3, theta3[0]*y3[k-1] + theta3[1]*u[k-2] \
            + theta3[2]*u[k-1]**2 + theta3[3]*y3[k-2]**2 + e[k])

plt.plot(y3)
plt.plot(y)

# %% MERR 5
theta5 = np.array([[0.5098], [0.8436], [1.0185], [-0.049], [0.5199]])

y5 = np.zeros((1, 1))# condições iniciais

for k in range(lag, len(e)):
        y5 =  np.append( y5, theta5[0]*y5[k-1] + theta5[1]*u[k-2] \
            + theta5[2]*u[k-1]**2 + theta5[3]*y5[k-2]**2 + e[k])

plt.plot(y5)
plt.plot(y)

#-------CÁLCULOS DOS RMSE DE CADA COMBINAÇÃO DE MERR COM O SISTEMA ORIGINAL

# %% 
n1 = np.square(np.sum((y-y1)**2))
d1 = np.square(np.sum((y - np.mean(y1))**2))
rmse1=np.sqrt(np.divide(n1, d1))
print(rmse1)
# %%
n2 = np.square(np.sum((y-y2)**2))
d2 = np.square(np.sum((y - np.mean(y2))**2))
rmse2=np.sqrt(np.divide(n2, d2))
print(rmse2)
# %%
n3 = np.square(np.sum((y-y3)**2))
d3 = np.square(np.sum((y - np.mean(y3))**2))
rmse3=np.sqrt(np.divide(n3, d3))
print(rmse3)

# %%
n5 = np.square(np.sum((y-y5)**2))
d5 = np.square(np.sum((y - np.mean(y5))**2))
rmse5=np.sqrt(np.divide(n5, d5))
print(rmse5)
# %%
