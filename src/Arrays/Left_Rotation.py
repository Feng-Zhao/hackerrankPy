#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    print(a)
    print(a[d-len(a):d])
    return a[d-len(a):d]

if __name__ == '__main__':
    a = [1,3,4,5,6]
    d = 3

    result = rotLeft(a, d)

    print(result)
