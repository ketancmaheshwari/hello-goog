#!/usr/bin/env python


class Fraction():

    def __init__(self, up, down):
        self.num = up
        self.den = down

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def rationalize(self):
        return float(self.num) / self.den

if __name__ == '__main__':
    f = Fraction(3, 4)

    print f

    print f.rationalize()
