# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:14:50 2018

@author: xiaojian
Modifications by JiM in Sept 2019 to:
- allow other start_options
- improve documentation
- 
"""

import datetime as dt
import pytz
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pytz import timezone
import numpy as np
import csv
from scipy import  interpolate
from matplotlib.dates import date2num,num2date
#from barycentric_polygonal_interpolation import get_drifter_track,get_fvcom,get_roms,calculate_SD,drifterhr
from barycentric_polygonal_interpolation import get_fvcom
######## Hard codes ##########
Model='30yr' # JiM changed from array to string
wind_get_type='FVCOM'
wind=0 
start_option='user_defined'# 'user_defined' # or 'box' or 'random'
days=4 # number of days to track
# Define start stop locations 
if start_option=='box': # as used in Liu et paper
	st_lat=[]
	st_lon=[]
	latc=np.linspace(41.8,42.0,10)
	lonc=np.linspace(-70.5,-70.2,10)
	for aa in np.arange(len(lonc)):
		for bb in np.arange(len(latc)):
			st_lat.append(latc[bb])
			st_lon.append(lonc[aa])
elif start_option=='user_defined':
	st_lat=[41.8572]#41.85784]#41.79346] # related to jeremeypt (3),sandyneck, and eastham landings
	st_lon=[-70.04724]#-70.46753]#-70.1198]
else: # random placement inside box
	num = 70
	st_lat = np.random.uniform(44.5,45,num)[:]
	st_lon = np.random.uniform(-66.8,-66,num)[:]
jia=14*0 # always zero
end_times=[]
start_time=[]
start_times=[dt.datetime(2014,11,29,19,50,0,0)]#,dt.datetime(2013,5,1,0,0,0,0),dt.datetime(2012,5,1,0,0,0,0),dt.datetime(2011,5,1,0,0,0,0),dt.datetime(2010,5,1,0,0,0,0),dt.datetime(2009,5,1,0,0,0,0),dt.datetime(2008,5,1,0,0,0,0),dt.datetime(2007,5,1,0,0,0,0)]
###############################################  END of HARDCODES  #########################################
for a in np.arange(len(start_times)):
    start_time.append(start_times[a]+timedelta(hours=jia*24))
m_ps =dict(lon=[],lat=[],time=[])
for a in np.arange(len(start_time)):
    print a
    end_time=start_time[a]+timedelta(hours=days*24)
    
    #i=Model[0] #why do this???
    GRIDS= ['GOM3','massbay','30yr']
    if Model in GRIDS:
        try:
            get_obj =  get_fvcom(Model)
            url_fvcom = get_obj.get_url(start_time[a],end_time)                
            b_points = get_obj.get_data(url_fvcom) # boundary points?
            model_points =dict(lon=[],lat=[],time=[]) # all point in the track of one start location
            for b in np.arange(len(st_lon)):
                print b
                modelpoints = dict(lon=[],lat=[],time=[]) # dictionary holding  one point for one of the 100 points
                modelpoints,windspeed= get_obj.get_track(st_lon[b],st_lat[b],0,start_time[a],wind,wind_get_type)
                model_points['lon'].append(modelpoints['lon'])
                model_points['lat'].append(modelpoints['lat'])  
                model_points['time'].append(modelpoints['time'])    
        except:
            print 'There is no model-point near the given-point'
            continue
    m_ps['lon'].append(model_points['lon'])
    m_ps['lat'].append(model_points['lat'])
    m_ps['time'].append(model_points['time'])
#np.save('m_ps'+str(start_time[0].year)+'-'+str(start_time[1].year),m_ps)# this 
np.save('particle_track_using_fvcom_'+str(start_time[0].month)+'_'+str(start_time[0].day)+'b_'+str(start_time[0].year),m_ps)# this 
