import numpy as np
import matplotlib.pyplot as plt
import skimage as skim

#Criando um array simples de 1's
a1 = np.ones(10)
#printando o array
print (a1)
print()

#Criando um array randomico
#randint possui os parametros: (inicio do intervalo possível de escolha, fim do intervalo de escolha, qtd de números que serão sorteados)
#random.seed TRAVA o aleatório do randint como se fosse uma seed de mapa. Posso rodar várias vezes que vai se repetir.
np.random.seed(44)
a2 = np.random.randint(1, 20, 6)

#Operações com Array
mult = a1 * 10
div = a1 / 2
soma = a1 + 4
sub = a1 - 6
sqrt = a1**2

print('Multiplicando array por 10')
print(mult)
print()

print('Dividindo array por 2')
print(div)
print()

print('Somando array com 4')
print(soma)
print()

print('Subtraindo 6 do array')
print(sub)
print()

print('Elevando ao quadrado')
print(sqrt)
print()

print('Printando um array aleatório com valores em um intervalo adicionado')
print (a2)
print()
#Operações entre arrays
#No Python, o que vem embaixo no codigo vem depois, então esse seed não interfere no de cima
np.random.seed(12)
a3 = np.random.randint(12, 44, 6)

print('Printando um novo array')
print(a3)

print('Somando arrays')
#lembrar que as operações não funcionam com arrays de tamanhos diferentes
#exceção à multiplicação de matrizes
print(a2+a3)
print()

print('Multiplicando Arrays')
print('ATENÇÃO: isso é uma multiplicação elemento a elemento e não multiplicação de matrizes')
print(a2*a3)
print()

print('Subtração de arrays')
print(a2-a3)
print()

print('Divisão de arrays')
print(a2/a3)
print()