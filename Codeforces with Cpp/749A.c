#include<stdio.h>
#include<string.h>
int main()
{
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

    int n;
    scanf("%d",&n);
    printf("%d\n",n/2 );

    while(n>3)
    {
    	printf("%d ",2 );
    	n=n-2;
    }
    printf("%d\n",n );

}