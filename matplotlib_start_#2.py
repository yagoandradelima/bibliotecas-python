import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)
y1 = np.sin(x) #Primeira linha
y2 = np.cos(x) #Segunda linha
y3 = np.sin(x) + np.sin(3*x) #Terceira linha

plt.title('Gráfico aula 2') #Titulo do gráfico
plt.xlabel('Eixo x') #Nome do eixo x
plt.ylabel('Eixo y') #Nome do eixo y
plt.grid(True) #colocando gradeamento
plt.plot(x, y1, label='Seno de x') #Plotando função 1 no gráfico 1. Colocando legenda
plt.plot(x, y2, label= 'Cosseno de x') #Plotando função 2 no gráfico 1. Colocando legenda
plt.plot(x, y3, label='Seno de x + 3*seno de x') #Plotando função 3 no gráfico 1. Colocando legenda
plt.legend(loc='upper right') #Solicitando legenda no gráfico. Mudando posicionamento (default = lower left)
plt.show() #Pedindo pra mostrar o gráfico
