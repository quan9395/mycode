import numpy as np
import matplotlib.pyplot as plt
from findMedian import findMedian
#import random
import medianOfMedians as mm
from operator import itemgetter
import sys

#from numpy.core.numeric import allclose

#generate array of f, m is size of array
def generate_f(m):
    f = np.random.randint(1, 9999999, m)
    s = sum(f)
    r = [ i/s for i in f ]
    return r

def generate_f2(m):
    d = 10**(len(str(m)) + 2)
    rand = [1]*m
    rand2 = generate_f(m)   #generate array of randoms, sum is 1
    for i in range(0,m):
        rand[i] = rand2[i]
    rnd_array = np.random.multinomial(d, rand, size=m)[np.random.randint(0,m)]
    rnd = [i/(d) for i in rnd_array]
    return rnd

class endPoint:
    def __init__(self, x, sumLeft, sumRight, sumI, f, side):
        self.x = x
        self.sumLeft = sumLeft
        self.sumRight = sumRight
        self.sumI = sumI
        self.f = f
        self.side = side


print("How many uncertain points? (n) ")
n = int(input())
print("How many locations for each point? (m) ")
m = int(input())

rows, cols = (n, m)
all_f = [[0 for i in range(cols)] for j in range(rows)]

for j in range(0, n):       #generate f array
    f_array = generate_f2(m)
    for i in range(0, m):
        all_f[j][i] = f_array[i]

print(all_f)

arr_I = []
arr_Ii = []
all_p = []
randX = []
randY = []

for j in range(0,n):        #generate all_p
    p1=[]
    for i in range(0,m):
        left = endPoint(0,0,0,0,0,0)
        right = endPoint(0,0,0,0,0,1)
        sample_point = {'x':0, 'y':0, 'f':f_array[0], 'left':left, 'right':right}
        new = dict(sample_point)
        new['x'] = np.random.randint(0, m*n)
        new['y'] = np.random.randint(0, m*n)
        new['f'] = all_f[j][i]
        new['left'].x = new['x'] - new['y']  #include negative value for y (abs)
        new['left'].f = new['f']
        new['right'].x = new['x'] + new['y']
        new['right'].f = new['f']
        p1.append(new)
    #new_p = sorted(p1, key=itemgetter('x'))
    all_p.append(p1)


for p in all_p:    #put endpoints in arrays
    for i in p:
        arr_I.append(i['left'])
        arr_I.append(i['right'])

for j in range (0,n):
    for i in range(0,m):
        print(all_p[j][i]['x'],all_p[j][i]['y'],all_p[j][i]['f'], all_p[j][i]['left'].x, all_p[j][i]['right'].x)
    print("======")


#for i in range(0,m):
 #   randX.append(new_p[i]['x'])
  #  randY.append(new_p[i]['y'])

#result = findMedian(arr_I)
#print(result)

#plt.scatter(randX,randY,marker=".")
#plt.show()

#print("{:.2f}".format(sum(all_f[0])))

