#!/usr/bin/env python


class astack(object):

    def __init__(self):
        self.container = []

    def size(self):
        return len(self.container)

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop(0)

    def display(self):
        print self.container


if __name__ == '__main__':
    mystack = astack()

    mystack.push(100)
    mystack.push(200)

    mystack.display()

    mystack.pop()
    mystack.display()
