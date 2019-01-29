# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 14:47:56 2018

@author: xiaojian
"""

from mpl_toolkits.basemap import Basemap  

import numpy as np
import matplotlib.pyplot as plt
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
time=['1991','1992','1993','1999','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
num=[20, 30,2, 149,94,259,95,36,55,88,43,85,182,234,138,408,224,1241,513]# from stranding data for J. Manning.xls
fig,axes=plt.subplots(1,1,figsize=(8,4))

df=pd.Series(np.array(num).T,index=np.array(time).T)
df.plot(kind='bar',ax=axes,color='green')

axes.set_ylim([0,1400])
axes.set_title('The number of turtles per year',fontsize=12)
plt.savefig('fig3.eps',format='eps',dpi=300,bbox_inches='tight')






