#!/usr/bin/env python

def heapsort(list):
    #TODO: heapsort
    print "Do heapsort"

def main():
    data = [int(data.strip()) for data in open('../../data/numlist10.txt')]
    sdata = mergesort(data)
    print sdata

if __name__=='__main__':
    main()
