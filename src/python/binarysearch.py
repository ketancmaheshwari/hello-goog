#!/bin/env python

# mainly for sys.argv[], sys.argv[0] is the name of the program
import sys
# mainly for arrays
import numpy as np


def bsearchrec(alist, item, imin, imax):
    if imin > imax:
        return
    else:
        imid = imin + ((imax - imin) / 2)
        if alist[imid] > item:
            return bsearchrec(alist, item, imin, imid - 1)
        elif alist[imid] < item:
            return bsearchrec(alist, item, imid + 1, imax)
        else:
            return imid


def bsearchiter(alist, item, imin, imax):
    while imax > imin:
        imid = imin + ((imax - imin) / 2)
        if item == alist[imid]:
            return imid
        elif item > alist[imid]:
            imin = imid + 1
        else:
            imax = imid - 1

    return

if __name__ == '__main__':
    a = [8, 5, 1, 2, 3, 4]

    #i=bsearchrec(sorted(a), 5, 0, len(a)-1)
    i = bsearchiter(sorted(a), 6, 0, len(a) - 1)
    try:
        if not i:
            print 'item not found'
        else:
            print i
    except ValueError:
        print 'item not found'
