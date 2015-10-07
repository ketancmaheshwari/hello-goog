#!/usr/bin/env python

import random
import time
import string
import subprocess

#create t.txt
tfile = open("t.txt", "w")
n=100000

for i in xrange(n):
    tfile.write(str(random.randint(1,1000))+" "+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))+"\n")

tfile.close()

mydict = {}

# with open('t.txt') as f:
#    for line in f:
#        k, v = line.split()
#        mydict[int(k)] = v

# Load the contents of a file into a dictionary
for line in open('t.txt'):
    k, v = line.split()
    mydict[int(k)] = v

print mydict.get(random.randint(1, n))

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

print "It took %f seconds to clear %d items from mem" % (delta, n)

print "Deleting tfile"

subprocess.call(["rm", "t.txt"])
