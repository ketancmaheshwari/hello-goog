#!/usr/bin/env python

data = [(1,2,3),(3,4,5),(89,98,78)]

prices = [54.3]
navs = {}
for (portfolio, equity, position) in data:
    navs.setdefault(portfolio, 0)
    #navs[portfolio] += position * prices[0]
print navs
