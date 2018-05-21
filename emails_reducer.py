#!/usr/bin/python
import sys
d={}
k=0
for line in sys.stdin:
 sender,count=line.split(',')
 if(k==0):
  d[sender]=int(count)
  k=k+1
 else:
  nh=[key for key in d]
  if(sender in nh):
   d[sender]=d[sender]+int(count)
  else:
   d[sender]=int(count)
desc_order_list=sorted(d,key=d.get,reverse=True)
for i in range(0,3):
 print(desc_order_list[i],d[desc_order_list[i]])