# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 09:48:58 2018

@author: huimin
Modified by JiM in Feb 2019
"""

import numpy as np
import matplotlib.pyplot as plt

date='Nov_18_25_2014'
#filepath='/home/hxu/huiminzou/from xiaojian/massbay/files_20141118-25/' #former location of some input files
filepath=''
m26=np.load('m_psFVCOM20141118_7days.npy')#'m_ps2011-2010_630.npy'
p=m26.tolist()
FN='necscoast_worldvec.dat'
CL=np.genfromtxt(FN,names=['lon','lat'])
#fig, ax=plt.subplots(1,1,figsize=(12,8))#sharex=True,sharey=True,dpi=800,figsize=(15,15))
fig=plt.figure(figsize=(17,7))
plt.subplots_adjust(wspace=0.08,hspace=0.1)

ax1=fig.add_subplot(1,2,1)  
ax1.plot(CL['lon'],CL['lat'],'b-')

for a in np.arange(len(p['lon'][0])):
    ax1.scatter(p['lon'][0][a][0],p['lat'][0][a][0],color='green')
    if len(p['lon'][0][a])>=361:
        
        ax1.scatter(p['lon'][0][a][360],p['lat'][0][a][360],color='red')
        ax1.plot([p['lon'][0][a][0],p['lon'][0][a][360]],[p['lat'][0][a][0],p['lat'][0][a][360]],'y-')#,linewidth=0.5)
    else:
        ax1.scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],color='red')
        ax1.plot(p['lon'][0][a][0:],p['lat'][0][a][0:],'y-')#,linewidth=0.5)

ax1.scatter(p['lon'][0][a][0],p['lat'][0][a][0],label='start',color='green')
ax1.scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],label='end',color='red')
 
ax1.legend(loc='upper right',scatterpoints=1) 
ax1.set_xlim([-70.7,-69.9])
ax1.set_ylim([41.5,42.1]) 
#ax1.xaxis.tick_top() 
ax1.set_title('GOM3',fontsize=16)
for tick in ax1.xaxis.get_major_ticks():  
    tick.label1.set_fontsize(13) 
for tick in ax1.yaxis.get_major_ticks():  
    tick.label1.set_fontsize(13) 
##################draw massbay##################
ax2=fig.add_subplot(1,2,2)
ax2.plot(CL['lon'],CL['lat'],'b-')
    
lons=np.load(filepath+'lonmassbay.npy')
lats=np.load(filepath+'latmassbay.npy')
times=np.load(filepath+'timemassbay.npy')

for i in range(len(lons)):
    ax2.scatter(lons[i][0],lats[i][0],color='green')
    ax2.scatter(lons[i][-2],lats[i][-2],color='red')
    ax2.plot(lons[i][:],lats[i][:],'y-')

ax2.scatter(lons[i][0],lats[i][0],color='green',label='start')
ax2.scatter(lons[i][-2],lats[i][-2],color='red',label='end')   
ax2.set_xlim([-70.7,-69.9])
ax2.set_ylim([41.5,42.1])
ax2.set_yticklabels([])
ax2.set_title('MassBay',fontsize=16)
for tick in ax2.xaxis.get_major_ticks():  
    tick.label1.set_fontsize(13) 
    
#plt.savefig('GOM3&mASSBAY'+'_'+date+'',dpi=100,bbox_inches="tight")
plt.savefig('fig19.eps',format='eps',dpi=400,bbox_inches='tight')
plt.show()
