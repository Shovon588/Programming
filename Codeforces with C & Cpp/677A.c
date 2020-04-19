#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,h,i,a,count=0;

    scanf("%d%d",&n,&h);
    for(i=0;i<n;i++)
    {
    	scanf("%d",&a);

    	if(a>h)
    	{
    		count=count+2;
    	}
    	else
    	{
    		count++;
    	}
    }

    printf("%d\n",count);

}