#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,a[10000]={0},c=1,count=0,b;
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    	scanf("%d",&b);

    	a[b]++;

    	if(a[b]==1)
    	{
    		count++;
    	}

    	if(a[b]>c)
    	{
    		c=a[b];
    	}

    }

    printf("%d %d\n",c,count );


}