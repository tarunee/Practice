class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        d={'0':"0",'1':"1", '2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        
        a=A[1:]
        if(len(A)==1):
            l = d[A[0]]
            s=[]
            for i in range(len(l)):
               s.append(l[i]) 
            return s
           
        l = self.letterCombinations(a)
        
        s = d[A[0]]
        ans = []
        for i in range(len(s)):
            for j in range(len(l)):
                ans.append(s[i]+l[j])
                
        return  ans
                
        
#Input: Digit string "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
