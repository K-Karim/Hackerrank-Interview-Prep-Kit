#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    freq = {}
    if len(s) <= 2:
        return("YES")
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    minl = min(freq.values())
    maxl = max(freq.values())
    lfreq = len(freq)
    if (list(freq.values()).count(minl) == lfreq):
        return("YES")
    elif list(freq.values()).count(minl) == 1 and lfreq -1 == list(freq.values()).count(maxl):
        return("YES")
    elif (list(freq.values()).count(minl) == (lfreq - 1)) and (maxl -1) == minl:
        return("YES")
    else:
        return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()