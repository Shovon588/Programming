#include<stdio.h>
int main()
{
    int a[3],i,temp,j,result;
    for(i=0;i<3;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
        if(a[i]>a[j])
        {
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    }
    }
   result=(a[0]-a[1])+(a[1]-a[2]);
   printf("%d",result);

    return 0;
}
