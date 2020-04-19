#include<stdio.h>
int main()
{
    int n,k,i,a,b,count=0,result;
    scanf("%d%d",&n,&k);
    b=5-k;
    for(i=0;i<n;i++)
    {
        scanf("%d",&a);
        if(a<=b)
        {
            count++;
        }
    }
    result=count/3;
    printf("%d",result);



    return 0;
}
