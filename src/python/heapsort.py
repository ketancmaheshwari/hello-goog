#!/usr/bin/env python

def heapsort(list):
    for item in list:
        print item
    #TODO: heapsort
    return list
def main():
    data = [int(data.strip()) for data in open('../../data/numlist10.txt')]
    sdata = heapsort(data)

    print sdata

if __name__=='__main__':
    main()
