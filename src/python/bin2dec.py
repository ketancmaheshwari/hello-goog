#!/bin/env python

import sys

decnum = 0
binstring = sys.argv[1]
j = 1
for i in reversed(binstring):
    decnum = decnum + j * int(i)
    j = j * 2
print decnum
