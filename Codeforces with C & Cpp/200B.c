#include<stdio.h>
int main()
{
    int i,n;
    double sum=0.0,b,a;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%lf",&a);
        sum=sum+a;
    }
    b=sum/n;
    printf("%.09lf",b);


    return 0;
}
