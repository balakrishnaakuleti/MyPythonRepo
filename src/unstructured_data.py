# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:49:48 2018

@author: I329986
"""
from collections import Counter

file = open('input.txt')

line = file.readline()
line_count = 1
while line:
    print("Line",line_count)
    print(line.strip())
    line=file.readline()
    line_count = line_count+1

file2 = open('input.txt')

print()    
print("Counter:")
print(Counter(file2.read().split()))
