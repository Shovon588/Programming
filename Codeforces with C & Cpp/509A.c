#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,j;
    scanf("%d",&n);
    int a[n][n];

    for(i=0;i<n;i++)
    {
    	a[0][i]=1;
    }

    for(i=0;i<n;i++)
    {
    	a[i][0]=1;
    }

    for(i=1;i<n;i++)
    {
    	for(j=1;j<n;j++)
    	{
    		a[i][j]=a[i-1][j]+a[i][j-1];
    	}
    }

     printf("%d\n",a[n-1][n-1] );
}