import os
import sys
import math
import random
import AdvancedMath

#Problem 10, Project Euler, Summation of Primes
#Find the sum of all the primes below two million.

count = 3
noofprimes = 2
sumofprimes = 2
number = 1000000

while(count < number - 1):
    if (AdvancedMath.IsPrime(count)):
        noofprimes += 1
        sumofprimes += count
    else:
        pass
    count += 2
else:
    print(sumofprimes)
    print(count)
    print(noofprimes)
