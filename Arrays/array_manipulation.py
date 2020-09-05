#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    maxi = 0
    curr = 0 

    for a, b, k in queries:
        arr[a-1] += k
        if b != n:
            arr[b] -= k
    for i in range(n):
        curr += arr[i]
        if maxi < curr:
            maxi = curr

    return(maxi)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
