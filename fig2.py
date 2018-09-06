# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 01:05:39 2017

@author: xiaojian
"""
from mpl_toolkits.basemap import Basemap  
import numpy as np
import matplotlib.pyplot as plt

f = np.genfromtxt('eMOLT_2012_2016_CCBay.csv',dtype=None,names=['s','t','lat','lon','deep','tem'],delimiter=',',skip_header=1)  
n=[0]
for a in np.arange(len(f['s'])-1):
    if f['s'][a]!=f['s'][a+1]:
        n.append(a+1)
n.append(len(f)-1)

fig,axes=plt.subplots(1,1,figsize=(8,10))
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
    elif f['s'][n[a]]=='AB01':
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=9,color='red')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.04,f['s'][n[a]],fontsize=8)
    elif f['s'][n[a]][:-1]=='DMF' and f['s'][n[a]]!='DMF4':
        XXX=a
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=9,marker='s',color='green')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.01,f['s'][n[a]],fontsize=8)
    elif f['s'][n[a]]=='DMF4':
        
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=9,marker='s',color='green')
        axes.text(f['lon'][n[a]]+0.02,f['lat'][n[a]]-0.01,f['s'][n[a]],fontsize=8)
    else:
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=9,color='red')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.01,f['s'][n[a]],fontsize=8)
axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=9,color='red',label='eMOLT')
axes.scatter(f['lon'][n[XXX]],f['lat'][n[XXX]],s=9,marker='s',color='green',label='DMF')

haa=[-70.566,42.52283]
axes.scatter(haa[0],haa[1],s=9,marker='^',color='blue',label='NERACOOS')
axes.text(haa[0]+0.02,haa[1],'Mooring A',fontsize=8)
axes.scatter(-70.32,41.83,s=9,marker='^',color='blue')
axes.text(-70.32+0.01,41.83-0.01,'CDIP',fontsize=8)
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
parallels = np.arange(41.5,42.7,0.2)
m.drawparallels(parallels,labels=[1,0,0,0],dashes=[1,1000],fontsize=10,zorder=0)
meridians = np.arange(-71.,-69.8,0.5)
m.drawmeridians(meridians,labels=[0,0,0,1],dashes=[1,1000],fontsize=10,zorder=0)
axes.axis([-71.,-69.8,41.5,42.7])

axes.xaxis.tick_top() 
plt.legend(loc='upper right',fontsize=8, scatterpoints=1)
plt.savefig('Fig2',dpi=400,bbox_inches='tight')
fig_saved=plt.gcf()#get current figure
fig_saved.savefig('fig2.eps',format='eps',dpi=400,bbox_inches='tight')
plt.show()