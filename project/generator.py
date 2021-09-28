import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

from numpy.core.numeric import allclose

#generate array of f, m is size of array
def generate_f(m):
    f = np.random.uniform(0.0, 1.0, m)
    s = sum(f)
    r = [ i/s for i in f ]
    return r

def generate_f2(m):
    d = 10**(len(str(m)) + 1)
    rnd_array = np.random.multinomial(d, np.ones(m)/(m), size=1)[0]
    rnd = [i/(d) for i in rnd_array]
    return rnd

print("How many uncertain points? (n) ")
n = int(input())
print("How many locations for each point? (m) ")
m = int(input())

rows, cols = (n, m)
all_f = [[0 for i in range(cols)] for j in range(rows)]

for j in range(0, n):
    f_array = generate_f2(m)
    for i in range(0, m):
        all_f[j][i] = f_array[i]

#print(all_f)

sample_point = {'x':0, 'y':0, 'f':f_array[0]}
all_p = []
randX = []
randY = []

for j in range(0,n):
    p1=[]
    for i in range(0,m):
        new = sample_point.copy()
        new['x'] = np.random.randint(0, m*n)
        new['y'] = np.random.randint(0, m*n)
        new['f'] = f_array[i]
        p1.append(new)
    new_p = sorted(p1, key=itemgetter('x'))
    all_p.append(new_p)

for j in range (0,n):
    for i in range(0,m):
        print(all_p[j][i])
    print("======")


for i in range(0,m):
    randX.append(new_p[i]['x'])
    randY.append(new_p[i]['y'])


#plt.scatter(randX,randY,marker=".")
#plt.show()

print("{:.2f}".format(sum(all_f[0])))

