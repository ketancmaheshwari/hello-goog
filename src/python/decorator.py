#!/bin/env python

# mainly for sys.argv[], sys.argv[0] is the name of the program
import sys
from functools import wraps


def makebold(fn):
    @wraps(fn)
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world!"

if __name__ == '__main__':
    print hello()
