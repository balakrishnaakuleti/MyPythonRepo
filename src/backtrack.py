# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:36:13 2018

@author: I329986
"""

def permute(numLetters, list):
    if numLetters == 1:
        return list
    else:
        return [ y + x 
                for y in permute(1, list )
                for x in permute(numLetters -1, list )
                ]
print ( permute(1, ["a","b","c"]))
print ( permute(2, ["a","b","c"]))
print ( permute(4, ["a","b","c"]))