# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 15:42:31 2018

@author: I329986
"""

import pandas as pd

df = pd.read_excel('sample_excel.xlsx')
print(df)

print()
print(df[:]['name'])

print()
print(df[0:4]['name'])

print()
print(df.loc[:,['name','salary']])

print()
print(df.loc[1:4,['name','salary']])

print()
print(df.loc[[1,3,5],['name','salary']])


xls = pd.ExcelFile('sample_excel.xlsx')

df1 = pd.read_excel(xls, 'Sheet1')

print()
print( df1[0:4]['name'])

df2 = pd.read_excel(xls, 'Sheet2')

print()
print( df2[0:4]['zipcode'])