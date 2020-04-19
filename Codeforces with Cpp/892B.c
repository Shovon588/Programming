#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count=0,j;
    scanf("%d",&n);
   	long long int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%lld",&a[i]);
    }

    i=n;

    for(j=n-1;j>=0;j--)
    {
    	if(j<i)
    	{
    		count++;
    	}

    	if(j-a[j]<i)
    		{
    			i=j-a[j];
    		}
    }

    printf("%d\n",count );


}