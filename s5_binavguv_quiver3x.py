#http://www.ngdc.noaa.gov/mgg/coast/
# coast line data extractor

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:27:09 2012

@author: vsheremet
"""
import numpy as np
#from pydap.client import open_url
import matplotlib.pyplot as plt
#from SeaHorseLib import *
#from datetime import *
#from scipy import interpolate
#import sys
#from SeaHorseTide import *
#import shutil
import matplotlib.mlab as mlab
import matplotlib.cm as cm


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
#            k=np.where((ix==iix) and (iy==iiy)) # wrong syntax
            k,=np.where((ix==iix) & (iy==iiy))
            zb_mean[iix-1,iiy-1]=np.mean(z[k])
            zb_median[iix-1,iiy-1]=np.median(z[k])
            zb_std[iix-1,iiy-1]=np.std(z[k])
            zb_num[iix-1,iiy-1]=len(z[k])
            
    return xb,yb,zb_mean,zb_median,zb_std,zb_num
"""
from netCDF4 import Dataset

# read in etopo5 topography/bathymetry.
url = 'http://ferret.pmel.noaa.gov/thredds/dodsC/data/PMEL/etopo5.nc'
etopodata = Dataset(url)

topoin = etopodata.variables['ROSE'][:]
lons = etopodata.variables['ETOPO05_X'][:]
lats = etopodata.variables['ETOPO05_Y'][:]
# shift data so lons go from -180 to 180 instead of 20 to 380.
topoin,lons = shiftgrid(180.,topoin,lons,start=False)
"""



"""
BATHY=np.genfromtxt('necscoast_noaa.dat',dtype=None,names=['coast_lon', 'coast_lat'])
coast_lon=BATHY['coast_lon']
coast_lat=BATHY['coast_lat']
"""

#BATHY=np.genfromtxt('coastlineNE.dat',names=['coast_lon', 'coast_lat'],dtype=None,comments='>')
#coast_lon=BATHY['coast_lon']
#coast_lat=BATHY['coast_lat']


# www.ngdc.noaa.gov
# world vector shoreline ascii
FNCL='necscoast_worldvec.dat'

CL=np.genfromtxt(FNCL,names=['lon','lat'])


FN='binned_drifter.npz'
#FN='binned_model.npz'
Z=np.load(FN) 
xb=Z['xb']
yb=Z['yb']
ub_mean=Z['ub_mean']
ub_median=Z['ub_median']
ub_std=Z['ub_std']
ub_num=Z['ub_num']
vb_mean=Z['vb_mean']
vb_median=Z['vb_median']
vb_std=Z['vb_std']
vb_num=Z['vb_num']
Z.close()

xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.03)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])
fig,axes=plt.subplots(2,2,figsize=(15,10))
#plt.figure()
plt.subplots_adjust(wspace=0.07,hspace=0.07)
ub = np.ma.array(ub_mean, mask=np.isnan(ub_mean))
vb = np.ma.array(vb_mean, mask=np.isnan(vb_mean))
Q=axes[0,0].quiver(xxb,yyb,ub.T,vb.T,scale=5.)
qk=axes[0,0].quiverkey(Q,0.1,0.45,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')

#plt.plot(coast_lon,coast_lat,'b.')
axes[0,0].plot(CL['lon'],CL['lat'])
axes[0,0].set_title('a')

axes[0,0].axis([-70.75,-69.8,41.5,42.23])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
#axes[0,0].xaxis.tick_top() 
axes[0,0].set_xticklabels([])

#plt.show()
###################################################################################33
#FN='binned_drifter01.npz'
FN='binned_model.npz'
Z1=np.load(FN) 
xb1=Z1['xb']
yb1=Z1['yb']
ub_mean1=Z1['ub_mean']
ub_median1=Z1['ub_median']
ub_std1=Z1['ub_std']
ub_num1=Z1['ub_num']
vb_mean1=Z1['vb_mean']
vb_median1=Z1['vb_median']
vb_std1=Z1['vb_std']
vb_num1=Z1['vb_num']
Z1.close()

#cmap = matplotlib.cm.jet
#cmap.set_bad('w',1.)
xxb,yyb = np.meshgrid(xb, yb)
cc=np.arange(-1.5,1.500001,0.03)
#cc=np.array([-1., -.75, -.5, -.25, -0.2, -.15, -.1, -0.05, 0., 0.05, .1, .15, .2, .25, .5, .75, 1.])
#fig,axes=plt.subplots(3,2,figsize=(7,5))
#plt.figure()
ub1 = np.ma.array(ub_mean1, mask=np.isnan(ub_mean1))
vb1 = np.ma.array(vb_mean1, mask=np.isnan(vb_mean1))
Q=axes[0,1].quiver(xxb,yyb,ub1.T,vb1.T,scale=5.)
UB1T=ub1.T
VB1T=vb1.T
qk=axes[0,1].quiverkey(Q,0.1,0.45,0.5, r'$0.1m/s$', fontproperties={'weight': 'bold'})

#plt.xlabel('''Mean current derived from historical drifter data (1-20m)''')
#axes[1,0].set_xticklabels([])
axes[1,0].set_title('c')
axes[0,1].set_title('b')
#plt.plot(coast_lon,coast_lat,'b.')
axes[0,1].plot(CL['lon'],CL['lat'])
axes[0,1].axis([-70.75,-69.8,41.5,42.23])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
#axes[1,0].xaxis.tick_top() 

for a in np.arange(len(xxb[0])):
    for b in np.arange(len(yyb)):
        if -70.75<xxb[0][a]<-69.8 and 41.5<yyb[b][0]<42.23 and ub_num[a][b]!=0:
            #plt.text(xxb[0][a],yyb[b][0],ubn[a][b],fontsize='smaller')
            axes[1,0].text(xxb[0][a]-0.03,yyb[b][0]-0.03,ub_num[a][b],fontsize=10)
            #axes[1,1].scatter(xxb[0][a],yyb[b][0],s=ubn[a][b]/float(100),color='red',marker='o')
axes[1,0].plot(CL['lon'],CL['lat'])
axes[1,0].axis([-70.75,-69.8,41.5,42.23])
#axes[0,1].xaxis.tick_top() 
axes[0,1].set_yticklabels([])
axes[0,1].set_xticklabels([])
###########################################
data = np.genfromtxt('sea.csv',dtype=None,names=['x','y','h'],delimiter=',')    
x=[]
y=[]
h=[]
x=data['x']
y=data['y']
h=data['h']
xi = np.arange(-70.75,-69.8,0.03)
yi = np.arange(41.5,42.23,0.03)
xb,yb,hb_mean,hb_median,hb_std,hb_num = sh_bindata(x, y, h, xi, yi)
xxxb,yyyb = np.meshgrid(xb, yb)
for a in np.arange(len(hb_mean)):
    for b in np.arange(len(hb_mean[0])):
        if hb_mean[a][b]>100000:
            hb_mean[a][b]=0
CS=axes[1,1].contour(xxxb, yyyb, -abs(hb_mean.T),colors=('r', 'green', 'blue', (1, 1, 0), '#afeeee', '0.5'),levels=[-100,-60,-30,-20,-10])
axes[1,1].clabel(CS, inline=1, fontsize=12,fmt='%4.0f')
axes[1,1].plot(CL['lon'],CL['lat'])
axes[1,1].axis([-70.75,-69.8,41.5,42.23])
#axes.xaxis.tick_top() 
#axes[1,1].set_xticklabels([])
axes[1,1].set_yticklabels([])
axes[1,1].set_title('d')

#plt.title('binned_drifter_num')
plt.savefig('drifter_model',dpi=400)

#############################################################################################

plt.figure()
#plt.
uumodel=np.load('uumodel.npy')
vvmodel=np.load('vvmodel.npy')

uudrifter=np.load('uudrifter.npy')
vvdrifter=np.load('vvdrifter.npy')

x=np.load('xx.npy')
y=np.load('yy.npy')

xi = np.arange(-70.75,-69.80000,0.05)
yi = np.arange(41.5,42.250000,0.05)

dr=dict(lon=[],lat=[],uudiff=[],vvdiff=[])

'''
# for dr1.npy
uudiff=np.sqrt((uudrifter*uudrifter+vvdrifter*vvdrifter))-np.sqrt((uumodel*uumodel+vvmodel*vvmodel))
vvdiff=uudrifter
'''
# for dr.npy
uudiff=uudrifter-uumodel#(uudrifter*uudrifter+vvdrifter*vvdrifter))-np.sqrt((uumodel*uumodel+vvmodel*vvmodel)
vvdiff=vvdrifter-vvmodel

for a in np.arange(len(x)):
    print 'a',a
    if  x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[0] and x[a]<xi[1] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[0]+xi[1])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    ######################################################################################
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[1] and x[a]<xi[2] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[1]+xi[2])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    ######################################################################
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[2] and x[a]<xi[3] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[2]+xi[3])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #########################################################
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[3] and x[a]<xi[4] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[3]+xi[4])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    #############################################
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[4] and x[a]<xi[5] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[4]+xi[5])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ##################################################################
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[5] and x[a]<xi[6] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[5]+xi[6])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ##########################################################3
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[6] and x[a]<xi[7] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[6]+xi[7])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ####################################################
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[7] and x[a]<xi[8] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[7]+xi[8])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
   
    ######################################################
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[8] and x[a]<xi[9] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[8]+xi[9])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ###################################################
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[9] and x[a]<xi[10] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[9]+xi[10])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ######################################################################
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[10] and x[a]<xi[11] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[10]+xi[11])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ##########################################################
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[11] and x[a]<xi[12] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[11]+xi[12])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ######################################################################
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[12] and x[a]<xi[13] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[12]+xi[13])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    #########################################################
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[13] and x[a]<xi[14] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[13]+xi[14])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    #############################################
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[14] and x[a]<xi[15] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[14]+xi[15])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ########################################################
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[15] and x[a]<xi[16] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[15]+xi[16])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ##########################################################3
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[16] and x[a]<xi[17] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[16]+xi[17])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ####################################################
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[17] and x[a]<xi[18] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[17]+xi[18])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
    ######################################################
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[0] and y[a]<yi[1]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[0]+yi[1])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    #yys=yys+1
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[1] and y[a]<yi[2]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[1]+yi[2])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[2] and y[a]<yi[3]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[2]+yi[3])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[3] and y[a]<yi[4]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[3]+yi[4])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[4] and y[a]<yi[5]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[4]+yi[5])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[5] and y[a]<yi[6]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[5]+yi[6])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[6] and y[a]<yi[7]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[6]+yi[7])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[7] and y[a]<yi[8]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[7]+yi[8])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[8] and y[a]<yi[9]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[8]+yi[9])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[9] and y[a]<yi[10]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[9]+yi[10])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[10] and y[a]<yi[11]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[10]+yi[11])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[11] and y[a]<yi[12]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[11]+yi[12])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[12] and y[a]<yi[13]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[12]+yi[13])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    if x[a]>=xi[18] and x[a]<xi[19] and y[a]>=yi[13] and y[a]<yi[14]:
        dr['lon'].append((xi[18]+xi[19])/2.0)
        dr['lat'].append((yi[13]+yi[14])/2.0)
        dr['uudiff'].append(uudiff[a])
        dr['vvdiff'].append(vvdiff[a])
    
np.save('dr',dr)