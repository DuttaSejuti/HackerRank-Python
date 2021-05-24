#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_pos=0
    count_neg=0
    count_zero=0
    for i in range(n):
        if(arr[i]>0):
            count_pos=count_pos+1
        if(arr[i]<0):
            count_neg=count_neg+1
        if(arr[i]==0):
            count_zero=count_zero+1
    print('{:.6f}'.format(count_pos/n))
    print('{:.6f}'.format(count_neg/n))
    print('{:.6f}'.format(count_zero/n))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
