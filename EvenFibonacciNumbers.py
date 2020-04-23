
import os
import math
import sys

#Problem 2, Project Euler, Even Fibonacci Numbers 

total = 0
nextnumber = 0
number = 2
prevnumber = 1

while(number < 4000000):

    if (number % 2 == 0):
        total = total + number
        nextnumber = prevnumber + number
        prevnumber = number
        number = nextnumber
        
    else:
        nextnumber = prevnumber + number
        prevnumber = number
        number = nextnumber

print(total)
input()