# -*- coding: utf-8 -*-
"""
Intervalos com Python

atualização: 12/11/2020
"""
#Pacotes necessários
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from mpmath import *
from ivmpftools import *

iv.dps = 1000
y = np.array([iv.mpf(mp.rand())], dtype=object)
r = 3.9
#r = iv.mpf('3.9')
h=1
N=1600


for k in range(h,N):
    y = np.append(y, r*y[k-1] - r*y[k-1]**2)


# Modelo Formualação Matemática Modificada
y1=[y[0]]

for k in range(h,N):
    y1 = np.append(y1, y1[k-1]*(r - r*y1[k-1]))
    
    
    
    
    
y_p = ivmpf_disassembler(y)
y_p1 = ivmpf_disassembler(y1)

plt.figure(figsize=(16, 8))
#plt.plot(y_p[:,0],'k',linewidth=5)
#plt.plot(y_p[:,1],'k',linewidth=5)
plt.plot(y_p1[:,0],linewidth=1)
plt.plot(y_p1[:,1],linewidth=1)


