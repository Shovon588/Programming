#include<bits/stdc++.h>
using namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    long long int n,m,i,result;
    
    scanf("%lld%lld",&n,&m);
    long long int a[n],b[m];
    
    for(i=0;i<n;i++)
    {
        scanf("%lld",&a[i]);
    }
    
    for(i=0;i<m;i++)
    {
        scanf("%lld",&b[i]);
    }
    
    sort(a,a+n);
    
    sort(b,b+m);
    
    result=a[n-2]*b[m-1];
    
    printf("%lld",result);



    return 0;

    


}