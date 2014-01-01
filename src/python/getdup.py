#!/usr/bin/env python

def getduplines(etcfile):
    ulist = {}
    with open(etcfile) as f:
        for aline in f:
            seprec=aline.split(':')
            if seprec[0] not in ulist:
                ulist[seprec[0]] = seprec[1]
            else:
                ulist[seprec[0]] += ',' + seprec[1]

    return ulist

def main():
   print  getduplines('/etc/passwd')

if __name__ == '__main__':
    main()
