#!/usr/bin/env python

def bad_append(new_item, a_list=[]):
    a_list.append(new_item)
    return a_list

def good_append(new_item, alist=None):
    if alist is None:
        alist = []
    alist.append(new_item)

    return alist

def main():
    mylist = [43, 23, 18, 90]
    print bad_append(34, mylist)
    print  good_append(34)

if __name__ == '__main__':
    main()
