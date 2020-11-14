import pandas as pd

df = pd.read_csv("https://cdncontribute.geeksforgeeks.org/wp-content/uploads/nba.csv")

df.head(4)

df.shape

stack_df = df.stack()

udf = stack_df.unstack()

udf.head()
