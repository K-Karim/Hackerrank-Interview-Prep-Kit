#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    sortedarr = list(range(1,len(arr)+1))
    while arr != sortedarr:
        for i in range(len(arr)):
            if arr[i] != i+1:
                arr = swap(arr,i,arr[i]-1)
                swaps +=1
    return (swaps)

def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
