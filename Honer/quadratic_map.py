# -*- coding: utf-8 -*-
"""
* GERANDO DADOS DO MODELO DE REFERÊNCIA, SIMULADO COM PACOTE MPMATH PARA MELHORA
DA PRECISÃO. 
* ESSE MODELO FOI OBTIDO COM PACOTE SYSIDENTPY A PARTIR DO SISTEMA ORIGINAL.
* AS CONDIÇÕES INICIAIS APRESENTADAS AQUI TAMBÉM FORAM OBTIDAS DO SISTEMA ORIGINAL
* TODAS ESSAS SIMULAÇÕES FORAM REALIZADAS NOS ARQUIVOS DAS PASTAS MODELS E
MODELS-INTERVAL
----------------------------------------------------------------------------------
Para comparar serão simuladas duas versões do modelo, uma com a forma original
outra trocando o ** pela sua expansão. Esse será o critério para decidir qual
a precisão que iremos utilizar. 
====================================
Created on Thu Nov 12 20:57:13 2020

@author: thalitanazare

Version: 1.1 - 15/11/2020

====================================
"""

# Pacotes Básicos
import numpy as np #Usado para construir os dados de entrada do algoritmo
from numpy import random
import matplotlib.pyplot as plt #Gerar gráficos
import pandas as pd #Exibit tabelas organizadas com DataFrame
import math as mt
import csv
# Pacotes mpmath 
import mpmath as mp
from mpmath import *

# Início Programa
N=300
p=80
mp.dps=p
y=[mp.mpf('0.966287829861518'),mp.mpf('0.9662878298615181')] #cond inicial
y2=y
h=2


with open("dados/mq.csv", "w", newline='') as mq: 
    dados = csv.writer(mq)
    for k in range(h,N):
        y = np.append(y, 0.6435*y[k-2]**2 - y[k-1]**2 + 0.6774 + 0.6435*y[k-1])
        dados.writerow([y[k]])

"""
with -> para salvar em csv. chamo o path que quero salvar. 
no caso criei uma pasta dentro do diretório que está meu .py
então, chamo o path dados/mp.csv. o arquivo mq.csv já tem que estar criado
"w" é de escrever
newline'' é para não saltar uma linha ao escrever, e sim ficar uma seguida
da outra. 
"""

for k in range(h,N):
    y2 = np.append(y2, 0.6435*y2[k-2]*y2[k-2] - y2[k-1]*y2[k-1] + 0.6774 + 0.6435*y2[k-1])
    
    
#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(y,color='black', label='y',alpha = 1,linewidth=2)
plt.plot(y2,color='orange', label='y2',alpha = 1,linewidth=2)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('k',fontsize=20,**csfont)
plt.ylabel('y(k)', fontsize=20,**csfont)
plt.title('Modelo Mapa Quadrático - Precisão: %i' %p, fontsize=20,**csfont)
#plt.legend(loc=2,fontsize=19)
#plt.savefig('/Users/thali/Desktop/mestrado2020/Andamento/Python/modelos_com_intervalos/imagens/mapa_quadratico/modelo_mp_mpf.png')


#%%==============================================================================
# SIMULANDO COM NUMPY PARA COMPARAR COM Y (UTILIZANDO EQUAÇÃO ORIGINAL)

# Início Programa

ynp=[0.966287829861518,0.9662878298615181] #cond inicial
h=2


for k in range(h,N):
    ynp = np.append(ynp, 0.6435*ynp[k-2]**2 - ynp[k-1]**2 + 0.6774 + 0.6435*ynp[k-1])



#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(y,color='black', label='yMP',alpha = 1,linewidth=2)
plt.plot(ynp,color='red', label='yNP',alpha = 1,linewidth=2)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('k',fontsize=20,**csfont)
plt.ylabel('y(k)', fontsize=20,**csfont)
plt.title('Comparação modelo: Mpmath x Numpy ', fontsize=20,**csfont)
plt.legend(loc=3,fontsize=19)


#%%==============================================================================
# APLICANDO MÉTODO DE HORNER COM NUMPY PARA COMPARAR COM Y DE PRECISÃO


yh=[0.966287829861518,0.9662878298615181] #cond inicial
h=2

for k in range(h,N):
    yh = np.append(yh, 0.6774 + 0.6435*yh[k-2]**2 \
                   + yh[k-1]*(0.6435 - yh[k-1]))



#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(y,color='black', label='yMP',alpha = 1,linewidth=2)
plt.plot(yh,color='blue', label='yHoner',alpha = 1,linewidth=2)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('k',fontsize=20,**csfont)
plt.ylabel('y(k)', fontsize=20,**csfont)
plt.title('Comparação Horner Numpy x Modelo Mpmath ', fontsize=20,**csfont)
plt.legend(loc=3,fontsize=19)



#%%==============================================================================
# APLICANDO MÉTODO DE HORNER COM MP PARA COMPARAR COM HORNER NUMPY

yhMP=[mp.mpf('0.966287829861518'),mp.mpf('0.9662878298615181')] #cond inicial
h=2

for k in range(h,N):
    yhMP = np.append(yhMP, 0.6774 + 0.6435*yhMP[k-2]**2 \
                   + yhMP[k-1]*(0.6435 - yhMP[k-1]))



#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(yh,color='blue', label='yhorner',alpha = 0.9,linewidth=2)
plt.plot(yhMP,color='grey', label='yHonerMP',alpha = 1,linewidth=2)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('k',fontsize=20,**csfont)
plt.ylabel('y(k)', fontsize=20,**csfont)
plt.title('Comparação Horner: Mpmath x Numpy', fontsize=20,**csfont)
plt.legend(loc=3,fontsize=19)

# DESSA FORMA, O QUE ME INTERESSA É O NRMSE DE Y COM YNP E YH COM YHMP

#%%==================================================================================
# Comparação com Matlab

ymodel=np.loadtxt("mapaquadratico_ymodel.dat")
yhorner=np.loadtxt("mapaquadratico_yhorner.dat")


#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(yhorner,color='green', label='matlab horner',alpha = 1,linewidth=2)
plt.plot(y,color='black', label='ynumpy',alpha = 1,linewidth=2)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('k',fontsize=20,**csfont)
plt.ylabel('y(k)', fontsize=20,**csfont)
plt.title('Comparação Matlab Horner x Modelo Numpy', fontsize=20,**csfont)
plt.legend(loc=3,fontsize=19)




#%% CÁLCULO RMSE

# 
nrmse1= (np.sqrt(np.sum((y - y2)**2)))/(np.sqrt(np.sum((y - np.mean(y2)**2))))
print('============================================================')
print('NRMSE MODELO: Y e Y2')
print(nrmse1)
print('')

nrmse2= (np.sqrt(np.sum((y - ynp)**2)))/(np.sqrt(np.sum((y - np.mean(ynp)**2))))
print('============================================================')
print('NRMSE MODELO: MPMATH X NUMPY')
print(nrmse2)
print('')

nrmseh= (np.sqrt(np.sum((y - yh)**2)))/(np.sqrt(np.sum((y - np.mean(yh)**2))))
print('============================================================')
print('NRMSE MODELO MPMATH com HORNER NUMPY')
print(nrmseh)
print('')

nrmsehmp= (np.sqrt(np.sum((yh - yhMP)**2)))/(np.sqrt(np.sum((yh - np.mean(yhMP)**2))))
print('============================================================')
print('NRMSE HORNER NUMPY X HORNER MPMATH')
print(nrmsehmp)
print('')

nrmse_matlabH= (np.sqrt(np.sum((y - yhorner[0:300])**2)))/(np.sqrt(np.sum((y - np.mean(yhorner[0:300])**2))))
print('============================================================')
print('NRMSE MODELO MPMATH X HORNER MATLAB')
print(nrmse_matlabH)
print('')








































