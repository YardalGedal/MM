# Script Name : MMCrypt.py
# Author : Yardal Gedal
# Created : 09 October 2017
# Last Modified	: 09 October 2017
# Version : 1.0.0

# Modifications	: 1.0.0

# Description : Crypt/encrupy input string

class MMCrypt:
    def __init__(self):
        self.salt = 1/e
        self.accuracy = 1 # more - better, only int
        
    def crypt(self, data):
        return ",".join([str(round(ord(i)*self.salt, self.accuracy)) for i in data])
    
    def encrypt(self, data):
        return "".join([chr(round(float(i)/self.salt)) for i in data.split(',')])
