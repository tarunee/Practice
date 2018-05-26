
#https://www.hackerrank.com/contests/world-codesprint-13/challenges/watsons-love-for-arrays/copy-from/1307783262
#!/bin/python3

import os
import sys

# Complete the howManyGoodSubarrays function below.
def howManyGoodSubarrays(A, m, k):
    # Return the number of good subarrays of A.
    n=len(A)
    dp = [[0]*n for i in range(n)]
    c=0
    
    for i in range(n):
        dp[i][i]=A[i]
        if(dp[i][i]%m == k):
            c=c+1
    
    
    for j in range(1,n):
        for i in range(n):
            if(i+j<n):
                dp[i][i+j]=dp[i][i+j-1]*A[i+j]
                if(dp[i][i+j]%m == k):
                    c=c+1

    #for i in range(n):
        #print(dp[i])
    
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
