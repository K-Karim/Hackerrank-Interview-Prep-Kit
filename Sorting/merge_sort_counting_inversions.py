#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    larr = len(arr)
    if larr < 2:
        return 0
    llarr = larr // 2
    rlarr = larr - llarr
    left = arr[:llarr]
    right = arr[llarr:]
    count = countInversions(left) + countInversions(right)
    j, k = 0, 0
    for i in range(larr):
        if llarr > j and (rlarr <= k or left[j] <= right[k]):
            arr[i] = left[j]
            count += k
            j += 1
        elif k < rlarr:
            arr[i] = right[k]
            k += 1
    return (count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
