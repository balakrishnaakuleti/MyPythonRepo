'''
Created on Jun 6, 2018

@author: Balakrishna Akuleti
'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import pylab

chart = plt.figure()

chart_3d = chart.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.08)

chart_3d.plot_wireframe(X, Y, Z, color='r',rstride=15, cstride=10)


pylab.show()
