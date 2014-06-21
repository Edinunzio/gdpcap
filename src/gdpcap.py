import math
import numpy as np
import itertools as it
import pandas as pd
import matplotlib.pyplot as plt
def euclid_dist(p0,p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

df1 = pd.read_csv('clean_dataset.csv', header =0)
#df.drop(["Country"],inplace=True,axis=1)
df2 = df1.ix[1:]
print df2 
#for row in df:
#my_combo= list(it.combinations(row,2))
#print my_combo

#	my_list= []
#	for x,y in my_combo:
#   		my_list.append(euclid_dist)
#        
#gdp = np.loadtxt(my_list, delimiter=",", dtype='float')
#plt.hist(gdp, bins=10, facecolor='red')
#plt.show()                
