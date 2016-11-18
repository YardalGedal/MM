# Script Name	: MMHash.py
# Author		: Yardal Gedal
# Created		: 08 October 2016
# Last Modified	: 18 November 2016
# Version		: 7.0.0

# Modifications	: 7.0.0

# Description	: Hashing entered string 

class MMHash:
    def __init__(self, hashingstring, hashsize=256):
        self.hashsize = hashsize
        self.x = int(hashsize / 16)
        self.__hashlen = (self.hashsize / 4) + self.x # Length of hash
        self.hash = self.__hashing(hashingstring)
    def __hashing(self, hashingstring):
        a = self.__exec_hashing_modify(hashingstring)
        while len(str(a)) < self.__hashlen + self.x:
            a = a + self.__exec_hashing_modify(a)
        a = hex(int(a))[self.x:int(self.__hashlen)]
        return a[::-1]
    def __exec_hashing_modify(self, hashingstring):
        a = ''
        for s, x in enumerate(hashingstring):
            a = a + str(self.__hashing_modify(str(x), int(s), len(hashingstring)))
        return a
    def __hashing_modify(self, s, x, len_of_hashingstring):
        n = ord(s) * (x + 1) * len_of_hashingstring * self.hashsize
        return n
