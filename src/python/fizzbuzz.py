#!/bin/env python

import sys

def fizzbuzz():
    for i in xrange(10):
        if i % 3 == 0:
            print 'fizz'
        else:
            print 'buzz'


if __name__=='__main__':
    print 'hello'
    fizzbuzz()
