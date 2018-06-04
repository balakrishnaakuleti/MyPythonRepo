# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:30:10 2018

@author: I329986
"""
import pandas as pd

data = pd.read_csv('Data.csv')
print(data)
print()
print(data[:]['salary'])

print()
print(data.loc[:,['name','salary']])

print()
print(data.loc[[1,3,6],['name','salary']])

print()
print(data.loc[2:5,['name','salary']])