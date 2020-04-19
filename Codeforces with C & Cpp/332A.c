#include<stdio.h>
int main()
{
    int a,b,result,count,i,temp;
    scanf("%d%d",&a,&b);

    if(a%10==0 || a%10==b)
    {
        result=1;
        printf("%d",result);
    }
    else
    {
        count=0;
        for(i=1;i<=10;i++)
        {
            temp=a*i;
            count++;
            if(temp%10==b || temp%10==0)
            {
                printf("%d",count);
                break;
            }
        }
    }

    return 0;
}
