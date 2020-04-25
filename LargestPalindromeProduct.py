import os
import sys
import math
import random
import AdvancedMath
from AdvancedMath import IsPalindrome

num1 = 999
num2 = 999
highest = 0
found = False
while (found == False):
    while (num1 > 0):
        if (IsPalindrome(num1 * num2) == True):
            if(num1 * num2 > highest):
                highest = num1 * num2
            else:
                pass
        else:
            pass
    num1 -= 1
    else: 
else:
    pass
