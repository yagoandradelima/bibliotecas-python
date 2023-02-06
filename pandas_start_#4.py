import pandas as pd
import numpy as np

df = pd.read_csv('datasets/titanic_passengers.csv') #sep=';' caso o separado seja outro simbolo se não a vírgula
print('Printando as 5 primeiras linhas do dataset')
print(df.head)
print()

print('Printando as 5 últimas linhas do dataset')
print(df.tail) #Caso eu queir mais ou menos do que cinco linhas, basta usar df.tail(8) onde o (8) é um inteiro com o número de linhas
print()

print('Printando dados internos dos dados númericos do dataset')
print(df.describe())
print()

#para ler um xlsx basta usar o pd.read_excel
#também é necessário instalar via pip o módulo openpyxl
#caso os cabeçalhos não estejam na primeira linha do excel, eles contam como dados ao inve´s de labels
#além disso qualquer coluna entre a coluna 1 e os dados são tabeladas como NaN
df2 = pd.read_excel('datasets/bd_zero.xlsx', sheet_name='Planilha2') #sheet_name= escolhe a pasta de trabalho com a qual quero trabalhar
print('Dataset do excel')
print(df2)
print()

#salvando e convertendo um arquivo ao mesmo tempo:
#df.to_csv('datasets/bd_zero.csv')