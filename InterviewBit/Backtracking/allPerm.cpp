vector<vector<int> > Solution::permute(vector<int> &A) {
    
    int n = A.size();
    //sort(A,A+n);
    
    if(n==1)
    {
        vector<vector<int>> p;
        p.push_back(A);
        return p;
    }
    
    if(n==2)
    {
        vector<vector<int>> p;
        for(int i=0;i<2;i++)
        {
            vector<int> v;
            v.push_back(A[i]);
            v.push_back(A[1-i]);
           // cout<<"n=2 "<<A[i]<<A[1-i]<<endl;
            p.push_back(v);
        }
        
        return p;
    }
    
    vector<int> perm_next ;//n-1 vector
    for(int i=1;i<n;i++)
        perm_next.push_back(A[i]);
    
    vector<vector<int>> perm_now;
    
    vector<vector<int>> p = permute(perm_next);//gets perm of n-1
    
    for(int k=0;k<p.size();k++)
    {
        vector<int> t = p[k];
        
        for(int i=0;i<n;i++)
        {
            vector<int> v(n,0);
            v[i]=A[0];
            int k=0;
            for(int j=0;j<n;j++)
            {
                if(v[j]==0)
                {
                    v[j]=t[k++];
                }
                //cout<<" "<<v[j];
            }
            
            //cout<<endl;
            perm_now.push_back(v);
        
        }//creating n pos for each t vector
        
    }//get all perm of n-1
    
    return perm_now;
    
}
