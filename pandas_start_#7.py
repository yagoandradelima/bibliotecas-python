import pandas as pd
import numpy as np

dados = np.array([ 1,  2,  np.nan],
                 [12,  np.nan,  np.nan],
                 [ 3,  5,  2])

df = pd.DataFrame(data=dados, columns='A B C'.strip())