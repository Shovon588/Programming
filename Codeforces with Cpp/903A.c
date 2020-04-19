#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,a,i;
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a);
	
			if(a%3==0)
	    	{
	    		printf("YES\n");
	    	}
	    	else if(a%7==0)
	    	{
	    		printf("YES\n");
	    	}
	    	else if(a==10)
	    	{
	    		printf("YES\n");
	    	}
	    	else if(a>12)
	    	{
	    		printf("YES\n");
	    	}
	    	else
	    	{
	    		printf("NO\n");
	    	}
	    }
	}
