# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:51:35 2018

@author: I329986
"""

def linearSearch(list, toFind):
    for i in range(0, len(list)):
        if toFind is list[i]:
            return i
    return False
def binarySearch(list, searchTerm):
    mid= int(len(list)/2)
    left = 0
    right = len(list)
    while searchTerm != list[mid] and left != right:
        if searchTerm >list[mid]:
            left = mid+1
        else:
            right = mid=1
    return mid
        
 
def selectionSort(list):
    for i in range(len(list)):
        small=i
        for j in range(i+1, len(list)):
            if list[j]<list[small]:
                small = j
        list[small], list[i]= list[i],list[small]

list = [12,54,11,99,56,66,22,98]
print(list)
selectionSort(list)
print(list)
print("Lenear Search of 56 is " +str(linearSearch(list, 56)))
print("Binary Search of 56 is " +str(binarySearch(list, 56)))

print (linearSearch)
