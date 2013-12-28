#!/bin/env python

#TODO: #Demonstrate classes and objects

#mainly for sys.argv[], sys.argv[0] is the name of the program
import sys
#mainly for arrays
import numpy as np

class Account(object):
    def __init__(self, name, initbalance, curbalance):
        self.name=name
        self.initbalance=initbalance
        self.curbalance=curbalance

    def enquiry(self):
        return self.curbalance

    def deposit(self, amt):
        self.curbalance += amt
    
    def withdraw(self, amt):
        if self.curbalance >= amt:
            self.curbalance -= amt
        else:
            print 'insufficient funds'


def hello (name):
    print 'Hello there '+ name

if __name__=='__main__':
    #call the routine you'd like to run as main
    #hello (sys.argv[1])
    ketan=Account('Ketan', 100, 100)
    ketan.deposit(2000)
    print ketan.enquiry()
    ketan.withdraw(1200)
    print ketan.enquiry()
    ketan.withdraw(200)

