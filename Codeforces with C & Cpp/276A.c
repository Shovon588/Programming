#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,k,i,f,t;
    scanf("%lld%lld",&n,&k);
    long long int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%lld%lld",&f,&t);

        if(t>k)
        {
            a[i]=f-(t-k);
        }
        else
        {
            a[i]=f;
        }
    }
    sort(a,a+n);
    printf("%lld\n",a[n-1] );
    

}

