# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:28:46 2020

@author: thali
"""

# Artigo NMLM2018 Equação de Mackey-Glass

import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import mpmath as mp
from mpmath import *
from ivmpftools import *
# Modelo Eq. 18 do artigo 

N=350
iv.dps = 500
x=np.array([iv.mpf(mp.rand())], dtype=object)
for k in range(1,10):
    x= np.append(x, np.array([iv.mpf(mp.rand())], dtype=object) )


x1=x
h=10

for k in range(h,N):
    x = np.append(x, 0.24662*10*x[k-1] - 0.16423*10*x[k-2]\
                    + 0.60992*x[k-3] + 0.73012e-1*x[k-5]**2*x[k-10]**2\
                    + 0.38566*x[k-3]*x[k-10]\
                    + 0.66999*x[k-1]*x[k-10]**2\
                    + 0.88364*x[k-1]**3\
                    - 0.67300*x[k-4]*x[k-10]**2\
                    - 0.11929*10*x[k-1]**2\
                    - 0.50451e-1*x[k-4]*x[k-5] - 0.24765*x[k-1]**4\
                    + 0.42081*x[k-4]*x[k-9]*x[k-10]**2\
                    - 0.70406*x[k-1]*x[k-10]**3\
                    - 0.14089*x[k-5]*x[k-8]**2\
                    + 0.14807*x[k-1]*x[k-7]*x[k-10]   )





for i in range(h,N):
    x1 = np.append(x1, 0.24662*(10*x1[i-1]) - 0.16423*10*x1[i-2]\
                    + 0.60992*x1[i-3] + 0.73012e-1*x1[i-5]**2*x1[i-10]**2\
                    + 0.38566*x1[i-3]*x1[i-10]\
                    + 0.66999*x1[i-1]*x1[i-10]**2\
                    + 0.88364*x1[i-1]**3\
                    - 0.67300*x1[i-4]*x1[i-10]**2\
                    - 0.11929*10*x1[i-1]**2\
                    - 0.50451e-1*x1[i-4]*x1[i-5] - 0.24765*x1[i-1]**4\
                    + 0.42081*x1[i-4]*x1[i-9]*x1[i-10]**2\
                    - 0.70406*x1[i-1]*x1[i-10]**3\
                    - 0.14089*x1[i-5]*x1[i-8]**2\
                    + 0.14807*x1[i-1]*x1[i-7]*x1[i-10]   )


x_p = ivmpf_disassembler(x)
x_p1 = ivmpf_disassembler(x1)

plt.figure(figsize=(16, 8))
plt.plot(x_p[:,0],'k',linewidth=5)
plt.plot(x_p[:,1],'k',linewidth=5)
plt.plot(x_p1[:,0],linewidth=1)
plt.plot(x_p1[:,1],linewidth=1)
