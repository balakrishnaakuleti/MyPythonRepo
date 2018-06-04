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
y = x*x
print(y)
plt.plot(x,y)
pylab.show()