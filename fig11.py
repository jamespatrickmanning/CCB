# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 01:05:39 2017

@author: xiaojian
"""
from mpl_toolkits.basemap import Basemap  

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pytz
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pytz import timezone
import numpy as np
import csv
from scipy import  interpolate
from matplotlib.dates import date2num,num2date


fig=plt.figure(figsize=(8,10))
axes1=fig.add_subplot(1,1,1)

lon10=np.linspace(-70.45,-70.2,10)
lat10=np.linspace(42.05,41.8,10)
#axes1.axis([-70.75,-69.8,41.5,42.23])
axes1.scatter(lon10,lat10,color='red',s=7)



label=['A','B','C','D','E','F','G','H','I','J']
dian=['a','b','c','d','e','f','g','h','i','j']


for a in np.arange(len(label)):
    axes1.text(lon10[a]-0.05,lat10[a]-0.03,label[a],fontsize=12)


#axes3.set_xlabel('c',fontsize=12)

lat=np.linspace(41.8,42.4,10)
lon=np.linspace(-70.15,-70.75,10)

#CL=np.genfromtxt(FN,names=['lon','lat'])
#axes3.plot(CL['lon'],CL['lat'])
#axes3.axis([-70.94,-70.0,41.52659,42.562711])
axes1.scatter(lon,lat,s=7,color='green')
for a in np.arange(len(lon)):
    axes1.text(lon[a]+0.02,lat[a],dian[a],fontsize=12)
#axes3.xaxis.tick_top() 
m = Basemap(projection='cyl',llcrnrlat=41.5,urcrnrlat=42.5,\
            llcrnrlon=-71,urcrnrlon=-70.0,resolution='h')#,fix_aspect=False)
    #  draw coastlines
m.drawcoastlines(color='black')
m.ax=axes1
m.fillcontinents(color='grey',alpha=1,zorder=2)
m.drawmapboundary()
#draw major rivers
#m.drawrivers()
parallels = np.arange(41.5,42.5,0.2)
m.drawparallels(parallels,labels=[1,0,0,0],dashes=[1,1000],fontsize=10,zorder=0)
meridians = np.arange(-71,-69.98,0.5)
m.drawmeridians(meridians,labels=[0,0,0,1],dashes=[1,1000],fontsize=10,zorder=0)

plt.savefig('fig11',dpi=400,bbox_inches='tight')
fig_saved=plt.gcf()#get current figure
fig_saved.savefig('fig11.eps',format='eps',dpi=400,bbox_inches='tight')
plt.show()
