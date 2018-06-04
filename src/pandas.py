# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:27:44 2018

@author: I329986
"""

import pandas as pd
import numpy as np

#Series
a = np.array([1,2,3,4])
p = pd.Series(a)
print(p)

#DataFrame
a1 = {'Name': ['Bala','krishna','Reddy'], "iddnumber":[4,5,6]}

p1 = pd.DataFrame(a1, index ={"index1","index2","index3"})

print(p1)


#Panel

a2 = {'item1': pd.DataFrame(np.random.randn(4,8)),
     'item2': pd.DataFrame(np.random.randn(4,7))
     }
p2 = pd.Panel(a2)

print(p2)

