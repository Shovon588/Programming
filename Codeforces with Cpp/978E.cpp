#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,w,i,max=0,min=1000000000,a,total=0;

    scanf("%d%d",&n,&w);

    for(i=0;i<n;i++)
    {
        scanf("%d",&a);
        total=total+a;

        if(total>max)
        {
            max=total;
        }
        if(total<min)
        {
            min=total;
        }
    }

    if(w-max+1+min>0)
    {
        printf("%d",w-max+1+min);
    }
    else
    {
        printf("0\n");
    }

    return 0;
}
