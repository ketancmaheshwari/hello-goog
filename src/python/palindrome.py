#!/bin/env python

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys

#mainly for arrays
import numpy as np

#ToDo: use traditional logic
def palindrome (name):
    flag=True
    #find length of string
    slen = len(name)
    i=0
    j=slen-1
    while i<=j:
        if name[i]!=name[j]:
            flag=False
        i=i+1
        j=j-1

    return flag


if __name__=='__main__':
    #call the routine you'd like to run as main
    if palindrome (sys.argv[1]):
        print sys.argv[1] + " is a palindrome"
    else:
        print sys.argv[1] + " is not a palindrome"
