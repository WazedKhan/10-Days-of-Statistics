import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    print(round(math.sqrt(sum([int((arr[i]-(sum(arr)/len(arr))))**2 for i in range(len(arr))])/len(arr)), 1)) #one line ans
    """
    n = 0
    mean = sum(arr)/len(arr)
    for i in range(len(arr)):
        n += (int((arr[i]-mean)**2))
    n = round(math.sqrt(n/len(arr)), 1)
    print(n)
    """
if __name__ == '__main__':
    n = 5 #int(input().strip())

    vals = list(map(int, '10 40 30 50 20'.rstrip().split()))

    stdDev(vals)