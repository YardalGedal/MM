# Script Name	: MMHash.py
# Author		: Yardal Gedal
# Created		: 08 October 2016
# Last Modified	: 22 October 2016
# Version		: 5.0.0

# Modifications	: 5.0.0

# Description	: Hashing entered string 

class MMHash:
    def __init__(self, hashingstring, hashsize=256):
        self.hashsize = hashsize
        self.__hashlen = (self.hashsize / 4) + 2 # Length of hash
        self.hash = self.__hashing(hashingstring)
    def __hashing(self, hashingstring):
        a = self.__exec_hashing_modify(hashingstring)
        while len(str(a)) < self.__hashlen:
            a = a + self.__exec_hashing_modify(a)
        return hex(int(a))[2:int(self.__hashlen)]
    def __exec_hashing_modify(self, hashingstring):
        a = ''
        for s, x in enumerate(hashingstring):
            a = a + str(self.__hashing_modify(str(x), int(s), len(hashingstring)))
        return a
    def __hashing_modify(self, s, x, len_of_hashingstring):
        n = ord(s) * (x + 1) * len_of_hashingstring * self.hashsize
        return n
