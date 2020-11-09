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

df_a = pd.DataFrame(cadastro_a, columns = ['Id','Nome', 'Idade', 'CEP'])

df_b = pd.DataFrame(cadastro_b, columns = ['Id','Nome', 'Idade', 'CEP'])

df_c = pd.DataFrame(compras, columns = ['Id','Data', 'Valor'])

#inner join
pd.merge(df_a, df_b, on=['Id'], how='inner')
pd.merge(df_a, df_b[['Id','Idade','CEP']], on=['Id'], how ='inner')
pd.merge(df_a, df_b[['Id','Idade','CEP']], on=['Id'], how ='inner', suffixes = ('_A','_B'))

#full join
lojas = pd.concat([df_a, df_b], ignore_index = True)
clientes_unicos = lojas.drop_duplicates(subset='Id')

#left join
esquerda = pd.merge(df_a, df_c, on=['Id'], how='left')

#groupby
esquerda.groupby(['Id', 'Nome'])['Valor'].sum()

#outer join
pd.merge(df_a, df_b, how='outer', on=['Id'], indicator = True)
