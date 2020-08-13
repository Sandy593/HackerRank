# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:37:36 2020

@author: Soundarya.Rupavatara
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here

    x = range(1, n+1)

    for y in x:
        if y % 3 == 0 and y % 5 == 0:
            print('FizzBuzz')
        elif y % 3 == 0:
            print('Fizz')
        elif y % 5 == 0:
            print('Buzz')
        else:
            print(y)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
