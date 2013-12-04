#!/bin/env python

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys

#mainly for arrays
import numpy as np

def erato (data):
   print "implement eratosthenes sieve" 

if __name__=='__main__':
    #call the routine you'd like to run as main
    data = np.loadtxt("../../data/numlist100.txt")
    erato ()
