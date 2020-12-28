
# Artigo Aguirre1995: Retrieving Dynamical Invariants from Chaotic Data Using NARMAX Models
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import math as mt

# Equação Original
x=np.random.rand(2)

print(x)
h=2
N=160

for k in range(h,N):
    x = np.append(x, 1 - 1.4*mt.pow(x[k-1],2) + 0.3*x[k-2] )

# Modelo do sistema
x1=[x[0], x[1], x[2]]
h=3
print(x1)
for i in range(h,N):
    x1 = np.append(x1, -1.3772*x1[i-1]**2 + 0.96958 \
                        + 0.00083*x1[i-1]**2*x1[i-3] \
                        + 0.3410*x1[i-2] - 0.03352*x1[i-1]*x1[i-2]*x1[i-3]\
                        - 0.04836*x1[i-1]*x1[i-3]**2 )


# Comparação usando duas formas matemáticas do modelo
x2=[x[0], x[1], x[2]]
h=3
print(x2)
for l in range(h,N):
    x2 = np.append(x2, -1.3772*x2[l-1]*x2[l-1] + 0.96958 \
                        + 0.00083*x2[l-1]*x2[l-1]*x2[l-3] \
                        + 0.3410*x2[l-2] - 0.03352*x2[l-1]*x2[l-2]*x2[l-3]\
                        - 0.04836*x2[l-1]*x2[l-3]*x2[l-3] )

plt.figure(figsize=(16, 8))
plt.plot(x1)
plt.plot(x2)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('Número de Iterações',fontsize=20)
plt.title('Mapa de Hénon', fontsize=20)

