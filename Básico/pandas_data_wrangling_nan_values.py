import pandas as pd
import numpy as np

datas = pd.date_range('20190101', periods = 60, freq="D")

df = pd.DataFrame(np.random.randn(60,5), index = datas, columns = list("ABCDE"))

df['F'] = df.A[df.A > 0]

df2 = df.copy()

df3 = df.copy()

#remover linhas com NaN
df2.dropna().shape

df3.head(3)
#substituir valores NaN da coluna F com a média dos valores da coluna A
df3.F.fillna(np.mean(df3.A))

df4 = df.copy()
#substituir todos os valores de "NaN" do dataFrame com o valor 77777
df4.fillna(value = 77777)
