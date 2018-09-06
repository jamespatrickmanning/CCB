# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 00:37:37 2017

@author: xiaojian
"""
from mpl_toolkits.basemap import Basemap  

import numpy as np
import matplotlib.pyplot as plt
from sympy import * 

c2 = np.genfromtxt('strandings2012C.csv',dtype=None,names=['a1','a2','a3'],delimiter=',',skip_header=1)
cc2=[]
for a in c2['a3']:
    if a not in cc2:
        cc2.append(a)

clat2=[41.7353,41.7088,41.7898,41.7003,41.9948,41.8300,41.9305,41.7601,41.5265,41.5532,42.2918,41.9584,41.7615,41.7056,41.7590,41.7426,41.7413,41.2835,42.2418]
clon2=[-70.1939,-70.2134,-69.9897,-70.3002,-70.0490,-69.9740,-70.0310,-70.0828,-70.6731,-70.6086,-70.8745,-70.6673,-70.7197,-70.2287,-70.4939,-70.1620,-70.5989,-70.0995,-70.8898]

c3 = np.genfromtxt('strandings2013C.csv',dtype=None,names=['a1','a2','a3'],delimiter=',',skip_header=1)  
cc3=[]
for a in c3['a3']:
    if a not in cc3:
        cc3.append(a)

clat3=[41.7601,41.7353,41.8300,42.0584,41.9305,41.9948,41.7003,41.7601,41.7898,41.3744]
clon3=[-70.0828,-70.1939,-69.9740,-70.1786,-70.0310,-70.0490,-70.3002,-70.0828,-69.9897,-70.4729]

c4 = np.genfromtxt('strandings2014C.csv',dtype=None,names=['a1','a2','a3'],delimiter=',',skip_header=1)  
cc4=[]
for a in c4['a3']:
    if a not in cc4:
        cc4.append(a)
clat4=[41.9305,41.9948,41.3805,41.7003,41.7353,41.7601,41.7898,41.8300,42.3021,42.0584,41.7088,41.7413,41.7590,41.5532,41.2835,41.6821,41.6043,42.0393]
clon4=[-70.0310,-70.0490,-70.6455,-70.3002,-70.1939,-70.0828,-69.9897,-69.9740,-70.9078,-70.1786,-70.2134,-70.5989,-70.4939,-70.6086,-70.0995,-69.9598,-70.6345,-70.0972]

c5 = np.genfromtxt('strandings2015C.csv',dtype=None,names=['a1','a2','a3'],delimiter=',',skip_header=1) 
cc5=[]
for a in c5['a3']:
    if a not in cc5:
        cc5.append(a)
clat5=[41.9305,41.9584,41.9948,41.7353,42.2418,41.7003,41.3812,41.7590,42.0584,41.8300,41.7898,42.3021,41.7601,41.7615,41.7056,41.5532,41.2835,42.0418]
clon5=[-70.0310,-70.6673,-70.0490,-70.1939,-70.8898,-70.3002,-70.6745,-70.4939,-70.1786,-69.9740,-69.9897,-70.9078,-70.0828,-70.7197,-70.2287,-70.6086,-70.0995,-70.6723]
ct=[]
lon=[]
lat=[]
for a in np.arange(len(cc2)):
    ct.append(cc2[a])
    lon.append(clon2[a])
    lat.append(clat2[a])
for a in np.arange(len(cc3)):
    ct.append(cc3[a])
    lon.append(clon3[a])
    lat.append(clat3[a])
for a in np.arange(len(cc4)):
    ct.append(cc4[a])
    lon.append(clon4[a])
    lat.append(clat4[a])
for a in np.arange(len(cc5)):
    ct.append(cc5[a])
    lon.append(clon5[a])
    lat.append(clat5[a])
ct1=[]
clon1=[]
clat1=[]
for a in ct:
    if a not in ct1:
        ct1.append(a)
index=[]
for a in np.arange(len(ct1)):
    for b in np.arange(len(ct)):
        if ct1[a]==ct[b]:
            index.append(b)
            #ct[b]='c%s'%(b)
for a in lon:
    if a not in clon1:
        clon1.append(a)
for a in lat:
    if a not in clat1:
        clat1.append(a)
lonx=[-70.1939,-70.2134,-69.9897,-70.3002,-70.0490,-69.9740,-70.0310,-70.0828,-70.6731,-70.6086,-70.8745,-70.6673,-70.7197,-70.2287,-70.4939,-70.1620,-70.5989,-70.0995,-70.8898,-70.1786,-70.4729,-70.6455,-70.9078,-69.9598,-70.6345,-70.0972,-70.6745,-70.6723]
latx=[41.7353,41.7088,41.7898,41.7003,41.9948,41.8300,41.9305,41.7601,41.5265,41.5532,42.2918,41.9584,41.7615,41.7056,41.7590,41.7426,41.7413,41.2835,42.2418,42.0584,41.3744,41.3805,42.3021,41.6821,41.6043,42.0393,41.3812,42.0418]
#plt.axis([-71.00,-69.8,41.2,42.38])
fig,axes=plt.subplots(1,1,figsize=(10,10))
#plt.scatter(lonx,latx,color='red')
m = Basemap(projection='cyl',llcrnrlat=41.2,urcrnrlat=42.38,\
            llcrnrlon=-71,urcrnrlon=-69.8,resolution='h')#,fix_aspect=False)
    #  draw coastlines
m.drawcoastlines()
m.ax=axes
m.fillcontinents(color='oldlace',alpha=1,zorder=0)
m.drawmapboundary()
#draw major rivers
#m.drawrivers()
parallels = np.arange(41.2,42.38,0.2)
m.drawparallels(parallels,labels=[1,0,0,0],dashes=[1,1000],fontsize=10,zorder=0)
meridians = np.arange(-71.,-69.8,0.5)
m.drawmeridians(meridians,labels=[0,0,0,1],dashes=[1,1000],fontsize=10,zorder=0)

Hull=0
Nantasket_Beach=0
Hingham=0
Duxbury=0
Wareham=0
Woods_Hole=0
Chatham=0
West_Tisbury=0
Martha_s_Vineyard=0
Chappaquiddick=0

Nantucket=0
Barnstable=0
Yarmouth=0
Brewster=0
Provincetown=0
Truro=0
Wellfleet=0
Eastham=0
Orleans=0
Dennis=0
Sandwich=0
Plymouth=0
Bourne=0
Falmouth=0

for a in np.arange(len(c2['a3'])):
    if c2['a3'][a]=='Hull':
        Hull=Hull+1
    if c2['a3'][a]=='Nantasket Beach':
        Nantasket_Beach=Nantasket_Beach+1
    if c2['a3'][a]=='Hingham':
        Hingham=Hingham+1
    if c2['a3'][a]=='Duxbury':
        Duxbury=Duxbury+1
    if c2['a3'][a]=='Wareham':
        Wareham=Wareham+1  
    if c2['a3'][a]=='Woods Hole':
        Woods_Hole=Woods_Hole+1 
    if c2['a3'][a]=='Chatham':
        Chatham=Chatham+1  
    if c2['a3'][a]=='West Tisbury':
        West_Tisbury=West_Tisbury+1  
    if c2['a3'][a]=='''Martha's Vineyard''':
        Martha_s_Vineyard=Martha_s_Vineyard+1 
    if c2['a3'][a]=='Chappaquiddick':
        Chappaquiddick=Chappaquiddick+1 
    if c2['a3'][a]=='Nantucket':
        Nantucket=Nantucket+1
    if c2['a3'][a]=='Barnstable':
        Barnstable=Barnstable+1
    if c2['a3'][a]=='Yarmouth':
        Yarmouth=Yarmouth+1
    if c2['a3'][a]=='Brewster':
        Brewster=Brewster+1
    if c2['a3'][a]=='Provincetown':
        Provincetown=Provincetown+1
    if c2['a3'][a]=='Truro':
        Truro=Truro+1
    if c2['a3'][a]=='Wellfleet':
        Wellfleet=Wellfleet+1
    if c2['a3'][a]=='Eastham':
        Eastham=Eastham+1
    if c2['a3'][a]=='Orleans':
        Orleans=Orleans+1
    if c2['a3'][a]=='Dennis':
        Dennis=Dennis+1
    if c2['a3'][a]=='Sandwich':
        Sandwich=Sandwich+1
    if c2['a3'][a]=='Plymouth':
        Plymouth=Plymouth+1
    if c2['a3'][a]=='Bourne':
        Bourne=Bourne+1
    if c2['a3'][a]=='Falmouth':
        Falmouth=Falmouth+1
        

for a in np.arange(len(c3['a3'])):
    if c3['a3'][a]=='Hull':
        Hull=Hull+1
    if c3['a3'][a]=='Nantasket Beach':
        Nantasket_Beach=Nantasket_Beach+1
    if c3['a3'][a]=='Hingham':
        Hingham=Hingham+1
    if c3['a3'][a]=='Duxbury':
        Duxbury=Duxbury+1
    if c3['a3'][a]=='Wareham':
        Wareham=Wareham+1  
    if c3['a3'][a]=='Woods Hole':
        Woods_Hole=Woods_Hole+1 
    if c3['a3'][a]=='Chatham':
        Chatham=Chatham+1  
    if c3['a3'][a]=='West Tisbury':
        West_Tisbury=West_Tisbury+1  
    if c3['a3'][a]=='''Martha's Vineyard''':
        Martha_s_Vineyard=Martha_s_Vineyard+1 
    if c3['a3'][a]=='Chappaquiddick':
        Chappaquiddick=Chappaquiddick+1 
    if c3['a3'][a]=='Nantucket':
        Nantucket=Nantucket+1
    if c3['a3'][a]=='Barnstable':
        Barnstable=Barnstable+1
    if c3['a3'][a]=='Yarmouth':
        Yarmouth=Yarmouth+1
    if c3['a3'][a]=='Brewster':
        Brewster=Brewster+1
    if c3['a3'][a]=='Provincetown':
        Provincetown=Provincetown+1
    if c3['a3'][a]=='Truro':
        Truro=Truro+1
    if c3['a3'][a]=='Wellfleet':
        Wellfleet=Wellfleet+1
    if c3['a3'][a]=='Eastham':
        Eastham=Eastham+1
    if c3['a3'][a]=='Orleans':
        Orleans=Orleans+1
    if c3['a3'][a]=='Dennis':
        Dennis=Dennis+1
    if c3['a3'][a]=='Sandwich':
        Sandwich=Sandwich+1
    if c3['a3'][a]=='Plymouth':
        Plymouth=Plymouth+1
    if c3['a3'][a]=='Bourne':
        Bourne=Bourne+1
    if c3['a3'][a]=='Falmouth':
        Falmouth=Falmouth+1

for a in np.arange(len(c4['a3'])):
    if c4['a3'][a]=='Hull':
        Hull=Hull+1
    if c4['a3'][a]=='Nantasket Beach':
        Nantasket_Beach=Nantasket_Beach+1
    if c4['a3'][a]=='Hingham':
        Hingham=Hingham+1
    if c4['a3'][a]=='Duxbury':
        Duxbury=Duxbury+1
    if c4['a3'][a]=='Wareham':
        Wareham=Wareham+1  
    if c4['a3'][a]=='Woods Hole':
        Woods_Hole=Woods_Hole+1 
    if c4['a3'][a]=='Chatham':
        Chatham=Chatham+1  
    if c4['a3'][a]=='West Tisbury':
        West_Tisbury=West_Tisbury+1  
    if c4['a3'][a]=='''Martha's Vineyard''':
        Martha_s_Vineyard=Martha_s_Vineyard+1 
    if c4['a3'][a]=='Chappaquiddick':
        Chappaquiddick=Chappaquiddick+1 
    if c4['a3'][a]=='Nantucket':
        Nantucket=Nantucket+1
    if c4['a3'][a]=='Barnstable':
        Barnstable=Barnstable+1
    if c4['a3'][a]=='Yarmouth':
        Yarmouth=Yarmouth+1
    if c4['a3'][a]=='Brewster':
        Brewster=Brewster+1
    if c4['a3'][a]=='Provincetown':
        Provincetown=Provincetown+1
    if c4['a3'][a]=='Truro':
        Truro=Truro+1
    if c4['a3'][a]=='Wellfleet':
        Wellfleet=Wellfleet+1
    if c4['a3'][a]=='Eastham':
        Eastham=Eastham+1
    if c4['a3'][a]=='Orleans':
        Orleans=Orleans+1
    if c4['a3'][a]=='Dennis':
        Dennis=Dennis+1
    if c4['a3'][a]=='Sandwich':
        Sandwich=Sandwich+1
    if c4['a3'][a]=='Plymouth':
        Plymouth=Plymouth+1
    if c4['a3'][a]=='Bourne':
        Bourne=Bourne+1
    if c4['a3'][a]=='Falmouth':
        Falmouth=Falmouth+1
for a in np.arange(len(c5['a3'])):
    if c5['a3'][a]=='Hull':
        Hull=Hull+1
    if c5['a3'][a]=='Nantasket Beach':
        Nantasket_Beach=Nantasket_Beach+1
    if c5['a3'][a]=='Hingham':
        Hingham=Hingham+1
    if c5['a3'][a]=='Duxbury':
        Duxbury=Duxbury+1
    if c5['a3'][a]=='Wareham':
        Wareham=Wareham+1  
    if c5['a3'][a]=='Woods Hole':
        Woods_Hole=Woods_Hole+1 
    if c5['a3'][a]=='Chatham':
        Chatham=Chatham+1  
    if c5['a3'][a]=='West Tisbury':
        West_Tisbury=West_Tisbury+1  
    if c5['a3'][a]=='''Martha's Vineyard''':
        Martha_s_Vineyard=Martha_s_Vineyard+1 
    if c5['a3'][a]=='Chappaquiddick':
        Chappaquiddick=Chappaquiddick+1 
    if c5['a3'][a]=='Nantucket':
        Nantucket=Nantucket+1
    if c5['a3'][a]=='Barnstable':
        Barnstable=Barnstable+1
    if c5['a3'][a]=='Yarmouth':
        Yarmouth=Yarmouth+1
    if c5['a3'][a]=='Brewster':
        Brewster=Brewster+1
    if c5['a3'][a]=='Provincetown':
        Provincetown=Provincetown+1
    if c5['a3'][a]=='Truro':
        Truro=Truro+1
    if c5['a3'][a]=='Wellfleet':
        Wellfleet=Wellfleet+1
    if c5['a3'][a]=='Eastham':
        Eastham=Eastham+1
    if c5['a3'][a]=='Orleans':
        Orleans=Orleans+1
    if c5['a3'][a]=='Dennis':
        Dennis=Dennis+1
    if c5['a3'][a]=='Sandwich':
        Sandwich=Sandwich+1
    if c5['a3'][a]=='Plymouth':
        Plymouth=Plymouth+1
    if c5['a3'][a]=='Bourne':
        Bourne=Bourne+1
    if c5['a3'][a]=='Falmouth':
        Falmouth=Falmouth+1
    
for a in np.arange(len(ct1)):
    if ct1[a]=='Hull':
        plt.text(lonx[a]+0.03,latx[a]+0.01,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Hull,color='red')
    elif ct1[a]=='Nantasket Beach':
        plt.text(lonx[a]+0.03,latx[a]-0.015,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Nantasket_Beach,color='red')
    elif ct1[a]=='Hingham':
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Hingham,color='red')
    elif ct1[a]=='Duxbury':
        plt.text(lonx[a]-0.12,latx[a],ct1[a])
        plt.scatter(lonx[a],latx[a],s=Duxbury,color='red')
    elif ct1[a]=='Wareham':
        plt.text(lonx[a],latx[a]+0.03,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Wareham,color='red')
    elif ct1[a]=='West Falmouth':
        pass
    elif ct1[a]=='East Dennis':
        pass
    elif ct1[a]=='Yarmouth Port':
        pass
    elif ct1[a]=='North Truro':
        pass
    elif ct1[a]=='Woods Hole':
        plt.text(lonx[a]-0.12,latx[a]+0.03,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Woods_Hole,color='red')
    elif ct1[a]=='Chatham':
        plt.text(lonx[a]+0.04,latx[a]+0,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Chatham,color='red')
    elif ct1[a]=='West Tisbury':
        plt.text(lonx[a]-0.22,latx[a]+0,ct1[a])
        plt.scatter(lonx[a],latx[a],s=West_Tisbury,color='red')
    elif ct1[a]=="Martha's Vineyard":
        plt.text(lonx[a]-0.02,latx[a]-0.08,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Martha_s_Vineyard,color='red')
    elif ct1[a]=="Chappaquiddick":
        plt.text(lonx[a]+0.03,latx[a]-0.,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Chappaquiddick,color='red')
    elif ct1[a]=="Nantucket":
        plt.text(lonx[a]-0.12,latx[a]+0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Nantucket,color='red')
    elif ct1[a]=="Barnstable":
        plt.text(lonx[a]-0.06,latx[a]+0.06,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Barnstable,color='#930093')
    elif ct1[a]=="Yarmouth":
        plt.text(lonx[a]-0.06,latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Yarmouth,color='#930093')
    elif ct1[a]=="Brewster":
        plt.text(lonx[a]-0.04,latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Brewster,color='#930093')
    elif ct1[a]=="Provincetown":
        plt.text(lonx[a]-0.04,latx[a]+0.05,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Provincetown,color='green')
    elif ct1[a]=="Truro":
        plt.text(lonx[a]+0.04,latx[a]+0.01,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Truro,color='green')
        plt.text(lonx[a]-0.02,latx[a]-0.01,'%s'%Truro,color='white',weight='bold')
    elif ct1[a]=="Wellfleet":
        plt.text(lonx[a]+0.05,latx[a]+0.0,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Wellfleet,color='green')
        plt.text(lonx[a]-0.02,latx[a]-0.01,'%s'%Wellfleet,color='white',weight='bold')
    elif ct1[a]=="Falmouth":
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Sandwich,color='red',label='other towns(number=%s)'%(Falmouth))
   
    elif ct1[a]=="Eastham":
        plt.text(lonx[a]+0.05,latx[a]+0.0,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Eastham,color='green',label="'Outer Cape' Towns(number=%s)"%(Eastham))
        plt.text(lonx[a]-0.02,latx[a]-0.01,'%s'%Eastham,color='white',weight='bold')
    elif ct1[a]=="Orleans":
    
        plt.text(lonx[a]+0.06,latx[a]-0.02,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Orleans,color='green')
    elif ct1[a]=="Dennis":
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Dennis,color='#930093',label="'Mid Cape' Towns(number=%s)"%(Dennis))
    elif ct1[a]=="Sandwich":
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Sandwich,color='#930093')
    elif ct1[a]=="Plymouth":
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Sandwich,color='red')
    elif ct1[a]=="Bourne":
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],s=Sandwich,color='red')
    else:
        continue
        """
        plt.text(lonx[a],latx[a]-0.04,ct1[a])
        plt.scatter(lonx[a],latx[a],color='red',label='other towns')
        """
FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])
#plt.plot(CL['lon'],CL['lat'],'b-',linewidth=0.7)
#plt.axis([-71.00,-69.8,41.2,42.38])#axes[0].axis([-71,-64.75,42.5,45.33])-67.875,-64.75,43.915,45.33
plt.legend(loc='upper right',fontsize='x-large',scatterpoints=1)
#axes.xaxis.tick_top() 
#plt.xlabel('longitude')
#plt.ylabel('latitude')
plt.savefig('turtle_city(2012-2015)new',dpi=400,bbox_inches='tight')
fig_saved=plt.gcf()#get current figure
fig_saved.savefig('fig4.eps',format='eps',dpi=400,bbox_inches='tight')
plt.show()