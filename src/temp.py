# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Importing the libraries

import time
import calendar

myintvar = 123;
myStringVar = "This is test string";

print (myintvar);
print (myStringVar);
print( "This is my input integer : %d ", myintvar)

myList = ["First Element", 123, 'C'];

print(myList);
print(myList[0]);
myList[0]= 33333333333;
print(myList);

myTuple = ("My Tuple First Element", 456, "D");
print(myTuple);
myTuple = tuple(myList) + myTuple
print(myTuple);
myList= myTuple + tuple(myList);
myTuple= myList;
myList = myTuple;

myDict = {"first":123, 2:5}
print(myDict);
print(myDict[2]);

time1 = time.time();
print(time1);

time2 = time.localtime();
print(time2);

time3 = time.asctime(time.localtime(time.time()));
print(time3);

myCal = calendar.calendar(2018, 0);
print(myCal)
print(time.timezone);
print(time.tzname)

myMonth = calendar.month(2018, 5, w=0, l=0)
print(myMonth)
myMonth2 = calendar.monthcalendar(2018, 5)
print(myMonth2)