#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    long long int n,i,count=0,temp=0;
    scanf("%lld",&n);
    long long int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%lld",&a[i]);
    }

    sort(a,a+n);
    for(i=0;i<n;i++)
    {
        if(temp<=a[i])
        {
            count++;
            temp=temp+a[i];
        }
    }
    printf("%lld\n",count );

}

