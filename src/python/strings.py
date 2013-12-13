#!/bin/env python


def hello_user(name):
    print 'Hello there '+ name

#call the routine you'd like to run as main
if __name__ == '__main__':
    import sys
    import numpy as np
    hello_user(str(sys.argv[1].split('t')))
    multilinestring = """This is a
                      multiline string"""
    print multilinestring

