#include<stdio.h>
int main()
{
    int a=1,b=1,i=1,result;

    for(i=0;i<20;i++)
    {
        result=a+b;
        printf("%d\n",result);
        b=a;
        a=result;
    }



    return 0;
}
