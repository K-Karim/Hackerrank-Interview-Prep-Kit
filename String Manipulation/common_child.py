#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    prev = [0] * (len(s1) + 1)
    curr = [0] * (len(s1) + 1)
    for c1 in s1:
        curr, prev = prev, curr
        for j, c2 in enumerate(s2, 1):
            curr[j] = (
                1 + prev[j - 1] if c1 == c2 else
                max(prev[j], curr[j - 1])
            )
    return curr[-1]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
