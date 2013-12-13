#!/usr/bin/env python

alist = [(4, 5), (3, 2), (2, 1), (6, 7)]
print alist

# Decorate:
to_sort = [(item[1], item) for item in alist]
print to_sort

# Sort:
to_sort.sort()
print to_sort

# Undecorate:
alist = [item[-1] for item in to_sort]
print alist
