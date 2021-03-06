# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:24:35 2018

@author: I329986
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = x^2
plt.xlabel("Time")
plt.ylabel("Revune")
plt.title("Revenue chart w.r.t time")
plt.plot(x,y)

plt.plot(x,y,'r')

plt.plot(x,y, '>    ')
plt.savefig("testChartPrint.pdf", format="pdf")
