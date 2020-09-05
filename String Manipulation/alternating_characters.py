#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0
    if s.count("A") == len(s) or s.count("B") == len(s):
        return (len(s) - 1)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            deletions +=1
            s = s[:i] + s[i+1:]
        else:
            i += 1
    return (deletions)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
