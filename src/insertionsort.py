#!/bin/env python

import numpy as np

#controls printing array corners
#np.set_printoptions(threshold='nan')

#insertion sort according to the Cormen book

# read file into a numpy array
data = np.loadtxt('../data/numlist10.txt')

print "unsorted data:", data

def insertionsort (data):
    for j in range(1, len(data)):
        key=data[j]
        i=j-1
        while i >= 0:
            if data[i] > key:
                data[i+1] = data[i]
                data[i] = key
                i = i - 1
            else:
                break

if __name__ == "__main__":
    insertionsort (data)
    print "sorted data:", data
