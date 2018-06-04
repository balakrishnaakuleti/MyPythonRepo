# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:46:27 2018

@author: I329986
"""
import pandas as pd

data = pd.read_json('data.json')
print (data)

print()
print(data[:]['Name'])


print()
print(data[2:5]['Dept'])

print()
print(data[:4]['Name'])

print()
print(data.loc[1:4,['Name','Dept']])

print()
print(data.loc[[1,3,5],['Name']])