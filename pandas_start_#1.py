import numpy as np
import pandas as pd

#Series é como uma linha ou coluna do DataFrame(tabela). Ele pode parecer um array do numpy, mas possui atributos diferentes
#Fazendo uma series de passos dos meus ultimos 5 dias
steps = pd.Series([836, 856, 3775, 5747, 3311])
print(steps)