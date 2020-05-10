import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

def bubbleSort(n,a):
    for i in range(1,n):
        for j in range(n-i):
            if a[j]>a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a

def selectionSort(n,a):
    for i in range(n):
        mind = 0
        mmax = a[0]
        for j in range(1,n-i):
            if a[j]>mmax:
                mmax = a[j]
                mind = j
        tmp = a[n-1-i]
        a[n-1-i] = a[mind]
        a[mind] = tmp
    return a

def selectionSortFrames(n,a):
    sortingFrames = list()
    for i in range(n):
        mind = 0
        mmax = a[0]
        for j in range(1,n-i):
            if a[j]>mmax:
                mmax = a[j]
                mind = j
        tmp = a[n-1-i]
        a[n-1-i] = a[mind]
        a[mind] = tmp
        sortingFrames.append(list(a))
    return sortingFrames

def bubbleSortingFrames(n,a):
    sortingFrames = list()
    for i in range(1,n):
        for j in range(n-i):
            if a[j]>a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
            sortingFrames.append(list(a))
    return sortingFrames
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
#a = selectionSort(n,a)
#print(a)

#sortingFrames = bubbleSortingFrames(n,a)
sortingFrames = selectionSortFrames(n,a)
# Add Animation for bubble sort
fig, ax = plt.subplots()
ydata = sortingFrames[0]
xdata = np.arange(n)
xmin = 0
xmax = n
ymin = 0
ymax = n
axis = [xmin,xmax,ymin,ymax]
width = 1
align = 'edge'
interval = 0.0000001
rects = plt.bar(xdata,ydata,width = width,align = align)

def update(frame):
    i = 0
    for rect in rects:
        rect.set_height(frame[i])
        i = i+1
    return rects
    #return plt.bar(xdata,frame,width = width,align = align)
ani = FuncAnimation(fig, update, frames=sortingFrames, blit=True,interval = interval)
plt.show()

'''
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
'''