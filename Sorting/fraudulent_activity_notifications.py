#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    counter = 0
    meds = [0] * 201
    med = float()
    l_iter = 0

    for i in range(d):
        meds[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        med = median(meds, d)
        if med * 2 <= expenditure[i]:
            counter += 1
        meds[expenditure[l_iter]] -= 1
        meds[expenditure[i]] +=1
        l_iter += 1
    return(counter)


def median(meds, d):
    counter = 0
    left, right = -1, -1
    if d % 2 == 1:
        for i, v in enumerate(meds):
            counter += v
            if counter > ((d//2)):
                return i
    else:
        for i, v in enumerate(meds):
            counter += v
            if counter == (d//2):
                left = i
                right = i+1
                return (left+right) / 2
            if counter > (d//2):
                return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
