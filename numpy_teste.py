import numpy as np

#ATENÇÃO: A dimensão de um array é sua quantidade de linhas

#                       LENDO ARRAYS
#   a = np.array ([1, 2, 3])
#   ([]) - Todo Array de NumPy precisa estar dentro dessa estrutura mínima;
#        - Cada elemento dentro dele é uma linha diferente vista da seguinte maneira:
#            a = [1]
#                [2]
#                [3]
#   
#   b = np.array ([[1, 2, 3], [2, 3, 4], [5, 6, 7]])
#        - Notar que aqui há listas dentro de uma lista;
#        - Essa array é lida da seguinte maneira:
#            b = [1 2 3]
#                [2 3 4]
#                [5 6 7] 

#Criando um array unidimensional
a = np.array([[1,2,3]])

#Criando um array bidimensional
b = np.array([[0, 1, 2], [3, 4, 5]])

#Printando o array
print('Printando o array A')
print(a)
print()
print('Printando o array B')
print(b)
print()

#Printando as dimensões do array
print('Printando as dimensões do array A')
print(a.ndim)
print()
print('Printando as dimensões do array B')
print(b.ndim)
print()

#Printando o formato do array (linhas, colunas)
print('Printando o formato do array A')
print(a.shape)
print()
print('Printando o formato do array B')
print(b.shape)
print()

#Printando o tamanho da array
#Mas cuidado! Pega somente o tamanho da primeira dimensão
print('Printando o tamanho da primeira dimensão do array A')
print(len(a))
print()
print('Printando o tamanho da primeira dimensão do Array B')
print(len(b))
print()

#Verificando se é uma array numpy
print('Printando o tipo do array A')
print(type(a))
print()
print('Printando o tipo do array B')
print(type(b))
print()

#Criando um novo array do 0
#np.arange(valor inicial, valor final , passo)
#Valor final = não é incluso ao final devido aos fundamentos do python
#Passo = de quanto em quanto será feita a progressão
c = np.arange(0, 100, 1)
print()
print('Printando um novo Array automatico C')
print(c)