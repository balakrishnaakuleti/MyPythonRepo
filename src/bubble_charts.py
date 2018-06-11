'''
Created on Jun 5, 2018

@author: Balakrishna Akuleti
'''

import numpy as np
import matplotlib.pyplot as plt
import pylab

x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)
colors = np.random.rand(40)

plt.scatter(x=x, y=y, s=z*1000, c=colors)

pylab.show()