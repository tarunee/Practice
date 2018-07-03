//backtracking here somewhat
int Solution::Mod(int A, int B, int C) {
    long long int ans;
    
    if(A==0)//if given number = 0
    {
        ans=0;
    }
    else if(B==0)//power =0
    {
        ans= 1;
    }
    else if(B%2==0)
    {
        long long int y = Mod(A,B/2,C);
        ans = (y*y)%C;
    }
    else{
        long long int x = Mod(A,B-1,C) ;
        ans = ((A%C)*x)%C;
    }
    
    if(ans>=0)//negative mod
        return ans;
    else
        return ans + C;
}
