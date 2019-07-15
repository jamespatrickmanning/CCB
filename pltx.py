# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 09:21:18 2017

@author: xiaojian
"""
from mpl_toolkits.basemap import Basemap  
from matplotlib.path import Path
import sys
import datetime as dt
from matplotlib.path import Path
import netCDF4
import matplotlib.pyplot as plt
from dateutil.parser import parse
import numpy as np
import math
import pandas as pd
from datetime import datetime, timedelta
from math import radians, cos, sin, atan, sqrt  
from matplotlib.dates import date2num,num2date
def haversine(lon1, lat1, lon2, lat2): 
    """ 
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    """   
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
    #print 34
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * atan(sqrt(a)/sqrt(1-a))   
    r = 6371 
    d=c * r
    #print type(d)
    return d
#np.save('lonnnnn201360x15XXXXXXX',lonnnnn)#.append(back['lon'])
#np.save('lattttt201360x15XXXXXXX',lattttt)#.append(back['lat'])
#np.save('time201360x15XXXXXXX',timedian)
#np.save('temp201360x15XXXXXXX',tempp)

lon=np.load('lonnnnn2013X.npy')
lat=np.load('lattttt2013X.npy')
time=np.load('time2013X.npy')
temp=np.load('temp2013X.npy')

lon1=np.load('lonnnnn2012X.npy')
lat1=np.load('lattttt2012X.npy')
time1=np.load('timedian2012X.npy')
temp1=np.load('temp2012X.npy')
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
#plt.figure(figsize=(10,5))
for a in np.arange(len(lon1)):
    for b in np.arange(len(temp1[a])):
       if temp1[a][b]>=10.5:
           x=b
           n1=n1+1
           #print 'jjjjjjjjjjjjjjjjjjjjjj',a
           if a==262:
               #plt.plot([time1[a][0],time1[a][x]],[temp1[a][0],temp1[a][x]],color='blue')
               axes[0].plot(time1[a][0:x+1],temp1[a][0:x+1],color='blue',alpha=1)
               axes[0].scatter(time1[a][0],temp1[a][0],color='red',alpha=1,label='Temperature after stranding')
               axes[0].scatter(time1[a][x],temp1[a][x],color='green',alpha=1,label='Pre-freezing temperature')
           else:
               axes[0].plot(time1[a][0:x+1],temp1[a][0:x+1],color='blue',alpha=1)
               axes[0].scatter(time1[a][0],temp1[a][0],color='red',alpha=1)
               axes[0].scatter(time1[a][x],temp1[a][x],color='green',alpha=1)
          
           
           if time1[a][x]>datetime(2012,12,1,0) and time1[a][x]<datetime(2013,1,1,0):
               print 'xxxxxxxxxx2012',a
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
axes[0].set_title('the temperature along the trajectory',fontsize=17)
#plt.savefig('temp2012',dpi=400,bbox_inches='tight')
#plt.show() 
#plt.figure(figsize=(10,5))
##########################################################################################    
for a in np.arange(len(lon)):
    for b in np.arange(len(temp[a])):
       if temp[a][b]>=10.5:
           x=b
           n1=n1+1
           #plt.plot([time[a][0],time[a][x]],[temp[a][0],temp[a][x]],color='blue')
           axes[1].plot(time[a][0:x+1],temp[a][0:x+1],color='blue',alpha=1)
           axes[1].scatter(time[a][0],temp[a][0],color='red',alpha=1)
           axes[1].scatter(time[a][x],temp[a][x],color='green',alpha=1)
           
           if time[a][x]>datetime(2013,12,1) and time[a][x]<datetime(2014,1,1):
               print 'xxxxxxxxxx2013',a
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
            print 'numx0',timex[a][0]
            #if timex[a][0]>datetime(2012,12,1): 
            axes.scatter(lonx[a][0],latx[a][0],color='red',s=40,label='end point')
            axes.scatter(lonx[a][-1],latx[a][-1],color='green',s=40,label='start point')
            axes.plot(lonx[a],latx[a])
            '''
            if timex[a][0]>datetime(2013,12,1):
                axes.scatter(lonx[a][0],latx[a][0],color='red',s=40)
                axes.scatter(lonx[a][-1],latx[a][-1],color='blue',s=40)
                axes.plot(lonx,latx)
            if timex[a][0]<datetime(2012,12,1):
                axes.scatter(lonx[a][0],latx[a][0],color='red')
                axes.scatter(lonx[a][-1],latx[a][-1],color='blue')
                axes.plot(lonx,latx)
            if  timex[a][0]<datetime(2013,12,1):
                axes.scatter(lonx[a][0],latx[a][0],color='red')
                axes.scatter(lonx[a][-1],latx[a][-1],color='blue')
                axes.plot(lonx,latx)
            '''
        else:
            if timex[a][0]>=datetime(2012,12,1,0) and timex[a][0]<datetime(2013,1,1,0): 
                '''
                ds=(timex[a][0]-timex[a][-1]).days+(timex[a][0]-timex[a][-1]).seconds/(60*60*24.0)
                l=ds*20000/3.0/111111
                
                p1 = plt.Circle((lonx[a][-1],latx[a][-1]),l,color='green',alpha=0.01)
                
                axes.add_patch(p1)
                '''
                numx1=numx1+1
                axes.scatter(lonx[a][0],latx[a][0],color='red',s=40)
                axes.scatter(lonx[a][-1],latx[a][-1],color='green',s=40)
            if timex[a][0]>=datetime(2013,12,1,0) and timex[a][0]<datetime(2014,1,1,0):
                #ds=(timex[a][0]-timex[a][-1]).days+(timex[a][0]-timex[a][-1]).seconds/(60*60*24.0)
                '''
                ds=(timex[a][0]-timex[a][-1]).days+(timex[a][0]-timex[a][-1]).seconds/(60*60*24.0)
                l=ds*20000/3.0/111111
                
                p1 = plt.Circle((lonx[a][-1],latx[a][-1]),l,color='green',alpha=0.01)
                axes.add_patch(p1)
                '''
                numx2=numx2+1
                #axes.scatter(lonx[a][0],latx[a][0],color='red',s=40)
                axes.scatter(lonx[a][-1],latx[a][-1],color='green',s=40)
                
            if timex[a][0]<datetime(2012,12,1,0) and timex[a][0]>datetime(2012,11,1,0):
                '''
                ds=(timex[a][0]-timex[a][-1]).days+(timex[a][0]-timex[a][-1]).seconds/(60*60*24.0)
                l=ds*20000/3.0/111111
                
                p1 = plt.Circle((lonx[a][-1],latx[a][-1]),l,color='green',alpha=0.01)
                axes.add_patch(p1)
                '''
                #print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',a
                if a==50:
                    numx3=numx3+1
                    print 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
                    axes.scatter(lonx[a][0],latx[a][0],color='red')
                    axes.scatter(lonx[a][-1],latx[a][-1],color='blue',label='start point')
                else:
                    numx3=numx3+1
                    axes.scatter(lonx[a][0],latx[a][0],color='red')
                    axes.scatter(lonx[a][-1],latx[a][-1],color='blue')
                #print 'munx3',lonx[a][-1],latx[a][-1]
            if  timex[a][0]>datetime(2013,11,1,0) and timex[a][0]<datetime(2013,12,1,0):
                '''
                ds=(timex[a][0]-timex[a][-1]).days+(timex[a][0]-timex[a][-1]).seconds/(60*60*24.0)
                l=ds*20000/3.0/111111
                
                p1 = plt.Circle((lonx[a][-1],latx[a][-1]),l,color='green',alpha=0.01)
                #ds=(timex[a][0]-timex[a][-1]).days+(timex[a][0]-timex[a][-1]).seconds/(60*60*24.0)
                axes.add_patch(p1)
                '''
                numx4=numx4+1
                #print 'numx4',timex[a][0]
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

"""
plt.plot(CL['lon'],CL['lat'],linewidth=0.7)
plt.axis([-71.0,-69.8,41.63,43.5])
"""
plt.legend(fontsize='large')
plt.savefig('track_gom3',dpi=400,bbox_inches='tight') 
