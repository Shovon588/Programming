#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,count=1,temp=0;
    scanf("%d",&n);
    int a[n];


    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for(i=0;i<n-1;i++)
    {
    	if(a[i]<=a[i+1])
    	{
    		count++;
    		if(temp<count)
    		{
    			temp=count;
    		}
    	}
    	else
    	{
    		count=1;
    	}

    }

if(n==1 || temp==0)
{
	printf("1\n");
}
else
{
	printf("%d\n",temp );
}



}