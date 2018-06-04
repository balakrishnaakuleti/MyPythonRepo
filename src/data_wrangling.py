# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:00:15 2018

@author: I329986
"""

import pandas as pd

data1 = {'Id': ['1','2','3','4','5','6'],
       'Name' : ['Bala','krishna','reddy','akuleti','krish','bal'],
       'Subject': ['Science','English','Hindi','Social','Telugu','Maths']
       }
data2 = {'Id': [7,8,9],
         'Name':['Seetha','Geetha','Latha'],
         'Subject':['Science','Maths','Social']
        }
df1 = pd.DataFrame(data1)
print(df1)

print()
df2 = pd.DataFrame(data2)
print(df2)
print()

df3 = pd.concat([df1,df2])
print()
print(df3)
print()

grouped_data =df3.groupby('Subject')
print( grouped_data.get_group('Maths'))