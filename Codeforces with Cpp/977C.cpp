#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,k,i;
    scanf("%lld%lld",&n,&k);
    long long int a[n];

    for(i=0;i<n;i++)
    {
        scanf("%lld",&a[i]);
    }

    sort(a,a+n);


    if(a[k]==a[k-1])
    {
        printf("-1");
    }
    else if(k==0 && a[0]==1)
    {
        printf("-1");
    }
    else if(k==0 && a[0]!=0)
    {
        printf("%lld",a[0]-1);
    }
    else
    {
        printf("%lld",a[k-1]);
    }



    return 0;
}
