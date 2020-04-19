#include<stdio.h>
int main()
{
    int a,b,n,i,temp;
    scanf("%d%d%d",&a,&b,&n);

    temp=gcd(a,b);



    for(i=1;i<105;i++)
    {
        if(i%2!=0)
        {
            temp=gcd(a,n);

            if(temp>n || temp==0)
            {
                break;
            }
            else
            {
                n=n-temp;
            }
        }
        else
        {
            temp=gcd(b,n);

            if(temp>n || temp==0)
            {
                break;
            }
            else
            {
                n=n-temp;
            }
        }

    }

    if(i%2==0)
    {
        printf("0");
    }
    else
    {
        printf("1");
    }
    return 0;
}

int gcd(int x, int y)
{
    if(y==0)
    {
        return y;
    }
    else
    {
        while(x!=y)
        {
            if(x>y)
            {
                x-=y;
            }
            else
            {
                y-=x;
            }
        }
        return x;
    }
}
