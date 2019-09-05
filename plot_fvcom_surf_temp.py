
"""
Created on 5 Sept 2019
plot horizontal slice of FVCOM
@author: JiM
"""
# routine to plot FVCOM surface temps
# taken from Rich's blog at
# http://rsignell-usgs.github.io/blog/blog/2014/01/08/fvcom/

from pylab import *
import matplotlib.tri as Tri
import netCDF4
from datetime import datetime as dt


############################
# HARDCODES
mode='Hindcasts'    # or Hindcasts
run='OCEAN_MASSBAY' # only needed in Forecasts case
dtime=dt(2014,11,4,1,0,0)
area='inside_CCBAY'
layer='surface'     # or bottom
levels=arange(10,14,0.25)

def getgbox(area):
  # gets geographic box based on area
  if area=='SNE':
    gbox=[-70.,-64.,39.,42.] # for SNE
  elif area=='GBANK':
    gbox=[-70.,-64.,39.,42.] # for SNE
  elif area=='GS':           
    gbox=[-71.,-63.,37.,42.] # for Gulf Stream
  elif area=='NorthShore':
    gbox=[-71.,-70.,42.,43.] # for north shore
  elif area=='CCBAY':
    gbox=[-70.75,-69.8,41.5,42.23] # CCBAY
  elif area=='inside_CCBAY':
    gbox=[-70.75,-70.,41.7,42.23] # CCBAY  
  return gbox

## DAP Data URL
if mode=='Forecasts':
	url = 'http://www.smast.umassd.edu:8080/thredds/dodsC/FVCOM/NECOFS/Forecasts/NECOFS_FVCOM_'+run+'_FORECAST.nc'
else:
	url='http://www.smast.umassd.edu:8080/thredds/dodsC/fvcom/hindcasts/30yr_gom3'
	
nc = netCDF4.Dataset(url).variables

#start = dt.datetime.utcnow() + dt.timedelta(hours=18)
time_var = nc['time']
itime = netCDF4.date2index(dtime,time_var,select='nearest')

# Get lon,lat coordinates for nodes (depth)
lat = nc['lat'][:]
lon = nc['lon'][:]
# Get lon,lat coordinates for cell centers (depth)
latc = nc['latc'][:]
lonc = nc['lonc'][:]
# Get Connectivity array
nv = nc['nv'][:].T - 1 
# Get depth
#h = nc['h'][:]  # depth

dtime = netCDF4.num2date(time_var[itime],time_var.units)
daystr = dtime.strftime('%Y-%b-%d %H:%M')
#print(daystr)

tri = Tri.Triangulation(lon,lat, triangles=nv)
if layer=='surface':
	ilayer = 0 #surface
else:
	ilayer =-1 #bottom
sst = nc['temp'][itime, ilayer, :]

# define contour levels if blank
if len(levels)==0:
	levels=arange(int(min(sst)),int(max(sst)+1),1)
ax = getgbox(area)# returns a geographic box like [-70.7, -70.6, 41.48, 41.55]
#maxvel = 1.0
#subsample = 2

# find velocity points in bounding box
ind = argwhere((lonc >= ax[0]) & (lonc <= ax[1]) & (latc >= ax[2]) & (latc <= ax[3]))

figure(figsize=(12,8))
subplot(111,aspect=(1.0/cos(mean(lat)*pi/180.0)))
#tricontourf(tri, sst,levels=levels,shading='faceted',cmap=plt.cm.gist_earth)
tricontourf(tri, sst,levels=levels,shading='faceted',cmap=plt.cm.jet)
axis(ax)
gca().patch.set_facecolor('0.5')
cbar=colorbar()
cbar.set_label('SST (degC)', rotation=-90)
#Q = quiver(lonc[idv],latc[idv],u[idv],v[idv],scale=20)
#maxstr='%3.1f m/s' % maxvel
#qk = quiverkey(Q,0.92,0.08,maxvel,maxstr,labelpos='W')
title('FVCOM '+layer+' %s UTC' % (daystr[0:12])+' using '+mode)
savefig('/net/pubweb_html/epd/ocean/MainPage/turtle/ccbay/FVCOM_sst_'+daystr[0:12]+'+.png')



