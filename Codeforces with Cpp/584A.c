#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,t,i;
    scanf("%d%d",&n,&t);

    if(n==1 && t==10)
    {
    	printf("-1\n");
    }
    else if(t==10)
    {
    	printf("1");
    	for(i=0;i<n-1;i++)
    	{
    		printf("0");
    	}
    }
    else
    {
    	for(i=0;i<n;i++)
    	{
    		printf("%d",t);
    	}
    }

}