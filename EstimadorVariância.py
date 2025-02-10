import matplotlib.pyplot as plt
import numpy as np
import random

#Autor: Leonardo Ayres M. Queiroz

n_pop = 3000 # Qtd. de elementos na população
n_amo = 10 # Qtd de registros na amostra
mu = 2050 # Média da população
E1 = [] # Estimador sem correção de Bessel
E2 = [] # Estimador com correção de Bessel

for i in range (10000):
    soma_pop = 0 # Guarda a somatória para calcular a variância
    soma_amo = 0 # Guarda a somatória para calcular a variância

    P = [] # Lista p/ guardar todos os elementos da população
    A = [] # Lista p/ guardar registros da amostra

    for i in range(n_pop): 
        população = np.random.normal(mu,50)
        P.append(população)

    for i in range(n_amo):
        A.append(random.choice(P))

    xm_amo = np.mean(A) # Valor médio dos registros da minha amostra

    for i in range(n_amo):
        soma_amo = soma_amo + (A[i] - xm_amo)**2
        soma_pop = soma_pop + (A[i] - mu)**2

    soma_amo = soma_amo/n_amo
    soma_pop = soma_pop/n_amo

    E1.append(soma_pop - soma_amo)


for i in range (10000):
    soma_pop = 0
    soma_amo = 0

    P = [] # Lista p/ guardar todos os elementos da população
    A = [] # Lista p/ guardar registros da amostra

    for i in range(n_pop): 
        população = np.random.normal(mu,50)
        P.append(população)

    for i in range(n_amo):
        A.append(random.choice(P))

    xm_amo = np.mean(A) # Valor médio dos registros da minha amostra

    for i in range(n_amo):
        soma_amo = soma_amo + (A[i] - xm_amo)**2
        soma_pop = soma_pop + (A[i] - mu)**2

    soma_amo = soma_amo/(n_amo-1)
    soma_pop = soma_pop/n_amo

    E2.append(soma_pop - soma_amo)

print('Média Estimador s/ correção= ',np.mean(E1))
plt.hist(E1,bins=100)
plt.grid()
plt.title('Estimador sem correção')
plt.show()

print('Média Estimador c/ correção de Bessel= ',np.mean(E2))
plt.hist(E2,bins=100,color='r')
plt.grid()
plt.title('Estimador com correção')
plt.show()

plt.hist(E1,bins=100,label='Sem correção')
plt.hist(E2,bins=100,color='r',label='Com correção')
plt.grid()
plt.title('Estimadores')
plt.legend()
plt.show()
