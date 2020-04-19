#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j,count,b=0;
    scanf("%d",&n);
    long long int a[n],temp;

    for(i=0;i<n;i++)
    {
    	scanf("%lld",&a[i]);
    }

    for(i=0;i<n;i++)
    {
    	count=0;
    	for(j=i+1;j<n;j++)
    	{
    		if(a[i]==a[j])
    		{
    			count++;
    		}
    	}
    	if(count>b)
    	{
    		b=count;
    	}
    }


    printf("%d\n",b+1 );


}