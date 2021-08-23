import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def median(arr):
    if len(arr)%2 != 0:
        return(arr[len(arr)//2])
    else:
        mid = arr[(int(len(arr)/2)-1)] + arr[(int(len(arr)//2))]
        return(mid//2)

def quartiles(arr):
    # Write your code here
    print(median(arr[:len(arr)//2]))
    print(median(arr))
    arr.reverse()
    print(median(arr[:len(arr)//2]))

if __name__ == '__main__':
    #n = int(input().strip())
    data =sorted(list(map(int, '3 7 8 5 12 14 21 13 18'.rstrip().split())))
    res = quartiles(data)