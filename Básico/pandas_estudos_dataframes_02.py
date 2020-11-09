import pandas as pd
import numpy as np

datas = pd.date_range('20190101', periods = 60, freq = "D")

df = pd.DataFrame(np.random.randn(60, 5), index = datas, columns = list("ABCDE"))

print(df.head(3))

df['F'] = 1

print(df.head(10))

df['G'] = range(60)

print(df.head(10))

df['Produto'] = df['A']* df['B']

print(df.head(5))

df['D'] = 88

print(df.head(4))
