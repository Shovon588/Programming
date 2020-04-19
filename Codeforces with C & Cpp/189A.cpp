#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,a,b,c,min,mid,max;

    scanf("%d%d%d%d",&n,&a,&b,&c);

    if(a>=b && a>=c)
    {
        max=a;
        if(b>=c)
        {
            mid=b;
            min=c;
        }
        else
        {
            mid=c;
            min=b;
        }
    }
    else if(b>=a && b>=c)
    {
        max=b;
        if(a>=c)
        {
            mid=a;
            min=c;
        }
        else
        {
            mid=c;
            min=a;
        }
    }
    else if(c>=a && c>=b)
    {
        max=c;
        if(a>=b)
        {
            mid=a;
            min=b;
        }
        else
        {
            mid=b;
            min=a;
        }
    }

    int count=0;
    while(n!=0)
    {
        if(n-min==0)
        {
            n=n-min;
            count++;
        }
        else if(n-min>=mid || n-min>=max)
        {
            n=n-min;
            count++;
        }
        else if(n-mid==0)
        {
            n=n-mid;
            count++;
        }
        else if(n-mid>=max)
        {
            n=n-mid;
            count++;
        }
        else if(n-max==0)
        {
            n=n-max;
            count++;
        }
        else if(n-max>=max)
        {
            n=n-max;
            count++;
        }

        printf("%d--%d\n",n,count);
    }

   printf("count=%d",count);


    return 0;
}
