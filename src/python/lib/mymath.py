#!/usr/bin/env python

import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('A debug message')
logging.info('An info message')
logging.warning('A warning message')

def fact(n):

    logging.info('Invoke fact')
    logging.warning('Invoke fact '+str(n))
    if n==0:
        return 1
    else:
        return fact(n-1)*n

if __name__=='__main__':
    print "Hello from main"
