import os
import sys
import math
import random

def ShowFunctionList():
    print("IsPrime(), Sqr(), HighestFactor(), IsPalindrome(), ReverseString()")

def IsPrime(x):
    i = 3
    if(x <= 1):
        return False
    else:
        if(x == 2):
            return True
        else:
            while(i < x):
                if(x % i == 0):
                    return False
                    i += 2
                else:
                    i += 2
            else:
                return True

def sqr(x):
    return (x * x)

def HighestFactor(x):
    hf = 0
    for i in range(1, x):
        if(x % i == 0):
            if(i > hf):
                hf = i
    return hf
 
def ReverseString(x):
      return str(x[::-1])

def IsPalindrome(x):
    x = str(x)
    reverse = str(x[::-1])
    if(x == reverse):
        return True
    else:
        return False
    
    
