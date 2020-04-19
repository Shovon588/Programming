#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,temp;
    scanf("%d",&n);
    int a[n];

    for(i=0;i<n;i++)
    {
    	scanf("%d",&a[i]);
    }

    temp=a[n-2]-a[n-1];

    if(a[n-1]==15)
    {
    	printf("DOWN\n");
    }
    else if(a[n-1]==0)
    {
    	printf("UP\n");
    }
    else if(temp==1)
    {
    	printf("DOWN\n");
    }
    else if(temp==-1)
    {
    	printf("UP\n");
    }
    else
    {
    	printf("-1\n");
    }


}