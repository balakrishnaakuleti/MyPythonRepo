# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:20:25 2018

@author: I329986
"""
import pandas as pd
import numpy as np

import urllib2
from bs4 import BeautifulSou

df = pd.DataFrame(np.random.randn(10,4), columns=['A','B','C','D'])
print(df)
r = df.rolling(window=13,min_periods=1)
print("START")
print(r)
print("END")
print( r.aggregate(np.sum))

print(r['A'].aggregate(np.sum))

print()
print(r[['A','B']].aggregate(np.sum))

