#!/bin/env python

#TODO: #Demonstrate classes and objects

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys

#mainly for arrays
import numpy as np

def hello (name):
    print 'Hello there '+ name

if __name__=='__main__':
    #call the routine you'd like to run as main
    hello (sys.argv[1])
