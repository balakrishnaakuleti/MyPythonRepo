
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:39:25 2018

@author: I329986
"""
import datetime

print( 'The Date Today is  :', datetime.datetime.today())
today = datetime.date.today()
day1 = datetime.date(2017,8,18)
day2 = datetime.date(2017,8,14 )
date_delta =  day1-day2 
print(date_delta)
print()

if today  < day1:
    print("day1 is bigger")

print(today)
print(today.day)
print(today.month)
print(today.year)




