#!/bin/python3

import os
import sys

# Complete the howManyGoodSubarrays function below.
def howManyGoodSubarrays(A, m, k):
    # Return the number of good subarrays of A.
    n=len(A)
    c=0
    for i in range(n):
        p=1
        for j in range(i,n):
            p=p*A[j]
            if(p%m == k):
                c=c+1
                
    return c
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nmk = input().split()

        n = int(nmk[0])

        m = int(nmk[1])

        k = int(nmk[2])

        A = list(map(int, input().rstrip().split()))

        result = howManyGoodSubarrays(A, m, k)

        fptr.write(str(result) + '\n')

    fptr.close()
