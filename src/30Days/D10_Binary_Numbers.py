#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    strb = bin(n)

    count = 0
    max_c = 0
    for c in strb:
        if c == '1':
            count += 1
            if count > max_c:
                max_c = count
        else:
            count = 0
    print(max_c)