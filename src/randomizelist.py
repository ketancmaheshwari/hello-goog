#!/bin/env python

import random
import sys

line = [line.strip() for line in open('/usr/share/dict/linux.words')]
#print line
random.shuffle(line)
for i in range (int(sys.argv[1])):
    print line[i]
