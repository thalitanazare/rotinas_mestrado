# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:07:50 2020

@author: nazare

Versao: 1.3
Data de atualização: 10/11/2020
"""

#  Simulando mapa quadrático e identificar um modelo para ele usando o pacote sysidentpy
# Pacotes Básicos
import numpy as np #Usado para construir os dados de entrada do algoritmo
from numpy import random
import matplotlib.pyplot as plt #Gerar gráficos
import pandas as pd #Exibit tabelas organizadas com DataFrame
import math as mt
#Pacotes para Identificação
import sysidentpy.polynomial_basis as sip #Usado para gerar o modelo
import sysidentpy.metrics as sim #Usado para validar o modelo (RMSE)
# Pacotes para intervalos
import mpmath as mp
from mpmath import *
from ivmpftools import *


# Simulando mapa quadrático
a=1.9 #parametro caotico, porem com a cond inicial fica primeiro em ponto fixo.
x0=mt.sqrt((a-((mt.sqrt(4*a + 1)-1)/2))) #cond inicial controlada
#%%
#x0= 0.4
x=[x0]
x1=x
N=500
h=1

for k in range (h,N):
    x = np.append(x, a - mt.pow(x[k-1],2))

# fazendo um teste mudando formulação matemática ( muda para cond in aleatória)

for k in range (h,N):
    x1 = np.append(x1, - x1[k-1]*x1[k-1] + a )

#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(x[0:150],color='orange', label='X',alpha = 1)
plt.plot(x1[0:150],color='black', label='X1',alpha = 1)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('Número de Iterações',fontsize=20,**csfont)
plt.title('Mapa Quadrático - Sistema Variáveis Numpy ', fontsize=20,**csfont)
plt.legend(loc=2,fontsize=19)
plt.savefig('/Users/thali/Desktop/mestrado2020/Andamento/Python/modelos_com_intervalos/imagens/mapa_quadratico/sistema.png')

#%%============================================================================
# SIMULANDO A EQUAÇÃO ORIGINAL MAS DECLARANDO VARIÁVEIS MP.MPF
mp.mp.dps=50

a1=mp.mpf('1.9') #parametro caotico, porem com a cond inicial fica primeiro em ponto fixo.
x2=[mp.sqrt((a1-((mp.sqrt(4*a1 + 1)-1)/2)))] #cond in

#x0= 0.4
N=500
h=1

for k in range (h,N):
    x2 = np.append(x2, a1 - x2[k-1]**2  )

plt.figure(figsize=(16, 8))
plt.plot(x2,color='black', label='x2',alpha = 1, linewidth=2)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('Número de Iterações',fontsize=20,**csfont)
plt.title('Mapa Quadrático - Sistema Variáveis mp.mpf', fontsize=20,**csfont)
plt.legend(loc=2,fontsize=19)
plt.savefig('/Users/thali/Desktop/mestrado2020/Andamento/Python/modelos_com_intervalos/imagens/mapa_quadratico/sistema_mp_mpf.png')

# %% ==========================================================================
# Usando pacote sysindetpy para identificar um modelo para o mapa quadrático
u_id=np.zeros(len(x[0:250]))
y_id=x[0:250]

u_val=np.zeros(len(x[250:500]))
y_val=x[250:500]


u_id = u_id.reshape(-1,1)
y_id = y_id.reshape(-1,1)

u_val = u_val.reshape(-1,1)
y_val = y_val.reshape(-1,1)

# O uso do pacote começa aqui:
#% Aqui, defini qual o grau de não linearidade, os atrasos máximos e
# o critério de informação usado e mandei ele definir  por conta própria
# o número de regressores do modelo (o parâmetro order_selection)
model_obj = sip.PolynomialNarmax(non_degree=2,
                                 ylag=2, xlag=2,
                                 info_criteria='bic',
                                 order_selection=True)

# Executei a identificação usando a configuração feita acima sobre os
# dados de identificação
model_obj.fit(u_id, y_id)

# Executei a simulação do sistema usando a condição inicial do y_val e usando o
# u_val como entrada
y_simulado = model_obj.predict(u_val, y_val)

# Calculei o RMSE comparando os dados da simulação com o y_val
rmse = sim.root_relative_squared_error(y_val, y_simulado)

# O uso do pacote em si (o processo de identificação) terminou na linha acima
# A partir daqui é só mostrando resultados

# Mostra a tabela com os regressores que compõem o modelo
results = pd.DataFrame(model_obj.results(err_precision=8,dtype='dec'),
                       columns=['Regressors', 'Parameters', 'ERR'])

print(results)

# Faz a análise dos resíduos:
# ee - auto-correlação do resíduo
# eu - Correlação resíduo com entrada
ee, eu, _, _ = model_obj.residuals(u_val, y_val, y_simulado)

# Plota o gráfico dos dados de validação do modelo
# e os gráficos das correlações
model_obj.plot_result(y_val, y_simulado, ee, eu)
#plt.savefig('quadraticoID.png', format='png')
#gera a sequência de 1 até o número de regressores candidatos, usado como eixo X do gráfico do critério de informação
eixo_x = range(1,(model_obj.n_info_values+1))
# Plota o critério de informação
plt.plot(eixo_x, model_obj.info_values)


#%%============================================================================
# Simulando o modelo e aplicando variações matemáticas
iv.dps=100
N= 150
y1=[iv.mpf(x[0]), iv.mpf(x[1])]

y2=y1
h=2

for k in range(h,N):
    y1 = np.append(y1, 0.6435*y1[k-2]**2 - y1[k-1]**2 + 0.6774 + 0.6435*y1[k-1])


# outra forma de escrever

for k in range(h,N):
    y2 = np.append(y2, 0.6435*y2[k-2]*y2[k-2] - y2[k-1]*y2[k-1] + 0.6774 + 0.6435*y2[k-1])



y1_p = ivmpf_disassembler(y1)
y2_p = ivmpf_disassembler(y2)

#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(y1_p[:,0],color='orange', label='y1',alpha = 1,linewidth=5)
plt.plot(y1_p[:,1],color='orange',alpha = 1,linewidth=5)
plt.plot(y2_p[:,0],color='black', label='y2',alpha = 1,linewidth=2)
plt.plot(y2_p[:,1],color='black',alpha = 1,linewidth=1)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('Número de Iterações',fontsize=20,**csfont)
plt.title('Mapa Quadrático - Modelos Com Intervalos', fontsize=20,**csfont)
plt.legend(loc=2,fontsize=19)
plt.savefig('/Users/thali/Desktop/mestrado2020/Andamento/Python/modelos_com_intervalos/imagens/mapa_quadratico/modelo_iv.png')


#%%
# FAZENDO UM NOVO TESTE - SEM INTERVALOS MAS COM VARIÁVEIS MP.MPF

mp.mp.dps=50

y3=[mp.mpf(x[0]), mp.mpf(x[1])]
y4=y3

for k in range(h,N):
    y3 = np.append(y3, 0.6435*y3[k-2]**2 - y3[k-1]**2 + 0.6774 + 0.6435*y3[k-1])
    

# outra forma de escrever
for k in range(h,N):
    y4 = np.append(y4, 0.6435*y4[k-2]*y4[k-2] - y4[k-1]*y4[k-1] + 0.6774 + 0.6435*y4[k-1])
    
#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(y3,color='orange', label='y3',alpha = 1,linewidth=5)
plt.plot(y4,color='black', label='y4',alpha = 1,linewidth=2)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('Número de Iterações',fontsize=20,**csfont)
plt.title('Mapa Quadrático - Modelo sem Intervalo Variáveis mp.mpf', fontsize=20,**csfont)
plt.legend(loc=2,fontsize=19)
plt.savefig('/Users/thali/Desktop/mestrado2020/Andamento/Python/modelos_com_intervalos/imagens/mapa_quadratico/modelo_mp_mpf.png')


#%% SIMULANDO O MODELO SEM INTERVALOS E UTILIZANDO O NUMPY


N= 150
y5=[x[0], x[1]]

y6=y5
h=2

for k in range(h,N):
    y5 = np.append(y5, 0.6435*y5[k-2]**2 - y5[k-1]**2 + 0.6774 + 0.6435*y5[k-1])


# outra forma de escrever

for k in range(h,N):
    y6 = np.append(y6, 0.6435*y6[k-2]*y6[k-2] - y6[k-1]*y6[k-1] + 0.6774 + 0.6435*y6[k-1])
    
#======FIGURE======
plt.figure(figsize=(16, 8))
csfont = {'fontname':'Times New Roman'}
plt.plot(y5,color='orange', label='y5',alpha = 1,linewidth=3)
plt.plot(y6,color='black', label='y6',alpha = 1,linewidth=3)
plt.xticks(fontsize=18,**csfont)
plt.yticks(fontsize=18,**csfont)
plt.xlabel('Número de Iterações',fontsize=20,**csfont)
plt.title('Mapa Quadrático - Modelo sem Intervalo Variáveis Numpy', fontsize=20,**csfont)
plt.legend(loc=2,fontsize=19)
plt.savefig('/Users/thali/Desktop/mestrado2020/Andamento/Python/modelos_com_intervalos/imagens/mapa_quadratico/modelo_numpy.png')


   
    

