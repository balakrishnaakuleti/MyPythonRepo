'''
Created on Jun 6, 2018

@author: Balakrishna Akuleti
'''

import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

data = pd.read_csv('stock.csv')

print(data)

df = pd.DataFrame(data, columns=['ValueDate','Price'])

df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
del df['ValueDate']

print(df)



df.plot(figsize=(15,3))
plt.show()

