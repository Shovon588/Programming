#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int a,b,i,j,k,m,temp,count=0;

    scanf("%lld%lld",&a,&b);

    long long int a1[a],a2[b];

    scanf("%lld%lld",&k,&m);

    for(i=0;i<a;i++)
    {
        scanf("%lld",&a1[i]);
    }

    for(i=0;i<b;i++)
    {
        scanf("%lld",&a2[i]);
    }

    temp=a1[k-1];

    for(i=0;i<b;i++)
    {
        if(a2[i]>temp)
        {
            count++;
        }

        if(count>=m)
        {
            break;
        }
    }

    if(count>=m)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }


    return 0;
}
