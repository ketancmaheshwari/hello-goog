#!/bin/env python

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys

#mainly for arrays
import numpy as np

def simplerec (num):
    print num
    if num == 0:
        return 
    simplerec(num - 1)

def recursive(a, num):
    print a
    print num
    recursive(a, num+1)
    if num > 100:
        return

if __name__=='__main__':
    #call the routine you'd like to run as main
    simplerec (int(sys.argv[1]))
    recursive("hello recursion", 0)
