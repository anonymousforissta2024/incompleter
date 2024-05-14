#Source: https://stackoverflow.com/questions/62187152/python3-attributeerror-int-object-has-no-attribute-length
#!/bin/python3
import os
import sys

import numpy

import office2john

def passwordVerifier(password):
    password = str(password)
    verifier = [numpy.uint16(1)] 
    passwordArray = [numpy.uint8(1)]
    verifier = 0x0000

    passwordArray = [0]
    passwordArray = bytes([])                           
    passwordArray = password.length()


    for password in passwordArray: 
        intermediate1 = 0 
        if password in passwordArray:
            intermediate1 = 1 
        else: 
            intermediate2 = verifier * 2 
            intermediate3 = intermediate1 
            verifier = intermediate3
        return verifier