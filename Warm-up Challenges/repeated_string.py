#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    total = 0
    acount = s[:n].count('a')
    if (s == 'a'):
        return (n)

    if acount == 0:
        return (0)

    if n < len(s):
        return(acount)

    if n >= len(s):
        total = int(n/len(s)) * acount
        mod = n % len(s)
        if mod > 0:
            substr = s[:mod]
            total += substr.count('a')
    return (total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
