class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A=sorted(A)
        l=[]
        n=len(A)
        if(n==0):
            l.append([])
            return l
        if(n==1):
            l.append([])
            l.append(A)
            return l
        p=1
        if(A[0]==A[1]):
            while(p+1<n and A[p]==A[p+1]):
                p = p+1 #subsets after removing dups for this num
            p=p+1
        else:
            p=1 #subset A-1 if no dups
        
        B=[]
        for i in range(p,n):
            B.append(A[i])
            
        #print(A,B)
        
        fin = self.subsetsWithDup(B)
        
        if p>1:#case with dups
            dup = []
            for i in range(p):
                a = [A[0] for j in range(i+1)]
                dup.append(a)
            #print("d",dup)
            #print("f",fin)
            
            if(len(fin)==1):
                dup.insert(0,[])
                return dup
            
            #because 33 should come before 35
            #but dup has 3 , 33 so reverse dup
            dup.reverse()
            
            for i in range(len(dup)):
                k=dup[i]
                for j in range(1,len(fin)):
                    l.append(k+fin[j])
            
            #actual order is 3, 33 so append it in front at the end
            dup.reverse()   
            l=dup+l
                    
            #print("l",l)
            
        else:#case with no dups
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
        
        #if in doubt check case 6 6 6 3 3 6 5
        
