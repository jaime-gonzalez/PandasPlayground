import pandas as pd
import numpy as np

dias = pd.date_range(start='20190101', periods=12)

Pessoa =['George','Victor','Lucas']

np.random.choice(Pessoa)

Nome = []
Gasto = []
for i in range(12):
    Nome.append(np.random.choice(Pessoa))
    Gasto.append(np.round(np.random.rand()*100,2))
Nome

df = pd.DataFrame({'Dia':dias, 'Nome':Nome, 'Gasto':Gasto})

df2 = df.groupby(['Nome']).Gasto.agg(["min","max","sum"])

df.pivot(index='Dia', columns='Nome', values='Gasto')

merged = pd.merge(df, df2, on='Id', how='left', indicator = True)
