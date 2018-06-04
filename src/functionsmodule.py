# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:09:40 2018

@author: I329986
"""

import time
import os

def sumEverything(*b):
    "He he this is my first ever fuction in Python"
    sum = 0;
    for var in b:
        sum+=var;
    return sum;

print("My Method result : ",sumEverything(0,1,3,4,5,6,7));

myLambdaFnction = lambda arg1, *arg2 : arg1 ;
print(myLambdaFnction(12,12));
print(dir(time))



myFile = open("python_test_File.txt", "w+")
print(myFile.closed)
print(myFile.write("adfadsfadfasdfafewfdsafwaefasfasfsad"))
print(myFile.name)
print(myFile.mode)
print(myFile.read())

print(os.getcwd())