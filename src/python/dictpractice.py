#!/usr/bin/env python

import random
import time

mydict = {}

# with open('t.txt') as f:
#    for line in f:
#        k, v = line.split()
#        mydict[int(k)] = v

# Load the contents of a file into a dictionary
for line in open('t.txt'):
    k, v = line.split()
    mydict[int(k)] = v
# print it
# print mydict

# add an element to dict
mydict[-999] = 'atestvalue'

print mydict.get(random.randint(1, 1000000))

# iteritems() iterkeys() itervalues()
# for key, value in mydict.iteritems():
#    print "The value %s is for key %d ..." % (value, key)

# popitem
print '3 popitem calls'
print mydict.popitem()
print mydict.popitem()
print mydict.popitem()

# print values
# print 'just print dict values via mydict.values()'
# print mydict.values()

# finally clear the dictionary
print 'Clean up the dictionary ...'
starttime = time.clock()
mydict.clear()
delta = time.clock() - starttime

print "it took %f seconds to clear a million items from mem" % delta
