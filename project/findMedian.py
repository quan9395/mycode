from math import pi
import numpy as np
import medianOfMedians as mm
from operator import itemgetter
import sys

def findMedian(I):
    #for i in all_p:
        #print(i['x'],i['y'],i['f'], i['left'].x, i['right'].x)
    I2=[]
    for i in I:
        I2.append(i.x)
    #p = mm.select(I2, 0, len(I2)-1, len(I2)/2)   #pick middle endpoint
    pivot = I[int((len(I2))/2)]
    #for i in I:
     #   if(i == i.x):
      #      pivot = i

    I_l=[]
    I_r=[]

    for i in I:     #partition into 3 array I
        if(i.x < pivot.x):
            I_l.append(i)
        elif(i.x > pivot.x):
            I_r.append(i)
        else:
            continue

    for i in I:            #calculate f for middle endpoint
        if(i.side == 0 and pivot.x < i.x):
            pivot.sumRight += i.f
        if(i.side == 1 and pivot.x > i.x):
            pivot.sumLeft += i.f
    slope = pivot.sumLeft - pivot.sumRight
    print(slope)

    I2=[]   #select neighbor
    for i in I_r:
        I2.append(i.x)               
    n = min(I2)
    neighbor = I_r[0]
    for i in I_r:
        if(n == i.x):
            neighbor = i
    
    if(pivot.side == 1 and neighbor.side == 1):
        neighbor.sumLeft = pivot.sumLeft + pivot.f
        neighbor.sumRight = pivot.sumRight
    if(pivot.side == 1 and neighbor.side == 0):
        neighbor.sumLeft = pivot.sumLeft + pivot.f
        neighbor.sumRight = pivot.sumRight - neighbor.f
    if(pivot.side == 0 and neighbor.side == 0):
        neighbor.sumLeft = pivot.sumLeft
        neighbor.sumRight = pivot.sumRight - neighbor.f
    if(pivot.side == 0 and neighbor.side == 1):
        neighbor.sumLeft = pivot.sumLeft
        neighbor.sumRight = pivot.sumRight

    slope2 = neighbor.sumLeft - neighbor.sumRight
    print(slope2)

    if(slope*slope2 < 0):
        return pivot
    elif(slope < 0 and slope2 < 0):
        for i in I_l:
            try:
                index = i['left'].index(i)
                i.pop(index)
            except ValueError:
                continue
        for i in I_l:
            try:
                index = i['right'].index(i)
                i.pop(index)
            except ValueError:
                continue
        findMedian(I)
    else:
        for i in I_r:
            try:
                index = all_p['left'].index(i)
                all_p.pop(index)
            except ValueError:
                continue
        for i in I_r:
            try:
                index = all_p['right'].index(i)
                all_p.pop(index)
            except ValueError:
                continue
        findMedian(I)