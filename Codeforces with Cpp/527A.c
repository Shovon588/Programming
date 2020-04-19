#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int a,b,count=0,x,y;
    scanf("%lld%lld",&a,&b);

    while(a!=0 && b!=0)
    {
    	if(a==b)
    	{
    		count=count+1;
    		a=0;b=0;
    	}
    	else if(a>b)
    	{
    		if(a%b==0)
    		{
    			count=count+(a/b);
    			a=0;b=0;
    		}
    		else
    		{
    			x=a/b;
    			a=a-(x*b);
    			count=count+x;
    		}
    	}
    	else if(b>a)
    	{ 
    		if(b%a==0)
    		{
    			count=count+(b/a);
    			a=0;
    			b=0;
    		}
    		else
    		{
    			x=b/a;
    			b=b-(x*a);
    			count=count+x;
    		}
    	}
    }

    printf("%lld\n",count );


}