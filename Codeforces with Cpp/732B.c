#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,k,i,sum=0;
    scanf("%d%d",&n,&k);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for(i=1;i<n;i++)
    {
    	if(a[i]+a[i-1]<k)
    	{
    		sum=sum+k-a[i-1]-a[i];
    		a[i]=k-a[i-1];
    	}
    }

    printf("%d\n%d",sum,a[0] );
    for(i=1;i<n;i++)
    {
    	printf(" %d",a[i] );
    }
    
}