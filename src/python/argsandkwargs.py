#!/bin/env python

# mainly for sys.argv[], sys.argv[0] is the name of the program
import sys

# mainly for arrays
import numpy as np


def print_args(*args):
    for i, item in enumerate(args):
        print '{}:{}'.format(i, item)


def print_kwargs(**kwargs):
    for name, value in kwargs.items():
        print '{}:{}'.format(name, value)

if __name__ == '__main__':
    # call the routine you'd like to run as main
    print_args('apple', 'mango', 'banana')
    print_kwargs(fruit='apple', vegetable='potato')
