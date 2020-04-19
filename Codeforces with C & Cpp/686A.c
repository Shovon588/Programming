#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,x,i,count=0,a;

    scanf("%lld%lld",&n,&x);
    char c,b;

    for(i=0;i<n;i++)
    {
    	scanf(" %c %lld",&c,&a);

    	if(c=='+')
    	{
    		x=x+a;
    	}
    	else
    	{
    		if(x>=a)
    		{
    			x=x-a;
    		}
    		else
    		{
    			count++;
    		}
    	}
    }
    
    printf("%lld %lld\n",x,count );



	return 0;
}