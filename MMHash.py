# Script Name : MMHash.py
# Author : Yardal Gedal
# Created : 08 October 2016
# Last Modified	: 18 November 2016
# Version : 8.0.0

# Modifications	: 8.0.0

# Description : Hashing entered string

from functools import reduce

class MMHash:
    def __init__(self, S):
        x = 256
        L = (x // 8) * 2
        f = lambda ords: str(hex(reduce(lambda x, y: int(x)*int(y),  ords) + int("".join(ords))))
        while len(S) < L:
            S = f([str((n + x) * x) + str(ord(i)) for n, i in enumerate(S)])
        return S[-L//2:]
