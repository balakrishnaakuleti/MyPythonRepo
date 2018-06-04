# -*- coding: utf-8 -*-
"""
Created on Wed May  9 12:22:40 2018

@author: I329986
"""

class a:
    classvar =0
    __hiddenclassvar =0
    def __init__(self, b):
        #a._a__classvar += 1
        self._a__hiddenclassvar += 2;
        print("Objected created - ")
        self.b=b;
    def _str_(self):
        return "class var "+ str(a.classvar), " object var", str(self.b);
    def __str__(self):
        string = "To String; class var "+ str(a.classvar), " object var", str(self.b)
        return str(string);
    def __simply__(self):
        print("Simpley calling method")
        return;

myclass = a(10);
print(myclass)
print(myclass.__simply__())
print(a.__dict__)