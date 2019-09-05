# routine to plot a bathymetry file in "bty" format
# with options on 60 and 100m via sys_arg
from matplotlib import pyplot as plt
import sys
import pandas as pd
def pltbty():
  try:
    depth=sys.argv[1]
  except:
    depth='both'
  print depth
  if depth=='100':
    f2= open('/net/data5/jmanning/bathy/gofmgbk_100m.bty')
  elif depth=='60':
    f2= open('/net/data5/jmanning/bathy/necs_60m.bty') #you may need to change this path
  else:
    f2= open('/net/data5/jmanning/bathy/necs_60m_100m.bty') # both 60 and 100
    d3=pd.read_csv('/net/data5/jmanning/bathy/bathy_60_100_200.dat',sep='\s*',header=None)
    #f3=open('/net/data5/jmanning/bathy/bathy_60_100_200.dat') # both 60 and 100
    plt.scatter(d3[:][0].values,d3[:][1].values,color='k',s=2)
  d=f2.readlines()
  id=[]
  for j in range(len(d)):
    if len(d[j])>21: # start of new segment
      id.append(j)
  for k in range(len(id)-1): # loop through each section
      lon,lat=[],[]
      for i in range(id[k]+1,id[k+1]):
        lon.append(-1*float(d[i][0:10]))
        lat.append(float(d[i][11:20]))      
      plt.plot(lon,lat,'k-')
  
