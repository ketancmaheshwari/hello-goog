#!/usr/bin/env python

def walkfiles(apath, apattern=None):
    for dir, dirlist, filelist in os.walk(apath):
        for fname in filelist:
            if apattern and not fnmatch.fnmatch(fname, apattern):
                continue
            yield os.path.join(dir, fname)

if __name__  ==  '__main__':
    import os
    import fnmatch
    ar = walkfiles('/home/kcm92/hello-goog', '*.txt')
    print ar
