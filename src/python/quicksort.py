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
            #print "splitter: %d, end: %d, array[splitter]: %d, array[end]: %d" % (splitter, end, array[splitter], array[end])
            if splitter != end:
                array[splitter],array[end]=array[end],array[splitter]
    
    array[splitter+1], array[upper] = array[upper], array[splitter+1]
    #print array
    return splitter+1

def quicksort2(array):
    lo = []
    up = []

    if len(array) < 2:
        return array
    pivot = array.pop(0)
    for x in array:
        if x <= pivot:
            lo.append(x)
        else:
            up.append(x)

    return quicksort2(lo) + [pivot] + quicksort2(up)

def main():
    data = [9,5,7,10,12,18,21,6,15]
    print data
    quicksort(data, 0, len(data)-1)
    print data
    dsorted = quicksort2(data)

    print dsorted

if __name__=='__main__':
    main()
