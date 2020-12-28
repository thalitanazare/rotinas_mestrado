# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:07:50 2020

@author: thali
"""

#  Simulando mapa quadrático e identificar um modelo para ele usando o pacote sysidentpy
# Esses são os pacotes fundamentais para tudo funcionar.
import numpy as np #Usado para construir os dados de entrada do algoritmo
import sysidentpy.polynomial_basis as sip #Usado para gerar o modelo
import sysidentpy.metrics as sim #Usado para validar o modelo (RMSE)

import matplotlib.pyplot as plt #Gerar gráficos
import pandas as pd #Exibit tabelas organizadas com DataFrame
import math as mt
from numpy import random

# Simulando mapa quadrático
a=1.9 #parametro caotico, porem com a cond inicial fica primeiro em ponto fixo.
x0=mt.sqrt((a-((mt.sqrt(4*a + 1)-1)/2))) #cond in
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

plt.figure(figsize=(16, 8))
plt.plot(x[0:150],color='orange', label='X',alpha = 1)
plt.plot(x1[0:150],color='black', label='X1',alpha = 1)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('Número de Iterações',fontsize=20)
plt.title('Mapa Quadrático - Sistema', fontsize=20)
plt.savefig('quadraticosis.png', format='png')
plt.legend(loc=2,fontsize=19)
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
plt.savefig('quadraticoID.png', format='png')
#gera a sequência de 1 até o número de regressores candidatos, usado como eixo X do gráfico do critério de informação
eixo_x = range(1,(model_obj.n_info_values+1))
# Plota o critério de informação
plt.plot(eixo_x, model_obj.info_values)


# Simulando o modelo e aplicando variações matemáticas

N= 150
y1=[x[0], x[1]]

y2=y1
h=2

for k in range(h,N):
    y1 = np.append(y1, 0.6435*y1[k-2]**2 - y1[k-1]**2 + 0.6774 + 0.6435*y1[k-1])


# outra forma de escrever

for k in range(h,N):
    y2 = np.append(y2, 0.6435*y2[k-2]*y2[k-2] - y2[k-1]*y2[k-1] + 0.6774 + 0.6435*y2[k-1])

plt.figure(figsize=(16, 8))
plt.plot(y1,color='orange', label='Y1',alpha = 1)
plt.plot(y2,color='black', label='y2',alpha = 1)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('Número de Iterações',fontsize=20)
plt.title('Mapa Quadrático - Modelo', fontsize=20)
plt.savefig('quadraticomodel.png', format='png')
plt.legend(loc=2,fontsize=19)





