# -*- coding: utf-8 -*-
"""
Xiaojian's code modified by JiM in June 2019
Given time and geographic box, it creates a series of panels
Note: to make single panel set "numframes=1".

assumes:
  -you have access to the coastline file in '/net/data5/jmanning/bathy/necscoast_worldvec.dat'
  -you have access to the bathymetry contours in '/net/data5/jmanning/bathy/*bty' if you want to have them overlaid
  -you already know the name of the sst file you want to access in the MARACOOS/UDEL collection by viewing https://marine.rutgers.edu/cool/sat_data/?bm=5&bd=3&by=2013&sort=date&em=6&ed=13&ey=2013&region=gulfstream&product=sst&nothumbs=0&okb.x=41&okb.y=28
  -you have a working version of LINUX "convert" program that can subsequently make the gif given the png images created with "pltsst"
  -you have either pydap or netCDF4 modules installed

JiM modification 25 June 2019 to use netCDF4 to read images didn't work
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import sys
from pydap.client import open_url
import netCDF4
import time
import pltbty
from pandas import read_csv

#  HARDCODES #############
temprange=np.arange(17,29,0.25)# summer
#temprange=np.arange(6,16,0.25)# fall
#temprange=np.arange(10,14,0.25)# Fall stranding
#colorticks=np.linspace(6,16,11)# fall
#colorticks=np.linspace(10,14,17)# fall stranding
colorticks=np.linspace(17,29,13)# summer where the first two numbers as the same as temprange and the last is the number of labels
#time_wanted=[dt.datetime(2014,11,3,23,59,59,0),dt.datetime(2014,12,19,23,59,59,0),dt.datetime(2014,12,26,23,59,59,0)]# these are datetimes associated with clear SST imagery
#time_wanted=dt.datetime(2014,11,4,1,0,0) # cape cod stranding case
time_wanted=dt.datetime(2019,8,28,0,0,0) # Sep 2019 gs impingement experiment
#time_wanted=dt.datetime(2013,4,18,0,0,0)
data='realtime'#maracoos_modis' # or 'realtime', 'maracoos',  'udel' , 'maracoos_modis' where:
   # realtime is only available for the past week
   # maracoos is apparently available back to 2013 (minus this past year)
numday_agg=7 #number of days of aggregation 1,3,7 for maracoos & realtime and 1,3,8 for maracoos_modis
hours_per_frame=24 # number of hours between each frame where it looks like 3 hours is the minimum
numframes=10   #number of frames to step through
numpanels=1 # if numpanels=1, it only plots the first in list
area='GS' # area of interest (see function below)
drifter_file='/net/pubweb_html/drifter/drift_staceyNSF_2019_1.csv'#ma_2018_1
drifter=198390691#193420701
legend_size=0.05
FNCL='/net/data5/jmanning/bathy/necscoast_worldvec.dat'
method='pydap'# 'pydap' # netCDF4 method still needs work
new=0 #number to start the images at
#########################
#Functions
def getURL(url, outFile):
    response = urllib.urlretrieve(myURL, outFile)
    return(response)
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

def getssturl(data):
  # gets OPeNDAP url based on dataset
  if data=='maracoos':
    url='http://tds.maracoos.org/thredds/dodsC/AVHRR/'+str(time_wanted.year)+'/'+str(numday_agg)+'Agg' # ARCHIVE
  elif data=='realtime':
    url='http://tds.maracoos.org/thredds/dodsC/AVHRR'+str(numday_agg)+'.nc' # last week
  elif data=='maracoos_modis':
    end_d=time_wanted+dt.timedelta(days=numday_agg-1)
    url='http://tds.maracoos.org/thredds/dodsC/MODIS/'+str(time_wanted.year)+'/'+str(numday_agg)+'/aqua.'+str(time_wanted.year)+str(time_wanted.timetuple().tm_yday).zfill(3)+'.'+str(time_wanted.month).zfill(2)+str(time_wanted.day).zfill(2)+'-'+str(end_d.year)+str(end_d.timetuple().tm_yday).zfill(3)+'.'+str(end_d.month).zfill(2)+str(end_d.day).zfill(2)+'.D.L3.modis.NAT.v09.1000m.nc4' # another Archive
  elif data=='udel':
    #url=['http://basin.ceoe.udel.edu/thredds/dodsC/ModisAqua/2014/aqua.2014307.1103.235959.D.L3.modis.NAT.v09.1000m.nc4','http://basin.ceoe.udel.edu/thredds/dodsC/ModisAqua/2014/aqua.2014323.1119.235959.D.L3.modis.NAT.v09.1000m.nc4','http://basin.ceoe.udel.edu/thredds/dodsC/ModisAqua/2014/aqua.2014360.1226.235959.D.L3.modis.NAT.v09.1000m.nc4']
    url='http://basin.ceoe.udel.edu/thredds/dodsC/ModisAqua/'+str(time_wanted.year)+'/aqua.'+str(time_wanted.year)+str(time_wanted.timetuple().tm_yday).zfill(3)+'.'+str(time_wanted.month).zfill(2)+str(time_wanted.day).zfill(2)+'.235959.D.L3.modis.NAT.v09.1000m.nc4'
    method='netCDF4'
  return url

#############################
# Main program
gbox=getgbox(area) # gets geographic box w/lat lon corners
url=getssturl(data) # gets the url of sst imagery
if len(drifter_file)>0: # if there is a drifter file you wan to overlay
    dd=read_csv(drifter_file)
    dd=dd[dd['ID']==drifter]# select certain drifter
    dd=dd.drop_duplicates()
    d_datet=[] # create a date time based on ID
    yr=2000+int(str(drifter)[0:2])# based on 1st 2 digits of id
    for k in range(len(dd)):
       d1=dt.datetime(yr,dd['MTH'].values[k],dd['DAY'].values[k],dd['HR_GMT'].values[k],dd['MIN'].values[k],0)
       if (k>0):
         if d1.timetuple().tm_yday<d_datet[k-1].timetuple().tm_yday: #indication of strattling new year
            yr=yr+1
       d_datet.append(dt.datetime(yr,dd['MTH'].values[k],dd['DAY'].values[k],dd['HR_GMT'].values[k],dd['MIN'].values[k],0).replace(tzinfo=None))    
    dd['d_datet']=d_datet
for j in range(numframes):
  CL=np.genfromtxt(FNCL,names=['lon','lat'])# load some coastline
  fig,axes=plt.subplots(numpanels,1,figsize=(15,10)) #setup a plot frame
  plt.plot(CL['lon'],CL['lat'])#plot the coastline
  plt.axis(gbox)# confine the box to user-specified "gbox" area

  latsize=[gbox[2],gbox[3]]
  lonsize=[gbox[0],gbox[1]]
  for i in [numpanels-1]:
    if method=='pydap':
      dataset=open_url(url)
    else: # use netCDF4
      dataset=netCDF4.Dataset(url)
    times=list(dataset['time'])  
    second=time.mktime(time_wanted.timetuple())
    if (second<times[0]-60*60*24.) and (second>times[-1]+60*60*24.): # if the sat times are within one day of time_wanted, that's good (Note: changed "or" to "and" 7/3019)
      print 'data not available for this time'
      break
    index=int(round(np.interp(second,times,range(len(times)))))
    if (data=='maracoos') or (data=='realtime'):
      url1=url+'?lat[0:1:3660],lon[0:1:4499],'+'mcsst['+str(index)+':1:'+str(index)+'][0:1:0][0:1:0]'+',time['+str(index)+':1:'+str(index)+']'
    else:
      url1=url+'?lat[0:1:4499],lon[0:1:4999],'+'sst['+str(index)+':1:'+str(index)+'][0:1:4499][0:1:4999]'+',time['+str(index)+':1:'+str(index)+']'
    try:
        print url1
        if method=='pydap':
          dataset1=open_url(url1) # old method
        else:
          dataset1=netCDF4.Dataset(url1)
    except:
        print "please check your url!"
        sys.exit(0)   
    if (data!='maracoos') and (data!='realtime') and (data!='udel'):
      sst=dataset1['sst'].sst
    else:
      if method=='pydap':
        sst=dataset1['mcsst'].mcsst
        lat=dataset1['lat']
        lon=dataset1['lon']
      else:
        sst=dataset1['sst']#.compressed() # makes it not a masked array
        #sst=sst[sst.mask == False]
        lat=dataset1['lat'][:]
        lon=dataset1['lon'][:]

    # find the index for the gbox
    index_lon11=int(round(np.interp(gbox[0],list(lon),range(len(list(lon))))))
    index_lon12=int(round(np.interp(gbox[1],list(lon),range(len(list(lon))))))
    index_lat11=int(round(np.interp(gbox[2],list(lat),range(len(list(lat))))))
    index_lat12=int(round(np.interp(gbox[3],list(lat),range(len(list(lat))))))
    # get part of the sst
    sst_part=sst[index,index_lat11:index_lat12,index_lon11:index_lon12]#.compressed()# added .compressed for udel case 7/25/19
    sst_part[(sst_part==-999)]=np.NaN # if sst_part=-999, convert to NaN
    X1,Y1=np.meshgrid(lon[index_lon11:index_lon12],lat[index_lat11:index_lat12])
    if i==0: #upper left
        #conf=axes[0,0].contourf(X1,Y1,sst_part[0],temprange,zorder=0)
        conf=plt.contourf(X1,Y1,sst_part[0],temprange,zorder=0)
    elif i==1: #lower left
        conf=axes[1,0].contourf(X1,Y1,sst_part[0],temprange,zorder=0)
    else: #i==2
        conf=axes[1,1].contourf(X1,Y1,sst_part[0],temprange,zorder=0)
  plt.title('{:%Y-%m-%d }'.format(time_wanted)+' '+str(numday_agg)+' day aggregate from '+data)
  pltbty.pltbty() # function to plot 60 and 100m isibaths on NE Shelf
  if len(drifter_file)>0:
    dnow=dd[dd['d_datet']<=time_wanted]#+dt.timedelta(days=j)]
    plt.plot(dnow['LON'],dnow['LAT'],linewidth=3)
  fig.subplots_adjust(right=0.83,hspace=0.1,wspace=0.1)
  cbar_ax=fig.add_axes([0.85,0.15,0.015,0.7])#[left,bottom,right,top]
  cb=fig.colorbar(conf,cax=cbar_ax)
  cb.set_ticks(colorticks)
  cb.ax.tick_params(labelsize=12)
  #cb.set_ticks.fontsize(20)
  cb.set_label('Degree C',fontsize=14)

  plt.show()
  plt.savefig('/net/home3/ocn/jmanning/sst/SST_'+str(j+new).zfill(2)+'.png',dpi=100,bbox_inches="tight")
  #plt.close('all')
  time_wanted=time_wanted+dt.timedelta(hours=hours_per_frame) # add one day and go to the next
#on the NOVA machine: convert -delay 10 -loop 0 SST*.png /pubweb_html/drifter/sne_jul2019.gif

