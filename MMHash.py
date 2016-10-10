# Script Name	: MMHash.py
# Author		: Yardal Gedal
# Created		: 08 October 2016
# Last Modified	: 08 October 2016
# Version		: 1.0

# Modifications	: 1.0

# Description	: Hashing entered string 

class MMHash:
    def __init__(self, hashingstring='test'):
        self.hash = self.hashing(hashingstring)
    def hashing(self, hashingstring):
        a = ''
        c = ''
        for s, x in enumerate(hashingstring):
            a = a + str(self.__hashing_modify(str(x), int(s), hashingstring))
        while len(str(a)) <= 34:
            b = a
            for s, x in enumerate(b):
                c = c + str(self.__hashing_modify(str(x), int(s), b))
            a = a + c
        a = hex(int(a))
        if len(str(a)) > 34:
            a = a[2:34]
        return str(a[2:])
    def __list(n):
        return n[len(str(n))-1]
    def __hashing_modify(self, s, x, hashing_str):
        n = ord(s) * (x + 1) * len(hashing_str) * (ord(hashing_str[0])) * (ord(hashing_str[len(hashing_str) - 1]))
        return self.__list(str(n))
