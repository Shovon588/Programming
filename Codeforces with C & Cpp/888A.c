#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for(i=1;i<n-1;i++)
    {
    	if(a[i]>a[i-1] && a[i]>a[i+1])
    	{
    		count++;
    	}
    	else if(a[i]<a[i-1] && a[i]<a[i+1])
    	{
    		count++;
    	}
    }

    printf("%d\n",count );





}