#!/bin/env python

# mainly for sys.argv[], sys.argv[0] is the name of the program
import sys


def makebold(fn):
    def wrapped(a):
        return "<b>" + fn(a) + "</b>"
    return wrapped


def makeitalic(fn):
    def wrapped(b):
        return "<i>" + fn(b) + "</i>"
    return wrapped


@makebold
@makeitalic
def hello(a):
    return "hello world! " + a

if __name__ == "__main__":
    print hello("ketan")
