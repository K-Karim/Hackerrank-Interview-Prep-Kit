#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numswaps = 0
    while sorted(a) != a:
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                numswaps += 1
        
    print("Array is sorted in {} swaps.".format(numswaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
