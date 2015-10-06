#!/bin/env python

import numpy as np

# controls printing array corners
# np.set_printoptions(threshold='nan')

zero = np.zeros(10)
one = np.ones(20)

print zero
print one

# read file into a numpy array
data = np.loadtxt('../data/strlist10k.txt', dtype='string')

print data
