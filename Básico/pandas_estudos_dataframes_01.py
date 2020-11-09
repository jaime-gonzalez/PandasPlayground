import pandas as pd
import numpy as np

series = pd.Series([7, 4, 2, np.nan, 6, 9])

print(series)

type(series)

datas = pd.date_range('20180101', periods=6)

print(datas)

datas = pd.date_range('20180101', periods=6, freq="M")

datas_yearly = pd.date_range('20180101', periods=6, freq="Y")

df = pd.DataFrame(np.random.randn(6,4), index = datas, columns = list("ABCD"))

print(df)

df2 = pd.DataFrame({"A":7, 
                    "B": pd.Timestamp('20190101'),
                    "C": pd.Series(1, index = list(range(4)), dtype = 'float32'),
                    "D": np.array([3]*4, dtype = 'int32'),
                    "E": pd.Categorical(['test','train', 'test','train']),
                    "F": 'Python'
                        })
print(df2.dtypes)

print(df.head(3))

print(df.tail)

print(df.index)

C = df.columns

print(df)

df.to_numpy()

print(df)

df.T

df2.to_numpy()
