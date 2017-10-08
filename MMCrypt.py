# Script Name : MMCrypt.py
# Author : Yardal Gedal
# Created : 09 October 2017
# Last Modified	: 09 October 2017
# Version : 1.0.0

# Modifications	: 1.0.0

# Description : Crypt/encrupy input string

from math import e

class MMCrypt:
    
    def __init__(self):
        self.SALT = 1/e
        self.ACCURACY = 1 # bigger is better, only integer
        
    def crypt(self, DATA):
        return ",".join([str(round(ord(i)*self.SALT, self.ACCURACY)) for i in DATA])
    
    def encrypt(self, data):
        return "".join([chr(round(float(i)/self.SALT)) for i in DATA.split(',')])
