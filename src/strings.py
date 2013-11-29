#!/bin/env python

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys

#mainly for arrays
import numpy as np

def hello (name):
    print 'Hello there '+ name

#call the routine you'd like to run as main
if __name__=='__main__':
    #hello (str(sys.argv[1].split('t')))
    multilinestring="""This is a
   multiline string"""
    print multilinestring

