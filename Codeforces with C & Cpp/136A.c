#include<stdio.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n,i,temp;
    scanf("%d",&n);
    int a[n],b[n];

    for(i=1;i<=n;i++)
    {
    	scanf("%d",&a[i]);
    }

    for (i=1;i<=n;i++)
    {
    	temp=a[i];
    	b[temp]=i;
    }
    printf("%d",b[1] );

    for(i=2;i<=n;i++)
    {
    	printf(" %d",b[i] );
    }

  

}