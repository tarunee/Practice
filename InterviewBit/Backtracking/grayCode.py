class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        
        if A==1:
            l=[0,1]
            return l
            
        l = self.grayCode(A-1)
        l_rev = []
        for i in range(len(l)):
            l_rev.insert(0,l[i])
            
        n = pow(2,A-1)
        for i in range(len(l)):
            l.append(l_rev[i]+n)
            
        return l
#The gray code is a binary numeral system where two successive values differ in only one bit.
#if A=2 return [00,01,11,10] ie [0,1,3,2]
