class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        
        if B==1:
            t=[]
            for i in range(1,A):
               t.append([i]) 
            return t
            
        t = self.combine(A,B-1)
        ans = []
        for i in range(len(t)):
            p = t[i]
            q = p[len(p)-1]
            for i in range(q+1,A):
                s = p + [i]
                ans.append(s)
                
        return ans
'''     
check for case n=4,k=1 clue
n=4 ,k=2
[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
'''
