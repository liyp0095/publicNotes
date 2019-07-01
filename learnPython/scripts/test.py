#!/bin/python
#-*- coding: utf8 -*-

import os

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [word.lower() for word in L1 if type(word) == type("")]
print(L2)


def pascal_triangle(max):
    n, a, b = 0, [], []
    while n < max:
        yield b
        a = b
        b = []
