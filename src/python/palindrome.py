#!/bin/env python

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys

#mainly for arrays
import numpy as np

#ToDo: use traditional logic
def palindrome (name):
    #find length of string
    slen = len(name)

    #find middle
    if slen % 2 == 0: # even
        middle=slen/2
    else:             # odd
        middle=slen/2 + 1

    #return name == name[::-1]
    return middle


if __name__=='__main__':
    #call the routine you'd like to run as main
    print palindrome (sys.argv[1])
