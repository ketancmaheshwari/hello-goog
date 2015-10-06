#!/bin/env python

# mainly for sys.argv[], sys.argv[0] is the name of the program
import sys
# mainly for arrays
import numpy as np

if __name__ == '__main__':
    fstring = 'First line: Name'
    sstring = 'Second line: Door no, Street'
    tstring = 'Third line: City, Pin code'
    splitted = fstring.split(':')

    print splitted[0] + "   :   " + splitted[1]
    print sstring.split(':')[0]
    print tstring
