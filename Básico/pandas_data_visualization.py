import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#fonte dos dados: https://www.kaggle.com/c/titanic/data?select=train.csv

df = pd.read_csv('C:/Users/55479/Pandas/titanic_train.csv')

plt.style.available

df.head()

df.shape

plt.rcParams['figure.figsize']=(20,7)



plt.plot(df.Age,'*-r')
plt.title('Informações dos passageiros')
plt.xlabel('Passageiro',size=12)
plt.ylabel('Idade', size=12)
plt.show()

df.Age.plot()
plt.show()

df.plot()

# Scatter Plot

plt.scatter(df.PassengerId, df.Age, color='black', marker='+')
plt.show()

df.Age.describe()

df.Age.hist()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('histograma01.png',transparent=False)
plt.show()
