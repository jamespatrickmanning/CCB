# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:46:35 2017

@author: xiaojian
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import  Series,DataFrame
cs=np.array([[118, 1, 18, 67, 25, 27, 65, 66, 1, 1, 1, 1, 1, 2, 9, 1, 1, 1, 1,0,0,0,0,0,0,0,0,0],
[36,0,17,4,24,37,33,65,0,0,0,0,0,0,0,0,0,0,0,3,1,0,0,0,0,0,0,0],
[38,1,63,88,292,316,286,99,0,1,1,0,0,0,3,0,14,0,0,14,0,1,2,1,1,6,0,0],
[33,0,13,31,104,96,124,61,0,1,0,1,2,1,9,0,0,1,1,28,0,0,1,0,0,0,1,1]])
c=[]
s=['Dennis','Yarmouth Port','Orleans','Barnstable','Truro','Eastham','Wellfleet','Brewster','Woods Hole','Falmouth','Nantasket Beach','Plymouth','Wareham','Yarmouth','Sandwich','East Dennis','Bourne','Nantucket','Hingham','Province town','Chappaquiddick','Marthas Vineyard','Hull','Chatham','West Falmouth','North Truro','West Tisbury','Duxbuy']
for a in np.arange(len(cs.T)):
    print a
    c.append(max(cs.T[a]))
    
for a in np.arange(len(c)):
    for b in np.arange(len(c)):
        
        if c[a]>=c[b]:
            t=c[a]
            c[a]=c[b]
            c[b]=t
            
            t1=s[a]
            s[a]=s[b]
            s[b]=t1
            
        
            t2=cs[0][a]
            cs[0][a]=cs[0][b]
            cs[0][b]=t2
            
        
            t3=cs[1][a]
            cs[1][a]=cs[1][b]
            cs[1][b]=t3
            
        
            t4=cs[2][a]
            cs[2][a]=cs[2][b]
            cs[2][b]=t4
        
            t5=cs[3][a]
            cs[3][a]=cs[3][b]
            cs[3][b]=t5
d=0            
for a in np.arange(len(s)):
    if s[a]=='Sandwich':
        d=a
    
cs1=list(cs[0][:8])
cs2=list(cs[1][:8])
cs3=list(cs[2][:8])
cs4=list(cs[3][:8])
cs1.append(cs[0][d])
cs2.append(cs[1][d])
cs3.append(cs[2][d])
cs4.append(cs[3][d])
ss=list(s[:8])
ss.append('Sandwich')
plt.figure()
#plt.title('Chart of the number of sea turtles in towns between 2012 - 2015')
df=DataFrame(np.array([cs1,cs2,cs3,cs4]).T,index=ss,columns=pd.Index(['2012','2013','2014','2015'],name='year'))
df.plot(kind='bar',alpha=0.5,rot=45,fontsize=10,figsize=(11,7))
plt.savefig('fig5',dpi=400)