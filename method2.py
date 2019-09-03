# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 18:31:28 2018

@author: xiaojian
Modifications by JiM in Sep 2019 after PlosOne 2nd review
Note: There are two options using the circle.
"""
from math import radians, cos, sin, atan, sqrt 
import numpy as np
from matplotlib.path import Path
from scipy import  interpolate
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
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


lon=-70.087
lat=41.767
size=0.03
r=0.015#unit degree
track_days=7
km=1.5
degree=km/111.0
endtime =datetime(2014,11,22,12,0,0)
starttime=endtime-timedelta(hours=track_days*24)

FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])
cl=dict(lon=[],lat=[])
for a in np.arange(len(CL['lon'])):
    if CL['lon'][a]>lon-size and CL['lon'][a]<lon+size and CL['lat'][a]<lat+size and CL['lat'][a]>lat-size:
        cl['lon'].append(CL['lon'][a])
        cl['lat'].append(CL['lat'][a])

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
ax.plot(cl['lon'],cl['lat'],color='black')
ax.scatter(lon,lat,color='red',s=80)
ax.axis([lon-size,lon+size,lat-size,lat+size])
cir1 = Circle(xy = (lon, lat), radius=r, alpha=0.5)
ax.add_patch(cir1)
p = Path.circle((lon,lat),radius=r)
points = np.vstack((np.array(cl['lon']).flatten(),np.array(cl['lat']).flatten())).T  
insidep = []
#collect the points included in Path.
for i in np.arange(len(points)):
    if p.contains_point(points[i]):# .contains_point return 0 or 1
        insidep.append(points[i])  
lon1=insidep[0][0]
lat1=insidep[0][1]

lon2=insidep[-1][0]
lat2=insidep[-1][1]

ax.scatter(lon1,lat1,s=80,color='green')
ax.scatter(lon2,lat2,s=80,color='green')
lonz=(lon1+lon2)/2.0
latz=(lat1+lat2)/2.0
ax.scatter(lonz,latz,color='green',s=80)
ax.plot([lon1,lon2],[lat1,lat2])
ax.scatter(lonz,latz,s=80)



k=(latz-lat)/(lonz-lon)

lon_w1=lonz+np.sqrt(degree**2/(1+k**2))
lon_w2=lonz-np.sqrt(degree**2/(1+k**2))
d1=abs(lon_w1-lon)
d2=abs(lon_w2-lon)
if d1>d2:
    lon_w=lon_w1
    lat_w=k*(lon_w-lonz)+latz
else:
    lon_w=lon_w2
    lat_w=k*(lon_w-lonz)+latz
ax.scatter(lon_w,lat_w,color='cyan',s=80)
ax.plot([lon,lon_w],[lat,lat_w])
plt.gca().ticklabel_format(axis='both', style='plain', useOffset=False)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.savefig('/net/pubweb_html/epd/ocean/MainPage/turtle/ccbay/circle1.png')
plt.show()
#######################################################################################################3
lon=-70.087
lat=41.767
size=0.03
r=0.010#unit degree
track_days=7
km=1.5
degree=km/111.0
endtime =datetime(2014,11,22,12,0,0)
starttime=endtime-timedelta(hours=track_days*24)

FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])
cl=dict(lon=[],lat=[])
for a in np.arange(len(CL['lon'])):
    if CL['lon'][a]>lon-size and CL['lon'][a]<lon+size and CL['lat'][a]<lat+size and CL['lat'][a]>lat-size:
        cl['lon'].append(CL['lon'][a])
        cl['lat'].append(CL['lat'][a])

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
ax.plot(cl['lon'],cl['lat'],color='black')
ax.scatter(lon,lat,color='red',s=80)
ax.axis([lon-size,lon+size,lat-size,lat+size])
cir1 = Circle(xy = (lon, lat), radius=r, alpha=0.5)
ax.add_patch(cir1)
p = Path.circle((lon,lat),radius=r)
points = np.vstack((np.array(cl['lon']).flatten(),np.array(cl['lat']).flatten())).T  
insidep = []
#collect the points included in Path.
for i in np.arange(len(points)):
    if p.contains_point(points[i]):# .contains_point return 0 or 1
        insidep.append(points[i])  
lon1=insidep[0][0]
lat1=insidep[0][1]

lon2=insidep[-1][0]
lat2=insidep[-1][1]

ax.scatter(lon1,lat1,s=80)
ax.scatter(lon2,lat2,s=80)
lonz=(lon1+lon2)/2.0
latz=(lat1+lat2)/2.0
ax.scatter(lonz,latz,color='green',s=80)
ax.plot([lon1,lon2],[lat1,lat2])
ax.scatter(lonz,latz,s=80,)



k=(latz-lat)/(lonz-lon)

lon_w1=lonz+np.sqrt(degree**2/(1+k**2))
lon_w2=lonz-np.sqrt(degree**2/(1+k**2))
d1=abs(lon_w1-lon)
d2=abs(lon_w2-lon)
if d1>d2:
    lon_w=lon_w1
    lat_w=k*(lon_w-lonz)+latz
else:
    lon_w=lon_w2
    lat_w=k*(lon_w-lonz)+latz
ax.scatter(lon_w,lat_w,color='cyan',s=80)
ax.plot([lon,lon_w],[lat,lat_w])
plt.gca().ticklabel_format(axis='both', style='plain', useOffset=False)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.savefig('/net/pubweb_html/epd/ocean/MainPage/turtle/ccbay/circle2.png')
plt.show()
#######################################################################################



