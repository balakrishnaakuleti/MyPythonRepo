# -*- coding: utf-8 -*-
"""
Created on Wed May  9 11:27:25 2018

@author: I329986


"""


class MyCustomException(RuntimeError):
    def _init_(self, arg):
        self.args = arg


class a:
    classvar =0
    def _init_(self, b):
        a.classvar+=1
        print("Objected created - "+a.classvar)
        self.b=b;
    def _str_(self):
        return "class var ", a.classvar, " object var", self.b;
        

def myfunction(a,b):
    raise MyCustomException("My Cusstome exception")
    return a/b;
try:
    print("inside try");
    print(myfunction(4,2));
except MyCustomException as e:
    print("Exception Thrown");
    print(e.args);
else:
    print("He he no exception thornw !")