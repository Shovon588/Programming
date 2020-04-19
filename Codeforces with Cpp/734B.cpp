#include<bits/stdc++.h>
using namespace std;
int main()
{
    int k2,k3,k5,k6,min,count=0;
    scanf("%d%d%d%d",&k2,&k3,&k5,&k6);

    if(k2<=k5 && k2<=k6)
    {
        min=k2;
    }
    else if(k5<=k2 && k5<=k6)
    {
        min=k5;
    }
    else if(k6<=k2 && k6<=k5)
    {
        min=k6;
    }
    count=count+(min*256);
    k2=k2-min;

    if(k2<=k3)
    {
        count=count+(k2*32);
    }
    else
    {
        count=count+(k3*32);
    }

    printf("%d",count);

    return 0;
}
