#!/usr/bin/env python

from collections import deque

myd = deque()
myd.append(1)
myd.append(2)
myd.append(3)
myd.append(4)
print myd
myd.rotate()
print myd
myd.rotate(2)
print myd
myd.extendleft([3])
myd.extend([9])
print myd
myd.append(99)
print myd
myd.appendleft(-99)
print myd
