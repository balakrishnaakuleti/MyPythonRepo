# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:08:02 2018

@author: I329986
"""
import pandas as pd
from sqlalchemy import create_engine
from pandas.io import sql

engine = create_engine('sqlite:///:memory:')

df = pd.read_excel('sample_excel.xlsx')
print(df)

print()

df.to_sql('data_table',engine)

res1 = pd.read_sql_query('Select * from data_table',engine)

print()
print(res1)

res2 = pd.read_sql_query('Select dept,SUM(salary) from data_table group by dept',engine)

print()
print(res2)

#INSERT A ROW INTO THE TABLE

sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)',engine,params =  [('id',9,'Ruby',711.20,'2015-03-27','IT')] )

res3 = pd.read_sql_query('select * from data_table',engine)

print()
print(res3)




sql.execute('Delete from data_table where name = (?) ', engine,  params=[('Gary')])


res4 = pd.read_sql_query('select * from data_table',engine)

print()
print(res4)