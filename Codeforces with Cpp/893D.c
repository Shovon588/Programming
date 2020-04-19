#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    long long int n,d,bal=0;
    scanf("%lld%lld",&n,&d);
    int a[n],i,count=0,br;

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for(i=0;i<n;i++)
    {
    	bal=bal+a[i];
    	if(bal>d)
    	{
    		br=1;
    		break;
    	}
    	else if(a[i]==0)
    	{
    		if(bal<0)
    		{
    			count++;
    		}
    	}
    }

    if(br==1)
    {
    	printf("-1\n");
    }
    else
    {
    	printf("%d\n",count );
    }




}