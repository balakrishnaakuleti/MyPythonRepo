# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:59:15 2018

@author: I329986
"""

import nltk

file1 = open('input.txt')
print(nltk.sent_tokenize(file1.read()))

print()
file2 = open('input.txt')
print(nltk.word_tokenize(file2.read()))
