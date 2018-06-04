# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:54:42 2018

@author: I329986
"""

import numpy as np
import pandas as pd

dataframe = pd.DataFrame(np.random.randn(5,3))

print(dataframe)
print()


dataframe = pd.DataFrame(np.random.randn(5,3), columns={'Column1','Column2','column3'})


print(dataframe)
print()

dataframe = pd.DataFrame(np.random.randn(5,3), columns={'Column1','Column2','column3'}, index ={'a','b','c','d','e'})


print(dataframe)
print()


dataframe = pd.DataFrame(np.random.randn(5,3), columns={'Column1','Column2','column3'}, index ={'a','b','c','d','e'})


print(dataframe)
print()


dataframe = dataframe.reindex(['j','a','k','b','k','c','g','l','d','h','e',])

print(dataframe)
print()
print(dataframe["Column1"].isnull() )

print()

print(dataframe.fillna(0))
print()

print(dataframe.fillna(method='ffill'))

print()

print(dataframe)

print()

print(dataframe.dropna())

df= pd.DataFrame({'one':[1,2,3,3,2],'two':[2,3,3,1,5]})
print(df)
print()
print(df.replace({3:9, 1:8}))
