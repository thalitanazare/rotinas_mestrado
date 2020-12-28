#%% Artigo Aguirre1995
#fazendo pequena alteração
#segundo teste
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import math as mt

# Modelo Artigo Aguirre1995

N=150
y=np.random.rand(1)
h=1
r=3.9

for k in range(h,N):
    y = np.append(y, r*y[k-1] - r*y[k-1]**2)


# Modelo Formualação Matemática Modificada
y1=[y[0]]

for k in range(h,N):
    y1 = np.append(y1, y1[k-1]*(r - r*y1[k-1]))



plt.figure(figsize=(16, 8))
plt.plot(y,linewidth=2)
plt.plot(y1)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('Número de Iterações',fontsize=20)
plt.title('Mapa Logistico', fontsize=20)
plt.savefig('logistico.png', format='png')
# %%
