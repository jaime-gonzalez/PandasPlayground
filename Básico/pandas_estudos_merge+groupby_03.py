import numpy as np
import pandas as pd

cadastro_a = {'Id':['AA2930','BB4563','CC2139','DE2521','GT3462','HH1158'],
              'Nome':['Victor','Amanda','Bruna','Carlos','Ricardo','Maria'],
              'Idade':[20,35,40,54,30,27],
              'CEP':['00092-029','11111-111','22222-888','00000-999','88888-111','77777-666']
              }

cadastro_b = {'Id':['CC9999','EF4488','DD9999','GT3462','HH1158'],
              'Nome':['Marcos','Patricia','Ericka','Ricardo','Maria'],
              'Idade':[19,30,22,30,27],
              'CEP':['00092-029','11111-111','11111-888','88888-111','77777-666']
              }

compras = {'Id':['AA2930','EF4488','CC2139','EF4488','CC9999','AA2930','HH1158'],
           'Data': ['2019-01-01','2019-01-30', '2019-02-01', '2019-02-20', '2019-03-15', '2019-04-01', '2019-04-10'],
           'Valor':[200,100,40,150,300,25,50]}

df1 = pd.DataFrame(cadastro_a, columns=['Id', 'Nome', 'Idade','CEP'])

df2 = pd.DataFrame(cadastro_b, columns=['Id', 'Nome','Idade','CEP'])

df3 = pd.DataFrame(compras, columns=['Id','Data','Valor'])

merged_df1 = pd.merge(df1, df2, on='Id', how='left', indicator = True)
merged_df2 = pd.merge(df1, df2, on='Id', how='right', indicator = True)
merged_df3 = pd.merge(df1, df2, on='Id', how='inner', indicator = True)
merged_df4 = pd.merge(df1, df2, on='Id', how='outer', indicator = True)

merged_df5 = pd.concat([df1, df2], ignore_index=True).drop_duplicates(subset='Id')

new_df = pd.merge(
pd.merge(merged_df5, df3, on='Id', how='left', indicator = True).groupby(
    ['Id','Nome','Idade','CEP'])['Valor'].sum(),
pd.merge(df2, df3, on='Id', how='left', indicator = True).groupby(
    ['Id','Nome','Idade','CEP'])['Valor'].mean(),
on=['Id','Nome','Idade','CEP'],
suffixes = ['_Sum','_Mean']
)
