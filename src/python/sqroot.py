#!/usr/bin/env python

# mainly for sys.argv[], sys.argv[0] is the name of the program
import sys


def sqroot(anum):
    """
    Compute square root of a number via Newton's method
    Newton's method is to approximate z = Sqrt(x) by picking a starting point z and then repeating:
    z = z - (z*z - x)/(2*z)
    """
    try:
        initguess = anum / 2.
        epsilon = 0.000001
        diff = initguess
        newres = 0

        while diff > epsilon:
            newres = initguess - (initguess**2 - anum) / (2. * initguess)
            diff = abs(newres - initguess)
            initguess = newres
    except ZeroDivisionError:
        print 'oops, divided by zero!'
    else:
        return initguess, newres


if __name__ == '__main__':
    init, new = sqroot(float(sys.argv[1]))
    print new
