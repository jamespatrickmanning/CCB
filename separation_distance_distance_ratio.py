# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:37:50 2018

@author: huimin
separation distance and distance ratio
"""

import numpy as np
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,2,figsize=(10,4))
plt.subplots_adjust(wspace=0.1,hspace=0.1)

drifter_list='cope1.csv'

drifters = np.genfromtxt(drifter_list,dtype=None,names=['ids','lon','lat','s','d'],delimiter=',',skip_header=1)
 
num=[]
x=[]
for b in np.arange(1,round(max(drifters['s']))+1):

    aa=0
    x.append(b-1)
    x.append(b)
    for a in np.arange(len(drifters['s'])):
        if drifters['s'][a]>=b-1 and drifters['s'][a]<b:
            aa=aa+1
    num.append(aa)
    num.append(aa)
num.append(0)
x.append(b)

axes[0].plot(x,num,'b-')
axes[0].set_xlabel('separation distance(km)',fontsize=13)
axes[0].set_ylabel('number',fontsize=13)
axes[0].set_ylim(0,30)


num1=[]
x1=[]
for b in np.arange(0.01,round(max(drifters['d'])*100)/float(100),0.01):

    aa=0
    x1.append(b-0.01)
    x1.append(b)
    for a in np.arange(len(drifters['d'])):
        if drifters['d'][a]>=b-0.01 and drifters['d'][a]<b:
            aa=aa+1
            
    num1.append(aa)
    num1.append(aa)
num1.append(0)
x1.append(b)

axes[1].plot(x1,num1,'b-')
axes[1].set_xlabel('distance ratio',fontsize=13)
axes[1].set_ylim(0,30)
axes[1].set_yticklabels([])
plt.savefig('separation_distance&distance_ratio',dpi=200,bbox_inches = "tight")
plt.savefig('separation_distance&distance_ratio.ps',dpi=200,bbox_inches = "tight")
plt.savefig('Figure7.eps',format='eps',dpi=400,bbox_inches='tight')
plt.show()
