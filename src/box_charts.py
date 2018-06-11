'''
Created on Jun 5, 2018

@author: Balakrishna Akuleti
'''

import numpy as np
import pandas as pd
from pandas import *
import pylab

df = pd.DataFrame(np.random.randn(10,5), columns=['A','B','C','D','E',]) 

df.boxplot(grid='true')


pylab.show()
print('Hello World')
