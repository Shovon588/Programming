#include<stdio.h>
int main()
{
    int a,b,same;
    scanf("%d%d",&a,&b);
    if(a>b)
    {
        same=(a-b)/2;
        printf("%d %d",b,same);
    }
    else if(b>a)
    {
        same=(b-a)/2;
        printf("%d %d",a,same);
    }
    else
    {
        printf("%d 0",a);
    }


    return 0;
}
