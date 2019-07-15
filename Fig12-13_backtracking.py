# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 09:21:18 2017

@author: xiaojian
Modified by Felicia July 2019 to function with Python 3 and removed unused commands
"""
from mpl_toolkits.basemap import Basemap
#conda install -c conda-forge basemap #for Python3
import matplotlib.pyplot as plt
import numpy as np
from math import radians, cos, sin, atan, sqrt  
from datetime import datetime, timedelta

def haversine(lon1, lat1, lon2, lat2): 
    """ 
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    """   
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * atan(sqrt(a)/sqrt(1-a))   
    r = 6371 
    d=c * r
    return d


lon=np.load('lonnnnn2013X.npy', encoding='bytes')
lat=np.load('lattttt2013X.npy', encoding='bytes')
time=np.load('time2013X.npy', encoding='bytes')
temp=np.load('temp2013X.npy', encoding='bytes')

lon1=np.load('lonnnnn2012X.npy', encoding='bytes')
lat1=np.load('lattttt2012X.npy', encoding='bytes')
time1=np.load('timedian2012X.npy', encoding='bytes')
temp1=np.load('temp2012X.npy', encoding='bytes')
FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])

n=0
n1=0
dd=0
lonx=[]
latx=[]
timex=[]
num=0
fig,axes=plt.subplots(2,1,figsize=(12,6))
for a in np.arange(len(lon1)):
    for b in np.arange(len(temp1[a])):
       if temp1[a][b]>=10.5:
           x=b
           n1=n1+1
           if a==262:
               axes[0].plot(time1[a][0:x+1],temp1[a][0:x+1],color='blue',alpha=1)
               axes[0].scatter(time1[a][0],temp1[a][0],color='red',alpha=1,label='Temperature after stranding')
               axes[0].scatter(time1[a][x],temp1[a][x],color='green',alpha=1,label='Pre-freezing temperature')
           else:
               axes[0].plot(time1[a][0:x+1],temp1[a][0:x+1],color='blue',alpha=1)
               axes[0].scatter(time1[a][0],temp1[a][0],color='red',alpha=1)
               axes[0].scatter(time1[a][x],temp1[a][x],color='green',alpha=1)
          
           
           if time1[a][x]>datetime(2012,12,1,0) and time1[a][x]<datetime(2013,1,1,0):
               print ('xxxxxxxxxx2012',a)
               num=num+1
        
           lonx.append(lon1[a][0:x+1])
           latx.append(lat1[a][0:x+1])
           timex.append(time1[a][0:x+1])
           break
axes[0].legend(fontsize='large')
axes[0].set_xlim([datetime(2012,11,10),datetime(2013,1,1,0)])
axes[0].plot([datetime(2012,11,10),datetime(2012,12,11,0)],[10.5,10.5],'--',color='black')
axes[0].text(datetime(2012,12,15),9.5,'2012',fontsize=20)
axes[1].text(datetime(2013,12,15),9,'2013',fontsize=20)
axes[1].plot([datetime(2013,11,10),datetime(2013,12,11,0)],[10.5,10.5],'--',color='black')

axes[0].set_ylabel('Degree Celsius',fontsize=15)
axes[1].set_ylabel('Degree Celsius',fontsize=15)
axes[0].set_title('Temperature Along Trajectory',fontsize=17) #FMP
##########################################################################################    
for a in np.arange(len(lon)):
    for b in np.arange(len(temp[a])):
       if temp[a][b]>=10.5:
           x=b
           n1=n1+1
           axes[1].plot(time[a][0:x+1],temp[a][0:x+1],color='blue',alpha=1)
           axes[1].scatter(time[a][0],temp[a][0],color='red',alpha=1)
           axes[1].scatter(time[a][x],temp[a][x],color='green',alpha=1)
           
           if time[a][x]>datetime(2013,12,1) and time[a][x]<datetime(2014,1,1):
               print ('xxxxxxxxxx2013',a)
               num=num+1
           lonx.append(lon[a][0:x+1])
           latx.append(lat[a][0:x+1])
           timex.append(time[a][0:x+1])
           break
axes[1].set_xlim([datetime(2013,11,10),datetime(2014,1,1)])

plt.savefig('temp_2012-2013_gom3',dpi=400,bbox_inches='tight') 
plt.show()
numx0=0
numx1=0
numx2=0
numx3=0
numx4=0
xxx=0
fig,axes=plt.subplots(1,1,figsize=(6,11))
for a in np.arange(len(lonx)):
    if len(lonx[a])>=2:
        xxx=xxx+1
        if lonx[a][0]<-70.6:
            numx0=numx0+1
            print ('numx0',timex[a][0])
            axes.scatter(lonx[a][0],latx[a][0],color='red',s=40,label='Stranding location')
            axes.scatter(lonx[a][-1],latx[a][-1],color='green',s=40,label='November origin')
            axes.plot(lonx[a],latx[a])
          
        else:
            if timex[a][0]>=datetime(2012,12,1,0) and timex[a][0]<datetime(2013,1,1,0): 
                numx1=numx1+1
                axes.scatter(lonx[a][0],latx[a][0],color='red',s=40)
                axes.scatter(lonx[a][-1],latx[a][-1],color='green',s=40)
            if timex[a][0]>=datetime(2013,12,1,0) and timex[a][0]<datetime(2014,1,1,0):
                numx2=numx2+1
                axes.scatter(lonx[a][-1],latx[a][-1],color='green',s=40)
                
            if timex[a][0]<datetime(2012,12,1,0) and timex[a][0]>datetime(2012,11,1,0):
               if a==50:
                    numx3=numx3+1
                    print ('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
                    axes.scatter(lonx[a][0],latx[a][0],color='red')
                    axes.scatter(lonx[a][-1],latx[a][-1],color='blue',label='December origin')
            else:
                    numx3=numx3+1
                    axes.scatter(lonx[a][0],latx[a][0],color='red')
                    axes.scatter(lonx[a][-1],latx[a][-1],color='blue')
            if  timex[a][0]>datetime(2013,11,1,0) and timex[a][0]<datetime(2013,12,1,0):
                numx4=numx4+1
                axes.scatter(lonx[a][0],latx[a][0],color='red')
                axes.scatter(lonx[a][-1],latx[a][-1],color='blue')
            

m = Basemap(projection='cyl',llcrnrlat=41.63,urcrnrlat=43.13,\
            llcrnrlon=-71.0,urcrnrlon=-69.8,resolution='h')#,fix_aspect=False)
    #  draw coastlines
m.drawcoastlines(color='black')
m.ax=axes
m.fillcontinents(color='grey',alpha=1,zorder=2)
m.drawmapboundary()
#draw major rivers
m.drawrivers()
m.drawstates()
parallels = np.arange(41.63,43.13,0.4)
m.drawparallels(parallels,labels=[1,0,0,0],dashes=[1,1000],fontsize=10,zorder=0)
meridians = np.arange(-71.0,-69.8,0.3)
m.drawmeridians(meridians,labels=[0,0,0,1],dashes=[1,1000],fontsize=10,zorder=0)

plt.legend(fontsize='large')
plt.savefig('track_gom3',dpi=400,bbox_inches='tight') 
