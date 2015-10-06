#!/usr/bin/env python

# Assume the left and right lists are sorted


def merge(left, right):
    result = list()
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # one of the left and right exhausted here
    result += left[i:]
    result += right[j:]
    return result


def mergesort(list):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)


def main():
    data = [int(data.strip()) for data in open('../../data/numlist10.txt')]
    sdata = mergesort(data)
    print sdata

if __name__ == '__main__':
    main()
