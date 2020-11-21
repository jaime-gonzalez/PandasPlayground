import numpy as np
import pandas as pd

df = pd.DataFrame({'Col1':['A','A','B',np.nan,'D','C'],'Col2':[2,1,9,8,7,4],'Col3':[0,1,9,4,2,3]})

df.sort_values(by='Col1')

df.sort_values(by='Col2')

df.sort_values(by=['Col3','Col1'])

df.sort_values(by=['Col3'],ascending=False)
