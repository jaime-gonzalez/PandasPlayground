
import pandas as pd
import numpy as np

datas = pd.date_range('20200101',periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A', 'Var_B','Var_C', 'Var_D'])

dft = df.T

df.shape

dft.shape

np.size(dft)

dft.values

v = dft.values

v.reshape((2,12))

v.reshape((3,8))
