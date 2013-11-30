#!/bin/env python

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys

#mainly for arrays
import numpy as np

#ToDo: use traditional logic
def palindrome (name):
    return name == name[::-1]


if __name__=='__main__':
    #call the routine you'd like to run as main
    if palindrome (sys.argv[1]):
        print sys.argv[1] + " is a palindrome"
    else:
        print sys.argv[1] + " is not a palindrome"
