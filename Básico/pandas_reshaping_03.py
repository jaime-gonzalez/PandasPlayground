import pandas as pd

Carros = [7,4,3,2,8]

dias = pd.date_range('20190101','20190101', periods = 5)

vendedor=['George','Vagner','Pedro','Vagner','George']

df=pd.DataFrame({'Vendas':Carros, 'Data':dias, 'Vendedor':vendedor})


dfPivot = pd.pivot_table(df,index='Data',columns='Vendedor',values='Vendas',aggfunc=['sum','mean','max','min'])

dfPivotTransposed = dfPivot.T
