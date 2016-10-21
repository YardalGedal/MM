# Script Name	: MMHash.py
# Author		: Yardal Gedal
# Created		: 08 October 2016
# Last Modified	: 22 October 2016
# Version		: 5.0.0

# Modifications	: 5.0.0

# Description	: Hashing entered string 

class MMHash:
    def __init__(self, hashingstring='test'):
        self.hash = self.hashing(hashingstring)
    def hashing(self, hashingstring):
        a = ''
        c = ''
        for s, x in enumerate(hashingstring):
            a = a + str(self.__hashing_modify(str(x), int(s), hashingstring))
        while len(str(a)) <= 66:
            b = a
            for s, x in enumerate(b):
                c = c + str(self.__hashing_modify(str(x), int(s), b))
            a = a + c
        a = hex(int(a))
        return str(a[2:66])
    def __hashing_modify(self, s, x, hashing_str):
        n = ord(s) * (x + 1) * len(hashing_str)
        return n
