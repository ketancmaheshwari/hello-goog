#!/usr/bin/env python

def parent(i):
    return i/2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def heapify(alist, i, n):
    largest=i
    l=left(i)
    r=right(i)

    if l <= n and alist[l] > alist[i]:
        largest=l
    else:
        largest=i

    if r <= n and alist[r] > alist[largest]:
        largest=r

    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]
        heapify(alist, largest, len(alist)-1)

def buildheap(alist, n):
    for i in range(n/2, -1, -1):
        heapify(alist, i, len(alist)-1)

def heapsort(list):
    for item in list:
        print item
    return list
def main():
    global data
    #data = [int(data.strip()) for data in open('../../data/numlist10.txt')]
    data=[2,1,5,4,10,3]
    print data
    buildheap(data, len(data)-1)
    #sdata = heapsort(data)
    print data

if __name__=='__main__':
    main()
