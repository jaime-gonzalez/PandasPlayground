import pandas as pd

data={
      "localizacao":['CidadeA','CidadeB'],
      "Temperatura":['Prevista','Atual'],
      "Set-2019":[30,32],
      "Out-2019":[45, 43],
      "Nov-2019":[24,22]
      }

print(data)

df = pd.DataFrame(data, columns=['localizacao','Temperatura','Set-2019','Out-2019','Nov-2019'])
print(df)

df2 = pd.melt(df, id_vars=['localizacao','Temperatura'],var_name="Date", value_name="Value")
print(df2)

df3 = pd.melt(df, id_vars=['localizacao'],var_name="Date", value_name="Value")
print(df3)
