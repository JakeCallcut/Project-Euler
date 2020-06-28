import os
import sys
import math

#problem 4, Project Euler, Largest Palindrome Product

def Reverse(stri):
    newString = ""
    for i in range (stri.Length, 0):
       newString = newString + (stri[i-1 : i])
    else:
        return newString

def IsPalindrome(Strin):
    reversedString = Reverse(Strin)
    if (reversedString == Strin):
        return True
    else:
        return False

print(IsPalindrome("abba"))
print(IsPalindrome("jake"))
print(Reverse("jake"))
print(True)