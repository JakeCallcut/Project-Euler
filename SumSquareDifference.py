
import os
import sys
import math

#Problem 4, Project Euler, Sum Square Difference

#!Square of sum
num = 0
total = 0

for num in range (1, 100):
    total = total + num
else:
    squaretotal = total * total
    print(squaretotal)

num = 0
total = 0


#!Sum of Square

for num in range (1,100):
    squarenum = num * num
    total = total + squarenum
else:
    print(total)

print(total - squaretotal)