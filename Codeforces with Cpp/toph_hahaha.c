#include<stdio.h>
int main()
{
    int n,a,b,c,i;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        scanf("%d%d",&a,&b);
        c=(a*a)+(b*b);
        printf("Case %d: %d\n",i,c);
    }


    return 0;
}
