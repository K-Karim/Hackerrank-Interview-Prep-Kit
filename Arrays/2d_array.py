#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxi = 0
    curr = 0
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            curr = (sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]))
            if (i == 0) and (j == 0):
                maxi = curr
            maxi = max(maxi, curr)

    return(maxi)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
