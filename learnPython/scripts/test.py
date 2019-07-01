#!/bin/python
#-*- coding: utf8 -*-

import os

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [word.lower() for word in L1 if type(word) == type("")]
print(L2)


import itertools

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def double_chuncker(iterable):
    extended = itertools.chain([0], iterable, [0])
    return pairwise(extended)


def pascal_next(iterable):
    return list(map(sum, double_chuncker(iterable)))


def pascal_triangle():
    row = [1]
    while True:
        yield row
        row = pascal_next(row)


def pascal_triangle_up_to(n):
    return list(itertools.islice(pascal_triangle(), n))


if __name__ == '__main__':
    # Testing
    for row in pascal_triangle():
        print(row, end='')
        if (input()):
            break
