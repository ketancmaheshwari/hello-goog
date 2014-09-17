#!/usr/bin/env python

import re
import sys

pattern="\d{4,9}"
regexp=re.compile(pattern,re.I) #ignore case

def main():

    for line in sys.stdin:
        result = regexp.search(line)
        
        if result:
            print line

if __name__=="__main__":
    main()

