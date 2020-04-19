#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif


    int a[5],i,sum=0;
    for(i=0;i<5;i++)
    {
        scanf("%d",&a[i]);
        sum=sum+a[i];
    }

    if(sum==0)
    {
        printf("-1\n");
    }

    else if(sum%5==0)
    {
        printf("%d\n",sum/5 );
    }
    else
    {
        printf("-1\n");
    }

}