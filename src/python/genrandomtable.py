#!/bin/env python

import sys
import random
import string

lines = [lines.strip() for lines in open('/usr/share/dict/linux.words')]

for i in range (int(sys.argv[1])):
    #print '%i %d %f' % i, random.randint(1,1000000), random.random() 
    print "{} {} {} {} {}".format(i, random.choice(lines), random.randint(1,1000000), random.random(), random.choice(string.ascii_lowercase))

