import pandas as pd
import numpy as np

df2 = pd.DataFrame({'A':1., 
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1, index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4, dtype='int32'),
                    'E':pd.Categorical(['test','train','test','train']),
                    'F':'Python',
                    'G':[2,2,4,4],
                    'H':[np.nan,2,4,np.nan]
                    })


#contar observações distintas com base nas linhas. 
#Default é axis=0 e dropna=true. 
#Quando axis=0, verificada a contagem de valores distintos pelo index, e assim por diante.
#Quando dropna = false, ele considera também os valores "NaN".

df2.nunique()

df2.nunique(axis=1,dropna=False)

df2.drop_duplicates(subset='G')

df2.drop_duplicates(subset='G', keep='last')
