#%%
# Artigo 1: Utilizando agora a equação do buck dc-dc 
# as equações são do artigo Aguirre(que é o sistema original)
# e as equações encontradas com MERR do artigo
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import math as mt

data_val=np.loadtxt("buck_val.dat")
#decimação de 12: pega a cada 12 pontos. Vem da autocovariância
# cap 12.2.4 do aguirre. Verificar como calcula a autocovar para verificar esses valores. 
temp_val = data_val[::12,0]
u = data_val[::12,1]
out_val = data_val[::12,2]

N=80
h=3

# Equação retirada do artigo do aguirre: sistema original
y=np.array([out_val[0], out_val[1], out_val[2]])

for k in range(h,len(u)):
    y = np.append(y, 1.2013*y[k-1] - 2.6082e-1*y[k-2]\
                     + 6.2479 - 2.6783*mt.pow(u[k-1],3)\
                     - 2.0807e-1*y[k-3] + 8.8399*mt.pow(u[k-1],2)*u[k-3]\
                     + 3.6636*mt.pow(u[k-3],3)\
                     - 6.1623e-1*u[k-1]*u[k-3]\
                     - 9.7707*u[k-1]*mt.pow(u[k-3],2))

# MERR 1
y1=np.array([out_val[0], out_val[1], out_val[2]])

for k in range(h,len(u)):
    y1 = np.append(y1, - 2.1340*u[k-1] - 2.8396*u[k-2]\
                       + 1.6168*y1[k-1] - 1.1554*y1[k-2]\
                       - 0.0863*mt.pow(y1[k-1],2) - 0.0744*mt.pow(y1[k-2],2)\
                       + 0.1519*y1[k-2]*y1[k-1] + 0.2079*u[k-2]*y1[k-2] + 13.9972 )

# MERR 2
y2=np.array([out_val[0], out_val[1], out_val[2]])

for k in range(h,len(u)):
    y2 = np.append(y2, - 2.1340*u[k-1] - 2.8396*u[k-2]\
                       + 1.6168*y2[k-1] - 1.1554*y2[k-2]\
                       - 0.0863*mt.pow(y2[k-1],2) - 0.0744*mt.pow(y2[k-2],2)\
                       + 0.1519*y2[k-2]*y2[k-1] + 0.2079*u[k-2]*y2[k-2] + 13.9972 )



# MERR 3
y3=np.array([out_val[0], out_val[1], out_val[2]])

for k in range(h,len(u)):
    y3 = np.append(y3, - 0.7677*u[k-1] - 0.4849*y3[k-1] \
                       + 0.1546*y3[k-2] - 3.0944*mt.pow(u[k-1],2)\
                       + 0.3150*mt.pow(u[k-2],2)\
                       + 1.2441*u[k-2]*u[k-1]\
                       + 0.7952*u[k-1]*y3[k-1]\
                       - 0.3438*u[k-2]*y3[k-2] + 14.0006)

# MERR 4
y4=np.array([out_val[0], out_val[1], out_val[2]])

for k in range(h,len(u)):
    y4 = np.append(y4,  - 5.6780*u[k-1] + 9.3834*u[k-2]\
                        - 0.0396*y4[k-1] - 1.0472*y4[k-2]\
                        - 0.8788*mt.pow(u[k-1],2)\
                        - 2.0131*mt.pow(u[k-2],2)\
                        + 0.0152*mt.pow(y4[k-2],2)\
                        + 0.5945*u[k-1]*y4[k-1]\
                        + 14.0005)

plt.plot(out_val)
plt.plot(y)
plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.plot(y4)




# %% 
n1 = np.square(np.sum((out_val-y1)**2))
d1 = np.square(np.sum((out_val - np.mean(y1))**2))
rmse1=np.sqrt(np.divide(n1, d1))
print(rmse1)
# %%
n2 = np.square(np.sum((out_val-y2)**2))
d2 = np.square(np.sum((out_val - np.mean(y2))**2))
rmse2=np.sqrt(np.divide(n2, d2))
print(rmse2)
# %%
n3 = np.square(np.sum((out_val-y3)**2))
d3 = np.square(np.sum((out_val - np.mean(y3))**2))
rmse3=np.sqrt(np.divide(n3, d3))
print(rmse3)
# %%
n4 = np.square(np.sum((out_val-y4)**2))
d4 = np.square(np.sum((out_val - np.mean(y4))**2))
rmse4=np.sqrt(np.divide(n4, d4))
print(rmse4)
# %%


# %%
