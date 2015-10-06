#!/usr/bin/env python


def hist(aword):
    d = {}
    for c in aword:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    #sorted(d, key=d.get)
    return d


def main():
    print hist('hello world')

if __name__ == "__main__":
    main()
