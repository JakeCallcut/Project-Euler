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
 
#def ReverseString(str):
#    newstr = ""
#    for i in range (len(str), 0)):
#        newstr = newstr + str[]
#    else:
#        print(newstr)

def IsPalindrome(x):
    x = str(x)

    if (len(x) % 2 == 0):
        #if(x[0:len(x)/2] = )
    #else:
        pass