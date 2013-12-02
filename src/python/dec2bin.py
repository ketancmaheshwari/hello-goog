#!/bin/env python

import sys

#still buggy

binum=""

decnum=int(sys.argv[1])
print decnum
while decnum > 0:
    binum=binum + str(decnum % 2)
    decnum = decnum / 2

print binum[::-1]
