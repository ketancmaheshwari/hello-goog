#!/usr/bin/env python


def heapify(alist, i, n):
    largest = i

    left = (i << 1)
    right = (i << 1) + 1

    if left < n and alist[left] > alist[i]:
        largest = left
    else:
        largest = i

    if right < n and alist[right] > alist[largest]:
        largest = right

    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]
        #heapify(alist, largest, len(alist))
        heapify(alist, largest, n)


def buildheap(alist, n):
    for i in range(n / 2, -1, -1):
        heapify(alist, i, n)


def heapsort(alist):
    slist = []
    buildheap(alist, len(alist))

    for i in range(len(alist), 0, -1):
        slist.append(alist.pop(0))
        heapify(alist, 0, len(alist))

    return slist


def main():
    data = [2, 1, 5, 4, 10, 3]
    buildheap(data, len(data))
    print data

    sdata = heapsort(data)
    print sdata

if __name__ == '__main__':
    main()
