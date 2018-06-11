'''
Created on Jun 5, 2018

@author: Balakrishna Akuleti
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import pylab 
df = pd.DataFrame(np.random.randn(5,4), columns=['A','B','C','D'])

plt.pcolor(df)

pylab.show()