# -*- coding: utf-8 -*-
"""
First Created on Thu Aug 03 20:55:51 2017
Figure 10 of CCBay manuscript w/4 panels
@author: xiaojian
Assumes preliminary programs s1-s4 have already been run in this folder
Modified by JiM to underlay Xiaojian's "variance_ellipses"
Modified by Felicia June 2019 to function in Python 3
"""
#conda install -c conda-forge pydap #this is necessary first run only for Python 3 and took many minutes on my desktop
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import sys
from pydap.client import open_url
import time
import variance_ellipse_function_felicia 
from matplotlib import cm #added for SST colormap gradient in Python 3

#  HARDCODES #############
temprange=np.arange(5,14,0.05)
colorticks=np.linspace(5,14,10)
time_wanted=[dt.datetime(2014,11,3,23,59,59,0),dt.datetime(2014,12,19,23,59,59,0),dt.datetime(2014,12,26,23,59,59,0)]# these are datetimes associated with clear SST imagery
url=['http://basin.ceoe.udel.edu/thredds/dodsC/ModisAqua/2014/aqua.2014307.1103.235959.D.L3.modis.NAT.v09.1000m.nc4','http://basin.ceoe.udel.edu/thredds/dodsC/ModisAqua/2014/aqua.2014323.1119.235959.D.L3.modis.NAT.v09.1000m.nc4','http://basin.ceoe.udel.edu/thredds/dodsC/ModisAqua/2014/aqua.2014360.1226.235959.D.L3.modis.NAT.v09.1000m.nc4']
gbox=[-70.75,-69.8,41.5,42.23]
legend_pos=[-70.58,41.64]
legend_size=0.05
max_ellipse_to_ignore=0.5 #m/s2 where Nantucket shoals tides are near 0.
latsize=[gbox[2],gbox[3]]
lonsize=[gbox[0],gbox[1]]
fig_name='wind_current_strandings_sst'

# FUNCTION TO BIN VARIABLES
def sh_bindata(x, y, z, xbins, ybins):
    """
    Bin irregularly spaced data on a rectangular grid.

    """
    ix=np.digitize(x,xbins)
    iy=np.digitize(y,ybins)
    xb=0.5*(xbins[:-1]+xbins[1:]) # bin x centers
    yb=0.5*(ybins[:-1]+ybins[1:]) # bin y centers
    zb_mean=np.empty((len(xbins)-1,len(ybins)-1),dtype=z.dtype)
    zb_median=np.empty((len(xbins)-1,len(ybins)-1),dtype=z.dtype)
    zb_std=np.empty((len(xbins)-1,len(ybins)-1),dtype=z.dtype)
    zb_num=np.zeros((len(xbins)-1,len(ybins)-1),dtype=int)    
    for iix in range(1,len(xbins)):
        for iiy in range(1,len(ybins)):
            k,=np.where((ix==iix) & (iy==iiy))
            zb_mean[iix-1,iiy-1]=np.mean(z[k])
            zb_median[iix-1,iiy-1]=np.median(z[k])
            zb_std[iix-1,iiy-1]=np.std(z[k])
            zb_num[iix-1,iiy-1]=len(z[k])
            
    return xb,yb,zb_mean,zb_median,zb_std,zb_num
#################################################

#  MAIN ROUTINE
# load wind positions
lon=np.load('low.npy')
lat=np.load('law.npy')
# load wind positions and
lo18_23=np.load('lo18_23.npy')
la18_23=np.load('la18_23.npy')
us18_23=np.load('us18_23.npy')
vs18_23=np.load('vs18_23.npy')
# load model velocities derived from MassBay grid
lo=np.load('lombx.npy')
la=np.load('lambx.npy')
umb18_23=np.load('umb18_23.npy')#This needs to be requested from the author because it was too large for GitHub
vmb18_23=np.load('vmb18_23.npy') #This needs to be requested from the author because it was too large for GitHub
# load 0-30 Nov 2014 winds
lof=np.load('lo0_30.npy')
laf=np.load('la0_30.npy')
us1=np.load('us0_30.npy')
vs1=np.load('vs0_30.npy')
FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])

# BIN U&V FIELDS
#xi = np.arange(-70.75,-69.8,0.05)
xi = np.arange(gbox[0],gbox[1],0.05)
#yi = np.arange(41.5,42.23,0.05)
yi = np.arange(gbox[2],gbox[3],0.05)
# wind 18_23
xb,yb,ub_mean,ub_median,ub_std,ub_num = sh_bindata(np.array(lo18_23), np.array(la18_23), np.array(us18_23), xi, yi)
xb,yb,vb_mean,vb_median,vb_std,vb_num = sh_bindata(np.array(lo18_23), np.array(la18_23), np.array(vs18_23), xi, yi)
# current 18_23
xb1,yb1,ub_mean1,ub_median1,ub_std1,ub_num1 = sh_bindata(np.array(lo), np.array(la), np.array(umb18_23), xi, yi)
xb1,yb1,vb_mean1,vb_median1,vb_std1,vb_num1 = sh_bindata(np.array(lo), np.array(la), np.array(vmb18_23), xi, yi)
# wind 0_30
xb2,yb2,ub_mean2,ub_median2,ub_std2,ub_num2 = sh_bindata(np.array(lof), np.array(laf), np.array(us1), xi, yi)
xb2,yb2,vb_mean2,vb_median2,vb_std2,vb_num2 = sh_bindata(np.array(lof), np.array(laf), np.array(vs1), xi, yi)

#########################333

xxb,yyb = np.meshgrid(xb, yb)

fig,axes=plt.subplots(2,2,figsize=(15,10))
# panel up-left wind 18_23
ub = np.ma.array(ub_mean, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_mean, mask=np.isnan(vb_mean))
Q=axes[0,0].quiver(xxb,yyb,ub.T,vb.T,scale=300.)
qk=axes[0,0].quiverkey(Q,0.1,0.5,10, r'$10m/s$', fontproperties={'weight': 'bold'},zorder=1)
# panel up-right current 18_23
ub1 = np.ma.array(ub_mean1, mask=np.isnan(ub_mean))
vb1 = np.ma.array(vb_mean1, mask=np.isnan(vb_mean))
Q=axes[0,1].quiver(xxb,yyb,ub1.T,vb1.T,scale=4.)
qk=axes[0,1].quiverkey(Q,0.1,0.4,0.2, r'$0.2m/s$', fontproperties={'weight': 'bold'},zorder=1)
print ('plotting variance ellipses')
variance_ellipse_function_felicia.variance_ellipses_under_means(axes[0,1],gbox,legend_pos,legend_size,max_ellipse_to_ignore)
lonnn=lon
lattt=lat

####################################################################
c = np.genfromtxt('strandings20141118.csv',dtype=None,names=['a1','a2','a3','a4','a5','a6','a7','a8'],delimiter=',',skip_header=1)  
news=[]
for a in c['a6']:
    #print a
    if a not in news:
        news.append(a)
num=[]
for a in np.arange(len(news)):
    j=0
    for b in np.arange(len(c['a6'])):
        if news[a]==c['a6'][b]:
            j=j+1
    num.append(j)            
    news[a]
# positions for each town
lon=[-70.0490,-69.9740,-69.9897,-70.0310,-69.9598,-70.0828,-70.1786,-70.6345,-70.5989,-70.1939,-70.0972,-70.9078]
lat=[41.9948,41.8300,41.7898,41.9305,41.6821,41.7601,42.0584,41.6043,41.7413,41.7353,42.0393,42.3021]

#axes[1,0].axis([-70.75,-69.8,41.5,42.23])
axes[1,0].axis(gbox)
for a in np.arange(len(num)):
    axes[1,0].scatter(lon[a],lat[a],s=num[a]*3,color='red')
axes[1,0].text(lon[0]+0.05,lat[0],(news[0]).decode('utf-8'))
axes[1,0].text(lon[1]+0.05,lat[1],(news[1]).decode('utf-8'))
axes[1,0].text(lon[2]+0.06,lat[2],(news[2]).decode('utf-8'))
axes[1,0].text(lon[3]+0.05,lat[3],(news[3]).decode('utf-8'))
axes[1,0].text(lon[4]+0.03,lat[4],(news[4]).decode('utf-8'))
axes[1,0].text(lon[5]-0.05,lat[5]-0.03,(news[5]).decode('utf-8'))
axes[1,0].text(lon[6]-0.05,lat[6]+0.03,(news[6]).decode('utf-8'))
axes[1,0].text(lon[7]+0.005,lat[7]+0.01,(news[7]).decode('utf-8'))
axes[1,0].text(lon[8]+0.02,lat[8],(news[8]).decode('utf-8'))
axes[1,0].text(lon[9]-0.05,lat[9]-0.04,(news[9]).decode('utf-8'))
axes[1,0].text(lon[10]+0.04,lat[10]+0.01,(news[10]).decode('utf-8'))
axes[1,0].text(lon[0]-0.025,lat[0]-0.01,str(num[0]),color='white',weight='bold')#print totals for Truro
axes[1,0].text(lon[1]-0.025,lat[1]-0.01,str(num[1]),color='white',weight='bold')#print totals for Eastham
axes[1,0].text(lon[3]-0.025,lat[3]-0.01,str(num[3]),color='white',weight='bold')#print totals for Eastham


axes[0,0].set_xticklabels([])
axes[0,1].set_xticklabels([])
#axes[1,0].xaxis.tick_top()
axes[0,1].set_yticklabels([])
#axes[1,0].set_xticklabels([])
axes[0,0].set_title('a',fontsize=20)
axes[0,1].set_title('b',fontsize=20)
axes[1,0].set_title('c',fontsize=20)
 
#############################################################

#mthly mean wind
ub2 = np.ma.array(ub_mean2, mask=np.isnan(ub_mean))
vb2 = np.ma.array(vb_mean2, mask=np.isnan(vb_mean))
Q=axes[1,1].quiver(xxb,yyb,ub2.T,vb2.T,scale=300.)
qk=axes[1,1].quiverkey(Q,0.1,0.4,10, r'$10m/s$', fontproperties={'weight': 'bold'},zorder=1)
axes[1,0].plot(CL['lon'],CL['lat'])
axes[0,0].plot(CL['lon'],CL['lat'])
axes[1,1].plot(CL['lon'],CL['lat'])
axes[0,1].plot(CL['lon'],CL['lat'])
axes[0,1].axis(gbox)
axes[1,1].axis(gbox)
axes[1,0].axis(gbox)
axes[0,0].axis(gbox)



axes[1,1].set_yticklabels([])
axes[1,1].set_title('d',fontsize=20)


################################################
# add SST imagery

for i in range(len(url)):
    dataset=open_url(url[i])
    times=list(dataset['time'])  
    second=time.mktime(time_wanted[i].timetuple())
    index=int(round(np.interp(second,times,range(len(times)))))
    url1=url[i]+'?lat[0:1:4499],lon[0:1:4999],'+'sst['+str(index)+':1:'+str(index)+'][0:1:4499][0:1:4999]'+',time['+str(index)+':1:'+str(index)+']'
    try:
        print(url1)
        dataset1=open_url(url1)
    except:
        print("please check your url!")
        sys.exit(0)   
    sst=dataset1['sst'].sst
    lat=dataset1['lat']
    lon=dataset1['lon']
    # find the index for the gbox
    index_lon11=int(round(np.interp(gbox[0],list(lon),range(len(list(lon))))))
    index_lon12=int(round(np.interp(gbox[1],list(lon),range(len(list(lon))))))
    index_lat11=int(round(np.interp(gbox[2],list(lat),range(len(list(lat))))))
    index_lat12=int(round(np.interp(gbox[3],list(lat),range(len(list(lat))))))
    # get part of the sst
    sst_part=np.array(sst[index,index_lat11:index_lat12,index_lon11:index_lon12])
    sst_part[sst_part==-999.]=np.NaN # if sst_part=-999, convert to NaN # JiM commented out 7/8/2019
    X1,Y1=np.meshgrid(lon[index_lon11:index_lon12],lat[index_lat11:index_lat12])
    if i==0: #upper left
        conf=axes[0,0].contourf(X1,Y1,sst_part[0],temprange,cmap=cm.jet,zorder=0)
    elif i==1: #lower left
        conf=axes[1,0].contourf(X1,Y1,sst_part[0],temprange,cmap=cm.jet,zorder=0)
    else: #i==2
        conf=axes[1,1].contourf(X1,Y1,sst_part[0],temprange,cmap=cm.jet,zorder=0)

fig.subplots_adjust(right=0.83,hspace=0.1,wspace=0.1)
cbar_ax=fig.add_axes([0.85,0.15,0.015,0.7])#[left,bottom,right,top]
cb=fig.colorbar(conf,cax=cbar_ax)
cb.set_ticks(colorticks)
cb.ax.tick_params(labelsize=12)
#cb.set_ticks.fontsize(20)
cb.set_label('Degree C',fontsize=14)
plt.show()

plt.savefig(fig_name+'.ps',dpi=100,bbox_inches="tight")
plt.savefig(fig_name+'.eps',dpi=400,bbox_inches="tight")
plt.savefig(fig_name+'.png',dpi=400,bbox_inches="tight")


