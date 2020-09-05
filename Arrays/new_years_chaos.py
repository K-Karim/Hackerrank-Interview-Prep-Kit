#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for end, start in enumerate(q):
        if end + 1 < start - 2: 
            print("Too chaotic")
            return
        infront = range(max(start - 2, 0), end)
        for p in infront:
            if q[p] > start:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
