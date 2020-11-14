import pandas as pd
import numpy as np

datas = pd.date_range('20180101', periods = 600, freq = "D")

df = pd.DataFrame(np.random.randn(600,5), index = datas, columns = list("ABCDE"))

df.head(2)

#slice com coluna
df['D']

#slice com linhas
df[1:5]

#slice com algumas colunas e todas as linhas
df.loc[:,['B','C','D']]

#slice por datas quando o index é uma data
f = df.loc['20180301':'20180901', ['A','E']]

len(f)

#slice de linhas por intervalos de indices
df.iloc[1]
df.iloc[1:4, 1:3]

#slice linhas por indices específicos
df.iloc[[1,5,6], [0,3]]

#slice das linhas de indice 1 ao 2 por todas as colunas
df.iloc[1:3, :]

#slice do DataFrame para todos os indices cujos valores da coluna "A" sejam maiores que zero.
df[df.A>0]

#slice dos dados de todas as colunas que possuam valores positivos (os negativos são substituídos por NaN)
df[df>0]
