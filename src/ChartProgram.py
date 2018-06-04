# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:24:35 2018

@author: Balakrishna Akuleti
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import pylab


print('This is a smaple chart using Python:')
x = np.arange(0,10)
y = x^2
plt.xlabel("Time")
plt.ylabel("Revune")
plt.title("Revenue chart w.r.t time")
plt.plot(x,y)

plt.plot(x,y,'r')

plt.plot(x,y, '>    ')
plt.savefig("testChartPrint.pdf", format="pdf")

a = arange(15).reshape(3, 5)
print ("The matrix a is \n"+str(a))
print ("a[1,2] = " +str(a[1,2]))
print ("the matrix dimension is " + str(a.shape))

matshow(a)
pylab.show()
