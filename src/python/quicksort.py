#!/usr/bin/env python

def quicksort(array, lower, upper):
    if lower >= upper:
        return

    pivot_pos=partition(array, lower, upper)
    quicksort(array, lower, pivot_pos - 1)

    quicksort(array, pivot_pos + 1, upper)

def partition(array, lower, upper):
    pivot=array[upper] # why it does not work when pivot is lower?
    splitter=lower - 1
    
    for end in xrange(lower, upper):
        if array[end] <= pivot:
            splitter = splitter + 1
            array[splitter],array[end]=array[end],array[splitter]
    
    array[splitter+1], array[upper] = array[upper], array[splitter+1]
    return splitter+1

def main():
    data = [7,1,5,9,2]
    quicksort(data, 0, len(data)-1)
    print data

if __name__=='__main__':
    main()
