#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int a,b,total,tempa,tempb,mid,restmid,i,count=0;
    scanf("%d%d",&a,&b);


    if(a>b)
    {
    	tempa=a;
    	tempb=b;
    }
    else
    {
    	tempa=b;
    	tempb=a;
    }

    total=tempa-tempb;

    mid=total/2;

    restmid=total-mid;


    for(i=1;i<=mid;i++)
    {
    	count=count+i;
    }

    for(i=1;i<=restmid;i++)
    {
    	count=count+i;
    }


    printf("%d\n",count );

}