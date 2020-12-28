# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:58:34 2020

@author: thali
"""


# Artigo Aguirre1995: Retrieving Dynamical Invariants from Chaotic Data Using NARMAX Models
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import mpmath as mp
from mpmath import *
from ivmpftools import *

# Equação Original
x=np.array([iv.mpf(mp.rand())], dtype=object)
for k in range(1,2):
    x= np.append(x, np.array([iv.mpf(mp.rand())], dtype=object) )

h=2
N=200
iv.dps=100

for k in range(h,N):
    x = np.append(x, 1 - 1.4*x[k-1]**2 + 0.3*x[k-2] )


# Modelo do sistema
x1=[x[0], x[1], x[2]]
h=3

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

x_p = ivmpf_disassembler(x)
x_p1 = ivmpf_disassembler(x1)
x_p2 = ivmpf_disassembler(x2)


plt.figure(figsize=(16, 8))
plt.plot(x_p[:,0],'k',linewidth=2)
plt.plot(x_p[:,1],'k',linewidth=2)
plt.figure(figsize=(16, 8))
plt.plot(x_p1[:,0],linewidth=5)
plt.plot(x_p1[:,1],linewidth=5)
plt.plot(x_p2[:,0],linewidth=2)
plt.plot(x_p2[:,1],linewidth=2)