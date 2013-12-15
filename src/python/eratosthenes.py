#!/bin/env python


#ToDo
def erato (bound):
    """
    compute primes by Eratosthenes algorithm
    """

    primecandidates = [True] * bound
    primecandidates[0] = primecandidates[1] = False
    
    for p in xrange(2, len(primecandidates)):
        if primecandidates[p]:
            yield p
        for x in xrange(p*p, bound, p):
            primecandidates[x] = False


if __name__ == '__main__':
    #call the routine you'd like to run as main
   print list(erato(10000))
