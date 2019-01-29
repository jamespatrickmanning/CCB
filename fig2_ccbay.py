# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 01:05:39 2017

@author: xiaojian
Modified by JiM in Dec 2018 to optionally add model points (using "fig11.py")
"""
from mpl_toolkits.basemap import Basemap  
import numpy as np
import matplotlib.pyplot as plt

#HARDCODES
addmodelpts='yes'
##########
fig,axes=plt.subplots(1,1,figsize=(8,10))
if addmodelpts=='yes':
  # add model surf temp sites
  lon10=np.linspace(-70.45,-70.2,10)
  lat10=np.linspace(42.05,41.8,10)
  axes.scatter(lon10,lat10,color='k',marker='*',s=40,label='Model Surface Temperatures')
  # add model wind sites
  lat=np.linspace(41.8,42.4,10)
  lon=np.linspace(-70.15,-70.75,10)
  axes.scatter(lon,lat,color='green',marker='o',s=40,label='Model Winds')

f = np.genfromtxt('eMOLT_2012_2016_CCBay.csv',dtype=None,names=['s','t','lat','lon','deep','tem'],delimiter=',',skip_header=1)  
n=[0]
for a in np.arange(len(f['s'])-1):
    if f['s'][a]!=f['s'][a+1]:
        n.append(a+1)
n.append(len(f)-1)


#FNCL='necscoast_worldvec.dat'
# lon lat pairs
# segments separated by nans

label=['A','B','C','D','E','F','G','H','I','J']
dian=['a','b','c','d','e','f','g','h','i','j']


#CL=np.genfromtxt(FNCL,names=['lon','lat'])
XXX=0
for a in np.arange(len(n)-1):
    if f['s'][n[a]]=='RM03' or f['s'][n[a]]=='BS02':
        pass
    elif f['s'][n[a]]=='AB01': #case where labels needs to be much higher
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,color='red')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.04,f['s'][n[a]],fontsize=10)
    elif f['s'][n[a]]=='DK01': #case where labels needs to be a bit higher
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,color='red')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.025,f['s'][n[a]],fontsize=10)
    elif f['s'][n[a]][:-1]=='DMF' and f['s'][n[a]]!='DMF4':
        XXX=a
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,marker='s',color='green')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.01,f['s'][n[a]],fontsize=10)
    elif f['s'][n[a]]=='DMF4':     
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,marker='s',color='green')
        axes.text(f['lon'][n[a]]+0.02,f['lat'][n[a]]-0.01,f['s'][n[a]],fontsize=10)
    else:
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,color='red')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.01,f['s'][n[a]],fontsize=10)
axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=9,color='red',label='Observed eMOLT')
axes.scatter(f['lon'][n[XXX]],f['lat'][n[XXX]],s=9,marker='s',color='green',label='Observed DMF')

haa=[-70.566,42.52283]
axes.scatter(haa[0],haa[1],s=40,marker='^',color='blue',label='Observed NERACOOS')
axes.text(haa[0]+0.02,haa[1],'Mooring A',fontsize=10)
axes.scatter(-70.32,41.83,s=40,marker='^',color='blue')
axes.text(-70.32+0.01,41.83-0.01,'CDIP',fontsize=10)
#axes.plot(CL['lon'],CL['lat'],linewidth=1)

m = Basemap(projection='cyl',llcrnrlat=41.5,urcrnrlat=42.7,\
            llcrnrlon=-71,urcrnrlon=-69.8,resolution='h')#,fix_aspect=False)
    #  draw coastlines
m.drawcoastlines(color='black')
m.ax=axes
m.fillcontinents(color='grey',alpha=1,zorder=2)
m.drawmapboundary()
#draw major rivers
#m.drawrivers()
parallels = np.arange(41.5,42.6,0.2)
m.drawparallels(parallels,labels=[1,0,0,0],dashes=[1,1000],fontsize=10,zorder=0)
meridians = np.arange(-71.,-69.8,0.5)
m.drawmeridians(meridians,labels=[0,0,0,1],dashes=[1,1000],fontsize=10,zorder=0)
axes.axis([-71.,-69.8,41.5,42.6])

axes.xaxis.tick_top() 
plt.legend(loc='upper right',fontsize=10, scatterpoints=1)
plt.savefig('/net/home3/ocn/jmanning/drift/noaaoe/figures/fig2_ccbay',dpi=400,bbox_inches='tight')
fig_saved=plt.gcf()#get current figure
fig_saved.savefig('/net/home3/ocn/jmanning/drift/noaaoe/figures/fig2_ccbay.eps',format='eps',dpi=400,bbox_inches='tight')
plt.show()
