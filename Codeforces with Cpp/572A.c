#include <bits/stdc++.h>
using  namespace std;
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int A,B,i,k,m,temp,count=0;
    scanf("%lld%lld",&A,&B);
    long long int a[A],b[B];
    scanf("%lld%lld",&k,&m);

    for(i=0;i<A;i++)
    {
        scanf("%lld",&a[i]);
    }
    temp=a[k-1];


    for(i=0;i<B;i++)
    {
        scanf("%lld",&b[i]);
    }

    for(i=B-1;i>=0;i--)
    {
        if(b[i]<=temp || count>m)
        {
            break;
        }
        else
        {
            count++;
        }
    }

    if(count>=m)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

}

