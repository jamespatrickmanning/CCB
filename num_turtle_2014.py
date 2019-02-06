# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:33:33 2018

@author: huimin
"""

import numpy as np
import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,1,figsize=(10,6))#,sharex=True)
tt2014=np.load('tt2014.npy')
h2014=np.load('h2014.npy')

#ax.set_title('The number of turtles reaching Cape Cod Bay every day in late 2014',fontsize=15)
ax.bar(tt2014,h2014,width=0.5,label='retention')
#df=pd.DataFrame(np.array(h).T,index=list(tt))#,columns=pd.Index(['2004','2005','2006','2007','2008','2009','2010']))#,name='Genus'))
#df.plot(kind='bar',ax=axes[0])
ax.set_ylim([0,210])
ax.set_ylabel('number',fontsize=13)
ax.xaxis_font = {'size':'13'}
for label in ax.get_xticklabels():
        label.set_rotation(10)
plt.savefig('num_turtle_2014',dpi=200,bbox_inches = "tight")
plt.savefig('Figure9.eps',format='eps',dpi=400,bbox_inches = "tight")
