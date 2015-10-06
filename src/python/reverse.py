#!/usr/bin/env python


def revrec(str):
    if len(str) < 2:
        return str

    return rev(str[1:]) + str[0]


def revitr(str):
    count = 1
    res = []
    for i in range(len(str)):

        res.append(str[len(str) - count])

        count += 1

    return ''.join(res)

if __name__ == '__main__':

    # rstr=revrec('ketan')
    rstr = revitr('ketan')

    print rstr
