'''
Created on Jun 5, 2018

@author: Balakrishna Akuleti
'''
import numpy as np
import pandas as pd
import pylab
from matplotlib import pyplot 

df = pd.DataFrame(np.random.randn(10,2), columns=['Col1','Col2'], index=['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10'])
print(df)
print(df['Col1'])

pyplot.scatter(x=df['Col1'], y=df['Col2'])

x= np.arange(10)

#pyplot.scatter(x=x, y=x*x)
pylab.show()