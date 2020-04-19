#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,x,i,temp=1,count=0;
    scanf("%d%d",&n,&x);
    int s,e;

    for(i=0;i<n;i++)
    {
        scanf("%d%d",&s,&e);
        while(temp+x<=s)
        {
            temp=temp+x;
        }
        count=count+(e-temp)+1;

        temp=e+1;
    }
    printf("%d",count);


    return 0;
}
