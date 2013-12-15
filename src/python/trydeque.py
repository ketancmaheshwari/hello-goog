#!/usr/bin/env python

class Deque(object):
    """
    Implements a deque
    """
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def addfront(self, item):
        self.items.append(item)

    def addrear(self, item):
        self.items.insert(0, item)
    
    def removefront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def main():
    myd = Deque()

    myd.addfront(10)
    myd.addrear(20)
    myd.addrear(20)

    print myd.removerear()
    print myd.removefront()

if __name__ == "__main__":
    main()
