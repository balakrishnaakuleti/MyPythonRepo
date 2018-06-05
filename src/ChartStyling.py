# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:24:39 2018

@author: Balakrishna Akuleti
"""

import numpy as np
from matplotlib import pyplot as plt
import pylab

x = np.arange(0,10)
print(x)
y = x^2
z = x^3
t = x^4
print(y)
plt.plot(x,y,'g')
#plt.plot(x,y,'>')
# Titles and Axis Labels
plt.title('Time Vs Speed Graph')
plt.xlabel('Time')
plt.ylabel('Speed')

#Annotating points
plt.annotate(xy=[0,2], s='First Entry')
plt.annotate(xy=[4,6], s='Second Entry')

#Plotting multiple graphs
plt.plot(x,z)
plt.plot(x,t)

#Legend
plt.legend(['x','y','z'], loc=4)

#Styling 

plt.style.use('fast')
plt.plot(x,z)


pylab.show()