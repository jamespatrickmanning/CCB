# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 14:47:56 2018

@author: xiaojian

Modified by Felicia and JiM June 2019 to remove unused packages and add alternative basic matplotlim commands. 
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#HARDCODES
#time=['1991','1992','1993','1999','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
#num=[20, 30,2, 149,94,259,95,36,55,88,43,85,182,234,138,408,224,1241,513]# extracted from stranding data for J. Manning.xls
# the following comes from Bob Prescott in Feb 2019
time=range(1979,2019)
num=[12,22,22,6,6,33,19,17,39,10,37,45,19,31,44,34,178,14,57,46,323,49,96,201,92,37,53,91,39,89,204,232,152,413,204,1241,613,476,420,818] # from Bob Prescott email in Feb 2019

method='new' # method of plotting where 'old' method used "Pandas"

fig,axes=plt.subplots(1,1,figsize=(8,4))

if method=='old':
  df=pd.Series(np.array(num).T,index=np.array(time).T)
  df.plot(kind='bar',ax=axes,color='green')
axes.set_ylim([0,1400])

else:
  #alternatively using basic matplotlib commands
  plt.bar(time,num,color='navy')
  fig.autofmt_xdate() # this makes the date labels more readable in slanted font
  
axes.set_title('The number of turtles per year',fontsize=12)
plt.show()
plt.savefig('fig3.eps',format='eps',dpi=300,bbox_inches='tight')






