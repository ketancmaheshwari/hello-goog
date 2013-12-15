#!/usr/bin/env python

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)        

    def display(self):
        return self.items

if __name__ == '__main__':
    myq = Queue()
    myq.enqueue(100)
    myq.enqueue('hello')
    myq.enqueue(200)
    myq.enqueue(300)
    myq.enqueue('hi')

    #print myq.size()

    print myq.dequeue()
    myq.enqueue(300)
    print myq.dequeue()

    print myq.display()
