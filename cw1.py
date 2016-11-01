from __future__ import division
import numpy
import sys
import matplotlib.pyplot as plt
import math

B=2
z=[-1,1]
d=[[0,0,0],
   [0,0,1],
   [0,1,0],
   [1,0,0],
   [1,1,0],
   [0,1,1],
   [1,0,1],
   [1,1,1]]
e=[-1,0,1,2]
XX=[]

for i in range(0,7):
   for znak in z:
      for cecha in e:
         x=znak*(d[i][0]/(B**1) + d[i][1]/(B**2) + d[i][2]/(B**3))*(B**cecha)
         XX.append(x)
   
Y = [0]*len(XX)

plt.figure(1)
plt.plot(XX,Y,"x")
plt.show()
