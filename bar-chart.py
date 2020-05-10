import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import time

def bubbleSort(n,a):
    for i in range(1,n):
        for j in range(n-i):
            if a[j]>a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a

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

def insertionSort(n,a):
    for i in range(1,n):
        for j in range(i,0,-1):
            if a[j]<a[j-1]:
                tmp = a[j]
                a[j]=a[j-1]
                a[j-1] = tmp
            else:
                break
    return a

def insertionSortFrames(n,a):
    sortingFrames = list()
    sortingFrames.append(a)
    for i in range(1,n):
        for j in range(i,0,-1):
            if a[j]<a[j-1]:
                tmp = a[j]
                a[j]=a[j-1]
                a[j-1] = tmp
                sortingFrames.append(list(a))
            else:
                break
    return sortingFrames

def merge(left,right):
    p1 = 0
    p2 = 0
    res = list()
    while p1<len(left) and p2 < len(right):
        if left[p1]<right[p2]:
            res.append(left[p1])
            p1 = p1+1
        else :
            res.append(right[p2])
            p2 = p2+1
    if p1 == len(left):
        while p2<len(right):
            res.append(right[p2])
            p2 = p2+1
    else :
        while p1<len(left):
            res.append(left[p1])
            p1 = p1+1
    return res

def mergeSort(n,a):
    if n==1:
        return a
    beg = 0
    end = n-1
    mid = (beg+end)//2
    left = mergeSort(mid+1,a[beg:mid+1])
    right = mergeSort(end - mid,a[mid+1:end+1])
    a = merge(left,right)
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
#sorting Algorithms comparison
b = list(a)
c = list(a)
d = list(a)
#print(a)
t1 = time.time()
a = mergeSort(n,a)
t2 = time.time()
#print(a)
print("timeof merge sort: " +  str(t2-t1))
#print(b)
t1 = time.time()
b = bubbleSort(n,b)
t2 = time.time()
#print(b)
print("timeof bubble sort: " +  str(t2-t1))
t1 = time.time()
c = selectionSort(n,c)
t2 = time.time()
#print(b)
print("timeof selection sort: " +  str(t2-t1))
t1 = time.time()
d = insertionSort(n,d)
t2 = time.time()
#print(b)
print("timeof insertion sort: " +  str(t2-t1))
'''
#sortingFrames = bubbleSortingFrames(n,a)
#sortingFrames = selectionSortFrames(n,a)
sortingFrames = insertionSortFrames(n,a)

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