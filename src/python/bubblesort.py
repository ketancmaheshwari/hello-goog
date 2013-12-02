#!/bin/env python

import numpy as np

#controls printing array corners
#np.set_printoptions(threshold='nan')

#insertion sort according to the Cormen book

# read file into a numpy array
data = np.loadtxt('../data/numlist10.txt')

print "unsorted data:", data

def bubblesort (data):
    sorted=False
    length=len(data) - 1

    while not sorted:
        sorted=True
        for i in range(length):
            if data [i] > data [i+1]:
                sorted=False
                data[i],data[i+1]=data[i+1],data[i]

if __name__ == "__main__":
    bubblesort (data)
    print "sorted data:", data
