#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = sorted(a)
    b = sorted(b)
    same = 0
    counter = len(a) + len(b)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                same += 2
                del(b[j])
                break
            else:
                continue 
    return (counter-same)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()