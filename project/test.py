import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

#generate array of f, m is size of array
def generate_f(m):
    f = np.random.uniform(0.0, 1.0, m)
    s = sum(f)
    r = [ i/s for i in f ]
    return r

n = 10
m = 10

f_array = generate_f(m)
sample_point = {'x':0, 'y':0, 'f':f_array[0]}
p1=[]
randX = []
randY = []
for i in range(0,m):
    new = sample_point.copy()
    new['x'] = np.random.randint(0, m*n)
    new['y'] = np.random.randint(0, m*n)
    new['f'] = f_array[i]
    p1.append(new)
new_p1 = sorted(p1, key=itemgetter('x'))

for i in range(0,m):
    print(new_p1[i])
for i in range(0,m):
    randX.append(new_p1[i]['x'])
    randY.append(new_p1[i]['y'])

plt.scatter(randX,randY,marker=".")
plt.show()

print(f_array)
print(sum(f_array))

#print (np.random.dirichlet(np.ones(10),size=1))