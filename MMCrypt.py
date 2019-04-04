import string
import random

from math import e

class MMCrypt:
    def __init__(self, salt: (int, float) = e, accuracy: int = 1):
        self.salt = salt
        self.accuracy = accuracy # bigger is better
        self.symbols = tuple(set(string.punctuation) - {'.'})

    def crypt(self, s: str):
        rsymbols = [random.choice(self.symbols) for _ in range(len(s))]
        
        return "".join(str(round(ord(i) * self.__salt(rsymbols), self.accuracy)) + j for i, j in zip(s, rsymbols))
    
    def encrypt(self, s: str):
        rsymbols = tuple(filter(lambda el: el in self.symbols, s))

        l = "".join(' ' if i in self.symbols else i for i in s).split(' ')

        return "".join(chr(round(float(i) / self.__salt(rsymbols))) 
                       for i in l if i)
    
    def __salt(self, rsymbols):
        return self.salt + self.__rsymbols_salt(rsymbols)
        
    def __rsymbols_salt(self, rsymbols):
        return sum(map(ord, rsymbols)) / len(rsymbols)
        
