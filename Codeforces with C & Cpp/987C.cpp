#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,i,j,k;
    scanf("%d",&n);
    long long int a[n],b[n],c[n]={0};
    for (i=0;i<n;i++)
    {
        scanf("%lld",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        scanf("%lld",&b[i]);
    }

    for(i=0;i<n;i++)
    {
        printf("%lld\n",c[i]);
    }


    return 0;
}
