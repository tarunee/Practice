class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort() #inplace sorting
        l=[]
        n=len(A)
        if(n==0):
            l.append([])
            return l
        if(n==1):
            l.append([])
            l.append(A)
            return l
        
        B=[]
        for i in range(1,n):
            B.append(A[i])
        
        fin = self.subsets(B)
        
        for i in range(len(fin)):
            k=[A[0]]+fin[i]
            l.append(k)
            
        if(A[0]<fin[1][0]):
            for i in range(len(l)):
                fin.insert(i+1,l[i])
        else:
            for i in range(len(l)):
                fin.append(l[i]);
        
        return fin
        
        
        
