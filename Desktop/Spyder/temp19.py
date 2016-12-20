# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:43:11 2016

@author: athira
"""

from collections import deque

n = 3017957

x1 = deque()
x2  = deque()

for i in range(1,int(n/2)+2):
    x1.append(i)

for i in range(int(n/2)+2,n+1):
    x2.append(i)
 
while len(x1)+len(x2)>1:   
    if len(x1)==len(x2):
        x2.popleft()
    else:
        x1.pop()
    x2.append(x1.popleft())
    x1.append(x2.popleft())
        
print(x1)
    

    