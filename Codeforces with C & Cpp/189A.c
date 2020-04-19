#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,a,b,c,count=0,max,min,mid,temp;
    scanf("%d%d%d%d",&n,&a,&b,&c);

    if(a>=b && a>=c)
    {
    	max=a;
    	if(b>c)
    	{
    		mid=b;
    		min=c;
    	}
    	else
    	{
    		mid=c;
    		min=b;
    	}
    }
    else if(b>=a && b>=c)
    {
    	max=b;
    	if(a>c)
    	{
    		mid=a;
    		min=c;
    	}
    	else
    	{
    		mid=c;
    		min=a;
    	}
    }
    else if(c>=b && c>=a)
    {
    	max=c;
    	if(b>a)
    	{
    		mid=b;
    		min=a;
    	}
    	else
    	{
    		mid=a;
    		min=b;
    	}
    }


    if(n%min==0)
    {
    	count=count+(n/min);
    	n=0;
    }
    else
    {
    	while((n-min)%mid || (n-min)%max)
    	{
    		n=n-min;
    		count++;
    	}
    }

    if(n%mid==0)
    {
    	count=count+(n/mid);
    	n=0;
    }
    else
    {
    	while((n-mid)==max || (n-mid)==min)
    	{
    		n=n-mid;
    		count++;
    	}
    }

    if(n%max==0 || n%mid==0 || n%min==0)
    {
    	count=count+(n/max);
    	n=0;
    }

    printf("%d\n",count );



}