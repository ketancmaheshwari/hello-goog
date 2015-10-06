#!/usr/bin/env python


def create2dimlist(N):
    grid = []
    for outer in range(N):
        tmp = []
        for inner in range(N):
            tmp.append(1)

        grid.append(tmp)
    return grid

if __name__ == '__main__':
    print create2dimlist(3)
