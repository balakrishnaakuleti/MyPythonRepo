'''
Created on Jun 6, 2018

@author: Balakrishna Akuleti
'''

import matplotlib.pyplot as plt
import cartopy.crs as ccrs    

fig = plt.figure(figsize =(15,10))

ax = fig.add_subplot(1,1,1, projection = ccrs.PlateCarree())
ax.set_extent((60,150,55,-25))
ax.stock_img()
ax.coastlines()
ax.tissot(facecolor='purple', alpha=0.8)


plt.show()