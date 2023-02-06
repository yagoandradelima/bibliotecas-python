import pandas as pd
import numpy as np

#Lembrar do formato de array ([]) << array simples onde cada valor inserido é uma coluna
array = np.array([[72, 180, 26],[80, 170, 19],[60, 165, 15]])
print(array)
print()
df = pd.DataFrame(data=array, index=['Pedro', 'Ricardo', 'Luana'], columns=['Peso', 'Altura', 'Idade'])
print(df)

print()