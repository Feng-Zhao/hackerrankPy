#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    res = 0
    briber = 0
    lastBriber = 0
    for i in range(0,len(q)):
        if (q[i] - 1 - i + (briber if q[i] < lastBriber else 0)) > 2:
            return "Too chaotic"
        elif (q[i] - 1 - i + (briber if q[i] < lastBriber else 0)) > 0:
            res += q[i] - 1 - i + (briber if q[i] < lastBriber else 0)
            briber += 1
            lastBriber = q[i]
    return res

if __name__ == '__main__':
    # t = int(input())


    # n = 5
    # q = [5,[2,1,5,3,4],5,[2,5,1,3,4]]
    q = [1,2,5,3,7,8,6,4]

    print(minimumBribes(q))
