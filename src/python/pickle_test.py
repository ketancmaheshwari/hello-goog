#!/bin/env python

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys
import pickle

#mainly for arrays
import numpy as np

def d (name, outfile):
    pickle.dump(name, outfile)

if __name__=='__main__':
    #call the routine you'd like to run as main
    d (sys.argv[1], open('hello.txt', 'w'))
