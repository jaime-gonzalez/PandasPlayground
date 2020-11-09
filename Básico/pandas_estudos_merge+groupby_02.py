
import numpy as np
import pandas as pd

df = pd.DataFrame({'A':['verdadeiro','falso','verdadeiro','falso',
                        'verdadeiro','falso','verdadeiro','falso'],
                   'B':['um','um','dois','tres','dois','dois','um','tres'],
                   'C':np.random.randn(8),
                   'D':np.random.randn(8)
                   })

df

df.groupby(['A']).sum()

df.groupby(['A']).mean()

df.groupby(['B']).sum()


x = df.groupby(['A','B']).sum()

y = df.groupby(['A','B']).mean()

z = pd.merge(x, y, on=['A','B'], suffixes=('_sum','_mean'))

z2 = pd.merge(
    df.groupby(['A','B']).sum(),
    df.groupby(['A','B']).mean(),
    on=['A','B'],
    suffixes=('_sum','_mean')
    )
