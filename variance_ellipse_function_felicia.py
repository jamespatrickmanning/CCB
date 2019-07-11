#!/usr/bin/python
"""
Created on Fri Jul 13 11:05:54 2018

@author: xiaojian
Modifications by JiM in Aug 2018 to add mean currents
Note: Xiaojian's original code included wind in first panel
This is a function to underlay ellipses on mean vectors

Modified by Felicia June 2019 to function with Python 3 and clean up unused strings
Flowcharted by JiM in July 2019 as "variance_ellipse.drawio"
"""
############ BASEMAP installation options ###############
#for Python <3
#from mpl_toolkits.basemap import Basemap 
#for Python 3
#conda install -c conda-forge basemap 
#conda install -c conda-forge basemap-data-hires

###################### PACKAGES #########################
from matplotlib.patches import Ellipse #, Circle # removing the "Circle" from this registered it as being "used"
import matplotlib.pyplot as plt
import numpy as np
import math

####################### FUNCTIONS #######################
def variance_ellipses_under_means(ax,gbox,legend_pos,legend_size,max_ellipse_to_ignorema):
  # HARDCODE examples
  # gbox=[-70.75,-69.8,41.5,42.25]
  # legend_pos=[-69.9,41.55]
  # legend_size=0.05
  # max_ellipse_to_ignore=0.5 #m/s2 where Nantucket shoals tides are near 0.5 

  # load the results of running "s2.py" which extracts MassBay velocities for particular time period
  print ('loading modeled velocity for long time ')
  lo=np.load('lombx.npy')
  la=np.load('lambx.npy')
  us1=np.load('umb18_23.npy')
  vs1=np.load('vmb18_23.npy')
  ff=1.0
  x=lo
  y=la
  xi = np.arange(gbox[0],gbox[1],0.05)
  yi = np.arange(gbox[2],gbox[3],0.05)
  print ('creating a dictionary of these values')
  dr=dict(lon=[],lat=[],us=[],vs=[]) # set up a dictionary called "dr"
  ########################################################################
  for a in np.arange(len(x)):
    #print 'a',a
    for b in np.arange(len(xi)-1):
        for c in np.arange(len(yi)-1):
            if x[a]>=xi[b] and x[a]<xi[b+1] and y[a]>=yi[c] and y[a]<yi[c+1]:
                d='%s'%a+'%s'%b # not sure what this is for.... not used (FMP)
                
                dr['lon'].append((xi[b]+xi[b+1])/2.0)
                dr['lat'].append((yi[c]+yi[c+1])/2.0)
                dr['us'].append(us1[a])
                dr['vs'].append(vs1[a])
                
  ########################################################################
  lonlat=[] #combination of lat/lon
  ud=[]
  vd=[]
  #####################################################################
  print ('finding the lon lat combinations of observations in each bin')
  for a in np.arange(len(dr['lon'])):
    if "%s+%s"%("%.4f" % dr['lon'][a],"%.4f" % dr['lat'][a]) not in lonlat:
        
        #lonlat.append("%s+%s"%(dr['lon'][a],dr['lat'][a]))
        lonlat.append("%s+%s"%("%.4f" % dr['lon'][a],"%.4f" % dr['lat'][a]))# JiM change
        #lat.append(dr['lat'][a])
  for a in np.arange(len(lonlat)):
    u=[]
    v=[]    
    for b in np.arange(len(dr['lon'])):
        if "%s+%s"%("%.4f" % dr['lon'][b],"%.4f" % dr['lat'][b])==lonlat[a]:    
            for c in np.arange(len(dr['us'][b])):
                u.append(dr['us'][b][c])
                v.append(dr['vs'][b][c])
    ud.append(u)
    vd.append(v)
  ####################################################
  #fig = plt.figure(figsize=(15,12))
  #ax = fig.add_subplot(1,1,1)
  wid=[]
  heigth=[]
  ####################################################
  print ('calculating ellipses')
  for a in np.arange(len(ud)):
    xie=np.cov(ud[a],vd[a])
    qxx=xie[0][0]
    qxy=xie[0][1]
    qyy=xie[1][1]
    st_2=math.atan(2*qxy/(qxx-qyy))
    st=st_2/2
    rx=qxx*math.cos(st)*math.cos(st)+qyy*math.sin(st)*math.sin(st)+qxy*math.sin(st_2)
    ry=qxx*math.sin(st)*math.sin(st)+qyy*math.cos(st)*math.cos(st)-qxy*math.sin(st_2)
    dirr=[]
    if qxy>=0:
        #print 'max=1,3'
        dirr.append(1)
        dirr.append(3)
    else:
        #print 'max=2,4'
        dirr.append(2)
        dirr.append(4)
    if rx>=ry:
        ma=rx
        mi=ry
    else:
        ma=ry
        mi=rx
    f=[st,st+math.pi/2,st+math.pi,st+math.pi*3/2]
    f=0 # what is "f" and why are we setting it to zero?
    if st_2>=0:
        f=1
    if st_2<0:
        f=4
    dr=dict(d=[],df=[],x=[],xf=[])
    p=[]
    if f in dirr:
        dr['d'].append(ma)
        dr['df'].append(st)
        dr['x'].append(mi)
        dr['xf'].append(st+math.pi/2)
    else:
        p.append(1)
        dr['d'].append(ma)
        dr['df'].append(st+math.pi/2)
        dr['x'].append(mi)
        dr['xf'].append(st)
    if p!=[]:
        #print 1
        #if  dr['d'][0]/ff>0.1 or dr['x'][0]/ff>0.1:#066401115712580779:
        
        if  dr['d'][0]/ff>max_ellipse_to_ignore or dr['x'][0]/ff>max_ellipse_to_ignore:#066401115712580779:
            pass
        else:
            ell1 = Ellipse(xy = (float(lonlat[a][0:7]), float(lonlat[a][8:14])), width = dr['x'][0]/ff, height = dr['d'][0]/ff, angle = dr['xf'][0]/(math.pi/2/180), facecolor= 'red',edgecolor='none', alpha=0.2)
            #print 'width',dr['x'][0]/ff
            wid.append(dr['d'][0]/ff)
            heigth.append(dr['x'][0]/ff)
    else:
        if  dr['d'][0]/ff>max_ellipse_to_ignore or dr['x'][0]/ff>max_ellipse_to_ignore: # Limiting big ellipses?
            pass
        else:
            ell1 = Ellipse(xy = (float(lonlat[a][0:7]), float(lonlat[a][8:14])), width = dr['d'][0]/ff, height = dr['x'][0]/ff, angle = dr['df'][0]/(math.pi/2/180), facecolor= 'red', edgecolor='none', alpha=0.2)
    #try:
    ax.add_patch(ell1)
    #except:
    #    continue
  # plot legend
  p=legend_pos
  s=legend_size
  ax.plot([p[0],p[0]+s],[p[1],p[1]],color='red')
  ax.plot([p[0]+s,p[0]+s],[p[1],p[1]+0.01],color='red')
  ax.plot([p[0],p[0]],[p[1],p[1]+0.01],color='red')
  ax.text(p[0],p[1]+0.03,'0.05 (m/$\mathregular{s)^{2}}$',color='red')
  plt.xlim(gbox[0],gbox[1])
  plt.ylim(gbox[2],gbox[3])
  return ff
#plt.savefig('current_and_variance',dpi=300,bbox_inches='tight')
#plt.show()


