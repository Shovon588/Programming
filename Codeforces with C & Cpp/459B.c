#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j;
    scanf("%d",&n);
    long long int a[n],maxdif,first=0,last=10000000000,countfirst=0,countlast=0;

    for(i=0;i<n;i++)
    {
    	scanf("%lld",&a[i]);

    	if(a[i]>first)
    	{
    		first=a[i];
    	}

    	if(a[i]<last)
    	{
    		last=a[i];
    	}
    }

    maxdif=first-last;

if(first!=last)
{
    for(i=0;i<n;i++)
    {
    	if(a[i]==first)
    	{
    		countfirst++;
    	}
    	else if (a[i]==last)
    	{
    		countlast++;
    	}
    }	
}
else
{
	for(i=0;i<n;i++)
    {
    	if(a[i]==first)
    	{
    		countfirst++;
    	}
    }

}


if(first==last && first!=1)
{
	printf("%lld %lld\n",maxdif,countfirst*(countfirst-1) );
}

else if(first==1)
{
	printf("%lld 1\n",maxdif );
}

else{
    if(countfirst==0)
    {
    	countfirst=1;
    }
    if(countlast==0)
    {
    	countlast=1;
    }

    printf("%lld %lld\n",maxdif,countfirst*countlast );
}

}