# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:46:35 2017

@auther JiM 
rewrite of Xiaojian's fig5.py in June 2019 made a "stranding_by_town.html" flowchart
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### Hardcode strandings by town for 2012-2015 apparently obtained by Xiaojian from strandings excel spreadsheet
years=['2012','2013','2014','2015']
towns=['Dennis','Yarmouth Port','Orleans','Barnstable','Truro','Eastham','Wellfleet','Brewster','Woods Hole','Falmouth','Nantasket Beach','Plymouth','Wareham','Yarmouth','Sandwich','East Dennis','Bourne','Nantucket','Hingham','Provincetown','Chappaquiddick','Marthas Vineyard','Hull','Chatham','West Falmouth','North Truro','West Tisbury','Duxbuy']
s2012=[118, 1, 18, 67, 25, 27, 65, 66, 1, 1, 1, 1, 1, 2, 9, 1, 1, 1, 1,0,0,0,0,0,0,0,0,0]
s2013=[36,0,17,4,24,37,33,65,0,0,0,0,0,0,0,0,0,0,0,3,1,0,0,0,0,0,0,0]
s2014=[38,1,63,88,292,316,286,99,0,1,1,0,0,0,3,0,14,0,0,14,0,1,2,1,1,6,0,0]
s2015=[33,0,13,31,104,96,124,61,0,1,0,1,2,1,9,0,0,1,1,28,0,0,1,0,0,0,1,1]
numtowns=8 # the number of top towns you want to include in plot
###

# now find out what are the top "numtowns" towns
stotal=[s2012[i]+s2013[i]+s2014[i]+s2015[i] for i in range(len(towns))] # totals all years for each town
ind=list(reversed(np.argsort(stotal))) # this is the index of towns sorted with the most strandings being first

# now redefine each year with only the top numtowns
s2012_top=[s2012[i] for i in ind][:numtowns]
s2013_top=[s2013[i] for i in ind][:numtowns]
s2014_top=[s2014[i] for i in ind][:numtowns]
s2015_top=[s2015[i] for i in ind][:numtowns]
towns_top=[towns[i] for i in ind][:numtowns]

# define a dataframe and plot it
df=pd.DataFrame(np.array([s2012_top,s2013_top,s2014_top,s2015_top]).T,index=list(towns_top),columns=pd.Index(years,name='Year'))
df.plot(kind='bar',alpha=0.5,rot=45,fontsize=10,figsize=(11,7))
plt.show()
plt.savefig('strandings_by_top'+str(numtowns)+'_towns.png',dpi=400)
