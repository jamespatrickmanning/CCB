# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 23:26:47 2017

@author: xiaojian
Modified by Felicia July 2019: cleared unused strings and updated for Python 3
"""

import numpy as np
import matplotlib.pyplot as plt

windv2012=np.load('2012windv.npy')
numv2012=np.load('2012numv.npy')
xxv2012=np.load('2012xxv.npy')
yyv2012=np.load('2012yyv.npy')

windu2012=np.load('2012windu.npy')
numu2012=np.load('2012numu.npy')
xxu2012=np.load('2012xxu.npy')
yyu2012=np.load('2012yyu.npy')

windv2013=np.load('2013windv.npy')
numv2013=np.load('2013numv.npy')
xxv2013=np.load('2013xxv.npy')
yyv2013=np.load('2013yyv.npy')

windu2013=np.load('2013windu.npy')
numu2013=np.load('2013numu.npy')
xxu2013=np.load('2013xxu.npy')
yyu2013=np.load('2013yyu.npy')

windv2014=np.load('2014windv.npy')
numv2014=np.load('2014numv.npy')
xxv2014=np.load('2014xxv.npy')
yyv2014=np.load('2014yyv.npy')

windu2014=np.load('2014windu.npy')
numu2014=np.load('2014numu.npy')
xxu2014=np.load('2014xxu.npy')
yyu2014=np.load('2014yyu.npy')

rows=4
cols=2
fig,axes=plt.subplots(rows,cols,figsize=(14,10.5))
plt.subplots_adjust(wspace=0.2,hspace=0.2)
xlim0=(-21,100)
xlim1=(-60,10)
ylim=(-200,460)
axes[0,0].scatter(windu2012,numu2012)
axes[0,1].scatter(windv2012,numv2012)
axes[1,0].scatter(windu2013,numu2013)
axes[1,1].scatter(windv2013,numv2013)

axes[0,0].plot(xxu2012,yyu2012)
axes[0,1].plot(xxv2012,yyv2012)
axes[1,0].plot(xxu2013,yyu2013)
axes[1,1].plot(xxv2013,yyv2013)

axes[2,0].scatter(windu2014,numu2014)
axes[2,1].scatter(windv2014,numv2014)


axes[2,0].plot(xxu2014,yyu2014)
axes[2,1].plot(xxv2014,yyv2014)


axes[0,0].text(60,300,'2012',fontsize=15)
axes[0,1].text(-20,300,'2012',fontsize=15)
axes[1,0].text(60,300,'2013',fontsize=15)
axes[1,1].text(-20,300,'2013',fontsize=15)

axes[2,0].text(60,300,'2014',fontsize=15)
axes[2,1].text(-20,300,'2014',fontsize=15)

axes[3,0].text(50,300,'mean(2012-2014)',fontsize=15)
axes[3,1].text(-20,300,'mean(2012-2014)',fontsize=15)

axes[0,0].text(60,200,'r$^2$=%s'%str(np.round(np.corrcoef(windu2012,numu2012)[0][1],2)),fontsize=13)
axes[0,1].text(-20,200,'r$^2$=%s'%str(np.round(np.corrcoef(windv2012,numv2012)[0][1],2)),fontsize=13)
axes[1,0].text(60,200,'r$^2$=%s'%str(np.round(np.corrcoef(windu2013,numu2013)[0][1],2)),fontsize=13)
axes[1,1].text(-20,200,'r$^2$=%s'%str(np.round(np.corrcoef(windv2013,numv2013)[0][1],2)),fontsize=13)

axes[2,0].text(60,200,'r$^2$=%s'%str(np.round(np.corrcoef(windu2014,numu2014)[0][1],2)),fontsize=13)
axes[2,1].text(-20,200,'r$^2$=%s'%str(np.round(np.corrcoef(windv2014,numv2014)[0][1],2)),fontsize=13)
axes[0,0].set_xlim(xlim0)
axes[1,0].set_xlim(xlim0)
axes[2,0].set_xlim(xlim0)
axes[3,0].set_xlim(xlim0)
axes[0,1].set_xlim(xlim1)
axes[1,1].set_xlim(xlim1)
axes[2,1].set_xlim(xlim1)
axes[3,1].set_xlim(xlim1)

axes[0,0].get_xaxis().set_visible(False)
axes[0,1].get_xaxis().set_visible(False)
axes[1,0].get_xaxis().set_visible(False)
axes[1,1].get_xaxis().set_visible(False)
axes[2,0].get_xaxis().set_visible(False)
axes[2,1].get_xaxis().set_visible(False)
axes[0,1].get_yaxis().set_visible(False)
axes[1,1].get_yaxis().set_visible(False)
axes[2,1].get_yaxis().set_visible(False)
axes[3,1].get_yaxis().set_visible(False)

axes[0,0].set_ylim(ylim)
axes[0,1].set_ylim(ylim)
axes[1,0].set_ylim(ylim)
axes[1,1].set_ylim(ylim)
axes[2,0].set_ylim(ylim)
axes[2,1].set_ylim(ylim)
axes[3,0].set_ylim(ylim)
axes[3,1].set_ylim(ylim)

#axes[0,0].set_ylabel('Number of Strandings (per 3 days)')
axes[1,0].set_ylabel('Number of Strandings (per 3 days)',fontsize=14)
#axes[2,0].set_ylabel('Number of Strandings (per 3 days)')
#axes[3,0].set_ylabel('Number of Strandings (per 3 days)')

axes[0,0].set_title('Eastward Wind Stress vs Strandings on Outer Cape Towns',fontsize=14)
axes[0,1].set_title('Northward Wind Stress vs Strandings on Mid Cape Towns',fontsize=14)

wu=[]
wv=[]
nu=[]
nv=[]
for a in np.arange(len(windu2012)):
    wu.append(windu2012[a])
    nu.append(numu2012[a])
for a in np.arange(len(windu2013)):
    wu.append(windu2013[a])
    nu.append(numu2013[a])
for a in np.arange(1,len(windu2014)):
    wu.append(windu2014[a])
    nu.append(numu2014[a])
for a in np.arange(len(windv2012)):
    wv.append(windv2012[a])
    nv.append(numv2012[a])
for a in np.arange(len(windv2013)):
    wv.append(windv2013[a])
    nv.append(numv2013[a])

for a in np.arange(1,len(windv2014)):
    wv.append(windv2014[a])
    nv.append(numv2014[a])

X=wu
Y=nu
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print (z1)  #[ 1.          1.49333333]
print (p1)  # 1 x + 1.493
'''
plt.figure()
plt.scatter(wu,nu)   
'''
xx=np.linspace(-20,80,100)
yy=[]
for a in np.arange(len(xx)):
    yy.append(xx[a]*p1[1]+p1[0])
X=wv
Y=nv
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print z1  #[ 1.          1.49333333]
print p1  # 1 x + 1.493
xx1=np.linspace(-50,5,100)
yy1=[]
for a in np.arange(len(xx)):
    yy1.append(xx1[a]*p1[1]+p1[0])

axes[3,0].scatter(wu,nu)  
axes[3,1].scatter(wv,nv) 
axes[3,0].plot(xx,yy)
axes[3,1].plot(xx1,yy1)
axes[3,0].text(60,200,'r$^2$=%s'%str(np.round(np.corrcoef(wu,nu)[0][1],2)),fontsize=13)
axes[3,1].text(-10,200,'r$^2$=%s'%str(np.round(np.corrcoef(wv,nv)[0][1],2)),fontsize=13)

axes[3,0].set_xlabel('Sum of Eastward Wind Stress per 3 days (Pa)',fontsize=13)
axes[3,1].set_xlabel('Sum of Northward Wind Stress per 3 days (Pa)',fontsize=13)

plt.subplots_adjust(wspace=0.1,hspace=0.1)
plt.savefig('corrxxmx',dpi=300,bbox_inches='tight')
plt.savefig('Figure15.eps',format='eps',dpi=400,bbox_inches='tight')
    
    
