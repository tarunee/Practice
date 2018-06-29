vector<int> Solution::primesum(int A) {
    
    //used seive of erasthannese
    int n=pow(A,0.5);
    vector<bool> prime;
    //array gave seg fault
    //int vect gave mem exceeded
    //vect bool is perfect
    vector<int> ans;
    for(int i=0;i<=A;i++)
        prime.push_back(1);
        
    prime[0]=0;
    prime[1]=0;
    
    //outer loop till sq n as smallest factor other comes as multiple
    for(int i=2;i<=n;i++)
    {
        if(prime[i]==1){
            for(int j=2;i*j<=A;j++)
            {
                prime[i*j]=0;
            }
        }
    }//routine gets all primes <n
    
    //for(int i=0;i<=A;i++)
      //  cout<<prime[i]<<" ";
    
    for(int i=2;i<=A;i++)
    {
        if(prime[i]==1)
        {
            if(prime[A-i]==1)
            {
                ans.push_back(i);
                ans.push_back(A-i);
                break;
            }
        }
    }
    
    return ans;
}
