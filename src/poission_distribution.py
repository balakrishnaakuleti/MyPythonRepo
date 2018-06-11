'''
Created on Jun 11, 2018

@author: Balakrishna Akuleti
'''

from scipy.stats import poisson
import seaborn as sb
import matplotlib.pyplot as plt


data_poission = poisson.rvs(mu=4, size = 10000)
ax = sb.distplot(data_poission, kde=True,color='green', hist_kws={"linewidth": 25,'alpha':1})

ax.set(xlabel='Poisson', ylabel='Frequency')
plt.show()

