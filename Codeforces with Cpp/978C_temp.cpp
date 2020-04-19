#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,m,i,j,b,temp=0,first,last,mid;
    scanf("%lld%lld",&n,&m);
    long long int a[n+1];

    a[0]=0;
    for(i=1;i<=n;i++)
    {
        scanf("%lld",&b);
        temp=temp+b;
        a[i]=temp;
    }

    for(i=0;i<m;i++)
    {
        scanf("%lld",&b);

        first=0;
        last=n;

        while(1)
        {
            mid=(first+last)/2;
            if(a[mid]==b)
            {
                printf("%lld %lld\n",mid,a[mid]);
                break;
            }
            else if(first==mid)
            {
                printf("%lld %lld\n",first+1,b-a[first]);
                break;
            }
            else if(a[mid]>b)
            {
                last=mid;
            }
            else if(a[mid]<b)
            {
                first=mid;
            }
        }
    }



 return 0;
}
