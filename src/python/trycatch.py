#!/usr/bin/env python

import math

def findroot(anum):
    """
    Find square root of a number
    """
    try:
        return math.sqrt(anum)
    except TypeError:
        return 'Not a number'

def main():
    """
    main method
    """
    print findroot('ana')

if __name__=='__main__':
    main()
