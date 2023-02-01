import numpy as np

#ATENÇÃO: A dimensão de um array é sua quantidade de linhas

#Criando um array unidimensional
a = np.array([1,2,3])

#Criando um array bidimensional
b = np.array([[0, 1, 2], [3, 4, 5]])

#Printando o array
print(a)
print(b)

#Printando as dimensões do array
print(a.ndim)
print(b.ndim)

#Printando o formato do array (linhas, colunas)
print(a.shape)
print(b.shape)

#Printando o tamanho da array
#Mas cuidado! Pega somente o tamanho da primeira dimensão
print(len[a])
print(len[b])

#Verificando se é uma array numpy
print(type(a))
print(type(b))

#Criando um novo array do 0
#np.arange(valor inicial, valor final , passo)
#Valor final = não é incluso ao final devido aos fundamentos do python
#Passo = de quanto em quanto será feita a progressão
c = np.arange(0, 100, 1)

print(c)