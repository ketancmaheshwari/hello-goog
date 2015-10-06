#!/usr/bin/env python

# mainly for sys.argv[], sys.argv[0] is the name of the program
import sys
import cPickle as pickle


def dopickle(name, outfile):
    pickle.dump(name, outfile)

if __name__ == '__main__':
    # call the routine you'd like to run as main
    dopickle(sys.argv[1], open('hello.txt', 'w'))
