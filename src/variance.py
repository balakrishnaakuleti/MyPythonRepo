'''
Created on Jun 11, 2018

@author: Balakrishna Akuleti
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
from matplotlib.pyplot import xlabel

dict = {'Name': pd.Series(['Krishna','Bala','Raghu','Girish','Sujoy','Deva','Nagesh','Sajiv','Bala','Krishna','Krishna']),
        'Age' : pd.Series([22,29,24,26,24,22,26,29,28,29,32]),
        'Rating' : pd.Series([3.5,4.5,5,2.5,1.5,3,5,4.5,1,1.5,1.5])
    }
df = pd.DataFrame(dict)

print(df.std())
print(df.skew())