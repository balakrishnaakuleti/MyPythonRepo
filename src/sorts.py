# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:37:15 2018

@author: I329986
"""
# BUBBLE SORT
def bubbleSort(list):
    for selected_Num_Index in range(len(list)-1, 0,-1):
        for i in range (selected_Num_Index):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i]=list[i+1]
                list[i+1]= temp;
# MERGE SORT
def mergeSort(list):
    if(len(list)<=1):
        return list
    middle = len(list)//2
    left_list = list[:middle]
    right_list = list[middle:]
    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)
    return (merge(left_list,right_list ))

def merge(left_half, right_half):
    res = []
    while(len(left_half) >0 and len(right_half) >0):
        if(left_half[0] < right_half[0]):
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if(len(left_half) == 0 ):
        res = res +right_half
    else:
        res = res + left_half
    return res

def insertionSort(list):
    # iterate from second element till the end
    for index in range(len(list)-1):
        tempIndex = index;
        eleToInsert =list[index+1]
        # take the element, compare with its prev till beginning till mismatch
        while (eleToInsert < list[tempIndex] and tempIndex>=0 ):
           # If mistmach first shift and then swap elements
           list[tempIndex+1] = list[tempIndex]
           tempIndex = tempIndex -1
        list[tempIndex+1] = eleToInsert
        
def shellSort(list):
    gap = len(list)/2
    while gap >0 :
        for temp in range(gap, len(list)):
            tempval = list[temp]
            mismatch=temp;
            while mismatch>=gap and temp < list[mismatch-gap]:
                list[mismatch]= list[mismatch-gap]
                mismatch = mismatch-gap
            list[mismatch] = tempval
        gap = gap/2
               
def selectionSort(list):
    for i in range(len(list)):
        small=i
        for j in range(i+1, len(list)):
            if list[j]<list[small]:
                small = j
        list[small], list[i]= list[i],list[small]
        
list = [45,76,12,34,99,8,44,89,34,66]
print("Bubble Sort:")
print(list)
bubbleSort(list)
print(list)

list2 = [64, 34, 25, 12, 22, 11, 90]
print("Merge Sort:")
print(list2)
print(mergeSort(list2))


list3 = [64, 34, 25, 12, 22, 11, 90]
print("Insertion Sort:")
print(list3)
insertionSort(list3)
print(list3)

list4 = [64, 34, 25, 12, 22, 11, 90]
print("Shell Sort:")
print(list4)
insertionSort(list4)
print(list4)


list5 = [19,2,31,45,30,11,121,27]
print("Selection Sort:")
print(list5)
insertionSort(list5)
print(list5)