import pandas as pd
import numpy as np

df = pd.read_csv('datasets/titanic_passengers.csv')
print('Printando antes de passar o Apply a coluna de idade: ')
print(df['Age'])
print()
#Método Apply
#O método apply aplica uma função em cada elemento de uma determinada coluna
#Não preciso colocar os () ao final
print('Printando após o Apply')
print(df['Age'].apply(np.sqrt))
print()

#trocando com apply o 0 em NO e 1 em YES na coluna survived
#criando uma função nova apenas para mudar 0 para NO e 1 para YES
def changeSurvived(elemento):
    if elemento == 0:
        return 'NO'
    else:
        return 'YES'

print(df['Survived'].apply(changeSurvived))
#Para aplicar diretamente essa coluna modificada e gravar ela no dataframe preciso aplicar o código abaixo
#df['Survived'] = df['Survived'].apply(changeSurvived)

#Colocando simbolo de dólar na coluna das tarifas
def changeFare(elemento):
    #Transoformando elemento em str pra poder concatenar, já que Fare é coluna int
    #return '$ ' + str(elemento)
    #Transformando utilizando format para manipular os elementos float
    return '${:.2f}'.format(elemento)

print(df['Fare'].apply(changeFare))
#Para aplicar a transformação, o código é:
#df['Fare'] = df['Fare'].apply(changeFare)