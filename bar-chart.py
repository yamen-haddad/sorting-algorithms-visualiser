import numpy as np
import matplotlib.pyplot as plt
import random

def bubbleSort(n,a):
    for i in range(1,n):
        for j in range(n-i):
            if a[j]>a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a
#reading the array from std input 
'''n = int(input())
s = input().split()
a = list()
for i in range(n):
    a.append(int(s[i]))'''
# Generating array of permutation of size n randomly positioned in the array
n = int(input())
a = [i for i in range(1,n+1)]
#print(a)
#shuffle a in place
random.shuffle(a)
#print(a)
plt.figure("array")
xmin = 0
xmax = n
ymin = 0
ymax = n
axis = [xmin,xmax,ymin,ymax]
width = 1
align = 'edge'
x = np.arange(n)
plt.subplot(2,1,1)
plt.axis(axis)
plt.bar(x,a,width = width,align = align)
a = bubbleSort(n,a)
plt.subplot(2,1,2)
plt.axis(axis)
plt.bar(x,a,width = width,align=align)
plt.show()
