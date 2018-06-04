# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:11:30 2018

@author: I329986
"""
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
porter_stemmer = PorterStemmer()
word_lemmatizer = WordNetLemmatizer()

file1 = open('input.txt')

words = nltk.word_tokenize(file1.read())
for word in words:
    print('Word is - ', word+'    : Stem is : ', porter_stemmer.stem(word))
    
print()
print()
file2 = open('input.txt')

words2 = nltk.word_tokenize(file2.read())
for word in words2:
    print('Word is - ', word+'    : Lemma is : ', word_lemmatizer.lemmatize(word))